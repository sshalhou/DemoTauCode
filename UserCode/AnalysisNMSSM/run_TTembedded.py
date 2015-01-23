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





#################
# embedded ttbar
#################
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_10_1_WV7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_11_1_OBv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_12_1_Red_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_13_1_Hka_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_14_1_sbU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_15_1_3LV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_16_1_g6K_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_17_1_AeZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_18_1_0Sy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_19_1_RNG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_1_1_YYr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_20_1_Rh0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_2_1_pYW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_3_1_Qbf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_4_1_nHw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_5_1_p8d_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_6_1_amk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_7_1_Dru_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_8_1_NEt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedETau_FLATv9Xntup/FlatTuple_9_1_ZM1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_10_1_1dM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_11_1_KUW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_12_1_poq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_13_1_l7K_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_14_1_mlN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_15_1_x8R_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_16_1_i9X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_17_1_Ka0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_18_1_hu4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_19_1_PEl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_1_1_0JE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_20_1_p0c_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_21_1_lqN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_2_1_rE1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_3_1_iC2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_4_1_vx0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_5_1_fRR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_6_1_7By_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_7_1_0y9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_8_1_sLC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TtBarEmbeddedMuTau_FLATv9Xntup/FlatTuple_9_1_zlR_skimmed.root')


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
					classification = classifyZDecay_Final(chain,maxPairTypeAndIndex)
					if classification == '_ZTT_':
						print 'filling a ', classification, 'event'
						# since will subtract from embedded ZTT fill the ZTT histograms :
						wt = getWeightEmbeddedTTbar(chain,maxPairTypeAndIndex,Verbose)
						Fill_ZTTembedded(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])




######################
# save filled histograms

WriteEverything()
writeCompFile()
