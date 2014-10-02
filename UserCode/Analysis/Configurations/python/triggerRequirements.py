import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile


def embeddedZTauTauTrigForETau(chain, index, Verbose):
  returnVal = False
  if Verbose:
    print 'checking passNonTopEmbeddedTriggerAndMass50 returns ', chain.eT_passNonTopEmbeddedTriggerAndMass50[index]
  if chain.eT_passNonTopEmbeddedTriggerAndMass50[index] is True:
    returnVal = True
  return returnVal;

def embeddedZTauTauTrigForMuTau(chain, index, Verbose):
  returnVal = False
  if Verbose:
    print 'checking passNonTopEmbeddedTriggerAndMass50 returns ', chain.muT_passNonTopEmbeddedTriggerAndMass50[index]
  if chain.muT_passNonTopEmbeddedTriggerAndMass50[index] is True:
    returnVal = True
  return returnVal;

def muonTrigger(chain, index, useNewTriggers):
  returnVal = False
  if chain.muT_muon_has_HltMatchMu17[index] is True:
    returnVal = True
  if chain.muT_muon_has_HltMatchMu18[index] is True:
    returnVal = True
  if chain.muT_muon_has_HltMatchMu24[index] is True and useNewTriggers is True:
    returnVal = True
  return returnVal;

def tauTriggerForMuTau(chain, index, useNewTriggers):
  returnVal = False
  if chain.muT_tau_has_HltMatchMu17[index] is True:
    returnVal = True
  if chain.muT_tau_has_HltMatchMu18[index] is True:
    returnVal = True
  if chain.muT_tau_has_HltMatchMu24[index] is True and useNewTriggers is True:
    returnVal = True
  return returnVal;

def electronTrigger(chain, index, useNewTriggers):
  returnVal = False
  if chain.eT_ele_has_HltMatchEle20[index] is True:
    returnVal = True
  if chain.eT_ele_has_HltMatchEle22[index] is True:
    returnVal = True
  if chain.eT_ele_has_HltMatchEle27[index] is True and useNewTriggers is True:
    returnVal = True
  return returnVal;

def tauTriggerForETau(chain, index, useNewTriggers):
  returnVal = False
  if chain.eT_tau_has_HltMatchEle20[index] is True:
    returnVal = True
  if chain.eT_tau_has_HltMatchEle22[index] is True:
    returnVal = True
  if chain.eT_tau_has_HltMatchEle27[index] is True and useNewTriggers is True:
    returnVal = True
  return returnVal;
