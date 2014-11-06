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
#listOfFiles.append('./HOLDER/DATAA_partial_FlatTuple_1_1_I5s.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_1_1_I5s_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_1_1_KIQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_1_1_Tj1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_1_1_tJt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_2_1_0S8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_2_1_JIl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_2_1_emp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_2_1_fvG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_3_1_PuD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_3_1_ROv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_3_1_tTy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_4_1_Qcy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_4_1_Yg5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_4_1_kxi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_5_1_2ss_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_5_1_9SD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_5_1_rtZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_6_1_JRW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_6_1_MAi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_6_1_l5M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_7_1_RoG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_7_1_tGi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_8_1_E1H_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_8_1_jWE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_9_1_6jK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/data_skimmed/FlatTuple_RecoveredJobs_skimmed.root')

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
	maxEntries = 1000

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
				if passesQCDSelectionETau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				if passesQCDSelectionMuTau(chain,index,UseNewTriggers,Verbose) is False:
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
				if maxPairTypeAndIndex[1] == 'eleTau':
					maxPairTypeAndIndex.append(eTauClassification_forQCD(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(chain.NAMEVAR)
				if PrintEvents:
					print maxPairTypeAndIndex[1], maxPairTypeAndIndex[2],eventID[0]+"-"+eventID[1]+"-"+eventID[2]

##################################################################################
# get weights and fill histograms


			if len(maxPairTypeAndIndex)	> 0:
				eventVariables = {}
				fillVariables(chain,eventVariables,maxPairTypeAndIndex,Verbose)
				SAMPLE_ADD = getSAMPLE_ADD(sampleName)
				assert(len(SAMPLE_ADD)>0), " Assert : unknown sample "
				if SAMPLE_ADD == '_data_obs_':
					SAMPLE_ADD = '_QCD_'
				QCDShapeWeightsDownNominalUp_dict = {}
				QCDShapeWeights(chain, maxPairTypeAndIndex, QCDShapeWeightsDownNominalUp_dict)
				#print QCDShapeWeightsDownNominalUp_dict
				FillQCDShapes(maxPairTypeAndIndex,SAMPLE_ADD,
									histogram_dict,
									QCDShapeWeightsDownNominalUp_dict,
									eventVariables['SVFitMass'])


######################
# save filled histograms

WriteEverything()
writeCompFile()
