import time
import sys
import os
import array, math


from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TApplication,TTreeCache,TMatrix,TVector,TString,AddressOf


# category
eventType = []
eventType.append("muTau")
eventType.append("eleTau")

# channels
channels = []
channels.append("inclusive") # this is inclusive but not btag or nonbtag
channels.append("btag_high")
channels.append("btag_low")
channels.append("nobtag_high")
channels.append("nobtag_medium")
channels.append("nobtag_low")



