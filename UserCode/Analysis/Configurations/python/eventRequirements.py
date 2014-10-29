import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile



def pairCutsMuTau(chain, index, verbose):
  returnVal = True
  failChain = {}
  passChain = {}
  eventPar = {}
  eventPar['sumCharge'] = chain.muT_sumCharge[index]
  if chain.muT_sumCharge[index] != 0:
    returnVal = False
    failChain['sumCharge'] = False
  else:
    passChain['sumCharge'] = True
  eventPar['DR'] = chain.muT_DR[index]
  if chain.muT_DR[index] <= 0.5:
    returnVal = False
    failChain['DR'] = False
  else:
    passChain['DR'] = True
  eventPar['TransverseMass'] = chain.muT_TransverseMass[index]
  if chain.muT_TransverseMass[index] > 30.00:
    returnVal = False
    failChain['TransverseMass'] = False
  else:
    passChain['TransverseMass'] = True
  eventPar['passesThirdLeptonVeto'] = chain.muT_passesThirdLeptonVeto[index]
  if chain.muT_passesThirdLeptonVeto[index] is not True:
    returnVal = False
    failChain['passesThirdLeptonVeto'] = False
  else:
    passChain['passesThirdLeptonVeto'] = True
  eventPar['passesSecondLeptonVeto'] = chain.muT_passesSecondLeptonVeto[index]
  if chain.muT_passesSecondLeptonVeto[index] is not True:
    returnVal = False
    failChain['passesSecondLeptonVeto'] = False
  else:
    passChain['passesSecondLeptonVeto'] = True
  if verbose:
    print 'eventCuts', eventPar
    if len(passChain) > 0:
      print "passed cuts = ",passChain
    if len(failChain) > 0:
      print "failed cuts = ",failChain
  return returnVal

def pairCutsETau(chain, index, verbose):
  returnVal = True
  failChain = {}
  passChain = {}
  eventPar = {}
  eventPar['sumCharge'] = chain.eT_sumCharge[index]
  if chain.eT_sumCharge[index] != 0:
    returnVal = False
    failChain['sumCharge'] = False
  else:
    passChain['sumCharge'] = True
  eventPar['DR'] = chain.eT_DR[index]
  if chain.eT_DR[index] <= 0.5:
    returnVal = False
    failChain['DR'] = False
  else:
    passChain['DR'] = True
  eventPar['TransverseMass'] = chain.eT_TransverseMass[index]
  if chain.eT_TransverseMass[index] > 30.00:
    returnVal = False
    failChain['TransverseMass'] = False
  else:
    passChain['TransverseMass'] = True
  eventPar['passesThirdLeptonVeto'] = chain.eT_passesThirdLeptonVeto[index]
  if chain.eT_passesThirdLeptonVeto[index] is not True:
    returnVal = False
    failChain['passesThirdLeptonVeto'] = False
  else:
    passChain['passesThirdLeptonVeto'] = True
  eventPar['passesSecondLeptonVeto'] = chain.eT_passesSecondLeptonVeto[index]
  if chain.eT_passesSecondLeptonVeto[index] is not True:
    returnVal = False
    failChain['passesSecondLeptonVeto'] = False
  else:
    passChain['passesSecondLeptonVeto'] = True
  if verbose:
    if len(passChain) > 0:
      print "passed cuts = ",passChain
    if len(failChain) > 0:
      print "failed cuts = ",failChain
  return returnVal


###########
# for high Mt



def pairCutsMuTau_forHighMt(chain, index, verbose):
  returnVal = True
  failChain = {}
  passChain = {}
  eventPar = {}
  eventPar['sumCharge'] = chain.muT_sumCharge[index]
  if chain.muT_sumCharge[index] != 0:
    returnVal = False
    failChain['sumCharge'] = False
  else:
    passChain['sumCharge'] = True
  eventPar['DR'] = chain.muT_DR[index]
  if chain.muT_DR[index] <= 0.5:
    returnVal = False
    failChain['DR'] = False
  else:
    passChain['DR'] = True
  eventPar['TransverseMass'] = chain.muT_TransverseMass[index]
  if chain.muT_TransverseMass[index] < 70.00:
    returnVal = False
    failChain['TransverseMass'] = False
  else:
    passChain['TransverseMass'] = True
  eventPar['passesThirdLeptonVeto'] = chain.muT_passesThirdLeptonVeto[index]
  if chain.muT_passesThirdLeptonVeto[index] is not True:
    returnVal = False
    failChain['passesThirdLeptonVeto'] = False
  else:
    passChain['passesThirdLeptonVeto'] = True
  eventPar['passesSecondLeptonVeto'] = chain.muT_passesSecondLeptonVeto[index]
  if chain.muT_passesSecondLeptonVeto[index] is not True:
    returnVal = False
    failChain['passesSecondLeptonVeto'] = False
  else:
    passChain['passesSecondLeptonVeto'] = True
  if verbose:
    print 'eventCuts', eventPar
    if len(passChain) > 0:
      print "passed cuts = ",passChain
    if len(failChain) > 0:
      print "failed cuts = ",failChain
  return returnVal

