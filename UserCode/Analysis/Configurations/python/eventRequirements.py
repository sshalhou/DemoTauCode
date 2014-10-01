import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile



def muonTrigger(chain, index, useNewTriggers):
  returnVal = False
  if chain.muT_muon_has_HltMatchMu17[index] is True:
    returnVal = True
  if chain.muT_muon_has_HltMatchMu18[index] is True:
    returnVal = True
  if chain.muT_muon_has_HltMatchMu24[index] is True and useNewTriggers is True:
    returnVal = True
  return returnVal;
