import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile,TMath



def tauID_eTau(chain, index, printCutValues):
  returnVal = True
  failChain = {}
  passChain = {}
  tau = {}
  Lvec = TLorentzVector(0,0,0,0)
  Lvec.SetXYZT(chain.eT_tau_corrected_p4_x[index], chain.eT_tau_corrected_p4_y[index], chain.eT_tau_corrected_p4_z[index],chain.eT_tau_corrected_p4_t[index])
  tau['pt'] = Lvec.Pt()
  if (Lvec.Pt()>20) is False:
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

  VtxZ = chain.eT_PVpositionZ[index]
  theta = Lvec.Theta()
  tanTheta = TMath.tan(theta)
  tau['ZimpactTau'] = 0.51
  if tanTheta != 0:
    tau['ZimpactTau'] = VtxZ + 130.0/( tanTheta )
  if (tau['ZimpactTau'] < -1.5 or tau['ZimpactTau'] > 0.5) is False :
    returnVal = False
    failChain['ZimpactTau'] = False
  else:
    passChain['ZimpactTau'] = True  



  tau['tauAbsDZ'] = abs(chain.eT_tau_vertex_z[index] - chain.eT_PVpositionZ[index])
  if tau['tauAbsDZ'] > 0.2:
    returnVal = False
    failChain['tauAbsDZ'] = False
  else:
    passChain['tauAbsDZ'] = True


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
  if (Lvec.Pt()>20) is False:
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

  tau['tauAbsDZ'] = abs(chain.muT_tau_vertex_z[index] - chain.muT_PVpositionZ[index])
  if tau['tauAbsDZ'] > 0.2:
    returnVal = False
    failChain['tauAbsDZ'] = False
  else:
    passChain['tauAbsDZ'] = True


  if printCutValues:
    print "-------------------------------------------"
    print "tau ", tau
    if len(passChain) > 0:
      print "passed cuts = ",passChain
    if len(failChain) > 0:
      print "failed cuts = ",failChain

  return returnVal





def tauID_eTau_forQCD(chain, index, printCutValues):
    returnVal = True
    failChain = {}
    passChain = {}
    tau = {}
    Lvec = TLorentzVector(0,0,0,0)
    Lvec.SetXYZT(chain.eT_tau_corrected_p4_x[index], chain.eT_tau_corrected_p4_y[index], chain.eT_tau_corrected_p4_z[index],chain.eT_tau_corrected_p4_t[index])
    tau['pt'] = Lvec.Pt()
    if (Lvec.Pt()>20) is False:
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

    tau['byLooseIsolationMVA3oldDMwLT'] = chain.eT_tau_byLooseIsolationMVA3oldDMwLT[index]
    if chain.eT_tau_byLooseIsolationMVA3oldDMwLT[index] <= 0.5:
        returnVal = False
        failChain['byLooseIsolationMVA3oldDMwLT'] = False
    else:
        passChain['byLooseIsolationMVA3oldDMwLT'] = True

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

    VtxZ = chain.eT_PVpositionZ[index]
    theta = Lvec.Theta()
    tanTheta = TMath.tan(theta)
    tau['ZimpactTau'] = 0.51
    if tanTheta != 0:
        tau['ZimpactTau'] = VtxZ + 130.0/( tanTheta )
    if (tau['ZimpactTau'] < -1.5 or tau['ZimpactTau'] > 0.5) is False :
        returnVal = False
        failChain['ZimpactTau'] = False
    else:
        passChain['ZimpactTau'] = True          

    tau['tauAbsDZ'] = abs(chain.eT_tau_vertex_z[index] - chain.eT_PVpositionZ[index])
    if tau['tauAbsDZ'] > 0.2:
        returnVal = False
        failChain['tauAbsDZ'] = False
    else:
        passChain['tauAbsDZ'] = True

    if printCutValues:
        print "-------------------------------------------"
        print "tau ", tau
        if len(passChain) > 0:
            print "passed cuts = ",passChain
        if len(failChain) > 0:
            print "failed cuts = ",failChain

    return returnVal




