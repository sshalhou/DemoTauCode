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

listOfFiles.append('./HOLDER/DYlowMass.root')
listOfFiles.append('./HOLDER/DY1jetLOWMASS.root')
listOfFiles.append('./HOLDER/DY2jetLOWMASS.root')


###########
# DY @ low Mass 


listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_10_1_k0X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_8_1_vkr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_6_1_Ye6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_14_1_xin_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_15_1_Mvu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_16_1_dIq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_18_1_KSR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_19_1_Qe7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_20_1_UBD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_17_1_MDx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_26_1_E8T_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_27_1_Oy7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_24_1_gNG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_25_1_72U_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_11_1_SnM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_23_1_SPv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_4_1_knt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_12_1_wEU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_3_1_ypI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_1_1_G22_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_28_1_qmf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_13_1_5MQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_21_1_Dhf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_2_1_lzn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_9_1_rsj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_22_1_ofg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_5_1_bDu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLL_M10To50_v9FlatTuple/FlatTuple_7_1_aH3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_4_1_kUU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_3_1_0Rq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_13_1_Azh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_11_1_zR3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_9_1_HkG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_6_1_VI4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_17_1_ZGn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_21_1_74A_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_7_1_tkU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_25_1_1Vp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_27_1_Ex0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_1_1_fPX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_8_1_tft_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_5_1_Lhd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_15_1_mGo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_12_1_vCp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_16_1_FLU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_18_1_ijH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_22_1_f3H_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_2_1_HrE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_19_1_CGj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_14_1_Rq8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_10_1_8i0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_23_1_AT6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_26_1_MON_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_24_1_Ikg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_28_1_FEQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_M10To50_v9FlatTuple/FlatTuple_20_1_L96_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_2_1_CVV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_4_1_2Ix_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_12_1_uG1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_5_1_36x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_6_1_Onb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_10_1_DMC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_9_1_1bd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_11_1_z95_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_13_1_AtC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_8_1_ZX6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_16_1_4hO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_18_1_Llk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_19_1_aFX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_20_1_mWs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_7_1_70p_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_23_1_5ZU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_27_1_P6L_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_14_1_iEQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_28_1_smB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_24_1_Pjk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_3_1_RJB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_25_1_KZk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_1_1_3oi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_17_1_MMC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_15_1_Qoy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_22_1_zeE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_26_1_6YH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_M10To50_v9FlatTuple/FlatTuple_21_1_qWB_skimmed.root')


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
					maxPairTypeAndIndex.append(muTauClassification_forQCD(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(chain.NAMEVAR)
					maxPairTypeAndIndex.append(muTauClassificationJECDOWN(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(muTauClassificationJECUP(chain, maxPairTypeAndIndex[0]))
				if maxPairTypeAndIndex[1] == 'eleTau':
					maxPairTypeAndIndex.append(eTauClassification_forQCD(chain, maxPairTypeAndIndex[0]))
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
				if SAMPLE_ADD == '_DYJetLowMass_' or SAMPLE_ADD == '_DY1JetLowMass_' or SAMPLE_ADD == '_DY2JetLowMass_':
					classification = '_ZTT_lowMass_'
					wt = 1.0
					wt = getWeightForLowMassDY(chain,maxPairTypeAndIndex,Verbose)
					Fill_ZTTlowMass(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					




######################
# save filled histograms

WriteEverything()
writeCompFile()
