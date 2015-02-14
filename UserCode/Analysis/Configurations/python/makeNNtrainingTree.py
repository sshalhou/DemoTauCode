import time
import sys
import os
import array, math


from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TApplication,TTreeCache,TMatrix,TVector


# create variables and their names in the tree

VAR_NAMES = []
VAR_NAMES.append('tauPt')
VAR_NAMES.append('tauEta')
VAR_NAMES.append('tauPhi')
VAR_NAMES.append('tauM')
VAR_NAMES.append('lepPt')
VAR_NAMES.append('lepEta')
VAR_NAMES.append('lepPhi')
VAR_NAMES.append('lepM')
VAR_NAMES.append('met')
VAR_NAMES.append('metPhi')
VAR_NAMES.append('j1Pt')
VAR_NAMES.append('j1Eta')
VAR_NAMES.append('j1Phi')
VAR_NAMES.append('j1M')
VAR_NAMES.append('j2Pt')
VAR_NAMES.append('j2Eta')
VAR_NAMES.append('j2Phi')
VAR_NAMES.append('j2M')
VAR_NAMES.append('njets')
VAR_NAMES.append('nBjets')



VAR_NAMES.append('METoverVisMass')
VAR_NAMES.append('VisMass')
VAR_NAMES.append('METoverHt')
VAR_NAMES.append('Ht')
VAR_NAMES.append('TauOverMET')
VAR_NAMES.append('LepOverMET')
VAR_NAMES.append('TauPlusLepOverMET')
VAR_NAMES.append('DRMETlepAndTau')
VAR_NAMES.append('DPhiMETlepAndTau')
VAR_NAMES.append('PtOfLEPandTauAndOppMET')
VAR_NAMES.append('PhiOfLEPandTauAndOppMET')
VAR_NAMES.append('PtOfLEPAndOppMET')
VAR_NAMES.append('PhiOfLEPAndOppMET')
VAR_NAMES.append('PtOfTAUAndOppMET')
VAR_NAMES.append('PhiOfTAUAndOppMET')
VAR_NAMES.append('DRtauLep')
VAR_NAMES.append('DRtauMet')
VAR_NAMES.append('DPHItauLep')
VAR_NAMES.append('DPHItauMet')
VAR_NAMES.append('DRlepMet')
VAR_NAMES.append('DPHIlepMet')
VAR_NAMES.append('DIFF_DRtauMet_DRlepMet')
VAR_NAMES.append('DIFF_DPHItauMet_DPHIlepMet')
VAR_NAMES.append('DRmetJets1and2')
VAR_NAMES.append('DPHImetJets1and2')
VAR_NAMES.append('DRlepJets1and2')
VAR_NAMES.append('DPHIlepJets1and2')
VAR_NAMES.append('DRtauJets1and2')
VAR_NAMES.append('DPHItauJets1and2')
VAR_NAMES.append('DRmetJet1')
VAR_NAMES.append('DPHImetJet1')
VAR_NAMES.append('DRlepJet1')
VAR_NAMES.append('DPHIlepJet1')
VAR_NAMES.append('DRtauJet1')
VAR_NAMES.append('DPHItauJet1')
VAR_NAMES.append('DRmetJet2')
VAR_NAMES.append('DPHImetJet2')
VAR_NAMES.append('DRlepJet2')
VAR_NAMES.append('DPHIlepJet2')
VAR_NAMES.append('DRtauJet2')
VAR_NAMES.append('DPHItauJet2')
VAR_NAMES.append('aplanarity')
VAR_NAMES.append('sphericity')
VAR_NAMES.append('ProjMetOnTau')
VAR_NAMES.append('ProjMetOnLep')
VAR_NAMES.append('ProjMetOnTauAndLep')
VAR_NAMES.append('DIFF_ABSDPHItauMet_ABSDPHIlepMet')

VAR_NAMES.append('tau_charge')
VAR_NAMES.append('tau_decayMode')
VAR_NAMES.append('tau_passFullId_muTau')
VAR_NAMES.append('tau_passFullId_eTau')
VAR_NAMES.append('tau_numStrips')
VAR_NAMES.append('tau_numHadrons')
VAR_NAMES.append('tau_byCombinedIsolationDeltaBetaCorrRaw')
VAR_NAMES.append('tau_byCombinedIsolationDeltaBetaCorrRaw3Hits')
VAR_NAMES.append('tau_byIsolationMVA3newDMwLTraw')
VAR_NAMES.append('tau_byIsolationMVA3newDMwoLTraw')
VAR_NAMES.append('tau_byIsolationMVA3oldDMwLTraw')
VAR_NAMES.append('tau_byIsolationMVA3oldDMwoLTraw')
VAR_NAMES.append('tau_chargedIsoPtSum')
VAR_NAMES.append('tau_decayModeFinding')
VAR_NAMES.append('tau_decayModeFindingNewDMs')
VAR_NAMES.append('tau_decayModeFindingOldDMs')
VAR_NAMES.append('tau_neutralIsoPtSum')
VAR_NAMES.append('tau_puCorrPtSum')
VAR_NAMES.append('tau_vertex_x')
VAR_NAMES.append('tau_vertex_y')
VAR_NAMES.append('tau_vertex_z')
VAR_NAMES.append('tau_vertex_theta')
VAR_NAMES.append('tau_vertex_eta')
VAR_NAMES.append('tau_vertex_phi')
VAR_NAMES.append('PVpositionZ')
VAR_NAMES.append('tau_DZ') 


