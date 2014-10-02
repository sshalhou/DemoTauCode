import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile

gROOT.Reset()


################
# some global settings

UseNewTriggers = False
Verbose = False

chain = TChain('demo/FlatTuple')

listOfFiles = []
listOfFiles.append('./FlatTuple_eTau.root')


#listOfFiles.append('/Users/shalhout/Desktop/CMS_ANALYSIS/scratch/120_SYNC/FlatAna/FlatTuple_eTau.root')

for afile in listOfFiles:
	for index in range(0,100):
		treeName = 'demo/FlatTuple;'+str(index)
		chain.AddFile(afile,0,treeName)

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




#for entry in range(0,100):
for entry in range(0,chain.GetEntries()):
		entryNumber = chain.GetEntryNumber(entry);
		localEntry = chain.LoadTree(entryNumber);
		if (localEntry >= 0):
			selector.Process(localEntry)
			passingETauIndices = []
			passingMuTauIndices = []
			maxPairTypeAndIndex = []

#########################################################
# loop over eTau pairs and store all that pass in list

			for index in range(0, chain.eT_correctedSVFitMass.size()):
				if electronID(chain,index,Verbose) and tauID_eTau(chain, index,Verbose) and pairCutsETau(chain, index):
					if electronTrigger(chain,index,UseNewTriggers) is True and tauTriggerForETau(chain, index, UseNewTriggers) is True:
						#print 'PASS eTau'
						passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				if muonID(chain,index,Verbose) and tauID_muTau(chain, index, Verbose) and pairCutsMuTau(chain, index):
					if muonTrigger(chain,index,UseNewTriggers) is True and tauTriggerForMuTau(chain, index, UseNewTriggers) is True:
						#print 'PASS muTau'
						passingMuTauIndices.append(index)

#########################################################
# if have multiple passing H candidates in the same event
# find the highest sumPt pair

			if (len(passingETauIndices) + len(passingMuTauIndices)) == 1:
				if len(passingETauIndices) == 1 :
					maxPairTypeAndIndex.append(passingETauIndices[0])
					maxPairTypeAndIndex.append('electronTau')
				elif len(passingMuTauIndices) == 1:
					maxPairTypeAndIndex.append(passingMuTauIndices[0])
					maxPairTypeAndIndex.append('muonTau')
			if (len(passingETauIndices) + len(passingMuTauIndices)) > 1:
					getMaxPtPairIndex(chain, maxPairTypeAndIndex, passingMuTauIndices, passingETauIndices)
			print 'PASS', maxPairTypeAndIndex

#########################################################
# now classify the event based on tauPt and nbtags
# add run, event, lumi to FlatTree
