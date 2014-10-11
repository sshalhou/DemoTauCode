import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile

comparisonFile = TFile( "comparisonFile.root", 'RECREATE', 'test' )

njet_eleTau = TH1F("njet_eleTau","njet_eleTau",5,0,5)
nbjet_eleTau = TH1F("nbjet_eleTau","nbjet_eleTau",5,0,5)
svMass_eleTau =  TH1F("svMass_eleTau","svMass_eleTau",50,0,250)
mvaMET_eleTau = TH1F("mvaMET_eleTau","mvaMET_eleTau",50,0,250)

njet_muTau = TH1F("njet_muTau","njet_muTau",5,0,5)
nbjet_muTau = TH1F("nbjet_muTau","nbjet_muTau",5,0,5)
svMass_muTau =  TH1F("svMass_muTau","svMass_muTau",50,0,250)
mvaMET_muTau = TH1F("mvaMET_muTau","mvaMET_muTau",50,0,250)


def writeCompFile():
  comparisonFile.cd()
  njet_eleTau.Write()
  nbjet_eleTau.Write()
  svMass_eleTau.Write()
  mvaMET_eleTau.Write()
  njet_muTau.Write()
  nbjet_muTau.Write()
  svMass_muTau.Write()
  mvaMET_muTau.Write()
  return
