import time
import sys
import os

############
# due to 3 crashing events
# impose the following SF
# bbSUSY900 GEV (997674-2217)/997674.0 = 9.97777831235453716e-01
# ggHSUSY 250 GeV (1000441-2223)/1000441.0 = 9.97777979910859258e-01
# ggHSUSY 900 GeV (975744-2168.)/975744 = 9.97778105732651133e-01

from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TApplication,TTreeCache


################
# some global settings

UseNewTriggers = False
OnlyCheckEmbeddedTriggers = False

Verbose = False
SmallRun = False

PrintEvents = False
check_events = []
#check_events.append('1-287-187567')




chain = TChain('*/FlatTuple')

listOfFiles = []
#listOfFiles.append('./HOLDER/FlatTuple_SZS_SUSYBBHToTauTauM80_v5ntup.root')

listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM1000_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM100_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM110_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM120_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM130_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM140_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM160_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM180_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM200_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM250_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM300_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM350_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM400_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM450_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM500_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM600_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM700_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM800_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM80_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM900_v5ntup.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_SUSYBBHToTauTauM90_v5ntup.root')

for afile in listOfFiles:
	chain.AddFile(afile,0,'TauEsNominal/FlatTuple')
	chain.AddFile(afile,0,'TauEsUp/FlatTuple')
	chain.AddFile(afile,0,'TauEsDown/FlatTuple')




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


maxEntries = chain.GetEntries()


if SmallRun is True:
	maxEntries = 1000

for entry in range(0,maxEntries):
		entryNumber = chain.GetEntryNumber(entry);
		localEntry = chain.LoadTree(entryNumber);
		if (localEntry >= 0):
			#print "NAMEVAR = ", chain.NAMEVAR
			if(entryNumber%1000==0):
				print 'processing entry ',entryNumber, 'of', maxEntries
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
				if passesDefaultSelectionETau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesSUSYBBExtraSelectionETau(chain,index) is False:
					passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				if passesDefaultSelectionMuTau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesSUSYBBExtraSelectionMuTau(chain,index) is False:
					passesCuts = False
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
					maxPairTypeAndIndex.append(muTauClassificationJECDOWN(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(muTauClassificationJECUP(chain, maxPairTypeAndIndex[0]))
				if maxPairTypeAndIndex[1] == 'eleTau':
					maxPairTypeAndIndex.append(eTauClassification(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(chain.NAMEVAR)
					maxPairTypeAndIndex.append(eTauClassificationJECDOWN(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(eTauClassificationJECUP(chain, maxPairTypeAndIndex[0]))
				if PrintEvents:
					print maxPairTypeAndIndex[1], maxPairTypeAndIndex[2],eventID[0]+"-"+eventID[1]+"-"+eventID[2]

##################################################################################
# get weights and fill histograms


			if len(maxPairTypeAndIndex)	> 0:
				eventVariables = {}
				fillVariables(chain,eventVariables,maxPairTypeAndIndex,Verbose)
				finalWt = signalSUSYweightBB(chain, maxPairTypeAndIndex, Verbose)
				highPtTauWtSYS =  highPtTauSYS(chain, maxPairTypeAndIndex)
				SAMPLE_ADD = getSAMPLE_ADD(sampleName)
				assert(len(SAMPLE_ADD)>0), " Assert : unknown sample "
				#print maxPairTypeAndIndex
				FillSUSYBB(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,highPtTauWtSYS,histogram_dict,eventVariables['SVFitMass'])


######################
# save filled histograms

WriteEverything()
writeCompFile()