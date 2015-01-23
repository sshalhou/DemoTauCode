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

#listOfFiles.append('./HOLDER/embeddedZTTetau.root')
#listOfFiles.append('./HOLDER/embeddedZTTmutau.root')


##################
#embedded Ztt
##################
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauA_FLATv9Xntup/FlatTuple_1_1_Qgg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauA_FLATv9Xntup/FlatTuple_2_1_wEV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauB_FLATv9Xntup/FlatTuple_1_1_MXw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauB_FLATv9Xntup/FlatTuple_2_1_Aob_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauB_FLATv9Xntup/FlatTuple_3_1_URu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauB_FLATv9Xntup/FlatTuple_4_1_2Zi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauB_FLATv9Xntup/FlatTuple_5_1_EMs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauC_FLATv9Xntup/FlatTuple_1_1_1S0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauC_FLATv9Xntup/FlatTuple_2_1_qtH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauC_FLATv9Xntup/FlatTuple_3_1_zq1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauC_FLATv9Xntup/FlatTuple_4_1_akB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauC_FLATv9Xntup/FlatTuple_5_1_j2c_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauC_FLATv9Xntup/FlatTuple_6_1_EEz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauC_FLATv9Xntup/FlatTuple_7_1_uKe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauC_FLATv9Xntup/FlatTuple_8_1_s32_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauC_FLATv9Xntup/FlatTuple_9_1_er2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauD_FLATv9Xntup/FlatTuple_1_1_dky_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauD_FLATv9Xntup/FlatTuple_2_1_sMn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauD_FLATv9Xntup/FlatTuple_3_1_SqQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauD_FLATv9Xntup/FlatTuple_4_1_2na_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauD_FLATv9Xntup/FlatTuple_5_1_9C1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauD_FLATv9Xntup/FlatTuple_6_1_1bj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauD_FLATv9Xntup/FlatTuple_7_1_CHg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedETauD_FLATv9Xntup/FlatTuple_8_1_rwV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauA_FLATv9Xntup/FlatTuple_1_1_rY9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauA_FLATv9Xntup/FlatTuple_2_1_53k_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauB_FLATv9Xntup/FlatTuple_1_1_of4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauB_FLATv9Xntup/FlatTuple_2_1_5ri_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauB_FLATv9Xntup/FlatTuple_3_1_rvG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauB_FLATv9Xntup/FlatTuple_4_1_djN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauB_FLATv9Xntup/FlatTuple_5_1_oUI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauC_FLATv9Xntup/FlatTuple_1_1_JAV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauC_FLATv9Xntup/FlatTuple_2_1_E1M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauC_FLATv9Xntup/FlatTuple_3_1_z04_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauC_FLATv9Xntup/FlatTuple_4_1_biY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauC_FLATv9Xntup/FlatTuple_5_1_Oh4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauC_FLATv9Xntup/FlatTuple_6_1_NyK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauC_FLATv9Xntup/FlatTuple_7_1_IZD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauC_FLATv9Xntup/FlatTuple_8_1_4DU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauC_FLATv9Xntup/FlatTuple_9_1_HJt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauD_FLATv9Xntup/FlatTuple_1_1_dxz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauD_FLATv9Xntup/FlatTuple_2_1_ZWw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauD_FLATv9Xntup/FlatTuple_3_1_3CO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauD_FLATv9Xntup/FlatTuple_4_1_7cx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauD_FLATv9Xntup/FlatTuple_5_1_b3x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauD_FLATv9Xntup/FlatTuple_6_1_J9X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauD_FLATv9Xntup/FlatTuple_7_1_Drm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZTauTauEmbeddedMuTauD_FLATv9Xntup/FlatTuple_8_1_hJL_skimmed.root')

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
				if passesEmbeddedZTauTauSelectionETau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				if passesEmbeddedZTauTauSelectionMuTau(chain,index,UseNewTriggers,Verbose) is False:
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

				if SAMPLE_ADD == '_embeddedZTT_':
					classification = classifyZDecay_Final(chain,maxPairTypeAndIndex)
					if classification == '_ZTT_':
						print 'filling a ', classification, 'event'
						wt = getWeightEmbeddedZTT(chain,maxPairTypeAndIndex,Verbose)
						Fill_ZTTembedded(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])


######################
# save filled histograms

WriteEverything()
writeCompFile()