def pairCutsETau_forHighMt(chain, index, verbose):
  returnVal = True
  failChain = {}
  passChain = {}
  eventPar = {}
  eventPar['sumCharge'] = chain.eT_sumCharge[index]
  if chain.eT_sumCharge[index] != 0:
    returnVal = False
    failChain['sumCharge'] = False
  else:
    passChain['sumCharge'] = True
  eventPar['DR'] = chain.eT_DR[index]
  if chain.eT_DR[index] <= 0.5:
    returnVal = False
    failChain['DR'] = False
  else:
    passChain['DR'] = True
  eventPar['TransverseMass'] = chain.eT_TransverseMass[index]
  if chain.eT_TransverseMass[index] < 70.00:
    returnVal = False
    failChain['TransverseMass'] = False
  else:
    passChain['TransverseMass'] = True
  eventPar['passesThirdLeptonVeto'] = chain.eT_passesThirdLeptonVeto[index]
  if chain.eT_passesThirdLeptonVeto[index] is not True:
    returnVal = False
    failChain['passesThirdLeptonVeto'] = False
  else:
    passChain['passesThirdLeptonVeto'] = True
  eventPar['passesSecondLeptonVeto'] = chain.eT_passesSecondLeptonVeto[index]
  if chain.eT_passesSecondLeptonVeto[index] is not True:
    returnVal = False
    failChain['passesSecondLeptonVeto'] = False
  else:
    passChain['passesSecondLeptonVeto'] = True
  if verbose:
    if len(passChain) > 0:
      print "passed cuts = ",passChain
    if len(failChain) > 0:
      print "failed cuts = ",failChain
  return returnVal


###########
# for QCD

def pairCutsMuTau_forQCD(chain, index, verbose):
    returnVal = True
    failChain = {}
    passChain = {}
    eventPar = {}
    eventPar['sumCharge'] = chain.muT_sumCharge[index]
    if abs(chain.muT_sumCharge[index]) != 2:
        returnVal = False
        failChain['sumCharge'] = False
    else:
        passChain['sumCharge'] = True
    eventPar['DR'] = chain.muT_DR[index]
    if chain.muT_DR[index] <= 0.5:
        returnVal = False
        failChain['DR'] = False
    else:
        passChain['DR'] = True
    eventPar['TransverseMass'] = chain.muT_TransverseMass[index]
    if chain.muT_TransverseMass[index] > 30.00:
        returnVal = False
        failChain['TransverseMass'] = False
    else:
        passChain['TransverseMass'] = True
    eventPar['passesThirdLeptonVeto'] = chain.muT_passesThirdLeptonVeto[index]
    if chain.muT_passesThirdLeptonVeto[index] is not True:
        returnVal = False
        failChain['passesThirdLeptonVeto'] = False
    else:
        passChain['passesThirdLeptonVeto'] = True
    eventPar['passesSecondLeptonVeto'] = chain.muT_passesSecondLeptonVeto[index]
    if chain.muT_passesSecondLeptonVeto[index] is not True:
        returnVal = False
        failChain['passesSecondLeptonVeto'] = False
    else:
        passChain['passesSecondLeptonVeto'] = True
    if verbose:
        print 'eventCuts', eventPar
        if len(passChain) > 0:
            print "passed cuts = ",passChain
        if len(failChain) > 0:
            print "failed cuts = ",failChain
    return returnVal

def pairCutsETau_forQCD(chain, index, verbose):
    returnVal = True
    failChain = {}
    passChain = {}
    eventPar = {}
    eventPar['sumCharge'] = chain.eT_sumCharge[index]
    if abs(chain.eT_sumCharge[index]) != 2:
        returnVal = False
        failChain['sumCharge'] = False
    else:
        passChain['sumCharge'] = True
    eventPar['DR'] = chain.eT_DR[index]
    if chain.eT_DR[index] <= 0.5:
        returnVal = False
        failChain['DR'] = False
    else:
        passChain['DR'] = True
    eventPar['TransverseMass'] = chain.eT_TransverseMass[index]
    if chain.eT_TransverseMass[index] > 30.00:
        returnVal = False
        failChain['TransverseMass'] = False
    else:
        passChain['TransverseMass'] = True
    eventPar['passesThirdLeptonVeto'] = chain.eT_passesThirdLeptonVeto[index]
    if chain.eT_passesThirdLeptonVeto[index] is not True:
        returnVal = False
        failChain['passesThirdLeptonVeto'] = False
    else:
        passChain['passesThirdLeptonVeto'] = True
    eventPar['passesSecondLeptonVeto'] = chain.eT_passesSecondLeptonVeto[index]
    if chain.eT_passesSecondLeptonVeto[index] is not True:
        returnVal = False
        failChain['passesSecondLeptonVeto'] = False
    else:
        passChain['passesSecondLeptonVeto'] = True
    if verbose:
        if len(passChain) > 0:
            print "passed cuts = ",passChain
        if len(failChain) > 0:
            print "failed cuts = ",failChain
    return returnVal






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
      maxPairTypeAndIndex.append('muTau')
  for index in passingETauIndices:
    if chain.eT_scalarSumPt[index] > currentMaxPt:
      del maxPairTypeAndIndex[:]
      currentMaxPt = chain.eT_scalarSumPt[index]
      maxPairTypeAndIndex.append(index)
      maxPairTypeAndIndex.append('eleTau')
  return
