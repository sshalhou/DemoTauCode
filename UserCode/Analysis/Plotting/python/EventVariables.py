import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile



def resetVariables(eventVar):
  eventVar['SVFitMass'] = -999.0
  eventVar['VisibleMass'] = -999.0
  eventVar['MVAmet'] = -999.0
  eventVar['Mt'] = -999.0
  eventVar['leptonPt'] = -999.0
  eventVar['tauPt'] = -999.0
  eventVar['leptonD0'] = -999.0
  eventVar['leptonDZ'] = -999.0
  eventVar['leptonIso'] = -999.0
  eventVar['numberOfJets'] = -999.0
  eventVar['numberOfBTaggedJets'] = -999.0
  eventVar['jet1Pt'] = -999.0
  eventVar['jet2Pt'] = -999.0
  return

def fillVariables(chain,eventVar,maxPairTypeAndIndex,Verbose):
  resetVariables(eventVar)
  pairType = maxPairTypeAndIndex[1].split('-')
  if pairType[0] == 'muonTau':
    fillVariablesMuTau(chain,eventVar,maxPairTypeAndIndex,Verbose)
  elif pairType[0] == 'electronTau':
    fillVariablesETau(chain,eventVar,maxPairTypeAndIndex,Verbose)
  return

def fillVariablesETau(chain,eventVar,maxPairTypeAndIndex,Verbose):
  index = maxPairTypeAndIndex[0]
  Tvec = TLorentzVector(0,0,0,0)
  Tvec.SetXYZT(chain.eT_tau_corrected_p4_x[index], chain.eT_tau_corrected_p4_y[index], chain.eT_tau_corrected_p4_z[index],chain.eT_tau_corrected_p4_t[index])
  Lvec = TLorentzVector(0,0,0,0)
  Lvec.SetXYZT(chain.eT_ele_p4_x[index], chain.eT_ele_p4_y[index], chain.eT_ele_p4_z[index],chain.eT_ele_p4_t[index])
  Jvec1 = TLorentzVector(0,0,0,0)
  Jvec1.SetXYZT(chain.eT_jet1P4_x[index],chain.eT_jet1P4_y[index],chain.eT_jet1P4_z[index],chain.eT_jet1P4_t[index])
  Jvec2 = TLorentzVector(0,0,0,0)
  Jvec2.SetXYZT(chain.eT_jet2P4_x[index],chain.eT_jet2P4_y[index],chain.eT_jet2P4_z[index],chain.eT_jet2P4_t[index])
  eventVar['SVFitMass'] = chain.eT_correctedSVFitMass[index]
  eventVar['VisibleMass'] = (Lvec+Tvec).M()
  eventVar['MVAmet'] = chain.eT_mvaMET[index]
  eventVar['Mt'] = chain.eT_TransverseMass[index]
  eventVar['leptonPt'] = Lvec.Pt()
  eventVar['tauPt'] = Tvec.Pt()
  eventVar['leptonD0'] = chain.eT_ele_dxy[index]
  eventVar['leptonDZ'] = chain.eT_ele_dz[index]
  eventVar['leptonIso'] = chain.eT_ele_relativeIso[index]
  eventVar['numberOfJets'] = chain.eT_njets[index]
  eventVar['numberOfBTaggedJets'] = chain.eT_nbjets[index]
  eventVar['jet1Pt'] = Jvec1.Pt()
  eventVar['jet2Pt'] = Jvec2.Pt()
  if Verbose:
    print eventVar
  return


def fillVariablesMuTau(chain,eventVar,maxPairTypeAndIndex,Verbose):
  index = maxPairTypeAndIndex[0]
  Tvec = TLorentzVector(0,0,0,0)
  Tvec.SetXYZT(chain.muT_tau_corrected_p4_x[index], chain.muT_tau_corrected_p4_y[index], chain.muT_tau_corrected_p4_z[index],chain.muT_tau_corrected_p4_t[index])
  Lvec = TLorentzVector(0,0,0,0)
  Lvec.SetXYZT(chain.muT_muon_p4_x[index], chain.muT_muon_p4_y[index], chain.muT_muon_p4_z[index],chain.muT_muon_p4_t[index])
  Jvec1 = TLorentzVector(0,0,0,0)
  Jvec1.SetXYZT(chain.muT_jet1P4_x[index],chain.muT_jet1P4_y[index],chain.muT_jet1P4_z[index],chain.muT_jet1P4_t[index])
  Jvec2 = TLorentzVector(0,0,0,0)
  Jvec2.SetXYZT(chain.muT_jet2P4_x[index],chain.muT_jet2P4_y[index],chain.muT_jet2P4_z[index],chain.muT_jet2P4_t[index])
  eventVar['SVFitMass'] = chain.muT_correctedSVFitMass[index]
  eventVar['VisibleMass'] = (Lvec+Tvec).M()
  eventVar['MVAmet'] = chain.muT_mvaMET[index]
  eventVar['Mt'] = chain.muT_TransverseMass[index]
  eventVar['leptonPt'] = Lvec.Pt()
  eventVar['tauPt'] = Tvec.Pt()
  eventVar['leptonD0'] = chain.muT_muon_dxy[index]
  eventVar['leptonDZ'] = chain.muT_muon_dz[index]
  eventVar['leptonIso'] = chain.muT_muon_relativeIso_DR4[index]
  eventVar['numberOfJets'] = chain.muT_njets[index]
  eventVar['numberOfBTaggedJets'] = chain.muT_nbjets[index]
  eventVar['jet1Pt'] = Jvec1.Pt()
  eventVar['jet2Pt'] = Jvec2.Pt()
  if Verbose:
    print eventVar
  return
