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
  returnWord = ''
  if btags == 0:
    returnWord = 'nobtag'
    if tauPt <= 30:
      print tauPt
      returnWord += '-ForgotToCorrectTauPt?'
    elif tauPt > 30 and tauPt <= 45:
      returnWord += '_low'
    elif tauPt > 45 and tauPt <= 60:
      returnWord += '_medium'
    elif tauPt > 60:
      returnWord += '_high'
  elif njets<2 and btagsLooseCSV>0:
    returnWord = 'btag'
    if tauPt <= 30:
      print tauPt
      returnWord += '-ForgotToCorrectTauPt?'
    elif tauPt > 30 and tauPt <= 45:
      returnWord += '_low'
    elif tauPt > 45:
      returnWord += '_high'
  else:
    returnWord = 'Reject'
  return returnWord


def btagAndTauPtCategory(btags, tauPt, njets):
  returnWord = ''
  if btags == 0:
    returnWord = 'nobtag'
    if tauPt <= 30:
      print tauPt
      returnWord += '-ForgotToCorrectTauPt?'
    elif tauPt > 30 and tauPt <= 45:
      returnWord += '_low'
    elif tauPt > 45 and tauPt <= 60:
      returnWord += '_medium'
    elif tauPt > 60:
      returnWord += '_high'
  elif njets<2:
    returnWord = 'btag'
    if tauPt <= 30:
      print tauPt
      returnWord += '-ForgotToCorrectTauPt?'
    elif tauPt > 30 and tauPt <= 45:
      returnWord += '_low'
    elif tauPt > 45:
      returnWord += '_high'
  else:
    returnWord = 'Reject'
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
    elif(sampleName=='/SUSYBBHToTauTau_M-300_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'):
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
