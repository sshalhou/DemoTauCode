import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
import math
import glob


def listFlatTrees(path):
    flatRootTrees = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
        	if os.path.join(path, name).endswith('.root'):
	            flatRootTrees.append(os.path.join(path, name))
    return flatRootTrees 



#####################
# for local tests

testList = []
for path in glob.glob('/Users/shalhout/Desktop/CMS_ANALYSIS/Git/Demo*Code/UserCode/Analysis/HOLDER'):
	testList += listFlatTrees(path)


#####################
# for bbH SUSY signal 

bbHsusyList = []
for path in glob.glob('/uscms/home/shalhout/no_backup/NEWSKIMV10/SUSYBBHToTauTauM*_FlatTupeV10'):
	bbHsusyList += listFlatTrees(path)

#####################
# for GluGluH SUSY signal 

ggHsusyList = []
for path in glob.glob('/uscms/home/shalhout/no_backup/NEWSKIMV10/SUSYGluGluToHToTauTauM*_FlatTupeV10'):
	ggHsusyList += listFlatTrees(path)


#####################
# for nMSSM signal 

nmssmSignalList = []
for path in glob.glob('/uscms/home/shalhout/no_backup/NEWSKIMV10/nMSSM_bba1tautaum*_FlatTupeV10'):
	nmssmSignalList += listFlatTrees(path)


#####################
# for data

dataList = []
for path in glob.glob('/uscms/home/shalhout/no_backup/NEWSKIMV10/DATA*_FlatTupeV10'):
	dataList += listFlatTrees(path)

######################
# for ZTauTau Embedded

zttEmbeddedList = []
for path in glob.glob('/uscms/home/shalhout/no_backup/NEWSKIMV10/ZTauTauEmbedded*_FlatTupeV10'):
	zttEmbeddedList += listFlatTrees(path)

######################
# for ttBar Embedded

ttBarEmbeddedList = []
for path in glob.glob('/uscms/home/shalhout/no_backup/NEWSKIMV10/TtBarEmbedded*_FlatTupeV10'):
	ttBarEmbeddedList += listFlatTrees(path)

######################
# for diboson (ZZ,WZ,WW)

dibosonList = []
for path in glob.glob('/uscms/home/shalhout/no_backup/NEWSKIMV10/ZZJets*_FlatTupeV10'):
	dibosonList += listFlatTrees(path)
for path in glob.glob('/uscms/home/shalhout/no_backup/NEWSKIMV10/WZJets*_FlatTupeV10'):
	dibosonList += listFlatTrees(path)
for path in glob.glob('/uscms/home/shalhout/no_backup/NEWSKIMV10/WWJets*_FlatTupeV10'):
	dibosonList += listFlatTrees(path)		

######################
# for singleTop 

singleTopList = []
for path in glob.glob('/uscms/home/shalhout/no_backup/NEWSKIMV10/*tWchannel*_FlatTupeV10'):
	singleTopList += listFlatTrees(path)


######################
# for MC ttBar

ttBarMcList = []
for path in glob.glob('/uscms/home/shalhout/no_backup/NEWSKIMV10/TTJets_*MGDecays_FlatTupeV10'):
	ttBarMcList += listFlatTrees(path)

######################
# for sm 125 Higgs

smH125List = []
for path in glob.glob('/uscms/home/shalhout/no_backup/NEWSKIMV10/*HToTauTauM125*_FlatTupeV10'):
	smH125List += listFlatTrees(path)


######################
# for wJets

wJetsList = []
for path in glob.glob('/uscms/home/shalhout/no_backup/NEWSKIMV10/W*jetsLNu*_FlatTupeV10'):
	wJetsList += listFlatTrees(path)

######################
# for DYjets

dyJetsList = []
for path in glob.glob('/uscms/home/shalhout/no_backup/NEWSKIMV10/DY*JetsToLL_FlatTupeV10'):
	dyJetsList += listFlatTrees(path)

###################
# DY jets no Tau Polarization

dyJetsTauPolOffList = []
for path in glob.glob('/uscms/home/shalhout/no_backup/NEWSKIMV10/DYJetsToLLTauSpin_FlatTupeV10'):
	dyJetsTauPolOffList += listFlatTrees(path)


######################
# for DYjets (low mass)

dyJetsLowMassList = []
for path in glob.glob('/uscms/home/shalhout/no_backup/NEWSKIMV10/DY*JetsToLL_M10To50_FlatTupeV10'):
	dyJetsLowMassList += listFlatTrees(path)


#for i in range(0,len(testList)):
#	print testList[i]



