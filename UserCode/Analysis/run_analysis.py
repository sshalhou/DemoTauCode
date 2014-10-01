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

for afile in listOfFiles:
	for index in range(0,100):
		treeName = 'demo/FlatTuple;'+str(index)
		chain.AddFile(afile,0,treeName)

theselector = "../FlatTreeSel.C+"
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




#for entry in range(0,100):
for entry in range(0,chain.GetEntries()):
		entryNumber = chain.GetEntryNumber(entry);
		localEntry = chain.LoadTree(entryNumber);
		if (localEntry >= 0):
			selector.Process(localEntry)
			for index in range(0, chain.eT_correctedSVFitMass.size()):
				if electronID(chain,index,Verbose) is True and tauID_eTau(chain, index,Verbose) is True:
					if electronTrigger(chain,index,UseNewTriggers) is True and tauTriggerForETau(chain, index, UseNewTriggers) is True:
						print 'PASS eTau'
			for index in range(0, chain.muT_correctedSVFitMass.size()):
				if muonID(chain,index,Verbose) is True and tauID_muTau(chain, index, Verbose) is True:
					if muonTrigger(chain,index,UseNewTriggers) is True and tauTriggerForMuTau(chain, index, UseNewTriggers) is True:
						print 'PASS muTau'
