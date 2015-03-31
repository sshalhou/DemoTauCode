import time
import sys
import os
import array, math


from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TApplication,TTreeCache,TMatrix,TVector,TString,AddressOf




data_file = TFile("../VAR_TREES/MSSMV10_DATA__variableTree.root","READ")
qcd_file = TFile("../VAR_TREES/MSSMV10_QCDshapes__variableTree.root","READ")
std_file = TFile("../VAR_TREES/MSSMV10_StdBks_FIX__variableTree.root","READ")
ttEmbed_file = TFile("../VAR_TREES/MSSMV10_TTBarEmbedded__variableTree.root","READ")
w_file = TFile("../VAR_TREES/MSSMV10_WjetsShape__variableTree.root","READ")
zttEmbed_file = TFile("../VAR_TREES/MSSMV10_ZTTembedded__variableTree.root","READ")
bbH_file = TFile("../VAR_TREES/MSSMV10_bbH_FIX__variableTree.root","READ")
ggH_file = TFile("../VAR_TREES/MSSMV10_ggH_FIX__variableTree.root","READ")
zlzj_file = TFile("../VAR_TREES/MSSMV10xGEN_ZLandZJSHAPEDY__variableTree.root","READ")

files = []
files.append(data_file)
files.append(qcd_file)
files.append(std_file)
files.append(ttEmbed_file)
files.append(w_file)
#files.append(bbH_file)
#files.append(ggH_file)
files.append(zlzj_file)
files.append(zttEmbed_file)

def get_sample_list(fileList):
	all_samples = []
	for FILE in fileList :
		TREE = FILE.Get("varTree")
		for i in range(0,TREE.GetEntries()):
			TREE.GetEntry(i)
			if str(TREE.sampleType) not in all_samples:
				all_samples.append( str(TREE.sampleType))					
	return all_samples

def get_channel_list(fileList):
	all_channels = []
	for FILE in fileList :
		TREE = FILE.Get("varTree")
		for i in range(0,TREE.GetEntries()):
			TREE.GetEntry(i)
			if str(TREE.channel) not in all_channels:
				all_channels.append( str(TREE.channel))					
	return all_channels

