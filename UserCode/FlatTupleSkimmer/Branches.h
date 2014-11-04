#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>

// Header file for the classes stored in the TTree if any.
#include <string>
#include <vector>
#include <iostream>

using namespace std;

TTree          *fChain;   //!pointer to the analyzed TTree or TChain


// Declaration of leaf types
UInt_t          run;
UInt_t          luminosityBlock;
UInt_t          event;
Bool_t          isRealData;
Int_t           bunchCrossing;
Int_t           orbitNumber;
string          *NAMEVAR;
string          *SampleName;
string          *PhysicsProcess;
Bool_t          isNonTopEmbeddedSample;
Bool_t          isTopEmbeddedSample;
Double_t        MASS;
Double_t        crossSection;
Double_t        branchingFraction;
Int_t           numberEvents;
vector<double>  *eT_p4_x;
vector<double>  *eT_p4_y;
vector<double>  *eT_p4_z;
vector<double>  *eT_p4_t;
vector<double>  *eT_corrected_p4_x;
vector<double>  *eT_corrected_p4_y;
vector<double>  *eT_corrected_p4_z;
vector<double>  *eT_corrected_p4_t;
vector<int>     *eT_electronIndex;
vector<int>     *eT_tauIndex;
vector<double>  *eT_scalarSumPt;
vector<double>  *eT_DR;
vector<int>     *eT_sumCharge;
vector<double>  *eT_correctedSVFitMass;
vector<double>  *eT_rawSVFitMass;
vector<double>  *eT_TransverseMass;
vector<double>  *eT_rawTransverseMass;
vector<double>  *eT_mvaMETraw;
vector<double>  *eT_mvaMET;
vector<double>  *eT_mvaMETphiRaw;
vector<double>  *eT_mvaMETphi;
vector<int>     *eT_MAX;
vector<bool>    *eT_isGoodTriggerPair;
vector<int>     *eT_njets;
vector<int>     *eT_nbjets;
vector<int>     *eT_nbjetsLOOSE;
vector<int>     *eT_nbjetsLOOSEUP;
vector<int>     *eT_nbjetsLOOSEDOWN;
vector<int>     *eT_njetsUP;
vector<int>     *eT_nbjetsUP;
vector<int>     *eT_njetsDOWN;
vector<int>     *eT_nbjetsDOWN;
vector<double>  *eT_jet1P4_x;
vector<double>  *eT_jet1P4_y;
vector<double>  *eT_jet1P4_z;
vector<double>  *eT_jet1P4_t;
vector<double>  *eT_jet1RawP4_x;
vector<double>  *eT_jet1RawP4_y;
vector<double>  *eT_jet1RawP4_z;
vector<double>  *eT_jet1RawP4_t;
vector<double>  *eT_jet1IDMVA;
vector<double>  *eT_jet1BTAGMVA;
vector<double>  *eT_jet2P4_x;
vector<double>  *eT_jet2P4_y;
vector<double>  *eT_jet2P4_z;
vector<double>  *eT_jet2P4_t;
vector<double>  *eT_jet2RawP4_x;
vector<double>  *eT_jet2RawP4_y;
vector<double>  *eT_jet2RawP4_z;
vector<double>  *eT_jet2RawP4_t;
vector<double>  *eT_jet2IDMVA;
vector<double>  *eT_jet2BTAGMVA;
vector<double>  *eT_cov00;
vector<double>  *eT_cov01;
vector<double>  *eT_cov10;
vector<double>  *eT_cov11;
vector<bool>    *eT_passesTriLeptonVeto;
vector<bool>    *eT_passNonTopEmbeddedTriggerAndMass50;
vector<bool>    *eT_passSignalGeneratorMass70to130Cut;
vector<double>  *eT_genBosonP4_x;
vector<double>  *eT_genBosonP4_y;
vector<double>  *eT_genBosonP4_z;
vector<double>  *eT_genBosonP4_t;
vector<double>  *eT_genTOPp4_x;
vector<double>  *eT_genTOPp4_y;
vector<double>  *eT_genTOPp4_z;
vector<double>  *eT_genTOPp4_t;
vector<double>  *eT_genTOPBARp4_x;
vector<double>  *eT_genTOPBARp4_y;
vector<double>  *eT_genTOPBARp4_z;
vector<double>  *eT_genTOPBARp4_t;
vector<int>     *eT_numberOfGoodVertices;
vector<int>     *eT_PVndof;
vector<double>  *eT_PVz;
vector<double>  *eT_PVpositionRho;
vector<double>  *eT_PVp4_x;
vector<double>  *eT_PVp4_y;
vector<double>  *eT_PVp4_z;
vector<double>  *eT_PVp4_t;
vector<bool>    *eT_isDecayZtauTau;
vector<bool>    *eT_isDecayZeE;
vector<bool>    *eT_isDecayZmuMu;
vector<bool>    *eT_isRecoLep_matchedTo_GenTauFromZ;
vector<bool>    *eT_isRecoTau_matchedTo_GenTauFromZ;
vector<bool>    *eT_isRecoLep_matchedTo_GenElecFromZ;
vector<bool>    *eT_isRecoTau_matchedTo_GenElecFromZ;
vector<bool>    *eT_isRecoLep_matchedTo_GenMuonFromZ;
vector<bool>    *eT_isRecoTau_matchedTo_GenMuonFromZ;
vector<bool>    *eT_isRecoLep_matchedTo_GenElecFromTau;
vector<bool>    *eT_isRecoTau_matchedTo_GenElecFromTau;
vector<bool>    *eT_isRecoLep_matchedTo_GenMuonFromTau;
vector<bool>    *eT_isRecoTau_matchedTo_GenMuonFromTau;
vector<bool>    *eT_passEmbeddedTrigger;
vector<double>  *eT_ele_p4_x;
vector<double>  *eT_ele_p4_y;
vector<double>  *eT_ele_p4_z;
vector<double>  *eT_ele_p4_t;
vector<double>  *eT_ele_genP4_x;
vector<double>  *eT_ele_genP4_y;
vector<double>  *eT_ele_genP4_z;
vector<double>  *eT_ele_genP4_t;
vector<double>  *eT_ele_pfP4_x;
vector<double>  *eT_ele_pfP4_y;
vector<double>  *eT_ele_pfP4_z;
vector<double>  *eT_ele_pfP4_t;
vector<int>     *eT_ele_charge;
vector<int>     *eT_ele_PFpdgId;
vector<int>     *eT_ele_GENpdgId;
vector<int>     *eT_ele_numberOfMissingInnerHits;
vector<bool>    *eT_ele_passConversionVeto;
vector<double>  *eT_ele_dz;
vector<double>  *eT_ele_dB;
vector<double>  *eT_ele_dxy;
vector<double>  *eT_ele_SuperClusterEta;
vector<double>  *eT_ele_mvaTrigV0;
vector<double>  *eT_ele_mvaTrigNoIPV0;
vector<double>  *eT_ele_mvaNonTrigV0;
vector<bool>    *eT_ele_pass_tight_mvaNonTrigV0;
vector<bool>    *eT_ele_passFullId;
vector<double>  *eT_ele_chargedHadronIso;
vector<double>  *eT_ele_photonIso;
vector<double>  *eT_ele_neutralHadronIso;
vector<double>  *eT_ele_puChargedHadronIso;
vector<double>  *eT_ele_relativeIso;
vector<bool>    *eT_ele_isEB;
vector<bool>    *eT_ele_isEE;
vector<bool>    *eT_ele_isEBEEGap;
vector<bool>    *eT_ele_isEBEtaGap;
vector<bool>    *eT_ele_isEBPhiGap;
vector<bool>    *eT_ele_isEEDeeGap;
vector<bool>    *eT_ele_isEERingGap;
vector<double>  *eT_ele_sigmaEtaEta;
vector<double>  *eT_ele_sigmaIetaIeta;
vector<double>  *eT_ele_sigmaIphiIphi;
vector<bool>    *eT_ele_has_HltMatchEle20;
vector<bool>    *eT_ele_has_HltMatchEle22;
vector<bool>    *eT_ele_has_HltMatchEle27;
vector<bool>    *eT_ele_isTriLeptonVetoCandidate;
vector<double>  *eT_ele_deltaPhiSuperClusterTrackAtVtx;
vector<double>  *eT_ele_deltaEtaSuperClusterTrackAtVtx;
vector<double>  *eT_ele_hadronicOverEm;
vector<double>  *eT_tau_pfJetRefP4_x;
vector<double>  *eT_tau_pfJetRefP4_y;
vector<double>  *eT_tau_pfJetRefP4_z;
vector<double>  *eT_tau_pfJetRefP4_t;
vector<double>  *eT_tau_p4_x;
vector<double>  *eT_tau_p4_y;
vector<double>  *eT_tau_p4_z;
vector<double>  *eT_tau_p4_t;
vector<double>  *eT_tau_genP4_x;
vector<double>  *eT_tau_genP4_y;
vector<double>  *eT_tau_genP4_z;
vector<double>  *eT_tau_genP4_t;
vector<double>  *eT_tau_genJet_x;
vector<double>  *eT_tau_genJet_y;
vector<double>  *eT_tau_genJet_z;
vector<double>  *eT_tau_genJet_t;
vector<double>  *eT_tau_corrected_p4_x;
vector<double>  *eT_tau_corrected_p4_y;
vector<double>  *eT_tau_corrected_p4_z;
vector<double>  *eT_tau_corrected_p4_t;
vector<int>     *eT_tau_pdgId;
vector<int>     *eT_tau_pdgIdGEN;
vector<int>     *eT_tau_charge;
vector<int>     *eT_tau_decayMode;
vector<bool>    *eT_tau_passFullId_muTau;
vector<bool>    *eT_tau_passFullId_eTau;
vector<int>     *eT_tau_numStrips;
vector<int>     *eT_tau_numHadrons;
vector<float>   *eT_tau_againstElectronDeadECAL;
vector<float>   *eT_tau_againstElectronLoose;
vector<float>   *eT_tau_againstElectronLooseMVA5;
vector<float>   *eT_tau_againstElectronMVA5category;
vector<float>   *eT_tau_againstElectronMVA5raw;
vector<float>   *eT_tau_againstElectronMedium;
vector<float>   *eT_tau_againstElectronMediumMVA5;
vector<float>   *eT_tau_againstElectronTight;
vector<float>   *eT_tau_againstElectronTightMVA5;
vector<float>   *eT_tau_againstElectronVLooseMVA5;
vector<float>   *eT_tau_againstElectronVTightMVA5;
vector<float>   *eT_tau_againstMuonLoose;
vector<float>   *eT_tau_againstMuonLoose2;
vector<float>   *eT_tau_againstMuonLoose3;
vector<float>   *eT_tau_againstMuonLooseMVA;
vector<float>   *eT_tau_againstMuonMVAraw;
vector<float>   *eT_tau_againstMuonMedium;
vector<float>   *eT_tau_againstMuonMedium2;
vector<float>   *eT_tau_againstMuonMediumMVA;
vector<float>   *eT_tau_againstMuonTight;
vector<float>   *eT_tau_againstMuonTight2;
vector<float>   *eT_tau_againstMuonTight3;
vector<float>   *eT_tau_againstMuonTightMVA;
vector<float>   *eT_tau_byCombinedIsolationDeltaBetaCorrRaw;
vector<float>   *eT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits;
vector<float>   *eT_tau_byIsolationMVA3newDMwLTraw;
vector<float>   *eT_tau_byIsolationMVA3newDMwoLTraw;
vector<float>   *eT_tau_byIsolationMVA3oldDMwLTraw;
vector<float>   *eT_tau_byIsolationMVA3oldDMwoLTraw;
vector<float>   *eT_tau_byLooseCombinedIsolationDeltaBetaCorr;
vector<float>   *eT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits;
vector<float>   *eT_tau_byLooseIsolation;
vector<float>   *eT_tau_byLooseIsolationMVA3newDMwLT;
vector<float>   *eT_tau_byLooseIsolationMVA3newDMwoLT;
vector<float>   *eT_tau_byLooseIsolationMVA3oldDMwLT;
vector<float>   *eT_tau_byLooseIsolationMVA3oldDMwoLT;
vector<float>   *eT_tau_byMediumCombinedIsolationDeltaBetaCorr;
vector<float>   *eT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits;
vector<float>   *eT_tau_byMediumIsolationMVA3newDMwLT;
vector<float>   *eT_tau_byMediumIsolationMVA3newDMwoLT;
vector<float>   *eT_tau_byMediumIsolationMVA3oldDMwLT;
vector<float>   *eT_tau_byMediumIsolationMVA3oldDMwoLT;
vector<float>   *eT_tau_byTightCombinedIsolationDeltaBetaCorr;
vector<float>   *eT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits;
vector<float>   *eT_tau_byTightIsolationMVA3newDMwLT;
vector<float>   *eT_tau_byTightIsolationMVA3newDMwoLT;
vector<float>   *eT_tau_byTightIsolationMVA3oldDMwLT;
vector<float>   *eT_tau_byTightIsolationMVA3oldDMwoLT;
vector<float>   *eT_tau_byVLooseCombinedIsolationDeltaBetaCorr;
vector<float>   *eT_tau_byVLooseIsolationMVA3newDMwLT;
vector<float>   *eT_tau_byVLooseIsolationMVA3newDMwoLT;
vector<float>   *eT_tau_byVLooseIsolationMVA3oldDMwLT;
vector<float>   *eT_tau_byVLooseIsolationMVA3oldDMwoLT;
vector<float>   *eT_tau_byVTightIsolationMVA3newDMwLT;
vector<float>   *eT_tau_byVTightIsolationMVA3newDMwoLT;
vector<float>   *eT_tau_byVTightIsolationMVA3oldDMwLT;
vector<float>   *eT_tau_byVTightIsolationMVA3oldDMwoLT;
vector<float>   *eT_tau_byVVTightIsolationMVA3newDMwLT;
vector<float>   *eT_tau_byVVTightIsolationMVA3newDMwoLT;
vector<float>   *eT_tau_byVVTightIsolationMVA3oldDMwLT;
vector<float>   *eT_tau_byVVTightIsolationMVA3oldDMwoLT;
vector<float>   *eT_tau_chargedIsoPtSum;
vector<float>   *eT_tau_decayModeFinding;
vector<float>   *eT_tau_decayModeFindingNewDMs;
vector<float>   *eT_tau_decayModeFindingOldDMs;
vector<float>   *eT_tau_neutralIsoPtSum;
vector<float>   *eT_tau_puCorrPtSum;
vector<bool>    *eT_tau_has_HltMatchEle20;
vector<bool>    *eT_tau_has_HltMatchEle22;
vector<bool>    *eT_tau_has_HltMatchEle27;
vector<bool>    *eT_tau_has_HltMatchMu17;
vector<bool>    *eT_tau_has_HltMatchMu18;
vector<bool>    *eT_tau_has_HltMatchMu24;
vector<double>  *eT_puWeight;
vector<double>  *eT_puWeightM1;
vector<double>  *eT_puWeightP1;
vector<float>   *eT_NumPileupInt;
vector<float>   *eT_NumTruePileUpInt;
vector<float>   *eT_NumPileupIntM1;
vector<float>   *eT_NumTruePileUpIntM1;
vector<float>   *eT_NumPileupIntP1;
vector<float>   *eT_NumTruePileUpIntP1;
vector<double>  *eT_EffDataELE20andELE22;
vector<double>  *eT_EffMcELE20andELE22;
vector<double>  *eT_HadronicTauDataTrigEffAntiEMed;
vector<double>  *eT_HadronicTauMcTrigEffAntiEMed;
vector<double>  *eT_HadronicTauDataTrigEffAntiETight;
vector<double>  *eT_HadronicTauMcTrigEffAntiETight;
vector<double>  *eT_electronDataIDweight;
vector<double>  *eT_electronMcIDweight;
vector<double>  *eT_electronDataISOLweight;
vector<double>  *eT_electronMcISOLweight;
vector<double>  *eT_EffDataHighPtTauTrigger;
vector<double>  *eT_EffMcHighPtTauTrigger;
vector<double>  *eT_TauFakeCorrection;
vector<double>  *eT_DecayModeCorrectionFactor;
vector<double>  *eT_ZeeScaleFactor;
vector<double>  *eT_nominalHIGLUXHQTmhmax;
vector<double>  *eT_upHIGLUXHQTmhmax;
vector<double>  *eT_downHIGLUXHQTmhmax;
vector<double>  *eT_nominalPOWHEGmhmod;
vector<double>  *eT_upPOWHEGmhmod;
vector<double>  *eT_downPOWHEGmhmod;
vector<double>  *eT_upPOWHEGscale;
vector<double>  *eT_downPOWHEGscale;
vector<double>  *eT_etaDepQCDShapeTemplateCorrection;
vector<double>  *eT_inclusiveQCDShapeTemplateCorrection;
vector<double>  *eT_TTbarPtWeight;
vector<double>  *eT_TauSpinnerWT;
vector<double>  *eT_TauSpinnerWTFlip;
vector<double>  *eT_TauSpinnerWThminus;
vector<double>  *eT_TauSpinnerWThplus;
vector<int>     *eT_hepNUP;
vector<double>  *eT_weightHEPNUP_DYJets;
vector<double>  *eT_weightHEPNUP_WJets;
vector<bool>    *eT_passesSecondLeptonVeto;
vector<bool>    *eT_passesThirdLeptonVeto;
vector<double>  *muT_p4_x;
vector<double>  *muT_p4_y;
vector<double>  *muT_p4_z;
vector<double>  *muT_p4_t;
vector<double>  *muT_corrected_p4_x;
vector<double>  *muT_corrected_p4_y;
vector<double>  *muT_corrected_p4_z;
vector<double>  *muT_corrected_p4_t;
vector<int>     *muT_muonIndex;
vector<int>     *muT_tauIndex;
vector<double>  *muT_scalarSumPt;
vector<double>  *muT_DR;
vector<int>     *muT_sumCharge;
vector<double>  *muT_correctedSVFitMass;
vector<double>  *muT_rawSVFitMass;
vector<double>  *muT_TransverseMass;
vector<double>  *muT_rawTransverseMass;
vector<double>  *muT_mvaMETraw;
vector<double>  *muT_mvaMET;
vector<double>  *muT_mvaMETphiRaw;
vector<double>  *muT_mvaMETphi;
vector<int>     *muT_MAX;
vector<bool>    *muT_isGoodTriggerPair;
vector<int>     *muT_njets;
vector<int>     *muT_nbjets;
vector<int>     *muT_nbjetsLOOSE;
vector<int>     *muT_nbjetsLOOSEUP;
vector<int>     *muT_nbjetsLOOSEDOWN;
vector<int>     *muT_njetsUP;
vector<int>     *muT_nbjetsUP;
vector<int>     *muT_njetsDOWN;
vector<int>     *muT_nbjetsDOWN;
vector<double>  *muT_jet1P4_x;
vector<double>  *muT_jet1P4_y;
vector<double>  *muT_jet1P4_z;
vector<double>  *muT_jet1P4_t;
vector<double>  *muT_jet1RawP4_x;
vector<double>  *muT_jet1RawP4_y;
vector<double>  *muT_jet1RawP4_z;
vector<double>  *muT_jet1RawP4_t;
vector<double>  *muT_jet1IDMVA;
vector<double>  *muT_jet1BTAGMVA;
vector<double>  *muT_jet2P4_x;
vector<double>  *muT_jet2P4_y;
vector<double>  *muT_jet2P4_z;
vector<double>  *muT_jet2P4_t;
vector<double>  *muT_jet2RawP4_x;
vector<double>  *muT_jet2RawP4_y;
vector<double>  *muT_jet2RawP4_z;
vector<double>  *muT_jet2RawP4_t;
vector<double>  *muT_jet2IDMVA;
vector<double>  *muT_jet2BTAGMVA;
vector<double>  *muT_cov00;
vector<double>  *muT_cov01;
vector<double>  *muT_cov10;
vector<double>  *muT_cov11;
vector<bool>    *muT_passesTriLeptonVeto;
vector<bool>    *muT_passNonTopEmbeddedTriggerAndMass50;
vector<bool>    *muT_passSignalGeneratorMass70to130Cut;
vector<double>  *muT_genBosonP4_x;
vector<double>  *muT_genBosonP4_y;
vector<double>  *muT_genBosonP4_z;
vector<double>  *muT_genBosonP4_t;
vector<double>  *muT_genTOPp4_x;
vector<double>  *muT_genTOPp4_y;
vector<double>  *muT_genTOPp4_z;
vector<double>  *muT_genTOPp4_t;
vector<double>  *muT_genTOPBARp4_x;
vector<double>  *muT_genTOPBARp4_y;
vector<double>  *muT_genTOPBARp4_z;
vector<double>  *muT_genTOPBARp4_t;
vector<int>     *muT_numberOfGoodVertices;
vector<int>     *muT_PVndof;
vector<double>  *muT_PVz;
vector<double>  *muT_PVpositionRho;
vector<double>  *muT_PVp4_x;
vector<double>  *muT_PVp4_y;
vector<double>  *muT_PVp4_z;
vector<double>  *muT_PVp4_t;
vector<bool>    *muT_isDecayZtauTau;
vector<bool>    *muT_isDecayZeE;
vector<bool>    *muT_isDecayZmuMu;
vector<bool>    *muT_isRecoLep_matchedTo_GenTauFromZ;
vector<bool>    *muT_isRecoTau_matchedTo_GenTauFromZ;
vector<bool>    *muT_isRecoLep_matchedTo_GenElecFromZ;
vector<bool>    *muT_isRecoTau_matchedTo_GenElecFromZ;
vector<bool>    *muT_isRecoLep_matchedTo_GenMuonFromZ;
vector<bool>    *muT_isRecoTau_matchedTo_GenMuonFromZ;
vector<bool>    *muT_isRecoLep_matchedTo_GenElecFromTau;
vector<bool>    *muT_isRecoTau_matchedTo_GenElecFromTau;
vector<bool>    *muT_isRecoLep_matchedTo_GenMuonFromTau;
vector<bool>    *muT_isRecoTau_matchedTo_GenMuonFromTau;
vector<bool>    *muT_passEmbeddedTrigger;
vector<double>  *muT_muon_p4_x;
vector<double>  *muT_muon_p4_y;
vector<double>  *muT_muon_p4_z;
vector<double>  *muT_muon_p4_t;
vector<double>  *muT_muon_pfP4_x;
vector<double>  *muT_muon_pfP4_y;
vector<double>  *muT_muon_pfP4_z;
vector<double>  *muT_muon_pfP4_t;
vector<double>  *muT_muon_genP4_x;
vector<double>  *muT_muon_genP4_y;
vector<double>  *muT_muon_genP4_z;
vector<double>  *muT_muon_genP4_t;
vector<bool>    *muT_muon_isGlobalMuon;
vector<bool>    *muT_muon_isTightMuon;
vector<bool>    *muT_muon_isPFMuon;
vector<bool>    *muT_muon_isLooseMuon;
vector<double>  *muT_muon_sumChargedParticlePt_DR4;
vector<double>  *muT_muon_sumPhotonEt_DR4;
vector<double>  *muT_muon_sumNeutralHadronEt_DR4;
vector<double>  *muT_muon_sumPUPt_DR4;
vector<double>  *muT_muon_relativeIso_DR4;
vector<double>  *muT_muon_sumChargedParticlePt_DR3;
vector<double>  *muT_muon_sumPhotonEt_DR3;
vector<double>  *muT_muon_sumNeutralHadronEt_DR3;
vector<double>  *muT_muon_sumPUPt_DR3;
vector<double>  *muT_muon_relativeIso_DR3;
vector<bool>    *muT_muon_isPFIsolationValid;
vector<int>     *muT_muon_charge;
vector<int>     *muT_muon_PFpdgId;
vector<int>     *muT_muon_GENpdgId;
vector<double>  *muT_muon_normalizedChi2;
vector<int>     *muT_muon_numberOfValidMuonHits;
vector<int>     *muT_muon_numberOfMatchedStations;
vector<int>     *muT_muon_numberOfValidPixelHits;
vector<int>     *muT_muon_trackerLayersWithMeasurement;
vector<double>  *muT_muon_dB;
vector<double>  *muT_muon_dz;
vector<double>  *muT_muon_dxy;
vector<bool>    *muT_muon_passFullId;
vector<bool>    *muT_muon_has_HltMatchMu17;
vector<bool>    *muT_muon_has_HltMatchMu18;
vector<bool>    *muT_muon_has_HltMatchMu24;
vector<bool>    *muT_muon_isTriLeptonVetoCandidate;
vector<bool>    *muT_muon_isTrackerMuon;
vector<double>  *muT_tau_pfJetRefP4_x;
vector<double>  *muT_tau_pfJetRefP4_y;
vector<double>  *muT_tau_pfJetRefP4_z;
vector<double>  *muT_tau_pfJetRefP4_t;
vector<double>  *muT_tau_p4_x;
vector<double>  *muT_tau_p4_y;
vector<double>  *muT_tau_p4_z;
vector<double>  *muT_tau_p4_t;
vector<double>  *muT_tau_genP4_x;
vector<double>  *muT_tau_genP4_y;
vector<double>  *muT_tau_genP4_z;
vector<double>  *muT_tau_genP4_t;
vector<double>  *muT_tau_genJet_x;
vector<double>  *muT_tau_genJet_y;
vector<double>  *muT_tau_genJet_z;
vector<double>  *muT_tau_genJet_t;
vector<double>  *muT_tau_corrected_p4_x;
vector<double>  *muT_tau_corrected_p4_y;
vector<double>  *muT_tau_corrected_p4_z;
vector<double>  *muT_tau_corrected_p4_t;
vector<int>     *muT_tau_pdgId;
vector<int>     *muT_tau_pdgIdGEN;
vector<int>     *muT_tau_charge;
vector<int>     *muT_tau_decayMode;
vector<bool>    *muT_tau_passFullId_muTau;
vector<bool>    *muT_tau_passFullId_eTau;
vector<int>     *muT_tau_numStrips;
vector<int>     *muT_tau_numHadrons;
vector<float>   *muT_tau_againstElectronDeadECAL;
vector<float>   *muT_tau_againstElectronLoose;
vector<float>   *muT_tau_againstElectronLooseMVA5;
vector<float>   *muT_tau_againstElectronMVA5category;
vector<float>   *muT_tau_againstElectronMVA5raw;
vector<float>   *muT_tau_againstElectronMedium;
vector<float>   *muT_tau_againstElectronMediumMVA5;
vector<float>   *muT_tau_againstElectronTight;
vector<float>   *muT_tau_againstElectronTightMVA5;
vector<float>   *muT_tau_againstElectronVLooseMVA5;
vector<float>   *muT_tau_againstElectronVTightMVA5;
vector<float>   *muT_tau_againstMuonLoose;
vector<float>   *muT_tau_againstMuonLoose2;
vector<float>   *muT_tau_againstMuonLoose3;
vector<float>   *muT_tau_againstMuonLooseMVA;
vector<float>   *muT_tau_againstMuonMVAraw;
vector<float>   *muT_tau_againstMuonMedium;
vector<float>   *muT_tau_againstMuonMedium2;
vector<float>   *muT_tau_againstMuonMediumMVA;
vector<float>   *muT_tau_againstMuonTight;
vector<float>   *muT_tau_againstMuonTight2;
vector<float>   *muT_tau_againstMuonTight3;
vector<float>   *muT_tau_againstMuonTightMVA;
vector<float>   *muT_tau_byCombinedIsolationDeltaBetaCorrRaw;
vector<float>   *muT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits;
vector<float>   *muT_tau_byIsolationMVA3newDMwLTraw;
vector<float>   *muT_tau_byIsolationMVA3newDMwoLTraw;
vector<float>   *muT_tau_byIsolationMVA3oldDMwLTraw;
vector<float>   *muT_tau_byIsolationMVA3oldDMwoLTraw;
vector<float>   *muT_tau_byLooseCombinedIsolationDeltaBetaCorr;
vector<float>   *muT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits;
vector<float>   *muT_tau_byLooseIsolation;
vector<float>   *muT_tau_byLooseIsolationMVA3newDMwLT;
vector<float>   *muT_tau_byLooseIsolationMVA3newDMwoLT;
vector<float>   *muT_tau_byLooseIsolationMVA3oldDMwLT;
vector<float>   *muT_tau_byLooseIsolationMVA3oldDMwoLT;
vector<float>   *muT_tau_byMediumCombinedIsolationDeltaBetaCorr;
vector<float>   *muT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits;
vector<float>   *muT_tau_byMediumIsolationMVA3newDMwLT;
vector<float>   *muT_tau_byMediumIsolationMVA3newDMwoLT;
vector<float>   *muT_tau_byMediumIsolationMVA3oldDMwLT;
vector<float>   *muT_tau_byMediumIsolationMVA3oldDMwoLT;
vector<float>   *muT_tau_byTightCombinedIsolationDeltaBetaCorr;
vector<float>   *muT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits;
vector<float>   *muT_tau_byTightIsolationMVA3newDMwLT;
vector<float>   *muT_tau_byTightIsolationMVA3newDMwoLT;
vector<float>   *muT_tau_byTightIsolationMVA3oldDMwLT;
vector<float>   *muT_tau_byTightIsolationMVA3oldDMwoLT;
vector<float>   *muT_tau_byVLooseCombinedIsolationDeltaBetaCorr;
vector<float>   *muT_tau_byVLooseIsolationMVA3newDMwLT;
vector<float>   *muT_tau_byVLooseIsolationMVA3newDMwoLT;
vector<float>   *muT_tau_byVLooseIsolationMVA3oldDMwLT;
vector<float>   *muT_tau_byVLooseIsolationMVA3oldDMwoLT;
vector<float>   *muT_tau_byVTightIsolationMVA3newDMwLT;
vector<float>   *muT_tau_byVTightIsolationMVA3newDMwoLT;
vector<float>   *muT_tau_byVTightIsolationMVA3oldDMwLT;
vector<float>   *muT_tau_byVTightIsolationMVA3oldDMwoLT;
vector<float>   *muT_tau_byVVTightIsolationMVA3newDMwLT;
vector<float>   *muT_tau_byVVTightIsolationMVA3newDMwoLT;
vector<float>   *muT_tau_byVVTightIsolationMVA3oldDMwLT;
vector<float>   *muT_tau_byVVTightIsolationMVA3oldDMwoLT;
vector<float>   *muT_tau_chargedIsoPtSum;
vector<float>   *muT_tau_decayModeFinding;
vector<float>   *muT_tau_decayModeFindingNewDMs;
vector<float>   *muT_tau_decayModeFindingOldDMs;
vector<float>   *muT_tau_neutralIsoPtSum;
vector<float>   *muT_tau_puCorrPtSum;
vector<bool>    *muT_tau_has_HltMatchEle20;
vector<bool>    *muT_tau_has_HltMatchEle22;
vector<bool>    *muT_tau_has_HltMatchEle27;
vector<bool>    *muT_tau_has_HltMatchMu17;
vector<bool>    *muT_tau_has_HltMatchMu18;
vector<bool>    *muT_tau_has_HltMatchMu24;
vector<double>  *muT_puWeight;
vector<double>  *muT_puWeightM1;
vector<double>  *muT_puWeightP1;
vector<float>   *muT_NumPileupInt;
vector<float>   *muT_NumTruePileUpInt;
vector<float>   *muT_NumPileupIntM1;
vector<float>   *muT_NumTruePileUpIntM1;
vector<float>   *muT_NumPileupIntP1;
vector<float>   *muT_NumTruePileUpIntP1;
vector<double>  *muT_EffDataISOMU17andISOMU18;
vector<double>  *muT_EffMcISOMU17andISOMU18;
vector<double>  *muT_HadronicTauDataTrigEffAntiMuMed;
vector<double>  *muT_HadronicTauMcTrigEffAntiMuMed;
vector<double>  *muT_muonDataIDweight;
vector<double>  *muT_muonMcIDweight;
vector<double>  *muT_muonDataISOLweight;
vector<double>  *muT_muonMcISOLweight;
vector<double>  *muT_EffDataHighPtTauTrigger;
vector<double>  *muT_EffMcHighPtTauTrigger;
vector<double>  *muT_TauFakeCorrection;
vector<double>  *muT_DecayModeCorrectionFactor;
vector<double>  *muT_nominalHIGLUXHQTmhmax;
vector<double>  *muT_upHIGLUXHQTmhmax;
vector<double>  *muT_downHIGLUXHQTmhmax;
vector<double>  *muT_nominalPOWHEGmhmod;
vector<double>  *muT_upPOWHEGmhmod;
vector<double>  *muT_downPOWHEGmhmod;
vector<double>  *muT_upPOWHEGscale;
vector<double>  *muT_downPOWHEGscale;
vector<double>  *muT_etaDepQCDShapeTemplateCorrection;
vector<double>  *muT_inclusiveQCDShapeTemplateCorrection;
vector<double>  *muT_TTbarPtWeight;
vector<double>  *muT_TauSpinnerWT;
vector<double>  *muT_TauSpinnerWTFlip;
vector<double>  *muT_TauSpinnerWThminus;
vector<double>  *muT_TauSpinnerWThplus;
vector<int>     *muT_hepNUP;
vector<double>  *muT_weightHEPNUP_DYJets;
vector<double>  *muT_weightHEPNUP_WJets;
vector<bool>    *muT_passesSecondLeptonVeto;
vector<bool>    *muT_passesThirdLeptonVeto;
vector <double> * eT_embedWeight;
vector <double> * muT_embedWeight;

// List of accessors

