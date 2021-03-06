// -*- C++ -*-
//
// Package:    NtupleMuons
// Class:      NtupleMuons
//
/**\class NtupleMuons NtupleMuons.cc TEMP/NtupleMuons/src/NtupleMuons.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Wed May  7 08:19:29 CDT 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

// needed by ntuple muons producer
#include <vector>
#include <iostream>
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;
using namespace std;
using namespace edm;

//
// class declaration
//

class NtupleMuons : public edm::EDProducer {
public:
  explicit NtupleMuons(const edm::ParameterSet&);
  ~NtupleMuons();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  virtual void beginRun(edm::Run&, edm::EventSetup const&);
  virtual void endRun(edm::Run&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

  // ----------member data ---------------------------
  edm::InputTag muonSrc_;

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
NtupleMuons::NtupleMuons(const edm::ParameterSet& iConfig):
muonSrc_(iConfig.getUntrackedParameter<edm::InputTag>("muonSrc" ))
{


  produces<int>( "muonCount" ).setBranchAlias( "muonCount");
  produces<vector<LorentzVector>>("patmuonP4").setBranchAlias("patmuonP4");
  produces<vector<bool>>("isGlobal").setBranchAlias("isGlobal");


  //register your products
  /* Examples
  produces<ExampleData2>();

  //if do put with a label
  produces<ExampleData2>("label");

  //if you want to put into the Run
  produces<ExampleData2,InRun>();
  */
  //now do what ever other initialization is needed

}


NtupleMuons::~NtupleMuons()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
NtupleMuons::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{



  // get muon collection
  edm::Handle<edm::View<pat::Muon> > muons;
  iEvent.getByLabel(muonSrc_,muons);

  auto_ptr<int> muonCount (new int);
  auto_ptr<vector<LorentzVector>> patmuonP4 (new vector<LorentzVector>);
  auto_ptr<vector<bool>> isGlobal (new vector<bool>);


  const int muonP4size = muons->size();
  patmuonP4->reserve( muonP4size );
  isGlobal->reserve( muonP4size );

  


  edm::View<pat::Muon>::const_iterator muon;
  for(muon=muons->begin(); muon!=muons->end(); ++muon)
  {
   cout<<" is loose "<<muon->isLooseMuon()<<endl;
   cout<<" is loose "<<muon->isLooseMuon()<<endl;


   patmuonP4->push_back(muon->p4());
   isGlobal->push_back(muon->isGood("AllGlobalMuons"));


  }

  *muonCount = muons->size();







  iEvent.put( muonCount, "muonCount" );
  iEvent.put( patmuonP4, "patmuonP4" );
  iEvent.put( isGlobal, "isGlobal" );



  /* This is an event example
  //Read 'ExampleData' from the Event
  Handle<ExampleData> pIn;
  iEvent.getByLabel("example",pIn);

  //Use the ExampleData to create an ExampleData2 which
  // is put into the Event
  auto_ptr<ExampleData2> pOut(new ExampleData2(*pIn));
  iEvent.put(pOut);
  */

  /* this is an EventSetup example
  //Read SetupData from the SetupRecord in the EventSetup
  ESHandle<SetupData> pSetup;
  iSetup.get<SetupRecord>().get(pSetup);
  */

}

// ------------ method called once each job just before starting event loop  ------------
void
NtupleMuons::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
NtupleMuons::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
NtupleMuons::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
NtupleMuons::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
NtupleMuons::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
NtupleMuons::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
NtupleMuons::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(NtupleMuons);
