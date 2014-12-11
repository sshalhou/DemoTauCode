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



listOfFiles.append('./HOLDER/TTembedET.root')
listOfFiles.append('./HOLDER/TTembedMT.root')



#################
# embedded ttbar
#################

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_8_1_77R_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_3_1_BOa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_2_1_paW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_9_1_cVT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_13_1_L2Y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_5_1_2pM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_7_1_TMB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_14_1_TMn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_1_1_jlf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_4_1_TiG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_19_1_rk7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_18_1_TCD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_6_1_OJn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_17_1_Uqc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_11_1_Zmz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_12_1_cQU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_10_1_GW8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_21_1_CiT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_15_1_R2U_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_16_1_alW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedETau_v8FLATtuple/FlatTuple_20_1_A0D_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_12_1_rQf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_7_1_wY3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_17_1_I2J_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_10_1_naD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_14_1_YaV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_16_1_ZSz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_18_1_QRm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_13_1_bQq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_5_1_XK1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_6_1_cfo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_3_1_uVC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_19_1_5zp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_9_1_uPW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_11_1_pCy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_15_1_L3q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_8_1_94L_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_20_1_Lgz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_2_1_EZE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_1_1_jzd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_4_1_33C_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TtBarEmbeddedMuTau_v8FLATtuple/FlatTuple_21_1_cOk_skimmed.root')


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