UInt_t          run_;
UInt_t          luminosityBlock_;
UInt_t          event_;
Bool_t          isRealData_;
Int_t           bunchCrossing_;
Int_t           orbitNumber_;
string          NAMEVAR_;
string          SampleName_;
string          PhysicsProcess_;
Bool_t          isNonTopEmbeddedSample_;
Bool_t          isTopEmbeddedSample_;
Double_t        MASS_;
Double_t        crossSection_;
Double_t        branchingFraction_;
Int_t           numberEvents_;
vector<double>  eT_p4_x_;
vector<double>  eT_p4_y_;
vector<double>  eT_p4_z_;
vector<double>  eT_p4_t_;
vector<double>  eT_corrected_p4_x_;
vector<double>  eT_corrected_p4_y_;
vector<double>  eT_corrected_p4_z_;
vector<double>  eT_corrected_p4_t_;
vector<int>     eT_electronIndex_;
vector<int>     eT_tauIndex_;
vector<double>  eT_scalarSumPt_;
vector<double>  eT_DR_;
vector<int>     eT_sumCharge_;
vector<double>  eT_correctedSVFitMass_;
vector<double>  eT_rawSVFitMass_;
vector<double>  eT_TransverseMass_;
vector<double>  eT_rawTransverseMass_;
vector<double>  eT_mvaMETraw_;
vector<double>  eT_mvaMET_;
vector<double>  eT_mvaMETphiRaw_;
vector<double>  eT_mvaMETphi_;
vector<int>     eT_MAX_;
vector<bool>    eT_isGoodTriggerPair_;
vector<int>     eT_njets_;
vector<int>     eT_nbjets_;
vector<int>     eT_nbjetsLOOSE_;
vector<int>     eT_nbjetsLOOSEUP_;
vector<int>     eT_nbjetsLOOSEDOWN_;
vector<int>     eT_njetsUP_;
vector<int>     eT_nbjetsUP_;
vector<int>     eT_njetsDOWN_;
vector<int>     eT_nbjetsDOWN_;
vector<double>  eT_jet1P4_x_;
vector<double>  eT_jet1P4_y_;
vector<double>  eT_jet1P4_z_;
vector<double>  eT_jet1P4_t_;
vector<double>  eT_jet1RawP4_x_;
vector<double>  eT_jet1RawP4_y_;
vector<double>  eT_jet1RawP4_z_;
vector<double>  eT_jet1RawP4_t_;
vector<double>  eT_jet1IDMVA_;
vector<double>  eT_jet1BTAGMVA_;
vector<double>  eT_jet2P4_x_;
vector<double>  eT_jet2P4_y_;
vector<double>  eT_jet2P4_z_;
vector<double>  eT_jet2P4_t_;
vector<double>  eT_jet2RawP4_x_;
vector<double>  eT_jet2RawP4_y_;
vector<double>  eT_jet2RawP4_z_;
vector<double>  eT_jet2RawP4_t_;
vector<double>  eT_jet2IDMVA_;
vector<double>  eT_jet2BTAGMVA_;
vector<double>  eT_cov00_;
vector<double>  eT_cov01_;
vector<double>  eT_cov10_;
vector<double>  eT_cov11_;
vector<bool>    eT_passesTriLeptonVeto_;
vector<bool>    eT_passNonTopEmbeddedTriggerAndMass50_;
vector<bool>    eT_passSignalGeneratorMass70to130Cut_;
vector<double>  eT_genBosonP4_x_;
vector<double>  eT_genBosonP4_y_;
vector<double>  eT_genBosonP4_z_;
vector<double>  eT_genBosonP4_t_;
vector<double>  eT_genTOPp4_x_;
vector<double>  eT_genTOPp4_y_;
vector<double>  eT_genTOPp4_z_;
vector<double>  eT_genTOPp4_t_;
vector<double>  eT_genTOPBARp4_x_;
vector<double>  eT_genTOPBARp4_y_;
vector<double>  eT_genTOPBARp4_z_;
vector<double>  eT_genTOPBARp4_t_;
vector<int>     eT_numberOfGoodVertices_;
vector<int>     eT_PVndof_;
vector<double>  eT_PVz_;
vector<double>  eT_PVpositionRho_;
vector<double>  eT_PVp4_x_;
vector<double>  eT_PVp4_y_;
vector<double>  eT_PVp4_z_;
vector<double>  eT_PVp4_t_;
vector<bool>    eT_isDecayZtauTau_;
vector<bool>    eT_isDecayZeE_;
vector<bool>    eT_isDecayZmuMu_;
vector<bool>    eT_isRecoLep_matchedTo_GenTauFromZ_;
vector<bool>    eT_isRecoTau_matchedTo_GenTauFromZ_;
vector<bool>    eT_isRecoLep_matchedTo_GenElecFromZ_;
vector<bool>    eT_isRecoTau_matchedTo_GenElecFromZ_;
vector<bool>    eT_isRecoLep_matchedTo_GenMuonFromZ_;
vector<bool>    eT_isRecoTau_matchedTo_GenMuonFromZ_;
vector<bool>    eT_isRecoLep_matchedTo_GenElecFromTau_;
vector<bool>    eT_isRecoTau_matchedTo_GenElecFromTau_;
vector<bool>    eT_isRecoLep_matchedTo_GenMuonFromTau_;
vector<bool>    eT_isRecoTau_matchedTo_GenMuonFromTau_;
vector<bool>    eT_passEmbeddedTrigger_;
vector<double>  eT_ele_p4_x_;
vector<double>  eT_ele_p4_y_;
vector<double>  eT_ele_p4_z_;
vector<double>  eT_ele_p4_t_;
vector<double>  eT_ele_genP4_x_;
vector<double>  eT_ele_genP4_y_;
vector<double>  eT_ele_genP4_z_;
vector<double>  eT_ele_genP4_t_;
vector<double>  eT_ele_pfP4_x_;
vector<double>  eT_ele_pfP4_y_;
vector<double>  eT_ele_pfP4_z_;
vector<double>  eT_ele_pfP4_t_;
vector<int>     eT_ele_charge_;
vector<int>     eT_ele_PFpdgId_;
vector<int>     eT_ele_GENpdgId_;
vector<int>     eT_ele_numberOfMissingInnerHits_;
vector<bool>    eT_ele_passConversionVeto_;
vector<double>  eT_ele_dz_;
vector<double>  eT_ele_dB_;
vector<double>  eT_ele_dxy_;
vector<double>  eT_ele_SuperClusterEta_;
vector<double>  eT_ele_mvaTrigV0_;
vector<double>  eT_ele_mvaTrigNoIPV0_;
vector<double>  eT_ele_mvaNonTrigV0_;
vector<bool>    eT_ele_pass_tight_mvaNonTrigV0_;
vector<bool>    eT_ele_passFullId_;
vector<double>  eT_ele_chargedHadronIso_;
vector<double>  eT_ele_photonIso_;
vector<double>  eT_ele_neutralHadronIso_;
vector<double>  eT_ele_puChargedHadronIso_;
vector<double>  eT_ele_relativeIso_;
vector<bool>    eT_ele_isEB_;
vector<bool>    eT_ele_isEE_;
vector<bool>    eT_ele_isEBEEGap_;
vector<bool>    eT_ele_isEBEtaGap_;
vector<bool>    eT_ele_isEBPhiGap_;
vector<bool>    eT_ele_isEEDeeGap_;
vector<bool>    eT_ele_isEERingGap_;
vector<double>  eT_ele_sigmaEtaEta_;
vector<double>  eT_ele_sigmaIetaIeta_;
vector<double>  eT_ele_sigmaIphiIphi_;
vector<bool>    eT_ele_has_HltMatchEle20_;
vector<bool>    eT_ele_has_HltMatchEle22_;
vector<bool>    eT_ele_has_HltMatchEle27_;
vector<bool>    eT_ele_isTriLeptonVetoCandidate_;
vector<double>  eT_ele_deltaPhiSuperClusterTrackAtVtx_;
vector<double>  eT_ele_deltaEtaSuperClusterTrackAtVtx_;
vector<double>  eT_ele_hadronicOverEm_;
vector<double>  eT_tau_pfJetRefP4_x_;
vector<double>  eT_tau_pfJetRefP4_y_;
vector<double>  eT_tau_pfJetRefP4_z_;
vector<double>  eT_tau_pfJetRefP4_t_;
vector<double>  eT_tau_p4_x_;
vector<double>  eT_tau_p4_y_;
vector<double>  eT_tau_p4_z_;
vector<double>  eT_tau_p4_t_;
vector<double>  eT_tau_genP4_x_;
vector<double>  eT_tau_genP4_y_;
vector<double>  eT_tau_genP4_z_;
vector<double>  eT_tau_genP4_t_;
vector<double>  eT_tau_genJet_x_;
vector<double>  eT_tau_genJet_y_;
vector<double>  eT_tau_genJet_z_;
vector<double>  eT_tau_genJet_t_;
vector<double>  eT_tau_corrected_p4_x_;
vector<double>  eT_tau_corrected_p4_y_;
vector<double>  eT_tau_corrected_p4_z_;
vector<double>  eT_tau_corrected_p4_t_;
vector<int>     eT_tau_pdgId_;
vector<int>     eT_tau_pdgIdGEN_;
vector<int>     eT_tau_charge_;
vector<int>     eT_tau_decayMode_;
vector<bool>    eT_tau_passFullId_muTau_;
vector<bool>    eT_tau_passFullId_eTau_;
vector<int>     eT_tau_numStrips_;
vector<int>     eT_tau_numHadrons_;
vector<float>   eT_tau_againstElectronDeadECAL_;
vector<float>   eT_tau_againstElectronLoose_;
vector<float>   eT_tau_againstElectronLooseMVA5_;
vector<float>   eT_tau_againstElectronMVA5category_;
vector<float>   eT_tau_againstElectronMVA5raw_;
vector<float>   eT_tau_againstElectronMedium_;
vector<float>   eT_tau_againstElectronMediumMVA5_;
vector<float>   eT_tau_againstElectronTight_;
vector<float>   eT_tau_againstElectronTightMVA5_;
vector<float>   eT_tau_againstElectronVLooseMVA5_;
vector<float>   eT_tau_againstElectronVTightMVA5_;
vector<float>   eT_tau_againstMuonLoose_;
vector<float>   eT_tau_againstMuonLoose2_;
vector<float>   eT_tau_againstMuonLoose3_;
vector<float>   eT_tau_againstMuonLooseMVA_;
vector<float>   eT_tau_againstMuonMVAraw_;
vector<float>   eT_tau_againstMuonMedium_;
vector<float>   eT_tau_againstMuonMedium2_;
vector<float>   eT_tau_againstMuonMediumMVA_;
vector<float>   eT_tau_againstMuonTight_;
vector<float>   eT_tau_againstMuonTight2_;
vector<float>   eT_tau_againstMuonTight3_;
vector<float>   eT_tau_againstMuonTightMVA_;
vector<float>   eT_tau_byCombinedIsolationDeltaBetaCorrRaw_;
vector<float>   eT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits_;
vector<float>   eT_tau_byIsolationMVA3newDMwLTraw_;
vector<float>   eT_tau_byIsolationMVA3newDMwoLTraw_;
vector<float>   eT_tau_byIsolationMVA3oldDMwLTraw_;
vector<float>   eT_tau_byIsolationMVA3oldDMwoLTraw_;
vector<float>   eT_tau_byLooseCombinedIsolationDeltaBetaCorr_;
vector<float>   eT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits_;
vector<float>   eT_tau_byLooseIsolation_;
vector<float>   eT_tau_byLooseIsolationMVA3newDMwLT_;
vector<float>   eT_tau_byLooseIsolationMVA3newDMwoLT_;
vector<float>   eT_tau_byLooseIsolationMVA3oldDMwLT_;
vector<float>   eT_tau_byLooseIsolationMVA3oldDMwoLT_;
vector<float>   eT_tau_byMediumCombinedIsolationDeltaBetaCorr_;
vector<float>   eT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits_;
vector<float>   eT_tau_byMediumIsolationMVA3newDMwLT_;
vector<float>   eT_tau_byMediumIsolationMVA3newDMwoLT_;
vector<float>   eT_tau_byMediumIsolationMVA3oldDMwLT_;
vector<float>   eT_tau_byMediumIsolationMVA3oldDMwoLT_;
vector<float>   eT_tau_byTightCombinedIsolationDeltaBetaCorr_;
vector<float>   eT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits_;
vector<float>   eT_tau_byTightIsolationMVA3newDMwLT_;
vector<float>   eT_tau_byTightIsolationMVA3newDMwoLT_;
vector<float>   eT_tau_byTightIsolationMVA3oldDMwLT_;
vector<float>   eT_tau_byTightIsolationMVA3oldDMwoLT_;
vector<float>   eT_tau_byVLooseCombinedIsolationDeltaBetaCorr_;
vector<float>   eT_tau_byVLooseIsolationMVA3newDMwLT_;
vector<float>   eT_tau_byVLooseIsolationMVA3newDMwoLT_;
vector<float>   eT_tau_byVLooseIsolationMVA3oldDMwLT_;
vector<float>   eT_tau_byVLooseIsolationMVA3oldDMwoLT_;
vector<float>   eT_tau_byVTightIsolationMVA3newDMwLT_;
vector<float>   eT_tau_byVTightIsolationMVA3newDMwoLT_;
vector<float>   eT_tau_byVTightIsolationMVA3oldDMwLT_;
vector<float>   eT_tau_byVTightIsolationMVA3oldDMwoLT_;
vector<float>   eT_tau_byVVTightIsolationMVA3newDMwLT_;
vector<float>   eT_tau_byVVTightIsolationMVA3newDMwoLT_;
vector<float>   eT_tau_byVVTightIsolationMVA3oldDMwLT_;
vector<float>   eT_tau_byVVTightIsolationMVA3oldDMwoLT_;
vector<float>   eT_tau_chargedIsoPtSum_;
vector<float>   eT_tau_decayModeFinding_;
vector<float>   eT_tau_decayModeFindingNewDMs_;
vector<float>   eT_tau_decayModeFindingOldDMs_;
vector<float>   eT_tau_neutralIsoPtSum_;
vector<float>   eT_tau_puCorrPtSum_;
vector<bool>    eT_tau_has_HltMatchEle20_;
vector<bool>    eT_tau_has_HltMatchEle22_;
vector<bool>    eT_tau_has_HltMatchEle27_;
vector<bool>    eT_tau_has_HltMatchMu17_;
vector<bool>    eT_tau_has_HltMatchMu18_;
vector<bool>    eT_tau_has_HltMatchMu24_;
vector<double>  eT_puWeight_;
vector<double>  eT_puWeightM1_;
vector<double>  eT_puWeightP1_;
vector<float>   eT_NumPileupInt_;
vector<float>   eT_NumTruePileUpInt_;
vector<float>   eT_NumPileupIntM1_;
vector<float>   eT_NumTruePileUpIntM1_;
vector<float>   eT_NumPileupIntP1_;
vector<float>   eT_NumTruePileUpIntP1_;
vector<double>  eT_EffDataELE20andELE22_;
vector<double>  eT_EffMcELE20andELE22_;
vector<double>  eT_HadronicTauDataTrigEffAntiEMed_;
vector<double>  eT_HadronicTauMcTrigEffAntiEMed_;
vector<double>  eT_HadronicTauDataTrigEffAntiETight_;
vector<double>  eT_HadronicTauMcTrigEffAntiETight_;
vector<double>  eT_electronDataIDweight_;
vector<double>  eT_electronMcIDweight_;
vector<double>  eT_electronDataISOLweight_;
vector<double>  eT_electronMcISOLweight_;
vector<double>  eT_EffDataHighPtTauTrigger_;
vector<double>  eT_EffMcHighPtTauTrigger_;
vector<double>  eT_TauFakeCorrection_;
vector<double>  eT_DecayModeCorrectionFactor_;
vector<double>  eT_ZeeScaleFactor_;
vector<double>  eT_nominalHIGLUXHQTmhmax_;
vector<double>  eT_upHIGLUXHQTmhmax_;
vector<double>  eT_downHIGLUXHQTmhmax_;
vector<double>  eT_nominalPOWHEGmhmod_;
vector<double>  eT_upPOWHEGmhmod_;
vector<double>  eT_downPOWHEGmhmod_;
vector<double>  eT_upPOWHEGscale_;
vector<double>  eT_downPOWHEGscale_;
vector<double>  eT_etaDepQCDShapeTemplateCorrection_;
vector<double>  eT_inclusiveQCDShapeTemplateCorrection_;
vector<double>  eT_TTbarPtWeight_;
vector<double>  eT_TauSpinnerWT_;
vector<double>  eT_TauSpinnerWTFlip_;
vector<double>  eT_TauSpinnerWThminus_;
vector<double>  eT_TauSpinnerWThplus_;
vector<int>     eT_hepNUP_;
vector<double>  eT_weightHEPNUP_DYJets_;
vector<double>  eT_weightHEPNUP_WJets_;
vector<bool>    eT_passesSecondLeptonVeto_;
vector<bool>    eT_passesThirdLeptonVeto_;
vector<double>  muT_p4_x_;
vector<double>  muT_p4_y_;
vector<double>  muT_p4_z_;
vector<double>  muT_p4_t_;
vector<double>  muT_corrected_p4_x_;
vector<double>  muT_corrected_p4_y_;
vector<double>  muT_corrected_p4_z_;
vector<double>  muT_corrected_p4_t_;
vector<int>     muT_muonIndex_;
vector<int>     muT_tauIndex_;
vector<double>  muT_scalarSumPt_;
vector<double>  muT_DR_;
vector<int>     muT_sumCharge_;
vector<double>  muT_correctedSVFitMass_;
vector<double>  muT_rawSVFitMass_;
vector<double>  muT_TransverseMass_;
vector<double>  muT_rawTransverseMass_;
vector<double>  muT_mvaMETraw_;
vector<double>  muT_mvaMET_;
vector<double>  muT_mvaMETphiRaw_;
vector<double>  muT_mvaMETphi_;
vector<int>     muT_MAX_;
vector<bool>    muT_isGoodTriggerPair_;
vector<int>     muT_njets_;
vector<int>     muT_nbjets_;
vector<int>     muT_nbjetsLOOSE_;
vector<int>     muT_nbjetsLOOSEUP_;
vector<int>     muT_nbjetsLOOSEDOWN_;
vector<int>     muT_njetsUP_;
vector<int>     muT_nbjetsUP_;
vector<int>     muT_njetsDOWN_;
vector<int>     muT_nbjetsDOWN_;
vector<double>  muT_jet1P4_x_;
vector<double>  muT_jet1P4_y_;
vector<double>  muT_jet1P4_z_;
vector<double>  muT_jet1P4_t_;
vector<double>  muT_jet1RawP4_x_;
vector<double>  muT_jet1RawP4_y_;
vector<double>  muT_jet1RawP4_z_;
vector<double>  muT_jet1RawP4_t_;
vector<double>  muT_jet1IDMVA_;
vector<double>  muT_jet1BTAGMVA_;
vector<double>  muT_jet2P4_x_;
vector<double>  muT_jet2P4_y_;
vector<double>  muT_jet2P4_z_;
vector<double>  muT_jet2P4_t_;
vector<double>  muT_jet2RawP4_x_;
vector<double>  muT_jet2RawP4_y_;
vector<double>  muT_jet2RawP4_z_;
vector<double>  muT_jet2RawP4_t_;
vector<double>  muT_jet2IDMVA_;
vector<double>  muT_jet2BTAGMVA_;
vector<double>  muT_cov00_;
vector<double>  muT_cov01_;
vector<double>  muT_cov10_;
vector<double>  muT_cov11_;
vector<bool>    muT_passesTriLeptonVeto_;
vector<bool>    muT_passNonTopEmbeddedTriggerAndMass50_;
vector<bool>    muT_passSignalGeneratorMass70to130Cut_;
vector<double>  muT_genBosonP4_x_;
vector<double>  muT_genBosonP4_y_;
vector<double>  muT_genBosonP4_z_;
vector<double>  muT_genBosonP4_t_;
vector<double>  muT_genTOPp4_x_;
vector<double>  muT_genTOPp4_y_;
vector<double>  muT_genTOPp4_z_;
vector<double>  muT_genTOPp4_t_;
vector<double>  muT_genTOPBARp4_x_;
vector<double>  muT_genTOPBARp4_y_;
vector<double>  muT_genTOPBARp4_z_;
vector<double>  muT_genTOPBARp4_t_;
vector<int>     muT_numberOfGoodVertices_;
vector<int>     muT_PVndof_;
vector<double>  muT_PVz_;
vector<double>  muT_PVpositionRho_;
vector<double>  muT_PVp4_x_;
vector<double>  muT_PVp4_y_;
vector<double>  muT_PVp4_z_;
vector<double>  muT_PVp4_t_;
vector<bool>    muT_isDecayZtauTau_;
vector<bool>    muT_isDecayZeE_;
vector<bool>    muT_isDecayZmuMu_;
vector<bool>    muT_isRecoLep_matchedTo_GenTauFromZ_;
vector<bool>    muT_isRecoTau_matchedTo_GenTauFromZ_;
vector<bool>    muT_isRecoLep_matchedTo_GenElecFromZ_;
vector<bool>    muT_isRecoTau_matchedTo_GenElecFromZ_;
vector<bool>    muT_isRecoLep_matchedTo_GenMuonFromZ_;
vector<bool>    muT_isRecoTau_matchedTo_GenMuonFromZ_;
vector<bool>    muT_isRecoLep_matchedTo_GenElecFromTau_;
vector<bool>    muT_isRecoTau_matchedTo_GenElecFromTau_;
vector<bool>    muT_isRecoLep_matchedTo_GenMuonFromTau_;
vector<bool>    muT_isRecoTau_matchedTo_GenMuonFromTau_;
vector<bool>    muT_passEmbeddedTrigger_;
vector<double>  muT_muon_p4_x_;
vector<double>  muT_muon_p4_y_;
vector<double>  muT_muon_p4_z_;
vector<double>  muT_muon_p4_t_;
vector<double>  muT_muon_pfP4_x_;
vector<double>  muT_muon_pfP4_y_;
vector<double>  muT_muon_pfP4_z_;
vector<double>  muT_muon_pfP4_t_;
vector<double>  muT_muon_genP4_x_;
vector<double>  muT_muon_genP4_y_;
vector<double>  muT_muon_genP4_z_;
vector<double>  muT_muon_genP4_t_;
vector<bool>    muT_muon_isGlobalMuon_;
vector<bool>    muT_muon_isTightMuon_;
vector<bool>    muT_muon_isPFMuon_;
vector<bool>    muT_muon_isLooseMuon_;
vector<double>  muT_muon_sumChargedParticlePt_DR4_;
vector<double>  muT_muon_sumPhotonEt_DR4_;
vector<double>  muT_muon_sumNeutralHadronEt_DR4_;
vector<double>  muT_muon_sumPUPt_DR4_;
vector<double>  muT_muon_relativeIso_DR4_;
vector<double>  muT_muon_sumChargedParticlePt_DR3_;
vector<double>  muT_muon_sumPhotonEt_DR3_;
vector<double>  muT_muon_sumNeutralHadronEt_DR3_;
vector<double>  muT_muon_sumPUPt_DR3_;
vector<double>  muT_muon_relativeIso_DR3_;
vector<bool>    muT_muon_isPFIsolationValid_;
vector<int>     muT_muon_charge_;
vector<int>     muT_muon_PFpdgId_;
vector<int>     muT_muon_GENpdgId_;
vector<double>  muT_muon_normalizedChi2_;
vector<int>     muT_muon_numberOfValidMuonHits_;
vector<int>     muT_muon_numberOfMatchedStations_;
vector<int>     muT_muon_numberOfValidPixelHits_;
vector<int>     muT_muon_trackerLayersWithMeasurement_;
vector<double>  muT_muon_dB_;
vector<double>  muT_muon_dz_;
vector<double>  muT_muon_dxy_;
vector<bool>    muT_muon_passFullId_;
vector<bool>    muT_muon_has_HltMatchMu17_;
vector<bool>    muT_muon_has_HltMatchMu18_;
vector<bool>    muT_muon_has_HltMatchMu24_;
vector<bool>    muT_muon_isTriLeptonVetoCandidate_;
vector<bool>    muT_muon_isTrackerMuon_;
vector<double>  muT_tau_pfJetRefP4_x_;
vector<double>  muT_tau_pfJetRefP4_y_;
vector<double>  muT_tau_pfJetRefP4_z_;
vector<double>  muT_tau_pfJetRefP4_t_;
vector<double>  muT_tau_p4_x_;
vector<double>  muT_tau_p4_y_;
vector<double>  muT_tau_p4_z_;
vector<double>  muT_tau_p4_t_;
vector<double>  muT_tau_genP4_x_;
vector<double>  muT_tau_genP4_y_;
vector<double>  muT_tau_genP4_z_;
vector<double>  muT_tau_genP4_t_;
vector<double>  muT_tau_genJet_x_;
vector<double>  muT_tau_genJet_y_;
vector<double>  muT_tau_genJet_z_;
vector<double>  muT_tau_genJet_t_;
vector<double>  muT_tau_corrected_p4_x_;
vector<double>  muT_tau_corrected_p4_y_;
vector<double>  muT_tau_corrected_p4_z_;
vector<double>  muT_tau_corrected_p4_t_;
vector<int>     muT_tau_pdgId_;
vector<int>     muT_tau_pdgIdGEN_;
vector<int>     muT_tau_charge_;
vector<int>     muT_tau_decayMode_;
vector<bool>    muT_tau_passFullId_muTau_;
vector<bool>    muT_tau_passFullId_eTau_;
vector<int>     muT_tau_numStrips_;
vector<int>     muT_tau_numHadrons_;
vector<float>   muT_tau_againstElectronDeadECAL_;
vector<float>   muT_tau_againstElectronLoose_;
vector<float>   muT_tau_againstElectronLooseMVA5_;
vector<float>   muT_tau_againstElectronMVA5category_;
vector<float>   muT_tau_againstElectronMVA5raw_;
vector<float>   muT_tau_againstElectronMedium_;
vector<float>   muT_tau_againstElectronMediumMVA5_;
vector<float>   muT_tau_againstElectronTight_;
vector<float>   muT_tau_againstElectronTightMVA5_;
vector<float>   muT_tau_againstElectronVLooseMVA5_;
vector<float>   muT_tau_againstElectronVTightMVA5_;
vector<float>   muT_tau_againstMuonLoose_;
vector<float>   muT_tau_againstMuonLoose2_;
vector<float>   muT_tau_againstMuonLoose3_;
vector<float>   muT_tau_againstMuonLooseMVA_;
vector<float>   muT_tau_againstMuonMVAraw_;
vector<float>   muT_tau_againstMuonMedium_;
vector<float>   muT_tau_againstMuonMedium2_;
vector<float>   muT_tau_againstMuonMediumMVA_;
vector<float>   muT_tau_againstMuonTight_;
vector<float>   muT_tau_againstMuonTight2_;
vector<float>   muT_tau_againstMuonTight3_;
vector<float>   muT_tau_againstMuonTightMVA_;
vector<float>   muT_tau_byCombinedIsolationDeltaBetaCorrRaw_;
vector<float>   muT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits_;
vector<float>   muT_tau_byIsolationMVA3newDMwLTraw_;
vector<float>   muT_tau_byIsolationMVA3newDMwoLTraw_;
vector<float>   muT_tau_byIsolationMVA3oldDMwLTraw_;
vector<float>   muT_tau_byIsolationMVA3oldDMwoLTraw_;
vector<float>   muT_tau_byLooseCombinedIsolationDeltaBetaCorr_;
vector<float>   muT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits_;
vector<float>   muT_tau_byLooseIsolation_;
vector<float>   muT_tau_byLooseIsolationMVA3newDMwLT_;
vector<float>   muT_tau_byLooseIsolationMVA3newDMwoLT_;
vector<float>   muT_tau_byLooseIsolationMVA3oldDMwLT_;
vector<float>   muT_tau_byLooseIsolationMVA3oldDMwoLT_;
vector<float>   muT_tau_byMediumCombinedIsolationDeltaBetaCorr_;
vector<float>   muT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits_;
vector<float>   muT_tau_byMediumIsolationMVA3newDMwLT_;
vector<float>   muT_tau_byMediumIsolationMVA3newDMwoLT_;
vector<float>   muT_tau_byMediumIsolationMVA3oldDMwLT_;
vector<float>   muT_tau_byMediumIsolationMVA3oldDMwoLT_;
vector<float>   muT_tau_byTightCombinedIsolationDeltaBetaCorr_;
vector<float>   muT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits_;
vector<float>   muT_tau_byTightIsolationMVA3newDMwLT_;
vector<float>   muT_tau_byTightIsolationMVA3newDMwoLT_;
vector<float>   muT_tau_byTightIsolationMVA3oldDMwLT_;
vector<float>   muT_tau_byTightIsolationMVA3oldDMwoLT_;
vector<float>   muT_tau_byVLooseCombinedIsolationDeltaBetaCorr_;
vector<float>   muT_tau_byVLooseIsolationMVA3newDMwLT_;
vector<float>   muT_tau_byVLooseIsolationMVA3newDMwoLT_;
vector<float>   muT_tau_byVLooseIsolationMVA3oldDMwLT_;
vector<float>   muT_tau_byVLooseIsolationMVA3oldDMwoLT_;
vector<float>   muT_tau_byVTightIsolationMVA3newDMwLT_;
vector<float>   muT_tau_byVTightIsolationMVA3newDMwoLT_;
vector<float>   muT_tau_byVTightIsolationMVA3oldDMwLT_;
vector<float>   muT_tau_byVTightIsolationMVA3oldDMwoLT_;
vector<float>   muT_tau_byVVTightIsolationMVA3newDMwLT_;
vector<float>   muT_tau_byVVTightIsolationMVA3newDMwoLT_;
vector<float>   muT_tau_byVVTightIsolationMVA3oldDMwLT_;
vector<float>   muT_tau_byVVTightIsolationMVA3oldDMwoLT_;
vector<float>   muT_tau_chargedIsoPtSum_;
vector<float>   muT_tau_decayModeFinding_;
vector<float>   muT_tau_decayModeFindingNewDMs_;
vector<float>   muT_tau_decayModeFindingOldDMs_;
vector<float>   muT_tau_neutralIsoPtSum_;
vector<float>   muT_tau_puCorrPtSum_;
vector<bool>    muT_tau_has_HltMatchEle20_;
vector<bool>    muT_tau_has_HltMatchEle22_;
vector<bool>    muT_tau_has_HltMatchEle27_;
vector<bool>    muT_tau_has_HltMatchMu17_;
vector<bool>    muT_tau_has_HltMatchMu18_;
vector<bool>    muT_tau_has_HltMatchMu24_;
vector<double>  muT_puWeight_;
vector<double>  muT_puWeightM1_;
vector<double>  muT_puWeightP1_;
vector<float>   muT_NumPileupInt_;
vector<float>   muT_NumTruePileUpInt_;
vector<float>   muT_NumPileupIntM1_;
vector<float>   muT_NumTruePileUpIntM1_;
vector<float>   muT_NumPileupIntP1_;
vector<float>   muT_NumTruePileUpIntP1_;
vector<double>  muT_EffDataISOMU17andISOMU18_;
vector<double>  muT_EffMcISOMU17andISOMU18_;
vector<double>  muT_HadronicTauDataTrigEffAntiMuMed_;
vector<double>  muT_HadronicTauMcTrigEffAntiMuMed_;
vector<double>  muT_muonDataIDweight_;
vector<double>  muT_muonMcIDweight_;
vector<double>  muT_muonDataISOLweight_;
vector<double>  muT_muonMcISOLweight_;
vector<double>  muT_EffDataHighPtTauTrigger_;
vector<double>  muT_EffMcHighPtTauTrigger_;
vector<double>  muT_TauFakeCorrection_;
vector<double>  muT_DecayModeCorrectionFactor_;
vector<double>  muT_nominalHIGLUXHQTmhmax_;
vector<double>  muT_upHIGLUXHQTmhmax_;
vector<double>  muT_downHIGLUXHQTmhmax_;
vector<double>  muT_nominalPOWHEGmhmod_;
vector<double>  muT_upPOWHEGmhmod_;
vector<double>  muT_downPOWHEGmhmod_;
vector<double>  muT_upPOWHEGscale_;
vector<double>  muT_downPOWHEGscale_;
vector<double>  muT_etaDepQCDShapeTemplateCorrection_;
vector<double>  muT_inclusiveQCDShapeTemplateCorrection_;
vector<double>  muT_TTbarPtWeight_;
vector<double>  muT_TauSpinnerWT_;
vector<double>  muT_TauSpinnerWTFlip_;
vector<double>  muT_TauSpinnerWThminus_;
vector<double>  muT_TauSpinnerWThplus_;
vector<int>     muT_hepNUP_;
vector<double>  muT_weightHEPNUP_DYJets_;
vector<double>  muT_weightHEPNUP_WJets_;
vector<bool>    muT_passesSecondLeptonVeto_;
vector<bool>    muT_passesThirdLeptonVeto_;
vector <double> eT_embedWeight_;
vector <double> muT_embedWeight_;