VAR_NAMES.append('ele_SuperClusterEta') 
VAR_NAMES.append('ele_chargedHadronIso') 
VAR_NAMES.append('ele_deltaEtaSuperClusterTrackAtVtx') 
VAR_NAMES.append('ele_deltaPhiSuperClusterTrackAtVtx') 
VAR_NAMES.append('ele_hadronicOverEm') 
VAR_NAMES.append('ele_isEB') 
VAR_NAMES.append('ele_isEBEEGap') 
VAR_NAMES.append('ele_isEBEtaGap') 
VAR_NAMES.append('ele_isEBPhiGap') 
VAR_NAMES.append('ele_isEE') 
VAR_NAMES.append('ele_isEEDeeGap') 
VAR_NAMES.append('ele_isEERingGap') 
VAR_NAMES.append('ele_mvaNonTrigV0') 
VAR_NAMES.append('ele_mvaTrigNoIPV0') 
VAR_NAMES.append('ele_mvaTrigV0') 
VAR_NAMES.append('ele_neutralHadronIso') 
VAR_NAMES.append('ele_numberOfMissingInnerHits') 
VAR_NAMES.append('ele_passConversionVeto') 
VAR_NAMES.append('ele_passFullId') 
VAR_NAMES.append('ele_pass_tight_mvaNonTrigV0') 
VAR_NAMES.append('ele_photonIso') 
VAR_NAMES.append('ele_puChargedHadronIso') 
VAR_NAMES.append('ele_sigmaEtaEta') 
VAR_NAMES.append('ele_sigmaIetaIeta') 
VAR_NAMES.append('ele_sigmaIphiIphi') 
VAR_NAMES.append('isLEPelectron') 
VAR_NAMES.append('isLEPmuon') 
VAR_NAMES.append('lep_Charge') 
VAR_NAMES.append('lep_dB') 
VAR_NAMES.append('lep_dxy') 
VAR_NAMES.append('lep_dz') 
VAR_NAMES.append('lep_relIso') 
VAR_NAMES.append('muon_isGlobalMuon') 
VAR_NAMES.append('muon_isLooseMuon') 
VAR_NAMES.append('muon_isPFMuon') 
VAR_NAMES.append('muon_isTightMuon') 
VAR_NAMES.append('muon_isTrackerMuon') 
VAR_NAMES.append('muon_normalizedChi2') 
VAR_NAMES.append('muon_numberOfMatchedStations') 
VAR_NAMES.append('muon_numberOfValidMuonHits') 
VAR_NAMES.append('muon_numberOfValidPixelHits') 
VAR_NAMES.append('muon_passFullId') 
VAR_NAMES.append('muon_sumChargedParticlePt_DR4') 
VAR_NAMES.append('muon_sumNeutralHadronEt_DR4') 
VAR_NAMES.append('muon_sumPUPt_DR4') 
VAR_NAMES.append('muon_sumPhotonEt_DR4') 
VAR_NAMES.append('muon_trackerLayersWithMeasurement') 


VAR_NAMES.append('GENtauPt')
VAR_NAMES.append('GENtauEta')
VAR_NAMES.append('GENtauPhi')
VAR_NAMES.append('GENtauM')
VAR_NAMES.append('GENlepPt')
VAR_NAMES.append('GENlepEta')
VAR_NAMES.append('GENlepPhi')
VAR_NAMES.append('GENlepM')
VAR_NAMES.append('GENdiTauMass')
VAR_NAMES.append('SVMass')



#  SVmass,
# type, decayMode, gTvec.Pt(), gTvec.Eta(), gTvec.Phi(), gLvec.Pt(), 
# gLvec.Eta(), gLvec.Phi(), (gLvec+gTvec).M(), bVec.M(), genVEC.Pt()/Tvec.Pt()


for i in range(0,len(VAR_NAMES)):
	execString = "var_"+VAR_NAMES[i]+" = array.array(\x27f\x27,[0])"
	exec(execString)


# create file
nnTrainFile = TFile("nnTrainFile.root","RECREATE")


def InitTreeAndFile(nnVARS_DICT):

	# create Tree
	nnTree = TTree("nnTree","nnTree")	

	# add branches and init dict to hold values for each event

	for i in range(0,len(VAR_NAMES)):
		nnVARS_DICT[VAR_NAMES[i]] = 0.0
		execString = "nnTree.Branch(\x27"+VAR_NAMES[i]+"\x27,var_"+VAR_NAMES[i]+",\x27"+VAR_NAMES[i]+"/F\x27)"
		exec(execString)

	return nnTree


def fillTree(nnTree, nnVARS_DICT):
	for key, value in nnVARS_DICT.iteritems():
		command = "var_"+key+"[0] = nnVARS_DICT[\x27"+key+"\x27]"
		#print command
		exec(command)
	nnTree.Fill()
	return


def WriteTree(nnTree):
	nnTrainFile.cd()
	nnTree.Write("nnTree")
	nnTrainFile.Close()
	return

