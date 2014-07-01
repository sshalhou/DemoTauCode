// -*- C++ -*-
//
// Package:    SyncTree
// Class:      SyncTree
//
/**\class SyncTree SyncTree.cc TEMP/SyncTree/src/SyncTree.cc

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


#include <string>
#include "TTree.h"
#include "TFile.h"

using namespace edm;
using namespace std;

typedef math::XYZTLorentzVector LorentzVector;

//
// class declaration
//

class SyncTree : public edm::EDAnalyzer {
public:
  explicit SyncTree(const edm::ParameterSet&);
  ~SyncTree();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

  // ----------member data ---------------------------

  edm::InputTag tauSrc_;
  edm::InputTag leptonSrc_;
  edm::InputTag leptonTauSrc_;
  string NAME_;


  TFile *syncFile;
  TTree *syncTree;

  // tree variables from
  // https://github.com/ajgilbert/ICHiggsTauTau/blob/master/Analysis/HiggsTauTau/interface/HTTSync.h

  int   lRun;
  int   lLumi;
  int   lEvt;
  int   lNPV;
  int   lNPU;
  float lRho;
  float lMCWeight;
  float lPUWeight;
  float lFakeWeight;
  float lTrigweight_1;
  float lTrigweight_2;
  float lIdweight_1;
  float lIdweight_2;
  float lIsoweight_1;
  float lIsoweight_2;
  float lEffWeight;
  float lWeight;
  float lEmbeddedWeight;
  float lSignalWeight;
  float lMSV;
  float lPtSV;
  float lEtaSV;
  float lPhiSV;
  float lMVis;
  float lMSVUp;
  float lMSVDown;
  float lPt1;
  float lPhi1;
  float lEta1;
  float lM1;
  int   lq1;
  float lIso1;
  float lMVA1;
  float lD01;
  float lDZ1;
  bool  lPassId1;
  bool  lPassIso1;
  float lMt1;
  float lPtTT;
  float lPt2;
  float lPhi2;
  float lEta2;
  float lM2;
  int   lq2;
  float lIso2;
  float lD02;
  float lDZ2;
  float l3Hits_2;
  float lagainstElectronMVA3raw_2;
  float lbyIsolationMVA2raw_2;
  float lagainstMuonLoose2_2;
  float lagainstMuonMedium2_2;
  float lagainstMuonTight2_2;
  float lMVA2;
  bool  lPassId2;
  bool  lPassIso2;
  float lMt2;
  float lMet;
  float lMetPhi;
  float lL1Met;
  float lL1MetPhi;
  float lL1MetCorr;
  float lCaloMet;
  float lCaloMetPhi;
  float lCaloMetCorr;
  float lCaloMetPhiCorr;
  float lMVAMet;
  float lMVAMetPhi;
  float lPZetaVis;
  float lPZetaMiss;
  float lMetCov00;
  float lMetCov01;
  float lMetCov10;
  float lMetCov11;
  float lMVACov00;
  float lMVACov01;
  float lMVACov10;
  float lMVACov11;
  float lJPt1;
  float lJEta1;
  float lJPhi1;
  float lJPtRaw1;
  float lJPtUnc1;
  float lJMVA1;
  float lLRM1;
  int lCTM1;
  bool  lJPass1;
  float lJPt2;
  float lJEta2;
  float lJPhi2;
  float lJPtRaw2;
  float lJPtUnc2;
  float lJMVA2;
  float lLRM2;
  int lCTM2;
  bool  lJPass2;
  float lBTagPt;
  float lBTagEta;
  float lBTagPhi;
  float lMJJ;
  float lJDEta;
  int   lNJetInGap;
  float lMVA;
  float lJDPhi;
  float lDiJetPt;
  float lDiJetPhi;
  float lHDJetPhi;
  float lVisJetEta;
  float lPtVis;
  int   lNBTag;
  int   lNJets;
  int   lNJetsPt20;
  float em_gf_mva_;
  float em_vbf_mva_;


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
SyncTree::SyncTree(const edm::ParameterSet& iConfig):
tauSrc_(iConfig.getParameter<edm::InputTag>("tauSrc" )),
leptonSrc_(iConfig.getParameter<edm::InputTag>("leptonSrc" )),
leptonTauSrc_(iConfig.getParameter<edm::InputTag>("leptonTauSrc" )),
NAME_(iConfig.getParameter<string>("NAME" ))
{
  //now do what ever initialization is needed


  lRun = -999;
  lLumi  = -999;
  lEvt = -999;
  lNPV = -999;
  lNPU = -999;
  lRho = -999.;
  lMCWeight = -999.;
  lPUWeight = -999.;
  lFakeWeight = -999.;
  lTrigweight_1 = -999.;
  lTrigweight_2 = -999.;
  lIdweight_1 = -999.;
  lIdweight_2 = -999.;
  lIsoweight_1 = -999.;
  lIsoweight_2 = -999.;
  lEffWeight = -999.;
  lWeight = -999.;
  lEmbeddedWeight = -999.;
  lSignalWeight = -999.;
  lMSV = -999.;
  lPtSV = -999.;
  lEtaSV = -999.;
  lPhiSV = -999.;
  lMVis = -999.;
  lMSVUp = -999.;
  lMSVDown = -999.;
  lPt1 = -999.;
  lPhi1 = -999.;
  lEta1 = -999.;
  lM1 = -999.;
  lq1  = -999;
  lIso1 = -999.;
  lMVA1 = -999.;
  lD01 = -999.;
  lDZ1 = -999.;
  lPassId1 = 0;
  lPassIso1 = 0;
  lMt1 = -999.;
  lPtTT = -999.;
  lPt2 = -999.;
  lPhi2 = -999.;
  lEta2 = -999.;
  lM2 = -999.;
  lq2  = -999;
  lIso2 = -999.;
  lD02 = -999.;
  lDZ2 = -999.;
  l3Hits_2 = -999.;
  lagainstElectronMVA3raw_2 = -999.;
  lbyIsolationMVA2raw_2 = -999.;
  lagainstMuonLoose2_2 = -999.;
  lagainstMuonMedium2_2 = -999.;
  lagainstMuonTight2_2 = -999.;
  lMVA2 = -999.;
  lPassId2 = 0;
  lPassIso2 = 0;
  lMt2 = -999.;
  lMet = -999.;
  lMetPhi = -999.;
  lL1Met = -999.;
  lL1MetPhi = -999.;
  lL1MetCorr = -999.;
  lCaloMet = -999.;
  lCaloMetPhi = -999.;
  lCaloMetCorr = -999.;
  lCaloMetPhiCorr = -999.;
  lMVAMet = -999.;
  lMVAMetPhi = -999.;
  lPZetaVis = -999.;
  lPZetaMiss = -999.;
  lMetCov00 = -999.;
  lMetCov01 = -999.;
  lMetCov10 = -999.;
  lMetCov11 = -999.;
  lMVACov00 = -999.;
  lMVACov01 = -999.;
  lMVACov10 = -999.;
  lMVACov11 = -999.;
  lJPt1 = -999.;
  lJEta1 = -999.;
  lJPhi1 = -999.;
  lJPtRaw1 = -999.;
  lJPtUnc1 = -999.;
  lJMVA1 = -999.;
  lLRM1 = -999.;
  lCTM1  = -999;
  lJPass1 = 0;
  lJPt2 = -999.;
  lJEta2 = -999.;
  lJPhi2 = -999.;
  lJPtRaw2 = -999.;
  lJPtUnc2 = -999.;
  lJMVA2 = -999.;
  lLRM2 = -999.;
  lCTM2  = -999;
  lJPass2 = 0;
  lBTagPt = -999.;
  lBTagEta = -999.;
  lBTagPhi = -999.;
  lMJJ = -999.;
  lJDEta = -999.;
  lNJetInGap  = -999;
  lMVA = -999.;
  lJDPhi = -999.;
  lDiJetPt = -999.;
  lDiJetPhi = -999.;
  lHDJetPhi = -999.;
  lVisJetEta = -999.;
  lPtVis = -999.;
  lNBTag  = -999;
  lNJets  = -999;
  lNJetsPt20  = -999;
  em_gf_mva_ = -999.;
  em_vbf_mva_ = -999.;


  //////////////////
  // create a file based on the name and sample

  char fname[1000];
  sprintf(fname,"Sync_SUSYGGH120_Davis_%s.root",NAME_.c_str());
  cout<<" creating a file of name "<<fname<<endl;
  syncFile = new TFile(fname, "RECREATE");
  syncFile->cd();


  ///////////////////
  // create the tree
  syncTree = new TTree("TauCheck", "TauCheck");


  ///////////////////
  // the tree variables
  // were copied directly
  // from https://github.com/ajgilbert/ICHiggsTauTau/blob/master/Analysis/HiggsTauTau/src/HTTSync.cc#L25-L322

  // Run
  syncTree->Branch("run", &lRun, "lRun/I");
  // Lumi
  syncTree->Branch("lumi", &lLumi, "lLumi/I");
  // Event
  syncTree->Branch("evt", &lEvt, "lEvt/I");

  // Number of primary vertices passing good vertex selection
  syncTree->Branch("npv", &lNPV, "lNPV/I");
  // Number of in-time pileup interactions (used for pileup reweighting)
  syncTree->Branch("npu", &lNPU, "lNPU/I");
  // The rho used for jet energy corrections
  syncTree->Branch("rho", &lRho, "lRho/F");

  // The lumi scaling factor for mc * additional weights
  // (not filled in IC trees!)
  syncTree->Branch("mcweight", &lMCWeight, "lMCWeight/F");
  // Pileup weight
  syncTree->Branch("puweight", &lPUWeight, "lPUWeight/F");

  // Tag-and-probe weights for leptons
  // Total trigger weight for lepton 1
  syncTree->Branch("trigweight_1", &lTrigweight_1, "trigweight_1/F");
  // Total trigger weight for lepton 2
  syncTree->Branch("trigweight_2", &lTrigweight_2, "trigweight_2/F");
  // Total ID weight for lepton 1
  syncTree->Branch("idweight_1", &lIdweight_1, "idweight_1/F");
  // Total ID weight for lepton 2
  syncTree->Branch("idweight_2", &lIdweight_2, "idweight_2/F");
  // Total iso weight for lepton 1
  syncTree->Branch("isoweight_1", &lIsoweight_1, "isoweight_1/F");
  // Total iso weight for lepton 2
  syncTree->Branch("isoweight_2", &lIsoweight_2, "isoweight_2/F");
  // Product of all trigger, ID and iso weights
  syncTree->Branch("effweight", &lEffWeight, "lEffWeight/F");
  // Jet->tau fake rate weight (pT-dependent)
  syncTree->Branch("fakeweight", &lFakeWeight, "lFakeWeight/F");
  // Product of all embedded weights, but only for rechit samples
  syncTree->Branch("embeddedWeight", &lEmbeddedWeight, "lEmbeddedWeight/F");
  // Higgs pt weights (for ggh samples)
  syncTree->Branch("signalWeight", &lSignalWeight, "lSignalWeight/F");
  // Total combined event weight (excluding lumi weighting)
  // NB: may contain weights not included in the above
  syncTree->Branch("weight", &lWeight, "lWeight/F");

  // Visible di-tau mass
  syncTree->Branch("mvis", &lMVis, "lMVis/F");
  // SVFit di-tau mass
  syncTree->Branch("m_sv", &lMSV, "lMSV/F");
  // SVFit di-tau pt (only for Markov-Chain SVFit)
  syncTree->Branch("pt_sv", &lPtSV, "lPtSV/F");
  // SVFit di-tau eta (only for Markov-Chain SVFit)
  syncTree->Branch("eta_sv", &lEtaSV, "lEtaSV/F");
  // SVFit di-tau phi (only for Markov-Chain SVFit)
  syncTree->Branch("phi_sv", &lPhiSV, "lPhiSV/F");
  // High energy scale SVFit mass (not filled)
  syncTree->Branch("m_sv_Up", &lMSVUp, "lMSVUp/F");
  // Low energy scale SVFit mass (not filled)
  syncTree->Branch("m_sv_Down", &lMSVDown, "lMSVDown/F");

  // Lepton 1 properties
  // pt (including effect of any energy scale corrections)
  syncTree->Branch("pt_1", &lPt1, "lPt1/F");
  // phi
  syncTree->Branch("phi_1", &lPhi1, "lPhi1/F");
  // eta
  syncTree->Branch("eta_1", &lEta1, "lEta1/F");
  // mass
  syncTree->Branch("m_1", &lM1, "lM1/F");
  // charge
  syncTree->Branch("q_1", &lq1, "lq1/I");
  // delta-beta corrected isolation (relative or absolute as appropriate)
  // If lepton 1 is a tau, this is the value of byIsolationMVAraw,
  // which is no longer used in the analysis, but retained for legacy
  // reasons
  syncTree->Branch("iso_1", &lIso1, "lIso1/F");
  // If an electron, the output of the ID MVA, zero otherwise
  syncTree->Branch("mva_1", &lMVA1, "lMMVA1/F");
  // Transverse (x-y) impact parameter w.r.t to the primary vertex
  syncTree->Branch("d0_1", &lD01, "lD0/F");
  // Longitudinal (z) impact parameter w.r.t to the primary vertex
  syncTree->Branch("dZ_1", &lDZ1, "lDZ/F");
  // Whether lepton passes ID selection (always true in IC ntuples)
  syncTree->Branch("passid_1", &lPassId1, "lPassId1/B");
  // Whether lepton passes iso selection (always true in IC ntuples)
  syncTree->Branch("passiso_1", &lPassIso1, "lPassIso1/B");
  // Transverse mass of lepton 1 and MVA MET
  syncTree->Branch("mt_1", &lMt1, "lMt1/F");

  // Lepton 2 properties
  // pt (including effect of any energy scale corrections)
  syncTree->Branch("pt_2", &lPt2, "lPt2/F");
  // phi
  syncTree->Branch("phi_2", &lPhi2, "lPhi2/F");
  // eta
  syncTree->Branch("eta_2", &lEta2, "lEta2/F");
  // mass
  syncTree->Branch("m_2", &lM2, "lM2/F");
  // charge
  syncTree->Branch("q_2", &lq2, "lq2/I");
  // delta-beta corrected isolation (relative or absolute as appropriate)
  // If lepton 2 is a tau, this is the value of byIsolationMVAraw,
  // which is no longer used in the analysis, but retained for legacy
  // reasons
  syncTree->Branch("iso_2", &lIso2, "lIso2/F");
  // Transverse (x-y) impact parameter w.r.t to the primary vertex
  syncTree->Branch("d0_2", &lD02, "lD02/F");
  // Longitudinal (z) impact parameter w.r.t to the primary vertex
  syncTree->Branch("dZ_2", &lDZ2, "lDZ2/F");
  // If an electron, the output of the ID MVA, zero otherwise
  syncTree->Branch("mva_2", &lMVA2, "lMMVA2/F");
  // Whether lepton passes ID selection (always true in IC ntuples)
  syncTree->Branch("passid_2", &lPassId2, "lPassId2/B");
  // Whether lepton passes iso selection (always true in IC ntuples)
  syncTree->Branch("passiso_2", &lPassIso2, "lPassIso2/B");
  // Transverse mass of lepton 2 and MVA MET
  syncTree->Branch("mt_2", &lMt2, "lMt2/F");

  // Variables defined when lepton 2 is a tau
  // raw value of the 3hits delta-beta isolation
  syncTree->Branch("byCombinedIsolationDeltaBetaCorrRaw3Hits_2", &l3Hits_2,
  "byCombinedIsolationDeltaBetaCorrRaw3Hits_2/F");
  // raw value of the anti-electron MVA3 output
  syncTree->Branch("againstElectronMVA3raw_2", &lagainstElectronMVA3raw_2,
  "againstElectronMVA3raw_2/F");
  // raw value of the MVA2 isolation
  syncTree->Branch("byIsolationMVA2raw_2", &lbyIsolationMVA2raw_2,
  "byIsolationMVA2raw_2/F");
  // output of againstMuonLoose2
  syncTree->Branch("againstMuonLoose2_2", &lagainstMuonLoose2_2,
  "againstMuonLoose2_2/F");
  // output of againstMuonMedium2
  syncTree->Branch("againstMuonMedium2_2", &lagainstMuonMedium2_2,
  "againstMuonMedium2_2/F");
  // output of againstMuonTight2
  syncTree->Branch("againstMuonTight2_2", &lagainstMuonTight2_2,
  "againstMuonTight2_2/F");

  // Uncorrected PF MET (not used in analysis)
  syncTree->Branch("met", &lMet, "lMet/F");
  // Uncorrected PF MET phi (not used in analysis)
  syncTree->Branch("metphi", &lMetPhi, "lMetPhi/F");
  // Elements of the PF MET covariance matrix (not used in analysis)
  syncTree->Branch("metcov00", &lMetCov00, "lMetCov00/F");
  syncTree->Branch("metcov01", &lMetCov01, "lMetCov01/F");
  syncTree->Branch("metcov10", &lMetCov10, "lMetCov10/F");
  syncTree->Branch("metcov11", &lMetCov11, "lMetCov11/F");

  // Following variables used for soft muon + tau + MET analysis
  // L1 MET
  syncTree->Branch("l1met", &lL1Met, "lL1Met/F");
  // L1 MET phi
  syncTree->Branch("l1metphi", &lL1MetPhi, "lL1MetPhi/F");
  // Corrected L1 MET
  syncTree->Branch("l1metcorr", &lL1MetCorr, "lL1Metcorr/F");
  // Calo MET (NoHF)
  syncTree->Branch("calomet", &lCaloMet, "lCaloMet/F");
  // Calo MET phi (NoHF)
  syncTree->Branch("calometphi", &lCaloMetPhi, "lCaloMetPhi/F");
  // Corrected calo MET (NoHF)
  syncTree->Branch("calometcorr", &lCaloMetCorr, "lCaloMetCorr/F");
  // Corrected calo MET phi (NoHF)
  syncTree->Branch("calometphicorr", &lCaloMetPhiCorr, "lCaloMetPhiCorr/F");

  // MVA MET
  syncTree->Branch("mvamet", &lMVAMet, "lMet/F");
  // MVA MET phi
  syncTree->Branch("mvametphi", &lMVAMetPhi, "lMetPhi/F");
  // Elements of the MVA MET covariance matrix
  syncTree->Branch("mvacov00", &lMVACov00, "lMVACov00/F");
  syncTree->Branch("mvacov01", &lMVACov01, "lMVACov01/F");
  syncTree->Branch("mvacov10", &lMVACov10, "lMVACov10/F");
  syncTree->Branch("mvacov11", &lMVACov11, "lMVACov11/F");

  // pt of the di-tau + MET system
  syncTree->Branch("pt_tt", &lPtTT, "lPtTT/F");

  // Visible pzeta
  syncTree->Branch("pzetavis", &lPZetaVis, "lPZetaVis/F");
  // MET pzeta
  syncTree->Branch("pzetamiss", &lPZetaMiss, "lPZetaMiss/F");
  // ttbar-rejection MVA output (emu channel only)
  syncTree->Branch("mva_gf", &em_gf_mva_, "MVAGF/F");
  // ttbar-rejection MVA output for VBF (deprecated)
  syncTree->Branch("mva_vbf", &em_vbf_mva_, "MVAVBF/F");

  // Jet properties
  // The following properties are for the leading (1) and sub-leading (2) jets
  // with pt > 30, |eta| < 4.7 after jet energy corrections, PF jet ID and
  // pileup jet ID are applied. Jets overlapping with either selected lepton
  // are not counted

  // Number of jets passing above selection
  syncTree->Branch("njets", &lNJets, "lNJets/I");
  // Number of jets passing above selection but with
  // pt > 20 instead of pt > 30
  syncTree->Branch("njetspt20", &lNJetsPt20, "lNJetsPt20/I");

  // Leading Jet
  // pt
  syncTree->Branch("jpt_1", &lJPt1, "lJPt1/F");
  // eta
  syncTree->Branch("jeta_1", &lJEta1, "lJEta1/F");
  // phi
  syncTree->Branch("jphi_1", &lJPhi1, "lJPhi1/F");
  // raw pt (before JEC)
  syncTree->Branch("jptraw_1", &lJPtRaw1, "lJPtRaw1/F");
  // pt uncertainty relative to corrected pt (not in IC ntuples)
  syncTree->Branch("jptunc_1", &lJPtUnc1, "lJPtUnc1/F");
  // Pileup ID MVA output
  syncTree->Branch("jmva_1", &lJMVA1, "lJMVA1/F");
  // Linear radial moment (not used in htt analysis)
  syncTree->Branch("jlrm_1", &lLRM1, "lLRM1/F");
  // Charged track multiplicity (not used in htt analysis)
  syncTree->Branch("jctm_1", &lCTM1, "lCTM1/I");
  // True if jet passes MVA pileup ID (deprecated, do not use)
  syncTree->Branch("jpass_1", &lJPass1, "lJPass1/B");

  // Sub-leading Jet
  // pt
  syncTree->Branch("jpt_2", &lJPt2, "lJPt2/F");
  // eta
  syncTree->Branch("jeta_2", &lJEta2, "lJEta2/F");
  // phi
  syncTree->Branch("jphi_2", &lJPhi2, "lJPhi2/F");
  // raw pt (before JEC)
  syncTree->Branch("jptraw_2", &lJPtRaw2, "lJPtRaw2/F");
  // pt uncertainty relative to corrected pt (not in IC ntuples)
  syncTree->Branch("jptunc_2", &lJPtUnc2, "lJPtUnc2/F");
  // Pileup ID MVA output
  syncTree->Branch("jmva_2", &lJMVA2, "lJMVA2/F");
  // Linear radial moment (not used in htt analysis)
  syncTree->Branch("jlrm_2", &lLRM2, "lLRM2/F");
  // Charged track multiplicity (not used in htt analysis)
  syncTree->Branch("jctm_2", &lCTM2, "lCTM2/I");
  // True if jet passes MVA pileup ID (deprecated, do not use)
  syncTree->Branch("jpass_2", &lJPass2, "lJPass2/B");

  // Di-jet properties
  // Calculated with leading and sub-leading jets when njets >= 2
  // di-jet mass
  syncTree->Branch("mjj", &lMJJ, "lMJJ/F");
  // absolute difference in eta
  syncTree->Branch("jdeta", &lJDEta, "lJDEta/F");
  // number of jets, passing above selections, in pseudorapidity gap
  // between jets
  syncTree->Branch("njetingap", &lNJetInGap, "lNJetInGap/I");

  // B-Tagged Jet properties
  // The following properties are for the leading (in pt) CSV medium b-tagged
  // jet with pt > 20, |eta| < 2.4 after jet energy corrections, PF jet ID and
  // pileup jet ID are applied. Jets overlapping with either selected lepton
  // are not counted

  // Number of b-tagging jets passing above selections
  syncTree->Branch("nbtag", &lNBTag, "lNBTag/I");
  // pt
  syncTree->Branch("bpt", &lBTagPt, "lBTagPt/F");
  // eta
  syncTree->Branch("beta", &lBTagEta, "lBTagEta/F");
  // phi
  syncTree->Branch("bphi", &lBTagPhi, "lBTagPhi/F");

  // Variables that go into the VBF MVA
  // Deprecated since HCP 2012
  syncTree->Branch("mva", &lMVA, "lMVA/F");
  // Delta Phi between two leading jets
  syncTree->Branch("jdphi", &lJDPhi, "lJDPhi/F");
  // Pt of the di jet system
  syncTree->Branch("dijetpt", &lDiJetPt, "lDiJetPt/F");
  // Phi of the di jet system
  syncTree->Branch("dijetphi", &lDiJetPhi, "lDiJetPhi/F");
  // Phi of the di jet system - Higgs system phi
  syncTree->Branch("hdijetphi", &lHDJetPhi, "lHDJetPhi/F");
  // TMath::Min(eta_vis - jeta,eta_vis,jeta2);
  syncTree->Branch("visjeteta", &lVisJetEta, "lVisJetEta/F");
  // Pt Vis
  syncTree->Branch("ptvis", &lPtVis, "lPtVis/F");




}


SyncTree::~SyncTree()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
SyncTree::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{


  /////////////////
  // reset variables each
  // event


  lRun = -999;
  lLumi  = -999;
  lEvt = -999;
  lNPV = -999;
  lNPU = -999;
  lRho = -999.;
  lMCWeight = -999.;
  lPUWeight = -999.;
  lFakeWeight = -999.;
  lTrigweight_1 = -999.;
  lTrigweight_2 = -999.;
  lIdweight_1 = -999.;
  lIdweight_2 = -999.;
  lIsoweight_1 = -999.;
  lIsoweight_2 = -999.;
  lEffWeight = -999.;
  lWeight = -999.;
  lEmbeddedWeight = -999.;
  lSignalWeight = -999.;
  lMSV = -999.;
  lPtSV = -999.;
  lEtaSV = -999.;
  lPhiSV = -999.;
  lMVis = -999.;
  lMSVUp = -999.;
  lMSVDown = -999.;
  lPt1 = -999.;
  lPhi1 = -999.;
  lEta1 = -999.;
  lM1 = -999.;
  lq1  = -999;
  lIso1 = -999.;
  lMVA1 = -999.;
  lD01 = -999.;
  lDZ1 = -999.;
  lPassId1 = 0;
  lPassIso1 = 0;
  lMt1 = -999.;
  lPtTT = -999.;
  lPt2 = -999.;
  lPhi2 = -999.;
  lEta2 = -999.;
  lM2 = -999.;
  lq2  = -999;
  lIso2 = -999.;
  lD02 = -999.;
  lDZ2 = -999.;
  l3Hits_2 = -999.;
  lagainstElectronMVA3raw_2 = -999.;
  lbyIsolationMVA2raw_2 = -999.;
  lagainstMuonLoose2_2 = -999.;
  lagainstMuonMedium2_2 = -999.;
  lagainstMuonTight2_2 = -999.;
  lMVA2 = -999.;
  lPassId2 = 0;
  lPassIso2 = 0;
  lMt2 = -999.;
  lMet = -999.;
  lMetPhi = -999.;
  lL1Met = -999.;
  lL1MetPhi = -999.;
  lL1MetCorr = -999.;
  lCaloMet = -999.;
  lCaloMetPhi = -999.;
  lCaloMetCorr = -999.;
  lCaloMetPhiCorr = -999.;
  lMVAMet = -999.;
  lMVAMetPhi = -999.;
  lPZetaVis = -999.;
  lPZetaMiss = -999.;
  lMetCov00 = -999.;
  lMetCov01 = -999.;
  lMetCov10 = -999.;
  lMetCov11 = -999.;
  lMVACov00 = -999.;
  lMVACov01 = -999.;
  lMVACov10 = -999.;
  lMVACov11 = -999.;
  lJPt1 = -999.;
  lJEta1 = -999.;
  lJPhi1 = -999.;
  lJPtRaw1 = -999.;
  lJPtUnc1 = -999.;
  lJMVA1 = -999.;
  lLRM1 = -999.;
  lCTM1  = -999;
  lJPass1 = 0;
  lJPt2 = -999.;
  lJEta2 = -999.;
  lJPhi2 = -999.;
  lJPtRaw2 = -999.;
  lJPtUnc2 = -999.;
  lJMVA2 = -999.;
  lLRM2 = -999.;
  lCTM2  = -999;
  lJPass2 = 0;
  lBTagPt = -999.;
  lBTagEta = -999.;
  lBTagPhi = -999.;
  lMJJ = -999.;
  lJDEta = -999.;
  lNJetInGap  = -999;
  lMVA = -999.;
  lJDPhi = -999.;
  lDiJetPt = -999.;
  lDiJetPhi = -999.;
  lHDJetPhi = -999.;
  lVisJetEta = -999.;
  lPtVis = -999.;
  lNBTag  = -999;
  lNJets  = -999;
  lNJetsPt20  = -999;
  em_gf_mva_ = -999.;
  em_vbf_mva_ = -999.;


  ///////
  // analysis is slightly different depending on
  // what the final state is
  // probably should replace these
  // to avoid duplicate code



  if(NAME_.compare("eTau")==0)
  {

    edm::Handle< TupleElectronTauCollection > eTaus;
    iEvent.getByLabel(leptonTauSrc_, eTaus);

    for (std::size_t i = 0; i < eTaus->size(); ++i)
    {

      const TupleElectronTau eTau =   ((*eTau)[i]);

      /////////////////////
      // basic selection
      // DR > 0.5
      // sum charge = 0
      // MAX = 1 (highest pt pair in the event)
      // pass trigger
      // mt < 30

      bool passAll = 1;
      if( !(eTau.DR()>0.5) ) passAll = 0;
      if( !(eTau.sumCharge()==0) ) passAll = 0;
      if( !(eTau.TransverseMass()<30) ) passAll = 0;
      if( !(eTau.isGoodTriggerPair()==1) ) passAll = 0;
      if( !(eTau.MAX()==1) ) passAll = 0;

      ///////////////////
      // if it has passed all selections
      // fill some plots

      if(passAll==1)
      {


        // Visible di-tau mass
        lmvis = eTau.p4().M();
        // SVFit di-tau mass
        lm_sv = eTau.correctedSVFitMass();
        // MVA MET
        lmvamet = eTau.mvaMET();
        // MVA MET phi
        lmvametphi = eTau.mvaMETphi();


        //////
        // fill the tree

        syncTree->Fill();
      }


    }


  }

  else if(NAME_.compare("muTau")==0)
  {
    edm::Handle< TupleMuonTauCollection > muTaus;
    iEvent.getByLabel(leptonTauSrc_, muTaus);


    for (std::size_t i = 0; i < muTaus->size(); ++i)
    {

      const TupleMuonTau muTau =   ((*muTau)[i]);

      /////////////////////
      // basic selection
      // DR > 0.5
      // sum charge = 0
      // MAX = 1 (highest pt pair in the event)
      // pass trigger
      // mt < 30

      bool passAll = 1;
      if( !(muTau.DR()>0.5) ) passAll = 0;
      if( !(muTau.sumCharge()==0) ) passAll = 0;
      if( !(muTau.TransverseMass()<30) ) passAll = 0;
      if( !(muTau.isGoodTriggerPair()==1) ) passAll = 0;
      if( !(muTau.MAX()==1) ) passAll = 0;


      if(passAll==1)
      {



        // Visible di-tau mass
        lmvis = muTau.p4().M();
        // SVFit di-tau mass
        lm_sv = muTau.correctedSVFitMass();
        // MVA MET
        lmvamet = muTau.mvaMET();
        // MVA MET phi
        lmvametphi = muTau.mvaMETphi();

        //////
        // fill the tree

        syncTree->Fill();
      }


    }


  }


















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
SyncTree::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
SyncTree::endJob()
{
  syncTree->Write();
  syncFile->Close();


}

// ------------ method called when starting to processes a run  ------------
void
SyncTree::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
SyncTree::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
SyncTree::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
SyncTree::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SyncTree::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SyncTree);
