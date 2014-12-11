import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TDirectoryFile
from array import array


############
# arrays

binning_nominal_btag = [0 , 5 , 10 , 15 , 20 , 25, 30, 35, 40, 45, 
50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 
160, 180, 200]

binning_nominal_nobtag = [0 , 5 , 10 , 15 , 20 , 25, 30, 35, 40, 45, 
50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 
160, 180, 200]




############
# lists

fine_binning = []
fine_binning.append(400)
fine_binning.append(0)
fine_binning.append(2000)
