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


listOfFiles.append('./HOLDER/DYTauPolOff.root')
listOfFiles.append('./HOLDER/DYTauPolOff2.root')

###########
# DY



listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_6_1_Jtt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_4_1_qvF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_10_1_C0Y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_17_1_BLT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_11_1_IWL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_13_1_lm4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_23_1_MhF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_16_1_Tdx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_18_1_x7K_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_20_1_kGp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_22_1_yeu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_25_1_q1R_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_27_1_05a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_28_1_agm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_7_1_NJr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_26_1_4LR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_12_1_ctf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_21_1_LRh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_19_1_Db2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_1_1_txh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_3_1_L8L_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_14_1_Siv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_2_1_fuj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_15_1_0SO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_8_1_AZl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_5_1_c7x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_9_1_FGV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_24_1_YUp_skimmed.root')


for afile in listOfFiles:
	chain.AddFile(afile,0,'TauEsNominal/FlatTuple')
	#chain.AddFile(afile,0,'TauEsUp/FlatTuple')
	#chain.AddFile(afile,0,'TauEsDown/FlatTuple')


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
				if passesDefaultSelectionETau_NoMtCut(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				if passesDefaultSelectionMuTau_NoMtCut(chain,index,UseNewTriggers,Verbose) is False:
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
				if SAMPLE_ADD == '_DYTauPolOff_':
					classification = classifyZDecay_Final(chain,maxPairTypeAndIndex)
					print classification
					wt = 1.0
					if classification == '_ZTT_':
						wt = getWeightForTauPolOffDY_NOSTITCH_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					elif classification == '_ZL_':
						wt = getWeightForTauPolOffDY_NOSTITCH_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose)
						# contains an internal check for e->tau
						wt = wt * getFakeZeeWeight(chain,maxPairTypeAndIndex)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					elif classification == '_ZJ_':
						wt = getWeightForTauPolOffDY_NOSTITCH_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])





######################
# save filled histograms

WriteEverything()
writeCompFile()