def tauID_muTau_forQCD(chain, index, printCutValues):
    returnVal = True
    failChain = {}
    passChain = {}
    tau = {}
    Lvec = TLorentzVector(0,0,0,0)
    Lvec.SetXYZT(chain.muT_tau_corrected_p4_x[index], chain.muT_tau_corrected_p4_y[index], chain.muT_tau_corrected_p4_z[index],chain.muT_tau_corrected_p4_t[index])

    tau['pt'] = Lvec.Pt()
    if (Lvec.Pt()>20) is False:
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

    tau['byLooseIsolationMVA3oldDMwLT'] = chain.muT_tau_byLooseIsolationMVA3oldDMwLT[index]
    if chain.muT_tau_byLooseIsolationMVA3oldDMwLT[index] <= 0.5:
        returnVal = False
        failChain['byLooseIsolationMVA3oldDMwLT'] = False
    else:
        passChain['byLooseIsolationMVA3oldDMwLT'] = True

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

    tau['tauAbsDZ'] = abs(chain.muT_tau_vertex_z[index] - chain.muT_PVpositionZ[index])
    if tau['tauAbsDZ'] > 0.2:
        returnVal = False
        failChain['tauAbsDZ'] = False
    else:
        passChain['tauAbsDZ'] = True

    if printCutValues:
        print "-------------------------------------------"
        print "tau ", tau
        if len(passChain) > 0:
            print "passed cuts = ",passChain
        if len(failChain) > 0:
            print "failed cuts = ",failChain

    return returnVal



def tauID_eTau_looseORtightISO(chain, index, printCutValues):
    returnVal = True
    failChain = {}
    passChain = {}
    tau = {}
    Lvec = TLorentzVector(0,0,0,0)
    Lvec.SetXYZT(chain.eT_tau_corrected_p4_x[index], chain.eT_tau_corrected_p4_y[index], chain.eT_tau_corrected_p4_z[index],chain.eT_tau_corrected_p4_t[index])
    tau['pt'] = Lvec.Pt()
    if (Lvec.Pt()>20) is False:
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

    tau['byLooseOrTightIsolationMVA3oldDMwLT'] = ( chain.eT_tau_byLooseIsolationMVA3oldDMwLT[index] or
                                                    chain.eT_tau_byTightIsolationMVA3oldDMwLT[index] )
    if chain.eT_tau_byLooseIsolationMVA3oldDMwLT[index] <= 0.5 and chain.eT_tau_byTightIsolationMVA3oldDMwLT[index] <= 0.5:
        returnVal = False
        failChain['byLooseOrTightIsolationMVA3oldDMwLT'] = False
    else:
        passChain['byLooseOrTightIsolationMVA3oldDMwLT'] = True

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

    VtxZ = chain.eT_PVpositionZ[index]
    theta = Lvec.Theta()
    tanTheta = TMath.tan(theta)
    tau['ZimpactTau'] = 0.51
    if tanTheta != 0:
        tau['ZimpactTau'] = VtxZ + 130.0/( tanTheta )
    if (tau['ZimpactTau'] < -1.5 or tau['ZimpactTau'] > 0.5) is False :
        returnVal = False
        failChain['ZimpactTau'] = False
    else:
        passChain['ZimpactTau'] = True  

    tau['tauAbsDZ'] = abs(chain.eT_tau_vertex_z[index] - chain.eT_PVpositionZ[index])
    if tau['tauAbsDZ'] > 0.2:
        returnVal = False
        failChain['tauAbsDZ'] = False
    else:
        passChain['tauAbsDZ'] = True           

    if printCutValues:
        print "-------------------------------------------"
        print "tau ", tau
        if len(passChain) > 0:
            print "passed cuts = ",passChain
        if len(failChain) > 0:
            print "failed cuts = ",failChain

    return returnVal




def tauID_muTau_looseORtightISO(chain, index, printCutValues):
    returnVal = True
    failChain = {}
    passChain = {}
    tau = {}
    Lvec = TLorentzVector(0,0,0,0)
    Lvec.SetXYZT(chain.muT_tau_corrected_p4_x[index], chain.muT_tau_corrected_p4_y[index], chain.muT_tau_corrected_p4_z[index],chain.muT_tau_corrected_p4_t[index])

    tau['pt'] = Lvec.Pt()
    if (Lvec.Pt()>20) is False:
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

    tau['byLooseOrTightIsolationMVA3oldDMwLT'] = ( chain.muT_tau_byLooseIsolationMVA3oldDMwLT[index] or
                                                    chain.muT_tau_byTightIsolationMVA3oldDMwLT[index] )
    if chain.muT_tau_byLooseIsolationMVA3oldDMwLT[index] <= 0.5 and chain.muT_tau_byTightIsolationMVA3oldDMwLT[index] <= 0.5:
        returnVal = False
        failChain['byLooseOrTightIsolationMVA3oldDMwLT'] = False
    else:
        passChain['byLooseOrTightIsolationMVA3oldDMwLT'] = True

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

    tau['tauAbsDZ'] = abs(chain.muT_tau_vertex_z[index] - chain.muT_PVpositionZ[index])
    if tau['tauAbsDZ'] > 0.2:
        returnVal = False
        failChain['tauAbsDZ'] = False
    else:
        passChain['tauAbsDZ'] = True  

    if printCutValues:
        print "-------------------------------------------"
        print "tau ", tau
        if len(passChain) > 0:
            print "passed cuts = ",passChain
        if len(failChain) > 0:
            print "failed cuts = ",failChain

    return returnVal