##############################
##############################
##############################
def SetVariableValues(nnVARS_DICT,chain, maxPairTypeAndIndex):
	i = maxPairTypeAndIndex[0]
	DRCUT = 0.05
	# reset to zero
	for key, value in nnVARS_DICT.iteritems():
		nnVARS_DICT[key] = 0.0


	# get gen info for all tau_h, tau_lep events
	genVecs = {}
	genVecs['genLepTau'] = TLorentzVector(0,0,0,0)
	genVecs['genHadTau'] = TLorentzVector(0,0,0,0)

	if getGenDecay(chain,genVecs,DRCUT) is False:
		print 'NOT lepTau'
		return False

	# get recoVecs, tau, lep, jet info, and met
	recoVecs = {}
	jetCount = {}
	recoVecs['recoLepTau'] = TLorentzVector(0,0,0,0)
	recoVecs['recoHadTau'] = TLorentzVector(0,0,0,0)
	recoVecs['recoMET'] = TLorentzVector(0,0,0,0)
	recoVecs['jet1'] = TLorentzVector(0,0,0,0)
	recoVecs['jet2'] = TLorentzVector(0,0,0,0)

	jetCount['njets'] = 0
	jetCount['nBjets'] = 0

	getRecoVecsAndJetCount(chain,recoVecs,jetCount,maxPairTypeAndIndex)




	#print 'gen', genVecs['genLepTau'].Pt(), genVecs['genHadTau'].Pt()
	#print 'reco', recoVecs['recoLepTau'].Pt(), recoVecs['recoHadTau'].Pt(), recoVecs['recoMET'].Pt()
	#print 'DR', genVecs['genLepTau'].DeltaR(recoVecs['recoLepTau']), genVecs['genHadTau'].DeltaR(recoVecs['recoHadTau'])

	if genVecs['genLepTau'].DeltaR(recoVecs['recoLepTau']) >= DRCUT or genVecs['genHadTau'].DeltaR(recoVecs['recoHadTau'])>= DRCUT:
		print 'BAD DR'
		return False

	#print genVecs['genLepTau'].Pt()/recoVecs['recoLepTau'].Pt(),
	#print genVecs['genHadTau'].Pt()/recoVecs['recoHadTau'].Pt()

	# set tree values for the reco 4-vectors and jet quantities

	writeReco4vectorsAndJetInfoInTree(recoVecs,jetCount,nnVARS_DICT)

	writeGenInfo(genVecs,nnVARS_DICT)



	if maxPairTypeAndIndex[1] == 'muTau':
		setVarsMuTau(chain,i,nnVARS_DICT)
	elif maxPairTypeAndIndex[1] == 'eleTau':
		setVarsETau(chain,i,nnVARS_DICT)


	writeHadTauParameters(nnVARS_DICT,chain, maxPairTypeAndIndex)
	writeLepTauParameters(nnVARS_DICT,chain, maxPairTypeAndIndex)

	return True
##############################
##############################
##############################


def setVarsMuTau(chain,i,nnVARS_DICT):
	nnVARS_DICT['SVMass'] = chain.muT_correctedSVFitMass[i]
	return

def setVarsETau(chain,i,nnVARS_DICT):
	nnVARS_DICT['SVMass'] = chain.eT_correctedSVFitMass[i]
	return


def getGenDecay(chain,genVecs,DRcut):

	genTauPlus = TLorentzVector(0,0,0,0)
	tauPlusInx = 0
	genTauMinus = TLorentzVector(0,0,0,0)
	tauMinusInx = 0
	#print '---------'

	#print 'find the hard scatter taus'

	for i in range(0,chain.pdgId.size()):
		#print i, chain.pdgId[i],chain.pdgIdmother[i], chain.status[i]
		if chain.pdgId[i] == 15 and chain.status[i]==3:
			genTauPlus.SetXYZT(chain.gen_x[i],chain.gen_y[i],chain.gen_z[i],chain.gen_t[i])
			tauPlusInx = i
		if chain.pdgId[i] == -15 and chain.status[i]==3:
			genTauMinus.SetXYZT(chain.gen_x[i],chain.gen_y[i],chain.gen_z[i],chain.gen_t[i])
			tauMinusInx = i

	if tauPlusInx==0 or genTauMinus==0:
		return False

	#print '+tau', tauPlusInx, '-tau',tauMinusInx



	#print 'figure out which of the 2 taus decays leptonically'
	#print 'if both or none are skip the event'
	NUM_LEP_MATCHED = 0
	tempVec = TLorentzVector(0,0,0,0)
	for i in range(0,chain.pdgId.size()):
		if abs(chain.pdgId[i]) == 11 or abs(chain.pdgId[i])==13: 
			if abs(chain.pdgIdmother[i]) == 15:
				tempVec.SetXYZT(chain.gen_x[i],chain.gen_y[i],chain.gen_z[i],chain.gen_t[i])
				if 	chain.pdgIdmother[i] == -15 and tempVec.DeltaR(genTauMinus)<DRcut:
					NUM_LEP_MATCHED += 1	
					genVecs['genLepTau'] = genTauMinus
					genVecs['genHadTau'] = genTauPlus			
				if 	chain.pdgIdmother[i] == 15 and tempVec.DeltaR(genTauPlus)<DRcut:
					NUM_LEP_MATCHED += 1
					genVecs['genLepTau'] = genTauPlus
					genVecs['genHadTau'] = genTauMinus	

	#print 'lep matched count ', NUM_LEP_MATCHED

	if NUM_LEP_MATCHED != 1:
		return False

	return True


