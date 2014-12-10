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

#listOfFiles.append('./HOLDER/DYOFFnew_skimmed.root')
#listOfFiles.append('./HOLDER/DY2JetsFlatTuple_5_1_bfs.root')



###########
# DY

listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_10_1_2Ih_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_11_1_5YE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_12_1_tLc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_13_1_2wW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_14_1_4b6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_15_1_kx8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_16_1_UI2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_17_1_KHg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_18_1_hKK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_19_1_XMj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_1_1_blg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_2_1_XEG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_3_1_O9X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_4_1_4xG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_5_1_rCz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_6_1_XMN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_7_1_I78_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_8_1_pk7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_9_1_8X3_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_10_1_9c7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_11_1_z0I_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_12_1_ZGr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_13_1_XGW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_14_1_FWE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_15_1_byZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_16_1_tUv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_17_1_swU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_18_1_NUu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_1_1_ClI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_2_1_G54_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_3_1_tPo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_4_1_ley_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_5_1_bfs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_6_1_ox0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_7_1_INJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_8_1_QtR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_9_1_34f_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_10_1_ge0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_11_1_sgb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_12_1_qx4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_13_1_IOH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_14_1_vEj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_15_1_YGT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_16_1_62i_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_1_1_0Xm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_2_1_7oh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_3_1_8z5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_4_1_iAU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_5_1_iFj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_6_1_LUk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_7_1_jUe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_8_1_WlK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_9_1_Z5R_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_10_1_NgC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_11_1_T5r_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_12_1_7ed_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_13_1_BgD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_14_1_rDN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_15_1_U5j_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_16_1_tY0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_1_1_qtj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_2_1_Wo3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_3_1_fuh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_4_1_3ph_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_5_1_3nZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_6_1_sMS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_7_1_BnP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_8_1_8k8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_9_1_Kqb_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_10_1_0dZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_11_1_Fy8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_12_1_Cyl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_13_1_gHI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_14_1_7JL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_15_1_mSd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_16_1_STt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_17_1_aiY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_18_1_nUb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_1_1_lEU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_2_1_nrG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_3_1_LcN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_4_1_LO1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_5_1_GQM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_6_1_wqp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_7_1_ubt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_8_1_awC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_9_1_reh_skimmed.root')


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
				if passesDefaultSelectionETau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				if passesDefaultSelectionMuTau(chain,index,UseNewTriggers,Verbose) is False:
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
					if classification == '_ZL_':
						wt = getWeightForTauPolOffDY_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose)
						# contains an internal check for e->tau
						wt = wt * getFakeZeeWeight(chain,maxPairTypeAndIndex)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					elif classification == '_ZJ_':
						wt = getWeightForTauPolOffDY_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
				elif (SAMPLE_ADD=='_DY1Jet_' or
				      SAMPLE_ADD=='_DY2Jet_' or
					  SAMPLE_ADD=='_DY3Jet_' or
					  SAMPLE_ADD=='_DY4Jet_'):
					classification = classifyZDecay_Final(chain,maxPairTypeAndIndex)
					print classification
					wt = 1.0
					if classification == '_ZL_':
						wt = getWeightForRegularDY_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose)
						# contains an internal check for e->tau
						wt = wt * getFakeZeeWeight(chain,maxPairTypeAndIndex)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					elif classification == '_ZJ_':
						wt = getWeightForRegularDY_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])



######################
# save filled histograms

WriteEverything()
writeCompFile()
