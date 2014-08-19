// -*- C++ -*-
//
// Package:    TupleElectronTauProducer
// Class:      TupleElectronTauProducer
//
/**\class TupleElectronTauProducer TupleElectronTauProducer.cc TEMP/TupleElectronTauProducer/src/TupleElectronTauProducer.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Thu May 15 06:16:07 CDT 2014
// $Id$
//
//


// system include files
#include <memory>
#include <string>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

// needed by ntuple tau producer
#include <vector>
#include <iostream>
#include "DataFormats/Math/interface/LorentzVector.h"
#include "UserCode/TupleObjects/interface/TupleTau.h"
#include "UserCode/TupleObjects/interface/TupleElectron.h"
#include "UserCode/TupleObjects/interface/TupleElectronTau.h"
#include "TauAnalysis/CandidateTools/interface/NSVfitStandaloneAlgorithm.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "Math/GenVector/VectorUtil.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETCollection.h"
#include "UserCode/RecoilCorrector/interface/RecoilCorrector.hh"
#include "UserCode/GenBosonDecayFinder/interface/GenBosonDecayFinder.hh"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "UserCode/TupleHelpers/interface/TupleHelpers.hh"
#include "UserCode/TupleHelpers/interface/BtagSF.hh"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/PileupJetIdentifier.h"
#include "DataFormats/Math/interface/deltaR.h"


//#include "PhysicsTools/SelectorUtils/interface/EventSelector.h"
//#include "PhysicsTools/SelectorUtils/interface/JetIDSelectionFunctor.h"
//#include "PhysicsTools/SelectorUtils/interface/PFJetIDSelectionFunctor.h"







typedef math::XYZTLorentzVector LorentzVector;
typedef std::vector<edm::InputTag> vInputTag;



//
// class declaration
//

class TupleElectronTauProducer : public edm::EDProducer {
public:
  explicit TupleElectronTauProducer(const edm::ParameterSet&);
  ~TupleElectronTauProducer();

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
TupleElectronTauProducer::TupleElectronTauProducer(const edm::ParameterSet& iConfig)
{







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


TupleElectronTauProducer::~TupleElectronTauProducer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TupleElectronTauProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{




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
TupleElectronTauProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TupleElectronTauProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
TupleElectronTauProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TupleElectronTauProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TupleElectronTauProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TupleElectronTauProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleElectronTauProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleElectronTauProducer);