def getRecoVecsAndJetCount(chain,recoVecs,jetCount,maxPairTypeAndIndex):
	i = maxPairTypeAndIndex[0]
	
	if maxPairTypeAndIndex[1] == 'muTau':
		recoVecs['recoLepTau'].SetXYZT(chain.muT_muon_p4_x[i], chain.muT_muon_p4_y[i], chain.muT_muon_p4_z[i],chain.muT_muon_p4_t[i])
		recoVecs['recoHadTau'].SetXYZT(chain.muT_tau_corrected_p4_x[i], chain.muT_tau_corrected_p4_y[i], chain.muT_tau_corrected_p4_z[i],chain.muT_tau_corrected_p4_t[i])
		recoVecs['recoMET'].SetPtEtaPhiM(chain.muT_mvaMET[i],0.0,chain.muT_mvaMETphi[i],0)
		#print chain.muT_njets[i], chain.muT_nbjets[i]
		jetCount['njets'] = chain.muT_njets[i]
		jetCount['nBjets'] = chain.muT_nbjets[i]
		if chain.muT_njets[i] > 0 :
			recoVecs['jet1'].SetXYZT(chain.muT_jet1P4_x[i] , chain.muT_jet1P4_y[i] , chain.muT_jet1P4_z[i] , chain.muT_jet1P4_t[i])
		if chain.muT_njets[i] > 1 :
			recoVecs['jet2'].SetXYZT(chain.muT_jet2P4_x[i] , chain.muT_jet2P4_y[i] , chain.muT_jet2P4_z[i] , chain.muT_jet2P4_t[i])


	elif maxPairTypeAndIndex[1] == 'eleTau':
		recoVecs['recoLepTau'].SetXYZT(chain.eT_ele_p4_x[i], chain.eT_ele_p4_y[i], chain.eT_ele_p4_z[i],chain.eT_ele_p4_t[i])
		recoVecs['recoHadTau'].SetXYZT(chain.eT_tau_corrected_p4_x[i], chain.eT_tau_corrected_p4_y[i], chain.eT_tau_corrected_p4_z[i],chain.eT_tau_corrected_p4_t[i])
		recoVecs['recoMET'].SetPtEtaPhiM(chain.eT_mvaMET[i],0.0,chain.eT_mvaMETphi[i],0.0)
		jetCount['njets'] = chain.eT_njets[i]
		jetCount['nBjets'] = chain.eT_nbjets[i]
		if chain.eT_njets[i] > 0 :
			recoVecs['jet1'].SetXYZT(chain.eT_jet1P4_x[i] , chain.eT_jet1P4_y[i] , chain.eT_jet1P4_z[i] , chain.eT_jet1P4_t[i])
		if chain.eT_njets[i] > 1 :
			recoVecs['jet2'].SetXYZT(chain.eT_jet2P4_x[i] , chain.eT_jet2P4_y[i] , chain.eT_jet2P4_z[i] , chain.eT_jet2P4_t[i])



	return


