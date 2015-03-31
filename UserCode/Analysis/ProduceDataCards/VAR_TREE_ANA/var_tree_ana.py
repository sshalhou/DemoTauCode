import time
import sys
import os
import array, math


from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TApplication,TTreeCache,TMatrix,TVector,TString,AddressOf




from python.Files import *
from python.Channels import *
from python.Classification import *
from python.Histograms import *
from python.Weights import *


print files
print channels

# all_samples = get_sample_list(files)

# print all_samples


# chan = get_channel_list(files)
# print chan

HIST_SV = {}
HIST_DM = {}
initialize_decay_vs_SVplots(HIST_DM)
initialize_mass_vs_DMplots(HIST_SV)

#print HIST_DM


WriteDicts(HIST_DM, HIST_SV)

for FILE in files :
		TREE = FILE.Get("varTree")
		for i in range(0,TREE.GetEntries()):
			TREE.GetEntry(i)
			classification = GetSampleClassification(str(FILE.GetName()),str(TREE.sampleType))
			evType = ''
			if TREE.isMuonTau == 1.0:
				evType = 'muTau'
			if TREE.isMuonTau == 0.0:
				evType = 'eleTau'
			sfM = getWeightSF('muTau',TREE.channel,classification)
			sfE = getWeightSF('eleTau',TREE.channel,classification)
			if classification=='QCD':
				print sfM, sfE, TREE.channel


# FILE = TFile("ProduceDataCards/VAR_TREES/MSSMV10_TTBarEmbedded__variableTree.root","READ")

# TREE = FILE.Get("varTree")

# for i in range(0,TREE.GetEntries()):
# 	TREE.GetEntry(i)
# 	print TREE.tauEs, TREE.sampleType, TREE.channel

# TREE.Draw("SVmass",'tauEs=="TauEsNominal" && channel=="btag_low" && decay_mode_2==1','')	
# TREE.Draw("SVmass",'tauEs=="TauEsNominal" && channel=="btag_low" && decay_mode_2==2','sames')	
# TREE.Draw("SVmass",'tauEs=="TauEsNominal" && channel=="btag_low" && decay_mode_2==0','sames')	


var = raw_input("Please enter something: ")
