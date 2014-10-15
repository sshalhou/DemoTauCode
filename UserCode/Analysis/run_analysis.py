import time
import sys
import os


from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile

gROOT.Reset()

################
# some global settings

UseNewTriggers = False
OnlyCheckEmbeddedTriggers = False

Verbose = False
SmallRun = False

PrintEvents = False
check_events = []
#check_events.append('1-287-187567')




chain = TChain('demo/FlatTuple')

listOfFiles = []
#listOfFiles.append('./FlatTuple_eTau.root')
#listOfFiles.append('FlatTupleHold/FlatTuple_ggHUP.root') # tau ES up
#listOfFiles.append('FlatTupleHold/FlatTuple_ggH.root')
#listOfFiles.append('./FlatTuple_newVersion.root')
listOfFiles.append('./FlatTuple_bbH90.root')
listOfFiles.append('./FlatTuple_bbH80.root')

for afile in listOfFiles:
	chain.AddFile(afile,0,'demo/FlatTuple')




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
	maxEntries = 300

for entry in range(0,maxEntries):
		entryNumber = chain.GetEntryNumber(entry);
		localEntry = chain.LoadTree(entryNumber);
		if (localEntry >= 0):
			if(entryNumber%500==0):
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
				if chain.eT_passSignalGeneratorMass70to130Cut[index] is False:
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
				if chain.muT_passSignalGeneratorMass70to130Cut[index] is False:
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
				if(sampleName=='/SUSYBBHToTauTau_M-90_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
					SAMPLE_ADD = '_bbH90_'
#				print 'Filling'
				thingToFill = maxPairTypeAndIndex[1]+SAMPLE_ADD+maxPairTypeAndIndex[2]
				thingToFillinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+'inclusive'
#				print thingToFill, maxPairTypeAndIndex, finalWt, thingToFillinc
#				print finalWt
				histogram_dict[thingToFillinc].Fill(eventVariables['SVFitMass'],finalWt)
				if maxPairTypeAndIndex[2] != 'Reject':
					histogram_dict[thingToFill].Fill(eventVariables['SVFitMass'],finalWt)
				if maxPairTypeAndIndex[1] == 'eleTau':
					#print 'xxx', eventID[0]+"-"+eventID[1]+"-"+eventID[2]+"-"+str(eventVariables['numberOfBTaggedJets'])
					njet_eleTau.Fill(eventVariables['numberOfJets'],finalWt)
					nbjet_eleTau.Fill(eventVariables['numberOfBTaggedJets'],finalWt)
					svMass_eleTau.Fill(eventVariables['SVFitMass'],finalWt)
					mvaMET_eleTau.Fill(eventVariables['MVAmet'],finalWt)
					if math.isnan(eventVariables['jet1Pt']) is False:
						j1Pt_eleTau.Fill(eventVariables['jet1Pt'],finalWt)
					if eventVariables['SVFitMass'] < 50:
						print maxPairTypeAndIndex, eventID, eventVariables['SVFitMass']
				elif maxPairTypeAndIndex[1] == 'muTau':
					njet_muTau.Fill(eventVariables['numberOfJets'],finalWt)
					nbjet_muTau.Fill(eventVariables['numberOfBTaggedJets'],finalWt)
					svMass_muTau.Fill(eventVariables['SVFitMass'],finalWt)
					mvaMET_muTau.Fill(eventVariables['MVAmet'],finalWt)
					if math.isnan(eventVariables['jet1Pt']) is False:
						j1Pt_muTau.Fill(eventVariables['jet1Pt'],finalWt)
					if eventVariables['SVFitMass'] < 50:
						print maxPairTypeAndIndex, eventID, eventVariables['SVFitMass']

######################
# save filled histograms

WriteEverything()
writeCompFile()