def writeReco4vectorsAndJetInfoInTree(recoVecs,jetCount,nnVARS_DICT):

	nnVARS_DICT['tauPt'] =   recoVecs['recoHadTau'].Pt()
	nnVARS_DICT['tauEta'] =  recoVecs['recoHadTau'].Eta()
	nnVARS_DICT['tauPhi'] = recoVecs['recoHadTau'].Phi()
	nnVARS_DICT['tauM'] = recoVecs['recoHadTau'].M()
	nnVARS_DICT['lepPt'] = recoVecs['recoLepTau'].Pt()
	nnVARS_DICT['lepEta'] = recoVecs['recoLepTau'].Eta()
	nnVARS_DICT['lepPhi'] = recoVecs['recoLepTau'].Phi()
	nnVARS_DICT['lepM'] = recoVecs['recoLepTau'].M()
	nnVARS_DICT['met'] = recoVecs['recoMET'].Pt()
	nnVARS_DICT['metPhi'] = recoVecs['recoMET'].Phi()

	nnVARS_DICT['njets'] = jetCount['njets']
	nnVARS_DICT['nBjets'] = jetCount['nBjets']


	nnVARS_DICT['VisMass'] = (recoVecs['recoHadTau']+recoVecs['recoLepTau']).M()
 	nnVARS_DICT['METoverVisMass'] = (recoVecs['recoMET'].Pt())/nnVARS_DICT['VisMass']
	nnVARS_DICT['Ht'] = recoVecs['recoHadTau'].Pt()+recoVecs['recoLepTau'].Pt()
	nnVARS_DICT['METoverHt'] = nnVARS_DICT['met'] / nnVARS_DICT['Ht']


	nnVARS_DICT['DRtauLep'] = recoVecs['recoHadTau'].DeltaR(recoVecs['recoLepTau'])
	nnVARS_DICT['DRtauMet'] = recoVecs['recoHadTau'].DeltaR(recoVecs['recoMET'])
	nnVARS_DICT['DRlepMet'] = recoVecs['recoLepTau'].DeltaR(recoVecs['recoMET'])

	nnVARS_DICT['DPHItauLep'] = recoVecs['recoHadTau'].DeltaPhi(recoVecs['recoLepTau'])
	nnVARS_DICT['DPHItauMet'] = recoVecs['recoHadTau'].DeltaPhi(recoVecs['recoMET'])
	nnVARS_DICT['DPHIlepMet'] = recoVecs['recoLepTau'].DeltaPhi(recoVecs['recoMET'])

	lepAndTau = recoVecs['recoHadTau']+recoVecs['recoLepTau']

	nnVARS_DICT['DRMETlepAndTau'] = lepAndTau.DeltaR(recoVecs['recoMET'])
	nnVARS_DICT['DPhiMETlepAndTau'] =  lepAndTau.DeltaPhi(recoVecs['recoMET'])
	nnVARS_DICT['PtOfLEPandTauAndOppMET'] = (lepAndTau - recoVecs['recoMET']).Pt()
	nnVARS_DICT['PhiOfLEPandTauAndOppMET'] = (lepAndTau - recoVecs['recoMET']).Eta()
	nnVARS_DICT['PtOfLEPAndOppMET'] = (recoVecs['recoLepTau'] - recoVecs['recoMET']).Pt()
	nnVARS_DICT['PhiOfLEPAndOppMET'] =  (recoVecs['recoLepTau'] - recoVecs['recoMET']).Phi()
	nnVARS_DICT['PtOfTAUAndOppMET'] = (recoVecs['recoHadTau'] - recoVecs['recoMET']).Pt()
	nnVARS_DICT['PhiOfTAUAndOppMET'] =  (recoVecs['recoHadTau'] - recoVecs['recoMET']).Phi()

	nnVARS_DICT['DIFF_DPHItauMet_DPHIlepMet'] = nnVARS_DICT['DPHItauMet'] - nnVARS_DICT['DPHIlepMet']
	nnVARS_DICT['DIFF_DRtauMet_DRlepMet']  = nnVARS_DICT['DRtauMet'] - nnVARS_DICT['DRlepMet']

	nnVARS_DICT['DIFF_ABSDPHItauMet_ABSDPHIlepMet'] = abs(nnVARS_DICT['DPHItauMet']) - abs(nnVARS_DICT['DPHIlepMet'])
	nnVARS_DICT['DIFF_DRtauMet_DRlepMet']  = nnVARS_DICT['DRtauMet'] - nnVARS_DICT['DRlepMet']

	nnVARS_DICT['ProjMetOnTau'] = recoVecs['recoMET'].Px()*recoVecs['recoHadTau'].Px()
	nnVARS_DICT['ProjMetOnTau'] += recoVecs['recoMET'].Py()*recoVecs['recoHadTau'].Py()
	den = recoVecs['recoHadTau'].Px()*recoVecs['recoHadTau'].Px() 
	den += recoVecs['recoHadTau'].Py()*recoVecs['recoHadTau'].Py() 
	den += recoVecs['recoHadTau'].Pz()*recoVecs['recoHadTau'].Pz() 
	den = math.sqrt(den)
	nnVARS_DICT['ProjMetOnTau'] /= den

	nnVARS_DICT['ProjMetOnLep'] = recoVecs['recoMET'].Px()*recoVecs['recoLepTau'].Px()
	nnVARS_DICT['ProjMetOnLep'] += recoVecs['recoMET'].Py()*recoVecs['recoLepTau'].Py()
	den = recoVecs['recoLepTau'].Px()*recoVecs['recoLepTau'].Px() 
	den += recoVecs['recoLepTau'].Py()*recoVecs['recoLepTau'].Py() 
	den += recoVecs['recoLepTau'].Pz()*recoVecs['recoLepTau'].Pz() 
	den = math.sqrt(den)
	nnVARS_DICT['ProjMetOnLep'] /= den


	nnVARS_DICT['ProjMetOnTauAndLep'] = lepAndTau.Px()*lepAndTau.Px()
	nnVARS_DICT['ProjMetOnTauAndLep'] += recoVecs['recoMET'].Py()*lepAndTau.Py()
	den = lepAndTau.Px()*lepAndTau.Px() 
	den += lepAndTau.Py()*lepAndTau.Py() 
	den += lepAndTau.Pz()*lepAndTau.Pz() 
	den = math.sqrt(den)
	nnVARS_DICT['ProjMetOnTauAndLep'] /= den


	writeAplanarityAndSphericity(nnVARS_DICT,recoVecs)




	if nnVARS_DICT['met'] > 0.0 :
		nnVARS_DICT['TauOverMET'] = nnVARS_DICT['tauPt'] / nnVARS_DICT['met']
		nnVARS_DICT['LepOverMET'] = nnVARS_DICT['lepPt'] / nnVARS_DICT['met']
		nnVARS_DICT['TauPlusLepOverMET']  = (nnVARS_DICT['tauPt'] + nnVARS_DICT['lepPt']) / nnVARS_DICT['met']


	if jetCount['njets'] > 0:
		nnVARS_DICT['j1Pt'] = recoVecs['jet1'].Pt()
		nnVARS_DICT['j1Eta'] = recoVecs['jet1'].Eta()
		nnVARS_DICT['j1Phi'] = recoVecs['jet1'].Phi()
		nnVARS_DICT['j1M'] = recoVecs['jet1'].M()
		nnVARS_DICT['DRmetJet1'] = recoVecs['recoMET'].DeltaR(recoVecs['jet1'])
		nnVARS_DICT['DRtauJet1'] = recoVecs['recoHadTau'].DeltaR(recoVecs['jet1'])
		nnVARS_DICT['DRlepJet1'] = recoVecs['recoLepTau'].DeltaR(recoVecs['jet1'])
		nnVARS_DICT['DPHImetJet1'] = recoVecs['recoMET'].DeltaPhi(recoVecs['jet1'])
		nnVARS_DICT['DPHItauJet1'] = recoVecs['recoHadTau'].DeltaPhi(recoVecs['jet1'])
		nnVARS_DICT['DPHIlepJet1'] = recoVecs['recoLepTau'].DeltaPhi(recoVecs['jet1'])

	if jetCount['njets'] > 1:
		nnVARS_DICT['j2Pt'] = recoVecs['jet2'].Pt()
		nnVARS_DICT['j2Eta'] = recoVecs['jet2'].Eta()
		nnVARS_DICT['j2Phi'] = recoVecs['jet2'].Phi()
		nnVARS_DICT['j2M'] = recoVecs['jet2'].M()
		nnVARS_DICT['DRmetJet2'] = recoVecs['recoMET'].DeltaR(recoVecs['jet2'])
		nnVARS_DICT['DRtauJet2'] = recoVecs['recoHadTau'].DeltaR(recoVecs['jet2'])
		nnVARS_DICT['DRlepJet2'] = recoVecs['recoLepTau'].DeltaR(recoVecs['jet2'])
		nnVARS_DICT['DPHImetJet2'] = recoVecs['recoMET'].DeltaPhi(recoVecs['jet2'])
		nnVARS_DICT['DPHItauJet2'] = recoVecs['recoHadTau'].DeltaPhi(recoVecs['jet2'])
		nnVARS_DICT['DPHIlepJet2'] = recoVecs['recoLepTau'].DeltaPhi(recoVecs['jet2'])

		Jets1and2 = recoVecs['jet1']+recoVecs['jet2']

		nnVARS_DICT['DRmetJets1and2'] = recoVecs['recoMET'].DeltaR(Jets1and2)
		nnVARS_DICT['DRtauJets1and2'] = recoVecs['recoHadTau'].DeltaR(Jets1and2)
		nnVARS_DICT['DRlepJets1and2'] = recoVecs['recoLepTau'].DeltaR(Jets1and2)

		nnVARS_DICT['DPHImetJets1and2'] = recoVecs['recoMET'].DeltaPhi(Jets1and2)
		nnVARS_DICT['DPHItauJets1and2'] = recoVecs['recoHadTau'].DeltaPhi(Jets1and2)
		nnVARS_DICT['DPHIlepJets1and2'] = recoVecs['recoLepTau'].DeltaPhi(Jets1and2)

	return

