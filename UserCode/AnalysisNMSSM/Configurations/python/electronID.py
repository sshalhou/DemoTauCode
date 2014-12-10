import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile



def electronID(chain, index, printCutValues):
  returnVal = True
  failChain = {}
  passChain = {}
  electron = {}
  Lvec = TLorentzVector(0,0,0,0)
  Lvec.SetXYZT(chain.eT_ele_p4_x[index], chain.eT_ele_p4_y[index], chain.eT_ele_p4_z[index],chain.eT_ele_p4_t[index])

  electron['pt'] = Lvec.Pt()
  if (Lvec.Pt()>24) is False:
    returnVal = False
    failChain['pt'] = False
  else:
    passChain['pt'] = True

  electron['eta'] = Lvec.Eta()
  if (abs(Lvec.Eta())<2.1) is False:
    returnVal = False
    failChain['eta'] = False
  else:
    passChain['eta'] = True

  electron['numberMissingInnerHits'] = chain.eT_ele_numberOfMissingInnerHits[index]
  if (chain.eT_ele_numberOfMissingInnerHits[index]==0) is False:
    returnVal = False
    failChain['numberMissingInnerHits'] = False
  else:
    passChain['numberMissingInnerHits'] = True

  electron['passConversionVeto'] = chain.eT_ele_passConversionVeto[index]
  if chain.eT_ele_passConversionVeto[index] is False:
    returnVal = False
    failChain['passConversionVeto'] = False
  else:
    passChain['passConversionVeto'] = True

  electron['tight_mvaNonTrigV0'] = chain.eT_ele_pass_tight_mvaNonTrigV0[index]
  if chain.eT_ele_pass_tight_mvaNonTrigV0[index] is False:
    returnVal = False
    failChain['tight_mvaNonTrigV0'] = False
  else:
    passChain['tight_mvaNonTrigV0'] = True

  electron['relativeIso'] = chain.eT_ele_relativeIso[index]

  if (chain.eT_ele_relativeIso[index]<0.1) is False:
    returnVal = False
    failChain['relativeIso'] = False
  else:
    passChain['relativeIso'] = True

  electron['dxy'] = chain.eT_ele_dxy[index]
  if (abs(chain.eT_ele_dxy[index])<0.045) is False:
    returnVal = False
    failChain['dxy'] = False
  else:
    passChain['dxy'] = True

  electron['dz'] = chain.eT_ele_dz[index]
  if (abs(chain.eT_ele_dz[index])<0.2) is False:
    returnVal = False
    failChain['dz'] = False
  else:
    passChain['dz'] = True

  if printCutValues:
    print "-------------------------------------------"
    print "electron ", electron
    if len(passChain) > 0:
      print "passed cuts = ",passChain
    if len(failChain) > 0:
      print "failed cuts = ",failChain

  return returnVal



def electronIDforQCD(chain, index, printCutValues):
  returnVal = True
  failChain = {}
  passChain = {}
  electron = {}
  Lvec = TLorentzVector(0,0,0,0)
  Lvec.SetXYZT(chain.eT_ele_p4_x[index], chain.eT_ele_p4_y[index], chain.eT_ele_p4_z[index],chain.eT_ele_p4_t[index])

  electron['pt'] = Lvec.Pt()
  if (Lvec.Pt()>24) is False:
    returnVal = False
    failChain['pt'] = False
  else:
    passChain['pt'] = True

  electron['eta'] = Lvec.Eta()
  if (abs(Lvec.Eta())<2.1) is False:
    returnVal = False
    failChain['eta'] = False
  else:
    passChain['eta'] = True

  electron['numberMissingInnerHits'] = chain.eT_ele_numberOfMissingInnerHits[index]
  if (chain.eT_ele_numberOfMissingInnerHits[index]==0) is False:
    returnVal = False
    failChain['numberMissingInnerHits'] = False
  else:
    passChain['numberMissingInnerHits'] = True

  electron['passConversionVeto'] = chain.eT_ele_passConversionVeto[index]
  if chain.eT_ele_passConversionVeto[index] is False:
    returnVal = False
    failChain['passConversionVeto'] = False
  else:
    passChain['passConversionVeto'] = True

  electron['tight_mvaNonTrigV0'] = chain.eT_ele_pass_tight_mvaNonTrigV0[index]
  if chain.eT_ele_pass_tight_mvaNonTrigV0[index] is False:
    returnVal = False
    failChain['tight_mvaNonTrigV0'] = False
  else:
    passChain['tight_mvaNonTrigV0'] = True

  electron['relativeIso'] = chain.eT_ele_relativeIso[index]
  if (chain.eT_ele_relativeIso[index]<0.5 and chain.eT_ele_relativeIso[index]>0.2) is False:
    returnVal = False
    failChain['relativeIso'] = False
  else:
    passChain['relativeIso'] = True
    #print 'ele iso ', chain.eT_ele_relativeIso[index]

  electron['dxy'] = chain.eT_ele_dxy[index]
  if (abs(chain.eT_ele_dxy[index])<0.045) is False:
    returnVal = False
    failChain['dxy'] = False
  else:
    passChain['dxy'] = True

  electron['dz'] = chain.eT_ele_dz[index]
  if (abs(chain.eT_ele_dz[index])<0.2) is False:
    returnVal = False
    failChain['dz'] = False
  else:
    passChain['dz'] = True

  if printCutValues:
    print "-------------------------------------------"
    print "electron ", electron
    if len(passChain) > 0:
      print "passed cuts = ",passChain
    if len(failChain) > 0:
      print "failed cuts = ",failChain

  return returnVal
