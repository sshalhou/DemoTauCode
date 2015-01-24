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


listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_10_1_7RJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_11_1_Tf1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_12_1_0hn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_13_1_u4x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_14_1_yP7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_15_1_8IV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_16_1_44N_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_17_1_Lqj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_18_1_dBv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_19_1_bT6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_1_1_I3B_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_20_1_Obg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_21_1_bVB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_22_1_cqC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_23_1_Qlt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_24_1_MUo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_25_1_DJE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_26_1_huI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_27_1_U0g_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_28_1_viC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_2_1_cV5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_3_1_Qra_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_4_1_N59_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_5_1_M1n_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_6_1_AMW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_7_1_KxW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_8_1_9kw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_M10To50_FLATv9Xntup/FlatTuple_9_1_eu1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_10_1_sZm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_11_1_SMW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_12_1_Zo5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_13_1_sEB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_14_1_oAe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_15_1_l4U_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_16_1_MZp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_17_1_PoY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_18_1_YQY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_19_1_VpI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_1_1_Maf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_20_1_fxl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_21_1_yXJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_22_1_2q4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_23_1_O9z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_24_1_u1K_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_25_1_Yfh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_26_1_7YP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_27_1_fNJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_28_1_e3W_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_2_1_uyq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_3_1_7Ga_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_4_1_lky_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_5_1_Dg2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_6_1_rvY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_7_1_rsl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_8_1_CqM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_M10To50_FLATv9Xntup/FlatTuple_9_1_5Ud_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_10_1_nBP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_11_1_0WI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_12_1_qJ4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_13_1_UHY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_14_1_JpO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_15_1_G7r_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_16_1_taG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_17_1_t9T_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_18_1_TVi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_19_1_REV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_1_1_x0R_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_20_1_AL1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_21_1_5XC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_22_1_NRW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_23_1_S7A_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_24_1_nTO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_25_1_IWD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_26_1_cil_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_27_1_wEu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_28_1_GsC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_2_1_Cgb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_3_1_9Ou_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_4_1_mQh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_5_1_GpT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_6_1_g4R_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_7_1_fBz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_8_1_z3T_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_M10To50_FLATv9Xntup/FlatTuple_9_1_NEH_skimmed.root')

###########
# DY @ low Mass 


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
				if SAMPLE_ADD == '_DYJetLowMass_' or SAMPLE_ADD == '_DY1JetLowMass_' or SAMPLE_ADD == '_DY2JetLowMass_':
					classification = '_ZTT_lowMass_'
					wt = 1.0
					wt = getWeightForLowMassDY(chain,maxPairTypeAndIndex,Verbose)
					Fill_ZTTlowMass(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					




######################
# save filled histograms

WriteEverything()
writeCompFile()
