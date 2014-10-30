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
SmallRun = False

PrintEvents = False
check_events = []
#check_events.append('1-287-187567')

print "loading files ..."

chain = TChain('*/FlatTuple')

listOfFiles = []

#listOfFiles.append('./HOLDER/TTEmbedMuTauFlatTuple_10_1_wuj.root')


##################
## embedded ttbar
##################
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedETau_V7FlatTupleEx/FlatTuple_10_1_u9P.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedETau_V7FlatTupleEx/FlatTuple_11_1_BLX.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedETau_V7FlatTupleEx/FlatTuple_12_1_ovK.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedETau_V7FlatTupleEx/FlatTuple_13_1_deR.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedETau_V7FlatTupleEx/FlatTuple_14_1_DUm.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedETau_V7FlatTupleEx/FlatTuple_15_1_kJ0.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedETau_V7FlatTupleEx/FlatTuple_16_1_OeR.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedETau_V7FlatTupleEx/FlatTuple_1_1_CgF.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedETau_V7FlatTupleEx/FlatTuple_2_1_W5W.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedETau_V7FlatTupleEx/FlatTuple_3_1_rb1.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedETau_V7FlatTupleEx/FlatTuple_4_1_DnI.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedETau_V7FlatTupleEx/FlatTuple_5_1_3EL.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedETau_V7FlatTupleEx/FlatTuple_6_1_pW7.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedETau_V7FlatTupleEx/FlatTuple_7_1_Er7.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedETau_V7FlatTupleEx/FlatTuple_8_1_Ze1.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedETau_V7FlatTupleEx/FlatTuple_9_1_Gdd.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedMuTau_V7FlatTupleEx/FlatTuple_10_1_wuj.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedMuTau_V7FlatTupleEx/FlatTuple_11_1_NQk.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedMuTau_V7FlatTupleEx/FlatTuple_12_1_Gm9.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedMuTau_V7FlatTupleEx/FlatTuple_13_1_13w.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedMuTau_V7FlatTupleEx/FlatTuple_14_1_HUf.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedMuTau_V7FlatTupleEx/FlatTuple_15_1_LAe.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedMuTau_V7FlatTupleEx/FlatTuple_16_1_PHT.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedMuTau_V7FlatTupleEx/FlatTuple_1_1_AUs.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedMuTau_V7FlatTupleEx/FlatTuple_2_1_20w.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedMuTau_V7FlatTupleEx/FlatTuple_3_1_UFn.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedMuTau_V7FlatTupleEx/FlatTuple_4_1_pfR.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedMuTau_V7FlatTupleEx/FlatTuple_5_1_yZM.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedMuTau_V7FlatTupleEx/FlatTuple_6_1_BuK.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedMuTau_V7FlatTupleEx/FlatTuple_7_1_XCZ.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedMuTau_V7FlatTupleEx/FlatTuple_8_1_jv0.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/ttEMBED/TtBarEmbeddedMuTau_V7FlatTupleEx/FlatTuple_9_1_nzV.root')


for afile in listOfFiles:
	chain.AddFile(afile,0,'TauEsNominal/FlatTuple')
	chain.AddFile(afile,0,'TauEsUp/FlatTuple')
	chain.AddFile(afile,0,'TauEsDown/FlatTuple')


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

print 'getting n events'

maxEntries = chain.GetEntries()



print 'starting loop ...'

if SmallRun is True:
	maxEntries = 15000

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
				if passesEmbeddedTTbarSelectionETau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				if passesEmbeddedTTbarSelectionMuTau(chain,index,UseNewTriggers,Verbose) is False:
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
				SAMPLE_ADD = getSAMPLE_ADD(sampleName)
				assert(len(SAMPLE_ADD)>0), " Assert : unknown sample "

				if SAMPLE_ADD == '_embeddedTTbar_':
					# since will subtract from embedded ZTT fill the ZTT histograms :
					classification = '_ZTT_'
					wt = getWeightEmbeddedTTbar(chain,maxPairTypeAndIndex,Verbose)
					Fill_ZTTembedded(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])


######################
# save filled histograms

WriteEverything()
writeCompFile()