// List of branches
TBranch        *b_run;   //!
TBranch        *b_luminosityBlock;   //!
TBranch        *b_event;   //!
TBranch        *b_isRealData;   //!
TBranch        *b_bunchCrossing;   //!
TBranch        *b_orbitNumber;   //!
TBranch        *b_NAMEVAR;   //!
TBranch        *b_SampleName;   //!
TBranch        *b_PhysicsProcess;   //!
TBranch        *b_isNonTopEmbeddedSample;   //!
TBranch        *b_isTopEmbeddedSample;   //!
TBranch        *b_MASS;   //!
TBranch        *b_crossSection;   //!
TBranch        *b_branchingFraction;   //!
TBranch        *b_numberEvents;   //!
TBranch        *b_eT_p4_x;   //!
TBranch        *b_eT_p4_y;   //!
TBranch        *b_eT_p4_z;   //!
TBranch        *b_eT_p4_t;   //!
TBranch        *b_eT_corrected_p4_x;   //!
TBranch        *b_eT_corrected_p4_y;   //!
TBranch        *b_eT_corrected_p4_z;   //!
TBranch        *b_eT_corrected_p4_t;   //!
TBranch        *b_eT_electronIndex;   //!
TBranch        *b_eT_tauIndex;   //!
TBranch        *b_eT_scalarSumPt;   //!
TBranch        *b_eT_DR;   //!
TBranch        *b_eT_sumCharge;   //!
TBranch        *b_eT_correctedSVFitMass;   //!
TBranch        *b_eT_rawSVFitMass;   //!
TBranch        *b_eT_TransverseMass;   //!
TBranch        *b_eT_rawTransverseMass;   //!
TBranch        *b_eT_mvaMETraw;   //!
TBranch        *b_eT_mvaMET;   //!
TBranch        *b_eT_mvaMETphiRaw;   //!
TBranch        *b_eT_mvaMETphi;   //!
TBranch        *b_eT_MAX;   //!
TBranch        *b_eT_isGoodTriggerPair;   //!
TBranch        *b_eT_njets;   //!
TBranch        *b_eT_nbjets;   //!
TBranch        *b_eT_nbjetsLOOSE;   //!
TBranch        *b_eT_nbjetsLOOSEUP;   //!
TBranch        *b_eT_nbjetsLOOSEDOWN;   //!
TBranch        *b_eT_njetsUP;   //!
TBranch        *b_eT_nbjetsUP;   //!
TBranch        *b_eT_njetsDOWN;   //!
TBranch        *b_eT_nbjetsDOWN;   //!
TBranch        *b_eT_jet1P4_x;   //!
TBranch        *b_eT_jet1P4_y;   //!
TBranch        *b_eT_jet1P4_z;   //!
TBranch        *b_eT_jet1P4_t;   //!
TBranch        *b_eT_jet1RawP4_x;   //!
TBranch        *b_eT_jet1RawP4_y;   //!
TBranch        *b_eT_jet1RawP4_z;   //!
TBranch        *b_eT_jet1RawP4_t;   //!
TBranch        *b_eT_jet1IDMVA;   //!
TBranch        *b_eT_jet1BTAGMVA;   //!
TBranch        *b_eT_jet2P4_x;   //!
TBranch        *b_eT_jet2P4_y;   //!
TBranch        *b_eT_jet2P4_z;   //!
TBranch        *b_eT_jet2P4_t;   //!
TBranch        *b_eT_jet2RawP4_x;   //!
TBranch        *b_eT_jet2RawP4_y;   //!
TBranch        *b_eT_jet2RawP4_z;   //!
TBranch        *b_eT_jet2RawP4_t;   //!
TBranch        *b_eT_jet2IDMVA;   //!
TBranch        *b_eT_jet2BTAGMVA;   //!
TBranch        *b_eT_cov00;   //!
TBranch        *b_eT_cov01;   //!
TBranch        *b_eT_cov10;   //!
TBranch        *b_eT_cov11;   //!
TBranch        *b_eT_passesTriLeptonVeto;   //!
TBranch        *b_eT_passNonTopEmbeddedTriggerAndMass50;   //!
TBranch        *b_eT_passSignalGeneratorMass70to130Cut;   //!
TBranch        *b_eT_genBosonP4_x;   //!
TBranch        *b_eT_genBosonP4_y;   //!
TBranch        *b_eT_genBosonP4_z;   //!
TBranch        *b_eT_genBosonP4_t;   //!
TBranch        *b_eT_genTOPp4_x;   //!
TBranch        *b_eT_genTOPp4_y;   //!
TBranch        *b_eT_genTOPp4_z;   //!
TBranch        *b_eT_genTOPp4_t;   //!
TBranch        *b_eT_genTOPBARp4_x;   //!
TBranch        *b_eT_genTOPBARp4_y;   //!
TBranch        *b_eT_genTOPBARp4_z;   //!
TBranch        *b_eT_genTOPBARp4_t;   //!
TBranch        *b_eT_numberOfGoodVertices;   //!
TBranch        *b_eT_PVndof;   //!
TBranch        *b_eT_PVz;   //!
TBranch        *b_eT_PVpositionRho;   //!
TBranch        *b_eT_PVp4_x;   //!
TBranch        *b_eT_PVp4_y;   //!
TBranch        *b_eT_PVp4_z;   //!
TBranch        *b_eT_PVp4_t;   //!
TBranch        *b_eT_isDecayZtauTau;   //!
TBranch        *b_eT_isDecayZeE;   //!
TBranch        *b_eT_isDecayZmuMu;   //!
TBranch        *b_eT_isRecoLep_matchedTo_GenTauFromZ;   //!
TBranch        *b_eT_isRecoTau_matchedTo_GenTauFromZ;   //!
TBranch        *b_eT_isRecoLep_matchedTo_GenElecFromZ;   //!
TBranch        *b_eT_isRecoTau_matchedTo_GenElecFromZ;   //!
TBranch        *b_eT_isRecoLep_matchedTo_GenMuonFromZ;   //!
TBranch        *b_eT_isRecoTau_matchedTo_GenMuonFromZ;   //!
TBranch        *b_eT_isRecoLep_matchedTo_GenElecFromTau;   //!
TBranch        *b_eT_isRecoTau_matchedTo_GenElecFromTau;   //!
TBranch        *b_eT_isRecoLep_matchedTo_GenMuonFromTau;   //!
TBranch        *b_eT_isRecoTau_matchedTo_GenMuonFromTau;   //!
TBranch        *b_eT_passEmbeddedTrigger;   //!
TBranch        *b_eT_ele_p4_x;   //!
TBranch        *b_eT_ele_p4_y;   //!
TBranch        *b_eT_ele_p4_z;   //!
TBranch        *b_eT_ele_p4_t;   //!
TBranch        *b_eT_ele_genP4_x;   //!
TBranch        *b_eT_ele_genP4_y;   //!
TBranch        *b_eT_ele_genP4_z;   //!
TBranch        *b_eT_ele_genP4_t;   //!
TBranch        *b_eT_ele_pfP4_x;   //!
TBranch        *b_eT_ele_pfP4_y;   //!
TBranch        *b_eT_ele_pfP4_z;   //!
TBranch        *b_eT_ele_pfP4_t;   //!
TBranch        *b_eT_ele_charge;   //!
TBranch        *b_eT_ele_PFpdgId;   //!
TBranch        *b_eT_ele_GENpdgId;   //!
TBranch        *b_eT_ele_numberOfMissingInnerHits;   //!
TBranch        *b_eT_ele_passConversionVeto;   //!
TBranch        *b_eT_ele_dz;   //!
TBranch        *b_eT_ele_dB;   //!
TBranch        *b_eT_ele_dxy;   //!
TBranch        *b_eT_ele_SuperClusterEta;   //!
TBranch        *b_eT_ele_mvaTrigV0;   //!
TBranch        *b_eT_ele_mvaTrigNoIPV0;   //!
TBranch        *b_eT_ele_mvaNonTrigV0;   //!
TBranch        *b_eT_ele_pass_tight_mvaNonTrigV0;   //!
TBranch        *b_eT_ele_passFullId;   //!
TBranch        *b_eT_ele_chargedHadronIso;   //!
TBranch        *b_eT_ele_photonIso;   //!
TBranch        *b_eT_ele_neutralHadronIso;   //!
TBranch        *b_eT_ele_puChargedHadronIso;   //!
TBranch        *b_eT_ele_relativeIso;   //!
TBranch        *b_eT_ele_isEB;   //!
TBranch        *b_eT_ele_isEE;   //!
TBranch        *b_eT_ele_isEBEEGap;   //!
TBranch        *b_eT_ele_isEBEtaGap;   //!
TBranch        *b_eT_ele_isEBPhiGap;   //!
TBranch        *b_eT_ele_isEEDeeGap;   //!
TBranch        *b_eT_ele_isEERingGap;   //!
TBranch        *b_eT_ele_sigmaEtaEta;   //!
TBranch        *b_eT_ele_sigmaIetaIeta;   //!
TBranch        *b_eT_ele_sigmaIphiIphi;   //!
TBranch        *b_eT_ele_has_HltMatchEle20;   //!
TBranch        *b_eT_ele_has_HltMatchEle22;   //!
TBranch        *b_eT_ele_has_HltMatchEle27;   //!
TBranch        *b_eT_ele_isTriLeptonVetoCandidate;   //!
TBranch        *b_eT_ele_deltaPhiSuperClusterTrackAtVtx;   //!
TBranch        *b_eT_ele_deltaEtaSuperClusterTrackAtVtx;   //!
TBranch        *b_eT_ele_hadronicOverEm;   //!
TBranch        *b_eT_tau_pfJetRefP4_x;   //!
TBranch        *b_eT_tau_pfJetRefP4_y;   //!
TBranch        *b_eT_tau_pfJetRefP4_z;   //!
TBranch        *b_eT_tau_pfJetRefP4_t;   //!
TBranch        *b_eT_tau_p4_x;   //!
TBranch        *b_eT_tau_p4_y;   //!
TBranch        *b_eT_tau_p4_z;   //!
TBranch        *b_eT_tau_p4_t;   //!
TBranch        *b_eT_tau_genP4_x;   //!
TBranch        *b_eT_tau_genP4_y;   //!
TBranch        *b_eT_tau_genP4_z;   //!
TBranch        *b_eT_tau_genP4_t;   //!
TBranch        *b_eT_tau_genJet_x;   //!
TBranch        *b_eT_tau_genJet_y;   //!
TBranch        *b_eT_tau_genJet_z;   //!
TBranch        *b_eT_tau_genJet_t;   //!
TBranch        *b_eT_tau_corrected_p4_x;   //!
TBranch        *b_eT_tau_corrected_p4_y;   //!
TBranch        *b_eT_tau_corrected_p4_z;   //!
TBranch        *b_eT_tau_corrected_p4_t;   //!
TBranch        *b_eT_tau_pdgId;   //!
TBranch        *b_eT_tau_pdgIdGEN;   //!
TBranch        *b_eT_tau_charge;   //!
TBranch        *b_eT_tau_decayMode;   //!
TBranch        *b_eT_tau_passFullId_muTau;   //!
TBranch        *b_eT_tau_passFullId_eTau;   //!
TBranch        *b_eT_tau_numStrips;   //!
TBranch        *b_eT_tau_numHadrons;   //!
TBranch        *b_eT_tau_againstElectronDeadECAL;   //!
TBranch        *b_eT_tau_againstElectronLoose;   //!
TBranch        *b_eT_tau_againstElectronLooseMVA5;   //!
TBranch        *b_eT_tau_againstElectronMVA5category;   //!
TBranch        *b_eT_tau_againstElectronMVA5raw;   //!
TBranch        *b_eT_tau_againstElectronMedium;   //!
TBranch        *b_eT_tau_againstElectronMediumMVA5;   //!
TBranch        *b_eT_tau_againstElectronTight;   //!
TBranch        *b_eT_tau_againstElectronTightMVA5;   //!
TBranch        *b_eT_tau_againstElectronVLooseMVA5;   //!
TBranch        *b_eT_tau_againstElectronVTightMVA5;   //!
TBranch        *b_eT_tau_againstMuonLoose;   //!
TBranch        *b_eT_tau_againstMuonLoose2;   //!
TBranch        *b_eT_tau_againstMuonLoose3;   //!
TBranch        *b_eT_tau_againstMuonLooseMVA;   //!
TBranch        *b_eT_tau_againstMuonMVAraw;   //!
TBranch        *b_eT_tau_againstMuonMedium;   //!
TBranch        *b_eT_tau_againstMuonMedium2;   //!
TBranch        *b_eT_tau_againstMuonMediumMVA;   //!
TBranch        *b_eT_tau_againstMuonTight;   //!
TBranch        *b_eT_tau_againstMuonTight2;   //!
TBranch        *b_eT_tau_againstMuonTight3;   //!
TBranch        *b_eT_tau_againstMuonTightMVA;   //!
TBranch        *b_eT_tau_byCombinedIsolationDeltaBetaCorrRaw;   //!
TBranch        *b_eT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits;   //!
TBranch        *b_eT_tau_byIsolationMVA3newDMwLTraw;   //!
TBranch        *b_eT_tau_byIsolationMVA3newDMwoLTraw;   //!
TBranch        *b_eT_tau_byIsolationMVA3oldDMwLTraw;   //!
TBranch        *b_eT_tau_byIsolationMVA3oldDMwoLTraw;   //!
TBranch        *b_eT_tau_byLooseCombinedIsolationDeltaBetaCorr;   //!
TBranch        *b_eT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits;   //!
TBranch        *b_eT_tau_byLooseIsolation;   //!
TBranch        *b_eT_tau_byLooseIsolationMVA3newDMwLT;   //!
TBranch        *b_eT_tau_byLooseIsolationMVA3newDMwoLT;   //!
TBranch        *b_eT_tau_byLooseIsolationMVA3oldDMwLT;   //!
TBranch        *b_eT_tau_byLooseIsolationMVA3oldDMwoLT;   //!
TBranch        *b_eT_tau_byMediumCombinedIsolationDeltaBetaCorr;   //!
TBranch        *b_eT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits;   //!
TBranch        *b_eT_tau_byMediumIsolationMVA3newDMwLT;   //!
TBranch        *b_eT_tau_byMediumIsolationMVA3newDMwoLT;   //!
TBranch        *b_eT_tau_byMediumIsolationMVA3oldDMwLT;   //!
TBranch        *b_eT_tau_byMediumIsolationMVA3oldDMwoLT;   //!
TBranch        *b_eT_tau_byTightCombinedIsolationDeltaBetaCorr;   //!
TBranch        *b_eT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits;   //!
TBranch        *b_eT_tau_byTightIsolationMVA3newDMwLT;   //!
TBranch        *b_eT_tau_byTightIsolationMVA3newDMwoLT;   //!
TBranch        *b_eT_tau_byTightIsolationMVA3oldDMwLT;   //!
TBranch        *b_eT_tau_byTightIsolationMVA3oldDMwoLT;   //!
TBranch        *b_eT_tau_byVLooseCombinedIsolationDeltaBetaCorr;   //!
TBranch        *b_eT_tau_byVLooseIsolationMVA3newDMwLT;   //!
TBranch        *b_eT_tau_byVLooseIsolationMVA3newDMwoLT;   //!
TBranch        *b_eT_tau_byVLooseIsolationMVA3oldDMwLT;   //!
TBranch        *b_eT_tau_byVLooseIsolationMVA3oldDMwoLT;   //!
TBranch        *b_eT_tau_byVTightIsolationMVA3newDMwLT;   //!
TBranch        *b_eT_tau_byVTightIsolationMVA3newDMwoLT;   //!
TBranch        *b_eT_tau_byVTightIsolationMVA3oldDMwLT;   //!
TBranch        *b_eT_tau_byVTightIsolationMVA3oldDMwoLT;   //!
TBranch        *b_eT_tau_byVVTightIsolationMVA3newDMwLT;   //!
TBranch        *b_eT_tau_byVVTightIsolationMVA3newDMwoLT;   //!
TBranch        *b_eT_tau_byVVTightIsolationMVA3oldDMwLT;   //!
TBranch        *b_eT_tau_byVVTightIsolationMVA3oldDMwoLT;   //!
TBranch        *b_eT_tau_chargedIsoPtSum;   //!
TBranch        *b_eT_tau_decayModeFinding;   //!
TBranch        *b_eT_tau_decayModeFindingNewDMs;   //!
TBranch        *b_eT_tau_decayModeFindingOldDMs;   //!
TBranch        *b_eT_tau_neutralIsoPtSum;   //!
TBranch        *b_eT_tau_puCorrPtSum;   //!
TBranch        *b_eT_tau_has_HltMatchEle20;   //!
TBranch        *b_eT_tau_has_HltMatchEle22;   //!
TBranch        *b_eT_tau_has_HltMatchEle27;   //!
TBranch        *b_eT_tau_has_HltMatchMu17;   //!
TBranch        *b_eT_tau_has_HltMatchMu18;   //!
TBranch        *b_eT_tau_has_HltMatchMu24;   //!
TBranch        *b_eT_puWeight;   //!
TBranch        *b_eT_puWeightM1;   //!
TBranch        *b_eT_puWeightP1;   //!
TBranch        *b_eT_NumPileupInt;   //!
TBranch        *b_eT_NumTruePileUpInt;   //!
TBranch        *b_eT_NumPileupIntM1;   //!
TBranch        *b_eT_NumTruePileUpIntM1;   //!
TBranch        *b_eT_NumPileupIntP1;   //!
TBranch        *b_eT_NumTruePileUpIntP1;   //!
TBranch        *b_eT_EffDataELE20andELE22;   //!
TBranch        *b_eT_EffMcELE20andELE22;   //!
TBranch        *b_eT_HadronicTauDataTrigEffAntiEMed;   //!
TBranch        *b_eT_HadronicTauMcTrigEffAntiEMed;   //!
TBranch        *b_eT_HadronicTauDataTrigEffAntiETight;   //!
TBranch        *b_eT_HadronicTauMcTrigEffAntiETight;   //!
TBranch        *b_eT_electronDataIDweight;   //!
TBranch        *b_eT_electronMcIDweight;   //!
TBranch        *b_eT_electronDataISOLweight;   //!
TBranch        *b_eT_electronMcISOLweight;   //!
TBranch        *b_eT_EffDataHighPtTauTrigger;   //!
TBranch        *b_eT_EffMcHighPtTauTrigger;   //!
TBranch        *b_eT_TauFakeCorrection;   //!
TBranch        *b_eT_DecayModeCorrectionFactor;   //!
TBranch        *b_eT_ZeeScaleFactor;   //!
TBranch        *b_eT_nominalHIGLUXHQTmhmax;   //!
TBranch        *b_eT_upHIGLUXHQTmhmax;   //!
TBranch        *b_eT_downHIGLUXHQTmhmax;   //!
TBranch        *b_eT_nominalPOWHEGmhmod;   //!
TBranch        *b_eT_upPOWHEGmhmod;   //!
TBranch        *b_eT_downPOWHEGmhmod;   //!
TBranch        *b_eT_upPOWHEGscale;   //!
TBranch        *b_eT_downPOWHEGscale;   //!
TBranch        *b_eT_etaDepQCDShapeTemplateCorrection;   //!
TBranch        *b_eT_inclusiveQCDShapeTemplateCorrection;   //!
TBranch        *b_eT_TTbarPtWeight;   //!
TBranch        *b_eT_TauSpinnerWT;   //!
TBranch        *b_eT_TauSpinnerWTFlip;   //!
TBranch        *b_eT_TauSpinnerWThminus;   //!
TBranch        *b_eT_TauSpinnerWThplus;   //!
TBranch        *b_eT_hepNUP;   //!
TBranch        *b_eT_weightHEPNUP_DYJets;   //!
TBranch        *b_eT_weightHEPNUP_WJets;   //!
TBranch        *b_eT_passesSecondLeptonVeto;   //!
TBranch        *b_eT_passesThirdLeptonVeto;   //!
TBranch        *b_muT_p4_x;   //!
TBranch        *b_muT_p4_y;   //!
TBranch        *b_muT_p4_z;   //!
TBranch        *b_muT_p4_t;   //!
TBranch        *b_muT_corrected_p4_x;   //!
TBranch        *b_muT_corrected_p4_y;   //!
TBranch        *b_muT_corrected_p4_z;   //!
TBranch        *b_muT_corrected_p4_t;   //!
TBranch        *b_muT_muonIndex;   //!
TBranch        *b_muT_tauIndex;   //!
TBranch        *b_muT_scalarSumPt;   //!
TBranch        *b_muT_DR;   //!
TBranch        *b_muT_sumCharge;   //!
TBranch        *b_muT_correctedSVFitMass;   //!
TBranch        *b_muT_rawSVFitMass;   //!
TBranch        *b_muT_TransverseMass;   //!
TBranch        *b_muT_rawTransverseMass;   //!
TBranch        *b_muT_mvaMETraw;   //!
TBranch        *b_muT_mvaMET;   //!
TBranch        *b_muT_mvaMETphiRaw;   //!
TBranch        *b_muT_mvaMETphi;   //!
TBranch        *b_muT_MAX;   //!
TBranch        *b_muT_isGoodTriggerPair;   //!
TBranch        *b_muT_njets;   //!
TBranch        *b_muT_nbjets;   //!
TBranch        *b_muT_nbjetsLOOSE;   //!
TBranch        *b_muT_nbjetsLOOSEUP;   //!
TBranch        *b_muT_nbjetsLOOSEDOWN;   //!
TBranch        *b_muT_njetsUP;   //!
TBranch        *b_muT_nbjetsUP;   //!
TBranch        *b_muT_njetsDOWN;   //!
TBranch        *b_muT_nbjetsDOWN;   //!
TBranch        *b_muT_jet1P4_x;   //!
TBranch        *b_muT_jet1P4_y;   //!
TBranch        *b_muT_jet1P4_z;   //!
TBranch        *b_muT_jet1P4_t;   //!
TBranch        *b_muT_jet1RawP4_x;   //!
TBranch        *b_muT_jet1RawP4_y;   //!
TBranch        *b_muT_jet1RawP4_z;   //!
TBranch        *b_muT_jet1RawP4_t;   //!
TBranch        *b_muT_jet1IDMVA;   //!
TBranch        *b_muT_jet1BTAGMVA;   //!
TBranch        *b_muT_jet2P4_x;   //!
TBranch        *b_muT_jet2P4_y;   //!
TBranch        *b_muT_jet2P4_z;   //!
TBranch        *b_muT_jet2P4_t;   //!
TBranch        *b_muT_jet2RawP4_x;   //!
TBranch        *b_muT_jet2RawP4_y;   //!
TBranch        *b_muT_jet2RawP4_z;   //!
TBranch        *b_muT_jet2RawP4_t;   //!
TBranch        *b_muT_jet2IDMVA;   //!
TBranch        *b_muT_jet2BTAGMVA;   //!
TBranch        *b_muT_cov00;   //!
TBranch        *b_muT_cov01;   //!
TBranch        *b_muT_cov10;   //!
TBranch        *b_muT_cov11;   //!
TBranch        *b_muT_passesTriLeptonVeto;   //!
TBranch        *b_muT_passNonTopEmbeddedTriggerAndMass50;   //!
TBranch        *b_muT_passSignalGeneratorMass70to130Cut;   //!
TBranch        *b_muT_genBosonP4_x;   //!
TBranch        *b_muT_genBosonP4_y;   //!
TBranch        *b_muT_genBosonP4_z;   //!
TBranch        *b_muT_genBosonP4_t;   //!
TBranch        *b_muT_genTOPp4_x;   //!
TBranch        *b_muT_genTOPp4_y;   //!
TBranch        *b_muT_genTOPp4_z;   //!
TBranch        *b_muT_genTOPp4_t;   //!
TBranch        *b_muT_genTOPBARp4_x;   //!
TBranch        *b_muT_genTOPBARp4_y;   //!
TBranch        *b_muT_genTOPBARp4_z;   //!
TBranch        *b_muT_genTOPBARp4_t;   //!
TBranch        *b_muT_numberOfGoodVertices;   //!
TBranch        *b_muT_PVndof;   //!
TBranch        *b_muT_PVz;   //!
TBranch        *b_muT_PVpositionRho;   //!
TBranch        *b_muT_PVp4_x;   //!
TBranch        *b_muT_PVp4_y;   //!
TBranch        *b_muT_PVp4_z;   //!
TBranch        *b_muT_PVp4_t;   //!
TBranch        *b_muT_isDecayZtauTau;   //!
TBranch        *b_muT_isDecayZeE;   //!
TBranch        *b_muT_isDecayZmuMu;   //!
TBranch        *b_muT_isRecoLep_matchedTo_GenTauFromZ;   //!
TBranch        *b_muT_isRecoTau_matchedTo_GenTauFromZ;   //!
TBranch        *b_muT_isRecoLep_matchedTo_GenElecFromZ;   //!
TBranch        *b_muT_isRecoTau_matchedTo_GenElecFromZ;   //!
TBranch        *b_muT_isRecoLep_matchedTo_GenMuonFromZ;   //!
TBranch        *b_muT_isRecoTau_matchedTo_GenMuonFromZ;   //!
TBranch        *b_muT_isRecoLep_matchedTo_GenElecFromTau;   //!
TBranch        *b_muT_isRecoTau_matchedTo_GenElecFromTau;   //!
TBranch        *b_muT_isRecoLep_matchedTo_GenMuonFromTau;   //!
TBranch        *b_muT_isRecoTau_matchedTo_GenMuonFromTau;   //!
TBranch        *b_muT_passEmbeddedTrigger;   //!
TBranch        *b_muT_muon_p4_x;   //!
TBranch        *b_muT_muon_p4_y;   //!
TBranch        *b_muT_muon_p4_z;   //!
TBranch        *b_muT_muon_p4_t;   //!
TBranch        *b_muT_muon_pfP4_x;   //!
TBranch        *b_muT_muon_pfP4_y;   //!
TBranch        *b_muT_muon_pfP4_z;   //!
TBranch        *b_muT_muon_pfP4_t;   //!
TBranch        *b_muT_muon_genP4_x;   //!
TBranch        *b_muT_muon_genP4_y;   //!
TBranch        *b_muT_muon_genP4_z;   //!
TBranch        *b_muT_muon_genP4_t;   //!
TBranch        *b_muT_muon_isGlobalMuon;   //!
TBranch        *b_muT_muon_isTightMuon;   //!
TBranch        *b_muT_muon_isPFMuon;   //!
TBranch        *b_muT_muon_isLooseMuon;   //!
TBranch        *b_muT_muon_sumChargedParticlePt_DR4;   //!
TBranch        *b_muT_muon_sumPhotonEt_DR4;   //!
TBranch        *b_muT_muon_sumNeutralHadronEt_DR4;   //!
TBranch        *b_muT_muon_sumPUPt_DR4;   //!
TBranch        *b_muT_muon_relativeIso_DR4;   //!
TBranch        *b_muT_muon_sumChargedParticlePt_DR3;   //!
TBranch        *b_muT_muon_sumPhotonEt_DR3;   //!
TBranch        *b_muT_muon_sumNeutralHadronEt_DR3;   //!
TBranch        *b_muT_muon_sumPUPt_DR3;   //!
TBranch        *b_muT_muon_relativeIso_DR3;   //!
TBranch        *b_muT_muon_isPFIsolationValid;   //!
TBranch        *b_muT_muon_charge;   //!
TBranch        *b_muT_muon_PFpdgId;   //!
TBranch        *b_muT_muon_GENpdgId;   //!
TBranch        *b_muT_muon_normalizedChi2;   //!
TBranch        *b_muT_muon_numberOfValidMuonHits;   //!
TBranch        *b_muT_muon_numberOfMatchedStations;   //!
TBranch        *b_muT_muon_numberOfValidPixelHits;   //!
TBranch        *b_muT_muon_trackerLayersWithMeasurement;   //!
TBranch        *b_muT_muon_dB;   //!
TBranch        *b_muT_muon_dz;   //!
TBranch        *b_muT_muon_dxy;   //!
TBranch        *b_muT_muon_passFullId;   //!
TBranch        *b_muT_muon_has_HltMatchMu17;   //!
TBranch        *b_muT_muon_has_HltMatchMu18;   //!
TBranch        *b_muT_muon_has_HltMatchMu24;   //!
TBranch        *b_muT_muon_isTriLeptonVetoCandidate;   //!
TBranch        *b_muT_muon_isTrackerMuon;   //!
TBranch        *b_muT_tau_pfJetRefP4_x;   //!
TBranch        *b_muT_tau_pfJetRefP4_y;   //!
TBranch        *b_muT_tau_pfJetRefP4_z;   //!
TBranch        *b_muT_tau_pfJetRefP4_t;   //!
TBranch        *b_muT_tau_p4_x;   //!
TBranch        *b_muT_tau_p4_y;   //!
TBranch        *b_muT_tau_p4_z;   //!
TBranch        *b_muT_tau_p4_t;   //!
TBranch        *b_muT_tau_genP4_x;   //!
TBranch        *b_muT_tau_genP4_y;   //!
TBranch        *b_muT_tau_genP4_z;   //!
TBranch        *b_muT_tau_genP4_t;   //!
TBranch        *b_muT_tau_genJet_x;   //!
TBranch        *b_muT_tau_genJet_y;   //!
TBranch        *b_muT_tau_genJet_z;   //!
TBranch        *b_muT_tau_genJet_t;   //!
TBranch        *b_muT_tau_corrected_p4_x;   //!
TBranch        *b_muT_tau_corrected_p4_y;   //!
TBranch        *b_muT_tau_corrected_p4_z;   //!
TBranch        *b_muT_tau_corrected_p4_t;   //!
TBranch        *b_muT_tau_pdgId;   //!
TBranch        *b_muT_tau_pdgIdGEN;   //!
TBranch        *b_muT_tau_charge;   //!
TBranch        *b_muT_tau_decayMode;   //!
TBranch        *b_muT_tau_passFullId_muTau;   //!
TBranch        *b_muT_tau_passFullId_eTau;   //!
TBranch        *b_muT_tau_numStrips;   //!
TBranch        *b_muT_tau_numHadrons;   //!
TBranch        *b_muT_tau_againstElectronDeadECAL;   //!
TBranch        *b_muT_tau_againstElectronLoose;   //!
TBranch        *b_muT_tau_againstElectronLooseMVA5;   //!
TBranch        *b_muT_tau_againstElectronMVA5category;   //!
TBranch        *b_muT_tau_againstElectronMVA5raw;   //!
TBranch        *b_muT_tau_againstElectronMedium;   //!
TBranch        *b_muT_tau_againstElectronMediumMVA5;   //!
TBranch        *b_muT_tau_againstElectronTight;   //!
TBranch        *b_muT_tau_againstElectronTightMVA5;   //!
TBranch        *b_muT_tau_againstElectronVLooseMVA5;   //!
TBranch        *b_muT_tau_againstElectronVTightMVA5;   //!
TBranch        *b_muT_tau_againstMuonLoose;   //!
TBranch        *b_muT_tau_againstMuonLoose2;   //!
TBranch        *b_muT_tau_againstMuonLoose3;   //!
TBranch        *b_muT_tau_againstMuonLooseMVA;   //!
TBranch        *b_muT_tau_againstMuonMVAraw;   //!
TBranch        *b_muT_tau_againstMuonMedium;   //!
TBranch        *b_muT_tau_againstMuonMedium2;   //!
TBranch        *b_muT_tau_againstMuonMediumMVA;   //!
TBranch        *b_muT_tau_againstMuonTight;   //!
TBranch        *b_muT_tau_againstMuonTight2;   //!
TBranch        *b_muT_tau_againstMuonTight3;   //!
TBranch        *b_muT_tau_againstMuonTightMVA;   //!
TBranch        *b_muT_tau_byCombinedIsolationDeltaBetaCorrRaw;   //!
TBranch        *b_muT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits;   //!
TBranch        *b_muT_tau_byIsolationMVA3newDMwLTraw;   //!
TBranch        *b_muT_tau_byIsolationMVA3newDMwoLTraw;   //!
TBranch        *b_muT_tau_byIsolationMVA3oldDMwLTraw;   //!
TBranch        *b_muT_tau_byIsolationMVA3oldDMwoLTraw;   //!
TBranch        *b_muT_tau_byLooseCombinedIsolationDeltaBetaCorr;   //!
TBranch        *b_muT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits;   //!
TBranch        *b_muT_tau_byLooseIsolation;   //!
TBranch        *b_muT_tau_byLooseIsolationMVA3newDMwLT;   //!
TBranch        *b_muT_tau_byLooseIsolationMVA3newDMwoLT;   //!
TBranch        *b_muT_tau_byLooseIsolationMVA3oldDMwLT;   //!
TBranch        *b_muT_tau_byLooseIsolationMVA3oldDMwoLT;   //!
TBranch        *b_muT_tau_byMediumCombinedIsolationDeltaBetaCorr;   //!
TBranch        *b_muT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits;   //!
TBranch        *b_muT_tau_byMediumIsolationMVA3newDMwLT;   //!
TBranch        *b_muT_tau_byMediumIsolationMVA3newDMwoLT;   //!
TBranch        *b_muT_tau_byMediumIsolationMVA3oldDMwLT;   //!
TBranch        *b_muT_tau_byMediumIsolationMVA3oldDMwoLT;   //!
TBranch        *b_muT_tau_byTightCombinedIsolationDeltaBetaCorr;   //!
TBranch        *b_muT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits;   //!
TBranch        *b_muT_tau_byTightIsolationMVA3newDMwLT;   //!
TBranch        *b_muT_tau_byTightIsolationMVA3newDMwoLT;   //!
TBranch        *b_muT_tau_byTightIsolationMVA3oldDMwLT;   //!
TBranch        *b_muT_tau_byTightIsolationMVA3oldDMwoLT;   //!
TBranch        *b_muT_tau_byVLooseCombinedIsolationDeltaBetaCorr;   //!
TBranch        *b_muT_tau_byVLooseIsolationMVA3newDMwLT;   //!
TBranch        *b_muT_tau_byVLooseIsolationMVA3newDMwoLT;   //!
TBranch        *b_muT_tau_byVLooseIsolationMVA3oldDMwLT;   //!
TBranch        *b_muT_tau_byVLooseIsolationMVA3oldDMwoLT;   //!
TBranch        *b_muT_tau_byVTightIsolationMVA3newDMwLT;   //!
TBranch        *b_muT_tau_byVTightIsolationMVA3newDMwoLT;   //!
TBranch        *b_muT_tau_byVTightIsolationMVA3oldDMwLT;   //!
TBranch        *b_muT_tau_byVTightIsolationMVA3oldDMwoLT;   //!
TBranch        *b_muT_tau_byVVTightIsolationMVA3newDMwLT;   //!
TBranch        *b_muT_tau_byVVTightIsolationMVA3newDMwoLT;   //!
TBranch        *b_muT_tau_byVVTightIsolationMVA3oldDMwLT;   //!
TBranch        *b_muT_tau_byVVTightIsolationMVA3oldDMwoLT;   //!
TBranch        *b_muT_tau_chargedIsoPtSum;   //!
TBranch        *b_muT_tau_decayModeFinding;   //!
TBranch        *b_muT_tau_decayModeFindingNewDMs;   //!
TBranch        *b_muT_tau_decayModeFindingOldDMs;   //!
TBranch        *b_muT_tau_neutralIsoPtSum;   //!
TBranch        *b_muT_tau_puCorrPtSum;   //!
TBranch        *b_muT_tau_has_HltMatchEle20;   //!
TBranch        *b_muT_tau_has_HltMatchEle22;   //!
TBranch        *b_muT_tau_has_HltMatchEle27;   //!
TBranch        *b_muT_tau_has_HltMatchMu17;   //!
TBranch        *b_muT_tau_has_HltMatchMu18;   //!
TBranch        *b_muT_tau_has_HltMatchMu24;   //!
TBranch        *b_muT_puWeight;   //!
TBranch        *b_muT_puWeightM1;   //!
TBranch        *b_muT_puWeightP1;   //!
TBranch        *b_muT_NumPileupInt;   //!
TBranch        *b_muT_NumTruePileUpInt;   //!
TBranch        *b_muT_NumPileupIntM1;   //!
TBranch        *b_muT_NumTruePileUpIntM1;   //!
TBranch        *b_muT_NumPileupIntP1;   //!
TBranch        *b_muT_NumTruePileUpIntP1;   //!
TBranch        *b_muT_EffDataISOMU17andISOMU18;   //!
TBranch        *b_muT_EffMcISOMU17andISOMU18;   //!
TBranch        *b_muT_HadronicTauDataTrigEffAntiMuMed;   //!
TBranch        *b_muT_HadronicTauMcTrigEffAntiMuMed;   //!
TBranch        *b_muT_muonDataIDweight;   //!
TBranch        *b_muT_muonMcIDweight;   //!
TBranch        *b_muT_muonDataISOLweight;   //!
TBranch        *b_muT_muonMcISOLweight;   //!
TBranch        *b_muT_EffDataHighPtTauTrigger;   //!
TBranch        *b_muT_EffMcHighPtTauTrigger;   //!
TBranch        *b_muT_TauFakeCorrection;   //!
TBranch        *b_muT_DecayModeCorrectionFactor;   //!
TBranch        *b_muT_nominalHIGLUXHQTmhmax;   //!
TBranch        *b_muT_upHIGLUXHQTmhmax;   //!
TBranch        *b_muT_downHIGLUXHQTmhmax;   //!
TBranch        *b_muT_nominalPOWHEGmhmod;   //!
TBranch        *b_muT_upPOWHEGmhmod;   //!
TBranch        *b_muT_downPOWHEGmhmod;   //!
TBranch        *b_muT_upPOWHEGscale;   //!
TBranch        *b_muT_downPOWHEGscale;   //!
TBranch        *b_muT_etaDepQCDShapeTemplateCorrection;   //!
TBranch        *b_muT_inclusiveQCDShapeTemplateCorrection;   //!
TBranch        *b_muT_TTbarPtWeight;   //!
TBranch        *b_muT_TauSpinnerWT;   //!
TBranch        *b_muT_TauSpinnerWTFlip;   //!
TBranch        *b_muT_TauSpinnerWThminus;   //!
TBranch        *b_muT_TauSpinnerWThplus;   //!
TBranch        *b_muT_hepNUP;   //!
TBranch        *b_muT_weightHEPNUP_DYJets;   //!
TBranch        *b_muT_weightHEPNUP_WJets;   //!
TBranch        *b_muT_passesSecondLeptonVeto;   //!
TBranch        *b_muT_passesThirdLeptonVeto;   //!
TBranch        *b_eT_embedWeight;
TBranch        *b_muT_embedWeight;



