// -*- C++ -*-
//
// Package:    TupleUserSpecifiedDataProducer
// Class:      TupleUserSpecifiedDataProducer
//
/**\class TupleUserSpecifiedDataProducer TupleUserSpecifiedDataProducer.cc TEMP/TupleUserSpecifiedDataProducer/src/TupleUserSpecifiedDataProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Fri May 23 09:32:39 CDT 2014
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
#include "UserCode/TupleObjects/interface/TupleUserSpecifiedData.h"

using namespace std;
//
// class declaration
//

class TupleUserSpecifiedDataProducer : public edm::EDProducer {
   public:
      explicit TupleUserSpecifiedDataProducer(const edm::ParameterSet&);
      ~TupleUserSpecifiedDataProducer();

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
      string SampleName_;
      string PhysicsProcess_;
      bool isNonTopEmbeddedSample_;
      bool isTopEmbeddedSample_;
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
TupleUserSpecifiedDataProducer::TupleUserSpecifiedDataProducer(const edm::ParameterSet& iConfig):
SampleName_(iConfig.getParameter<string>("SampleName" )),
PhysicsProcess_(iConfig.getParameter<string>("PhysicsProcess" )),
isNonTopEmbeddedSample_(iConfig.getParameter<bool>("isNonTopEmbeddedSample" )),
isTopEmbeddedSample_(iConfig.getParameter<bool>("isTopEmbeddedSample" ))
{


  produces< vector<TupleUserSpecifiedData> >("TupleUserSpecifiedData").setBranchAlias("TupleUserSpecifiedData");



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


TupleUserSpecifiedDataProducer::~TupleUserSpecifiedDataProducer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TupleUserSpecifiedDataProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{


auto_ptr<TupleUserSpecifiedDataCollection> UserData (new TupleUserSpecifiedDataCollection);
UserData->reserve( 1 );


TupleUserSpecifiedData CurrentTupleUserSpecifiedData;
CurrentTupleUserSpecifiedData.set_SampleName(SampleName_);
CurrentTupleUserSpecifiedData.set_PhysicsProcess(PhysicsProcess_);
CurrentTupleUserSpecifiedData.set_isNonTopEmbeddedSample(isNonTopEmbeddedSample_);
CurrentTupleUserSpecifiedData.set_isTopEmbeddedSample(isTopEmbeddedSample_);


////////////
// store the TupleUserSpecifiedData

UserData->push_back(CurrentTupleUserSpecifiedData);


iEvent.put( UserData, "TupleUserSpecifiedData" );


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
TupleUserSpecifiedDataProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TupleUserSpecifiedDataProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
TupleUserSpecifiedDataProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TupleUserSpecifiedDataProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TupleUserSpecifiedDataProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TupleUserSpecifiedDataProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleUserSpecifiedDataProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleUserSpecifiedDataProducer);
