// -*- C++ -*-
//
// Package:    TupleElectronTauWeightProducer
// Class:      TupleElectronTauWeightProducer
//
/**\class TupleElectronTauWeightProducer TupleElectronTauWeightProducer.cc TempDirect/TupleElectronTauWeightProducer/src/TupleElectronTauWeightProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Garrett Funk
//         Created:  Thu Jul 24 14:46:00 CDT 2014
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

//required for event weight producer
#include <vector>
#include <iostream>
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "EgammaAnalysis/ElectronTools/interface/EGammaCutBasedEleId.h"
#include "DataFormats/PatCandidates/interface/Conversion.h"
#include "DataFormats/PatCandidates/interface/Lepton.h"
#include "UserCode/TupleObjects/interface/TupleTau.h"
#include "UserCode/TupleObjects/interface/TupleElectron.h"
#include "UserCode/TupleObjects/interface/TupleElectronTau.h"
#include "UserCode/TupleObjects/interface/TupleElectronTauWeight.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "Math/GenVector/VectorUtil.h"
#include "DataFormats/PatCandidates/interface/PFParticle.h"
#include "UserCode/TupleHelpers/interface/TupleHelpers.hh"
#include "PhysicsTools/PatUtils/interface/TriggerHelper.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "TF1.h"
#include "TH1.h"
#include "TMath.h"

typedef math::XYZTLorentzVector LorentzVector;


//
// class declaration
//

class TupleElectronTauWeightProducer : public edm::EDProducer
{
   public:
      explicit TupleElectronTauWeightProducer(const edm::ParameterSet&);
      ~TupleElectronTauWeightProducer();
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

    string NAME_;
    edm::InputTag pileupSrc_;

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

TupleElectronTauWeightProducer::TupleElectronTauWeightProducer(const edm::ParameterSet& iConfig):
pileupSrc_(iConfig.getParameter<edm::InputTag>("pileupSrc"))
{

    produces<vector<TupleElectronTauWeight>>(NAME_).setBranchAlias(NAME_);




}


TupleElectronTauWeightProducer::~TupleElectronTauWeightProducer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}

//
// member functions
//


// ------------ method called to produce the data  ------------
void
TupleElectronTauWeightProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

}

// ------------ method called once each job just before starting event loop  ------------
void
TupleElectronTauWeightProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TupleElectronTauWeightProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
TupleElectronTauWeightProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TupleElectronTauWeightProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TupleElectronTauWeightProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TupleElectronTauWeightProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleElectronTauWeightProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleElectronTauWeightProducer);