void deRef()
{



  run_ = run;
  luminosityBlock_ = luminosityBlock;
  event_ = event;
  isRealData_ = isRealData;
  bunchCrossing_ = bunchCrossing;
  orbitNumber_ = orbitNumber;
  NAMEVAR_ = *NAMEVAR;
  SampleName_ = *SampleName;
  PhysicsProcess_ = *PhysicsProcess;
  isNonTopEmbeddedSample_ = isNonTopEmbeddedSample;
  isTopEmbeddedSample_ = isTopEmbeddedSample;
  MASS_ = MASS;
  crossSection_ = crossSection;
  branchingFraction_ = branchingFraction;
  numberEvents_ = numberEvents;
  eT_p4_x_ = *eT_p4_x;
  eT_p4_y_ = *eT_p4_y;
  eT_p4_z_ = *eT_p4_z;
  eT_p4_t_ = *eT_p4_t;
  eT_corrected_p4_x_ = *eT_corrected_p4_x;
  eT_corrected_p4_y_ = *eT_corrected_p4_y;
  eT_corrected_p4_z_ = *eT_corrected_p4_z;
  eT_corrected_p4_t_ = *eT_corrected_p4_t;
  eT_electronIndex_ = *eT_electronIndex;
  eT_tauIndex_ = *eT_tauIndex;
  eT_scalarSumPt_ = *eT_scalarSumPt;
  eT_DR_ = *eT_DR;
  eT_sumCharge_ = *eT_sumCharge;
  eT_correctedSVFitMass_ = *eT_correctedSVFitMass;
  eT_rawSVFitMass_ = *eT_rawSVFitMass;
  eT_TransverseMass_ = *eT_TransverseMass;
  eT_rawTransverseMass_ = *eT_rawTransverseMass;
  eT_mvaMETraw_ = *eT_mvaMETraw;
  eT_mvaMET_ = *eT_mvaMET;
  eT_mvaMETphiRaw_ = *eT_mvaMETphiRaw;
  eT_mvaMETphi_ = *eT_mvaMETphi;
  eT_MAX_ = *eT_MAX;
  eT_isGoodTriggerPair_ = *eT_isGoodTriggerPair;
  eT_njets_ = *eT_njets;
  eT_nbjets_ = *eT_nbjets;
  eT_nbjetsLOOSE_ = *eT_nbjetsLOOSE;
  eT_nbjetsLOOSEUP_ = *eT_nbjetsLOOSEUP;
  eT_nbjetsLOOSEDOWN_ = *eT_nbjetsLOOSEDOWN;
  eT_njetsUP_ = *eT_njetsUP;
  eT_nbjetsUP_ = *eT_nbjetsUP;
  eT_njetsDOWN_ = *eT_njetsDOWN;
  eT_nbjetsDOWN_ = *eT_nbjetsDOWN;
  eT_jet1P4_x_ = *eT_jet1P4_x;
  eT_jet1P4_y_ = *eT_jet1P4_y;
  eT_jet1P4_z_ = *eT_jet1P4_z;
  eT_jet1P4_t_ = *eT_jet1P4_t;
  eT_jet1RawP4_x_ = *eT_jet1RawP4_x;
  eT_jet1RawP4_y_ = *eT_jet1RawP4_y;
  eT_jet1RawP4_z_ = *eT_jet1RawP4_z;
  eT_jet1RawP4_t_ = *eT_jet1RawP4_t;
  eT_jet1IDMVA_ = *eT_jet1IDMVA;
  eT_jet1BTAGMVA_ = *eT_jet1BTAGMVA;
  eT_jet2P4_x_ = *eT_jet2P4_x;
  eT_jet2P4_y_ = *eT_jet2P4_y;
  eT_jet2P4_z_ = *eT_jet2P4_z;
  eT_jet2P4_t_ = *eT_jet2P4_t;
  eT_jet2RawP4_x_ = *eT_jet2RawP4_x;
  eT_jet2RawP4_y_ = *eT_jet2RawP4_y;
  eT_jet2RawP4_z_ = *eT_jet2RawP4_z;
  eT_jet2RawP4_t_ = *eT_jet2RawP4_t;
  eT_jet2IDMVA_ = *eT_jet2IDMVA;
  eT_jet2BTAGMVA_ = *eT_jet2BTAGMVA;
  eT_cov00_ = *eT_cov00;
  eT_cov01_ = *eT_cov01;
  eT_cov10_ = *eT_cov10;
  eT_cov11_ = *eT_cov11;
  eT_passesTriLeptonVeto_ = *eT_passesTriLeptonVeto;
  eT_passNonTopEmbeddedTriggerAndMass50_ = *eT_passNonTopEmbeddedTriggerAndMass50;
  eT_passSignalGeneratorMass70to130Cut_ = *eT_passSignalGeneratorMass70to130Cut;
  eT_genBosonP4_x_ = *eT_genBosonP4_x;
  eT_genBosonP4_y_ = *eT_genBosonP4_y;
  eT_genBosonP4_z_ = *eT_genBosonP4_z;
  eT_genBosonP4_t_ = *eT_genBosonP4_t;
  eT_genTOPp4_x_ = *eT_genTOPp4_x;
  eT_genTOPp4_y_ = *eT_genTOPp4_y;
  eT_genTOPp4_z_ = *eT_genTOPp4_z;
  eT_genTOPp4_t_ = *eT_genTOPp4_t;
  eT_genTOPBARp4_x_ = *eT_genTOPBARp4_x;
  eT_genTOPBARp4_y_ = *eT_genTOPBARp4_y;
  eT_genTOPBARp4_z_ = *eT_genTOPBARp4_z;
  eT_genTOPBARp4_t_ = *eT_genTOPBARp4_t;
  eT_numberOfGoodVertices_ = *eT_numberOfGoodVertices;
  eT_PVndof_ = *eT_PVndof;
  eT_PVz_ = *eT_PVz;
  eT_PVpositionRho_ = *eT_PVpositionRho;
  eT_PVp4_x_ = *eT_PVp4_x;
  eT_PVp4_y_ = *eT_PVp4_y;
  eT_PVp4_z_ = *eT_PVp4_z;
  eT_PVp4_t_ = *eT_PVp4_t;



  if(eT_isDecayZtauTau!=0) eT_isDecayZtauTau_ = *eT_isDecayZtauTau;
  if(eT_isDecayZeE!=0) eT_isDecayZeE_ = *eT_isDecayZeE;
  if(eT_isDecayZmuMu!=0) eT_isDecayZmuMu_ = *eT_isDecayZmuMu;
  if(eT_isRecoLep_matchedTo_GenTauFromZ!=0) eT_isRecoLep_matchedTo_GenTauFromZ_ = *eT_isRecoLep_matchedTo_GenTauFromZ;
  if(eT_isRecoTau_matchedTo_GenTauFromZ!=0) eT_isRecoTau_matchedTo_GenTauFromZ_ = *eT_isRecoTau_matchedTo_GenTauFromZ;
  if(eT_isRecoLep_matchedTo_GenElecFromZ!=0) eT_isRecoLep_matchedTo_GenElecFromZ_ = *eT_isRecoLep_matchedTo_GenElecFromZ;
  if(eT_isRecoTau_matchedTo_GenElecFromZ!=0) eT_isRecoTau_matchedTo_GenElecFromZ_ = *eT_isRecoTau_matchedTo_GenElecFromZ;
  if(eT_isRecoLep_matchedTo_GenMuonFromZ!=0) eT_isRecoLep_matchedTo_GenMuonFromZ_ = *eT_isRecoLep_matchedTo_GenMuonFromZ;
  if(eT_isRecoTau_matchedTo_GenMuonFromZ!=0) eT_isRecoTau_matchedTo_GenMuonFromZ_ = *eT_isRecoTau_matchedTo_GenMuonFromZ;
  if(eT_isRecoLep_matchedTo_GenElecFromTau!=0) eT_isRecoLep_matchedTo_GenElecFromTau_ = *eT_isRecoLep_matchedTo_GenElecFromTau;
  if(eT_isRecoTau_matchedTo_GenElecFromTau!=0) eT_isRecoTau_matchedTo_GenElecFromTau_ = *eT_isRecoTau_matchedTo_GenElecFromTau;
  if(eT_isRecoLep_matchedTo_GenMuonFromTau!=0) eT_isRecoLep_matchedTo_GenMuonFromTau_ = *eT_isRecoLep_matchedTo_GenMuonFromTau;
  if(eT_isRecoTau_matchedTo_GenMuonFromTau!=0) eT_isRecoTau_matchedTo_GenMuonFromTau_ = *eT_isRecoTau_matchedTo_GenMuonFromTau;
  if(eT_passEmbeddedTrigger!=0) eT_passEmbeddedTrigger_ = *eT_passEmbeddedTrigger;
  if(eT_embedWeight!=0) eT_embedWeight_ = *eT_embedWeight;


  eT_ele_p4_x_ = *eT_ele_p4_x;
  eT_ele_p4_y_ = *eT_ele_p4_y;
  eT_ele_p4_z_ = *eT_ele_p4_z;
  eT_ele_p4_t_ = *eT_ele_p4_t;
  eT_ele_genP4_x_ = *eT_ele_genP4_x;
  eT_ele_genP4_y_ = *eT_ele_genP4_y;
  eT_ele_genP4_z_ = *eT_ele_genP4_z;
  eT_ele_genP4_t_ = *eT_ele_genP4_t;
  eT_ele_pfP4_x_ = *eT_ele_pfP4_x;
  eT_ele_pfP4_y_ = *eT_ele_pfP4_y;
  eT_ele_pfP4_z_ = *eT_ele_pfP4_z;
  eT_ele_pfP4_t_ = *eT_ele_pfP4_t;
  eT_ele_charge_ = *eT_ele_charge;
  eT_ele_PFpdgId_ = *eT_ele_PFpdgId;
  eT_ele_GENpdgId_ = *eT_ele_GENpdgId;
  eT_ele_numberOfMissingInnerHits_ = *eT_ele_numberOfMissingInnerHits;
  eT_ele_passConversionVeto_ = *eT_ele_passConversionVeto;
  eT_ele_dz_ = *eT_ele_dz;
  eT_ele_dB_ = *eT_ele_dB;
  eT_ele_dxy_ = *eT_ele_dxy;
  eT_ele_SuperClusterEta_ = *eT_ele_SuperClusterEta;
  eT_ele_mvaTrigV0_ = *eT_ele_mvaTrigV0;
  eT_ele_mvaTrigNoIPV0_ = *eT_ele_mvaTrigNoIPV0;
  eT_ele_mvaNonTrigV0_ = *eT_ele_mvaNonTrigV0;
  eT_ele_pass_tight_mvaNonTrigV0_ = *eT_ele_pass_tight_mvaNonTrigV0;
  eT_ele_passFullId_ = *eT_ele_passFullId;
  eT_ele_chargedHadronIso_ = *eT_ele_chargedHadronIso;
  eT_ele_photonIso_ = *eT_ele_photonIso;
  eT_ele_neutralHadronIso_ = *eT_ele_neutralHadronIso;
  eT_ele_puChargedHadronIso_ = *eT_ele_puChargedHadronIso;
  eT_ele_relativeIso_ = *eT_ele_relativeIso;
  eT_ele_isEB_ = *eT_ele_isEB;
  eT_ele_isEE_ = *eT_ele_isEE;
  eT_ele_isEBEEGap_ = *eT_ele_isEBEEGap;
  eT_ele_isEBEtaGap_ = *eT_ele_isEBEtaGap;
  eT_ele_isEBPhiGap_ = *eT_ele_isEBPhiGap;
  eT_ele_isEEDeeGap_ = *eT_ele_isEEDeeGap;
  eT_ele_isEERingGap_ = *eT_ele_isEERingGap;
  eT_ele_sigmaEtaEta_ = *eT_ele_sigmaEtaEta;
  eT_ele_sigmaIetaIeta_ = *eT_ele_sigmaIetaIeta;
  eT_ele_sigmaIphiIphi_ = *eT_ele_sigmaIphiIphi;
  eT_ele_has_HltMatchEle20_ = *eT_ele_has_HltMatchEle20;
  eT_ele_has_HltMatchEle22_ = *eT_ele_has_HltMatchEle22;
  eT_ele_has_HltMatchEle27_ = *eT_ele_has_HltMatchEle27;
  eT_ele_isTriLeptonVetoCandidate_ = *eT_ele_isTriLeptonVetoCandidate;
  eT_ele_deltaPhiSuperClusterTrackAtVtx_ = *eT_ele_deltaPhiSuperClusterTrackAtVtx;
  eT_ele_deltaEtaSuperClusterTrackAtVtx_ = *eT_ele_deltaEtaSuperClusterTrackAtVtx;
  eT_ele_hadronicOverEm_ = *eT_ele_hadronicOverEm;
  eT_tau_pfJetRefP4_x_ = *eT_tau_pfJetRefP4_x;
  eT_tau_pfJetRefP4_y_ = *eT_tau_pfJetRefP4_y;
  eT_tau_pfJetRefP4_z_ = *eT_tau_pfJetRefP4_z;
  eT_tau_pfJetRefP4_t_ = *eT_tau_pfJetRefP4_t;
  eT_tau_p4_x_ = *eT_tau_p4_x;
  eT_tau_p4_y_ = *eT_tau_p4_y;
  eT_tau_p4_z_ = *eT_tau_p4_z;
  eT_tau_p4_t_ = *eT_tau_p4_t;
  eT_tau_genP4_x_ = *eT_tau_genP4_x;
  eT_tau_genP4_y_ = *eT_tau_genP4_y;
  eT_tau_genP4_z_ = *eT_tau_genP4_z;
  eT_tau_genP4_t_ = *eT_tau_genP4_t;
  eT_tau_genJet_x_ = *eT_tau_genJet_x;
  eT_tau_genJet_y_ = *eT_tau_genJet_y;
  eT_tau_genJet_z_ = *eT_tau_genJet_z;
  eT_tau_genJet_t_ = *eT_tau_genJet_t;
  eT_tau_corrected_p4_x_ = *eT_tau_corrected_p4_x;
  eT_tau_corrected_p4_y_ = *eT_tau_corrected_p4_y;
  eT_tau_corrected_p4_z_ = *eT_tau_corrected_p4_z;
  eT_tau_corrected_p4_t_ = *eT_tau_corrected_p4_t;
  eT_tau_pdgId_ = *eT_tau_pdgId;
  eT_tau_pdgIdGEN_ = *eT_tau_pdgIdGEN;
  eT_tau_charge_ = *eT_tau_charge;
  eT_tau_decayMode_ = *eT_tau_decayMode;
  eT_tau_passFullId_muTau_ = *eT_tau_passFullId_muTau;
  eT_tau_passFullId_eTau_ = *eT_tau_passFullId_eTau;
  eT_tau_numStrips_ = *eT_tau_numStrips;
  eT_tau_numHadrons_ = *eT_tau_numHadrons;
  eT_tau_againstElectronDeadECAL_ = *eT_tau_againstElectronDeadECAL;
  eT_tau_againstElectronLoose_ = *eT_tau_againstElectronLoose;
  eT_tau_againstElectronLooseMVA5_ = *eT_tau_againstElectronLooseMVA5;
  eT_tau_againstElectronMVA5category_ = *eT_tau_againstElectronMVA5category;
  eT_tau_againstElectronMVA5raw_ = *eT_tau_againstElectronMVA5raw;
  eT_tau_againstElectronMedium_ = *eT_tau_againstElectronMedium;
  eT_tau_againstElectronMediumMVA5_ = *eT_tau_againstElectronMediumMVA5;
  eT_tau_againstElectronTight_ = *eT_tau_againstElectronTight;
  eT_tau_againstElectronTightMVA5_ = *eT_tau_againstElectronTightMVA5;
  eT_tau_againstElectronVLooseMVA5_ = *eT_tau_againstElectronVLooseMVA5;
  eT_tau_againstElectronVTightMVA5_ = *eT_tau_againstElectronVTightMVA5;
  eT_tau_againstMuonLoose_ = *eT_tau_againstMuonLoose;
  eT_tau_againstMuonLoose2_ = *eT_tau_againstMuonLoose2;
  eT_tau_againstMuonLoose3_ = *eT_tau_againstMuonLoose3;
  eT_tau_againstMuonLooseMVA_ = *eT_tau_againstMuonLooseMVA;
  eT_tau_againstMuonMVAraw_ = *eT_tau_againstMuonMVAraw;
  eT_tau_againstMuonMedium_ = *eT_tau_againstMuonMedium;
  eT_tau_againstMuonMedium2_ = *eT_tau_againstMuonMedium2;
  eT_tau_againstMuonMediumMVA_ = *eT_tau_againstMuonMediumMVA;
  eT_tau_againstMuonTight_ = *eT_tau_againstMuonTight;
  eT_tau_againstMuonTight2_ = *eT_tau_againstMuonTight2;
  eT_tau_againstMuonTight3_ = *eT_tau_againstMuonTight3;
  eT_tau_againstMuonTightMVA_ = *eT_tau_againstMuonTightMVA;
  eT_tau_byCombinedIsolationDeltaBetaCorrRaw_ = *eT_tau_byCombinedIsolationDeltaBetaCorrRaw;
  eT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits_ = *eT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits;
  eT_tau_byIsolationMVA3newDMwLTraw_ = *eT_tau_byIsolationMVA3newDMwLTraw;
  eT_tau_byIsolationMVA3newDMwoLTraw_ = *eT_tau_byIsolationMVA3newDMwoLTraw;
  eT_tau_byIsolationMVA3oldDMwLTraw_ = *eT_tau_byIsolationMVA3oldDMwLTraw;
  eT_tau_byIsolationMVA3oldDMwoLTraw_ = *eT_tau_byIsolationMVA3oldDMwoLTraw;
  eT_tau_byLooseCombinedIsolationDeltaBetaCorr_ = *eT_tau_byLooseCombinedIsolationDeltaBetaCorr;
  eT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits_ = *eT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits;
  eT_tau_byLooseIsolation_ = *eT_tau_byLooseIsolation;
  eT_tau_byLooseIsolationMVA3newDMwLT_ = *eT_tau_byLooseIsolationMVA3newDMwLT;
  eT_tau_byLooseIsolationMVA3newDMwoLT_ = *eT_tau_byLooseIsolationMVA3newDMwoLT;
  eT_tau_byLooseIsolationMVA3oldDMwLT_ = *eT_tau_byLooseIsolationMVA3oldDMwLT;
  eT_tau_byLooseIsolationMVA3oldDMwoLT_ = *eT_tau_byLooseIsolationMVA3oldDMwoLT;
  eT_tau_byMediumCombinedIsolationDeltaBetaCorr_ = *eT_tau_byMediumCombinedIsolationDeltaBetaCorr;
  eT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits_ = *eT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits;
  eT_tau_byMediumIsolationMVA3newDMwLT_ = *eT_tau_byMediumIsolationMVA3newDMwLT;
  eT_tau_byMediumIsolationMVA3newDMwoLT_ = *eT_tau_byMediumIsolationMVA3newDMwoLT;
  eT_tau_byMediumIsolationMVA3oldDMwLT_ = *eT_tau_byMediumIsolationMVA3oldDMwLT;
  eT_tau_byMediumIsolationMVA3oldDMwoLT_ = *eT_tau_byMediumIsolationMVA3oldDMwoLT;
  eT_tau_byTightCombinedIsolationDeltaBetaCorr_ = *eT_tau_byTightCombinedIsolationDeltaBetaCorr;
  eT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits_ = *eT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits;
  eT_tau_byTightIsolationMVA3newDMwLT_ = *eT_tau_byTightIsolationMVA3newDMwLT;
  eT_tau_byTightIsolationMVA3newDMwoLT_ = *eT_tau_byTightIsolationMVA3newDMwoLT;
  eT_tau_byTightIsolationMVA3oldDMwLT_ = *eT_tau_byTightIsolationMVA3oldDMwLT;
  eT_tau_byTightIsolationMVA3oldDMwoLT_ = *eT_tau_byTightIsolationMVA3oldDMwoLT;
  eT_tau_byVLooseCombinedIsolationDeltaBetaCorr_ = *eT_tau_byVLooseCombinedIsolationDeltaBetaCorr;
  eT_tau_byVLooseIsolationMVA3newDMwLT_ = *eT_tau_byVLooseIsolationMVA3newDMwLT;
  eT_tau_byVLooseIsolationMVA3newDMwoLT_ = *eT_tau_byVLooseIsolationMVA3newDMwoLT;
  eT_tau_byVLooseIsolationMVA3oldDMwLT_ = *eT_tau_byVLooseIsolationMVA3oldDMwLT;
  eT_tau_byVLooseIsolationMVA3oldDMwoLT_ = *eT_tau_byVLooseIsolationMVA3oldDMwoLT;
  eT_tau_byVTightIsolationMVA3newDMwLT_ = *eT_tau_byVTightIsolationMVA3newDMwLT;
  eT_tau_byVTightIsolationMVA3newDMwoLT_ = *eT_tau_byVTightIsolationMVA3newDMwoLT;
  eT_tau_byVTightIsolationMVA3oldDMwLT_ = *eT_tau_byVTightIsolationMVA3oldDMwLT;
  eT_tau_byVTightIsolationMVA3oldDMwoLT_ = *eT_tau_byVTightIsolationMVA3oldDMwoLT;
  eT_tau_byVVTightIsolationMVA3newDMwLT_ = *eT_tau_byVVTightIsolationMVA3newDMwLT;
  eT_tau_byVVTightIsolationMVA3newDMwoLT_ = *eT_tau_byVVTightIsolationMVA3newDMwoLT;
  eT_tau_byVVTightIsolationMVA3oldDMwLT_ = *eT_tau_byVVTightIsolationMVA3oldDMwLT;
  eT_tau_byVVTightIsolationMVA3oldDMwoLT_ = *eT_tau_byVVTightIsolationMVA3oldDMwoLT;
  eT_tau_chargedIsoPtSum_ = *eT_tau_chargedIsoPtSum;
  eT_tau_decayModeFinding_ = *eT_tau_decayModeFinding;
  eT_tau_decayModeFindingNewDMs_ = *eT_tau_decayModeFindingNewDMs;
  eT_tau_decayModeFindingOldDMs_ = *eT_tau_decayModeFindingOldDMs;
  eT_tau_neutralIsoPtSum_ = *eT_tau_neutralIsoPtSum;
  eT_tau_puCorrPtSum_ = *eT_tau_puCorrPtSum;
  eT_tau_has_HltMatchEle20_ = *eT_tau_has_HltMatchEle20;
  eT_tau_has_HltMatchEle22_ = *eT_tau_has_HltMatchEle22;
  eT_tau_has_HltMatchEle27_ = *eT_tau_has_HltMatchEle27;
  eT_tau_has_HltMatchMu17_ = *eT_tau_has_HltMatchMu17;
  eT_tau_has_HltMatchMu18_ = *eT_tau_has_HltMatchMu18;
  eT_tau_has_HltMatchMu24_ = *eT_tau_has_HltMatchMu24;
  eT_puWeight_ = *eT_puWeight;
  eT_puWeightM1_ = *eT_puWeightM1;
  eT_puWeightP1_ = *eT_puWeightP1;
  eT_NumPileupInt_ = *eT_NumPileupInt;
  eT_NumTruePileUpInt_ = *eT_NumTruePileUpInt;
  eT_NumPileupIntM1_ = *eT_NumPileupIntM1;
  eT_NumTruePileUpIntM1_ = *eT_NumTruePileUpIntM1;
  eT_NumPileupIntP1_ = *eT_NumPileupIntP1;
  eT_NumTruePileUpIntP1_ = *eT_NumTruePileUpIntP1;
  eT_EffDataELE20andELE22_ = *eT_EffDataELE20andELE22;
  eT_EffMcELE20andELE22_ = *eT_EffMcELE20andELE22;
  eT_HadronicTauDataTrigEffAntiEMed_ = *eT_HadronicTauDataTrigEffAntiEMed;
  eT_HadronicTauMcTrigEffAntiEMed_ = *eT_HadronicTauMcTrigEffAntiEMed;
  eT_HadronicTauDataTrigEffAntiETight_ = *eT_HadronicTauDataTrigEffAntiETight;
  eT_HadronicTauMcTrigEffAntiETight_ = *eT_HadronicTauMcTrigEffAntiETight;
  eT_electronDataIDweight_ = *eT_electronDataIDweight;
  eT_electronMcIDweight_ = *eT_electronMcIDweight;
  eT_electronDataISOLweight_ = *eT_electronDataISOLweight;
  eT_electronMcISOLweight_ = *eT_electronMcISOLweight;
  eT_EffDataHighPtTauTrigger_ = *eT_EffDataHighPtTauTrigger;
  eT_EffMcHighPtTauTrigger_ = *eT_EffMcHighPtTauTrigger;
  eT_TauFakeCorrection_ = *eT_TauFakeCorrection;
  eT_DecayModeCorrectionFactor_ = *eT_DecayModeCorrectionFactor;
  eT_ZeeScaleFactor_ = *eT_ZeeScaleFactor;
  eT_nominalHIGLUXHQTmhmax_ = *eT_nominalHIGLUXHQTmhmax;
  eT_upHIGLUXHQTmhmax_ = *eT_upHIGLUXHQTmhmax;
  eT_downHIGLUXHQTmhmax_ = *eT_downHIGLUXHQTmhmax;
  eT_nominalPOWHEGmhmod_ = *eT_nominalPOWHEGmhmod;
  eT_upPOWHEGmhmod_ = *eT_upPOWHEGmhmod;
  eT_downPOWHEGmhmod_ = *eT_downPOWHEGmhmod;
  eT_upPOWHEGscale_ = *eT_upPOWHEGscale;
  eT_downPOWHEGscale_ = *eT_downPOWHEGscale;
  eT_etaDepQCDShapeTemplateCorrection_ = *eT_etaDepQCDShapeTemplateCorrection;
  eT_inclusiveQCDShapeTemplateCorrection_ = *eT_inclusiveQCDShapeTemplateCorrection;
  eT_TTbarPtWeight_ = *eT_TTbarPtWeight;
  eT_TauSpinnerWT_ = *eT_TauSpinnerWT;
  eT_TauSpinnerWTFlip_ = *eT_TauSpinnerWTFlip;
  eT_TauSpinnerWThminus_ = *eT_TauSpinnerWThminus;
  eT_TauSpinnerWThplus_ = *eT_TauSpinnerWThplus;
  eT_hepNUP_ = *eT_hepNUP;
  eT_weightHEPNUP_DYJets_ = *eT_weightHEPNUP_DYJets;
  eT_weightHEPNUP_WJets_ = *eT_weightHEPNUP_WJets;
  eT_passesSecondLeptonVeto_ = *eT_passesSecondLeptonVeto;
  eT_passesThirdLeptonVeto_ = *eT_passesThirdLeptonVeto;
  muT_p4_x_ = *muT_p4_x;
  muT_p4_y_ = *muT_p4_y;
  muT_p4_z_ = *muT_p4_z;
  muT_p4_t_ = *muT_p4_t;
  muT_corrected_p4_x_ = *muT_corrected_p4_x;
  muT_corrected_p4_y_ = *muT_corrected_p4_y;
  muT_corrected_p4_z_ = *muT_corrected_p4_z;
  muT_corrected_p4_t_ = *muT_corrected_p4_t;
  muT_muonIndex_ = *muT_muonIndex;
  muT_tauIndex_ = *muT_tauIndex;
  muT_scalarSumPt_ = *muT_scalarSumPt;
  muT_DR_ = *muT_DR;
  muT_sumCharge_ = *muT_sumCharge;
  muT_correctedSVFitMass_ = *muT_correctedSVFitMass;
  muT_rawSVFitMass_ = *muT_rawSVFitMass;
  muT_TransverseMass_ = *muT_TransverseMass;
  muT_rawTransverseMass_ = *muT_rawTransverseMass;
  muT_mvaMETraw_ = *muT_mvaMETraw;
  muT_mvaMET_ = *muT_mvaMET;
  muT_mvaMETphiRaw_ = *muT_mvaMETphiRaw;
  muT_mvaMETphi_ = *muT_mvaMETphi;
  muT_MAX_ = *muT_MAX;
  muT_isGoodTriggerPair_ = *muT_isGoodTriggerPair;
  muT_njets_ = *muT_njets;
  muT_nbjets_ = *muT_nbjets;
  muT_nbjetsLOOSE_ = *muT_nbjetsLOOSE;
  muT_nbjetsLOOSEUP_ = *muT_nbjetsLOOSEUP;
  muT_nbjetsLOOSEDOWN_ = *muT_nbjetsLOOSEDOWN;
  muT_njetsUP_ = *muT_njetsUP;
  muT_nbjetsUP_ = *muT_nbjetsUP;
  muT_njetsDOWN_ = *muT_njetsDOWN;
  muT_nbjetsDOWN_ = *muT_nbjetsDOWN;
  muT_jet1P4_x_ = *muT_jet1P4_x;
  muT_jet1P4_y_ = *muT_jet1P4_y;
  muT_jet1P4_z_ = *muT_jet1P4_z;
  muT_jet1P4_t_ = *muT_jet1P4_t;
  muT_jet1RawP4_x_ = *muT_jet1RawP4_x;
  muT_jet1RawP4_y_ = *muT_jet1RawP4_y;
  muT_jet1RawP4_z_ = *muT_jet1RawP4_z;
  muT_jet1RawP4_t_ = *muT_jet1RawP4_t;
  muT_jet1IDMVA_ = *muT_jet1IDMVA;
  muT_jet1BTAGMVA_ = *muT_jet1BTAGMVA;
  muT_jet2P4_x_ = *muT_jet2P4_x;
  muT_jet2P4_y_ = *muT_jet2P4_y;
  muT_jet2P4_z_ = *muT_jet2P4_z;
  muT_jet2P4_t_ = *muT_jet2P4_t;
  muT_jet2RawP4_x_ = *muT_jet2RawP4_x;
  muT_jet2RawP4_y_ = *muT_jet2RawP4_y;
  muT_jet2RawP4_z_ = *muT_jet2RawP4_z;
  muT_jet2RawP4_t_ = *muT_jet2RawP4_t;
  muT_jet2IDMVA_ = *muT_jet2IDMVA;
  muT_jet2BTAGMVA_ = *muT_jet2BTAGMVA;
  muT_cov00_ = *muT_cov00;
  muT_cov01_ = *muT_cov01;
  muT_cov10_ = *muT_cov10;
  muT_cov11_ = *muT_cov11;
  muT_passesTriLeptonVeto_ = *muT_passesTriLeptonVeto;
  muT_passNonTopEmbeddedTriggerAndMass50_ = *muT_passNonTopEmbeddedTriggerAndMass50;
  muT_passSignalGeneratorMass70to130Cut_ = *muT_passSignalGeneratorMass70to130Cut;
  muT_genBosonP4_x_ = *muT_genBosonP4_x;
  muT_genBosonP4_y_ = *muT_genBosonP4_y;
  muT_genBosonP4_z_ = *muT_genBosonP4_z;
  muT_genBosonP4_t_ = *muT_genBosonP4_t;
  muT_genTOPp4_x_ = *muT_genTOPp4_x;
  muT_genTOPp4_y_ = *muT_genTOPp4_y;
  muT_genTOPp4_z_ = *muT_genTOPp4_z;
  muT_genTOPp4_t_ = *muT_genTOPp4_t;
  muT_genTOPBARp4_x_ = *muT_genTOPBARp4_x;
  muT_genTOPBARp4_y_ = *muT_genTOPBARp4_y;
  muT_genTOPBARp4_z_ = *muT_genTOPBARp4_z;
  muT_genTOPBARp4_t_ = *muT_genTOPBARp4_t;
  muT_numberOfGoodVertices_ = *muT_numberOfGoodVertices;
  muT_PVndof_ = *muT_PVndof;
  muT_PVz_ = *muT_PVz;
  muT_PVpositionRho_ = *muT_PVpositionRho;
  muT_PVp4_x_ = *muT_PVp4_x;
  muT_PVp4_y_ = *muT_PVp4_y;
  muT_PVp4_z_ = *muT_PVp4_z;
  muT_PVp4_t_ = *muT_PVp4_t;


    if(muT_isDecayZtauTau!=0) muT_isDecayZtauTau_ = *muT_isDecayZtauTau;
    if(muT_isDecayZeE!=0) muT_isDecayZeE_ = *muT_isDecayZeE;
    if(muT_isDecayZmuMu!=0) muT_isDecayZmuMu_ = *muT_isDecayZmuMu;
    if(muT_isRecoLep_matchedTo_GenTauFromZ!=0) muT_isRecoLep_matchedTo_GenTauFromZ_ = *muT_isRecoLep_matchedTo_GenTauFromZ;
    if(muT_isRecoTau_matchedTo_GenTauFromZ!=0) muT_isRecoTau_matchedTo_GenTauFromZ_ = *muT_isRecoTau_matchedTo_GenTauFromZ;
    if(muT_isRecoLep_matchedTo_GenElecFromZ!=0) muT_isRecoLep_matchedTo_GenElecFromZ_ = *muT_isRecoLep_matchedTo_GenElecFromZ;
    if(muT_isRecoTau_matchedTo_GenElecFromZ!=0) muT_isRecoTau_matchedTo_GenElecFromZ_ = *muT_isRecoTau_matchedTo_GenElecFromZ;
    if(muT_isRecoLep_matchedTo_GenMuonFromZ!=0) muT_isRecoLep_matchedTo_GenMuonFromZ_ = *muT_isRecoLep_matchedTo_GenMuonFromZ;
    if(muT_isRecoTau_matchedTo_GenMuonFromZ!=0) muT_isRecoTau_matchedTo_GenMuonFromZ_ = *muT_isRecoTau_matchedTo_GenMuonFromZ;
    if(muT_isRecoLep_matchedTo_GenElecFromTau!=0) muT_isRecoLep_matchedTo_GenElecFromTau_ = *muT_isRecoLep_matchedTo_GenElecFromTau;
    if(muT_isRecoTau_matchedTo_GenElecFromTau!=0) muT_isRecoTau_matchedTo_GenElecFromTau_ = *muT_isRecoTau_matchedTo_GenElecFromTau;
    if(muT_isRecoLep_matchedTo_GenMuonFromTau!=0) muT_isRecoLep_matchedTo_GenMuonFromTau_ = *muT_isRecoLep_matchedTo_GenMuonFromTau;
    if(muT_isRecoTau_matchedTo_GenMuonFromTau!=0) muT_isRecoTau_matchedTo_GenMuonFromTau_ = *muT_isRecoTau_matchedTo_GenMuonFromTau;
    if(muT_passEmbeddedTrigger!=0) muT_passEmbeddedTrigger_ = *muT_passEmbeddedTrigger;
    if(muT_embedWeight!=0) muT_embedWeight_ = *muT_embedWeight;


  muT_muon_p4_x_ = *muT_muon_p4_x;
  muT_muon_p4_y_ = *muT_muon_p4_y;
  muT_muon_p4_z_ = *muT_muon_p4_z;
  muT_muon_p4_t_ = *muT_muon_p4_t;
  muT_muon_pfP4_x_ = *muT_muon_pfP4_x;
  muT_muon_pfP4_y_ = *muT_muon_pfP4_y;
  muT_muon_pfP4_z_ = *muT_muon_pfP4_z;
  muT_muon_pfP4_t_ = *muT_muon_pfP4_t;
  muT_muon_genP4_x_ = *muT_muon_genP4_x;
  muT_muon_genP4_y_ = *muT_muon_genP4_y;
  muT_muon_genP4_z_ = *muT_muon_genP4_z;
  muT_muon_genP4_t_ = *muT_muon_genP4_t;
  muT_muon_isGlobalMuon_ = *muT_muon_isGlobalMuon;
  muT_muon_isTightMuon_ = *muT_muon_isTightMuon;
  muT_muon_isPFMuon_ = *muT_muon_isPFMuon;
  muT_muon_isLooseMuon_ = *muT_muon_isLooseMuon;
  muT_muon_sumChargedParticlePt_DR4_ = *muT_muon_sumChargedParticlePt_DR4;
  muT_muon_sumPhotonEt_DR4_ = *muT_muon_sumPhotonEt_DR4;
  muT_muon_sumNeutralHadronEt_DR4_ = *muT_muon_sumNeutralHadronEt_DR4;
  muT_muon_sumPUPt_DR4_ = *muT_muon_sumPUPt_DR4;
  muT_muon_relativeIso_DR4_ = *muT_muon_relativeIso_DR4;
  muT_muon_sumChargedParticlePt_DR3_ = *muT_muon_sumChargedParticlePt_DR3;
  muT_muon_sumPhotonEt_DR3_ = *muT_muon_sumPhotonEt_DR3;
  muT_muon_sumNeutralHadronEt_DR3_ = *muT_muon_sumNeutralHadronEt_DR3;
  muT_muon_sumPUPt_DR3_ = *muT_muon_sumPUPt_DR3;
  muT_muon_relativeIso_DR3_ = *muT_muon_relativeIso_DR3;
  muT_muon_isPFIsolationValid_ = *muT_muon_isPFIsolationValid;
  muT_muon_charge_ = *muT_muon_charge;
  muT_muon_PFpdgId_ = *muT_muon_PFpdgId;
  muT_muon_GENpdgId_ = *muT_muon_GENpdgId;
  muT_muon_normalizedChi2_ = *muT_muon_normalizedChi2;
  muT_muon_numberOfValidMuonHits_ = *muT_muon_numberOfValidMuonHits;
  muT_muon_numberOfMatchedStations_ = *muT_muon_numberOfMatchedStations;
  muT_muon_numberOfValidPixelHits_ = *muT_muon_numberOfValidPixelHits;
  muT_muon_trackerLayersWithMeasurement_ = *muT_muon_trackerLayersWithMeasurement;
  muT_muon_dB_ = *muT_muon_dB;
  muT_muon_dz_ = *muT_muon_dz;
  muT_muon_dxy_ = *muT_muon_dxy;
  muT_muon_passFullId_ = *muT_muon_passFullId;
  muT_muon_has_HltMatchMu17_ = *muT_muon_has_HltMatchMu17;
  muT_muon_has_HltMatchMu18_ = *muT_muon_has_HltMatchMu18;
  muT_muon_has_HltMatchMu24_ = *muT_muon_has_HltMatchMu24;
  muT_muon_isTriLeptonVetoCandidate_ = *muT_muon_isTriLeptonVetoCandidate;
  muT_muon_isTrackerMuon_ = *muT_muon_isTrackerMuon;
  muT_tau_pfJetRefP4_x_ = *muT_tau_pfJetRefP4_x;
  muT_tau_pfJetRefP4_y_ = *muT_tau_pfJetRefP4_y;
  muT_tau_pfJetRefP4_z_ = *muT_tau_pfJetRefP4_z;
  muT_tau_pfJetRefP4_t_ = *muT_tau_pfJetRefP4_t;
  muT_tau_p4_x_ = *muT_tau_p4_x;
  muT_tau_p4_y_ = *muT_tau_p4_y;
  muT_tau_p4_z_ = *muT_tau_p4_z;
  muT_tau_p4_t_ = *muT_tau_p4_t;
  muT_tau_genP4_x_ = *muT_tau_genP4_x;
  muT_tau_genP4_y_ = *muT_tau_genP4_y;
  muT_tau_genP4_z_ = *muT_tau_genP4_z;
  muT_tau_genP4_t_ = *muT_tau_genP4_t;
  muT_tau_genJet_x_ = *muT_tau_genJet_x;
  muT_tau_genJet_y_ = *muT_tau_genJet_y;
  muT_tau_genJet_z_ = *muT_tau_genJet_z;
  muT_tau_genJet_t_ = *muT_tau_genJet_t;
  muT_tau_corrected_p4_x_ = *muT_tau_corrected_p4_x;
  muT_tau_corrected_p4_y_ = *muT_tau_corrected_p4_y;
  muT_tau_corrected_p4_z_ = *muT_tau_corrected_p4_z;
  muT_tau_corrected_p4_t_ = *muT_tau_corrected_p4_t;
  muT_tau_pdgId_ = *muT_tau_pdgId;
  muT_tau_pdgIdGEN_ = *muT_tau_pdgIdGEN;
  muT_tau_charge_ = *muT_tau_charge;
  muT_tau_decayMode_ = *muT_tau_decayMode;
  muT_tau_passFullId_muTau_ = *muT_tau_passFullId_muTau;
  muT_tau_passFullId_eTau_ = *muT_tau_passFullId_eTau;
  muT_tau_numStrips_ = *muT_tau_numStrips;
  muT_tau_numHadrons_ = *muT_tau_numHadrons;
  muT_tau_againstElectronDeadECAL_ = *muT_tau_againstElectronDeadECAL;
  muT_tau_againstElectronLoose_ = *muT_tau_againstElectronLoose;
  muT_tau_againstElectronLooseMVA5_ = *muT_tau_againstElectronLooseMVA5;
  muT_tau_againstElectronMVA5category_ = *muT_tau_againstElectronMVA5category;
  muT_tau_againstElectronMVA5raw_ = *muT_tau_againstElectronMVA5raw;
  muT_tau_againstElectronMedium_ = *muT_tau_againstElectronMedium;
  muT_tau_againstElectronMediumMVA5_ = *muT_tau_againstElectronMediumMVA5;
  muT_tau_againstElectronTight_ = *muT_tau_againstElectronTight;
  muT_tau_againstElectronTightMVA5_ = *muT_tau_againstElectronTightMVA5;
  muT_tau_againstElectronVLooseMVA5_ = *muT_tau_againstElectronVLooseMVA5;
  muT_tau_againstElectronVTightMVA5_ = *muT_tau_againstElectronVTightMVA5;
  muT_tau_againstMuonLoose_ = *muT_tau_againstMuonLoose;
  muT_tau_againstMuonLoose2_ = *muT_tau_againstMuonLoose2;
  muT_tau_againstMuonLoose3_ = *muT_tau_againstMuonLoose3;
  muT_tau_againstMuonLooseMVA_ = *muT_tau_againstMuonLooseMVA;
  muT_tau_againstMuonMVAraw_ = *muT_tau_againstMuonMVAraw;
  muT_tau_againstMuonMedium_ = *muT_tau_againstMuonMedium;
  muT_tau_againstMuonMedium2_ = *muT_tau_againstMuonMedium2;
  muT_tau_againstMuonMediumMVA_ = *muT_tau_againstMuonMediumMVA;
  muT_tau_againstMuonTight_ = *muT_tau_againstMuonTight;
  muT_tau_againstMuonTight2_ = *muT_tau_againstMuonTight2;
  muT_tau_againstMuonTight3_ = *muT_tau_againstMuonTight3;
  muT_tau_againstMuonTightMVA_ = *muT_tau_againstMuonTightMVA;
  muT_tau_byCombinedIsolationDeltaBetaCorrRaw_ = *muT_tau_byCombinedIsolationDeltaBetaCorrRaw;
  muT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits_ = *muT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits;
  muT_tau_byIsolationMVA3newDMwLTraw_ = *muT_tau_byIsolationMVA3newDMwLTraw;
  muT_tau_byIsolationMVA3newDMwoLTraw_ = *muT_tau_byIsolationMVA3newDMwoLTraw;
  muT_tau_byIsolationMVA3oldDMwLTraw_ = *muT_tau_byIsolationMVA3oldDMwLTraw;
  muT_tau_byIsolationMVA3oldDMwoLTraw_ = *muT_tau_byIsolationMVA3oldDMwoLTraw;
  muT_tau_byLooseCombinedIsolationDeltaBetaCorr_ = *muT_tau_byLooseCombinedIsolationDeltaBetaCorr;
  muT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits_ = *muT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits;
  muT_tau_byLooseIsolation_ = *muT_tau_byLooseIsolation;
  muT_tau_byLooseIsolationMVA3newDMwLT_ = *muT_tau_byLooseIsolationMVA3newDMwLT;
  muT_tau_byLooseIsolationMVA3newDMwoLT_ = *muT_tau_byLooseIsolationMVA3newDMwoLT;
  muT_tau_byLooseIsolationMVA3oldDMwLT_ = *muT_tau_byLooseIsolationMVA3oldDMwLT;
  muT_tau_byLooseIsolationMVA3oldDMwoLT_ = *muT_tau_byLooseIsolationMVA3oldDMwoLT;
  muT_tau_byMediumCombinedIsolationDeltaBetaCorr_ = *muT_tau_byMediumCombinedIsolationDeltaBetaCorr;
  muT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits_ = *muT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits;
  muT_tau_byMediumIsolationMVA3newDMwLT_ = *muT_tau_byMediumIsolationMVA3newDMwLT;
  muT_tau_byMediumIsolationMVA3newDMwoLT_ = *muT_tau_byMediumIsolationMVA3newDMwoLT;
  muT_tau_byMediumIsolationMVA3oldDMwLT_ = *muT_tau_byMediumIsolationMVA3oldDMwLT;
  muT_tau_byMediumIsolationMVA3oldDMwoLT_ = *muT_tau_byMediumIsolationMVA3oldDMwoLT;
  muT_tau_byTightCombinedIsolationDeltaBetaCorr_ = *muT_tau_byTightCombinedIsolationDeltaBetaCorr;
  muT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits_ = *muT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits;
  muT_tau_byTightIsolationMVA3newDMwLT_ = *muT_tau_byTightIsolationMVA3newDMwLT;
  muT_tau_byTightIsolationMVA3newDMwoLT_ = *muT_tau_byTightIsolationMVA3newDMwoLT;
  muT_tau_byTightIsolationMVA3oldDMwLT_ = *muT_tau_byTightIsolationMVA3oldDMwLT;
  muT_tau_byTightIsolationMVA3oldDMwoLT_ = *muT_tau_byTightIsolationMVA3oldDMwoLT;
  muT_tau_byVLooseCombinedIsolationDeltaBetaCorr_ = *muT_tau_byVLooseCombinedIsolationDeltaBetaCorr;
  muT_tau_byVLooseIsolationMVA3newDMwLT_ = *muT_tau_byVLooseIsolationMVA3newDMwLT;
  muT_tau_byVLooseIsolationMVA3newDMwoLT_ = *muT_tau_byVLooseIsolationMVA3newDMwoLT;
  muT_tau_byVLooseIsolationMVA3oldDMwLT_ = *muT_tau_byVLooseIsolationMVA3oldDMwLT;
  muT_tau_byVLooseIsolationMVA3oldDMwoLT_ = *muT_tau_byVLooseIsolationMVA3oldDMwoLT;
  muT_tau_byVTightIsolationMVA3newDMwLT_ = *muT_tau_byVTightIsolationMVA3newDMwLT;
  muT_tau_byVTightIsolationMVA3newDMwoLT_ = *muT_tau_byVTightIsolationMVA3newDMwoLT;
  muT_tau_byVTightIsolationMVA3oldDMwLT_ = *muT_tau_byVTightIsolationMVA3oldDMwLT;
  muT_tau_byVTightIsolationMVA3oldDMwoLT_ = *muT_tau_byVTightIsolationMVA3oldDMwoLT;
  muT_tau_byVVTightIsolationMVA3newDMwLT_ = *muT_tau_byVVTightIsolationMVA3newDMwLT;
  muT_tau_byVVTightIsolationMVA3newDMwoLT_ = *muT_tau_byVVTightIsolationMVA3newDMwoLT;
  muT_tau_byVVTightIsolationMVA3oldDMwLT_ = *muT_tau_byVVTightIsolationMVA3oldDMwLT;
  muT_tau_byVVTightIsolationMVA3oldDMwoLT_ = *muT_tau_byVVTightIsolationMVA3oldDMwoLT;
  muT_tau_chargedIsoPtSum_ = *muT_tau_chargedIsoPtSum;
  muT_tau_decayModeFinding_ = *muT_tau_decayModeFinding;
  muT_tau_decayModeFindingNewDMs_ = *muT_tau_decayModeFindingNewDMs;
  muT_tau_decayModeFindingOldDMs_ = *muT_tau_decayModeFindingOldDMs;
  muT_tau_neutralIsoPtSum_ = *muT_tau_neutralIsoPtSum;
  muT_tau_puCorrPtSum_ = *muT_tau_puCorrPtSum;
  muT_tau_has_HltMatchEle20_ = *muT_tau_has_HltMatchEle20;
  muT_tau_has_HltMatchEle22_ = *muT_tau_has_HltMatchEle22;
  muT_tau_has_HltMatchEle27_ = *muT_tau_has_HltMatchEle27;
  muT_tau_has_HltMatchMu17_ = *muT_tau_has_HltMatchMu17;
  muT_tau_has_HltMatchMu18_ = *muT_tau_has_HltMatchMu18;
  muT_tau_has_HltMatchMu24_ = *muT_tau_has_HltMatchMu24;
  muT_puWeight_ = *muT_puWeight;
  muT_puWeightM1_ = *muT_puWeightM1;
  muT_puWeightP1_ = *muT_puWeightP1;
  muT_NumPileupInt_ = *muT_NumPileupInt;
  muT_NumTruePileUpInt_ = *muT_NumTruePileUpInt;
  muT_NumPileupIntM1_ = *muT_NumPileupIntM1;
  muT_NumTruePileUpIntM1_ = *muT_NumTruePileUpIntM1;
  muT_NumPileupIntP1_ = *muT_NumPileupIntP1;
  muT_NumTruePileUpIntP1_ = *muT_NumTruePileUpIntP1;
  muT_EffDataISOMU17andISOMU18_ = *muT_EffDataISOMU17andISOMU18;
  muT_EffMcISOMU17andISOMU18_ = *muT_EffMcISOMU17andISOMU18;
  muT_HadronicTauDataTrigEffAntiMuMed_ = *muT_HadronicTauDataTrigEffAntiMuMed;
  muT_HadronicTauMcTrigEffAntiMuMed_ = *muT_HadronicTauMcTrigEffAntiMuMed;
  muT_muonDataIDweight_ = *muT_muonDataIDweight;
  muT_muonMcIDweight_ = *muT_muonMcIDweight;
  muT_muonDataISOLweight_ = *muT_muonDataISOLweight;
  muT_muonMcISOLweight_ = *muT_muonMcISOLweight;
  muT_EffDataHighPtTauTrigger_ = *muT_EffDataHighPtTauTrigger;
  muT_EffMcHighPtTauTrigger_ = *muT_EffMcHighPtTauTrigger;
  muT_TauFakeCorrection_ = *muT_TauFakeCorrection;
  muT_DecayModeCorrectionFactor_ = *muT_DecayModeCorrectionFactor;
  muT_nominalHIGLUXHQTmhmax_ = *muT_nominalHIGLUXHQTmhmax;
  muT_upHIGLUXHQTmhmax_ = *muT_upHIGLUXHQTmhmax;
  muT_downHIGLUXHQTmhmax_ = *muT_downHIGLUXHQTmhmax;
  muT_nominalPOWHEGmhmod_ = *muT_nominalPOWHEGmhmod;
  muT_upPOWHEGmhmod_ = *muT_upPOWHEGmhmod;
  muT_downPOWHEGmhmod_ = *muT_downPOWHEGmhmod;
  muT_upPOWHEGscale_ = *muT_upPOWHEGscale;
  muT_downPOWHEGscale_ = *muT_downPOWHEGscale;
  muT_etaDepQCDShapeTemplateCorrection_ = *muT_etaDepQCDShapeTemplateCorrection;
  muT_inclusiveQCDShapeTemplateCorrection_ = *muT_inclusiveQCDShapeTemplateCorrection;
  muT_TTbarPtWeight_ = *muT_TTbarPtWeight;
  muT_TauSpinnerWT_ = *muT_TauSpinnerWT;
  muT_TauSpinnerWTFlip_ = *muT_TauSpinnerWTFlip;
  muT_TauSpinnerWThminus_ = *muT_TauSpinnerWThminus;
  muT_TauSpinnerWThplus_ = *muT_TauSpinnerWThplus;
  muT_hepNUP_ = *muT_hepNUP;
  muT_weightHEPNUP_DYJets_ = *muT_weightHEPNUP_DYJets;
  muT_weightHEPNUP_WJets_ = *muT_weightHEPNUP_WJets;
  muT_passesSecondLeptonVeto_ = *muT_passesSecondLeptonVeto;
  muT_passesThirdLeptonVeto_ = *muT_passesThirdLeptonVeto;


}

void Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   NAMEVAR = 0;
   SampleName = 0;
   PhysicsProcess = 0;
   eT_p4_x = 0;
   eT_p4_y = 0;
   eT_p4_z = 0;
   eT_p4_t = 0;
   eT_corrected_p4_x = 0;
   eT_corrected_p4_y = 0;
   eT_corrected_p4_z = 0;
   eT_corrected_p4_t = 0;
   eT_electronIndex = 0;
   eT_tauIndex = 0;
   eT_scalarSumPt = 0;
   eT_DR = 0;
   eT_sumCharge = 0;
   eT_correctedSVFitMass = 0;
   eT_rawSVFitMass = 0;
   eT_TransverseMass = 0;
   eT_rawTransverseMass = 0;
   eT_mvaMETraw = 0;
   eT_mvaMET = 0;
   eT_mvaMETphiRaw = 0;
   eT_mvaMETphi = 0;
   eT_MAX = 0;
   eT_isGoodTriggerPair = 0;
   eT_njets = 0;
   eT_nbjets = 0;
   eT_nbjetsLOOSE = 0;
   eT_nbjetsLOOSEUP = 0;
   eT_nbjetsLOOSEDOWN = 0;
   eT_njetsUP = 0;
   eT_nbjetsUP = 0;
   eT_njetsDOWN = 0;
   eT_nbjetsDOWN = 0;
   eT_jet1P4_x = 0;
   eT_jet1P4_y = 0;
   eT_jet1P4_z = 0;
   eT_jet1P4_t = 0;
   eT_jet1RawP4_x = 0;
   eT_jet1RawP4_y = 0;
   eT_jet1RawP4_z = 0;
   eT_jet1RawP4_t = 0;
   eT_jet1IDMVA = 0;
   eT_jet1BTAGMVA = 0;
   eT_jet2P4_x = 0;
   eT_jet2P4_y = 0;
   eT_jet2P4_z = 0;
   eT_jet2P4_t = 0;
   eT_jet2RawP4_x = 0;
   eT_jet2RawP4_y = 0;
   eT_jet2RawP4_z = 0;
   eT_jet2RawP4_t = 0;
   eT_jet2IDMVA = 0;
   eT_jet2BTAGMVA = 0;
   eT_cov00 = 0;
   eT_cov01 = 0;
   eT_cov10 = 0;
   eT_cov11 = 0;
   eT_passesTriLeptonVeto = 0;
   eT_passNonTopEmbeddedTriggerAndMass50 = 0;
   eT_passSignalGeneratorMass70to130Cut = 0;
   eT_genBosonP4_x = 0;
   eT_genBosonP4_y = 0;
   eT_genBosonP4_z = 0;
   eT_genBosonP4_t = 0;
   eT_genTOPp4_x = 0;
   eT_genTOPp4_y = 0;
   eT_genTOPp4_z = 0;
   eT_genTOPp4_t = 0;
   eT_genTOPBARp4_x = 0;
   eT_genTOPBARp4_y = 0;
   eT_genTOPBARp4_z = 0;
   eT_genTOPBARp4_t = 0;
   eT_numberOfGoodVertices = 0;
   eT_PVndof = 0;
   eT_PVz = 0;
   eT_PVpositionRho = 0;
   eT_PVp4_x = 0;
   eT_PVp4_y = 0;
   eT_PVp4_z = 0;
   eT_PVp4_t = 0;
   eT_isDecayZtauTau = 0;
   eT_isDecayZeE = 0;
   eT_isDecayZmuMu = 0;
   eT_isRecoLep_matchedTo_GenTauFromZ = 0;
   eT_isRecoTau_matchedTo_GenTauFromZ = 0;
   eT_isRecoLep_matchedTo_GenElecFromZ = 0;
   eT_isRecoTau_matchedTo_GenElecFromZ = 0;
   eT_isRecoLep_matchedTo_GenMuonFromZ = 0;
   eT_isRecoTau_matchedTo_GenMuonFromZ = 0;
   eT_isRecoLep_matchedTo_GenElecFromTau = 0;
   eT_isRecoTau_matchedTo_GenElecFromTau = 0;
   eT_isRecoLep_matchedTo_GenMuonFromTau = 0;
   eT_isRecoTau_matchedTo_GenMuonFromTau = 0;
   eT_passEmbeddedTrigger = 0;
   eT_ele_p4_x = 0;
   eT_ele_p4_y = 0;
   eT_ele_p4_z = 0;
   eT_ele_p4_t = 0;
   eT_ele_genP4_x = 0;
   eT_ele_genP4_y = 0;
   eT_ele_genP4_z = 0;
   eT_ele_genP4_t = 0;
   eT_ele_pfP4_x = 0;
   eT_ele_pfP4_y = 0;
   eT_ele_pfP4_z = 0;
   eT_ele_pfP4_t = 0;
   eT_ele_charge = 0;
   eT_ele_PFpdgId = 0;
   eT_ele_GENpdgId = 0;
   eT_ele_numberOfMissingInnerHits = 0;
   eT_ele_passConversionVeto = 0;
   eT_ele_dz = 0;
   eT_ele_dB = 0;
   eT_ele_dxy = 0;
   eT_ele_SuperClusterEta = 0;
   eT_ele_mvaTrigV0 = 0;
   eT_ele_mvaTrigNoIPV0 = 0;
   eT_ele_mvaNonTrigV0 = 0;
   eT_ele_pass_tight_mvaNonTrigV0 = 0;
   eT_ele_passFullId = 0;
   eT_ele_chargedHadronIso = 0;
   eT_ele_photonIso = 0;
   eT_ele_neutralHadronIso = 0;
   eT_ele_puChargedHadronIso = 0;
   eT_ele_relativeIso = 0;
   eT_ele_isEB = 0;
   eT_ele_isEE = 0;
   eT_ele_isEBEEGap = 0;
   eT_ele_isEBEtaGap = 0;
   eT_ele_isEBPhiGap = 0;
   eT_ele_isEEDeeGap = 0;
   eT_ele_isEERingGap = 0;
   eT_ele_sigmaEtaEta = 0;
   eT_ele_sigmaIetaIeta = 0;
   eT_ele_sigmaIphiIphi = 0;
   eT_ele_has_HltMatchEle20 = 0;
   eT_ele_has_HltMatchEle22 = 0;
   eT_ele_has_HltMatchEle27 = 0;
   eT_ele_isTriLeptonVetoCandidate = 0;
   eT_ele_deltaPhiSuperClusterTrackAtVtx = 0;
   eT_ele_deltaEtaSuperClusterTrackAtVtx = 0;
   eT_ele_hadronicOverEm = 0;
   eT_tau_pfJetRefP4_x = 0;
   eT_tau_pfJetRefP4_y = 0;
   eT_tau_pfJetRefP4_z = 0;
   eT_tau_pfJetRefP4_t = 0;
   eT_tau_p4_x = 0;
   eT_tau_p4_y = 0;
   eT_tau_p4_z = 0;
   eT_tau_p4_t = 0;
   eT_tau_genP4_x = 0;
   eT_tau_genP4_y = 0;
   eT_tau_genP4_z = 0;
   eT_tau_genP4_t = 0;
   eT_tau_genJet_x = 0;
   eT_tau_genJet_y = 0;
   eT_tau_genJet_z = 0;
   eT_tau_genJet_t = 0;
   eT_tau_corrected_p4_x = 0;
   eT_tau_corrected_p4_y = 0;
   eT_tau_corrected_p4_z = 0;
   eT_tau_corrected_p4_t = 0;
   eT_tau_pdgId = 0;
   eT_tau_pdgIdGEN = 0;
   eT_tau_charge = 0;
   eT_tau_decayMode = 0;
   eT_tau_passFullId_muTau = 0;
   eT_tau_passFullId_eTau = 0;
   eT_tau_numStrips = 0;
   eT_tau_numHadrons = 0;
   eT_tau_againstElectronDeadECAL = 0;
   eT_tau_againstElectronLoose = 0;
   eT_tau_againstElectronLooseMVA5 = 0;
   eT_tau_againstElectronMVA5category = 0;
   eT_tau_againstElectronMVA5raw = 0;
   eT_tau_againstElectronMedium = 0;
   eT_tau_againstElectronMediumMVA5 = 0;
   eT_tau_againstElectronTight = 0;
   eT_tau_againstElectronTightMVA5 = 0;
   eT_tau_againstElectronVLooseMVA5 = 0;
   eT_tau_againstElectronVTightMVA5 = 0;
   eT_tau_againstMuonLoose = 0;
   eT_tau_againstMuonLoose2 = 0;
   eT_tau_againstMuonLoose3 = 0;
   eT_tau_againstMuonLooseMVA = 0;
   eT_tau_againstMuonMVAraw = 0;
   eT_tau_againstMuonMedium = 0;
   eT_tau_againstMuonMedium2 = 0;
   eT_tau_againstMuonMediumMVA = 0;
   eT_tau_againstMuonTight = 0;
   eT_tau_againstMuonTight2 = 0;
   eT_tau_againstMuonTight3 = 0;
   eT_tau_againstMuonTightMVA = 0;
   eT_tau_byCombinedIsolationDeltaBetaCorrRaw = 0;
   eT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits = 0;
   eT_tau_byIsolationMVA3newDMwLTraw = 0;
   eT_tau_byIsolationMVA3newDMwoLTraw = 0;
   eT_tau_byIsolationMVA3oldDMwLTraw = 0;
   eT_tau_byIsolationMVA3oldDMwoLTraw = 0;
   eT_tau_byLooseCombinedIsolationDeltaBetaCorr = 0;
   eT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits = 0;
   eT_tau_byLooseIsolation = 0;
   eT_tau_byLooseIsolationMVA3newDMwLT = 0;
   eT_tau_byLooseIsolationMVA3newDMwoLT = 0;
   eT_tau_byLooseIsolationMVA3oldDMwLT = 0;
   eT_tau_byLooseIsolationMVA3oldDMwoLT = 0;
   eT_tau_byMediumCombinedIsolationDeltaBetaCorr = 0;
   eT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits = 0;
   eT_tau_byMediumIsolationMVA3newDMwLT = 0;
   eT_tau_byMediumIsolationMVA3newDMwoLT = 0;
   eT_tau_byMediumIsolationMVA3oldDMwLT = 0;
   eT_tau_byMediumIsolationMVA3oldDMwoLT = 0;
   eT_tau_byTightCombinedIsolationDeltaBetaCorr = 0;
   eT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits = 0;
   eT_tau_byTightIsolationMVA3newDMwLT = 0;
   eT_tau_byTightIsolationMVA3newDMwoLT = 0;
   eT_tau_byTightIsolationMVA3oldDMwLT = 0;
   eT_tau_byTightIsolationMVA3oldDMwoLT = 0;
   eT_tau_byVLooseCombinedIsolationDeltaBetaCorr = 0;
   eT_tau_byVLooseIsolationMVA3newDMwLT = 0;
   eT_tau_byVLooseIsolationMVA3newDMwoLT = 0;
   eT_tau_byVLooseIsolationMVA3oldDMwLT = 0;
   eT_tau_byVLooseIsolationMVA3oldDMwoLT = 0;
   eT_tau_byVTightIsolationMVA3newDMwLT = 0;
   eT_tau_byVTightIsolationMVA3newDMwoLT = 0;
   eT_tau_byVTightIsolationMVA3oldDMwLT = 0;
   eT_tau_byVTightIsolationMVA3oldDMwoLT = 0;
   eT_tau_byVVTightIsolationMVA3newDMwLT = 0;
   eT_tau_byVVTightIsolationMVA3newDMwoLT = 0;
   eT_tau_byVVTightIsolationMVA3oldDMwLT = 0;
   eT_tau_byVVTightIsolationMVA3oldDMwoLT = 0;
   eT_tau_chargedIsoPtSum = 0;
   eT_tau_decayModeFinding = 0;
   eT_tau_decayModeFindingNewDMs = 0;
   eT_tau_decayModeFindingOldDMs = 0;
   eT_tau_neutralIsoPtSum = 0;
   eT_tau_puCorrPtSum = 0;
   eT_tau_has_HltMatchEle20 = 0;
   eT_tau_has_HltMatchEle22 = 0;
   eT_tau_has_HltMatchEle27 = 0;
   eT_tau_has_HltMatchMu17 = 0;
   eT_tau_has_HltMatchMu18 = 0;
   eT_tau_has_HltMatchMu24 = 0;
   eT_puWeight = 0;
   eT_puWeightM1 = 0;
   eT_puWeightP1 = 0;
   eT_NumPileupInt = 0;
   eT_NumTruePileUpInt = 0;
   eT_NumPileupIntM1 = 0;
   eT_NumTruePileUpIntM1 = 0;
   eT_NumPileupIntP1 = 0;
   eT_NumTruePileUpIntP1 = 0;
   eT_EffDataELE20andELE22 = 0;
   eT_EffMcELE20andELE22 = 0;
   eT_HadronicTauDataTrigEffAntiEMed = 0;
   eT_HadronicTauMcTrigEffAntiEMed = 0;
   eT_HadronicTauDataTrigEffAntiETight = 0;
   eT_HadronicTauMcTrigEffAntiETight = 0;
   eT_electronDataIDweight = 0;
   eT_electronMcIDweight = 0;
   eT_electronDataISOLweight = 0;
   eT_electronMcISOLweight = 0;
   eT_EffDataHighPtTauTrigger = 0;
   eT_EffMcHighPtTauTrigger = 0;
   eT_TauFakeCorrection = 0;
   eT_DecayModeCorrectionFactor = 0;
   eT_ZeeScaleFactor = 0;
   eT_nominalHIGLUXHQTmhmax = 0;
   eT_upHIGLUXHQTmhmax = 0;
   eT_downHIGLUXHQTmhmax = 0;
   eT_nominalPOWHEGmhmod = 0;
   eT_upPOWHEGmhmod = 0;
   eT_downPOWHEGmhmod = 0;
   eT_upPOWHEGscale = 0;
   eT_downPOWHEGscale = 0;
   eT_etaDepQCDShapeTemplateCorrection = 0;
   eT_inclusiveQCDShapeTemplateCorrection = 0;
   eT_TTbarPtWeight = 0;
   eT_TauSpinnerWT = 0;
   eT_TauSpinnerWTFlip = 0;
   eT_TauSpinnerWThminus = 0;
   eT_TauSpinnerWThplus = 0;
   eT_hepNUP = 0;
   eT_weightHEPNUP_DYJets = 0;
   eT_weightHEPNUP_WJets = 0;
   eT_passesSecondLeptonVeto = 0;
   eT_passesThirdLeptonVeto = 0;
   muT_p4_x = 0;
   muT_p4_y = 0;
   muT_p4_z = 0;
   muT_p4_t = 0;
   muT_corrected_p4_x = 0;
   muT_corrected_p4_y = 0;
   muT_corrected_p4_z = 0;
   muT_corrected_p4_t = 0;
   muT_muonIndex = 0;
   muT_tauIndex = 0;
   muT_scalarSumPt = 0;
   muT_DR = 0;
   muT_sumCharge = 0;
   muT_correctedSVFitMass = 0;
   muT_rawSVFitMass = 0;
   muT_TransverseMass = 0;
   muT_rawTransverseMass = 0;
   muT_mvaMETraw = 0;
   muT_mvaMET = 0;
   muT_mvaMETphiRaw = 0;
   muT_mvaMETphi = 0;
   muT_MAX = 0;
   muT_isGoodTriggerPair = 0;
   muT_njets = 0;
   muT_nbjets = 0;
   muT_nbjetsLOOSE = 0;
   muT_nbjetsLOOSEUP = 0;
   muT_nbjetsLOOSEDOWN = 0;
   muT_njetsUP = 0;
   muT_nbjetsUP = 0;
   muT_njetsDOWN = 0;
   muT_nbjetsDOWN = 0;
   muT_jet1P4_x = 0;
   muT_jet1P4_y = 0;
   muT_jet1P4_z = 0;
   muT_jet1P4_t = 0;
   muT_jet1RawP4_x = 0;
   muT_jet1RawP4_y = 0;
   muT_jet1RawP4_z = 0;
   muT_jet1RawP4_t = 0;
   muT_jet1IDMVA = 0;
   muT_jet1BTAGMVA = 0;
   muT_jet2P4_x = 0;
   muT_jet2P4_y = 0;
   muT_jet2P4_z = 0;
   muT_jet2P4_t = 0;
   muT_jet2RawP4_x = 0;
   muT_jet2RawP4_y = 0;
   muT_jet2RawP4_z = 0;
   muT_jet2RawP4_t = 0;
   muT_jet2IDMVA = 0;
   muT_jet2BTAGMVA = 0;
   muT_cov00 = 0;
   muT_cov01 = 0;
   muT_cov10 = 0;
   muT_cov11 = 0;
   muT_passesTriLeptonVeto = 0;
   muT_passNonTopEmbeddedTriggerAndMass50 = 0;
   muT_passSignalGeneratorMass70to130Cut = 0;
   muT_genBosonP4_x = 0;
   muT_genBosonP4_y = 0;
   muT_genBosonP4_z = 0;
   muT_genBosonP4_t = 0;
   muT_genTOPp4_x = 0;
   muT_genTOPp4_y = 0;
   muT_genTOPp4_z = 0;
   muT_genTOPp4_t = 0;
   muT_genTOPBARp4_x = 0;
   muT_genTOPBARp4_y = 0;
   muT_genTOPBARp4_z = 0;
   muT_genTOPBARp4_t = 0;
   muT_numberOfGoodVertices = 0;
   muT_PVndof = 0;
   muT_PVz = 0;
   muT_PVpositionRho = 0;
   muT_PVp4_x = 0;
   muT_PVp4_y = 0;
   muT_PVp4_z = 0;
   muT_PVp4_t = 0;
   muT_isDecayZtauTau = 0;
   muT_isDecayZeE = 0;
   muT_isDecayZmuMu = 0;
   muT_isRecoLep_matchedTo_GenTauFromZ = 0;
   muT_isRecoTau_matchedTo_GenTauFromZ = 0;
   muT_isRecoLep_matchedTo_GenElecFromZ = 0;
   muT_isRecoTau_matchedTo_GenElecFromZ = 0;
   muT_isRecoLep_matchedTo_GenMuonFromZ = 0;
   muT_isRecoTau_matchedTo_GenMuonFromZ = 0;
   muT_isRecoLep_matchedTo_GenElecFromTau = 0;
   muT_isRecoTau_matchedTo_GenElecFromTau = 0;
   muT_isRecoLep_matchedTo_GenMuonFromTau = 0;
   muT_isRecoTau_matchedTo_GenMuonFromTau = 0;
   muT_passEmbeddedTrigger = 0;
   muT_muon_p4_x = 0;
   muT_muon_p4_y = 0;
   muT_muon_p4_z = 0;
   muT_muon_p4_t = 0;
   muT_muon_pfP4_x = 0;
   muT_muon_pfP4_y = 0;
   muT_muon_pfP4_z = 0;
   muT_muon_pfP4_t = 0;
   muT_muon_genP4_x = 0;
   muT_muon_genP4_y = 0;
   muT_muon_genP4_z = 0;
   muT_muon_genP4_t = 0;
   muT_muon_isGlobalMuon = 0;
   muT_muon_isTightMuon = 0;
   muT_muon_isPFMuon = 0;
   muT_muon_isLooseMuon = 0;
   muT_muon_sumChargedParticlePt_DR4 = 0;
   muT_muon_sumPhotonEt_DR4 = 0;
   muT_muon_sumNeutralHadronEt_DR4 = 0;
   muT_muon_sumPUPt_DR4 = 0;
   muT_muon_relativeIso_DR4 = 0;
   muT_muon_sumChargedParticlePt_DR3 = 0;
   muT_muon_sumPhotonEt_DR3 = 0;
   muT_muon_sumNeutralHadronEt_DR3 = 0;
   muT_muon_sumPUPt_DR3 = 0;
   muT_muon_relativeIso_DR3 = 0;
   muT_muon_isPFIsolationValid = 0;
   muT_muon_charge = 0;
   muT_muon_PFpdgId = 0;
   muT_muon_GENpdgId = 0;
   muT_muon_normalizedChi2 = 0;
   muT_muon_numberOfValidMuonHits = 0;
   muT_muon_numberOfMatchedStations = 0;
   muT_muon_numberOfValidPixelHits = 0;
   muT_muon_trackerLayersWithMeasurement = 0;
   muT_muon_dB = 0;
   muT_muon_dz = 0;
   muT_muon_dxy = 0;
   muT_muon_passFullId = 0;
   muT_muon_has_HltMatchMu17 = 0;
   muT_muon_has_HltMatchMu18 = 0;
   muT_muon_has_HltMatchMu24 = 0;
   muT_muon_isTriLeptonVetoCandidate = 0;
   muT_muon_isTrackerMuon = 0;
   muT_tau_pfJetRefP4_x = 0;
   muT_tau_pfJetRefP4_y = 0;
   muT_tau_pfJetRefP4_z = 0;
   muT_tau_pfJetRefP4_t = 0;
   muT_tau_p4_x = 0;
   muT_tau_p4_y = 0;
   muT_tau_p4_z = 0;
   muT_tau_p4_t = 0;
   muT_tau_genP4_x = 0;
   muT_tau_genP4_y = 0;
   muT_tau_genP4_z = 0;
   muT_tau_genP4_t = 0;
   muT_tau_genJet_x = 0;
   muT_tau_genJet_y = 0;
   muT_tau_genJet_z = 0;
   muT_tau_genJet_t = 0;
   muT_tau_corrected_p4_x = 0;
   muT_tau_corrected_p4_y = 0;
   muT_tau_corrected_p4_z = 0;
   muT_tau_corrected_p4_t = 0;
   muT_tau_pdgId = 0;
   muT_tau_pdgIdGEN = 0;
   muT_tau_charge = 0;
   muT_tau_decayMode = 0;
   muT_tau_passFullId_muTau = 0;
   muT_tau_passFullId_eTau = 0;
   muT_tau_numStrips = 0;
   muT_tau_numHadrons = 0;
   muT_tau_againstElectronDeadECAL = 0;
   muT_tau_againstElectronLoose = 0;
   muT_tau_againstElectronLooseMVA5 = 0;
   muT_tau_againstElectronMVA5category = 0;
   muT_tau_againstElectronMVA5raw = 0;
   muT_tau_againstElectronMedium = 0;
   muT_tau_againstElectronMediumMVA5 = 0;
   muT_tau_againstElectronTight = 0;
   muT_tau_againstElectronTightMVA5 = 0;
   muT_tau_againstElectronVLooseMVA5 = 0;
   muT_tau_againstElectronVTightMVA5 = 0;
   muT_tau_againstMuonLoose = 0;
   muT_tau_againstMuonLoose2 = 0;
   muT_tau_againstMuonLoose3 = 0;
   muT_tau_againstMuonLooseMVA = 0;
   muT_tau_againstMuonMVAraw = 0;
   muT_tau_againstMuonMedium = 0;
   muT_tau_againstMuonMedium2 = 0;
   muT_tau_againstMuonMediumMVA = 0;
   muT_tau_againstMuonTight = 0;
   muT_tau_againstMuonTight2 = 0;
   muT_tau_againstMuonTight3 = 0;
   muT_tau_againstMuonTightMVA = 0;
   muT_tau_byCombinedIsolationDeltaBetaCorrRaw = 0;
   muT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits = 0;
   muT_tau_byIsolationMVA3newDMwLTraw = 0;
   muT_tau_byIsolationMVA3newDMwoLTraw = 0;
   muT_tau_byIsolationMVA3oldDMwLTraw = 0;
   muT_tau_byIsolationMVA3oldDMwoLTraw = 0;
   muT_tau_byLooseCombinedIsolationDeltaBetaCorr = 0;
   muT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits = 0;
   muT_tau_byLooseIsolation = 0;
   muT_tau_byLooseIsolationMVA3newDMwLT = 0;
   muT_tau_byLooseIsolationMVA3newDMwoLT = 0;
   muT_tau_byLooseIsolationMVA3oldDMwLT = 0;
   muT_tau_byLooseIsolationMVA3oldDMwoLT = 0;
   muT_tau_byMediumCombinedIsolationDeltaBetaCorr = 0;
   muT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits = 0;
   muT_tau_byMediumIsolationMVA3newDMwLT = 0;
   muT_tau_byMediumIsolationMVA3newDMwoLT = 0;
   muT_tau_byMediumIsolationMVA3oldDMwLT = 0;
   muT_tau_byMediumIsolationMVA3oldDMwoLT = 0;
   muT_tau_byTightCombinedIsolationDeltaBetaCorr = 0;
   muT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits = 0;
   muT_tau_byTightIsolationMVA3newDMwLT = 0;
   muT_tau_byTightIsolationMVA3newDMwoLT = 0;
   muT_tau_byTightIsolationMVA3oldDMwLT = 0;
   muT_tau_byTightIsolationMVA3oldDMwoLT = 0;
   muT_tau_byVLooseCombinedIsolationDeltaBetaCorr = 0;
   muT_tau_byVLooseIsolationMVA3newDMwLT = 0;
   muT_tau_byVLooseIsolationMVA3newDMwoLT = 0;
   muT_tau_byVLooseIsolationMVA3oldDMwLT = 0;
   muT_tau_byVLooseIsolationMVA3oldDMwoLT = 0;
   muT_tau_byVTightIsolationMVA3newDMwLT = 0;
   muT_tau_byVTightIsolationMVA3newDMwoLT = 0;
   muT_tau_byVTightIsolationMVA3oldDMwLT = 0;
   muT_tau_byVTightIsolationMVA3oldDMwoLT = 0;
   muT_tau_byVVTightIsolationMVA3newDMwLT = 0;
   muT_tau_byVVTightIsolationMVA3newDMwoLT = 0;
   muT_tau_byVVTightIsolationMVA3oldDMwLT = 0;
   muT_tau_byVVTightIsolationMVA3oldDMwoLT = 0;
   muT_tau_chargedIsoPtSum = 0;
   muT_tau_decayModeFinding = 0;
   muT_tau_decayModeFindingNewDMs = 0;
   muT_tau_decayModeFindingOldDMs = 0;
   muT_tau_neutralIsoPtSum = 0;
   muT_tau_puCorrPtSum = 0;
   muT_tau_has_HltMatchEle20 = 0;
   muT_tau_has_HltMatchEle22 = 0;
   muT_tau_has_HltMatchEle27 = 0;
   muT_tau_has_HltMatchMu17 = 0;
   muT_tau_has_HltMatchMu18 = 0;
   muT_tau_has_HltMatchMu24 = 0;
   muT_puWeight = 0;
   muT_puWeightM1 = 0;
   muT_puWeightP1 = 0;
   muT_NumPileupInt = 0;
   muT_NumTruePileUpInt = 0;
   muT_NumPileupIntM1 = 0;
   muT_NumTruePileUpIntM1 = 0;
   muT_NumPileupIntP1 = 0;
   muT_NumTruePileUpIntP1 = 0;
   muT_EffDataISOMU17andISOMU18 = 0;
   muT_EffMcISOMU17andISOMU18 = 0;
   muT_HadronicTauDataTrigEffAntiMuMed = 0;
   muT_HadronicTauMcTrigEffAntiMuMed = 0;
   muT_muonDataIDweight = 0;
   muT_muonMcIDweight = 0;
   muT_muonDataISOLweight = 0;
   muT_muonMcISOLweight = 0;
   muT_EffDataHighPtTauTrigger = 0;
   muT_EffMcHighPtTauTrigger = 0;
   muT_TauFakeCorrection = 0;
   muT_DecayModeCorrectionFactor = 0;
   muT_nominalHIGLUXHQTmhmax = 0;
   muT_upHIGLUXHQTmhmax = 0;
   muT_downHIGLUXHQTmhmax = 0;
   muT_nominalPOWHEGmhmod = 0;
   muT_upPOWHEGmhmod = 0;
   muT_downPOWHEGmhmod = 0;
   muT_upPOWHEGscale = 0;
   muT_downPOWHEGscale = 0;
   muT_etaDepQCDShapeTemplateCorrection = 0;
   muT_inclusiveQCDShapeTemplateCorrection = 0;
   muT_TTbarPtWeight = 0;
   muT_TauSpinnerWT = 0;
   muT_TauSpinnerWTFlip = 0;
   muT_TauSpinnerWThminus = 0;
   muT_TauSpinnerWThplus = 0;
   muT_hepNUP = 0;
   muT_weightHEPNUP_DYJets = 0;
   muT_weightHEPNUP_WJets = 0;
   muT_passesSecondLeptonVeto = 0;
   muT_passesThirdLeptonVeto = 0;
   eT_embedWeight = 0;
   muT_embedWeight = 0;





   fChain = tree;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("run", &run, &b_run);
   fChain->SetBranchAddress("luminosityBlock", &luminosityBlock, &b_luminosityBlock);
   fChain->SetBranchAddress("event", &event, &b_event);
   fChain->SetBranchAddress("isRealData", &isRealData, &b_isRealData);
   fChain->SetBranchAddress("bunchCrossing", &bunchCrossing, &b_bunchCrossing);
   fChain->SetBranchAddress("orbitNumber", &orbitNumber, &b_orbitNumber);
   fChain->SetBranchAddress("NAMEVAR", &NAMEVAR, &b_NAMEVAR);
   fChain->SetBranchAddress("SampleName", &SampleName, &b_SampleName);
   fChain->SetBranchAddress("PhysicsProcess", &PhysicsProcess, &b_PhysicsProcess);
   fChain->SetBranchAddress("isNonTopEmbeddedSample", &isNonTopEmbeddedSample, &b_isNonTopEmbeddedSample);
   fChain->SetBranchAddress("isTopEmbeddedSample", &isTopEmbeddedSample, &b_isTopEmbeddedSample);
   fChain->SetBranchAddress("MASS", &MASS, &b_MASS);
   fChain->SetBranchAddress("crossSection", &crossSection, &b_crossSection);
   fChain->SetBranchAddress("branchingFraction", &branchingFraction, &b_branchingFraction);
   fChain->SetBranchAddress("numberEvents", &numberEvents, &b_numberEvents);
   fChain->SetBranchAddress("eT_p4_x", &eT_p4_x, &b_eT_p4_x);
   fChain->SetBranchAddress("eT_p4_y", &eT_p4_y, &b_eT_p4_y);
   fChain->SetBranchAddress("eT_p4_z", &eT_p4_z, &b_eT_p4_z);
   fChain->SetBranchAddress("eT_p4_t", &eT_p4_t, &b_eT_p4_t);
   fChain->SetBranchAddress("eT_corrected_p4_x", &eT_corrected_p4_x, &b_eT_corrected_p4_x);
   fChain->SetBranchAddress("eT_corrected_p4_y", &eT_corrected_p4_y, &b_eT_corrected_p4_y);
   fChain->SetBranchAddress("eT_corrected_p4_z", &eT_corrected_p4_z, &b_eT_corrected_p4_z);
   fChain->SetBranchAddress("eT_corrected_p4_t", &eT_corrected_p4_t, &b_eT_corrected_p4_t);
   fChain->SetBranchAddress("eT_electronIndex", &eT_electronIndex, &b_eT_electronIndex);
   fChain->SetBranchAddress("eT_tauIndex", &eT_tauIndex, &b_eT_tauIndex);
   fChain->SetBranchAddress("eT_scalarSumPt", &eT_scalarSumPt, &b_eT_scalarSumPt);
   fChain->SetBranchAddress("eT_DR", &eT_DR, &b_eT_DR);
   fChain->SetBranchAddress("eT_sumCharge", &eT_sumCharge, &b_eT_sumCharge);
   fChain->SetBranchAddress("eT_correctedSVFitMass", &eT_correctedSVFitMass, &b_eT_correctedSVFitMass);
   fChain->SetBranchAddress("eT_rawSVFitMass", &eT_rawSVFitMass, &b_eT_rawSVFitMass);
   fChain->SetBranchAddress("eT_TransverseMass", &eT_TransverseMass, &b_eT_TransverseMass);
   fChain->SetBranchAddress("eT_rawTransverseMass", &eT_rawTransverseMass, &b_eT_rawTransverseMass);
   fChain->SetBranchAddress("eT_mvaMETraw", &eT_mvaMETraw, &b_eT_mvaMETraw);
   fChain->SetBranchAddress("eT_mvaMET", &eT_mvaMET, &b_eT_mvaMET);
   fChain->SetBranchAddress("eT_mvaMETphiRaw", &eT_mvaMETphiRaw, &b_eT_mvaMETphiRaw);
   fChain->SetBranchAddress("eT_mvaMETphi", &eT_mvaMETphi, &b_eT_mvaMETphi);
   fChain->SetBranchAddress("eT_MAX", &eT_MAX, &b_eT_MAX);
   fChain->SetBranchAddress("eT_isGoodTriggerPair", &eT_isGoodTriggerPair, &b_eT_isGoodTriggerPair);
   fChain->SetBranchAddress("eT_njets", &eT_njets, &b_eT_njets);
   fChain->SetBranchAddress("eT_nbjets", &eT_nbjets, &b_eT_nbjets);
   fChain->SetBranchAddress("eT_nbjetsLOOSE", &eT_nbjetsLOOSE, &b_eT_nbjetsLOOSE);
   fChain->SetBranchAddress("eT_nbjetsLOOSEUP", &eT_nbjetsLOOSEUP, &b_eT_nbjetsLOOSEUP);
   fChain->SetBranchAddress("eT_nbjetsLOOSEDOWN", &eT_nbjetsLOOSEDOWN, &b_eT_nbjetsLOOSEDOWN);
   fChain->SetBranchAddress("eT_njetsUP", &eT_njetsUP, &b_eT_njetsUP);
   fChain->SetBranchAddress("eT_nbjetsUP", &eT_nbjetsUP, &b_eT_nbjetsUP);
   fChain->SetBranchAddress("eT_njetsDOWN", &eT_njetsDOWN, &b_eT_njetsDOWN);
   fChain->SetBranchAddress("eT_nbjetsDOWN", &eT_nbjetsDOWN, &b_eT_nbjetsDOWN);
   fChain->SetBranchAddress("eT_jet1P4_x", &eT_jet1P4_x, &b_eT_jet1P4_x);
   fChain->SetBranchAddress("eT_jet1P4_y", &eT_jet1P4_y, &b_eT_jet1P4_y);
   fChain->SetBranchAddress("eT_jet1P4_z", &eT_jet1P4_z, &b_eT_jet1P4_z);
   fChain->SetBranchAddress("eT_jet1P4_t", &eT_jet1P4_t, &b_eT_jet1P4_t);
   fChain->SetBranchAddress("eT_jet1RawP4_x", &eT_jet1RawP4_x, &b_eT_jet1RawP4_x);
   fChain->SetBranchAddress("eT_jet1RawP4_y", &eT_jet1RawP4_y, &b_eT_jet1RawP4_y);
   fChain->SetBranchAddress("eT_jet1RawP4_z", &eT_jet1RawP4_z, &b_eT_jet1RawP4_z);
   fChain->SetBranchAddress("eT_jet1RawP4_t", &eT_jet1RawP4_t, &b_eT_jet1RawP4_t);
   fChain->SetBranchAddress("eT_jet1IDMVA", &eT_jet1IDMVA, &b_eT_jet1IDMVA);
   fChain->SetBranchAddress("eT_jet1BTAGMVA", &eT_jet1BTAGMVA, &b_eT_jet1BTAGMVA);
   fChain->SetBranchAddress("eT_jet2P4_x", &eT_jet2P4_x, &b_eT_jet2P4_x);
   fChain->SetBranchAddress("eT_jet2P4_y", &eT_jet2P4_y, &b_eT_jet2P4_y);
   fChain->SetBranchAddress("eT_jet2P4_z", &eT_jet2P4_z, &b_eT_jet2P4_z);
   fChain->SetBranchAddress("eT_jet2P4_t", &eT_jet2P4_t, &b_eT_jet2P4_t);
   fChain->SetBranchAddress("eT_jet2RawP4_x", &eT_jet2RawP4_x, &b_eT_jet2RawP4_x);
   fChain->SetBranchAddress("eT_jet2RawP4_y", &eT_jet2RawP4_y, &b_eT_jet2RawP4_y);
   fChain->SetBranchAddress("eT_jet2RawP4_z", &eT_jet2RawP4_z, &b_eT_jet2RawP4_z);
   fChain->SetBranchAddress("eT_jet2RawP4_t", &eT_jet2RawP4_t, &b_eT_jet2RawP4_t);
   fChain->SetBranchAddress("eT_jet2IDMVA", &eT_jet2IDMVA, &b_eT_jet2IDMVA);
   fChain->SetBranchAddress("eT_jet2BTAGMVA", &eT_jet2BTAGMVA, &b_eT_jet2BTAGMVA);
   fChain->SetBranchAddress("eT_cov00", &eT_cov00, &b_eT_cov00);
   fChain->SetBranchAddress("eT_cov01", &eT_cov01, &b_eT_cov01);
   fChain->SetBranchAddress("eT_cov10", &eT_cov10, &b_eT_cov10);
   fChain->SetBranchAddress("eT_cov11", &eT_cov11, &b_eT_cov11);
   fChain->SetBranchAddress("eT_passesTriLeptonVeto", &eT_passesTriLeptonVeto, &b_eT_passesTriLeptonVeto);
   fChain->SetBranchAddress("eT_passNonTopEmbeddedTriggerAndMass50", &eT_passNonTopEmbeddedTriggerAndMass50, &b_eT_passNonTopEmbeddedTriggerAndMass50);
   fChain->SetBranchAddress("eT_passSignalGeneratorMass70to130Cut", &eT_passSignalGeneratorMass70to130Cut, &b_eT_passSignalGeneratorMass70to130Cut);
   fChain->SetBranchAddress("eT_genBosonP4_x", &eT_genBosonP4_x, &b_eT_genBosonP4_x);
   fChain->SetBranchAddress("eT_genBosonP4_y", &eT_genBosonP4_y, &b_eT_genBosonP4_y);
   fChain->SetBranchAddress("eT_genBosonP4_z", &eT_genBosonP4_z, &b_eT_genBosonP4_z);
   fChain->SetBranchAddress("eT_genBosonP4_t", &eT_genBosonP4_t, &b_eT_genBosonP4_t);
   fChain->SetBranchAddress("eT_genTOPp4_x", &eT_genTOPp4_x, &b_eT_genTOPp4_x);
   fChain->SetBranchAddress("eT_genTOPp4_y", &eT_genTOPp4_y, &b_eT_genTOPp4_y);
   fChain->SetBranchAddress("eT_genTOPp4_z", &eT_genTOPp4_z, &b_eT_genTOPp4_z);
   fChain->SetBranchAddress("eT_genTOPp4_t", &eT_genTOPp4_t, &b_eT_genTOPp4_t);
   fChain->SetBranchAddress("eT_genTOPBARp4_x", &eT_genTOPBARp4_x, &b_eT_genTOPBARp4_x);
   fChain->SetBranchAddress("eT_genTOPBARp4_y", &eT_genTOPBARp4_y, &b_eT_genTOPBARp4_y);
   fChain->SetBranchAddress("eT_genTOPBARp4_z", &eT_genTOPBARp4_z, &b_eT_genTOPBARp4_z);
   fChain->SetBranchAddress("eT_genTOPBARp4_t", &eT_genTOPBARp4_t, &b_eT_genTOPBARp4_t);
   fChain->SetBranchAddress("eT_numberOfGoodVertices", &eT_numberOfGoodVertices, &b_eT_numberOfGoodVertices);
   fChain->SetBranchAddress("eT_PVndof", &eT_PVndof, &b_eT_PVndof);
   fChain->SetBranchAddress("eT_PVz", &eT_PVz, &b_eT_PVz);
   fChain->SetBranchAddress("eT_PVpositionRho", &eT_PVpositionRho, &b_eT_PVpositionRho);
   fChain->SetBranchAddress("eT_PVp4_x", &eT_PVp4_x, &b_eT_PVp4_x);
   fChain->SetBranchAddress("eT_PVp4_y", &eT_PVp4_y, &b_eT_PVp4_y);
   fChain->SetBranchAddress("eT_PVp4_z", &eT_PVp4_z, &b_eT_PVp4_z);
   fChain->SetBranchAddress("eT_PVp4_t", &eT_PVp4_t, &b_eT_PVp4_t);
   fChain->SetBranchAddress("eT_isDecayZtauTau", &eT_isDecayZtauTau, &b_eT_isDecayZtauTau);
   fChain->SetBranchAddress("eT_isDecayZeE", &eT_isDecayZeE, &b_eT_isDecayZeE);
   fChain->SetBranchAddress("eT_isDecayZmuMu", &eT_isDecayZmuMu, &b_eT_isDecayZmuMu);
   fChain->SetBranchAddress("eT_isRecoLep_matchedTo_GenTauFromZ", &eT_isRecoLep_matchedTo_GenTauFromZ, &b_eT_isRecoLep_matchedTo_GenTauFromZ);
   fChain->SetBranchAddress("eT_isRecoTau_matchedTo_GenTauFromZ", &eT_isRecoTau_matchedTo_GenTauFromZ, &b_eT_isRecoTau_matchedTo_GenTauFromZ);
   fChain->SetBranchAddress("eT_isRecoLep_matchedTo_GenElecFromZ", &eT_isRecoLep_matchedTo_GenElecFromZ, &b_eT_isRecoLep_matchedTo_GenElecFromZ);
   fChain->SetBranchAddress("eT_isRecoTau_matchedTo_GenElecFromZ", &eT_isRecoTau_matchedTo_GenElecFromZ, &b_eT_isRecoTau_matchedTo_GenElecFromZ);
   fChain->SetBranchAddress("eT_isRecoLep_matchedTo_GenMuonFromZ", &eT_isRecoLep_matchedTo_GenMuonFromZ, &b_eT_isRecoLep_matchedTo_GenMuonFromZ);
   fChain->SetBranchAddress("eT_isRecoTau_matchedTo_GenMuonFromZ", &eT_isRecoTau_matchedTo_GenMuonFromZ, &b_eT_isRecoTau_matchedTo_GenMuonFromZ);
   fChain->SetBranchAddress("eT_isRecoLep_matchedTo_GenElecFromTau", &eT_isRecoLep_matchedTo_GenElecFromTau, &b_eT_isRecoLep_matchedTo_GenElecFromTau);
   fChain->SetBranchAddress("eT_isRecoTau_matchedTo_GenElecFromTau", &eT_isRecoTau_matchedTo_GenElecFromTau, &b_eT_isRecoTau_matchedTo_GenElecFromTau);
   fChain->SetBranchAddress("eT_isRecoLep_matchedTo_GenMuonFromTau", &eT_isRecoLep_matchedTo_GenMuonFromTau, &b_eT_isRecoLep_matchedTo_GenMuonFromTau);
   fChain->SetBranchAddress("eT_isRecoTau_matchedTo_GenMuonFromTau", &eT_isRecoTau_matchedTo_GenMuonFromTau, &b_eT_isRecoTau_matchedTo_GenMuonFromTau);
   fChain->SetBranchAddress("eT_passEmbeddedTrigger", &eT_passEmbeddedTrigger, &b_eT_passEmbeddedTrigger);
   fChain->SetBranchAddress("eT_ele_p4_x", &eT_ele_p4_x, &b_eT_ele_p4_x);
   fChain->SetBranchAddress("eT_ele_p4_y", &eT_ele_p4_y, &b_eT_ele_p4_y);
   fChain->SetBranchAddress("eT_ele_p4_z", &eT_ele_p4_z, &b_eT_ele_p4_z);
   fChain->SetBranchAddress("eT_ele_p4_t", &eT_ele_p4_t, &b_eT_ele_p4_t);
   fChain->SetBranchAddress("eT_ele_genP4_x", &eT_ele_genP4_x, &b_eT_ele_genP4_x);
   fChain->SetBranchAddress("eT_ele_genP4_y", &eT_ele_genP4_y, &b_eT_ele_genP4_y);
   fChain->SetBranchAddress("eT_ele_genP4_z", &eT_ele_genP4_z, &b_eT_ele_genP4_z);
   fChain->SetBranchAddress("eT_ele_genP4_t", &eT_ele_genP4_t, &b_eT_ele_genP4_t);
   fChain->SetBranchAddress("eT_ele_pfP4_x", &eT_ele_pfP4_x, &b_eT_ele_pfP4_x);
   fChain->SetBranchAddress("eT_ele_pfP4_y", &eT_ele_pfP4_y, &b_eT_ele_pfP4_y);
   fChain->SetBranchAddress("eT_ele_pfP4_z", &eT_ele_pfP4_z, &b_eT_ele_pfP4_z);
   fChain->SetBranchAddress("eT_ele_pfP4_t", &eT_ele_pfP4_t, &b_eT_ele_pfP4_t);
   fChain->SetBranchAddress("eT_ele_charge", &eT_ele_charge, &b_eT_ele_charge);
   fChain->SetBranchAddress("eT_ele_PFpdgId", &eT_ele_PFpdgId, &b_eT_ele_PFpdgId);
   fChain->SetBranchAddress("eT_ele_GENpdgId", &eT_ele_GENpdgId, &b_eT_ele_GENpdgId);
   fChain->SetBranchAddress("eT_ele_numberOfMissingInnerHits", &eT_ele_numberOfMissingInnerHits, &b_eT_ele_numberOfMissingInnerHits);
   fChain->SetBranchAddress("eT_ele_passConversionVeto", &eT_ele_passConversionVeto, &b_eT_ele_passConversionVeto);
   fChain->SetBranchAddress("eT_ele_dz", &eT_ele_dz, &b_eT_ele_dz);
   fChain->SetBranchAddress("eT_ele_dB", &eT_ele_dB, &b_eT_ele_dB);
   fChain->SetBranchAddress("eT_ele_dxy", &eT_ele_dxy, &b_eT_ele_dxy);
   fChain->SetBranchAddress("eT_ele_SuperClusterEta", &eT_ele_SuperClusterEta, &b_eT_ele_SuperClusterEta);
   fChain->SetBranchAddress("eT_ele_mvaTrigV0", &eT_ele_mvaTrigV0, &b_eT_ele_mvaTrigV0);
   fChain->SetBranchAddress("eT_ele_mvaTrigNoIPV0", &eT_ele_mvaTrigNoIPV0, &b_eT_ele_mvaTrigNoIPV0);
   fChain->SetBranchAddress("eT_ele_mvaNonTrigV0", &eT_ele_mvaNonTrigV0, &b_eT_ele_mvaNonTrigV0);
   fChain->SetBranchAddress("eT_ele_pass_tight_mvaNonTrigV0", &eT_ele_pass_tight_mvaNonTrigV0, &b_eT_ele_pass_tight_mvaNonTrigV0);
   fChain->SetBranchAddress("eT_ele_passFullId", &eT_ele_passFullId, &b_eT_ele_passFullId);
   fChain->SetBranchAddress("eT_ele_chargedHadronIso", &eT_ele_chargedHadronIso, &b_eT_ele_chargedHadronIso);
   fChain->SetBranchAddress("eT_ele_photonIso", &eT_ele_photonIso, &b_eT_ele_photonIso);
   fChain->SetBranchAddress("eT_ele_neutralHadronIso", &eT_ele_neutralHadronIso, &b_eT_ele_neutralHadronIso);
   fChain->SetBranchAddress("eT_ele_puChargedHadronIso", &eT_ele_puChargedHadronIso, &b_eT_ele_puChargedHadronIso);
   fChain->SetBranchAddress("eT_ele_relativeIso", &eT_ele_relativeIso, &b_eT_ele_relativeIso);
   fChain->SetBranchAddress("eT_ele_isEB", &eT_ele_isEB, &b_eT_ele_isEB);
   fChain->SetBranchAddress("eT_ele_isEE", &eT_ele_isEE, &b_eT_ele_isEE);
   fChain->SetBranchAddress("eT_ele_isEBEEGap", &eT_ele_isEBEEGap, &b_eT_ele_isEBEEGap);
   fChain->SetBranchAddress("eT_ele_isEBEtaGap", &eT_ele_isEBEtaGap, &b_eT_ele_isEBEtaGap);
   fChain->SetBranchAddress("eT_ele_isEBPhiGap", &eT_ele_isEBPhiGap, &b_eT_ele_isEBPhiGap);
   fChain->SetBranchAddress("eT_ele_isEEDeeGap", &eT_ele_isEEDeeGap, &b_eT_ele_isEEDeeGap);
   fChain->SetBranchAddress("eT_ele_isEERingGap", &eT_ele_isEERingGap, &b_eT_ele_isEERingGap);
   fChain->SetBranchAddress("eT_ele_sigmaEtaEta", &eT_ele_sigmaEtaEta, &b_eT_ele_sigmaEtaEta);
   fChain->SetBranchAddress("eT_ele_sigmaIetaIeta", &eT_ele_sigmaIetaIeta, &b_eT_ele_sigmaIetaIeta);
   fChain->SetBranchAddress("eT_ele_sigmaIphiIphi", &eT_ele_sigmaIphiIphi, &b_eT_ele_sigmaIphiIphi);
   fChain->SetBranchAddress("eT_ele_has_HltMatchEle20", &eT_ele_has_HltMatchEle20, &b_eT_ele_has_HltMatchEle20);
   fChain->SetBranchAddress("eT_ele_has_HltMatchEle22", &eT_ele_has_HltMatchEle22, &b_eT_ele_has_HltMatchEle22);
   fChain->SetBranchAddress("eT_ele_has_HltMatchEle27", &eT_ele_has_HltMatchEle27, &b_eT_ele_has_HltMatchEle27);
   fChain->SetBranchAddress("eT_ele_isTriLeptonVetoCandidate", &eT_ele_isTriLeptonVetoCandidate, &b_eT_ele_isTriLeptonVetoCandidate);
   fChain->SetBranchAddress("eT_ele_deltaPhiSuperClusterTrackAtVtx", &eT_ele_deltaPhiSuperClusterTrackAtVtx, &b_eT_ele_deltaPhiSuperClusterTrackAtVtx);
   fChain->SetBranchAddress("eT_ele_deltaEtaSuperClusterTrackAtVtx", &eT_ele_deltaEtaSuperClusterTrackAtVtx, &b_eT_ele_deltaEtaSuperClusterTrackAtVtx);
   fChain->SetBranchAddress("eT_ele_hadronicOverEm", &eT_ele_hadronicOverEm, &b_eT_ele_hadronicOverEm);
   fChain->SetBranchAddress("eT_tau_pfJetRefP4_x", &eT_tau_pfJetRefP4_x, &b_eT_tau_pfJetRefP4_x);
   fChain->SetBranchAddress("eT_tau_pfJetRefP4_y", &eT_tau_pfJetRefP4_y, &b_eT_tau_pfJetRefP4_y);
   fChain->SetBranchAddress("eT_tau_pfJetRefP4_z", &eT_tau_pfJetRefP4_z, &b_eT_tau_pfJetRefP4_z);
   fChain->SetBranchAddress("eT_tau_pfJetRefP4_t", &eT_tau_pfJetRefP4_t, &b_eT_tau_pfJetRefP4_t);
   fChain->SetBranchAddress("eT_tau_p4_x", &eT_tau_p4_x, &b_eT_tau_p4_x);
   fChain->SetBranchAddress("eT_tau_p4_y", &eT_tau_p4_y, &b_eT_tau_p4_y);
   fChain->SetBranchAddress("eT_tau_p4_z", &eT_tau_p4_z, &b_eT_tau_p4_z);
   fChain->SetBranchAddress("eT_tau_p4_t", &eT_tau_p4_t, &b_eT_tau_p4_t);
   fChain->SetBranchAddress("eT_tau_genP4_x", &eT_tau_genP4_x, &b_eT_tau_genP4_x);
   fChain->SetBranchAddress("eT_tau_genP4_y", &eT_tau_genP4_y, &b_eT_tau_genP4_y);
   fChain->SetBranchAddress("eT_tau_genP4_z", &eT_tau_genP4_z, &b_eT_tau_genP4_z);
   fChain->SetBranchAddress("eT_tau_genP4_t", &eT_tau_genP4_t, &b_eT_tau_genP4_t);
   fChain->SetBranchAddress("eT_tau_genJet_x", &eT_tau_genJet_x, &b_eT_tau_genJet_x);
   fChain->SetBranchAddress("eT_tau_genJet_y", &eT_tau_genJet_y, &b_eT_tau_genJet_y);
   fChain->SetBranchAddress("eT_tau_genJet_z", &eT_tau_genJet_z, &b_eT_tau_genJet_z);
   fChain->SetBranchAddress("eT_tau_genJet_t", &eT_tau_genJet_t, &b_eT_tau_genJet_t);
   fChain->SetBranchAddress("eT_tau_corrected_p4_x", &eT_tau_corrected_p4_x, &b_eT_tau_corrected_p4_x);
   fChain->SetBranchAddress("eT_tau_corrected_p4_y", &eT_tau_corrected_p4_y, &b_eT_tau_corrected_p4_y);
   fChain->SetBranchAddress("eT_tau_corrected_p4_z", &eT_tau_corrected_p4_z, &b_eT_tau_corrected_p4_z);
   fChain->SetBranchAddress("eT_tau_corrected_p4_t", &eT_tau_corrected_p4_t, &b_eT_tau_corrected_p4_t);
   fChain->SetBranchAddress("eT_tau_pdgId", &eT_tau_pdgId, &b_eT_tau_pdgId);
   fChain->SetBranchAddress("eT_tau_pdgIdGEN", &eT_tau_pdgIdGEN, &b_eT_tau_pdgIdGEN);
   fChain->SetBranchAddress("eT_tau_charge", &eT_tau_charge, &b_eT_tau_charge);
   fChain->SetBranchAddress("eT_tau_decayMode", &eT_tau_decayMode, &b_eT_tau_decayMode);
   fChain->SetBranchAddress("eT_tau_passFullId_muTau", &eT_tau_passFullId_muTau, &b_eT_tau_passFullId_muTau);
   fChain->SetBranchAddress("eT_tau_passFullId_eTau", &eT_tau_passFullId_eTau, &b_eT_tau_passFullId_eTau);
   fChain->SetBranchAddress("eT_tau_numStrips", &eT_tau_numStrips, &b_eT_tau_numStrips);
   fChain->SetBranchAddress("eT_tau_numHadrons", &eT_tau_numHadrons, &b_eT_tau_numHadrons);
   fChain->SetBranchAddress("eT_tau_againstElectronDeadECAL", &eT_tau_againstElectronDeadECAL, &b_eT_tau_againstElectronDeadECAL);
   fChain->SetBranchAddress("eT_tau_againstElectronLoose", &eT_tau_againstElectronLoose, &b_eT_tau_againstElectronLoose);
   fChain->SetBranchAddress("eT_tau_againstElectronLooseMVA5", &eT_tau_againstElectronLooseMVA5, &b_eT_tau_againstElectronLooseMVA5);
   fChain->SetBranchAddress("eT_tau_againstElectronMVA5category", &eT_tau_againstElectronMVA5category, &b_eT_tau_againstElectronMVA5category);
   fChain->SetBranchAddress("eT_tau_againstElectronMVA5raw", &eT_tau_againstElectronMVA5raw, &b_eT_tau_againstElectronMVA5raw);
   fChain->SetBranchAddress("eT_tau_againstElectronMedium", &eT_tau_againstElectronMedium, &b_eT_tau_againstElectronMedium);
   fChain->SetBranchAddress("eT_tau_againstElectronMediumMVA5", &eT_tau_againstElectronMediumMVA5, &b_eT_tau_againstElectronMediumMVA5);
   fChain->SetBranchAddress("eT_tau_againstElectronTight", &eT_tau_againstElectronTight, &b_eT_tau_againstElectronTight);
   fChain->SetBranchAddress("eT_tau_againstElectronTightMVA5", &eT_tau_againstElectronTightMVA5, &b_eT_tau_againstElectronTightMVA5);
   fChain->SetBranchAddress("eT_tau_againstElectronVLooseMVA5", &eT_tau_againstElectronVLooseMVA5, &b_eT_tau_againstElectronVLooseMVA5);
   fChain->SetBranchAddress("eT_tau_againstElectronVTightMVA5", &eT_tau_againstElectronVTightMVA5, &b_eT_tau_againstElectronVTightMVA5);
   fChain->SetBranchAddress("eT_tau_againstMuonLoose", &eT_tau_againstMuonLoose, &b_eT_tau_againstMuonLoose);
   fChain->SetBranchAddress("eT_tau_againstMuonLoose2", &eT_tau_againstMuonLoose2, &b_eT_tau_againstMuonLoose2);
   fChain->SetBranchAddress("eT_tau_againstMuonLoose3", &eT_tau_againstMuonLoose3, &b_eT_tau_againstMuonLoose3);
   fChain->SetBranchAddress("eT_tau_againstMuonLooseMVA", &eT_tau_againstMuonLooseMVA, &b_eT_tau_againstMuonLooseMVA);
   fChain->SetBranchAddress("eT_tau_againstMuonMVAraw", &eT_tau_againstMuonMVAraw, &b_eT_tau_againstMuonMVAraw);
   fChain->SetBranchAddress("eT_tau_againstMuonMedium", &eT_tau_againstMuonMedium, &b_eT_tau_againstMuonMedium);
   fChain->SetBranchAddress("eT_tau_againstMuonMedium2", &eT_tau_againstMuonMedium2, &b_eT_tau_againstMuonMedium2);
   fChain->SetBranchAddress("eT_tau_againstMuonMediumMVA", &eT_tau_againstMuonMediumMVA, &b_eT_tau_againstMuonMediumMVA);
   fChain->SetBranchAddress("eT_tau_againstMuonTight", &eT_tau_againstMuonTight, &b_eT_tau_againstMuonTight);
   fChain->SetBranchAddress("eT_tau_againstMuonTight2", &eT_tau_againstMuonTight2, &b_eT_tau_againstMuonTight2);
   fChain->SetBranchAddress("eT_tau_againstMuonTight3", &eT_tau_againstMuonTight3, &b_eT_tau_againstMuonTight3);
   fChain->SetBranchAddress("eT_tau_againstMuonTightMVA", &eT_tau_againstMuonTightMVA, &b_eT_tau_againstMuonTightMVA);
   fChain->SetBranchAddress("eT_tau_byCombinedIsolationDeltaBetaCorrRaw", &eT_tau_byCombinedIsolationDeltaBetaCorrRaw, &b_eT_tau_byCombinedIsolationDeltaBetaCorrRaw);
   fChain->SetBranchAddress("eT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits", &eT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits, &b_eT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits);
   fChain->SetBranchAddress("eT_tau_byIsolationMVA3newDMwLTraw", &eT_tau_byIsolationMVA3newDMwLTraw, &b_eT_tau_byIsolationMVA3newDMwLTraw);
   fChain->SetBranchAddress("eT_tau_byIsolationMVA3newDMwoLTraw", &eT_tau_byIsolationMVA3newDMwoLTraw, &b_eT_tau_byIsolationMVA3newDMwoLTraw);
   fChain->SetBranchAddress("eT_tau_byIsolationMVA3oldDMwLTraw", &eT_tau_byIsolationMVA3oldDMwLTraw, &b_eT_tau_byIsolationMVA3oldDMwLTraw);
   fChain->SetBranchAddress("eT_tau_byIsolationMVA3oldDMwoLTraw", &eT_tau_byIsolationMVA3oldDMwoLTraw, &b_eT_tau_byIsolationMVA3oldDMwoLTraw);
   fChain->SetBranchAddress("eT_tau_byLooseCombinedIsolationDeltaBetaCorr", &eT_tau_byLooseCombinedIsolationDeltaBetaCorr, &b_eT_tau_byLooseCombinedIsolationDeltaBetaCorr);
   fChain->SetBranchAddress("eT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits", &eT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits, &b_eT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits);
   fChain->SetBranchAddress("eT_tau_byLooseIsolation", &eT_tau_byLooseIsolation, &b_eT_tau_byLooseIsolation);
   fChain->SetBranchAddress("eT_tau_byLooseIsolationMVA3newDMwLT", &eT_tau_byLooseIsolationMVA3newDMwLT, &b_eT_tau_byLooseIsolationMVA3newDMwLT);
   fChain->SetBranchAddress("eT_tau_byLooseIsolationMVA3newDMwoLT", &eT_tau_byLooseIsolationMVA3newDMwoLT, &b_eT_tau_byLooseIsolationMVA3newDMwoLT);
   fChain->SetBranchAddress("eT_tau_byLooseIsolationMVA3oldDMwLT", &eT_tau_byLooseIsolationMVA3oldDMwLT, &b_eT_tau_byLooseIsolationMVA3oldDMwLT);
   fChain->SetBranchAddress("eT_tau_byLooseIsolationMVA3oldDMwoLT", &eT_tau_byLooseIsolationMVA3oldDMwoLT, &b_eT_tau_byLooseIsolationMVA3oldDMwoLT);
   fChain->SetBranchAddress("eT_tau_byMediumCombinedIsolationDeltaBetaCorr", &eT_tau_byMediumCombinedIsolationDeltaBetaCorr, &b_eT_tau_byMediumCombinedIsolationDeltaBetaCorr);
   fChain->SetBranchAddress("eT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits", &eT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits, &b_eT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits);
   fChain->SetBranchAddress("eT_tau_byMediumIsolationMVA3newDMwLT", &eT_tau_byMediumIsolationMVA3newDMwLT, &b_eT_tau_byMediumIsolationMVA3newDMwLT);
   fChain->SetBranchAddress("eT_tau_byMediumIsolationMVA3newDMwoLT", &eT_tau_byMediumIsolationMVA3newDMwoLT, &b_eT_tau_byMediumIsolationMVA3newDMwoLT);
   fChain->SetBranchAddress("eT_tau_byMediumIsolationMVA3oldDMwLT", &eT_tau_byMediumIsolationMVA3oldDMwLT, &b_eT_tau_byMediumIsolationMVA3oldDMwLT);
   fChain->SetBranchAddress("eT_tau_byMediumIsolationMVA3oldDMwoLT", &eT_tau_byMediumIsolationMVA3oldDMwoLT, &b_eT_tau_byMediumIsolationMVA3oldDMwoLT);
   fChain->SetBranchAddress("eT_tau_byTightCombinedIsolationDeltaBetaCorr", &eT_tau_byTightCombinedIsolationDeltaBetaCorr, &b_eT_tau_byTightCombinedIsolationDeltaBetaCorr);
   fChain->SetBranchAddress("eT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits", &eT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits, &b_eT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits);
   fChain->SetBranchAddress("eT_tau_byTightIsolationMVA3newDMwLT", &eT_tau_byTightIsolationMVA3newDMwLT, &b_eT_tau_byTightIsolationMVA3newDMwLT);
   fChain->SetBranchAddress("eT_tau_byTightIsolationMVA3newDMwoLT", &eT_tau_byTightIsolationMVA3newDMwoLT, &b_eT_tau_byTightIsolationMVA3newDMwoLT);
   fChain->SetBranchAddress("eT_tau_byTightIsolationMVA3oldDMwLT", &eT_tau_byTightIsolationMVA3oldDMwLT, &b_eT_tau_byTightIsolationMVA3oldDMwLT);
   fChain->SetBranchAddress("eT_tau_byTightIsolationMVA3oldDMwoLT", &eT_tau_byTightIsolationMVA3oldDMwoLT, &b_eT_tau_byTightIsolationMVA3oldDMwoLT);
   fChain->SetBranchAddress("eT_tau_byVLooseCombinedIsolationDeltaBetaCorr", &eT_tau_byVLooseCombinedIsolationDeltaBetaCorr, &b_eT_tau_byVLooseCombinedIsolationDeltaBetaCorr);
   fChain->SetBranchAddress("eT_tau_byVLooseIsolationMVA3newDMwLT", &eT_tau_byVLooseIsolationMVA3newDMwLT, &b_eT_tau_byVLooseIsolationMVA3newDMwLT);
   fChain->SetBranchAddress("eT_tau_byVLooseIsolationMVA3newDMwoLT", &eT_tau_byVLooseIsolationMVA3newDMwoLT, &b_eT_tau_byVLooseIsolationMVA3newDMwoLT);
   fChain->SetBranchAddress("eT_tau_byVLooseIsolationMVA3oldDMwLT", &eT_tau_byVLooseIsolationMVA3oldDMwLT, &b_eT_tau_byVLooseIsolationMVA3oldDMwLT);
   fChain->SetBranchAddress("eT_tau_byVLooseIsolationMVA3oldDMwoLT", &eT_tau_byVLooseIsolationMVA3oldDMwoLT, &b_eT_tau_byVLooseIsolationMVA3oldDMwoLT);
   fChain->SetBranchAddress("eT_tau_byVTightIsolationMVA3newDMwLT", &eT_tau_byVTightIsolationMVA3newDMwLT, &b_eT_tau_byVTightIsolationMVA3newDMwLT);
   fChain->SetBranchAddress("eT_tau_byVTightIsolationMVA3newDMwoLT", &eT_tau_byVTightIsolationMVA3newDMwoLT, &b_eT_tau_byVTightIsolationMVA3newDMwoLT);
   fChain->SetBranchAddress("eT_tau_byVTightIsolationMVA3oldDMwLT", &eT_tau_byVTightIsolationMVA3oldDMwLT, &b_eT_tau_byVTightIsolationMVA3oldDMwLT);
   fChain->SetBranchAddress("eT_tau_byVTightIsolationMVA3oldDMwoLT", &eT_tau_byVTightIsolationMVA3oldDMwoLT, &b_eT_tau_byVTightIsolationMVA3oldDMwoLT);
   fChain->SetBranchAddress("eT_tau_byVVTightIsolationMVA3newDMwLT", &eT_tau_byVVTightIsolationMVA3newDMwLT, &b_eT_tau_byVVTightIsolationMVA3newDMwLT);
   fChain->SetBranchAddress("eT_tau_byVVTightIsolationMVA3newDMwoLT", &eT_tau_byVVTightIsolationMVA3newDMwoLT, &b_eT_tau_byVVTightIsolationMVA3newDMwoLT);
   fChain->SetBranchAddress("eT_tau_byVVTightIsolationMVA3oldDMwLT", &eT_tau_byVVTightIsolationMVA3oldDMwLT, &b_eT_tau_byVVTightIsolationMVA3oldDMwLT);
   fChain->SetBranchAddress("eT_tau_byVVTightIsolationMVA3oldDMwoLT", &eT_tau_byVVTightIsolationMVA3oldDMwoLT, &b_eT_tau_byVVTightIsolationMVA3oldDMwoLT);
   fChain->SetBranchAddress("eT_tau_chargedIsoPtSum", &eT_tau_chargedIsoPtSum, &b_eT_tau_chargedIsoPtSum);
   fChain->SetBranchAddress("eT_tau_decayModeFinding", &eT_tau_decayModeFinding, &b_eT_tau_decayModeFinding);
   fChain->SetBranchAddress("eT_tau_decayModeFindingNewDMs", &eT_tau_decayModeFindingNewDMs, &b_eT_tau_decayModeFindingNewDMs);
   fChain->SetBranchAddress("eT_tau_decayModeFindingOldDMs", &eT_tau_decayModeFindingOldDMs, &b_eT_tau_decayModeFindingOldDMs);
   fChain->SetBranchAddress("eT_tau_neutralIsoPtSum", &eT_tau_neutralIsoPtSum, &b_eT_tau_neutralIsoPtSum);
   fChain->SetBranchAddress("eT_tau_puCorrPtSum", &eT_tau_puCorrPtSum, &b_eT_tau_puCorrPtSum);
   fChain->SetBranchAddress("eT_tau_has_HltMatchEle20", &eT_tau_has_HltMatchEle20, &b_eT_tau_has_HltMatchEle20);
   fChain->SetBranchAddress("eT_tau_has_HltMatchEle22", &eT_tau_has_HltMatchEle22, &b_eT_tau_has_HltMatchEle22);
   fChain->SetBranchAddress("eT_tau_has_HltMatchEle27", &eT_tau_has_HltMatchEle27, &b_eT_tau_has_HltMatchEle27);
   fChain->SetBranchAddress("eT_tau_has_HltMatchMu17", &eT_tau_has_HltMatchMu17, &b_eT_tau_has_HltMatchMu17);
   fChain->SetBranchAddress("eT_tau_has_HltMatchMu18", &eT_tau_has_HltMatchMu18, &b_eT_tau_has_HltMatchMu18);
   fChain->SetBranchAddress("eT_tau_has_HltMatchMu24", &eT_tau_has_HltMatchMu24, &b_eT_tau_has_HltMatchMu24);
   fChain->SetBranchAddress("eT_puWeight", &eT_puWeight, &b_eT_puWeight);
   fChain->SetBranchAddress("eT_puWeightM1", &eT_puWeightM1, &b_eT_puWeightM1);
   fChain->SetBranchAddress("eT_puWeightP1", &eT_puWeightP1, &b_eT_puWeightP1);
   fChain->SetBranchAddress("eT_NumPileupInt", &eT_NumPileupInt, &b_eT_NumPileupInt);
   fChain->SetBranchAddress("eT_NumTruePileUpInt", &eT_NumTruePileUpInt, &b_eT_NumTruePileUpInt);
   fChain->SetBranchAddress("eT_NumPileupIntM1", &eT_NumPileupIntM1, &b_eT_NumPileupIntM1);
   fChain->SetBranchAddress("eT_NumTruePileUpIntM1", &eT_NumTruePileUpIntM1, &b_eT_NumTruePileUpIntM1);
   fChain->SetBranchAddress("eT_NumPileupIntP1", &eT_NumPileupIntP1, &b_eT_NumPileupIntP1);
   fChain->SetBranchAddress("eT_NumTruePileUpIntP1", &eT_NumTruePileUpIntP1, &b_eT_NumTruePileUpIntP1);
   fChain->SetBranchAddress("eT_EffDataELE20andELE22", &eT_EffDataELE20andELE22, &b_eT_EffDataELE20andELE22);
   fChain->SetBranchAddress("eT_EffMcELE20andELE22", &eT_EffMcELE20andELE22, &b_eT_EffMcELE20andELE22);
   fChain->SetBranchAddress("eT_HadronicTauDataTrigEffAntiEMed", &eT_HadronicTauDataTrigEffAntiEMed, &b_eT_HadronicTauDataTrigEffAntiEMed);
   fChain->SetBranchAddress("eT_HadronicTauMcTrigEffAntiEMed", &eT_HadronicTauMcTrigEffAntiEMed, &b_eT_HadronicTauMcTrigEffAntiEMed);
   fChain->SetBranchAddress("eT_HadronicTauDataTrigEffAntiETight", &eT_HadronicTauDataTrigEffAntiETight, &b_eT_HadronicTauDataTrigEffAntiETight);
   fChain->SetBranchAddress("eT_HadronicTauMcTrigEffAntiETight", &eT_HadronicTauMcTrigEffAntiETight, &b_eT_HadronicTauMcTrigEffAntiETight);
   fChain->SetBranchAddress("eT_electronDataIDweight", &eT_electronDataIDweight, &b_eT_electronDataIDweight);
   fChain->SetBranchAddress("eT_electronMcIDweight", &eT_electronMcIDweight, &b_eT_electronMcIDweight);
   fChain->SetBranchAddress("eT_electronDataISOLweight", &eT_electronDataISOLweight, &b_eT_electronDataISOLweight);
   fChain->SetBranchAddress("eT_electronMcISOLweight", &eT_electronMcISOLweight, &b_eT_electronMcISOLweight);
   fChain->SetBranchAddress("eT_EffDataHighPtTauTrigger", &eT_EffDataHighPtTauTrigger, &b_eT_EffDataHighPtTauTrigger);
   fChain->SetBranchAddress("eT_EffMcHighPtTauTrigger", &eT_EffMcHighPtTauTrigger, &b_eT_EffMcHighPtTauTrigger);
   fChain->SetBranchAddress("eT_TauFakeCorrection", &eT_TauFakeCorrection, &b_eT_TauFakeCorrection);
   fChain->SetBranchAddress("eT_DecayModeCorrectionFactor", &eT_DecayModeCorrectionFactor, &b_eT_DecayModeCorrectionFactor);
   fChain->SetBranchAddress("eT_ZeeScaleFactor", &eT_ZeeScaleFactor, &b_eT_ZeeScaleFactor);
   fChain->SetBranchAddress("eT_nominalHIGLUXHQTmhmax", &eT_nominalHIGLUXHQTmhmax, &b_eT_nominalHIGLUXHQTmhmax);
   fChain->SetBranchAddress("eT_upHIGLUXHQTmhmax", &eT_upHIGLUXHQTmhmax, &b_eT_upHIGLUXHQTmhmax);
   fChain->SetBranchAddress("eT_downHIGLUXHQTmhmax", &eT_downHIGLUXHQTmhmax, &b_eT_downHIGLUXHQTmhmax);
   fChain->SetBranchAddress("eT_nominalPOWHEGmhmod", &eT_nominalPOWHEGmhmod, &b_eT_nominalPOWHEGmhmod);
   fChain->SetBranchAddress("eT_upPOWHEGmhmod", &eT_upPOWHEGmhmod, &b_eT_upPOWHEGmhmod);
   fChain->SetBranchAddress("eT_downPOWHEGmhmod", &eT_downPOWHEGmhmod, &b_eT_downPOWHEGmhmod);
   fChain->SetBranchAddress("eT_upPOWHEGscale", &eT_upPOWHEGscale, &b_eT_upPOWHEGscale);
   fChain->SetBranchAddress("eT_downPOWHEGscale", &eT_downPOWHEGscale, &b_eT_downPOWHEGscale);
   fChain->SetBranchAddress("eT_etaDepQCDShapeTemplateCorrection", &eT_etaDepQCDShapeTemplateCorrection, &b_eT_etaDepQCDShapeTemplateCorrection);
   fChain->SetBranchAddress("eT_inclusiveQCDShapeTemplateCorrection", &eT_inclusiveQCDShapeTemplateCorrection, &b_eT_inclusiveQCDShapeTemplateCorrection);
   fChain->SetBranchAddress("eT_TTbarPtWeight", &eT_TTbarPtWeight, &b_eT_TTbarPtWeight);
   fChain->SetBranchAddress("eT_TauSpinnerWT", &eT_TauSpinnerWT, &b_eT_TauSpinnerWT);
   fChain->SetBranchAddress("eT_TauSpinnerWTFlip", &eT_TauSpinnerWTFlip, &b_eT_TauSpinnerWTFlip);
   fChain->SetBranchAddress("eT_TauSpinnerWThminus", &eT_TauSpinnerWThminus, &b_eT_TauSpinnerWThminus);
   fChain->SetBranchAddress("eT_TauSpinnerWThplus", &eT_TauSpinnerWThplus, &b_eT_TauSpinnerWThplus);
   fChain->SetBranchAddress("eT_hepNUP", &eT_hepNUP, &b_eT_hepNUP);
   fChain->SetBranchAddress("eT_weightHEPNUP_DYJets", &eT_weightHEPNUP_DYJets, &b_eT_weightHEPNUP_DYJets);
   fChain->SetBranchAddress("eT_weightHEPNUP_WJets", &eT_weightHEPNUP_WJets, &b_eT_weightHEPNUP_WJets);
   fChain->SetBranchAddress("eT_passesSecondLeptonVeto", &eT_passesSecondLeptonVeto, &b_eT_passesSecondLeptonVeto);
   fChain->SetBranchAddress("eT_passesThirdLeptonVeto", &eT_passesThirdLeptonVeto, &b_eT_passesThirdLeptonVeto);
   fChain->SetBranchAddress("muT_p4_x", &muT_p4_x, &b_muT_p4_x);
   fChain->SetBranchAddress("muT_p4_y", &muT_p4_y, &b_muT_p4_y);
   fChain->SetBranchAddress("muT_p4_z", &muT_p4_z, &b_muT_p4_z);
   fChain->SetBranchAddress("muT_p4_t", &muT_p4_t, &b_muT_p4_t);
   fChain->SetBranchAddress("muT_corrected_p4_x", &muT_corrected_p4_x, &b_muT_corrected_p4_x);
   fChain->SetBranchAddress("muT_corrected_p4_y", &muT_corrected_p4_y, &b_muT_corrected_p4_y);
   fChain->SetBranchAddress("muT_corrected_p4_z", &muT_corrected_p4_z, &b_muT_corrected_p4_z);
   fChain->SetBranchAddress("muT_corrected_p4_t", &muT_corrected_p4_t, &b_muT_corrected_p4_t);
   fChain->SetBranchAddress("muT_muonIndex", &muT_muonIndex, &b_muT_muonIndex);
   fChain->SetBranchAddress("muT_tauIndex", &muT_tauIndex, &b_muT_tauIndex);
   fChain->SetBranchAddress("muT_scalarSumPt", &muT_scalarSumPt, &b_muT_scalarSumPt);
   fChain->SetBranchAddress("muT_DR", &muT_DR, &b_muT_DR);
   fChain->SetBranchAddress("muT_sumCharge", &muT_sumCharge, &b_muT_sumCharge);
   fChain->SetBranchAddress("muT_correctedSVFitMass", &muT_correctedSVFitMass, &b_muT_correctedSVFitMass);
   fChain->SetBranchAddress("muT_rawSVFitMass", &muT_rawSVFitMass, &b_muT_rawSVFitMass);
   fChain->SetBranchAddress("muT_TransverseMass", &muT_TransverseMass, &b_muT_TransverseMass);
   fChain->SetBranchAddress("muT_rawTransverseMass", &muT_rawTransverseMass, &b_muT_rawTransverseMass);
   fChain->SetBranchAddress("muT_mvaMETraw", &muT_mvaMETraw, &b_muT_mvaMETraw);
   fChain->SetBranchAddress("muT_mvaMET", &muT_mvaMET, &b_muT_mvaMET);
   fChain->SetBranchAddress("muT_mvaMETphiRaw", &muT_mvaMETphiRaw, &b_muT_mvaMETphiRaw);
   fChain->SetBranchAddress("muT_mvaMETphi", &muT_mvaMETphi, &b_muT_mvaMETphi);
   fChain->SetBranchAddress("muT_MAX", &muT_MAX, &b_muT_MAX);
   fChain->SetBranchAddress("muT_isGoodTriggerPair", &muT_isGoodTriggerPair, &b_muT_isGoodTriggerPair);
   fChain->SetBranchAddress("muT_njets", &muT_njets, &b_muT_njets);
   fChain->SetBranchAddress("muT_nbjets", &muT_nbjets, &b_muT_nbjets);
   fChain->SetBranchAddress("muT_nbjetsLOOSE", &muT_nbjetsLOOSE, &b_muT_nbjetsLOOSE);
   fChain->SetBranchAddress("muT_nbjetsLOOSEUP", &muT_nbjetsLOOSEUP, &b_muT_nbjetsLOOSEUP);
   fChain->SetBranchAddress("muT_nbjetsLOOSEDOWN", &muT_nbjetsLOOSEDOWN, &b_muT_nbjetsLOOSEDOWN);
   fChain->SetBranchAddress("muT_njetsUP", &muT_njetsUP, &b_muT_njetsUP);
   fChain->SetBranchAddress("muT_nbjetsUP", &muT_nbjetsUP, &b_muT_nbjetsUP);
   fChain->SetBranchAddress("muT_njetsDOWN", &muT_njetsDOWN, &b_muT_njetsDOWN);
   fChain->SetBranchAddress("muT_nbjetsDOWN", &muT_nbjetsDOWN, &b_muT_nbjetsDOWN);
   fChain->SetBranchAddress("muT_jet1P4_x", &muT_jet1P4_x, &b_muT_jet1P4_x);
   fChain->SetBranchAddress("muT_jet1P4_y", &muT_jet1P4_y, &b_muT_jet1P4_y);
   fChain->SetBranchAddress("muT_jet1P4_z", &muT_jet1P4_z, &b_muT_jet1P4_z);
   fChain->SetBranchAddress("muT_jet1P4_t", &muT_jet1P4_t, &b_muT_jet1P4_t);
   fChain->SetBranchAddress("muT_jet1RawP4_x", &muT_jet1RawP4_x, &b_muT_jet1RawP4_x);
   fChain->SetBranchAddress("muT_jet1RawP4_y", &muT_jet1RawP4_y, &b_muT_jet1RawP4_y);
   fChain->SetBranchAddress("muT_jet1RawP4_z", &muT_jet1RawP4_z, &b_muT_jet1RawP4_z);
   fChain->SetBranchAddress("muT_jet1RawP4_t", &muT_jet1RawP4_t, &b_muT_jet1RawP4_t);
   fChain->SetBranchAddress("muT_jet1IDMVA", &muT_jet1IDMVA, &b_muT_jet1IDMVA);
   fChain->SetBranchAddress("muT_jet1BTAGMVA", &muT_jet1BTAGMVA, &b_muT_jet1BTAGMVA);
   fChain->SetBranchAddress("muT_jet2P4_x", &muT_jet2P4_x, &b_muT_jet2P4_x);
   fChain->SetBranchAddress("muT_jet2P4_y", &muT_jet2P4_y, &b_muT_jet2P4_y);
   fChain->SetBranchAddress("muT_jet2P4_z", &muT_jet2P4_z, &b_muT_jet2P4_z);
   fChain->SetBranchAddress("muT_jet2P4_t", &muT_jet2P4_t, &b_muT_jet2P4_t);
   fChain->SetBranchAddress("muT_jet2RawP4_x", &muT_jet2RawP4_x, &b_muT_jet2RawP4_x);
   fChain->SetBranchAddress("muT_jet2RawP4_y", &muT_jet2RawP4_y, &b_muT_jet2RawP4_y);
   fChain->SetBranchAddress("muT_jet2RawP4_z", &muT_jet2RawP4_z, &b_muT_jet2RawP4_z);
   fChain->SetBranchAddress("muT_jet2RawP4_t", &muT_jet2RawP4_t, &b_muT_jet2RawP4_t);
   fChain->SetBranchAddress("muT_jet2IDMVA", &muT_jet2IDMVA, &b_muT_jet2IDMVA);
   fChain->SetBranchAddress("muT_jet2BTAGMVA", &muT_jet2BTAGMVA, &b_muT_jet2BTAGMVA);
   fChain->SetBranchAddress("muT_cov00", &muT_cov00, &b_muT_cov00);
   fChain->SetBranchAddress("muT_cov01", &muT_cov01, &b_muT_cov01);
   fChain->SetBranchAddress("muT_cov10", &muT_cov10, &b_muT_cov10);
   fChain->SetBranchAddress("muT_cov11", &muT_cov11, &b_muT_cov11);
   fChain->SetBranchAddress("muT_passesTriLeptonVeto", &muT_passesTriLeptonVeto, &b_muT_passesTriLeptonVeto);
   fChain->SetBranchAddress("muT_passNonTopEmbeddedTriggerAndMass50", &muT_passNonTopEmbeddedTriggerAndMass50, &b_muT_passNonTopEmbeddedTriggerAndMass50);
   fChain->SetBranchAddress("muT_passSignalGeneratorMass70to130Cut", &muT_passSignalGeneratorMass70to130Cut, &b_muT_passSignalGeneratorMass70to130Cut);
   fChain->SetBranchAddress("muT_genBosonP4_x", &muT_genBosonP4_x, &b_muT_genBosonP4_x);
   fChain->SetBranchAddress("muT_genBosonP4_y", &muT_genBosonP4_y, &b_muT_genBosonP4_y);
   fChain->SetBranchAddress("muT_genBosonP4_z", &muT_genBosonP4_z, &b_muT_genBosonP4_z);
   fChain->SetBranchAddress("muT_genBosonP4_t", &muT_genBosonP4_t, &b_muT_genBosonP4_t);
   fChain->SetBranchAddress("muT_genTOPp4_x", &muT_genTOPp4_x, &b_muT_genTOPp4_x);
   fChain->SetBranchAddress("muT_genTOPp4_y", &muT_genTOPp4_y, &b_muT_genTOPp4_y);
   fChain->SetBranchAddress("muT_genTOPp4_z", &muT_genTOPp4_z, &b_muT_genTOPp4_z);
   fChain->SetBranchAddress("muT_genTOPp4_t", &muT_genTOPp4_t, &b_muT_genTOPp4_t);
   fChain->SetBranchAddress("muT_genTOPBARp4_x", &muT_genTOPBARp4_x, &b_muT_genTOPBARp4_x);
   fChain->SetBranchAddress("muT_genTOPBARp4_y", &muT_genTOPBARp4_y, &b_muT_genTOPBARp4_y);
   fChain->SetBranchAddress("muT_genTOPBARp4_z", &muT_genTOPBARp4_z, &b_muT_genTOPBARp4_z);
   fChain->SetBranchAddress("muT_genTOPBARp4_t", &muT_genTOPBARp4_t, &b_muT_genTOPBARp4_t);
   fChain->SetBranchAddress("muT_numberOfGoodVertices", &muT_numberOfGoodVertices, &b_muT_numberOfGoodVertices);
   fChain->SetBranchAddress("muT_PVndof", &muT_PVndof, &b_muT_PVndof);
   fChain->SetBranchAddress("muT_PVz", &muT_PVz, &b_muT_PVz);
   fChain->SetBranchAddress("muT_PVpositionRho", &muT_PVpositionRho, &b_muT_PVpositionRho);
   fChain->SetBranchAddress("muT_PVp4_x", &muT_PVp4_x, &b_muT_PVp4_x);
   fChain->SetBranchAddress("muT_PVp4_y", &muT_PVp4_y, &b_muT_PVp4_y);
   fChain->SetBranchAddress("muT_PVp4_z", &muT_PVp4_z, &b_muT_PVp4_z);
   fChain->SetBranchAddress("muT_PVp4_t", &muT_PVp4_t, &b_muT_PVp4_t);
   fChain->SetBranchAddress("muT_isDecayZtauTau", &muT_isDecayZtauTau, &b_muT_isDecayZtauTau);
   fChain->SetBranchAddress("muT_isDecayZeE", &muT_isDecayZeE, &b_muT_isDecayZeE);
   fChain->SetBranchAddress("muT_isDecayZmuMu", &muT_isDecayZmuMu, &b_muT_isDecayZmuMu);
   fChain->SetBranchAddress("muT_isRecoLep_matchedTo_GenTauFromZ", &muT_isRecoLep_matchedTo_GenTauFromZ, &b_muT_isRecoLep_matchedTo_GenTauFromZ);
   fChain->SetBranchAddress("muT_isRecoTau_matchedTo_GenTauFromZ", &muT_isRecoTau_matchedTo_GenTauFromZ, &b_muT_isRecoTau_matchedTo_GenTauFromZ);
   fChain->SetBranchAddress("muT_isRecoLep_matchedTo_GenElecFromZ", &muT_isRecoLep_matchedTo_GenElecFromZ, &b_muT_isRecoLep_matchedTo_GenElecFromZ);
   fChain->SetBranchAddress("muT_isRecoTau_matchedTo_GenElecFromZ", &muT_isRecoTau_matchedTo_GenElecFromZ, &b_muT_isRecoTau_matchedTo_GenElecFromZ);
   fChain->SetBranchAddress("muT_isRecoLep_matchedTo_GenMuonFromZ", &muT_isRecoLep_matchedTo_GenMuonFromZ, &b_muT_isRecoLep_matchedTo_GenMuonFromZ);
   fChain->SetBranchAddress("muT_isRecoTau_matchedTo_GenMuonFromZ", &muT_isRecoTau_matchedTo_GenMuonFromZ, &b_muT_isRecoTau_matchedTo_GenMuonFromZ);
   fChain->SetBranchAddress("muT_isRecoLep_matchedTo_GenElecFromTau", &muT_isRecoLep_matchedTo_GenElecFromTau, &b_muT_isRecoLep_matchedTo_GenElecFromTau);
   fChain->SetBranchAddress("muT_isRecoTau_matchedTo_GenElecFromTau", &muT_isRecoTau_matchedTo_GenElecFromTau, &b_muT_isRecoTau_matchedTo_GenElecFromTau);
   fChain->SetBranchAddress("muT_isRecoLep_matchedTo_GenMuonFromTau", &muT_isRecoLep_matchedTo_GenMuonFromTau, &b_muT_isRecoLep_matchedTo_GenMuonFromTau);
   fChain->SetBranchAddress("muT_isRecoTau_matchedTo_GenMuonFromTau", &muT_isRecoTau_matchedTo_GenMuonFromTau, &b_muT_isRecoTau_matchedTo_GenMuonFromTau);
   fChain->SetBranchAddress("muT_passEmbeddedTrigger", &muT_passEmbeddedTrigger, &b_muT_passEmbeddedTrigger);
   fChain->SetBranchAddress("muT_muon_p4_x", &muT_muon_p4_x, &b_muT_muon_p4_x);
   fChain->SetBranchAddress("muT_muon_p4_y", &muT_muon_p4_y, &b_muT_muon_p4_y);
   fChain->SetBranchAddress("muT_muon_p4_z", &muT_muon_p4_z, &b_muT_muon_p4_z);
   fChain->SetBranchAddress("muT_muon_p4_t", &muT_muon_p4_t, &b_muT_muon_p4_t);
   fChain->SetBranchAddress("muT_muon_pfP4_x", &muT_muon_pfP4_x, &b_muT_muon_pfP4_x);
   fChain->SetBranchAddress("muT_muon_pfP4_y", &muT_muon_pfP4_y, &b_muT_muon_pfP4_y);
   fChain->SetBranchAddress("muT_muon_pfP4_z", &muT_muon_pfP4_z, &b_muT_muon_pfP4_z);
   fChain->SetBranchAddress("muT_muon_pfP4_t", &muT_muon_pfP4_t, &b_muT_muon_pfP4_t);
   fChain->SetBranchAddress("muT_muon_genP4_x", &muT_muon_genP4_x, &b_muT_muon_genP4_x);
   fChain->SetBranchAddress("muT_muon_genP4_y", &muT_muon_genP4_y, &b_muT_muon_genP4_y);
   fChain->SetBranchAddress("muT_muon_genP4_z", &muT_muon_genP4_z, &b_muT_muon_genP4_z);
   fChain->SetBranchAddress("muT_muon_genP4_t", &muT_muon_genP4_t, &b_muT_muon_genP4_t);
   fChain->SetBranchAddress("muT_muon_isGlobalMuon", &muT_muon_isGlobalMuon, &b_muT_muon_isGlobalMuon);
   fChain->SetBranchAddress("muT_muon_isTightMuon", &muT_muon_isTightMuon, &b_muT_muon_isTightMuon);
   fChain->SetBranchAddress("muT_muon_isPFMuon", &muT_muon_isPFMuon, &b_muT_muon_isPFMuon);
   fChain->SetBranchAddress("muT_muon_isLooseMuon", &muT_muon_isLooseMuon, &b_muT_muon_isLooseMuon);
   fChain->SetBranchAddress("muT_muon_sumChargedParticlePt_DR4", &muT_muon_sumChargedParticlePt_DR4, &b_muT_muon_sumChargedParticlePt_DR4);
   fChain->SetBranchAddress("muT_muon_sumPhotonEt_DR4", &muT_muon_sumPhotonEt_DR4, &b_muT_muon_sumPhotonEt_DR4);
   fChain->SetBranchAddress("muT_muon_sumNeutralHadronEt_DR4", &muT_muon_sumNeutralHadronEt_DR4, &b_muT_muon_sumNeutralHadronEt_DR4);
   fChain->SetBranchAddress("muT_muon_sumPUPt_DR4", &muT_muon_sumPUPt_DR4, &b_muT_muon_sumPUPt_DR4);
   fChain->SetBranchAddress("muT_muon_relativeIso_DR4", &muT_muon_relativeIso_DR4, &b_muT_muon_relativeIso_DR4);
   fChain->SetBranchAddress("muT_muon_sumChargedParticlePt_DR3", &muT_muon_sumChargedParticlePt_DR3, &b_muT_muon_sumChargedParticlePt_DR3);
   fChain->SetBranchAddress("muT_muon_sumPhotonEt_DR3", &muT_muon_sumPhotonEt_DR3, &b_muT_muon_sumPhotonEt_DR3);
   fChain->SetBranchAddress("muT_muon_sumNeutralHadronEt_DR3", &muT_muon_sumNeutralHadronEt_DR3, &b_muT_muon_sumNeutralHadronEt_DR3);
   fChain->SetBranchAddress("muT_muon_sumPUPt_DR3", &muT_muon_sumPUPt_DR3, &b_muT_muon_sumPUPt_DR3);
   fChain->SetBranchAddress("muT_muon_relativeIso_DR3", &muT_muon_relativeIso_DR3, &b_muT_muon_relativeIso_DR3);
   fChain->SetBranchAddress("muT_muon_isPFIsolationValid", &muT_muon_isPFIsolationValid, &b_muT_muon_isPFIsolationValid);
   fChain->SetBranchAddress("muT_muon_charge", &muT_muon_charge, &b_muT_muon_charge);
   fChain->SetBranchAddress("muT_muon_PFpdgId", &muT_muon_PFpdgId, &b_muT_muon_PFpdgId);
   fChain->SetBranchAddress("muT_muon_GENpdgId", &muT_muon_GENpdgId, &b_muT_muon_GENpdgId);
   fChain->SetBranchAddress("muT_muon_normalizedChi2", &muT_muon_normalizedChi2, &b_muT_muon_normalizedChi2);
   fChain->SetBranchAddress("muT_muon_numberOfValidMuonHits", &muT_muon_numberOfValidMuonHits, &b_muT_muon_numberOfValidMuonHits);
   fChain->SetBranchAddress("muT_muon_numberOfMatchedStations", &muT_muon_numberOfMatchedStations, &b_muT_muon_numberOfMatchedStations);
   fChain->SetBranchAddress("muT_muon_numberOfValidPixelHits", &muT_muon_numberOfValidPixelHits, &b_muT_muon_numberOfValidPixelHits);
   fChain->SetBranchAddress("muT_muon_trackerLayersWithMeasurement", &muT_muon_trackerLayersWithMeasurement, &b_muT_muon_trackerLayersWithMeasurement);
   fChain->SetBranchAddress("muT_muon_dB", &muT_muon_dB, &b_muT_muon_dB);
   fChain->SetBranchAddress("muT_muon_dz", &muT_muon_dz, &b_muT_muon_dz);
   fChain->SetBranchAddress("muT_muon_dxy", &muT_muon_dxy, &b_muT_muon_dxy);
   fChain->SetBranchAddress("muT_muon_passFullId", &muT_muon_passFullId, &b_muT_muon_passFullId);
   fChain->SetBranchAddress("muT_muon_has_HltMatchMu17", &muT_muon_has_HltMatchMu17, &b_muT_muon_has_HltMatchMu17);
   fChain->SetBranchAddress("muT_muon_has_HltMatchMu18", &muT_muon_has_HltMatchMu18, &b_muT_muon_has_HltMatchMu18);
   fChain->SetBranchAddress("muT_muon_has_HltMatchMu24", &muT_muon_has_HltMatchMu24, &b_muT_muon_has_HltMatchMu24);
   fChain->SetBranchAddress("muT_muon_isTriLeptonVetoCandidate", &muT_muon_isTriLeptonVetoCandidate, &b_muT_muon_isTriLeptonVetoCandidate);
   fChain->SetBranchAddress("muT_muon_isTrackerMuon", &muT_muon_isTrackerMuon, &b_muT_muon_isTrackerMuon);
   fChain->SetBranchAddress("muT_tau_pfJetRefP4_x", &muT_tau_pfJetRefP4_x, &b_muT_tau_pfJetRefP4_x);
   fChain->SetBranchAddress("muT_tau_pfJetRefP4_y", &muT_tau_pfJetRefP4_y, &b_muT_tau_pfJetRefP4_y);
   fChain->SetBranchAddress("muT_tau_pfJetRefP4_z", &muT_tau_pfJetRefP4_z, &b_muT_tau_pfJetRefP4_z);
   fChain->SetBranchAddress("muT_tau_pfJetRefP4_t", &muT_tau_pfJetRefP4_t, &b_muT_tau_pfJetRefP4_t);
   fChain->SetBranchAddress("muT_tau_p4_x", &muT_tau_p4_x, &b_muT_tau_p4_x);
   fChain->SetBranchAddress("muT_tau_p4_y", &muT_tau_p4_y, &b_muT_tau_p4_y);
   fChain->SetBranchAddress("muT_tau_p4_z", &muT_tau_p4_z, &b_muT_tau_p4_z);
   fChain->SetBranchAddress("muT_tau_p4_t", &muT_tau_p4_t, &b_muT_tau_p4_t);
   fChain->SetBranchAddress("muT_tau_genP4_x", &muT_tau_genP4_x, &b_muT_tau_genP4_x);
   fChain->SetBranchAddress("muT_tau_genP4_y", &muT_tau_genP4_y, &b_muT_tau_genP4_y);
   fChain->SetBranchAddress("muT_tau_genP4_z", &muT_tau_genP4_z, &b_muT_tau_genP4_z);
   fChain->SetBranchAddress("muT_tau_genP4_t", &muT_tau_genP4_t, &b_muT_tau_genP4_t);
   fChain->SetBranchAddress("muT_tau_genJet_x", &muT_tau_genJet_x, &b_muT_tau_genJet_x);
   fChain->SetBranchAddress("muT_tau_genJet_y", &muT_tau_genJet_y, &b_muT_tau_genJet_y);
   fChain->SetBranchAddress("muT_tau_genJet_z", &muT_tau_genJet_z, &b_muT_tau_genJet_z);
   fChain->SetBranchAddress("muT_tau_genJet_t", &muT_tau_genJet_t, &b_muT_tau_genJet_t);
   fChain->SetBranchAddress("muT_tau_corrected_p4_x", &muT_tau_corrected_p4_x, &b_muT_tau_corrected_p4_x);
   fChain->SetBranchAddress("muT_tau_corrected_p4_y", &muT_tau_corrected_p4_y, &b_muT_tau_corrected_p4_y);
   fChain->SetBranchAddress("muT_tau_corrected_p4_z", &muT_tau_corrected_p4_z, &b_muT_tau_corrected_p4_z);
   fChain->SetBranchAddress("muT_tau_corrected_p4_t", &muT_tau_corrected_p4_t, &b_muT_tau_corrected_p4_t);
   fChain->SetBranchAddress("muT_tau_pdgId", &muT_tau_pdgId, &b_muT_tau_pdgId);
   fChain->SetBranchAddress("muT_tau_pdgIdGEN", &muT_tau_pdgIdGEN, &b_muT_tau_pdgIdGEN);
   fChain->SetBranchAddress("muT_tau_charge", &muT_tau_charge, &b_muT_tau_charge);
   fChain->SetBranchAddress("muT_tau_decayMode", &muT_tau_decayMode, &b_muT_tau_decayMode);
   fChain->SetBranchAddress("muT_tau_passFullId_muTau", &muT_tau_passFullId_muTau, &b_muT_tau_passFullId_muTau);
   fChain->SetBranchAddress("muT_tau_passFullId_eTau", &muT_tau_passFullId_eTau, &b_muT_tau_passFullId_eTau);
   fChain->SetBranchAddress("muT_tau_numStrips", &muT_tau_numStrips, &b_muT_tau_numStrips);
   fChain->SetBranchAddress("muT_tau_numHadrons", &muT_tau_numHadrons, &b_muT_tau_numHadrons);
   fChain->SetBranchAddress("muT_tau_againstElectronDeadECAL", &muT_tau_againstElectronDeadECAL, &b_muT_tau_againstElectronDeadECAL);
   fChain->SetBranchAddress("muT_tau_againstElectronLoose", &muT_tau_againstElectronLoose, &b_muT_tau_againstElectronLoose);
   fChain->SetBranchAddress("muT_tau_againstElectronLooseMVA5", &muT_tau_againstElectronLooseMVA5, &b_muT_tau_againstElectronLooseMVA5);
   fChain->SetBranchAddress("muT_tau_againstElectronMVA5category", &muT_tau_againstElectronMVA5category, &b_muT_tau_againstElectronMVA5category);
   fChain->SetBranchAddress("muT_tau_againstElectronMVA5raw", &muT_tau_againstElectronMVA5raw, &b_muT_tau_againstElectronMVA5raw);
   fChain->SetBranchAddress("muT_tau_againstElectronMedium", &muT_tau_againstElectronMedium, &b_muT_tau_againstElectronMedium);
   fChain->SetBranchAddress("muT_tau_againstElectronMediumMVA5", &muT_tau_againstElectronMediumMVA5, &b_muT_tau_againstElectronMediumMVA5);
   fChain->SetBranchAddress("muT_tau_againstElectronTight", &muT_tau_againstElectronTight, &b_muT_tau_againstElectronTight);
   fChain->SetBranchAddress("muT_tau_againstElectronTightMVA5", &muT_tau_againstElectronTightMVA5, &b_muT_tau_againstElectronTightMVA5);
   fChain->SetBranchAddress("muT_tau_againstElectronVLooseMVA5", &muT_tau_againstElectronVLooseMVA5, &b_muT_tau_againstElectronVLooseMVA5);
   fChain->SetBranchAddress("muT_tau_againstElectronVTightMVA5", &muT_tau_againstElectronVTightMVA5, &b_muT_tau_againstElectronVTightMVA5);
   fChain->SetBranchAddress("muT_tau_againstMuonLoose", &muT_tau_againstMuonLoose, &b_muT_tau_againstMuonLoose);
   fChain->SetBranchAddress("muT_tau_againstMuonLoose2", &muT_tau_againstMuonLoose2, &b_muT_tau_againstMuonLoose2);
   fChain->SetBranchAddress("muT_tau_againstMuonLoose3", &muT_tau_againstMuonLoose3, &b_muT_tau_againstMuonLoose3);
   fChain->SetBranchAddress("muT_tau_againstMuonLooseMVA", &muT_tau_againstMuonLooseMVA, &b_muT_tau_againstMuonLooseMVA);
   fChain->SetBranchAddress("muT_tau_againstMuonMVAraw", &muT_tau_againstMuonMVAraw, &b_muT_tau_againstMuonMVAraw);
   fChain->SetBranchAddress("muT_tau_againstMuonMedium", &muT_tau_againstMuonMedium, &b_muT_tau_againstMuonMedium);
   fChain->SetBranchAddress("muT_tau_againstMuonMedium2", &muT_tau_againstMuonMedium2, &b_muT_tau_againstMuonMedium2);
   fChain->SetBranchAddress("muT_tau_againstMuonMediumMVA", &muT_tau_againstMuonMediumMVA, &b_muT_tau_againstMuonMediumMVA);
   fChain->SetBranchAddress("muT_tau_againstMuonTight", &muT_tau_againstMuonTight, &b_muT_tau_againstMuonTight);
   fChain->SetBranchAddress("muT_tau_againstMuonTight2", &muT_tau_againstMuonTight2, &b_muT_tau_againstMuonTight2);
   fChain->SetBranchAddress("muT_tau_againstMuonTight3", &muT_tau_againstMuonTight3, &b_muT_tau_againstMuonTight3);
   fChain->SetBranchAddress("muT_tau_againstMuonTightMVA", &muT_tau_againstMuonTightMVA, &b_muT_tau_againstMuonTightMVA);
   fChain->SetBranchAddress("muT_tau_byCombinedIsolationDeltaBetaCorrRaw", &muT_tau_byCombinedIsolationDeltaBetaCorrRaw, &b_muT_tau_byCombinedIsolationDeltaBetaCorrRaw);
   fChain->SetBranchAddress("muT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits", &muT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits, &b_muT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits);
   fChain->SetBranchAddress("muT_tau_byIsolationMVA3newDMwLTraw", &muT_tau_byIsolationMVA3newDMwLTraw, &b_muT_tau_byIsolationMVA3newDMwLTraw);
   fChain->SetBranchAddress("muT_tau_byIsolationMVA3newDMwoLTraw", &muT_tau_byIsolationMVA3newDMwoLTraw, &b_muT_tau_byIsolationMVA3newDMwoLTraw);
   fChain->SetBranchAddress("muT_tau_byIsolationMVA3oldDMwLTraw", &muT_tau_byIsolationMVA3oldDMwLTraw, &b_muT_tau_byIsolationMVA3oldDMwLTraw);
   fChain->SetBranchAddress("muT_tau_byIsolationMVA3oldDMwoLTraw", &muT_tau_byIsolationMVA3oldDMwoLTraw, &b_muT_tau_byIsolationMVA3oldDMwoLTraw);
   fChain->SetBranchAddress("muT_tau_byLooseCombinedIsolationDeltaBetaCorr", &muT_tau_byLooseCombinedIsolationDeltaBetaCorr, &b_muT_tau_byLooseCombinedIsolationDeltaBetaCorr);
   fChain->SetBranchAddress("muT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits", &muT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits, &b_muT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits);
   fChain->SetBranchAddress("muT_tau_byLooseIsolation", &muT_tau_byLooseIsolation, &b_muT_tau_byLooseIsolation);
   fChain->SetBranchAddress("muT_tau_byLooseIsolationMVA3newDMwLT", &muT_tau_byLooseIsolationMVA3newDMwLT, &b_muT_tau_byLooseIsolationMVA3newDMwLT);
   fChain->SetBranchAddress("muT_tau_byLooseIsolationMVA3newDMwoLT", &muT_tau_byLooseIsolationMVA3newDMwoLT, &b_muT_tau_byLooseIsolationMVA3newDMwoLT);
   fChain->SetBranchAddress("muT_tau_byLooseIsolationMVA3oldDMwLT", &muT_tau_byLooseIsolationMVA3oldDMwLT, &b_muT_tau_byLooseIsolationMVA3oldDMwLT);
   fChain->SetBranchAddress("muT_tau_byLooseIsolationMVA3oldDMwoLT", &muT_tau_byLooseIsolationMVA3oldDMwoLT, &b_muT_tau_byLooseIsolationMVA3oldDMwoLT);
   fChain->SetBranchAddress("muT_tau_byMediumCombinedIsolationDeltaBetaCorr", &muT_tau_byMediumCombinedIsolationDeltaBetaCorr, &b_muT_tau_byMediumCombinedIsolationDeltaBetaCorr);
   fChain->SetBranchAddress("muT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits", &muT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits, &b_muT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits);
   fChain->SetBranchAddress("muT_tau_byMediumIsolationMVA3newDMwLT", &muT_tau_byMediumIsolationMVA3newDMwLT, &b_muT_tau_byMediumIsolationMVA3newDMwLT);
   fChain->SetBranchAddress("muT_tau_byMediumIsolationMVA3newDMwoLT", &muT_tau_byMediumIsolationMVA3newDMwoLT, &b_muT_tau_byMediumIsolationMVA3newDMwoLT);
   fChain->SetBranchAddress("muT_tau_byMediumIsolationMVA3oldDMwLT", &muT_tau_byMediumIsolationMVA3oldDMwLT, &b_muT_tau_byMediumIsolationMVA3oldDMwLT);
   fChain->SetBranchAddress("muT_tau_byMediumIsolationMVA3oldDMwoLT", &muT_tau_byMediumIsolationMVA3oldDMwoLT, &b_muT_tau_byMediumIsolationMVA3oldDMwoLT);
   fChain->SetBranchAddress("muT_tau_byTightCombinedIsolationDeltaBetaCorr", &muT_tau_byTightCombinedIsolationDeltaBetaCorr, &b_muT_tau_byTightCombinedIsolationDeltaBetaCorr);
   fChain->SetBranchAddress("muT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits", &muT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits, &b_muT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits);
   fChain->SetBranchAddress("muT_tau_byTightIsolationMVA3newDMwLT", &muT_tau_byTightIsolationMVA3newDMwLT, &b_muT_tau_byTightIsolationMVA3newDMwLT);
   fChain->SetBranchAddress("muT_tau_byTightIsolationMVA3newDMwoLT", &muT_tau_byTightIsolationMVA3newDMwoLT, &b_muT_tau_byTightIsolationMVA3newDMwoLT);
   fChain->SetBranchAddress("muT_tau_byTightIsolationMVA3oldDMwLT", &muT_tau_byTightIsolationMVA3oldDMwLT, &b_muT_tau_byTightIsolationMVA3oldDMwLT);
   fChain->SetBranchAddress("muT_tau_byTightIsolationMVA3oldDMwoLT", &muT_tau_byTightIsolationMVA3oldDMwoLT, &b_muT_tau_byTightIsolationMVA3oldDMwoLT);
   fChain->SetBranchAddress("muT_tau_byVLooseCombinedIsolationDeltaBetaCorr", &muT_tau_byVLooseCombinedIsolationDeltaBetaCorr, &b_muT_tau_byVLooseCombinedIsolationDeltaBetaCorr);
   fChain->SetBranchAddress("muT_tau_byVLooseIsolationMVA3newDMwLT", &muT_tau_byVLooseIsolationMVA3newDMwLT, &b_muT_tau_byVLooseIsolationMVA3newDMwLT);
   fChain->SetBranchAddress("muT_tau_byVLooseIsolationMVA3newDMwoLT", &muT_tau_byVLooseIsolationMVA3newDMwoLT, &b_muT_tau_byVLooseIsolationMVA3newDMwoLT);
   fChain->SetBranchAddress("muT_tau_byVLooseIsolationMVA3oldDMwLT", &muT_tau_byVLooseIsolationMVA3oldDMwLT, &b_muT_tau_byVLooseIsolationMVA3oldDMwLT);
   fChain->SetBranchAddress("muT_tau_byVLooseIsolationMVA3oldDMwoLT", &muT_tau_byVLooseIsolationMVA3oldDMwoLT, &b_muT_tau_byVLooseIsolationMVA3oldDMwoLT);
   fChain->SetBranchAddress("muT_tau_byVTightIsolationMVA3newDMwLT", &muT_tau_byVTightIsolationMVA3newDMwLT, &b_muT_tau_byVTightIsolationMVA3newDMwLT);
   fChain->SetBranchAddress("muT_tau_byVTightIsolationMVA3newDMwoLT", &muT_tau_byVTightIsolationMVA3newDMwoLT, &b_muT_tau_byVTightIsolationMVA3newDMwoLT);
   fChain->SetBranchAddress("muT_tau_byVTightIsolationMVA3oldDMwLT", &muT_tau_byVTightIsolationMVA3oldDMwLT, &b_muT_tau_byVTightIsolationMVA3oldDMwLT);
   fChain->SetBranchAddress("muT_tau_byVTightIsolationMVA3oldDMwoLT", &muT_tau_byVTightIsolationMVA3oldDMwoLT, &b_muT_tau_byVTightIsolationMVA3oldDMwoLT);
   fChain->SetBranchAddress("muT_tau_byVVTightIsolationMVA3newDMwLT", &muT_tau_byVVTightIsolationMVA3newDMwLT, &b_muT_tau_byVVTightIsolationMVA3newDMwLT);
   fChain->SetBranchAddress("muT_tau_byVVTightIsolationMVA3newDMwoLT", &muT_tau_byVVTightIsolationMVA3newDMwoLT, &b_muT_tau_byVVTightIsolationMVA3newDMwoLT);
   fChain->SetBranchAddress("muT_tau_byVVTightIsolationMVA3oldDMwLT", &muT_tau_byVVTightIsolationMVA3oldDMwLT, &b_muT_tau_byVVTightIsolationMVA3oldDMwLT);
   fChain->SetBranchAddress("muT_tau_byVVTightIsolationMVA3oldDMwoLT", &muT_tau_byVVTightIsolationMVA3oldDMwoLT, &b_muT_tau_byVVTightIsolationMVA3oldDMwoLT);
   fChain->SetBranchAddress("muT_tau_chargedIsoPtSum", &muT_tau_chargedIsoPtSum, &b_muT_tau_chargedIsoPtSum);
   fChain->SetBranchAddress("muT_tau_decayModeFinding", &muT_tau_decayModeFinding, &b_muT_tau_decayModeFinding);
   fChain->SetBranchAddress("muT_tau_decayModeFindingNewDMs", &muT_tau_decayModeFindingNewDMs, &b_muT_tau_decayModeFindingNewDMs);
   fChain->SetBranchAddress("muT_tau_decayModeFindingOldDMs", &muT_tau_decayModeFindingOldDMs, &b_muT_tau_decayModeFindingOldDMs);
   fChain->SetBranchAddress("muT_tau_neutralIsoPtSum", &muT_tau_neutralIsoPtSum, &b_muT_tau_neutralIsoPtSum);
   fChain->SetBranchAddress("muT_tau_puCorrPtSum", &muT_tau_puCorrPtSum, &b_muT_tau_puCorrPtSum);
   fChain->SetBranchAddress("muT_tau_has_HltMatchEle20", &muT_tau_has_HltMatchEle20, &b_muT_tau_has_HltMatchEle20);
   fChain->SetBranchAddress("muT_tau_has_HltMatchEle22", &muT_tau_has_HltMatchEle22, &b_muT_tau_has_HltMatchEle22);
   fChain->SetBranchAddress("muT_tau_has_HltMatchEle27", &muT_tau_has_HltMatchEle27, &b_muT_tau_has_HltMatchEle27);
   fChain->SetBranchAddress("muT_tau_has_HltMatchMu17", &muT_tau_has_HltMatchMu17, &b_muT_tau_has_HltMatchMu17);
   fChain->SetBranchAddress("muT_tau_has_HltMatchMu18", &muT_tau_has_HltMatchMu18, &b_muT_tau_has_HltMatchMu18);
   fChain->SetBranchAddress("muT_tau_has_HltMatchMu24", &muT_tau_has_HltMatchMu24, &b_muT_tau_has_HltMatchMu24);
   fChain->SetBranchAddress("muT_puWeight", &muT_puWeight, &b_muT_puWeight);
   fChain->SetBranchAddress("muT_puWeightM1", &muT_puWeightM1, &b_muT_puWeightM1);
   fChain->SetBranchAddress("muT_puWeightP1", &muT_puWeightP1, &b_muT_puWeightP1);
   fChain->SetBranchAddress("muT_NumPileupInt", &muT_NumPileupInt, &b_muT_NumPileupInt);
   fChain->SetBranchAddress("muT_NumTruePileUpInt", &muT_NumTruePileUpInt, &b_muT_NumTruePileUpInt);
   fChain->SetBranchAddress("muT_NumPileupIntM1", &muT_NumPileupIntM1, &b_muT_NumPileupIntM1);
   fChain->SetBranchAddress("muT_NumTruePileUpIntM1", &muT_NumTruePileUpIntM1, &b_muT_NumTruePileUpIntM1);
   fChain->SetBranchAddress("muT_NumPileupIntP1", &muT_NumPileupIntP1, &b_muT_NumPileupIntP1);
   fChain->SetBranchAddress("muT_NumTruePileUpIntP1", &muT_NumTruePileUpIntP1, &b_muT_NumTruePileUpIntP1);
   fChain->SetBranchAddress("muT_EffDataISOMU17andISOMU18", &muT_EffDataISOMU17andISOMU18, &b_muT_EffDataISOMU17andISOMU18);
   fChain->SetBranchAddress("muT_EffMcISOMU17andISOMU18", &muT_EffMcISOMU17andISOMU18, &b_muT_EffMcISOMU17andISOMU18);
   fChain->SetBranchAddress("muT_HadronicTauDataTrigEffAntiMuMed", &muT_HadronicTauDataTrigEffAntiMuMed, &b_muT_HadronicTauDataTrigEffAntiMuMed);
   fChain->SetBranchAddress("muT_HadronicTauMcTrigEffAntiMuMed", &muT_HadronicTauMcTrigEffAntiMuMed, &b_muT_HadronicTauMcTrigEffAntiMuMed);
   fChain->SetBranchAddress("muT_muonDataIDweight", &muT_muonDataIDweight, &b_muT_muonDataIDweight);
   fChain->SetBranchAddress("muT_muonMcIDweight", &muT_muonMcIDweight, &b_muT_muonMcIDweight);
   fChain->SetBranchAddress("muT_muonDataISOLweight", &muT_muonDataISOLweight, &b_muT_muonDataISOLweight);
   fChain->SetBranchAddress("muT_muonMcISOLweight", &muT_muonMcISOLweight, &b_muT_muonMcISOLweight);
   fChain->SetBranchAddress("muT_EffDataHighPtTauTrigger", &muT_EffDataHighPtTauTrigger, &b_muT_EffDataHighPtTauTrigger);
   fChain->SetBranchAddress("muT_EffMcHighPtTauTrigger", &muT_EffMcHighPtTauTrigger, &b_muT_EffMcHighPtTauTrigger);
   fChain->SetBranchAddress("muT_TauFakeCorrection", &muT_TauFakeCorrection, &b_muT_TauFakeCorrection);
   fChain->SetBranchAddress("muT_DecayModeCorrectionFactor", &muT_DecayModeCorrectionFactor, &b_muT_DecayModeCorrectionFactor);
   fChain->SetBranchAddress("muT_nominalHIGLUXHQTmhmax", &muT_nominalHIGLUXHQTmhmax, &b_muT_nominalHIGLUXHQTmhmax);
   fChain->SetBranchAddress("muT_upHIGLUXHQTmhmax", &muT_upHIGLUXHQTmhmax, &b_muT_upHIGLUXHQTmhmax);
   fChain->SetBranchAddress("muT_downHIGLUXHQTmhmax", &muT_downHIGLUXHQTmhmax, &b_muT_downHIGLUXHQTmhmax);
   fChain->SetBranchAddress("muT_nominalPOWHEGmhmod", &muT_nominalPOWHEGmhmod, &b_muT_nominalPOWHEGmhmod);
   fChain->SetBranchAddress("muT_upPOWHEGmhmod", &muT_upPOWHEGmhmod, &b_muT_upPOWHEGmhmod);
   fChain->SetBranchAddress("muT_downPOWHEGmhmod", &muT_downPOWHEGmhmod, &b_muT_downPOWHEGmhmod);
   fChain->SetBranchAddress("muT_upPOWHEGscale", &muT_upPOWHEGscale, &b_muT_upPOWHEGscale);
   fChain->SetBranchAddress("muT_downPOWHEGscale", &muT_downPOWHEGscale, &b_muT_downPOWHEGscale);
   fChain->SetBranchAddress("muT_etaDepQCDShapeTemplateCorrection", &muT_etaDepQCDShapeTemplateCorrection, &b_muT_etaDepQCDShapeTemplateCorrection);
   fChain->SetBranchAddress("muT_inclusiveQCDShapeTemplateCorrection", &muT_inclusiveQCDShapeTemplateCorrection, &b_muT_inclusiveQCDShapeTemplateCorrection);
   fChain->SetBranchAddress("muT_TTbarPtWeight", &muT_TTbarPtWeight, &b_muT_TTbarPtWeight);
   fChain->SetBranchAddress("muT_TauSpinnerWT", &muT_TauSpinnerWT, &b_muT_TauSpinnerWT);
   fChain->SetBranchAddress("muT_TauSpinnerWTFlip", &muT_TauSpinnerWTFlip, &b_muT_TauSpinnerWTFlip);
   fChain->SetBranchAddress("muT_TauSpinnerWThminus", &muT_TauSpinnerWThminus, &b_muT_TauSpinnerWThminus);
   fChain->SetBranchAddress("muT_TauSpinnerWThplus", &muT_TauSpinnerWThplus, &b_muT_TauSpinnerWThplus);
   fChain->SetBranchAddress("muT_hepNUP", &muT_hepNUP, &b_muT_hepNUP);
   fChain->SetBranchAddress("muT_weightHEPNUP_DYJets", &muT_weightHEPNUP_DYJets, &b_muT_weightHEPNUP_DYJets);
   fChain->SetBranchAddress("muT_weightHEPNUP_WJets", &muT_weightHEPNUP_WJets, &b_muT_weightHEPNUP_WJets);
   fChain->SetBranchAddress("muT_passesSecondLeptonVeto", &muT_passesSecondLeptonVeto, &b_muT_passesSecondLeptonVeto);
   fChain->SetBranchAddress("muT_passesThirdLeptonVeto", &muT_passesThirdLeptonVeto, &b_muT_passesThirdLeptonVeto);
   fChain->SetBranchAddress("eT_embedWeight", &eT_embedWeight, &eT_embedWeight);
   fChain->SetBranchAddress("muT_embedWeight", &muT_embedWeight, &muT_embedWeight);



}
