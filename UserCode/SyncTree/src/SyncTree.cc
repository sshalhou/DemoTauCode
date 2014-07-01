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

  // Sync Tree Variables
  // Definitions in HTTSync.cc
  int   dummy;


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


  //////////////////
  // create a file based on the name and sample

  char fname[1000];
  sprintf(fname,"Sync_SUSYGGH120_Davis_%s",NAME.c_str());
  cout<<" creating a file of name "<<fname<<endl;



  syncFile = new TFile(fname.c_str(), "RECREATE");
  syncFile->cd();
  // Tree should be named "TauCheck" to aid scripts which
  // make comparisons between sync trees
  syncTree = new TTree("TauCheck", "TauCheck");

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
  using namespace edm;



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
