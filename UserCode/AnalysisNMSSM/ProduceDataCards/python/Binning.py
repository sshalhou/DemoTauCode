import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TDirectoryFile
from array import array


############
# arrays
binning_nominal_btag = [0 , 20 , 40 , 60 , 80 , 100 , 120 , 140 , 160 , 180 ,
200 , 250 , 300 , 350 , 400 , 500 , 700 , 1000, 1500]



binning_nominal_nobtag = [0 , 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 ,
100 , 110 , 120 , 130 , 140 , 150 , 160 , 170 , 180 , 190 ,
200 , 225 , 250 , 275 , 300 , 325 , 350 , 400 , 500 , 700 ,
1000, 1500]


############
# lists

fine_binning = []
fine_binning.append(400)
fine_binning.append(0)
fine_binning.append(2000)
