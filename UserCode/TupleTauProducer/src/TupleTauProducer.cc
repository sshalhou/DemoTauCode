// -*- C++ -*-
//
// Package:    TupleTauProducer
// Class:      TupleTauProducer
//
/**\class TupleTauProducer TupleTauProducer.cc TEMP/TupleTauProducer/src/TupleTauProducer.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Wed May 14 08:47:40 CDT 2014
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

// needed by ntuple tau producer
#include <vector>
#include <iostream>
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "UserCode/TupleObjects/interface/TupleTau.h"
#include "UserCode/TupleTauProducer/interface/TupleTauProducer.h"

#include "UserCode/TupleObjects/interface/TupleMuon.h"

typedef math::XYZTLorentzVector LorentzVector;
using namespace std;
using namespace edm;


//
// class declaration
//

class TupleTauProducer : public edm::EDProducer {
public:
  explicit TupleTauProducer(const edm::ParameterSet&);
  ~TupleTauProducer();

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
  edm::InputTag tauSrc_;
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
TupleTauProducer::TupleTauProducer(const edm::ParameterSet& iConfig):
tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("tauSrc" ))
{

  produces<vector<TupleTau>>("TupleTaus").setBranchAlias("TupleTaus");



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


TupleTauProducer::~TupleTauProducer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TupleTauProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{



  // get tau collection
  edm::Handle<edm::View<pat::Tau> > taus;
  iEvent.getByLabel(tauSrc_,taus);



  ////////////

  // get tuple muon collection


  edm::Handle<TupleMuonCollection> muons;
  iEvent.getByLabel(muonSrc_, muons);

  std::vector<const TupleMuon*> muonPtrs;
  muonPtrs.reserve(muons->size());

  for (size_t i = 0; i < muons->size(); ++i)
  {

     cout<<"muon x "<<(*muons)[i].pdgId()<<endl;
    //muonPtrs.push_back( &( (*muons)[i] ) );
  }


  ////////////







  auto_ptr<TupleTauCollection> TupleTaus (new TupleTauCollection);

  const int TupleTauSize = taus->size();
  TupleTaus->reserve( TupleTauSize );


  edm::View<pat::Tau>::const_iterator tau;
  for(tau=taus->begin(); tau!=taus->end(); ++tau)
  {

    TupleTau CurrentTau;

    CurrentTau.set_p4(tau->p4());
    CurrentTau.set_corrected_p4(tau->p4(), tau->decayMode());
    CurrentTau.set_pdgId(tau->pdgId());
    CurrentTau.set_charge(tau->charge());
    CurrentTau.set_decayMode(tau->decayMode());




    ////////////
    // store the Tau

    TupleTaus->push_back(CurrentTau);

  }


  iEvent.put( TupleTaus, "TupleTaus" );

  /* This is an event example
  //Read 'ExampleData' from the Event
  Handle<ExampleData> pIn;
  iEvent.getByLabel("example",pIn);

  //Use the ExampleData to create an ExampleData2 which
  // is put into the Event
  std::auto_ptr<ExampleData2> pOut(new ExampleData2(*pIn));
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
TupleTauProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TupleTauProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
TupleTauProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TupleTauProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TupleTauProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TupleTauProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleTauProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleTauProducer);
