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
listOfFiles.append('./HOLDER/embeddedZTTmutau.root')


##################
#embedded Ztt
##################

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauC_v8FLATtuple/FlatTuple_9_1_4Wf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauC_v8FLATtuple/FlatTuple_3_1_9NM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauC_v8FLATtuple/FlatTuple_2_1_GvX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauC_v8FLATtuple/FlatTuple_5_1_DXk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauC_v8FLATtuple/FlatTuple_7_1_pLo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauC_v8FLATtuple/FlatTuple_4_1_8QQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauC_v8FLATtuple/FlatTuple_8_1_Tyu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauC_v8FLATtuple/FlatTuple_6_1_LOt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauC_v8FLATtuple/FlatTuple_1_1_cHX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauA_v8FLATtuple/FlatTuple_2_1_FLN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauA_v8FLATtuple/FlatTuple_1_1_pZ3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauC_v8FLATtuple/FlatTuple_5_1_pBI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauC_v8FLATtuple/FlatTuple_1_1_BEe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauC_v8FLATtuple/FlatTuple_6_1_PJ8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauC_v8FLATtuple/FlatTuple_4_1_ccS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauC_v8FLATtuple/FlatTuple_2_1_Dny_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauC_v8FLATtuple/FlatTuple_8_1_q42_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauC_v8FLATtuple/FlatTuple_7_1_aL3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauC_v8FLATtuple/FlatTuple_3_1_nWR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauC_v8FLATtuple/FlatTuple_9_1_iLi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauD_v8FLATtuple/FlatTuple_8_1_RjI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauD_v8FLATtuple/FlatTuple_3_1_sQY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauD_v8FLATtuple/FlatTuple_4_1_NvQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauD_v8FLATtuple/FlatTuple_2_1_gj6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauD_v8FLATtuple/FlatTuple_1_1_A8p_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauD_v8FLATtuple/FlatTuple_5_1_14N_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauD_v8FLATtuple/FlatTuple_6_1_dwK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauD_v8FLATtuple/FlatTuple_7_1_z0y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauA_v8FLATtuple/FlatTuple_1_1_iFV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauA_v8FLATtuple/FlatTuple_2_1_y6X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauB_v8FLATtuple/FlatTuple_1_1_mNx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauB_v8FLATtuple/FlatTuple_3_1_vS4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauB_v8FLATtuple/FlatTuple_4_1_eV8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauB_v8FLATtuple/FlatTuple_5_1_U1s_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedETauB_v8FLATtuple/FlatTuple_2_1_93S_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauB_v8FLATtuple/FlatTuple_3_1_rLt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauB_v8FLATtuple/FlatTuple_2_1_ANV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauB_v8FLATtuple/FlatTuple_5_1_6id_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauB_v8FLATtuple/FlatTuple_4_1_m17_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauB_v8FLATtuple/FlatTuple_1_1_GRr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauD_v8FLATtuple/FlatTuple_8_1_3hg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauD_v8FLATtuple/FlatTuple_6_1_rww_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauD_v8FLATtuple/FlatTuple_7_1_1dz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauD_v8FLATtuple/FlatTuple_2_1_eOr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauD_v8FLATtuple/FlatTuple_1_1_fd3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauD_v8FLATtuple/FlatTuple_3_1_33z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauD_v8FLATtuple/FlatTuple_4_1_9iw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZTauTauEmbeddedMuTauD_v8FLATtuple/FlatTuple_5_1_xon_skimmed.root')


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
					classification = '_ZTT_'
					wt = getWeightEmbeddedZTT(chain,maxPairTypeAndIndex,Verbose)
					Fill_ZTTembedded(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])


######################
# save filled histograms

WriteEverything()
writeCompFile()
