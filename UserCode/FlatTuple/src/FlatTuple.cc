// -*- C++ -*-
//
// Package:    FlatTuple
// Class:      FlatTuple
//
/**\class FlatTuple FlatTuple.cc TEMP/FlatTuple/src/FlatTuple.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Tue Jul  1 04:25:53 CDT 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "UserCode/TupleObjects/interface/TupleElectron.h"
#include "UserCode/TupleObjects/interface/TupleMuon.h"
#include "UserCode/TupleObjects/interface/TupleTau.h"
#include "UserCode/TupleObjects/interface/TupleElectronTau.h"
#include "UserCode/TupleObjects/interface/TupleMuonTau.h"
#include "UserCode/TupleObjects/interface/TupleElectronTauWeight.h"


#include <string>
#include "TTree.h"
#include "TFile.h"

using namespace edm;
using namespace std;

typedef math::XYZTLorentzVector LorentzVector;

//
// class declaration
//

class FlatTuple : public edm::EDAnalyzer
{
public:
  explicit FlatTuple(const edm::ParameterSet&);
  ~FlatTuple();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void reInit();

  // ----------member data ---------------------------


  edm::InputTag electronTauSrc_;
  edm::InputTag electronSrc_;
  edm::InputTag tauSrc_;
  edm::InputTag electronTauWtSrc_;

  edm::InputTag muonTauSrc_;
  std::string NAME_;


  TFile *outFile;
  TTree *lepTauTree;

  //////////////
  // variables for lepTau tree

  ///////
  // corresponding to electronTau object

  std::vector< double > eT_p4_x , eT_p4_y , eT_p4_z , eT_p4_t ;
  std::vector< double > eT_corrected_p4_x , eT_corrected_p4_y , eT_corrected_p4_z , eT_corrected_p4_t ;
  std::vector< int > eT_electronIndex ;
  std::vector< int > eT_tauIndex ;
  std::vector< double > eT_scalarSumPt ;
  std::vector< double > eT_DR ;
  std::vector< int > eT_sumCharge ;
  std::vector< double > eT_correctedSVFitMass ;
  std::vector< double > eT_rawSVFitMass ;
  std::vector< double > eT_TransverseMass ;
  std::vector< double > eT_rawTransverseMass ;
  std::vector< double > eT_mvaMETraw ;
  std::vector< double > eT_mvaMET ;
  std::vector< double > eT_mvaMETphiRaw ;
  std::vector< double > eT_mvaMETphi ;
  std::vector< int > eT_MAX ;
  std::vector< bool > eT_isGoodTriggerPair ;
  std::vector< int > eT_njets ;
  std::vector< int > eT_nbjets ;
  std::vector< double > eT_jet1P4_x , eT_jet1P4_y , eT_jet1P4_z , eT_jet1P4_t ;
  std::vector< double > eT_jet1RawP4_x , eT_jet1RawP4_y , eT_jet1RawP4_z , eT_jet1RawP4_t ;
  std::vector< double > eT_jet1IDMVA ;
  std::vector< double > eT_jet1BTAGMVA ;
  std::vector< double > eT_jet2P4_x , eT_jet2P4_y , eT_jet2P4_z , eT_jet2P4_t ;
  std::vector< double > eT_jet2RawP4_x , eT_jet2RawP4_y , eT_jet2RawP4_z , eT_jet2RawP4_t ;
  std::vector< double > eT_jet2IDMVA ;
  std::vector< double > eT_jet2BTAGMVA ;
  std::vector< double > eT_cov00 ;
  std::vector< double > eT_cov01 ;
  std::vector< double > eT_cov10 ;
  std::vector< double > eT_cov11 ;
  std::vector< bool > eT_passesTriLeptonVeto ;
  std::vector< bool > eT_passNonTopEmbeddedTriggerAndMass50 ;
  std::vector< bool > eT_passSignalGeneratorMass70to130Cut ;
  std::vector< double > eT_genBosonP4_x , eT_genBosonP4_y , eT_genBosonP4_z , eT_genBosonP4_t ;
  std::vector< double > eT_genTOPp4_x , eT_genTOPp4_y , eT_genTOPp4_z , eT_genTOPp4_t ;
  std::vector< double > eT_genTOPBARp4_x , eT_genTOPBARp4_y , eT_genTOPBARp4_z , eT_genTOPBARp4_t ;
  std::vector< int > eT_numberOfGoodVertices ;
  std::vector< int > eT_PVndof ;
  std::vector< double > eT_PVz ;
  std::vector< double > eT_PVpositionRho ;
  std::vector< double > eT_PVp4_x , eT_PVp4_y , eT_PVp4_z , eT_PVp4_t ;


  ////////////////
  // corresponding to electrons in eTau pairs

  std::vector< double > eT_ele_p4_x , eT_ele_p4_y , eT_ele_p4_z , eT_ele_p4_t ;
  std::vector< double > eT_ele_genP4_x , eT_ele_genP4_y , eT_ele_genP4_z , eT_ele_genP4_t ;
  std::vector< double > eT_ele_pfP4_x , eT_ele_pfP4_y , eT_ele_pfP4_z , eT_ele_pfP4_t ;
  std::vector< int > eT_ele_charge ;
  std::vector< int > eT_ele_PFpdgId ;
  std::vector< int > eT_ele_GENpdgId ;
  std::vector< int > eT_ele_numberOfMissingInnerHits ;
  std::vector< bool > eT_ele_passConversionVeto ;
  std::vector< double > eT_ele_dz ;
  std::vector< double > eT_ele_dB ;
  std::vector< double > eT_ele_dxy ;
  std::vector< double > eT_ele_SuperClusterEta ;
  std::vector< double > eT_ele_mvaTrigV0 ;
  std::vector< double > eT_ele_mvaTrigNoIPV0 ;
  std::vector< double > eT_ele_mvaNonTrigV0 ;
  std::vector< bool > eT_ele_pass_tight_mvaNonTrigV0 ;
  std::vector< bool > eT_ele_passFullId ;
  std::vector< double > eT_ele_chargedHadronIso ;
  std::vector< double > eT_ele_photonIso ;
  std::vector< double > eT_ele_neutralHadronIso ;
  std::vector< double > eT_ele_puChargedHadronIso ;
  std::vector< double > eT_ele_relativeIso ;
  std::vector< bool > eT_ele_isEB ;
  std::vector< bool > eT_ele_isEE ;
  std::vector< bool > eT_ele_isEBEEGap ;
  std::vector< bool > eT_ele_isEBEtaGap ;
  std::vector< bool > eT_ele_isEBPhiGap ;
  std::vector< bool > eT_ele_isEEDeeGap ;
  std::vector< bool > eT_ele_isEERingGap ;
  std::vector< double > eT_ele_sigmaEtaEta ;
  std::vector< double > eT_ele_sigmaIetaIeta ;
  std::vector< double > eT_ele_sigmaIphiIphi ;
  std::vector< bool > eT_ele_has_HltMatchEle20 ;
  std::vector< bool > eT_ele_has_HltMatchEle22 ;
  std::vector< bool > eT_ele_has_HltMatchEle27 ;
  std::vector< bool > eT_ele_isTriLeptonVetoCandidate ;

  //////////////////
  // the tau leg in eTau

  std::vector< double > eT_tau_pfJetRefP4_x , eT_tau_pfJetRefP4_y , eT_tau_pfJetRefP4_z , eT_tau_pfJetRefP4_t ;
  std::vector< double > eT_tau_p4_x , eT_tau_p4_y , eT_tau_p4_z , eT_tau_p4_t ;
  std::vector< double > eT_tau_genP4_x , eT_tau_genP4_y , eT_tau_genP4_z , eT_tau_genP4_t ;
  std::vector< double > eT_tau_genJet_x , eT_tau_genJet_y , eT_tau_genJet_z , eT_tau_genJet_t ;
  std::vector< double > eT_tau_corrected_p4_x , eT_tau_corrected_p4_y , eT_tau_corrected_p4_z , eT_tau_corrected_p4_t ;
  std::vector< int > eT_tau_pdgId ;
  std::vector< int > eT_tau_pdgIdGEN ;
  std::vector< int > eT_tau_charge ;
  std::vector< int > eT_tau_decayMode ;
  std::vector< bool > eT_tau_passFullId_muTau ;
  std::vector< bool > eT_tau_passFullId_eTau ;
  std::vector< int > eT_tau_numStrips ;
  std::vector< int > eT_tau_numHadrons ;
  std::vector< float > eT_tau_againstElectronDeadECAL ;
  std::vector< float > eT_tau_againstElectronLoose ;
  std::vector< float > eT_tau_againstElectronLooseMVA5 ;
  std::vector< float > eT_tau_againstElectronMVA5category ;
  std::vector< float > eT_tau_againstElectronMVA5raw ;
  std::vector< float > eT_tau_againstElectronMedium ;
  std::vector< float > eT_tau_againstElectronMediumMVA5 ;
  std::vector< float > eT_tau_againstElectronTight ;
  std::vector< float > eT_tau_againstElectronTightMVA5 ;
  std::vector< float > eT_tau_againstElectronVLooseMVA5 ;
  std::vector< float > eT_tau_againstElectronVTightMVA5 ;
  std::vector< float > eT_tau_againstMuonLoose ;
  std::vector< float > eT_tau_againstMuonLoose2 ;
  std::vector< float > eT_tau_againstMuonLoose3 ;
  std::vector< float > eT_tau_againstMuonLooseMVA ;
  std::vector< float > eT_tau_againstMuonMVAraw ;
  std::vector< float > eT_tau_againstMuonMedium ;
  std::vector< float > eT_tau_againstMuonMedium2 ;
  std::vector< float > eT_tau_againstMuonMediumMVA ;
  std::vector< float > eT_tau_againstMuonTight ;
  std::vector< float > eT_tau_againstMuonTight2 ;
  std::vector< float > eT_tau_againstMuonTight3 ;
  std::vector< float > eT_tau_againstMuonTightMVA ;
  std::vector< float > eT_tau_byCombinedIsolationDeltaBetaCorrRaw ;
  std::vector< float > eT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits ;
  std::vector< float > eT_tau_byIsolationMVA3newDMwLTraw ;
  std::vector< float > eT_tau_byIsolationMVA3newDMwoLTraw ;
  std::vector< float > eT_tau_byIsolationMVA3oldDMwLTraw ;
  std::vector< float > eT_tau_byIsolationMVA3oldDMwoLTraw ;
  std::vector< float > eT_tau_byLooseCombinedIsolationDeltaBetaCorr ;
  std::vector< float > eT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits ;
  std::vector< float > eT_tau_byLooseIsolation ;
  std::vector< float > eT_tau_byLooseIsolationMVA3newDMwLT ;
  std::vector< float > eT_tau_byLooseIsolationMVA3newDMwoLT ;
  std::vector< float > eT_tau_byLooseIsolationMVA3oldDMwLT ;
  std::vector< float > eT_tau_byLooseIsolationMVA3oldDMwoLT ;
  std::vector< float > eT_tau_byMediumCombinedIsolationDeltaBetaCorr ;
  std::vector< float > eT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits ;
  std::vector< float > eT_tau_byMediumIsolationMVA3newDMwLT ;
  std::vector< float > eT_tau_byMediumIsolationMVA3newDMwoLT ;
  std::vector< float > eT_tau_byMediumIsolationMVA3oldDMwLT ;
  std::vector< float > eT_tau_byMediumIsolationMVA3oldDMwoLT ;
  std::vector< float > eT_tau_byTightCombinedIsolationDeltaBetaCorr ;
  std::vector< float > eT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits ;
  std::vector< float > eT_tau_byTightIsolationMVA3newDMwLT ;
  std::vector< float > eT_tau_byTightIsolationMVA3newDMwoLT ;
  std::vector< float > eT_tau_byTightIsolationMVA3oldDMwLT ;
  std::vector< float > eT_tau_byTightIsolationMVA3oldDMwoLT ;
  std::vector< float > eT_tau_byVLooseCombinedIsolationDeltaBetaCorr ;
  std::vector< float > eT_tau_byVLooseIsolationMVA3newDMwLT ;
  std::vector< float > eT_tau_byVLooseIsolationMVA3newDMwoLT ;
  std::vector< float > eT_tau_byVLooseIsolationMVA3oldDMwLT ;
  std::vector< float > eT_tau_byVLooseIsolationMVA3oldDMwoLT ;
  std::vector< float > eT_tau_byVTightIsolationMVA3newDMwLT ;
  std::vector< float > eT_tau_byVTightIsolationMVA3newDMwoLT ;
  std::vector< float > eT_tau_byVTightIsolationMVA3oldDMwLT ;
  std::vector< float > eT_tau_byVTightIsolationMVA3oldDMwoLT ;
  std::vector< float > eT_tau_byVVTightIsolationMVA3newDMwLT ;
  std::vector< float > eT_tau_byVVTightIsolationMVA3newDMwoLT ;
  std::vector< float > eT_tau_byVVTightIsolationMVA3oldDMwLT ;
  std::vector< float > eT_tau_byVVTightIsolationMVA3oldDMwoLT ;
  std::vector< float > eT_tau_chargedIsoPtSum ;
  std::vector< float > eT_tau_decayModeFinding ;
  std::vector< float > eT_tau_decayModeFindingNewDMs ;
  std::vector< float > eT_tau_decayModeFindingOldDMs ;
  std::vector< float > eT_tau_neutralIsoPtSum ;
  std::vector< float > eT_tau_puCorrPtSum ;
  std::vector< bool > eT_tau_has_HltMatchEle20 ;
  std::vector< bool > eT_tau_has_HltMatchEle22 ;
  std::vector< bool > eT_tau_has_HltMatchEle27 ;
  std::vector< bool > eT_tau_has_HltMatchMu17 ;
  std::vector< bool > eT_tau_has_HltMatchMu18 ;
  std::vector< bool > eT_tau_has_HltMatchMu24 ;

  //////////////
  // weights for eTau

  std::vector< double > eT_puWeight ;
  std::vector< double > eT_puWeightM1 ;
  std::vector< double > eT_puWeightP1 ;
  std::vector< float > eT_NumPileupInt ;
  std::vector< float > eT_NumTruePileUpInt ;
  std::vector< float > eT_NumPileupIntM1 ;
  std::vector< float > eT_NumTruePileUpIntM1 ;
  std::vector< float > eT_NumPileupIntP1 ;
  std::vector< float > eT_NumTruePileUpIntP1 ;
  std::vector< double > eT_EffDataELE20andELE22 ;
  std::vector< double > eT_EffMcELE20andELE22 ;
  std::vector< double > eT_HadronicTauDataTrigEffAntiEMed ;
  std::vector< double > eT_HadronicTauMcTrigEffAntiEMed ;
  std::vector< double > eT_HadronicTauDataTrigEffAntiETight ;
  std::vector< double > eT_HadronicTauMcTrigEffAntiETight ;
  std::vector< double > eT_electronDataIDweight ;
  std::vector< double > eT_electronMcIDweight ;
  std::vector< double > eT_electronDataISOLweight ;
  std::vector< double > eT_electronMcISOLweight ;
  std::vector< double > eT_EffDataHighPtTauTrigger ;
  std::vector< double > eT_EffMcHighPtTauTrigger ;
  std::vector< double > eT_TauFakeCorrection ;
  std::vector< double > eT_DecayModeCorrectionFactor ;
  std::vector< double > eT_ZeeScaleFactor ;
  std::vector< double > eT_nominalHIGLUXHQTmhmax ;
  std::vector< double > eT_upHIGLUXHQTmhmax ;
  std::vector< double > eT_downHIGLUXHQTmhmax ;
  std::vector< double > eT_nominalPOWHEGmhmod ;
  std::vector< double > eT_upPOWHEGmhmod ;
  std::vector< double > eT_downPOWHEGmhmod ;
  std::vector< double > eT_etaDepQCDShapeTemplateCorrection ;
  std::vector< double > eT_inclusiveQCDShapeTemplateCorrection ;
  std::vector< double > eT_TTbarPtWeight ;
  std::vector< double > eT_TauSpinnerWT ;
  std::vector< double > eT_TauSpinnerWTFlip ;
  std::vector< double > eT_TauSpinnerWThminus ;
  std::vector< double > eT_TauSpinnerWThplus ;
  std::vector< int > eT_hepNUP ;
  std::vector< double > eT_weightHEPNUP_DYJets ;
  std::vector< double > eT_weightHEPNUP_WJets ;


  std::vector<double> muT_correctedSVFitMass;
  std::vector<double> muT_p4_x;
  std::vector<double> muT_p4_y;
  std::vector<double> muT_p4_z;
  std::vector<double> muT_p4_t;


};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
FlatTuple::FlatTuple(const edm::ParameterSet& iConfig):
electronTauSrc_(iConfig.getParameter<edm::InputTag>("electronTauSrc" )),
electronTauWtSrc_(iConfig.getParameter<edm::InputTag>("electronTauWtSrc" )),
electronSrc_(iConfig.getParameter<edm::InputTag>("electronSrc" )),
tauSrc_(iConfig.getParameter<edm::InputTag>("tauSrc" )),
muonTauSrc_(iConfig.getParameter<edm::InputTag>("muonTauSrc" )),
NAME_(iConfig.getParameter<string>("NAME" ))
{
  //now do what ever initialization is needed




  //////////////////
  // create a file based on the name and sample

  char fname[1000];
  sprintf(fname,"FlatTuple_%s.root",NAME_.c_str());
  cout<<" creating a file of name "<<fname<<endl;
  outFile = new TFile(fname, "RECREATE");
  outFile->cd();


  ///////////////////
  // create the tree
  lepTauTree = new TTree("FlatTuple", "FlatTuple");


  //////////////
  // init values

  reInit();




  ///////////////
  // add branches


// eTau

  lepTauTree->Branch("eT_p4_x", &eT_p4_x);
  lepTauTree->Branch("eT_p4_y", &eT_p4_y);
  lepTauTree->Branch("eT_p4_z", &eT_p4_z);
  lepTauTree->Branch("eT_p4_t", &eT_p4_t);
  lepTauTree->Branch("eT_corrected_p4_x", &eT_corrected_p4_x);
  lepTauTree->Branch("eT_corrected_p4_y", &eT_corrected_p4_y);
  lepTauTree->Branch("eT_corrected_p4_z", &eT_corrected_p4_z);
  lepTauTree->Branch("eT_corrected_p4_t", &eT_corrected_p4_t);
  lepTauTree->Branch("eT_electronIndex", &eT_electronIndex);
  lepTauTree->Branch("eT_tauIndex", &eT_tauIndex);
  lepTauTree->Branch("eT_scalarSumPt", &eT_scalarSumPt);
  lepTauTree->Branch("eT_DR", &eT_DR);
  lepTauTree->Branch("eT_sumCharge", &eT_sumCharge);
  lepTauTree->Branch("eT_correctedSVFitMass", &eT_correctedSVFitMass);
  lepTauTree->Branch("eT_rawSVFitMass", &eT_rawSVFitMass);
  lepTauTree->Branch("eT_TransverseMass", &eT_TransverseMass);
  lepTauTree->Branch("eT_rawTransverseMass", &eT_rawTransverseMass);
  lepTauTree->Branch("eT_mvaMETraw", &eT_mvaMETraw);
  lepTauTree->Branch("eT_mvaMET", &eT_mvaMET);
  lepTauTree->Branch("eT_mvaMETphiRaw", &eT_mvaMETphiRaw);
  lepTauTree->Branch("eT_mvaMETphi", &eT_mvaMETphi);
  lepTauTree->Branch("eT_MAX", &eT_MAX);
  lepTauTree->Branch("eT_isGoodTriggerPair", &eT_isGoodTriggerPair);
  lepTauTree->Branch("eT_njets", &eT_njets);
  lepTauTree->Branch("eT_nbjets", &eT_nbjets);
  lepTauTree->Branch("eT_jet1P4_x", &eT_jet1P4_x);
  lepTauTree->Branch("eT_jet1P4_y", &eT_jet1P4_y);
  lepTauTree->Branch("eT_jet1P4_z", &eT_jet1P4_z);
  lepTauTree->Branch("eT_jet1P4_t", &eT_jet1P4_t);
  lepTauTree->Branch("eT_jet1RawP4_x", &eT_jet1RawP4_x);
  lepTauTree->Branch("eT_jet1RawP4_y", &eT_jet1RawP4_y);
  lepTauTree->Branch("eT_jet1RawP4_z", &eT_jet1RawP4_z);
  lepTauTree->Branch("eT_jet1RawP4_t", &eT_jet1RawP4_t);
  lepTauTree->Branch("eT_jet1IDMVA", &eT_jet1IDMVA);
  lepTauTree->Branch("eT_jet1BTAGMVA", &eT_jet1BTAGMVA);
  lepTauTree->Branch("eT_jet2P4_x", &eT_jet2P4_x);
  lepTauTree->Branch("eT_jet2P4_y", &eT_jet2P4_y);
  lepTauTree->Branch("eT_jet2P4_z", &eT_jet2P4_z);
  lepTauTree->Branch("eT_jet2P4_t", &eT_jet2P4_t);
  lepTauTree->Branch("eT_jet2RawP4_x", &eT_jet2RawP4_x);
  lepTauTree->Branch("eT_jet2RawP4_y", &eT_jet2RawP4_y);
  lepTauTree->Branch("eT_jet2RawP4_z", &eT_jet2RawP4_z);
  lepTauTree->Branch("eT_jet2RawP4_t", &eT_jet2RawP4_t);
  lepTauTree->Branch("eT_jet2IDMVA", &eT_jet2IDMVA);
  lepTauTree->Branch("eT_jet2BTAGMVA", &eT_jet2BTAGMVA);
  lepTauTree->Branch("eT_cov00", &eT_cov00);
  lepTauTree->Branch("eT_cov01", &eT_cov01);
  lepTauTree->Branch("eT_cov10", &eT_cov10);
  lepTauTree->Branch("eT_cov11", &eT_cov11);
  lepTauTree->Branch("eT_passesTriLeptonVeto", &eT_passesTriLeptonVeto);
  lepTauTree->Branch("eT_passNonTopEmbeddedTriggerAndMass50", &eT_passNonTopEmbeddedTriggerAndMass50);
  lepTauTree->Branch("eT_passSignalGeneratorMass70to130Cut", &eT_passSignalGeneratorMass70to130Cut);
  lepTauTree->Branch("eT_genBosonP4_x", &eT_genBosonP4_x);
  lepTauTree->Branch("eT_genBosonP4_y", &eT_genBosonP4_y);
  lepTauTree->Branch("eT_genBosonP4_z", &eT_genBosonP4_z);
  lepTauTree->Branch("eT_genBosonP4_t", &eT_genBosonP4_t);
  lepTauTree->Branch("eT_genTOPp4_x", &eT_genTOPp4_x);
  lepTauTree->Branch("eT_genTOPp4_y", &eT_genTOPp4_y);
  lepTauTree->Branch("eT_genTOPp4_z", &eT_genTOPp4_z);
  lepTauTree->Branch("eT_genTOPp4_t", &eT_genTOPp4_t);
  lepTauTree->Branch("eT_genTOPBARp4_x", &eT_genTOPBARp4_x);
  lepTauTree->Branch("eT_genTOPBARp4_y", &eT_genTOPBARp4_y);
  lepTauTree->Branch("eT_genTOPBARp4_z", &eT_genTOPBARp4_z);
  lepTauTree->Branch("eT_genTOPBARp4_t", &eT_genTOPBARp4_t);
  lepTauTree->Branch("eT_numberOfGoodVertices", &eT_numberOfGoodVertices);
  lepTauTree->Branch("eT_PVndof", &eT_PVndof);
  lepTauTree->Branch("eT_PVz", &eT_PVz);
  lepTauTree->Branch("eT_PVpositionRho", &eT_PVpositionRho);
  lepTauTree->Branch("eT_PVp4_x", &eT_PVp4_x);
  lepTauTree->Branch("eT_PVp4_y", &eT_PVp4_y);
  lepTauTree->Branch("eT_PVp4_z", &eT_PVp4_z);
  lepTauTree->Branch("eT_PVp4_t", &eT_PVp4_t);

// electron in eTau

  lepTauTree->Branch("eT_ele_p4_x", &eT_ele_p4_x);
  lepTauTree->Branch("eT_ele_p4_y", &eT_ele_p4_y);
  lepTauTree->Branch("eT_ele_p4_z", &eT_ele_p4_z);
  lepTauTree->Branch("eT_ele_p4_t", &eT_ele_p4_t);
  lepTauTree->Branch("eT_ele_genP4_x", &eT_ele_genP4_x);
  lepTauTree->Branch("eT_ele_genP4_y", &eT_ele_genP4_y);
  lepTauTree->Branch("eT_ele_genP4_z", &eT_ele_genP4_z);
  lepTauTree->Branch("eT_ele_genP4_t", &eT_ele_genP4_t);
  lepTauTree->Branch("eT_ele_pfP4_x", &eT_ele_pfP4_x);
  lepTauTree->Branch("eT_ele_pfP4_y", &eT_ele_pfP4_y);
  lepTauTree->Branch("eT_ele_pfP4_z", &eT_ele_pfP4_z);
  lepTauTree->Branch("eT_ele_pfP4_t", &eT_ele_pfP4_t);
  lepTauTree->Branch("eT_ele_charge", &eT_ele_charge);
  lepTauTree->Branch("eT_ele_PFpdgId", &eT_ele_PFpdgId);
  lepTauTree->Branch("eT_ele_GENpdgId", &eT_ele_GENpdgId);
  lepTauTree->Branch("eT_ele_numberOfMissingInnerHits", &eT_ele_numberOfMissingInnerHits);
  lepTauTree->Branch("eT_ele_passConversionVeto", &eT_ele_passConversionVeto);
  lepTauTree->Branch("eT_ele_dz", &eT_ele_dz);
  lepTauTree->Branch("eT_ele_dB", &eT_ele_dB);
  lepTauTree->Branch("eT_ele_dxy", &eT_ele_dxy);
  lepTauTree->Branch("eT_ele_SuperClusterEta", &eT_ele_SuperClusterEta);
  lepTauTree->Branch("eT_ele_mvaTrigV0", &eT_ele_mvaTrigV0);
  lepTauTree->Branch("eT_ele_mvaTrigNoIPV0", &eT_ele_mvaTrigNoIPV0);
  lepTauTree->Branch("eT_ele_mvaNonTrigV0", &eT_ele_mvaNonTrigV0);
  lepTauTree->Branch("eT_ele_pass_tight_mvaNonTrigV0", &eT_ele_pass_tight_mvaNonTrigV0);
  lepTauTree->Branch("eT_ele_passFullId", &eT_ele_passFullId);
  lepTauTree->Branch("eT_ele_chargedHadronIso", &eT_ele_chargedHadronIso);
  lepTauTree->Branch("eT_ele_photonIso", &eT_ele_photonIso);
  lepTauTree->Branch("eT_ele_neutralHadronIso", &eT_ele_neutralHadronIso);
  lepTauTree->Branch("eT_ele_puChargedHadronIso", &eT_ele_puChargedHadronIso);
  lepTauTree->Branch("eT_ele_relativeIso", &eT_ele_relativeIso);
  lepTauTree->Branch("eT_ele_isEB", &eT_ele_isEB);
  lepTauTree->Branch("eT_ele_isEE", &eT_ele_isEE);
  lepTauTree->Branch("eT_ele_isEBEEGap", &eT_ele_isEBEEGap);
  lepTauTree->Branch("eT_ele_isEBEtaGap", &eT_ele_isEBEtaGap);
  lepTauTree->Branch("eT_ele_isEBPhiGap", &eT_ele_isEBPhiGap);
  lepTauTree->Branch("eT_ele_isEEDeeGap", &eT_ele_isEEDeeGap);
  lepTauTree->Branch("eT_ele_isEERingGap", &eT_ele_isEERingGap);
  lepTauTree->Branch("eT_ele_sigmaEtaEta", &eT_ele_sigmaEtaEta);
  lepTauTree->Branch("eT_ele_sigmaIetaIeta", &eT_ele_sigmaIetaIeta);
  lepTauTree->Branch("eT_ele_sigmaIphiIphi", &eT_ele_sigmaIphiIphi);
  lepTauTree->Branch("eT_ele_has_HltMatchEle20", &eT_ele_has_HltMatchEle20);
  lepTauTree->Branch("eT_ele_has_HltMatchEle22", &eT_ele_has_HltMatchEle22);
  lepTauTree->Branch("eT_ele_has_HltMatchEle27", &eT_ele_has_HltMatchEle27);
  lepTauTree->Branch("eT_ele_isTriLeptonVetoCandidate", &eT_ele_isTriLeptonVetoCandidate);

  // tau leg in eTau

  lepTauTree->Branch("eT_tau_pfJetRefP4_x", &eT_tau_pfJetRefP4_x);
  lepTauTree->Branch("eT_tau_pfJetRefP4_y", &eT_tau_pfJetRefP4_y);
  lepTauTree->Branch("eT_tau_pfJetRefP4_z", &eT_tau_pfJetRefP4_z);
  lepTauTree->Branch("eT_tau_pfJetRefP4_t", &eT_tau_pfJetRefP4_t);
  lepTauTree->Branch("eT_tau_p4_x", &eT_tau_p4_x);
  lepTauTree->Branch("eT_tau_p4_y", &eT_tau_p4_y);
  lepTauTree->Branch("eT_tau_p4_z", &eT_tau_p4_z);
  lepTauTree->Branch("eT_tau_p4_t", &eT_tau_p4_t);
  lepTauTree->Branch("eT_tau_genP4_x", &eT_tau_genP4_x);
  lepTauTree->Branch("eT_tau_genP4_y", &eT_tau_genP4_y);
  lepTauTree->Branch("eT_tau_genP4_z", &eT_tau_genP4_z);
  lepTauTree->Branch("eT_tau_genP4_t", &eT_tau_genP4_t);
  lepTauTree->Branch("eT_tau_genJet_x", &eT_tau_genJet_x);
  lepTauTree->Branch("eT_tau_genJet_y", &eT_tau_genJet_y);
  lepTauTree->Branch("eT_tau_genJet_z", &eT_tau_genJet_z);
  lepTauTree->Branch("eT_tau_genJet_t", &eT_tau_genJet_t);
  lepTauTree->Branch("eT_tau_corrected_p4_x", &eT_tau_corrected_p4_x);
  lepTauTree->Branch("eT_tau_corrected_p4_y", &eT_tau_corrected_p4_y);
  lepTauTree->Branch("eT_tau_corrected_p4_z", &eT_tau_corrected_p4_z);
  lepTauTree->Branch("eT_tau_corrected_p4_t", &eT_tau_corrected_p4_t);
  lepTauTree->Branch("eT_tau_pdgId", &eT_tau_pdgId);
  lepTauTree->Branch("eT_tau_pdgIdGEN", &eT_tau_pdgIdGEN);
  lepTauTree->Branch("eT_tau_charge", &eT_tau_charge);
  lepTauTree->Branch("eT_tau_decayMode", &eT_tau_decayMode);
  lepTauTree->Branch("eT_tau_passFullId_muTau", &eT_tau_passFullId_muTau);
  lepTauTree->Branch("eT_tau_passFullId_eTau", &eT_tau_passFullId_eTau);
  lepTauTree->Branch("eT_tau_numStrips", &eT_tau_numStrips);
  lepTauTree->Branch("eT_tau_numHadrons", &eT_tau_numHadrons);
  lepTauTree->Branch("eT_tau_againstElectronDeadECAL", &eT_tau_againstElectronDeadECAL);
  lepTauTree->Branch("eT_tau_againstElectronLoose", &eT_tau_againstElectronLoose);
  lepTauTree->Branch("eT_tau_againstElectronLooseMVA5", &eT_tau_againstElectronLooseMVA5);
  lepTauTree->Branch("eT_tau_againstElectronMVA5category", &eT_tau_againstElectronMVA5category);
  lepTauTree->Branch("eT_tau_againstElectronMVA5raw", &eT_tau_againstElectronMVA5raw);
  lepTauTree->Branch("eT_tau_againstElectronMedium", &eT_tau_againstElectronMedium);
  lepTauTree->Branch("eT_tau_againstElectronMediumMVA5", &eT_tau_againstElectronMediumMVA5);
  lepTauTree->Branch("eT_tau_againstElectronTight", &eT_tau_againstElectronTight);
  lepTauTree->Branch("eT_tau_againstElectronTightMVA5", &eT_tau_againstElectronTightMVA5);
  lepTauTree->Branch("eT_tau_againstElectronVLooseMVA5", &eT_tau_againstElectronVLooseMVA5);
  lepTauTree->Branch("eT_tau_againstElectronVTightMVA5", &eT_tau_againstElectronVTightMVA5);
  lepTauTree->Branch("eT_tau_againstMuonLoose", &eT_tau_againstMuonLoose);
  lepTauTree->Branch("eT_tau_againstMuonLoose2", &eT_tau_againstMuonLoose2);
  lepTauTree->Branch("eT_tau_againstMuonLoose3", &eT_tau_againstMuonLoose3);
  lepTauTree->Branch("eT_tau_againstMuonLooseMVA", &eT_tau_againstMuonLooseMVA);
  lepTauTree->Branch("eT_tau_againstMuonMVAraw", &eT_tau_againstMuonMVAraw);
  lepTauTree->Branch("eT_tau_againstMuonMedium", &eT_tau_againstMuonMedium);
  lepTauTree->Branch("eT_tau_againstMuonMedium2", &eT_tau_againstMuonMedium2);
  lepTauTree->Branch("eT_tau_againstMuonMediumMVA", &eT_tau_againstMuonMediumMVA);
  lepTauTree->Branch("eT_tau_againstMuonTight", &eT_tau_againstMuonTight);
  lepTauTree->Branch("eT_tau_againstMuonTight2", &eT_tau_againstMuonTight2);
  lepTauTree->Branch("eT_tau_againstMuonTight3", &eT_tau_againstMuonTight3);
  lepTauTree->Branch("eT_tau_againstMuonTightMVA", &eT_tau_againstMuonTightMVA);
  lepTauTree->Branch("eT_tau_byCombinedIsolationDeltaBetaCorrRaw", &eT_tau_byCombinedIsolationDeltaBetaCorrRaw);
  lepTauTree->Branch("eT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits", &eT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits);
  lepTauTree->Branch("eT_tau_byIsolationMVA3newDMwLTraw", &eT_tau_byIsolationMVA3newDMwLTraw);
  lepTauTree->Branch("eT_tau_byIsolationMVA3newDMwoLTraw", &eT_tau_byIsolationMVA3newDMwoLTraw);
  lepTauTree->Branch("eT_tau_byIsolationMVA3oldDMwLTraw", &eT_tau_byIsolationMVA3oldDMwLTraw);
  lepTauTree->Branch("eT_tau_byIsolationMVA3oldDMwoLTraw", &eT_tau_byIsolationMVA3oldDMwoLTraw);
  lepTauTree->Branch("eT_tau_byLooseCombinedIsolationDeltaBetaCorr", &eT_tau_byLooseCombinedIsolationDeltaBetaCorr);
  lepTauTree->Branch("eT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits", &eT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits);
  lepTauTree->Branch("eT_tau_byLooseIsolation", &eT_tau_byLooseIsolation);
  lepTauTree->Branch("eT_tau_byLooseIsolationMVA3newDMwLT", &eT_tau_byLooseIsolationMVA3newDMwLT);
  lepTauTree->Branch("eT_tau_byLooseIsolationMVA3newDMwoLT", &eT_tau_byLooseIsolationMVA3newDMwoLT);
  lepTauTree->Branch("eT_tau_byLooseIsolationMVA3oldDMwLT", &eT_tau_byLooseIsolationMVA3oldDMwLT);
  lepTauTree->Branch("eT_tau_byLooseIsolationMVA3oldDMwoLT", &eT_tau_byLooseIsolationMVA3oldDMwoLT);
  lepTauTree->Branch("eT_tau_byMediumCombinedIsolationDeltaBetaCorr", &eT_tau_byMediumCombinedIsolationDeltaBetaCorr);
  lepTauTree->Branch("eT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits", &eT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits);
  lepTauTree->Branch("eT_tau_byMediumIsolationMVA3newDMwLT", &eT_tau_byMediumIsolationMVA3newDMwLT);
  lepTauTree->Branch("eT_tau_byMediumIsolationMVA3newDMwoLT", &eT_tau_byMediumIsolationMVA3newDMwoLT);
  lepTauTree->Branch("eT_tau_byMediumIsolationMVA3oldDMwLT", &eT_tau_byMediumIsolationMVA3oldDMwLT);
  lepTauTree->Branch("eT_tau_byMediumIsolationMVA3oldDMwoLT", &eT_tau_byMediumIsolationMVA3oldDMwoLT);
  lepTauTree->Branch("eT_tau_byTightCombinedIsolationDeltaBetaCorr", &eT_tau_byTightCombinedIsolationDeltaBetaCorr);
  lepTauTree->Branch("eT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits", &eT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits);
  lepTauTree->Branch("eT_tau_byTightIsolationMVA3newDMwLT", &eT_tau_byTightIsolationMVA3newDMwLT);
  lepTauTree->Branch("eT_tau_byTightIsolationMVA3newDMwoLT", &eT_tau_byTightIsolationMVA3newDMwoLT);
  lepTauTree->Branch("eT_tau_byTightIsolationMVA3oldDMwLT", &eT_tau_byTightIsolationMVA3oldDMwLT);
  lepTauTree->Branch("eT_tau_byTightIsolationMVA3oldDMwoLT", &eT_tau_byTightIsolationMVA3oldDMwoLT);
  lepTauTree->Branch("eT_tau_byVLooseCombinedIsolationDeltaBetaCorr", &eT_tau_byVLooseCombinedIsolationDeltaBetaCorr);
  lepTauTree->Branch("eT_tau_byVLooseIsolationMVA3newDMwLT", &eT_tau_byVLooseIsolationMVA3newDMwLT);
  lepTauTree->Branch("eT_tau_byVLooseIsolationMVA3newDMwoLT", &eT_tau_byVLooseIsolationMVA3newDMwoLT);
  lepTauTree->Branch("eT_tau_byVLooseIsolationMVA3oldDMwLT", &eT_tau_byVLooseIsolationMVA3oldDMwLT);
  lepTauTree->Branch("eT_tau_byVLooseIsolationMVA3oldDMwoLT", &eT_tau_byVLooseIsolationMVA3oldDMwoLT);
  lepTauTree->Branch("eT_tau_byVTightIsolationMVA3newDMwLT", &eT_tau_byVTightIsolationMVA3newDMwLT);
  lepTauTree->Branch("eT_tau_byVTightIsolationMVA3newDMwoLT", &eT_tau_byVTightIsolationMVA3newDMwoLT);
  lepTauTree->Branch("eT_tau_byVTightIsolationMVA3oldDMwLT", &eT_tau_byVTightIsolationMVA3oldDMwLT);
  lepTauTree->Branch("eT_tau_byVTightIsolationMVA3oldDMwoLT", &eT_tau_byVTightIsolationMVA3oldDMwoLT);
  lepTauTree->Branch("eT_tau_byVVTightIsolationMVA3newDMwLT", &eT_tau_byVVTightIsolationMVA3newDMwLT);
  lepTauTree->Branch("eT_tau_byVVTightIsolationMVA3newDMwoLT", &eT_tau_byVVTightIsolationMVA3newDMwoLT);
  lepTauTree->Branch("eT_tau_byVVTightIsolationMVA3oldDMwLT", &eT_tau_byVVTightIsolationMVA3oldDMwLT);
  lepTauTree->Branch("eT_tau_byVVTightIsolationMVA3oldDMwoLT", &eT_tau_byVVTightIsolationMVA3oldDMwoLT);
  lepTauTree->Branch("eT_tau_chargedIsoPtSum", &eT_tau_chargedIsoPtSum);
  lepTauTree->Branch("eT_tau_decayModeFinding", &eT_tau_decayModeFinding);
  lepTauTree->Branch("eT_tau_decayModeFindingNewDMs", &eT_tau_decayModeFindingNewDMs);
  lepTauTree->Branch("eT_tau_decayModeFindingOldDMs", &eT_tau_decayModeFindingOldDMs);
  lepTauTree->Branch("eT_tau_neutralIsoPtSum", &eT_tau_neutralIsoPtSum);
  lepTauTree->Branch("eT_tau_puCorrPtSum", &eT_tau_puCorrPtSum);
  lepTauTree->Branch("eT_tau_has_HltMatchEle20", &eT_tau_has_HltMatchEle20);
  lepTauTree->Branch("eT_tau_has_HltMatchEle22", &eT_tau_has_HltMatchEle22);
  lepTauTree->Branch("eT_tau_has_HltMatchEle27", &eT_tau_has_HltMatchEle27);
  lepTauTree->Branch("eT_tau_has_HltMatchMu17", &eT_tau_has_HltMatchMu17);
  lepTauTree->Branch("eT_tau_has_HltMatchMu18", &eT_tau_has_HltMatchMu18);
  lepTauTree->Branch("eT_tau_has_HltMatchMu24", &eT_tau_has_HltMatchMu24);


  lepTauTree->Branch("eT_puWeight", &eT_puWeight);
  lepTauTree->Branch("eT_puWeightM1", &eT_puWeightM1);
  lepTauTree->Branch("eT_puWeightP1", &eT_puWeightP1);
  lepTauTree->Branch("eT_NumPileupInt", &eT_NumPileupInt);
  lepTauTree->Branch("eT_NumTruePileUpInt", &eT_NumTruePileUpInt);
  lepTauTree->Branch("eT_NumPileupIntM1", &eT_NumPileupIntM1);
  lepTauTree->Branch("eT_NumTruePileUpIntM1", &eT_NumTruePileUpIntM1);
  lepTauTree->Branch("eT_NumPileupIntP1", &eT_NumPileupIntP1);
  lepTauTree->Branch("eT_NumTruePileUpIntP1", &eT_NumTruePileUpIntP1);
  lepTauTree->Branch("eT_EffDataELE20andELE22", &eT_EffDataELE20andELE22);
  lepTauTree->Branch("eT_EffMcELE20andELE22", &eT_EffMcELE20andELE22);
  lepTauTree->Branch("eT_HadronicTauDataTrigEffAntiEMed", &eT_HadronicTauDataTrigEffAntiEMed);
  lepTauTree->Branch("eT_HadronicTauMcTrigEffAntiEMed", &eT_HadronicTauMcTrigEffAntiEMed);
  lepTauTree->Branch("eT_HadronicTauDataTrigEffAntiETight", &eT_HadronicTauDataTrigEffAntiETight);
  lepTauTree->Branch("eT_HadronicTauMcTrigEffAntiETight", &eT_HadronicTauMcTrigEffAntiETight);
  lepTauTree->Branch("eT_electronDataIDweight", &eT_electronDataIDweight);
  lepTauTree->Branch("eT_electronMcIDweight", &eT_electronMcIDweight);
  lepTauTree->Branch("eT_electronDataISOLweight", &eT_electronDataISOLweight);
  lepTauTree->Branch("eT_electronMcISOLweight", &eT_electronMcISOLweight);
  lepTauTree->Branch("eT_EffDataHighPtTauTrigger", &eT_EffDataHighPtTauTrigger);
  lepTauTree->Branch("eT_EffMcHighPtTauTrigger", &eT_EffMcHighPtTauTrigger);
  lepTauTree->Branch("eT_TauFakeCorrection", &eT_TauFakeCorrection);
  lepTauTree->Branch("eT_DecayModeCorrectionFactor", &eT_DecayModeCorrectionFactor);
  lepTauTree->Branch("eT_ZeeScaleFactor", &eT_ZeeScaleFactor);
  lepTauTree->Branch("eT_nominalHIGLUXHQTmhmax", &eT_nominalHIGLUXHQTmhmax);
  lepTauTree->Branch("eT_upHIGLUXHQTmhmax", &eT_upHIGLUXHQTmhmax);
  lepTauTree->Branch("eT_downHIGLUXHQTmhmax", &eT_downHIGLUXHQTmhmax);
  lepTauTree->Branch("eT_nominalPOWHEGmhmod", &eT_nominalPOWHEGmhmod);
  lepTauTree->Branch("eT_upPOWHEGmhmod", &eT_upPOWHEGmhmod);
  lepTauTree->Branch("eT_downPOWHEGmhmod", &eT_downPOWHEGmhmod);
  lepTauTree->Branch("eT_etaDepQCDShapeTemplateCorrection", &eT_etaDepQCDShapeTemplateCorrection);
  lepTauTree->Branch("eT_inclusiveQCDShapeTemplateCorrection", &eT_inclusiveQCDShapeTemplateCorrection);
  lepTauTree->Branch("eT_TTbarPtWeight", &eT_TTbarPtWeight);
  lepTauTree->Branch("eT_TauSpinnerWT", &eT_TauSpinnerWT);
  lepTauTree->Branch("eT_TauSpinnerWTFlip", &eT_TauSpinnerWTFlip);
  lepTauTree->Branch("eT_TauSpinnerWThminus", &eT_TauSpinnerWThminus);
  lepTauTree->Branch("eT_TauSpinnerWThplus", &eT_TauSpinnerWThplus);
  lepTauTree->Branch("eT_hepNUP", &eT_hepNUP);
  lepTauTree->Branch("eT_weightHEPNUP_DYJets", &eT_weightHEPNUP_DYJets);
  lepTauTree->Branch("eT_weightHEPNUP_WJets", &eT_weightHEPNUP_WJets);


  lepTauTree->Branch("muT_correctedSVFitMass",&muT_correctedSVFitMass);
  lepTauTree->Branch("muT_p4_x",&muT_p4_x);
  lepTauTree->Branch("muT_p4_y",&muT_p4_y);
  lepTauTree->Branch("muT_p4_z",&muT_p4_z);
  lepTauTree->Branch("muT_p4_t",&muT_p4_t);







}


FlatTuple::~FlatTuple()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
FlatTuple::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{


  //////////////
  // init values

  reInit();



  ///////////////
  // get eTaus

  edm::Handle< TupleElectronTauCollection > eTaus;
  iEvent.getByLabel(electronTauSrc_, eTaus);


  ///////////////
  // get eTausWts

  edm::Handle< TupleElectronTauWeightsCollection > eTauWts;
  iEvent.getByLabel(electronTauWtSrc_, eTauWts);

  ///////////////
  // get electrons

  edm::Handle< TupleElectronCollection > elecs;
  iEvent.getByLabel(electronSrc_, elecs);

  /////////////
  // get taus

  edm::Handle< TupleTauCollection > taus;
  iEvent.getByLabel(tauSrc_, taus);


  for (std::size_t i = 0; i < eTaus->size(); ++i)
    {

      const TupleElectronTau eTau =   ((*eTaus)[i]);
      const TupleElectronTauWeight eTauWt =   ((*eTauWts)[i]);
      const TupleElectron theElec =   ((*elecs)[eTau.electronIndex()]);
      const TupleTau theTau =   ((*taus)[eTau.tauIndex()]);


      eT_p4_x.push_back(eTau.p4().x());
      eT_p4_y.push_back(eTau.p4().y());
      eT_p4_z.push_back(eTau.p4().z());
      eT_p4_t.push_back(eTau.p4().t());
      eT_corrected_p4_x.push_back(eTau.corrected_p4().x());
      eT_corrected_p4_y.push_back(eTau.corrected_p4().y());
      eT_corrected_p4_z.push_back(eTau.corrected_p4().z());
      eT_corrected_p4_t.push_back(eTau.corrected_p4().t());
      eT_electronIndex.push_back(eTau.electronIndex());
      eT_tauIndex.push_back(eTau.tauIndex());
      eT_scalarSumPt.push_back(eTau.scalarSumPt());
      eT_DR.push_back(eTau.DR());
      eT_sumCharge.push_back(eTau.sumCharge());
      eT_correctedSVFitMass.push_back(eTau.correctedSVFitMass());
      eT_rawSVFitMass.push_back(eTau.rawSVFitMass());
      eT_TransverseMass.push_back(eTau.TransverseMass());
      eT_rawTransverseMass.push_back(eTau.rawTransverseMass());
      eT_mvaMETraw.push_back(eTau.mvaMETraw());
      eT_mvaMET.push_back(eTau.mvaMET());
      eT_mvaMETphiRaw.push_back(eTau.mvaMETphiRaw());
      eT_mvaMETphi.push_back(eTau.mvaMETphi());
      eT_MAX.push_back(eTau.MAX());
      eT_isGoodTriggerPair.push_back(eTau.isGoodTriggerPair());
      eT_njets.push_back(eTau.njets());
      eT_nbjets.push_back(eTau.nbjets());
      eT_jet1P4_x.push_back(eTau.jet1P4().x());
      eT_jet1P4_y.push_back(eTau.jet1P4().y());
      eT_jet1P4_z.push_back(eTau.jet1P4().z());
      eT_jet1P4_t.push_back(eTau.jet1P4().t());
      eT_jet1RawP4_x.push_back(eTau.jet1RawP4().x());
      eT_jet1RawP4_y.push_back(eTau.jet1RawP4().y());
      eT_jet1RawP4_z.push_back(eTau.jet1RawP4().z());
      eT_jet1RawP4_t.push_back(eTau.jet1RawP4().t());
      eT_jet1IDMVA.push_back(eTau.jet1IDMVA());
      eT_jet1BTAGMVA.push_back(eTau.jet1BTAGMVA());
      eT_jet2P4_x.push_back(eTau.jet2P4().x());
      eT_jet2P4_y.push_back(eTau.jet2P4().y());
      eT_jet2P4_z.push_back(eTau.jet2P4().z());
      eT_jet2P4_t.push_back(eTau.jet2P4().t());
      eT_jet2RawP4_x.push_back(eTau.jet2RawP4().x());
      eT_jet2RawP4_y.push_back(eTau.jet2RawP4().y());
      eT_jet2RawP4_z.push_back(eTau.jet2RawP4().z());
      eT_jet2RawP4_t.push_back(eTau.jet2RawP4().t());
      eT_jet2IDMVA.push_back(eTau.jet2IDMVA());
      eT_jet2BTAGMVA.push_back(eTau.jet2BTAGMVA());
      eT_cov00.push_back(eTau.cov00());
      eT_cov01.push_back(eTau.cov01());
      eT_cov10.push_back(eTau.cov10());
      eT_cov11.push_back(eTau.cov11());
      eT_passesTriLeptonVeto.push_back(eTau.passesTriLeptonVeto());
      eT_passNonTopEmbeddedTriggerAndMass50.push_back(eTau.passNonTopEmbeddedTriggerAndMass50());
      eT_passSignalGeneratorMass70to130Cut.push_back(eTau.passSignalGeneratorMass70to130Cut());
      eT_genBosonP4_x.push_back(eTau.genBosonP4().x());
      eT_genBosonP4_y.push_back(eTau.genBosonP4().y());
      eT_genBosonP4_z.push_back(eTau.genBosonP4().z());
      eT_genBosonP4_t.push_back(eTau.genBosonP4().t());
      eT_genTOPp4_x.push_back(eTau.genTOPp4().x());
      eT_genTOPp4_y.push_back(eTau.genTOPp4().y());
      eT_genTOPp4_z.push_back(eTau.genTOPp4().z());
      eT_genTOPp4_t.push_back(eTau.genTOPp4().t());
      eT_genTOPBARp4_x.push_back(eTau.genTOPBARp4().x());
      eT_genTOPBARp4_y.push_back(eTau.genTOPBARp4().y());
      eT_genTOPBARp4_z.push_back(eTau.genTOPBARp4().z());
      eT_genTOPBARp4_t.push_back(eTau.genTOPBARp4().t());
      eT_numberOfGoodVertices.push_back(eTau.numberOfGoodVertices());
      eT_PVndof.push_back(eTau.PVndof());
      eT_PVz.push_back(eTau.PVz());
      eT_PVpositionRho.push_back(eTau.PVpositionRho());
      eT_PVp4_x.push_back(eTau.PVp4().x());
      eT_PVp4_y.push_back(eTau.PVp4().y());
      eT_PVp4_z.push_back(eTau.PVp4().z());
      eT_PVp4_t.push_back(eTau.PVp4().t());


      eT_ele_p4_x.push_back(theElec.p4().x());
      eT_ele_p4_y.push_back(theElec.p4().y());
      eT_ele_p4_z.push_back(theElec.p4().z());
      eT_ele_p4_t.push_back(theElec.p4().t());
      eT_ele_genP4_x.push_back(theElec.genP4().x());
      eT_ele_genP4_y.push_back(theElec.genP4().y());
      eT_ele_genP4_z.push_back(theElec.genP4().z());
      eT_ele_genP4_t.push_back(theElec.genP4().t());
      eT_ele_pfP4_x.push_back(theElec.pfP4().x());
      eT_ele_pfP4_y.push_back(theElec.pfP4().y());
      eT_ele_pfP4_z.push_back(theElec.pfP4().z());
      eT_ele_pfP4_t.push_back(theElec.pfP4().t());
      eT_ele_charge.push_back(theElec.charge());
      eT_ele_PFpdgId.push_back(theElec.PFpdgId());
      eT_ele_GENpdgId.push_back(theElec.GENpdgId());
      eT_ele_numberOfMissingInnerHits.push_back(theElec.numberOfMissingInnerHits());
      eT_ele_passConversionVeto.push_back(theElec.passConversionVeto());
      eT_ele_dz.push_back(theElec.dz());
      eT_ele_dB.push_back(theElec.dB());
      eT_ele_dxy.push_back(theElec.dxy());
      eT_ele_SuperClusterEta.push_back(theElec.SuperClusterEta());
      eT_ele_mvaTrigV0.push_back(theElec.mvaTrigV0());
      eT_ele_mvaTrigNoIPV0.push_back(theElec.mvaTrigNoIPV0());
      eT_ele_mvaNonTrigV0.push_back(theElec.mvaNonTrigV0());
      eT_ele_pass_tight_mvaNonTrigV0.push_back(theElec.pass_tight_mvaNonTrigV0());
      eT_ele_passFullId.push_back(theElec.passFullId());
      eT_ele_chargedHadronIso.push_back(theElec.chargedHadronIso());
      eT_ele_photonIso.push_back(theElec.photonIso());
      eT_ele_neutralHadronIso.push_back(theElec.neutralHadronIso());
      eT_ele_puChargedHadronIso.push_back(theElec.puChargedHadronIso());
      eT_ele_relativeIso.push_back(theElec.relativeIso());
      eT_ele_isEB.push_back(theElec.isEB());
      eT_ele_isEE.push_back(theElec.isEE());
      eT_ele_isEBEEGap.push_back(theElec.isEBEEGap());
      eT_ele_isEBEtaGap.push_back(theElec.isEBEtaGap());
      eT_ele_isEBPhiGap.push_back(theElec.isEBPhiGap());
      eT_ele_isEEDeeGap.push_back(theElec.isEEDeeGap());
      eT_ele_isEERingGap.push_back(theElec.isEERingGap());
      eT_ele_sigmaEtaEta.push_back(theElec.sigmaEtaEta());
      eT_ele_sigmaIetaIeta.push_back(theElec.sigmaIetaIeta());
      eT_ele_sigmaIphiIphi.push_back(theElec.sigmaIphiIphi());
      eT_ele_has_HltMatchEle20.push_back(theElec.has_HltMatchEle20());
      eT_ele_has_HltMatchEle22.push_back(theElec.has_HltMatchEle22());
      eT_ele_has_HltMatchEle27.push_back(theElec.has_HltMatchEle27());
      eT_ele_isTriLeptonVetoCandidate.push_back(theElec.isTriLeptonVetoCandidate());

      eT_tau_pfJetRefP4_x.push_back(theTau.pfJetRefP4().x());
      eT_tau_pfJetRefP4_y.push_back(theTau.pfJetRefP4().y());
      eT_tau_pfJetRefP4_z.push_back(theTau.pfJetRefP4().z());
      eT_tau_pfJetRefP4_t.push_back(theTau.pfJetRefP4().t());
      eT_tau_p4_x.push_back(theTau.p4().x());
      eT_tau_p4_y.push_back(theTau.p4().y());
      eT_tau_p4_z.push_back(theTau.p4().z());
      eT_tau_p4_t.push_back(theTau.p4().t());
      eT_tau_genP4_x.push_back(theTau.genP4().x());
      eT_tau_genP4_y.push_back(theTau.genP4().y());
      eT_tau_genP4_z.push_back(theTau.genP4().z());
      eT_tau_genP4_t.push_back(theTau.genP4().t());
      eT_tau_genJet_x.push_back(theTau.genJet().x());
      eT_tau_genJet_y.push_back(theTau.genJet().y());
      eT_tau_genJet_z.push_back(theTau.genJet().z());
      eT_tau_genJet_t.push_back(theTau.genJet().t());
      eT_tau_corrected_p4_x.push_back(theTau.corrected_p4().x());
      eT_tau_corrected_p4_y.push_back(theTau.corrected_p4().y());
      eT_tau_corrected_p4_z.push_back(theTau.corrected_p4().z());
      eT_tau_corrected_p4_t.push_back(theTau.corrected_p4().t());
      eT_tau_pdgId.push_back(theTau.pdgId());
      eT_tau_pdgIdGEN.push_back(theTau.pdgIdGEN());
      eT_tau_charge.push_back(theTau.charge());
      eT_tau_decayMode.push_back(theTau.decayMode());
      eT_tau_passFullId_muTau.push_back(theTau.passFullId_muTau());
      eT_tau_passFullId_eTau.push_back(theTau.passFullId_eTau());
      eT_tau_numStrips.push_back(theTau.numStrips());
      eT_tau_numHadrons.push_back(theTau.numHadrons());
      eT_tau_againstElectronDeadECAL.push_back(theTau.againstElectronDeadECAL());
      eT_tau_againstElectronLoose.push_back(theTau.againstElectronLoose());
      eT_tau_againstElectronLooseMVA5.push_back(theTau.againstElectronLooseMVA5());
      eT_tau_againstElectronMVA5category.push_back(theTau.againstElectronMVA5category());
      eT_tau_againstElectronMVA5raw.push_back(theTau.againstElectronMVA5raw());
      eT_tau_againstElectronMedium.push_back(theTau.againstElectronMedium());
      eT_tau_againstElectronMediumMVA5.push_back(theTau.againstElectronMediumMVA5());
      eT_tau_againstElectronTight.push_back(theTau.againstElectronTight());
      eT_tau_againstElectronTightMVA5.push_back(theTau.againstElectronTightMVA5());
      eT_tau_againstElectronVLooseMVA5.push_back(theTau.againstElectronVLooseMVA5());
      eT_tau_againstElectronVTightMVA5.push_back(theTau.againstElectronVTightMVA5());
      eT_tau_againstMuonLoose.push_back(theTau.againstMuonLoose());
      eT_tau_againstMuonLoose2.push_back(theTau.againstMuonLoose2());
      eT_tau_againstMuonLoose3.push_back(theTau.againstMuonLoose3());
      eT_tau_againstMuonLooseMVA.push_back(theTau.againstMuonLooseMVA());
      eT_tau_againstMuonMVAraw.push_back(theTau.againstMuonMVAraw());
      eT_tau_againstMuonMedium.push_back(theTau.againstMuonMedium());
      eT_tau_againstMuonMedium2.push_back(theTau.againstMuonMedium2());
      eT_tau_againstMuonMediumMVA.push_back(theTau.againstMuonMediumMVA());
      eT_tau_againstMuonTight.push_back(theTau.againstMuonTight());
      eT_tau_againstMuonTight2.push_back(theTau.againstMuonTight2());
      eT_tau_againstMuonTight3.push_back(theTau.againstMuonTight3());
      eT_tau_againstMuonTightMVA.push_back(theTau.againstMuonTightMVA());
      eT_tau_byCombinedIsolationDeltaBetaCorrRaw.push_back(theTau.byCombinedIsolationDeltaBetaCorrRaw());
      eT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits.push_back(theTau.byCombinedIsolationDeltaBetaCorrRaw3Hits());
      eT_tau_byIsolationMVA3newDMwLTraw.push_back(theTau.byIsolationMVA3newDMwLTraw());
      eT_tau_byIsolationMVA3newDMwoLTraw.push_back(theTau.byIsolationMVA3newDMwoLTraw());
      eT_tau_byIsolationMVA3oldDMwLTraw.push_back(theTau.byIsolationMVA3oldDMwLTraw());
      eT_tau_byIsolationMVA3oldDMwoLTraw.push_back(theTau.byIsolationMVA3oldDMwoLTraw());
      eT_tau_byLooseCombinedIsolationDeltaBetaCorr.push_back(theTau.byLooseCombinedIsolationDeltaBetaCorr());
      eT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits.push_back(theTau.byLooseCombinedIsolationDeltaBetaCorr3Hits());
      eT_tau_byLooseIsolation.push_back(theTau.byLooseIsolation());
      eT_tau_byLooseIsolationMVA3newDMwLT.push_back(theTau.byLooseIsolationMVA3newDMwLT());
      eT_tau_byLooseIsolationMVA3newDMwoLT.push_back(theTau.byLooseIsolationMVA3newDMwoLT());
      eT_tau_byLooseIsolationMVA3oldDMwLT.push_back(theTau.byLooseIsolationMVA3oldDMwLT());
      eT_tau_byLooseIsolationMVA3oldDMwoLT.push_back(theTau.byLooseIsolationMVA3oldDMwoLT());
      eT_tau_byMediumCombinedIsolationDeltaBetaCorr.push_back(theTau.byMediumCombinedIsolationDeltaBetaCorr());
      eT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits.push_back(theTau.byMediumCombinedIsolationDeltaBetaCorr3Hits());
      eT_tau_byMediumIsolationMVA3newDMwLT.push_back(theTau.byMediumIsolationMVA3newDMwLT());
      eT_tau_byMediumIsolationMVA3newDMwoLT.push_back(theTau.byMediumIsolationMVA3newDMwoLT());
      eT_tau_byMediumIsolationMVA3oldDMwLT.push_back(theTau.byMediumIsolationMVA3oldDMwLT());
      eT_tau_byMediumIsolationMVA3oldDMwoLT.push_back(theTau.byMediumIsolationMVA3oldDMwoLT());
      eT_tau_byTightCombinedIsolationDeltaBetaCorr.push_back(theTau.byTightCombinedIsolationDeltaBetaCorr());
      eT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits.push_back(theTau.byTightCombinedIsolationDeltaBetaCorr3Hits());
      eT_tau_byTightIsolationMVA3newDMwLT.push_back(theTau.byTightIsolationMVA3newDMwLT());
      eT_tau_byTightIsolationMVA3newDMwoLT.push_back(theTau.byTightIsolationMVA3newDMwoLT());
      eT_tau_byTightIsolationMVA3oldDMwLT.push_back(theTau.byTightIsolationMVA3oldDMwLT());
      eT_tau_byTightIsolationMVA3oldDMwoLT.push_back(theTau.byTightIsolationMVA3oldDMwoLT());
      eT_tau_byVLooseCombinedIsolationDeltaBetaCorr.push_back(theTau.byVLooseCombinedIsolationDeltaBetaCorr());
      eT_tau_byVLooseIsolationMVA3newDMwLT.push_back(theTau.byVLooseIsolationMVA3newDMwLT());
      eT_tau_byVLooseIsolationMVA3newDMwoLT.push_back(theTau.byVLooseIsolationMVA3newDMwoLT());
      eT_tau_byVLooseIsolationMVA3oldDMwLT.push_back(theTau.byVLooseIsolationMVA3oldDMwLT());
      eT_tau_byVLooseIsolationMVA3oldDMwoLT.push_back(theTau.byVLooseIsolationMVA3oldDMwoLT());
      eT_tau_byVTightIsolationMVA3newDMwLT.push_back(theTau.byVTightIsolationMVA3newDMwLT());
      eT_tau_byVTightIsolationMVA3newDMwoLT.push_back(theTau.byVTightIsolationMVA3newDMwoLT());
      eT_tau_byVTightIsolationMVA3oldDMwLT.push_back(theTau.byVTightIsolationMVA3oldDMwLT());
      eT_tau_byVTightIsolationMVA3oldDMwoLT.push_back(theTau.byVTightIsolationMVA3oldDMwoLT());
      eT_tau_byVVTightIsolationMVA3newDMwLT.push_back(theTau.byVVTightIsolationMVA3newDMwLT());
      eT_tau_byVVTightIsolationMVA3newDMwoLT.push_back(theTau.byVVTightIsolationMVA3newDMwoLT());
      eT_tau_byVVTightIsolationMVA3oldDMwLT.push_back(theTau.byVVTightIsolationMVA3oldDMwLT());
      eT_tau_byVVTightIsolationMVA3oldDMwoLT.push_back(theTau.byVVTightIsolationMVA3oldDMwoLT());
      eT_tau_chargedIsoPtSum.push_back(theTau.chargedIsoPtSum());
      eT_tau_decayModeFinding.push_back(theTau.decayModeFinding());
      eT_tau_decayModeFindingNewDMs.push_back(theTau.decayModeFindingNewDMs());
      eT_tau_decayModeFindingOldDMs.push_back(theTau.decayModeFindingOldDMs());
      eT_tau_neutralIsoPtSum.push_back(theTau.neutralIsoPtSum());
      eT_tau_puCorrPtSum.push_back(theTau.puCorrPtSum());
      eT_tau_has_HltMatchEle20.push_back(theTau.has_HltMatchEle20());
      eT_tau_has_HltMatchEle22.push_back(theTau.has_HltMatchEle22());
      eT_tau_has_HltMatchEle27.push_back(theTau.has_HltMatchEle27());
      eT_tau_has_HltMatchMu17.push_back(theTau.has_HltMatchMu17());
      eT_tau_has_HltMatchMu18.push_back(theTau.has_HltMatchMu18());
      eT_tau_has_HltMatchMu24.push_back(theTau.has_HltMatchMu24());

      eT_puWeight.push_back(eTauWt.puWeight());
      eT_puWeightM1.push_back(eTauWt.puWeightM1());
      eT_puWeightP1.push_back(eTauWt.puWeightP1());
      eT_NumPileupInt.push_back(eTauWt.NumPileupInt());
      eT_NumTruePileUpInt.push_back(eTauWt.NumTruePileUpInt());
      eT_NumPileupIntM1.push_back(eTauWt.NumPileupIntM1());
      eT_NumTruePileUpIntM1.push_back(eTauWt.NumTruePileUpIntM1());
      eT_NumPileupIntP1.push_back(eTauWt.NumPileupIntP1());
      eT_NumTruePileUpIntP1.push_back(eTauWt.NumTruePileUpIntP1());
      eT_EffDataELE20andELE22.push_back(eTauWt.EffDataELE20andELE22());
      eT_EffMcELE20andELE22.push_back(eTauWt.EffMcELE20andELE22());
      eT_HadronicTauDataTrigEffAntiEMed.push_back(eTauWt.HadronicTauDataTrigEffAntiEMed());
      eT_HadronicTauMcTrigEffAntiEMed.push_back(eTauWt.HadronicTauMcTrigEffAntiEMed());
      eT_HadronicTauDataTrigEffAntiETight.push_back(eTauWt.HadronicTauDataTrigEffAntiETight());
      eT_HadronicTauMcTrigEffAntiETight.push_back(eTauWt.HadronicTauMcTrigEffAntiETight());
      eT_electronDataIDweight.push_back(eTauWt.electronDataIDweight());
      eT_electronMcIDweight.push_back(eTauWt.electronMcIDweight());
      eT_electronDataISOLweight.push_back(eTauWt.electronDataISOLweight());
      eT_electronMcISOLweight.push_back(eTauWt.electronMcISOLweight());
      eT_EffDataHighPtTauTrigger.push_back(eTauWt.EffDataHighPtTauTrigger());
      eT_EffMcHighPtTauTrigger.push_back(eTauWt.EffMcHighPtTauTrigger());
      eT_TauFakeCorrection.push_back(eTauWt.TauFakeCorrection());
      eT_DecayModeCorrectionFactor.push_back(eTauWt.DecayModeCorrectionFactor());
      eT_ZeeScaleFactor.push_back(eTauWt.ZeeScaleFactor());
      eT_nominalHIGLUXHQTmhmax.push_back(eTauWt.nominalHIGLUXHQTmhmax());
      eT_upHIGLUXHQTmhmax.push_back(eTauWt.upHIGLUXHQTmhmax());
      eT_downHIGLUXHQTmhmax.push_back(eTauWt.downHIGLUXHQTmhmax());
      eT_nominalPOWHEGmhmod.push_back(eTauWt.nominalPOWHEGmhmod());
      eT_upPOWHEGmhmod.push_back(eTauWt.upPOWHEGmhmod());
      eT_downPOWHEGmhmod.push_back(eTauWt.downPOWHEGmhmod());
      eT_etaDepQCDShapeTemplateCorrection.push_back(eTauWt.etaDepQCDShapeTemplateCorrection());
      eT_inclusiveQCDShapeTemplateCorrection.push_back(eTauWt.inclusiveQCDShapeTemplateCorrection());
      eT_TTbarPtWeight.push_back(eTauWt.TTbarPtWeight());
      eT_TauSpinnerWT.push_back(eTauWt.TauSpinnerWT());
      eT_TauSpinnerWTFlip.push_back(eTauWt.TauSpinnerWTFlip());
      eT_TauSpinnerWThminus.push_back(eTauWt.TauSpinnerWThminus());
      eT_TauSpinnerWThplus.push_back(eTauWt.TauSpinnerWThplus());
      eT_hepNUP.push_back(eTauWt.hepNUP());
      eT_weightHEPNUP_DYJets.push_back(eTauWt.weightHEPNUP_DYJets());
      eT_weightHEPNUP_WJets.push_back(eTauWt.weightHEPNUP_WJets());



    }


  ///////////////
  // get muTaus

  edm::Handle< TupleMuonTauCollection > muTaus;
  iEvent.getByLabel(muonTauSrc_, muTaus);


  for (std::size_t i = 0; i < muTaus->size(); ++i)
    {

      const TupleMuonTau muTau =   ((*muTaus)[i]);
      muT_correctedSVFitMass.push_back(muTau.correctedSVFitMass());
      muT_p4_x.push_back(muTau.p4().x());
      muT_p4_y.push_back(muTau.p4().y());
      muT_p4_z.push_back(muTau.p4().z());
      muT_p4_t.push_back(muTau.p4().t());


    }




    ///////////
    // fill the tree

    if(muTaus->size()+eTaus->size() > 0) lepTauTree->Fill();






















    #ifdef THIS_IS_AN_EVENT_EXAMPLE
    Handle<ExampleData> pIn;
    iEvent.getByLabel("example",pIn);
    #endif

    #ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
    ESHandle<SetupData> pSetup;
    iSetup.get<SetupRecord>().get(pSetup);
    #endif
  }


  // ------------ method called once each job just before starting event loop  ------------
  void
  FlatTuple::beginJob()
  {
  }

  // ------------ method called once each job just after ending the event loop  ------------
  void
  FlatTuple::endJob()
  {
    lepTauTree->Write();
    outFile->Close();


  }

  // ------------ method called when starting to processes a run  ------------
  void
  FlatTuple::beginRun(edm::Run const&, edm::EventSetup const&)
  {
  }

  // ------------ method called when ending the processing of a run  ------------
  void
  FlatTuple::endRun(edm::Run const&, edm::EventSetup const&)
  {
  }

  // ------------ method called when starting to processes a luminosity block  ------------
  void
  FlatTuple::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
  {
  }

  // ------------ method called when ending the processing of a luminosity block  ------------
  void
  FlatTuple::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
  {
  }

  void
  FlatTuple::reInit()
  {

    eT_p4_x.clear();
    eT_p4_y.clear();
    eT_p4_z.clear();
    eT_p4_t.clear();
    eT_corrected_p4_x.clear();
    eT_corrected_p4_y.clear();
    eT_corrected_p4_z.clear();
    eT_corrected_p4_t.clear();
    eT_electronIndex.clear();
    eT_tauIndex.clear();
    eT_scalarSumPt.clear();
    eT_DR.clear();
    eT_sumCharge.clear();
    eT_correctedSVFitMass.clear();
    eT_rawSVFitMass.clear();
    eT_TransverseMass.clear();
    eT_rawTransverseMass.clear();
    eT_mvaMETraw.clear();
    eT_mvaMET.clear();
    eT_mvaMETphiRaw.clear();
    eT_mvaMETphi.clear();
    eT_MAX.clear();
    eT_isGoodTriggerPair.clear();
    eT_njets.clear();
    eT_nbjets.clear();
    eT_jet1P4_x.clear();
    eT_jet1P4_y.clear();
    eT_jet1P4_z.clear();
    eT_jet1P4_t.clear();
    eT_jet1RawP4_x.clear();
    eT_jet1RawP4_y.clear();
    eT_jet1RawP4_z.clear();
    eT_jet1RawP4_t.clear();
    eT_jet1IDMVA.clear();
    eT_jet1BTAGMVA.clear();
    eT_jet2P4_x.clear();
    eT_jet2P4_y.clear();
    eT_jet2P4_z.clear();
    eT_jet2P4_t.clear();
    eT_jet2RawP4_x.clear();
    eT_jet2RawP4_y.clear();
    eT_jet2RawP4_z.clear();
    eT_jet2RawP4_t.clear();
    eT_jet2IDMVA.clear();
    eT_jet2BTAGMVA.clear();
    eT_cov00.clear();
    eT_cov01.clear();
    eT_cov10.clear();
    eT_cov11.clear();
    eT_passesTriLeptonVeto.clear();
    eT_passNonTopEmbeddedTriggerAndMass50.clear();
    eT_passSignalGeneratorMass70to130Cut.clear();
    eT_genBosonP4_x.clear();
    eT_genBosonP4_y.clear();
    eT_genBosonP4_z.clear();
    eT_genBosonP4_t.clear();
    eT_genTOPp4_x.clear();
    eT_genTOPp4_y.clear();
    eT_genTOPp4_z.clear();
    eT_genTOPp4_t.clear();
    eT_genTOPBARp4_x.clear();
    eT_genTOPBARp4_y.clear();
    eT_genTOPBARp4_z.clear();
    eT_genTOPBARp4_t.clear();
    eT_numberOfGoodVertices.clear();
    eT_PVndof.clear();
    eT_PVz.clear();
    eT_PVpositionRho.clear();
    eT_PVp4_x.clear();
    eT_PVp4_y.clear();
    eT_PVp4_z.clear();
    eT_PVp4_t.clear();

    eT_ele_p4_x.clear();
    eT_ele_p4_y.clear();
    eT_ele_p4_z.clear();
    eT_ele_p4_t.clear();
    eT_ele_genP4_x.clear();
    eT_ele_genP4_y.clear();
    eT_ele_genP4_z.clear();
    eT_ele_genP4_t.clear();
    eT_ele_pfP4_x.clear();
    eT_ele_pfP4_y.clear();
    eT_ele_pfP4_z.clear();
    eT_ele_pfP4_t.clear();
    eT_ele_charge.clear();
    eT_ele_PFpdgId.clear();
    eT_ele_GENpdgId.clear();
    eT_ele_numberOfMissingInnerHits.clear();
    eT_ele_passConversionVeto.clear();
    eT_ele_dz.clear();
    eT_ele_dB.clear();
    eT_ele_dxy.clear();
    eT_ele_SuperClusterEta.clear();
    eT_ele_mvaTrigV0.clear();
    eT_ele_mvaTrigNoIPV0.clear();
    eT_ele_mvaNonTrigV0.clear();
    eT_ele_pass_tight_mvaNonTrigV0.clear();
    eT_ele_passFullId.clear();
    eT_ele_chargedHadronIso.clear();
    eT_ele_photonIso.clear();
    eT_ele_neutralHadronIso.clear();
    eT_ele_puChargedHadronIso.clear();
    eT_ele_relativeIso.clear();
    eT_ele_isEB.clear();
    eT_ele_isEE.clear();
    eT_ele_isEBEEGap.clear();
    eT_ele_isEBEtaGap.clear();
    eT_ele_isEBPhiGap.clear();
    eT_ele_isEEDeeGap.clear();
    eT_ele_isEERingGap.clear();
    eT_ele_sigmaEtaEta.clear();
    eT_ele_sigmaIetaIeta.clear();
    eT_ele_sigmaIphiIphi.clear();
    eT_ele_has_HltMatchEle20.clear();
    eT_ele_has_HltMatchEle22.clear();
    eT_ele_has_HltMatchEle27.clear();
    eT_ele_isTriLeptonVetoCandidate.clear();

    eT_tau_pfJetRefP4_x.clear();
    eT_tau_pfJetRefP4_y.clear();
    eT_tau_pfJetRefP4_z.clear();
    eT_tau_pfJetRefP4_t.clear();
    eT_tau_p4_x.clear();
    eT_tau_p4_y.clear();
    eT_tau_p4_z.clear();
    eT_tau_p4_t.clear();
    eT_tau_genP4_x.clear();
    eT_tau_genP4_y.clear();
    eT_tau_genP4_z.clear();
    eT_tau_genP4_t.clear();
    eT_tau_genJet_x.clear();
    eT_tau_genJet_y.clear();
    eT_tau_genJet_z.clear();
    eT_tau_genJet_t.clear();
    eT_tau_corrected_p4_x.clear();
    eT_tau_corrected_p4_y.clear();
    eT_tau_corrected_p4_z.clear();
    eT_tau_corrected_p4_t.clear();
    eT_tau_pdgId.clear();
    eT_tau_pdgIdGEN.clear();
    eT_tau_charge.clear();
    eT_tau_decayMode.clear();
    eT_tau_passFullId_muTau.clear();
    eT_tau_passFullId_eTau.clear();
    eT_tau_numStrips.clear();
    eT_tau_numHadrons.clear();
    eT_tau_againstElectronDeadECAL.clear();
    eT_tau_againstElectronLoose.clear();
    eT_tau_againstElectronLooseMVA5.clear();
    eT_tau_againstElectronMVA5category.clear();
    eT_tau_againstElectronMVA5raw.clear();
    eT_tau_againstElectronMedium.clear();
    eT_tau_againstElectronMediumMVA5.clear();
    eT_tau_againstElectronTight.clear();
    eT_tau_againstElectronTightMVA5.clear();
    eT_tau_againstElectronVLooseMVA5.clear();
    eT_tau_againstElectronVTightMVA5.clear();
    eT_tau_againstMuonLoose.clear();
    eT_tau_againstMuonLoose2.clear();
    eT_tau_againstMuonLoose3.clear();
    eT_tau_againstMuonLooseMVA.clear();
    eT_tau_againstMuonMVAraw.clear();
    eT_tau_againstMuonMedium.clear();
    eT_tau_againstMuonMedium2.clear();
    eT_tau_againstMuonMediumMVA.clear();
    eT_tau_againstMuonTight.clear();
    eT_tau_againstMuonTight2.clear();
    eT_tau_againstMuonTight3.clear();
    eT_tau_againstMuonTightMVA.clear();
    eT_tau_byCombinedIsolationDeltaBetaCorrRaw.clear();
    eT_tau_byCombinedIsolationDeltaBetaCorrRaw3Hits.clear();
    eT_tau_byIsolationMVA3newDMwLTraw.clear();
    eT_tau_byIsolationMVA3newDMwoLTraw.clear();
    eT_tau_byIsolationMVA3oldDMwLTraw.clear();
    eT_tau_byIsolationMVA3oldDMwoLTraw.clear();
    eT_tau_byLooseCombinedIsolationDeltaBetaCorr.clear();
    eT_tau_byLooseCombinedIsolationDeltaBetaCorr3Hits.clear();
    eT_tau_byLooseIsolation.clear();
    eT_tau_byLooseIsolationMVA3newDMwLT.clear();
    eT_tau_byLooseIsolationMVA3newDMwoLT.clear();
    eT_tau_byLooseIsolationMVA3oldDMwLT.clear();
    eT_tau_byLooseIsolationMVA3oldDMwoLT.clear();
    eT_tau_byMediumCombinedIsolationDeltaBetaCorr.clear();
    eT_tau_byMediumCombinedIsolationDeltaBetaCorr3Hits.clear();
    eT_tau_byMediumIsolationMVA3newDMwLT.clear();
    eT_tau_byMediumIsolationMVA3newDMwoLT.clear();
    eT_tau_byMediumIsolationMVA3oldDMwLT.clear();
    eT_tau_byMediumIsolationMVA3oldDMwoLT.clear();
    eT_tau_byTightCombinedIsolationDeltaBetaCorr.clear();
    eT_tau_byTightCombinedIsolationDeltaBetaCorr3Hits.clear();
    eT_tau_byTightIsolationMVA3newDMwLT.clear();
    eT_tau_byTightIsolationMVA3newDMwoLT.clear();
    eT_tau_byTightIsolationMVA3oldDMwLT.clear();
    eT_tau_byTightIsolationMVA3oldDMwoLT.clear();
    eT_tau_byVLooseCombinedIsolationDeltaBetaCorr.clear();
    eT_tau_byVLooseIsolationMVA3newDMwLT.clear();
    eT_tau_byVLooseIsolationMVA3newDMwoLT.clear();
    eT_tau_byVLooseIsolationMVA3oldDMwLT.clear();
    eT_tau_byVLooseIsolationMVA3oldDMwoLT.clear();
    eT_tau_byVTightIsolationMVA3newDMwLT.clear();
    eT_tau_byVTightIsolationMVA3newDMwoLT.clear();
    eT_tau_byVTightIsolationMVA3oldDMwLT.clear();
    eT_tau_byVTightIsolationMVA3oldDMwoLT.clear();
    eT_tau_byVVTightIsolationMVA3newDMwLT.clear();
    eT_tau_byVVTightIsolationMVA3newDMwoLT.clear();
    eT_tau_byVVTightIsolationMVA3oldDMwLT.clear();
    eT_tau_byVVTightIsolationMVA3oldDMwoLT.clear();
    eT_tau_chargedIsoPtSum.clear();
    eT_tau_decayModeFinding.clear();
    eT_tau_decayModeFindingNewDMs.clear();
    eT_tau_decayModeFindingOldDMs.clear();
    eT_tau_neutralIsoPtSum.clear();
    eT_tau_puCorrPtSum.clear();
    eT_tau_has_HltMatchEle20.clear();
    eT_tau_has_HltMatchEle22.clear();
    eT_tau_has_HltMatchEle27.clear();
    eT_tau_has_HltMatchMu17.clear();
    eT_tau_has_HltMatchMu18.clear();
    eT_tau_has_HltMatchMu24.clear();



    eT_puWeight.clear();
    eT_puWeightM1.clear();
    eT_puWeightP1.clear();
    eT_NumPileupInt.clear();
    eT_NumTruePileUpInt.clear();
    eT_NumPileupIntM1.clear();
    eT_NumTruePileUpIntM1.clear();
    eT_NumPileupIntP1.clear();
    eT_NumTruePileUpIntP1.clear();
    eT_EffDataELE20andELE22.clear();
    eT_EffMcELE20andELE22.clear();
    eT_HadronicTauDataTrigEffAntiEMed.clear();
    eT_HadronicTauMcTrigEffAntiEMed.clear();
    eT_HadronicTauDataTrigEffAntiETight.clear();
    eT_HadronicTauMcTrigEffAntiETight.clear();
    eT_electronDataIDweight.clear();
    eT_electronMcIDweight.clear();
    eT_electronDataISOLweight.clear();
    eT_electronMcISOLweight.clear();
    eT_EffDataHighPtTauTrigger.clear();
    eT_EffMcHighPtTauTrigger.clear();
    eT_TauFakeCorrection.clear();
    eT_DecayModeCorrectionFactor.clear();
    eT_ZeeScaleFactor.clear();
    eT_nominalHIGLUXHQTmhmax.clear();
    eT_upHIGLUXHQTmhmax.clear();
    eT_downHIGLUXHQTmhmax.clear();
    eT_nominalPOWHEGmhmod.clear();
    eT_upPOWHEGmhmod.clear();
    eT_downPOWHEGmhmod.clear();
    eT_etaDepQCDShapeTemplateCorrection.clear();
    eT_inclusiveQCDShapeTemplateCorrection.clear();
    eT_TTbarPtWeight.clear();
    eT_TauSpinnerWT.clear();
    eT_TauSpinnerWTFlip.clear();
    eT_TauSpinnerWThminus.clear();
    eT_TauSpinnerWThplus.clear();
    eT_hepNUP.clear();
    eT_weightHEPNUP_DYJets.clear();
    eT_weightHEPNUP_WJets.clear();



  }


  // ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
  void
  FlatTuple::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    //The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
  }

  //define this as a plug-in
  DEFINE_FWK_MODULE(FlatTuple);
