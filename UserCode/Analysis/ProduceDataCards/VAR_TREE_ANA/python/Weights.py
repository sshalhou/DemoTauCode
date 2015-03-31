import time
import sys
import os
import math
from array import array

#python inform_generateCombinedDataCard.py | grep 'INFO-QCD' | grep -v CMS | grep -v fine
#cat txt.txt  | sed 's/\// /g' | sed 's/Tau_/Tau /g' | awk '{print "if channel==\x27"$8"\x27: channel_SF_ = "$9}'


from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TApplication,TTreeCache,TMatrix,TVector,TString,AddressOf

from python.Channels import *
from python.Classification import *

# have lists : samples, channels, eventType

def GetQCD_SF(eventType,channel):
	inclusive_SF_ = 1.0
	channel_SF_ = 1.0
	#########################


	if eventType == 'muTau':
		inclusive_SF_ = 0.284523286439
		if channel=='btag_high': channel_SF_ = 0.0581165819749
		if channel=='btag_low': channel_SF_ = 0.100161543984
		if channel=='nobtag_high': channel_SF_ = 0.42510788529
		if channel=='nobtag_medium': channel_SF_ = 0.257332298384
		if channel=='nobtag_low': channel_SF_ = 0.314492533885

	if eventType == 'eleTau':
		inclusive_SF_ = 1.00052119834
		if channel=='btag_high': channel_SF_ = 0.048419092884
		if channel=='btag_low': channel_SF_ = 0.189188101005
		if channel=='nobtag_high': channel_SF_ = 0.664718626881
		if channel=='nobtag_medium': channel_SF_ = 0.804637214646
		if channel=='nobtag_low': channel_SF_ = 1.22095509427		


	##########################
	return [inclusive_SF_,channel_SF_]


def GetWjets_SF(eventType,channel):
	inclusive_SF_ = 1.0
	channel_SF_ = 1.0
	#########################


	if eventType == 'muTau':
		inclusive_SF_ = 0.858107163297
		if channel=='btag_high': channel_SF_ = 0.050434572768
		if channel=='btag_low': channel_SF_ = 0.0434360603171
		if channel=='nobtag_high': channel_SF_ = 0.413697299791
		if channel=='nobtag_medium': channel_SF_ = 0.420715641563
		if channel=='nobtag_low': channel_SF_ = 0.427579614805

	if eventType == 'eleTau':
		inclusive_SF_ = 0.935617671169
		if channel=='btag_high': channel_SF_ = 0.0474878387009
		if channel=='btag_low': channel_SF_ = 0.0558824629042
		if channel=='nobtag_high': channel_SF_ = 0.43961233404
		if channel=='nobtag_medium': channel_SF_ = 0.45286494139
		if channel=='nobtag_low': channel_SF_ = 0.453903207777


	##########################
	return [inclusive_SF_,channel_SF_]


def GetZTT_SF(eventType,channel):
	inclusive_SF_ = 1.0
	channel_SF_ = 1.0
	#########################


	if eventType == 'muTau':
		inclusive_SF_ = 0.306483935407
		channel_SF_ = 0.306483935407
		
	if eventType == 'eleTau':
		inclusive_SF_ = 0.326529975915
		channel_SF_ = 0.326529975915
		

	##########################
	print 'subtract embedded ttBar then Scale when plotting, returning [1,1] for now'
	return [1.0,1.0]


def GetZL_SF(eventType,channel):
	inclusive_SF_ = 1.0
	channel_SF_ = 1.0
	#########################


	if eventType == 'muTau':
		inclusive_SF_ = 0.995659024711
		if channel=='nobtag_low': channel_SF_ = 1.02670910884
		if channel=='nobtag_medium': channel_SF_ = 1.03325090303
		if channel=='btag_low': channel_SF_ = 0.077508962761
		if channel=='btag_high': channel_SF_ = 0.153882766
		if channel=='nobtag_high': channel_SF_ = 1.12108951449


	if eventType == 'eleTau':
		inclusive_SF_ = 0.99656145764
		if channel=='nobtag_high': channel_SF_ = 1.10389383788
		if channel=='nobtag_low': channel_SF_ = 1.03120021504
		if channel=='btag_low': channel_SF_ = 0.134281450521
		if channel=='nobtag_medium': channel_SF_ = 1.03781638517
		if channel=='btag_high': channel_SF_ = 0.274719913641


	##########################
	return [inclusive_SF_,channel_SF_]



def GetZJ_SF(eventType,channel):
	inclusive_SF_ = 1.0
	channel_SF_ = 1.0
	#########################


	if eventType == 'muTau':		 
		inclusive_SF_ = 1.20675473945
		if channel=='nobtag_low': channel_SF_ = 1.39036890785
		if channel=='nobtag_medium': channel_SF_ = 1.23638121146
		if channel=='btag_low': channel_SF_ = 0.322102692782
		if channel=='btag_high': channel_SF_ = 0.283104255279
		if channel=='nobtag_high': channel_SF_ = 1.23408818663


	if eventType == 'eleTau':
		inclusive_SF_ = 1.11987602025
		if channel=='nobtag_low': channel_SF_ = 1.24962049643
		if channel=='btag_low': channel_SF_ = 0.209903988843
		if channel=='nobtag_medium': channel_SF_ = 1.23634898016
		if channel=='nobtag_high': channel_SF_ = 1.15227337878
		if channel=='btag_high': channel_SF_ = 0.239791628306



	##########################
	return [inclusive_SF_,channel_SF_]



def getWeightSF(eventType,channel,sampleClassification):
	# always returns 2 weight SFs [inclusive_SF, channel_SF]
	eventType = str(eventType)
	channel = str(channel)
	sampleClassification = str(sampleClassification)
	channel_SF = 1.0
	inclusive_SF  = 1.0

	if sampleClassification=='Data': return [1.0,1.0]
	if sampleClassification=='SM_Higgs125': return [1.0,1.0]
	if sampleClassification=='VV': return [1.0,1.0]

	if sampleClassification=='TT': 
		inclusive_SF = ((1.016)/(1.033))
		channel_SF = ((1.016)/(1.033))
		return [inclusive_SF, channel_SF]

	if sampleClassification=='embeddedTT': 
		inclusive_SF *= -1*((241.5*1.016*0.105)/(5.8869*4.45013504560974305))
		channel_SF *= -1*((241.5*1.016*0.105)/(5.8869*4.45013504560974305))
		return [inclusive_SF, channel_SF]

	if sampleClassification=='QCD': 
		RetList = GetQCD_SF(eventType,channel)
		return RetList

	if sampleClassification=='Wjets': 
		RetList = GetWjets_SF(eventType,channel)
		return RetList

	if sampleClassification=='ZTT': 
		RetList = GetZTT_SF(eventType,channel)
		return RetList

	if sampleClassification=='ZL': 
		RetList = GetZL_SF(eventType,channel)
		return RetList	

	if sampleClassification=='ZJ': 
		RetList = GetZJ_SF(eventType,channel)
		return RetList	

	return [inclusive_SF, channel_SF]