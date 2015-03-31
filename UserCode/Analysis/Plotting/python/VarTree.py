import time
import sys
import os
import array, math


from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TApplication,TTreeCache,TMatrix,TVector,TString,AddressOf

from Plotting.python.FileName import FileNamePrefix


VARIABLE_NAMES = []
VARIABLE_NAMES.append('SVmass')
VARIABLE_NAMES.append('VisMass')
VARIABLE_NAMES.append('mvaMET')
VARIABLE_NAMES.append('tauPt')
VARIABLE_NAMES.append('lepPt')
VARIABLE_NAMES.append('decay_mode_1')
VARIABLE_NAMES.append('decay_mode_2')
VARIABLE_NAMES.append('tau_numStrips')
VARIABLE_NAMES.append('tau_numHadrons')
VARIABLE_NAMES.append('fill_weight')
VARIABLE_NAMES.append('isMuonTau')


# string variables 
VARIABLE_NAMES.append('channel'); channel_String = TString("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
VARIABLE_NAMES.append('sampleType'); sampleType_String = TString("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
VARIABLE_NAMES.append('tauEs'); tauEs_String = TString("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
STRING_COUNT = 3

for i in range(0,len(VARIABLE_NAMES)-STRING_COUNT):
	execString = "var_"+VARIABLE_NAMES[i]+" = array.array(\x27f\x27,[0])"
	exec(execString)

	

# create file
fileOutName = str(FileNamePrefix)+'_variableTree.root'
varFile = TFile(fileOutName,"RECREATE")


def var_InitTreeAndFile(VARS_DICT):

	# create Tree
	varTree = TTree("varTree","varTree")	

	# add branches and init dict to hold values for each event

	for i in range(0,len(VARIABLE_NAMES)-STRING_COUNT):
		VARS_DICT[VARIABLE_NAMES[i]] = 0.0
		execString = "varTree.Branch(\x27"+VARIABLE_NAMES[i]+"\x27,var_"+VARIABLE_NAMES[i]+",\x27"+VARIABLE_NAMES[i]+"/F\x27)"
		exec(execString)

	varTree.Branch('channel',"TString",AddressOf(channel_String),1600,0)
	varTree.Branch('sampleType',"TString",AddressOf(sampleType_String),1600,0)
	varTree.Branch('tauEs',"TString",AddressOf(tauEs_String),1600,0)

	return varTree


def fill_varTree(chain,varTree,sampleClassification, maxPairTypeAndIndex, VARS_DICT, TREE_WEIGHT,channel_String,sampleType_String,tauEs_String):
	print sampleClassification, maxPairTypeAndIndex

	# TString branches
	channel_String.Clear()
	sampleType_String.Clear()
	tauEs_String.Clear()
	channel_String += str(maxPairTypeAndIndex[2])
	sampleType_String += str(sampleClassification)
	tauEs_String += str(maxPairTypeAndIndex[3])

	# other branches
	index = maxPairTypeAndIndex[0]

  	Tvec = TLorentzVector(0,0,0,0)
	Lvec = TLorentzVector(0,0,0,0)



	if maxPairTypeAndIndex[1] == 'muTau':

  		Tvec.SetXYZT(chain.muT_tau_corrected_p4_x[index], chain.muT_tau_corrected_p4_y[index], chain.muT_tau_corrected_p4_z[index],chain.muT_tau_corrected_p4_t[index])
 		Lvec.SetXYZT(chain.muT_muon_p4_x[index], chain.muT_muon_p4_y[index], chain.muT_muon_p4_z[index],chain.muT_muon_p4_t[index])
		VARS_DICT['fill_weight'] = TREE_WEIGHT
		VARS_DICT['SVmass'] = chain.muT_correctedSVFitMass[index]
		VARS_DICT['VisMass'] = (Tvec+Lvec).M()
		VARS_DICT['mvaMET'] = chain.muT_mvaMET[index]
		VARS_DICT['tauPt'] = Tvec.Pt()
		VARS_DICT['lepPt'] = Lvec.Pt()
		VARS_DICT['tau_numStrips'] = chain.muT_tau_numStrips[index]
		VARS_DICT['tau_numHadrons'] = chain.muT_tau_numHadrons[index]
		VARS_DICT['decay_mode_1']	= chain.muT_tau_decayModeFindingOldDMs[index]
		VARS_DICT['isMuonTau'] = 1.0

	if maxPairTypeAndIndex[1] == 'eleTau':

  		Tvec.SetXYZT(chain.eT_tau_corrected_p4_x[index], chain.eT_tau_corrected_p4_y[index], chain.eT_tau_corrected_p4_z[index],chain.eT_tau_corrected_p4_t[index])
 		Lvec.SetXYZT(chain.eT_ele_p4_x[index], chain.eT_ele_p4_y[index], chain.eT_ele_p4_z[index],chain.eT_ele_p4_t[index])
		VARS_DICT['fill_weight'] = TREE_WEIGHT
		VARS_DICT['SVmass'] = chain.eT_correctedSVFitMass[index]
		VARS_DICT['VisMass'] = (Tvec+Lvec).M()
		VARS_DICT['mvaMET'] = chain.eT_mvaMET[index]
		VARS_DICT['tauPt'] = Tvec.Pt()
		VARS_DICT['lepPt'] = Lvec.Pt()
		VARS_DICT['tau_numStrips'] = chain.eT_tau_numStrips[index]
		VARS_DICT['tau_numHadrons'] = chain.eT_tau_numHadrons[index]
		VARS_DICT['decay_mode_1']	= chain.eT_tau_decayModeFindingOldDMs[index]
		VARS_DICT['isMuonTau'] = 0.0




	decay_mode_2 = 999 # (had,strips) = (1,0) store 0; (1,>0) store 1,  (3,any) store 2 

	if VARS_DICT['tau_numHadrons'] == 1 and VARS_DICT['tau_numStrips']==0:
		VARS_DICT['decay_mode_2'] = 0

	if VARS_DICT['tau_numHadrons'] == 1 and VARS_DICT['tau_numStrips']>0:
		VARS_DICT['decay_mode_2'] = 1

	if VARS_DICT['tau_numHadrons'] == 3:
		VARS_DICT['decay_mode_2'] = 2



	for key, value in VARS_DICT.iteritems():
		command = "var_"+key+"[0] = VARS_DICT[\x27"+key+"\x27]"
		#print command
		exec(command)
	varTree.Fill()
	return



def var_WriteTree(varTree):
	varFile.cd()
	varTree.Write("varTree")
	varFile.Close()
	return	
