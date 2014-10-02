import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile



def pairCutsMuTau(chain, index, verbose):
  returnVal = True
  failChain = {}
  passChain = {}
  if chain.muT_sumCharge[index] != 0:
    returnVal = False
    failChain['sumCharge'] = False
  else:
    passChain['sumCharge'] = True

  if chain.muT_DR[index] <= 0.5:
    returnVal = False
    failChain['DR'] = False
  else:
    passChain['DR'] = True

  if chain.muT_passesTriLeptonVeto[index] is not True:
    returnVal = False
    failChain['passesTriLeptonVeto'] = False
  else:
    passChain['passesTriLeptonVeto'] = True
  if verbose:
    if len(passChain) > 0:
      print "passed cuts = ",passChain
    if len(failChain) > 0:
      print "failed cuts = ",failChain
  return returnVal;

def pairCutsETau(chain, index, verbose):
  returnVal = True
  failChain = {}
  passChain = {}
  if chain.eT_sumCharge[index] != 0:
    returnVal = False
    failChain['sumCharge'] = False
  else:
    passChain['sumCharge'] = True

  if chain.eT_DR[index] <= 0.5:
    returnVal = False
    failChain['DR'] = False
  else:
    passChain['DR'] = True

  if chain.eT_passesTriLeptonVeto[index] is not True:
    returnVal = False
    failChain['passesTriLeptonVeto'] = False
  else:
    passChain['passesTriLeptonVeto'] = True
  if verbose:
    if len(passChain) > 0:
      print "passed cuts = ",passChain
    if len(failChain) > 0:
      print "failed cuts = ",failChain
  return returnVal;


##############
# in cases with
# multiple good H candidates
# find the maxPt pair

def getMaxPtPairIndex(chain, maxPairTypeAndIndex, passingMuTauIndices, passingETauIndices):
  currentMaxPt = -999.
  for index in passingMuTauIndices:
    if chain.muT_scalarSumPt[index] > currentMaxPt:
      currentMaxPt = chain.muT_scalarSumPt[index]
      del maxPairTypeAndIndex[:]
      maxPairTypeAndIndex.append(index)
      maxPairTypeAndIndex.append('muonTau')
  for index in passingETauIndices:
    if chain.eT_scalarSumPt[index] > currentMaxPt:
      del maxPairTypeAndIndex[:]
      currentMaxPt = chain.eT_scalarSumPt[index]
      maxPairTypeAndIndex.append(index)
      maxPairTypeAndIndex.append('electronTau')
  return
