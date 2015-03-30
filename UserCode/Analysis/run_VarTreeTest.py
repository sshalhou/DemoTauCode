import time
import sys
import os



from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TApplication,TTreeCache


################
# some global settings

UseNewTriggers = False
OnlyCheckEmbeddedTriggers = False

Verbose = False
SmallRun = True

PrintEvents = False
check_events = []
#check_events.append('1-287-187567')

print "loading files ..."

chain = TChain('*/FlatTuple')

listOfFiles = []


##############
# import file lists
from InputFlatFiles.python.FlatFileLists import *

###########
# DY


listOfFiles += testList


###############
for f in range(0,len(listOfFiles)):
	print 'adding ', listOfFiles[f]



for afile in listOfFiles:
	chain.AddFile(afile,0,'TauEsNominal/FlatTuple')
	# chain.AddFile(afile,0,'TauEsUp/FlatTuple')
	# chain.AddFile(afile,0,'TauEsDown/FlatTuple')


print "finished loading ttrees (es nominal only) from files ..."


theselector = "./scripts/FlatTreeSel.C+"
selector = TSelector.GetSelector(theselector)

chain.SetNotify(selector)
selector.Init(chain)
selector.Begin(chain)

####################################################################
# read in electronID, muonID, tauID, trigger, and event selections

from Configurations.python.electronID import *
from Configurations.python.muonID import *
from Configurations.python.tauID import *
from Configurations.python.triggerRequirements import *
from Configurations.python.eventRequirements import *
from Configurations.python.eventClassification import *
from Plotting.python.EventVariables import *
from Plotting.python.DataCardHistograms import *
from EventWeights.python.eventWeightFunctions import *
from Plotting.python.ComparisonPlots import *
from Configurations.python.SampleSpecificSelections import *
from Plotting.python.FillHistogramsBySample import *
from Configurations.python.makeNNtrainingTree import *
from Plotting.python.VarTree import *


print 'initialize NN training tree'
nnVARS_DICT = {}
nnTree = InitTreeAndFile(nnVARS_DICT)


######### varTree -- start 1
print 'initialize varTree tree'
varTree_DICT = {}
varTree = var_InitTreeAndFile(varTree_DICT)
######### varTree -- end 2


print 'getting n events'

maxEntries = chain.GetEntries()



print 'starting loop ...'

if SmallRun is True:
	maxEntries = 50

for entry in range(0,maxEntries):
		entryNumber = chain.GetEntryNumber(entry);
		localEntry = chain.LoadTree(entryNumber);
		if (localEntry >= 0):
			#print "NAMEVAR = ", chain.NAMEVAR
			if(entryNumber%1000==0):
				print 'processing entry ',entryNumber, 'of', maxEntries
				sys.stdout.flush()
			selector.Process(localEntry)
			passingETauIndices = []
			passingMuTauIndices = []
			maxPairTypeAndIndex = []

			#########################################################
			# get event ID

			eventID = [str(chain.run), str(chain.luminosityBlock), str(chain.event)]
			eventString = str(chain.run)+"-"+str(chain.luminosityBlock)+"-"+str(chain.event)
			sampleName =  str(chain.SampleName)



#########################################################
# loop over eTau pairs and store all that pass in list

			for index in range(0, chain.eT_correctedSVFitMass.size()):
				passesCuts = True
				#if passesDefaultSelectionETau(chain,index,UseNewTriggers,Verbose) is False:
				#	passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				#if passesDefaultSelectionMuTau(chain,index,UseNewTriggers,Verbose) is False:
				#	passesCuts = False
				if passesCuts is True:
					passingMuTauIndices.append(index)



#########################################################
# if have multiple passing H candidates in the same event
# find the highest sumPt pair


			if (len(passingETauIndices) + len(passingMuTauIndices)) == 1:
				if len(passingETauIndices) == 1 :
					maxPairTypeAndIndex.append(passingETauIndices[0])
					maxPairTypeAndIndex.append('eleTau')
				elif len(passingMuTauIndices) == 1:
					maxPairTypeAndIndex.append(passingMuTauIndices[0])
					maxPairTypeAndIndex.append('muTau')
			if (len(passingETauIndices) + len(passingMuTauIndices)) > 1:
					getMaxPtPairIndex(chain, maxPairTypeAndIndex, passingMuTauIndices, passingETauIndices)

#########################################################
# now classify the event based on tauPt and nbtags

			if len(maxPairTypeAndIndex)	> 0:
				if maxPairTypeAndIndex[1] == 'muTau':
					maxPairTypeAndIndex.append(muTauClassification(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(chain.NAMEVAR)
					#maxPairTypeAndIndex.append(muTauClassificationJECDOWN(chain, maxPairTypeAndIndex[0]))
					#maxPairTypeAndIndex.append(muTauClassificationJECUP(chain, maxPairTypeAndIndex[0]))
				if maxPairTypeAndIndex[1] == 'eleTau':
					maxPairTypeAndIndex.append(eTauClassification(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(chain.NAMEVAR)
					#maxPairTypeAndIndex.append(eTauClassificationJECDOWN(chain, maxPairTypeAndIndex[0]))
					#maxPairTypeAndIndex.append(eTauClassificationJECUP(chain, maxPairTypeAndIndex[0]))
				if PrintEvents:
					print maxPairTypeAndIndex[1], maxPairTypeAndIndex[2],eventID[0]+"-"+eventID[1]+"-"+eventID[2]

##################################################################################
# get weights and fill histograms


			if len(maxPairTypeAndIndex)	> 0:
				if SetVariableValues(nnVARS_DICT,chain,maxPairTypeAndIndex) is True:
					fillTree(nnTree, nnVARS_DICT)

				######### varTree -- start 2
				TREE_WEIGHT = 1.0	
				fill_varTree(chain,varTree,getSAMPLE_ADD(sampleName), maxPairTypeAndIndex, varTree_DICT, TREE_WEIGHT,channel_String,sampleType_String,tauEs_String)		
				######### varTree -- end 2



######################
# save filled tree

WriteTree(nnTree)
######### varTree -- start 3
var_WriteTree(varTree)
######### varTree -- end 3

#WriteEverything()
#writeCompFile()
