import time
import sys
import os
import array, math


from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TApplication,TTreeCache,TMatrix,TVector,TString,AddressOf


# samples 

samples = []
samples.append('Data')
samples.append('QCD')
samples.append('SM_Higgs125')
samples.append('TT')
samples.append('VV')
samples.append('ZTT')
samples.append('embeddedTT')
samples.append('Wjets')
samples.append('ZL')
samples.append('ZJ')


# lists of samples plotted as one shape
SM_Higgs_list = ['_VH_SM125_', '_ggH_SM125_', '_qqH_SM125_']

TT_list = ['_TTJetsFullLept_', '_TTJetsHadronic_','_TTJetsSemiLept_']

VV_list = ['_SingleTop_', '_SingleTopBar_','_ZZJetsTo2L2Nu_', 
			'_ZZJetsTo2L2Q_', '_ZZJetsTo4L_', 
			'_WZJetsTo2L2Q_', '_WZJetsTo3LNu_', '_WWJetsTo2L2Nu_']

Wjets_list = ['_W4JetsToLNu_', '_WJetsToLNu_', 
			'_W1JetsToLNu_', '_W2JetsToLNu_', '_W3JetsToLNu_']

# also split by fileName
ZLZJ_list = ['_DYJetsInclusive_','_DY1Jet_','_DY2Jet_','_DY3Jet_','_DY4Jet_']


def GetSampleClassification(FileName,SampleType):
	FileName = str(FileName)
	SampleType = str(SampleType)
	classification = ''
	#print FileName, SampleType
	if SampleType == '_data_obs_' and 'QCD' not in FileName:
		classification = 'Data'
	elif SampleType == '_data_obs_' and 'QCD' in FileName:
		classification = 'QCD'		
	elif SampleType in SM_Higgs_list:
		classification = 'SM_Higgs125'
	elif SampleType in TT_list:
		classification = 'TT'
	elif SampleType in VV_list:
		classification = 'VV'	
	elif SampleType == '_embeddedZTT_':
		classification = 'ZTT'	
	elif SampleType == '_embeddedTTbar_':
		classification = 'embeddedTT'	
	elif SampleType in Wjets_list:
		classification = 'Wjets'
	elif SampleType in ZLZJ_list:
		if 'ZL_EXCLUSIVE' in FileName:
			classification = 'ZL'
		if 'ZJ_EXCLUSIVE' in FileName:
			classification = 'ZJ'
	return classification












