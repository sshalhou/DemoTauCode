// -*- C++ -*-
//
// Package:    EsCorrectedTauProducer
// Class:      EsCorrectedTauProducer
//
/**\class EsCorrectedTauProducer EsCorrectedTauProducer.cc TEMP/EsCorrectedTauProducer/src/EsCorrectedTauProducer.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Sat Jul 19 04:41:13 CDT 2014
// $Id$
//
//


// system include files
#include <memory>
#include <string>
#include <vector>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"


#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "CommonTools/Utils/interface/StringCutObjectSelector.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "PhysicsTools/PatUtils/interface/TriggerHelper.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "DataFormats/Math/interface/deltaR.h"


typedef math::XYZTLorentzVector LorentzVector;
using namespace std;
using namespace edm;
using namespace pat;

//
// class declaration
//

class EsCorrectedTauProducer : public edm::EDProducer {
public:
  explicit EsCorrectedTauProducer(const edm::ParameterSet&);
  ~EsCorrectedTauProducer();

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
  double TauESshift_;
  string NAME_;



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
EsCorrectedTauProducer::EsCorrectedTauProducer(const edm::ParameterSet& iConfig):
tauSrc_(iConfig.getParameter<edm::InputTag>("tauSrc" )),
TauESshift_(iConfig.getParameter<double>("TauESshift" )),
NAME_(iConfig.getParameter<string>("NAME" ))
{


  produces< vector<pat::Tau> >(NAME_).setBranchAlias(NAME_);


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


EsCorrectedTauProducer::~EsCorrectedTauProducer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
EsCorrectedTauProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{


  // get tau collection
  edm::Handle<edm::View<pat::Tau> > taus;
  iEvent.getByLabel(tauSrc_,taus);

  auto_ptr<vector<pat::Tau>> EsCorrectedTaus (new vector<pat::Tau>);

  std::size_t patTauSize = taus->size();
  EsCorrectedTaus->reserve( patTauSize );


  edm::View<pat::Tau>::const_iterator tau;
  for(tau=taus->begin(); tau!=taus->end(); ++tau)
  {


    //////////
    // new tau
    pat::Tau correctedTau(*tau);

    /////////
    // should write a single function used
    // here and by TupleTau, but for now

    size_t hadrons = 0;
    size_t strips = 0;

    hadrons = tau->signalPFChargedHadrCands().size();
    strips = tau->signalPFGammaCands().size();


    double v4_sf = 1.0;

    /////////////////////
    // 1% correction for improved
    // MSSM analysis if matched to generator
    // level hadronic tau decay

    if ( tau->genJet() && deltaR(tau->p4(), tau->genJet()->p4()) < 0.5 && tau->genJet()->pt() > 8. )
    {

      if((hadrons==1 && strips>0) || (hadrons==1 && strips==0) || (hadrons==3))
      {


        v4_sf *= 1.01;

      }
    }

    //////////////
    // scale the 4-vector
    reco::Candidate::LorentzVector EsCorrectedP4 = tau->p4();
    EsCorrectedP4 *= v4_sf*TauESshift_;

    //////////////////
    // store the new P4

    correctedTau.setP4(EsCorrectedP4);



    /////////
    // store the corrected tau


    EsCorrectedTaus->push_back(correctedTau);

  }


  
  iEvent.put( EsCorrectedTaus, NAME_ );


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
EsCorrectedTauProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
EsCorrectedTauProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
EsCorrectedTauProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
EsCorrectedTauProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
EsCorrectedTauProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
EsCorrectedTauProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
EsCorrectedTauProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(EsCorrectedTauProducer);
