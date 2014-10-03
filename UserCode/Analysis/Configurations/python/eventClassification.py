import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile


def btagAndTauPtCategory(nbtags, tauPt):
  returnWord = ''
  if nbtags == 0:
    returnWord = 'noBTAG'
    if tauPt <= 30:
      print tauPt
      returnWord += '-ForgotToCorrectTauPt?'
    elif tauPt > 30 and tauPt <= 45:
      returnWord += '-LOW'
    elif tauPt > 45 and tauPt <= 60:
      returnWord += '-MEDIUM'
    elif tauPt > 60:
      returnWord += '-HIGH'
  else:
    returnWord = 'BTAG'
    if tauPt <= 30:
      print tauPt
      returnWord += '-ForgotToCorrectTauPt?'
    elif tauPt > 30 and tauPt <= 45:
      returnWord += '-LOW'
    elif tauPt > 45:
      returnWord += '-HIGH'
  return returnWord




def muTauClassification(chain, index):
  Tvec =  TLorentzVector(0,0,0,0)
  Tvec.SetXYZT(chain.muT_tau_corrected_p4_x[index], chain.muT_tau_corrected_p4_y[index], chain.muT_tau_corrected_p4_z[index],chain.muT_tau_corrected_p4_t[index])
  return btagAndTauPtCategory(chain.muT_nbjets[index],Tvec.Pt())

def eTauClassification(chain, index):
  Tvec =  TLorentzVector(0,0,0,0)
  Tvec.SetXYZT(chain.eT_tau_corrected_p4_x[index], chain.eT_tau_corrected_p4_y[index], chain.eT_tau_corrected_p4_z[index],chain.eT_tau_corrected_p4_t[index])
  return btagAndTauPtCategory(chain.eT_nbjets[index],Tvec.Pt())
