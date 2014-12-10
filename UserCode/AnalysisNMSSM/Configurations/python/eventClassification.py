import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile


####################
# for QCD, the no-btag case
# uses loose CSV b-jets count
# while the no-btag case still uses
# the tight CSV b-jet count

def btagAndTauPtCategory_forQCD(btags, tauPt, njets, btagsLooseCSV):
  #print 'tight btags : ', btags
  #print 'loose btags : ', btagsLooseCSV
  returnWord = 'Reject'
  if btagsLooseCSV>0:
    returnWord = 'btag'    
  #print returnWord
  return returnWord


def btagAndTauPtCategory(btags, tauPt, njets):
  returnWord = 'Reject'
  if btags > 0:
    returnWord = 'btag'
  return returnWord


def getSAMPLE_ADD(sampleName):
    SAMPLE_ADD = ""
    if(sampleName=='/SUSYBBHToTauTau_M-80_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH80_'
    elif(sampleName=='/SUSYBBHToTauTau_M-90_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH90_'
    elif(sampleName=='/SUSYBBHToTauTau_M-100_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH100_'
    elif(sampleName=='/SUSYBBHToTauTau_M-110_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH110_'
    elif(sampleName=='/SUSYBBHToTauTau_M-120_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH120_'
    elif(sampleName=='/SUSYBBHToTauTau_M-130_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH130_'
    elif(sampleName=='/SUSYBBHToTauTau_M-140_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH140_'
    elif(sampleName=='/SUSYBBHToTauTau_M-160_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH160_'
    elif(sampleName=='/SUSYBBHToTauTau_M-180_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH180_'
    elif(sampleName=='/SUSYBBHToTauTau_M-200_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH200_'
    elif(sampleName=='/SUSYBBHToTauTau_M-250_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH250_'
    #elif(sampleName=='/SUSYBBHToTauTau_M-300_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
    #    SAMPLE_ADD = '_bbH300_'
    elif(sampleName=='/SUSYBBHToTauTau_M-300_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM'):
        SAMPLE_ADD = '_bbH300_'
    elif(sampleName=='/SUSYBBHToTauTau_M-350_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH350_'
    elif(sampleName=='/SUSYBBHToTauTau_M-400_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH400_'
    elif(sampleName=='/SUSYBBHToTauTau_M-450_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH450_'
    elif(sampleName=='/SUSYBBHToTauTau_M-500_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH500_'
    elif(sampleName=='/SUSYBBHToTauTau_M-600_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH600_'
    elif(sampleName=='/SUSYBBHToTauTau_M-700_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH700_'
    elif(sampleName=='/SUSYBBHToTauTau_M-800_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH800_'
    elif(sampleName=='/SUSYBBHToTauTau_M-900_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH900_'
   
    elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m25_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
    	SAMPLE_ADD = '_bba125_'
    elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m30_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
    	SAMPLE_ADD = '_bba130_'
    elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m35_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
    	SAMPLE_ADD = '_bba135_'    
    elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m40_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
    	SAMPLE_ADD = '_bba140_'
    elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m45_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
    	SAMPLE_ADD = '_bba145_'    	    
    elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m50_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
    	SAMPLE_ADD = '_bba150_'
    elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m55_FilterMuOrEle15_8TeV/Summer12DR53X-PU_S10_START53_V19-v2/AODSIM'):
    	SAMPLE_ADD = '_bba155_'
    elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m60_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
    	SAMPLE_ADD = '_bba160_'
    elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m65_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
    	SAMPLE_ADD = '_bba165_'
    elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m70_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
    	SAMPLE_ADD = '_bba170_'
    elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m75_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
    	SAMPLE_ADD = '_bba175_'    	
    elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m80_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
    	SAMPLE_ADD = '_bba180_'    	    	    	    	    	    		
  
  
  
    elif(sampleName=='/SUSYBBHToTauTau_M-1000_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_bbH1000_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-80_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH80_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-90_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH90_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-100_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH100_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-110_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH110_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-120_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH120_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-130_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH130_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-140_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH140_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-160_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH160_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-180_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH180_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-200_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH200_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-250_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH250_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-300_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH300_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-350_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH350_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-400_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH400_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-450_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH450_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-500_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH500_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-600_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH600_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-700_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH700_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-800_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH800_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-900_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH900_'
    elif(sampleName=='/SUSYGluGluToHToTauTau_M-1000_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH1000_'
    elif(sampleName=='/TauPlusX/Run2012A-22Jan2013-v1/AOD'):
        SAMPLE_ADD = '_data_obs_'
    elif(sampleName=='/TauPlusX/Run2012B-22Jan2013-v1/AOD'):
        SAMPLE_ADD = '_data_obs_'
    elif(sampleName=='/TauPlusX/Run2012C-22Jan2013-v1/AOD'):
        SAMPLE_ADD = '_data_obs_'
    elif(sampleName=='/TauPlusX/Run2012D-22Jan2013-v1/AOD'):
        SAMPLE_ADD = '_data_obs_'

    elif(sampleName=='/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_DYJetsInclusive_'

    elif(sampleName=='/DY1JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_DY1Jet_'

    elif(sampleName=='/DY2JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM'):
        SAMPLE_ADD = '_DY2Jet_'

    elif(sampleName=='/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_DY3Jet_'

    elif(sampleName=='/DY4JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_DY4Jet_'

    elif(sampleName=='/TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v2/AODSIM'):
        SAMPLE_ADD = '_TTJetsFullLept_'

    elif(sampleName=='/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM'):
        SAMPLE_ADD = '_TTJetsSemiLept_'

    elif(sampleName=='/TTJets_HadronicMGDecays_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A_ext-v1/AODSIM'):
        SAMPLE_ADD = '_TTJetsHadronic_'

    elif(sampleName=='/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_SingleTopBar_'

    elif(sampleName=='/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_SingleTop_'

    elif(sampleName=='/ZZJetsTo4L_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ZZJetsTo4L_'


    elif(sampleName=='/ZZJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v3/AODSIM'):
        SAMPLE_ADD = '_ZZJetsTo2L2Nu_'


#    elif(sampleName=='/ZZJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v3/AODSIM'):
#        SAMPLE_ADD = '_ZZJetsTo2L2Nu_'

    elif(sampleName=='/ZZJetsTo2L2Q_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ZZJetsTo2L2Q_'

    elif(sampleName=='/WWJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_WWJetsTo2L2Nu_'

    elif(sampleName=='/WZJetsTo2L2Q_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_WZJetsTo2L2Q_'

    elif(sampleName=='/WZJetsTo3LNu_TuneZ2_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_WZJetsTo3LNu_'
    elif(sampleName=='/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball-tauola-tauPolarOff/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
        SAMPLE_ADD = '_DYTauPolOff_'
    elif(sampleName=='/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM'):
        SAMPLE_ADD = '_WJetsToLNu_'
    elif(sampleName=='/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_WJetsToLNu_'
    elif(sampleName=='/W1JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_W1JetsToLNu_'
    elif(sampleName=='/W1JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
        SAMPLE_ADD = '_W1JetsToLNu_'
    elif(sampleName=='/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_W2JetsToLNu_'
    elif(sampleName=='/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
        SAMPLE_ADD = '_W2JetsToLNu_'
    elif(sampleName=='/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_W3JetsToLNu_'
    elif(sampleName=='/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
        SAMPLE_ADD = '_W3JetsToLNu_'
    elif(sampleName=='/W4JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_W4JetsToLNu_'
    elif(sampleName=='/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_qqH_SM125_'
    elif(sampleName=='/WH_ZH_TTH_HToTauTau_M-125_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_VH_SM125_'
    elif(sampleName=='/GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
        SAMPLE_ADD = '_ggH_SM125_'
    elif(sampleName=='/DoubleMu/StoreResults-Run2012A_22Jan2013_v1_PFembedded_trans1_tau115_ptelec1_20had1_18_v1-5ef1c0fd428eb740081f19333520fdc8/USER'):
        SAMPLE_ADD = '_embeddedZTT_'
    elif(sampleName=='/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau115_ptelec1_20had1_18_v1-5ef1c0fd428eb740081f19333520fdc8/USER'):
        SAMPLE_ADD = '_embeddedZTT_'
    elif(sampleName=='/DoubleMuParked/StoreResults-Run2012C_22Jan2013_v1_PFembedded_trans1_tau115_ptelec1_20had1_18_v1-5ef1c0fd428eb740081f19333520fdc8/USER'):
        SAMPLE_ADD = '_embeddedZTT_'
    elif(sampleName=='/DoubleMuParked/StoreResults-Run2012D_22Jan2013_v1_PFembedded_trans1_tau115_ptelec1_20had1_18_v1-5ef1c0fd428eb740081f19333520fdc8/USER'):
        SAMPLE_ADD = '_embeddedZTT_'
    elif(sampleName=='/DoubleMu/StoreResults-Run2012A_22Jan2013_v1_PFembedded_trans1_tau116_ptmu1_16had1_18_v1-5ef1c0fd428eb740081f19333520fdc8/USER'):
        SAMPLE_ADD = '_embeddedZTT_'
    elif(sampleName=='/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau116_ptmu1_16had1_18_v1-5ef1c0fd428eb740081f19333520fdc8/USER'):
        SAMPLE_ADD = '_embeddedZTT_'
    elif(sampleName=='/DoubleMuParked/StoreResults-Run2012C_22Jan2013_v1_PFembedded_trans1_tau116_ptmu1_16had1_18_v1-5ef1c0fd428eb740081f19333520fdc8/USER'):
        SAMPLE_ADD = '_embeddedZTT_'
    elif(sampleName=='/DoubleMuParked/StoreResults-Run2012D_22Jan2013_v1_PFembedded_trans1_tau116_ptmu1_16had1_18_v1-5ef1c0fd428eb740081f19333520fdc8/USER'):
        SAMPLE_ADD = '_embeddedZTT_'
    elif(sampleName=='/TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/StoreResults-Summer12_TTJets_FullLeptMGDecays_DR53X_PU_S10_START53_V7C_v2_PFembedded_trans1_tau115_ptelec1_20had1_18_v1-5ef1c0fd428eb740081f19333520fdc8/USER'):
        SAMPLE_ADD = '_embeddedTTbar_'
    elif(sampleName=='/TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/StoreResults-Summer12_TTJets_FullLeptMGDecays_DR53X_PU_S10_START53_V7C_v2_PFembedded_trans1_tau116_ptmu1_16had1_18_v1-5ef1c0fd428eb740081f19333520fdc8/USER'):
        SAMPLE_ADD = '_embeddedTTbar_'
    return SAMPLE_ADD











def muTauClassification_forQCD(chain, index):
  Tvec =  TLorentzVector(0,0,0,0)
  Tvec.SetXYZT(chain.muT_tau_corrected_p4_x[index], chain.muT_tau_corrected_p4_y[index], chain.muT_tau_corrected_p4_z[index],chain.muT_tau_corrected_p4_t[index])
  return btagAndTauPtCategory_forQCD(chain.muT_nbjets[index],Tvec.Pt(),chain.muT_njets[index],chain.muT_nbjetsLOOSE[index])

def eTauClassification_forQCD(chain, index):
  Tvec =  TLorentzVector(0,0,0,0)
  Tvec.SetXYZT(chain.eT_tau_corrected_p4_x[index], chain.eT_tau_corrected_p4_y[index], chain.eT_tau_corrected_p4_z[index],chain.eT_tau_corrected_p4_t[index])
  return btagAndTauPtCategory_forQCD(chain.eT_nbjets[index],Tvec.Pt(),chain.eT_njets[index],chain.eT_nbjetsLOOSE[index])




def muTauClassification(chain, index):
  Tvec =  TLorentzVector(0,0,0,0)
  Tvec.SetXYZT(chain.muT_tau_corrected_p4_x[index], chain.muT_tau_corrected_p4_y[index], chain.muT_tau_corrected_p4_z[index],chain.muT_tau_corrected_p4_t[index])
  return btagAndTauPtCategory(chain.muT_nbjets[index],Tvec.Pt(),chain.muT_njets[index])

def eTauClassification(chain, index):
  Tvec =  TLorentzVector(0,0,0,0)
  Tvec.SetXYZT(chain.eT_tau_corrected_p4_x[index], chain.eT_tau_corrected_p4_y[index], chain.eT_tau_corrected_p4_z[index],chain.eT_tau_corrected_p4_t[index])
  return btagAndTauPtCategory(chain.eT_nbjets[index],Tvec.Pt(),chain.eT_njets[index])


def muTauClassificationJECDOWN(chain, index):
  Tvec =  TLorentzVector(0,0,0,0)
  Tvec.SetXYZT(chain.muT_tau_corrected_p4_x[index], chain.muT_tau_corrected_p4_y[index], chain.muT_tau_corrected_p4_z[index],chain.muT_tau_corrected_p4_t[index])
  return btagAndTauPtCategory(chain.muT_nbjetsDOWN[index],Tvec.Pt(),chain.muT_njetsDOWN[index])

def eTauClassificationJECDOWN(chain, index):
  Tvec =  TLorentzVector(0,0,0,0)
  Tvec.SetXYZT(chain.eT_tau_corrected_p4_x[index], chain.eT_tau_corrected_p4_y[index], chain.eT_tau_corrected_p4_z[index],chain.eT_tau_corrected_p4_t[index])
  return btagAndTauPtCategory(chain.eT_nbjetsDOWN[index],Tvec.Pt(),chain.eT_njetsDOWN[index])


def muTauClassificationJECUP(chain, index):
  Tvec =  TLorentzVector(0,0,0,0)
  Tvec.SetXYZT(chain.muT_tau_corrected_p4_x[index], chain.muT_tau_corrected_p4_y[index], chain.muT_tau_corrected_p4_z[index],chain.muT_tau_corrected_p4_t[index])
  return btagAndTauPtCategory(chain.muT_nbjetsUP[index],Tvec.Pt(),chain.muT_njetsUP[index])

def eTauClassificationJECUP(chain, index):
  Tvec =  TLorentzVector(0,0,0,0)
  Tvec.SetXYZT(chain.eT_tau_corrected_p4_x[index], chain.eT_tau_corrected_p4_y[index], chain.eT_tau_corrected_p4_z[index],chain.eT_tau_corrected_p4_t[index])
  return btagAndTauPtCategory(chain.eT_nbjetsUP[index],Tvec.Pt(),chain.eT_njetsUP[index])


########
# jec variants under loose b-tag

def muTauClassificationJECDOWN_looseBtag(chain, index):
    Tvec =  TLorentzVector(0,0,0,0)
    Tvec.SetXYZT(chain.muT_tau_corrected_p4_x[index], chain.muT_tau_corrected_p4_y[index], chain.muT_tau_corrected_p4_z[index],chain.muT_tau_corrected_p4_t[index])
    return btagAndTauPtCategory_forQCD(chain.muT_nbjetsDOWN[index],Tvec.Pt(),chain.muT_njetsDOWN[index],chain.muT_nbjetsLOOSEDOWN[index])


def eTauClassificationJECDOWN_looseBtag(chain, index):
    Tvec =  TLorentzVector(0,0,0,0)
    Tvec.SetXYZT(chain.eT_tau_corrected_p4_x[index], chain.eT_tau_corrected_p4_y[index], chain.eT_tau_corrected_p4_z[index],chain.eT_tau_corrected_p4_t[index])
    return btagAndTauPtCategory_forQCD(chain.eT_nbjetsDOWN[index],Tvec.Pt(),chain.eT_njetsDOWN[index],chain.eT_nbjetsLOOSEDOWN[index])




def muTauClassificationJECUP_looseBtag(chain, index):
    Tvec =  TLorentzVector(0,0,0,0)
    Tvec.SetXYZT(chain.muT_tau_corrected_p4_x[index], chain.muT_tau_corrected_p4_y[index], chain.muT_tau_corrected_p4_z[index],chain.muT_tau_corrected_p4_t[index])
    return btagAndTauPtCategory_forQCD(chain.muT_nbjetsUP[index],Tvec.Pt(),chain.muT_njetsUP[index],chain.muT_nbjetsLOOSEUP[index])


def eTauClassificationJECUP_looseBtag(chain, index):
    Tvec =  TLorentzVector(0,0,0,0)
    Tvec.SetXYZT(chain.eT_tau_corrected_p4_x[index], chain.eT_tau_corrected_p4_y[index], chain.eT_tau_corrected_p4_z[index],chain.eT_tau_corrected_p4_t[index])
    return btagAndTauPtCategory_forQCD(chain.eT_nbjetsUP[index],Tvec.Pt(),chain.eT_njetsUP[index],chain.eT_nbjetsLOOSEUP[index])


####################
# classiffy Z->XX decays
# based on generator - recoTau matching

def classifyZDecay(chain,maxPairTypeAndIndex):
    classification = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    i=maxPairTypeAndIndex[0]
    ########################
    # check reco-gen matches
    tauMatches = {}
    tauMatches['genTau'] = False
    tauMatches['genLep'] = False
    tauMatches['lepFakesTau'] = False
    if maxPairTypeAndIndex[1] == 'muTau':
        if chain.muT_isDecayZtauTau[i] :
            if chain.muT_isRecoTau_matchedTo_GenTauFromZ[i] : tauMatches['genTau'] = True
            if chain.muT_isRecoTau_matchedTo_GenMuonFromTau[i] : tauMatches['genLep'] = True
            if tauMatches['genTau'] is True and tauMatches['genLep'] is False:
                classification = '_ZTT_'
                print 'found a ZTT in Z->tau tau'
            elif tauMatches['genTau'] is False and tauMatches['genLep'] is True:
                classification = '_ZL_'
                print 'found a ZL in Z->tau tau'
            elif tauMatches['genTau'] is False and tauMatches['genLep'] is False:
                classification = '_ZJ_'
                print 'found a ZJ in Z->tau tau'
            elif tauMatches['genTau'] is True and tauMatches['genLep'] is True:
                classification = '_X_'
                print 'found a X in Z->tau tau'
        elif chain.muT_isDecayZmuMu[i] :
            if chain.muT_isRecoTau_matchedTo_GenMuonFromZ[i]: tauMatches['lepFakesTau'] = True
            if tauMatches['lepFakesTau'] is True:
                classification = '_ZL_'
                print 'found a ZL in Z->mu mu'
            elif tauMatches['lepFakesTau'] is False:
                classification = '_ZJ_'
                print 'found a ZJ in Z->mu mu'

    elif maxPairTypeAndIndex[1] == 'eleTau':
        if chain.eT_isDecayZtauTau[i] :
            if chain.eT_isRecoTau_matchedTo_GenTauFromZ[i] : tauMatches['genTau'] = True
            if chain.eT_isRecoTau_matchedTo_GenElecFromTau[i] : tauMatches['genLep'] = True
            if tauMatches['genTau'] is True and tauMatches['genLep'] is False:
                classification = '_ZTT_'
                print 'found a ZTT in Z->tau tau'
            elif tauMatches['genTau'] is False and tauMatches['genLep'] is True:
                classification = '_ZL_'
                print 'found a ZL in Z->tau tau'
            elif tauMatches['genTau'] is False and tauMatches['genLep'] is False:
                classification = '_ZJ_'
                print 'found a ZJ in Z->tau tau'
            elif tauMatches['genTau'] is True and tauMatches['genLep'] is True:
                classification = '_X_'
                print 'found a X in Z->tau tau'
        elif chain.eT_isDecayZeE[i] :
            if chain.eT_isRecoTau_matchedTo_GenElecFromZ[i]: tauMatches['lepFakesTau'] = True
            if tauMatches['lepFakesTau'] is True:
                classification = '_ZL_'
                print 'found a ZL in Z->e e'
            elif tauMatches['lepFakesTau'] is False:
                classification = '_ZJ_'
                print 'found a ZJ in Z->e e'
    return classification

####################
# classiffy Z->XX decays
# based on generator - recoTau matching
# update based on email
#TRUE PROCESS  |        MATCHING
#              tau_h matches gen tau_h      tau_h matches gen e or mu    tau_h matches neither
#Z->tau tau    ZTT (*)                       ZTT                          ZJ
#Z->ll         --                            ZL                           ZJ


def classifyZDecay_Update(chain,maxPairTypeAndIndex):
    classification = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    i=maxPairTypeAndIndex[0]
    ########################
    # check reco-gen matches
    genInfo = {}
    genInfo['z->tau tau'] = False
    genInfo['z->l l'] = False
    genInfo['reco-genTau'] = False
    genInfo['reco-genLep'] = False
    if maxPairTypeAndIndex[1] == 'muTau':
        if chain.muT_isDecayZtauTau[i] :
            genInfo['z->tau tau'] = True
        elif chain.muT_isDecayZeE[i] or chain.muT_isDecayZmuMu[i] :
            genInfo['z->l l'] = True
        if chain.muT_isRecoTau_matchedTo_GenTauFromZ[i]:
            genInfo['reco-genTau'] = True
        elif (chain.muT_isRecoTau_matchedTo_GenElecFromZ[i]  or
            chain.muT_isRecoTau_matchedTo_GenMuonFromZ[i]   or
            chain.muT_isRecoTau_matchedTo_GenElecFromTau[i] or
            chain.muT_isRecoTau_matchedTo_GenMuonFromTau[i]   ) :
            genInfo['reco-genLep'] = True

    elif maxPairTypeAndIndex[1] == 'eleTau':
        if chain.eT_isDecayZtauTau[i] :
            genInfo['z->tau tau'] = True
        elif chain.eT_isDecayZeE[i] or chain.eT_isDecayZmuMu[i]:
            genInfo['z->l l'] = True
        if chain.eT_isRecoTau_matchedTo_GenTauFromZ[i]:
            genInfo['reco-genTau'] = True
        elif (chain.eT_isRecoTau_matchedTo_GenElecFromZ[i]  or
            chain.eT_isRecoTau_matchedTo_GenMuonFromZ[i]   or
            chain.eT_isRecoTau_matchedTo_GenElecFromTau[i] or
            chain.eT_isRecoTau_matchedTo_GenMuonFromTau[i]   ) :
            genInfo['reco-genLep'] = True

    if genInfo['z->tau tau'] :
        if genInfo['reco-genTau'] or genInfo['reco-genLep']:
            classification = '_ZTT_'
            print 'found a ZTT in Z->tau tau'
        else :
            classification = '_ZJ_'
            print 'found a ZJ in Z->tau tau'
    if genInfo['z->l l'] :
        if genInfo['reco-genLep'] :
            classification = '_ZL_'
            print 'found a ZL in Z->l l'
        else :
            classification = '_ZJ_'
            print 'found a ZJ in Z->l l'


    return classification

########################
# final version of this
# with corrections based on various
# discussions and emails




def classifyZDecay_Final(chain,maxPairTypeAndIndex):
    classification = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    i=maxPairTypeAndIndex[0]
    ########################
    # check reco-gen matches
    genInfo = {}
    genInfo['z->tau tau'] = False
    genInfo['z->l l'] = False
    genInfo['reco-match-genTau'] = False
    genInfo['reco-match-genLepFromZ'] = False
    genInfo['reco-match-genLepFromTau'] = False

    if maxPairTypeAndIndex[1] == 'muTau':
        if chain.muT_isDecayZtauTau[i] :
            genInfo['z->tau tau'] = True
        if chain.muT_isDecayZeE[i] or chain.muT_isDecayZmuMu[i] :
            genInfo['z->l l'] = True
        if chain.muT_isRecoTau_matchedTo_GenTauFromZ[i]:
            genInfo['reco-match-genTau'] = True
        if (chain.muT_isRecoTau_matchedTo_GenElecFromZ[i]  or
            chain.muT_isRecoTau_matchedTo_GenMuonFromZ[i] ):
            genInfo['reco-match-genLepFromZ'] = True
        if (chain.muT_isRecoTau_matchedTo_GenElecFromTau[i] or
            chain.muT_isRecoTau_matchedTo_GenMuonFromTau[i]   ) :
            genInfo['reco-match-genLepFromTau'] = True

    elif maxPairTypeAndIndex[1] == 'eleTau':
        if chain.eT_isDecayZtauTau[i] :
            genInfo['z->tau tau'] = True
        if chain.eT_isDecayZeE[i] or chain.eT_isDecayZmuMu[i] :
            genInfo['z->l l'] = True
        if chain.eT_isRecoTau_matchedTo_GenTauFromZ[i]:
            genInfo['reco-match-genTau'] = True
        if (chain.eT_isRecoTau_matchedTo_GenElecFromZ[i]  or
            chain.eT_isRecoTau_matchedTo_GenMuonFromZ[i] ):
            genInfo['reco-match-genLepFromZ'] = True
        if (chain.eT_isRecoTau_matchedTo_GenElecFromTau[i] or
            chain.eT_isRecoTau_matchedTo_GenMuonFromTau[i]   ) :
            genInfo['reco-match-genLepFromTau'] = True

    if genInfo['z->tau tau']:
        if genInfo['reco-match-genLepFromTau']:
            classification = '_ZL_'
            print 'found a ZL in Z->Tau Tau'
        elif genInfo['reco-match-genTau']:
            classification = '_ZTT_'
            print 'found a ZTT in Z->Tau Tau'
        else:
            classification = '_ZJ_'
            print 'found a ZJ in Z->Tau Tau'

    elif genInfo['z->l l']:
        if genInfo['reco-match-genLepFromTau']:
            classification = '_ZL_'
            print 'found a ZL in Z->l l'
        elif genInfo['reco-match-genLepFromZ']:
            classification = '_ZL_'
            print 'found a ZL in Z->l l'
        else:
            classification = '_ZJ_'
            print 'found a ZJ in Z->l l'

    return classification
