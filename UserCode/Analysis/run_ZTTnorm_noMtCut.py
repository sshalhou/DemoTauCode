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



###########
# DY

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_10_1_MxF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_11_1_Qnk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_12_1_O6A_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_13_1_QGG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_14_1_vsN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_15_1_tSI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_16_1_4X4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_17_1_rkv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_18_1_FcL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_19_1_D8A_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_1_1_Scv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_20_1_HSD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_21_1_sQw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_22_1_4Rh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_23_1_OPz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_24_1_1GE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_25_1_Fvy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_26_1_DJf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_27_1_jsE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_28_1_0Iy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_2_1_SjP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_3_1_Ss8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_4_1_TPm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_5_1_XuT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_6_1_DLa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_7_1_uAN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_8_1_ObR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLLTauSpin_FLATv9Xntup/FlatTuple_9_1_ZZm_skimmed.root')

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