def writeAplanarityAndSphericity(nnVARS_DICT,recoVecs):

	Asum = 0.0
	mxx = 0.0
	myy = 0.0
	mzz = 0.0
	mxy = 0.0
	mxz = 0.0
	myz = 0.0

	for key, value in recoVecs.iteritems():
		#print key, recoVecs[key].Pt()
		Asum += pow(recoVecs[key].P(),2)
		mxx += pow(recoVecs[key].Px(),2)
		myy += pow(recoVecs[key].Py(),2)
		mzz += pow(recoVecs[key].Pz(),2)
		mxy += recoVecs[key].Px()*recoVecs[key].Py()
		mxz += recoVecs[key].Px()*recoVecs[key].Pz()
		myz += recoVecs[key].Py()*recoVecs[key].Pz()

	if Asum != 0.0:
		mxx = mxx/Asum
		myy = myy/Asum
		mzz = mzz/Asum
		mxy = mxy/Asum
		mxz = mxz/Asum
		myz = myz/Asum

		tensor = TMatrix(3,3)

		tensor[0][0] = mxx
		tensor[1][1] = myy
		tensor[2][2] = mzz
		tensor[0][1] = mxy
		tensor[1][0] = mxy 
		tensor[0][2] = mxz
		tensor[2][0] = mxz
		tensor[1][2] = myz
		tensor[2][1] = myz
		#tensor.Print()

		eigenval = TVector(3)
		tensor.EigenVectors(eigenval)
		#eigenval.Print()

		for i in range(0,2):
			for j in range(i+1,3):				
				if eigenval[i]< eigenval[j]:
					EG = eigenval[i]
					eigenval[i]= eigenval[j]
					eigenval[j] = EG

		#eigenval.Print()


		nnVARS_DICT['sphericity'] = 3.0*(eigenval[1]+eigenval[2])/2.0
		nnVARS_DICT['aplanarity'] = 3.0*eigenval[2]/2.0


	return


