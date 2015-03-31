import time
import sys
import os
import math
from array import array


from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TApplication,TTreeCache,TMatrix,TVector,TString,AddressOf

from python.Channels import *
from python.Classification import *

# have lists : samples, channels, eventType


binning_nominal_btag = [0 , 20 , 40 , 60 , 80 , 100 , 120 , 140 , 160 , 180 ,
200 , 250 , 300 , 350 , 400 , 500 , 700 , 1000, 1500]

binning_nominal_nobtag = [0 , 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 ,
100 , 110 , 120 , 130 , 140 , 150 , 160 , 170 , 180 , 190 ,
200 , 225 , 250 , 275 , 300 , 325 , 350 , 400 , 500 , 700 ,
1000, 1500]


def initialize_decay_vs_SVplots(decayVSsvDict):
	for d in range(0,3):
		for e in range(0,len(eventType)):
			for c in range(0,len(channels)):
				for s in range(0, len(samples)):
					histname = str( samples[s]+'_DM_'+str(d)+'_'+eventType[e]+'_'+channels[c]  )
					binning = binning_nominal_nobtag
					if 'btag' in str(channels[c]) and 'nobtag' not in str(channels[c]):
						binning = binning_nominal_btag
	   				decayVSsvDict[histname] = TH1F(histname,histname,len(binning)-1,array.array('d',binning))
	return


def initialize_mass_vs_DMplots(massVSdmDict):
	for e in range(0,len(eventType)):
		for s in range(0, len(samples)):
			for c in range(0,len(channels)):
				binning = binning_nominal_nobtag
				if 'btag' in str(channels[c]) and 'nobtag' not in str(channels[c]):
					binning = binning_nominal_btag			
				#print binning
				for b in range(0,len(binning)-1):
					low = binning[b]
					high = binning[b+1]
					histname = str( samples[s]+'_'+eventType[e]+'_'+channels[c]+'_MASS_'+str(low)+'_'+str(high) )
					#print histname
					massVSdmDict[histname] = TH1F(histname,histname,6,-1,5)
	return



def WriteDicts(DICT1, DICT2):
	OUTFILE = TFile("VAROUT.root","RECREATE")
	OUTFILE.cd()
	for key, value in DICT1.iteritems():
		#print key
		value.Write(key)
	for key, value in DICT2.iteritems():
		value.Write(key)	
	OUTFILE.Close()
	return


