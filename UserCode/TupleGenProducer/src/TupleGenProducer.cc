// -*- C++ -*-
//
// Package:    TupleGenProducer
// Class:      TupleGenProducer
//
/**\class TupleGenProducer TupleGenProducer.cc TEMP/TupleGenProducer/src/TupleGenProducer.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Wed Sep 10 05:27:46 CDT 2014
// $Id$
//
//


// system include files
#include <memory>
#include <string>
#include <TMath.h>
#include <vector>


// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "UserCode/TupleObjects/interface/TupleGen.h"


typedef math::XYZTLorentzVector LorentzVector;


//
// class declaration
//

class TupleGenProducer : public edm::EDProducer {
public:
  explicit TupleGenProducer(const edm::ParameterSet&);
  ~TupleGenProducer();

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
  std::string NAME_;
  edm::InputTag genSrc_;
  edm::InputTag genTTembeddedSrc_;
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
TupleGenProducer::TupleGenProducer(const edm::ParameterSet& iConfig):
NAME_(iConfig.getParameter<std::string>("NAME" )),
genSrc_(iConfig.getParameter<edm::InputTag>("genSrc" )),
genTTembeddedSrc_(iConfig.getParameter<edm::InputTag>("genTTembeddedSrc" ))
{


  produces< std::vector<TupleGen> >(NAME_).setBranchAlias(NAME_);


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


TupleGenProducer::~TupleGenProducer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TupleGenProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  // get the gen particles

  /////////////////////////
  // this is pretty confusing, but we have 3 cases to consider
  // [1] standard MC --> want genParticles::SIM for everything
  // [2] data dervied embedded Z->tau tau samples --> want genParticles::EmbeddedRECO
  //     for everything
  // -------------------------------
  // -------------------------------
  // 1 and 2  are straight forward since there is only one version of genParticles
  // 3rd case is where issues creep in :
  // [3] mc derived embedded TTbar samples --> want both versions of genParticles,
  // for tau related stuff use genParticles::EmbeddedRECO
  // for top related stuff use genParticles::SIM


  /////////////////
  // gen will be our default case for [1] and [2]

  edm::Handle<std::vector<reco::GenParticle> > gen;
  iEvent.getByLabel(genSrc_, gen);

  ///////////////
  // genTTembedded will be used for case [3]

  edm::Handle<std::vector<reco::GenParticle> > genTTembedded;
  iEvent.getByLabel(genTTembeddedSrc_, genTTembedded);



  ////////////

  std::auto_ptr<TupleGenCollection> TupleGens (new TupleGenCollection);


  if ( gen.isValid() )
  {
    for(size_t mc = 0; mc < gen->size(); ++ mc)
    {
      const reco::GenParticle & genparticle = (*gen)[mc];

      TupleGen CurrentGen;
      CurrentGen.set_p4(genparticle.p4());
      CurrentGen.set_pdgId(genparticle.pdgId());
      int motherID = -999;
      if(genparticle.mother()) motherID = genparticle.mother()->pdgId();

      CurrentGen.set_pdgIdmother(motherID);

      CurrentGen.set_status(genparticle.status());

      ////////////
      // store the CurrentGen
      bool storeIt = 0;
      if(mc<30) storeIt = 1;
      if( abs(genparticle.pdgId())==11) storeIt = 1;
      if( abs(genparticle.pdgId())==13) storeIt = 1;
      if( abs(genparticle.pdgId())==15) storeIt = 1;

      if(storeIt) TupleGens->push_back(CurrentGen);

    }
  }


  if ( genTTembedded.isValid() )
  {
    for(size_t mc = 0; mc < genTTembedded->size(); ++ mc)
    {
      const reco::GenParticle & genparticle = (*genTTembedded)[mc];

      TupleGen CurrentGen;
      CurrentGen.set_p4(genparticle.p4());
      CurrentGen.set_pdgId(genparticle.pdgId());
      int motherID = -999;
      if(genparticle.mother()) motherID = genparticle.mother()->pdgId();

      CurrentGen.set_pdgIdmother(motherID);

      CurrentGen.set_status(genparticle.status());


      ////////////
      // store the CurrentGen
      bool storeIt = 0;
      if(mc<30) storeIt = 1;
      if( abs(genparticle.pdgId())==11) storeIt = 1;
      if( abs(genparticle.pdgId())==13) storeIt = 1;
      if( abs(genparticle.pdgId())==15) storeIt = 1;

      if(storeIt) TupleGens->push_back(CurrentGen);

    

    }
  }


  iEvent.put( TupleGens, NAME_ );


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
TupleGenProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TupleGenProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
TupleGenProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TupleGenProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TupleGenProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TupleGenProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleGenProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleGenProducer);