def writeHadTauParameters(nnVARS_DICT,chain, maxPairTypeAndIndex):
	i = maxPairTypeAndIndex[0]

	if maxPairTypeAndIndex[1] == 'muTau':
		nnVARS_DICT['tau_charge'] = 	  chain.muT_tau_charge[i]
		nnVARS_DICT['tau_decayMode'] = 	  chain.muT_tau_decayMode[i]
		nnVARS_DICT['tau_passFullId_muTau'] = 	  chain.muT_tau_passFullId_muTau[i]
		nnVARS_DICT['tau_passFullId_eTau'] = 	  chain.muT_tau_passFullId_eTau[i]
		nnVARS_DICT['tau_numStrips'] = 	  chain.muT_tau_numStrips[i]
		nnVARS_DICT['tau_numHadrons'] = 	  chain.muT_tau_numHadrons[i]
		nnVARS_DICT['tau_byCombinedIsolationDeltaBetaCorrRaw'] = 	  chain.muT_tau_byCombinedIsolationDeltaBetaCorrRaw[i]
		nnVARS_DICT['tau_byCombinedIsolationDeltaBetaCorrRaw3Hits'] = 	  chain.muT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits[i]
		nnVARS_DICT['tau_byIsolationMVA3newDMwLTraw'] = 	  chain.muT_tau_byIsolationMVA3newDMwLTraw[i]
		nnVARS_DICT['tau_byIsolationMVA3newDMwoLTraw'] = 	  chain.muT_tau_byIsolationMVA3newDMwoLTraw[i]
		nnVARS_DICT['tau_byIsolationMVA3oldDMwLTraw'] = 	  chain.muT_tau_byIsolationMVA3oldDMwLTraw[i]
		nnVARS_DICT['tau_byIsolationMVA3oldDMwoLTraw'] = 	  chain.muT_tau_byIsolationMVA3oldDMwoLTraw[i]
		nnVARS_DICT['tau_chargedIsoPtSum'] = 	  chain.muT_tau_chargedIsoPtSum[i]
		nnVARS_DICT['tau_decayModeFinding'] = 	  chain.muT_tau_decayModeFinding[i]
		nnVARS_DICT['tau_decayModeFindingNewDMs'] = 	  chain.muT_tau_decayModeFindingNewDMs[i]
		nnVARS_DICT['tau_decayModeFindingOldDMs'] = 	  chain.muT_tau_decayModeFindingOldDMs[i]
		nnVARS_DICT['tau_neutralIsoPtSum'] = 	  chain.muT_tau_neutralIsoPtSum[i]
		nnVARS_DICT['tau_puCorrPtSum'] = 	  chain.muT_tau_puCorrPtSum[i]
		nnVARS_DICT['tau_vertex_x'] = 	  chain.muT_tau_vertex_x[i]
		nnVARS_DICT['tau_vertex_y'] = 	  chain.muT_tau_vertex_y[i]
		nnVARS_DICT['tau_vertex_z'] = 	  chain.muT_tau_vertex_z[i]
		nnVARS_DICT['tau_vertex_theta'] = 	  chain.muT_tau_vertex_theta[i]
		nnVARS_DICT['tau_vertex_eta'] = 	  chain.muT_tau_vertex_eta[i]
		nnVARS_DICT['tau_vertex_phi'] = 	  chain.muT_tau_vertex_phi[i]
		nnVARS_DICT['PVpositionZ'] = 	  chain.muT_PVpositionZ[i]  
		nnVARS_DICT['tau_DZ'] =  	  (chain.muT_tau_vertex_z[i] - chain.muT_PVpositionZ[i])
	elif maxPairTypeAndIndex[1] == 'eleTau':
		nnVARS_DICT['tau_charge'] = 	  chain.eT_tau_charge[i]
		nnVARS_DICT['tau_decayMode'] = 	  chain.eT_tau_decayMode[i]
		nnVARS_DICT['tau_passFullId_muTau'] = 	  chain.eT_tau_passFullId_muTau[i]
		nnVARS_DICT['tau_passFullId_eTau'] = 	  chain.eT_tau_passFullId_eTau[i]
		nnVARS_DICT['tau_numStrips'] = 	  chain.eT_tau_numStrips[i]
		nnVARS_DICT['tau_numHadrons'] = 	  chain.eT_tau_numHadrons[i]
		nnVARS_DICT['tau_byCombinedIsolationDeltaBetaCorrRaw'] = 	  chain.eT_tau_byCombinedIsolationDeltaBetaCorrRaw[i]
		nnVARS_DICT['tau_byCombinedIsolationDeltaBetaCorrRaw3Hits'] = 	  chain.eT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits[i]
		nnVARS_DICT['tau_byIsolationMVA3newDMwLTraw'] = 	  chain.eT_tau_byIsolationMVA3newDMwLTraw[i]
		nnVARS_DICT['tau_byIsolationMVA3newDMwoLTraw'] = 	  chain.eT_tau_byIsolationMVA3newDMwoLTraw[i]
		nnVARS_DICT['tau_byIsolationMVA3oldDMwLTraw'] = 	  chain.eT_tau_byIsolationMVA3oldDMwLTraw[i]
		nnVARS_DICT['tau_byIsolationMVA3oldDMwoLTraw'] = 	  chain.eT_tau_byIsolationMVA3oldDMwoLTraw[i]
		nnVARS_DICT['tau_chargedIsoPtSum'] = 	  chain.eT_tau_chargedIsoPtSum[i]
		nnVARS_DICT['tau_decayModeFinding'] = 	  chain.eT_tau_decayModeFinding[i]
		nnVARS_DICT['tau_decayModeFindingNewDMs'] = 	  chain.eT_tau_decayModeFindingNewDMs[i]
		nnVARS_DICT['tau_decayModeFindingOldDMs'] = 	  chain.eT_tau_decayModeFindingOldDMs[i]
		nnVARS_DICT['tau_neutralIsoPtSum'] = 	  chain.eT_tau_neutralIsoPtSum[i]
		nnVARS_DICT['tau_puCorrPtSum'] = 	  chain.eT_tau_puCorrPtSum[i]
		nnVARS_DICT['tau_vertex_x'] = 	  chain.eT_tau_vertex_x[i]
		nnVARS_DICT['tau_vertex_y'] = 	  chain.eT_tau_vertex_y[i]
		nnVARS_DICT['tau_vertex_theta'] = 	  chain.eT_tau_vertex_theta[i]
		nnVARS_DICT['tau_vertex_eta'] = 	  chain.eT_tau_vertex_eta[i]
		nnVARS_DICT['tau_vertex_phi'] = 	  chain.eT_tau_vertex_phi[i]
		nnVARS_DICT['tau_vertex_z'] =  	  chain.eT_tau_vertex_z[i]
		nnVARS_DICT['PVpositionZ'] = 	  chain.eT_PVpositionZ[i]  
		nnVARS_DICT['tau_DZ'] =  	  (chain.eT_tau_vertex_z[i] - chain.eT_PVpositionZ[i])
	 	
	return

