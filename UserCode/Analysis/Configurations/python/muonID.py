import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile



def muonID(chain, index, printCutValues):
  returnVal = True
  failChain = {}
  passChain = {}
  muon = {}
  Lvec = TLorentzVector(0,0,0,0)
  Lvec.SetXYZT(chain.muT_muon_p4_x[index], chain.muT_muon_p4_y[index], chain.muT_muon_p4_z[index],chain.muT_muon_p4_t[index])

  muon['pt'] = Lvec.Pt()
  if (Lvec.Pt()>20) is False:
    returnVal = False
    failChain['pt'] = False
  else:
    passChain['pt'] = True

  muon['eta'] = Lvec.Eta()
  if (abs(Lvec.Eta())<2.1) is False:
    returnVal = False
    failChain['eta'] = False
  else:
    passChain['eta'] = True

  muon['isGlobal'] = chain.muT_muon_isGlobalMuon[index]
  if chain.muT_muon_isGlobalMuon[index] is False:
    returnVal = False
    failChain['isGlobal'] = False
  else:
    passChain['isGlobal'] = True

  muon['isTight'] = chain.muT_muon_isTightMuon[index]
  if chain.muT_muon_isTightMuon[index] is False:
    returnVal = False
    failChain['isTight'] = False
  else:
    passChain['isTight'] = True

  muon['isPF'] = chain.muT_muon_isPFMuon[index]
  if chain.muT_muon_isPFMuon[index] is False:
    returnVal = False
    failChain['isPF'] = False
  else:
    passChain['isPF'] = True

  muon['relativeIso'] = chain.muT_muon_relativeIso_DR4[index]
  if (chain.muT_muon_relativeIso_DR4[index]<0.1) is False:
    returnVal = False
    failChain['relativeIso'] = False
  else:
    passChain['relativeIso'] = True

  muon['dxy'] = chain.muT_muon_dxy[index]
  if (abs(chain.muT_muon_dxy[index])<0.045) is False:
    returnVal = False
    failChain['dxy'] = False
  else:
    passChain['dxy'] = True

  muon['dz'] = chain.muT_muon_dz[index]
  if (abs(chain.muT_muon_dz[index])<0.2) is False:
    returnVal = False
    failChain['dz'] = False
  else:
    passChain['dz'] = True

  if printCutValues:
    print "-------------------------------------------"
    print "muon ", muon
    if len(passChain) > 0:
      print "passed cuts = ",passChain
    if len(failChain) > 0:
      print "failed cuts = ",failChain

  return returnVal;
