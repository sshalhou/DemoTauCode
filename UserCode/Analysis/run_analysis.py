import time
import sys
import os

############
# due to 3 crashing events
# impose the following SF
# bbSUSY900 GEV (997674-2217)/997674.0 = 9.97777831235453716e-01
# ggHSUSY 250 GeV (1000441-2223)/1000441.0 = 9.97777979910859258e-01
# ggHSUSY 900 GeV (975744-2168.)/975744 = 9.97778105732651133e-01

from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TApplication


################
# some global settings

UseNewTriggers = False
OnlyCheckEmbeddedTriggers = False

Verbose = False
SmallRun = True

PrintEvents = False
check_events = []
#check_events.append('1-287-187567')




chain = TChain('*/FlatTuple')

listOfFiles = []
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNA_FlatTuple/FlatTuple_1_1_yol.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNA_FlatTuple/FlatTuple_2_1_ZFT.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_FlatTuple/FlatTuple_1_1_QUV.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_FlatTuple/FlatTuple_2_1_o9e.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_FlatTuple/FlatTuple_3_1_m5G.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_FlatTuple/FlatTuple_4_1_MYD.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_FlatTuple/FlatTuple_5_1_50n.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_FlatTuple/FlatTuple_6_1_LBA.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_FlatTuple/FlatTuple_1_1_NvJ.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_FlatTuple/FlatTuple_2_1_Ht3.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_FlatTuple/FlatTuple_3_1_HcU.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_FlatTuple/FlatTuple_4_1_jsl.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_FlatTuple/FlatTuple_5_1_Bib.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_FlatTuple/FlatTuple_6_1_Es4.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_FlatTuple/FlatTuple_7_1_KO3.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_FlatTuple/FlatTuple_8_1_fI6.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_FlatTuple/FlatTuple_9_1_hdX.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_FlatTuple/FlatTuple_1_1_EdN.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_FlatTuple/FlatTuple_2_1_vsX.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_FlatTuple/FlatTuple_3_1_Ocs.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_FlatTuple/FlatTuple_4_1_bjt.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_FlatTuple/FlatTuple_5_1_Grc.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_FlatTuple/FlatTuple_6_1_V69.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_FlatTuple/FlatTuple_7_1_tVQ.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_FlatTuple/FlatTuple_8_1_FtS.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_SZS_RECOVEREDDATA_ABCD_v5ntup.root')

for afile in listOfFiles:
	chain.AddFile(afile,0,'TauEsNominal/FlatTuple')
	#chain.AddFile(afile,0,'TauEsUp/FlatTuple')
	#chain.AddFile(afile,0,'TauEsDown/FlatTuple')




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

maxEntries = chain.GetEntries()

if SmallRun is True:
	maxEntries = 3000

for entry in range(0,maxEntries):
		entryNumber = chain.GetEntryNumber(entry);
		localEntry = chain.LoadTree(entryNumber);
		if (localEntry >= 0):
			#print "NAMEVAR = ", chain.NAMEVAR
			if(entryNumber%1000==0):
				print 'processing entry ',entryNumber, 'of', maxEntries
			selector.Process(localEntry)
			passingETauIndices = []
			passingMuTauIndices = []
			maxPairTypeAndIndex = []

			#########################################################
			# get event ID

			eventID = [str(chain.run), str(chain.luminosityBlock), str(chain.event)]
			eventString = str(chain.run)+"-"+str(chain.luminosityBlock)+"-"+str(chain.event)
			sampleName =  str(chain.SampleName)
			#if eventString in check_events:
			#	Verbose = True
			#	print "**********************************************"
			#	print "*********", eventString, "**************"
			#else:
			#	Verbose = False

			## temp
			#print "---------- checking Event",eventID[0],eventID[1],eventID[2],"-----------------------"



#########################################################
# loop over eTau pairs and store all that pass in list

			for index in range(0, chain.eT_correctedSVFitMass.size()):
				passesCuts = True
				if electronID(chain,index,Verbose) is False:
					passesCuts = False
				if tauID_eTau(chain, index, Verbose) is False:
					passesCuts = False
				if pairCutsETau(chain, index,Verbose) is False:
					passesCuts = False
				if OnlyCheckEmbeddedTriggers is True and embeddedZTauTauTrigForETau(chain, index, Verbose) is False:
					passesCuts = False
				if OnlyCheckEmbeddedTriggers is False and electronTrigger(chain,index,UseNewTriggers) is False:
					passesCuts = False
				if OnlyCheckEmbeddedTriggers is False and tauTriggerForETau(chain,index,UseNewTriggers) is False:
					passesCuts = False
				#if chain.eT_passSignalGeneratorMass70to130Cut[index] is False:
				#	passesCuts = False
				if chain.eT_correctedSVFitMass[index] < 50:
					passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				if muonID(chain,index,Verbose) is False:
					passesCuts = False
				if tauID_muTau(chain, index, Verbose) is False:
					passesCuts = False
				if pairCutsMuTau(chain, index,Verbose) is False:
					passesCuts = False
				if OnlyCheckEmbeddedTriggers is True and embeddedZTauTauTrigForMuTau(chain, index, Verbose) is False:
					passesCuts = False
				if OnlyCheckEmbeddedTriggers is False and muonTrigger(chain,index,UseNewTriggers) is False:
					passesCuts = False
				if OnlyCheckEmbeddedTriggers is False and tauTriggerForMuTau(chain,index,UseNewTriggers) is False:
					passesCuts = False
				#if chain.muT_passSignalGeneratorMass70to130Cut[index] is False:
				#	passesCuts = False
				if chain.muT_correctedSVFitMass[index] < 50:
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
				if maxPairTypeAndIndex[1] == 'eleTau':
					maxPairTypeAndIndex.append(eTauClassification(chain, maxPairTypeAndIndex[0]))
				if PrintEvents:
					print maxPairTypeAndIndex[1], maxPairTypeAndIndex[2],eventID[0]+"-"+eventID[1]+"-"+eventID[2]