def writeLepTauParameters(nnVARS_DICT,chain, maxPairTypeAndIndex):
	i = maxPairTypeAndIndex[0]

	if maxPairTypeAndIndex[1] == 'muTau':

		nnVARS_DICT['lep_dB'] = chain.muT_muon_dB[i]
		nnVARS_DICT['lep_dz'] = chain.muT_muon_dz[i]
		nnVARS_DICT['lep_dxy'] =    chain.muT_muon_dxy[i]
		nnVARS_DICT['lep_Charge'] =    chain.muT_muon_charge[i]
		nnVARS_DICT['lep_relIso'] =  chain.muT_muon_relativeIso_DR4[i]
		nnVARS_DICT['muon_isGlobalMuon'] = chain.muT_muon_isGlobalMuon[i]
		nnVARS_DICT['muon_isTightMuon'] = chain.muT_muon_isTightMuon[i]
		nnVARS_DICT['muon_isPFMuon'] = chain.muT_muon_isPFMuon[i]
		nnVARS_DICT['muon_isLooseMuon'] = chain.muT_muon_isLooseMuon[i]
		nnVARS_DICT['muon_numberOfValidMuonHits'] = chain.muT_muon_numberOfValidMuonHits[i]
		nnVARS_DICT['muon_numberOfMatchedStations'] = chain.muT_muon_numberOfMatchedStations[i]
		nnVARS_DICT['muon_numberOfValidPixelHits'] = chain.muT_muon_numberOfValidPixelHits[i]
		nnVARS_DICT['muon_trackerLayersWithMeasurement'] = chain.muT_muon_trackerLayersWithMeasurement[i]
		nnVARS_DICT['muon_passFullId'] = chain.muT_muon_passFullId[i]
		nnVARS_DICT['muon_isTrackerMuon'] = chain.muT_muon_isTrackerMuon[i]
		nnVARS_DICT['muon_sumChargedParticlePt_DR4'] = chain.muT_muon_sumChargedParticlePt_DR4[i]
		nnVARS_DICT['muon_sumPhotonEt_DR4'] = chain.muT_muon_sumPhotonEt_DR4[i]
		nnVARS_DICT['muon_sumNeutralHadronEt_DR4'] = chain.muT_muon_sumNeutralHadronEt_DR4[i]
		nnVARS_DICT['muon_sumPUPt_DR4'] = chain.muT_muon_sumPUPt_DR4[i]
		nnVARS_DICT['muon_normalizedChi2'] = chain.muT_muon_normalizedChi2[i]
		nnVARS_DICT['isLEPmuon'] = 1
		nnVARS_DICT['isLEPelectron'] = 0

	elif maxPairTypeAndIndex[1] == 'eleTau':

		nnVARS_DICT['lep_dB'] = chain.eT_ele_dB[i]
		nnVARS_DICT['lep_dz'] =  chain.eT_ele_dz[i]
		nnVARS_DICT['lep_dxy'] =    chain.eT_ele_dxy[i]
		nnVARS_DICT['lep_Charge'] = chain.eT_ele_charge[i]
		nnVARS_DICT['lep_relIso'] =  chain.eT_ele_relativeIso[i]
		nnVARS_DICT['ele_numberOfMissingInnerHits'] = chain.eT_ele_numberOfMissingInnerHits[i]
		nnVARS_DICT['ele_passConversionVeto'] = chain.eT_ele_passConversionVeto[i]
		nnVARS_DICT['ele_SuperClusterEta'] = chain.eT_ele_SuperClusterEta[i]
		nnVARS_DICT['ele_mvaTrigV0'] = chain.eT_ele_mvaTrigV0[i]
		nnVARS_DICT['ele_mvaTrigNoIPV0'] = chain.eT_ele_mvaTrigNoIPV0[i]
		nnVARS_DICT['ele_mvaNonTrigV0'] = chain.eT_ele_mvaNonTrigV0[i]
		nnVARS_DICT['ele_pass_tight_mvaNonTrigV0'] = chain.eT_ele_pass_tight_mvaNonTrigV0[i]
		nnVARS_DICT['ele_passFullId'] = chain.eT_ele_passFullId[i]
		nnVARS_DICT['ele_chargedHadronIso'] = chain.eT_ele_chargedHadronIso[i]
		nnVARS_DICT['ele_photonIso'] = chain.eT_ele_photonIso[i]
		nnVARS_DICT['ele_neutralHadronIso'] = chain.eT_ele_neutralHadronIso[i]
		nnVARS_DICT['ele_puChargedHadronIso'] = chain.eT_ele_puChargedHadronIso[i]
		nnVARS_DICT['ele_isEB'] = chain.eT_ele_isEB[i]
		nnVARS_DICT['ele_isEE'] = chain.eT_ele_isEE[i]
		nnVARS_DICT['ele_isEBEEGap'] = chain.eT_ele_isEBEEGap[i]
		nnVARS_DICT['ele_isEBEtaGap'] = chain.eT_ele_isEBEtaGap[i]
		nnVARS_DICT['ele_isEBPhiGap'] = chain.eT_ele_isEBPhiGap[i]
		nnVARS_DICT['ele_isEEDeeGap'] = chain.eT_ele_isEEDeeGap[i]
		nnVARS_DICT['ele_isEERingGap'] = chain.eT_ele_isEERingGap[i]
		nnVARS_DICT['ele_sigmaEtaEta'] = chain.eT_ele_sigmaEtaEta[i]
		nnVARS_DICT['ele_sigmaIetaIeta'] = chain.eT_ele_sigmaIetaIeta[i]
		nnVARS_DICT['ele_sigmaIphiIphi'] = chain.eT_ele_sigmaIphiIphi[i]
		nnVARS_DICT['ele_deltaPhiSuperClusterTrackAtVtx'] = chain.eT_ele_deltaPhiSuperClusterTrackAtVtx[i]
		nnVARS_DICT['ele_deltaEtaSuperClusterTrackAtVtx'] = chain.eT_ele_deltaEtaSuperClusterTrackAtVtx[i]
		nnVARS_DICT['ele_hadronicOverEm'] = chain.eT_ele_hadronicOverEm[i]
		nnVARS_DICT['isLEPmuon'] = 0
		nnVARS_DICT['isLEPelectron'] = 1

	return

def writeGenInfo(genVecs,nnVARS_DICT):

	nnVARS_DICT['GENtauPt'] = genVecs['genHadTau'].Pt()
	nnVARS_DICT['GENtauEta'] = genVecs['genHadTau'].Eta()
	nnVARS_DICT['GENtauPhi'] = genVecs['genHadTau'].Phi()
	nnVARS_DICT['GENtauM'] = genVecs['genHadTau'].M()
	nnVARS_DICT['GENlepPt'] = genVecs['genLepTau'].Pt()
	nnVARS_DICT['GENlepEta'] = genVecs['genLepTau'].Eta()
	nnVARS_DICT['GENlepPhi'] = genVecs['genLepTau'].Phi()
	nnVARS_DICT['GENlepM'] = genVecs['genLepTau'].M()
	nnVARS_DICT['GENdiTauMass'] = (genVecs['genHadTau'] + genVecs['genLepTau']).M()


	return

