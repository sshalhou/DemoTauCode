import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile



def tauID_eTau(chain, index, printCutValues):
  returnVal = True
  failChain = {}
  passChain = {}
  tau = {}
  Lvec = TLorentzVector(0,0,0,0)
  Lvec.SetXYZT(chain.eT_tau_corrected_p4_x[index], chain.eT_tau_corrected_p4_y[index], chain.eT_tau_corrected_p4_z[index],chain.eT_tau_corrected_p4_t[index])
  Lvec = Lvec
  tau['pt'] = Lvec.Pt()
  if (Lvec.Pt()>30) is False:
    returnVal = False
    failChain['pt'] = False
  else:
    passChain['pt'] = True

  tau['eta'] = Lvec.Eta()
  if (abs(Lvec.Eta())<2.3) is False:
    returnVal = False
    failChain['eta'] = False
  else:
    passChain['eta'] = True

  tau['byTightIsolationMVA3oldDMwLT'] = chain.eT_tau_byTightIsolationMVA3oldDMwLT[index]
  if chain.eT_tau_byTightIsolationMVA3oldDMwLT[index] <= 0.5:
    returnVal = False
    failChain['byTightIsolationMVA3oldDMwLT'] = False
  else:
    passChain['byTightIsolationMVA3oldDMwLT'] = True

  tau['decayModeFindingOldDMs'] = chain.eT_tau_decayModeFindingOldDMs[index]
  if chain.eT_tau_decayModeFindingOldDMs[index] <= 0.5:
    returnVal = False
    failChain['decayModeFindingOldDMs'] = False
  else:
    passChain['decayModeFindingOldDMs'] = True

  tau['againstElectronMediumMVA5'] = chain.eT_tau_againstElectronMediumMVA5[index]
  if chain.eT_tau_againstElectronMediumMVA5[index] <= 0.5:
    returnVal = False
    failChain['againstElectronMediumMVA5'] = False
  else:
    passChain['againstElectronMediumMVA5'] = True

  tau['againstMuonLoose3'] = chain.eT_tau_againstMuonLoose3[index]
  if chain.eT_tau_againstMuonLoose3[index] <= 0.5:
    returnVal = False
    failChain['againstMuonLoose3'] = False
  else:
    passChain['againstMuonLoose3'] = True


  if printCutValues:
    print "-------------------------------------------"
    print "tau ", tau
    if len(passChain) > 0:
      print "passed cuts = ",passChain
    if len(failChain) > 0:
      print "failed cuts = ",failChain

  return returnVal




def tauID_muTau(chain, index, printCutValues):
  returnVal = True
  failChain = {}
  passChain = {}
  tau = {}
  Lvec = TLorentzVector(0,0,0,0)
  Lvec.SetXYZT(chain.muT_tau_corrected_p4_x[index], chain.muT_tau_corrected_p4_y[index], chain.muT_tau_corrected_p4_z[index],chain.muT_tau_corrected_p4_t[index])

  tau['pt'] = Lvec.Pt()
  if (Lvec.Pt()>30) is False:
    returnVal = False
    failChain['pt'] = False
  else:
    passChain['pt'] = True

  tau['eta'] = Lvec.Eta()
  if (abs(Lvec.Eta())<2.3) is False:
    returnVal = False
    failChain['eta'] = False
  else:
    passChain['eta'] = True

  tau['byTightIsolationMVA3oldDMwLT'] = chain.muT_tau_byTightIsolationMVA3oldDMwLT[index]
  if chain.muT_tau_byTightIsolationMVA3oldDMwLT[index] <= 0.5:
    returnVal = False
    failChain['byTightIsolationMVA3oldDMwLT'] = False
  else:
    passChain['byTightIsolationMVA3oldDMwLT'] = True

  tau['decayModeFindingOldDMs'] = chain.muT_tau_decayModeFindingOldDMs[index]
  if chain.muT_tau_decayModeFindingOldDMs[index] <= 0.5:
    returnVal = False
    failChain['decayModeFindingOldDMs'] = False
  else:
    passChain['decayModeFindingOldDMs'] = True

  tau['againstMuonMediumMVA'] = chain.muT_tau_againstMuonMediumMVA[index]
  if chain.muT_tau_againstMuonMediumMVA[index] <= 0.5:
    returnVal = False
    failChain['againstMuonMediumMVA'] = False
  else:
    passChain['againstMuonMediumMVA'] = True

  tau['againstElectronLoose'] = chain.muT_tau_againstElectronLoose[index]
  if chain.muT_tau_againstElectronLoose[index] <= 0.5:
    returnVal = False
    failChain['againstElectronLoose'] = False
  else:
    passChain['againstElectronLoose'] = True


  if printCutValues:
    print "-------------------------------------------"
    print "tau ", tau
    if len(passChain) > 0:
      print "passed cuts = ",passChain
    if len(failChain) > 0:
      print "failed cuts = ",failChain

  return returnVal