##################################################################################
# next step is plotting, followed by process classification, followed by weights
# i would also like to save event totals to json format for later input
# http://stackoverflow.com/questions/11026959/python-writing-dict-to-txt-file-and-reading-dict-from-txt-file


			if len(maxPairTypeAndIndex)	> 0:
				eventVariables = {}
				fillVariables(chain,eventVariables,maxPairTypeAndIndex,Verbose)
				#print maxPairTypeAndIndex, eventVariables['SVFitMass'], eventVariables['numberOfBTaggedJets'],eventVariables['tauPt']
				finalWt = signalSUSYweight(chain, maxPairTypeAndIndex, Verbose)
				SAMPLE_ADD = '_ggH120_'
				if(sampleName=='/SUSYBBHToTauTau_M-80_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
					SAMPLE_ADD = '_bbH80_'
				elif(sampleName=='/SUSYBBHToTauTau_M-90_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
					SAMPLE_ADD = '_bbH90_'
				elif(sampleName=='/TauPlusX/Run2012A-22Jan2013-v1/AOD'):
					SAMPLE_ADD ='_data_obs_'
					finalWt = 1.0
				elif(sampleName=='/TauPlusX/Run2012B-22Jan2013-v1/AOD'):
					SAMPLE_ADD ='_data_obs_'
					finalWt = 1.0
				elif(sampleName=='/TauPlusX/Run2012C-22Jan2013-v1/AOD'):
					SAMPLE_ADD ='_data_obs_'
					finalWt = 1.0
				elif(sampleName=='/TauPlusX/Run2012D-22Jan2013-v1/AOD'):
					SAMPLE_ADD ='_data_obs_'
					finalWt = 1.0
				thingToFill = maxPairTypeAndIndex[1]+SAMPLE_ADD+maxPairTypeAndIndex[2]
				thingToFillinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+'inclusive'
				# fill inclusive
				histogram_dict[thingToFillinc].Fill(eventVariables['SVFitMass'],finalWt)
				# categorized
				if maxPairTypeAndIndex[2] != 'Reject':
					histogram_dict[thingToFill].Fill(eventVariables['SVFitMass'],finalWt)
				# if maxPairTypeAndIndex[1] == 'eleTau':
				# 	#print 'xxx', eventID[0]+"-"+eventID[1]+"-"+eventID[2]+"-"+str(eventVariables['numberOfBTaggedJets'])
				# 	njet_eleTau.Fill(eventVariables['numberOfJets'],finalWt)
				# 	nbjet_eleTau.Fill(eventVariables['numberOfBTaggedJets'],finalWt)
				# 	svMass_eleTau.Fill(eventVariables['SVFitMass'],finalWt)
				# 	mvaMET_eleTau.Fill(eventVariables['MVAmet'],finalWt)
				# 	if math.isnan(eventVariables['jet1Pt']) is False:
				# 		j1Pt_eleTau.Fill(eventVariables['jet1Pt'],finalWt)
				# 	if eventVariables['SVFitMass'] < 50:
				# 		print maxPairTypeAndIndex, eventID, eventVariables['SVFitMass']
				# elif maxPairTypeAndIndex[1] == 'muTau':
				# 	njet_muTau.Fill(eventVariables['numberOfJets'],finalWt)
				# 	nbjet_muTau.Fill(eventVariables['numberOfBTaggedJets'],finalWt)
				# 	svMass_muTau.Fill(eventVariables['SVFitMass'],finalWt)
				# 	mvaMET_muTau.Fill(eventVariables['MVAmet'],finalWt)
				# 	if math.isnan(eventVariables['jet1Pt']) is False:
				# 		j1Pt_muTau.Fill(eventVariables['jet1Pt'],finalWt)
				# 	if eventVariables['SVFitMass'] < 50:
				# 		print maxPairTypeAndIndex, eventID, eventVariables['SVFitMass']

######################
# save filled histograms

WriteEverything()
writeCompFile()
