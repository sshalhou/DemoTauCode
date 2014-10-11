import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile


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




def muTauClassification(chain, index):
  Tvec =  TLorentzVector(0,0,0,0)
  Tvec.SetXYZT(chain.muT_tau_corrected_p4_x[index], chain.muT_tau_corrected_p4_y[index], chain.muT_tau_corrected_p4_z[index],chain.muT_tau_corrected_p4_t[index])
  return btagAndTauPtCategory(chain.muT_nbjets[index],Tvec.Pt(),chain.muT_njets[index])

def eTauClassification(chain, index):
  Tvec =  TLorentzVector(0,0,0,0)
  Tvec.SetXYZT(chain.eT_tau_corrected_p4_x[index], chain.eT_tau_corrected_p4_y[index], chain.eT_tau_corrected_p4_z[index],chain.eT_tau_corrected_p4_t[index])
  return btagAndTauPtCategory(chain.eT_nbjets[index],Tvec.Pt(),chain.eT_njets[index])
