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

  std::string NAME_;
  edm::InputTag pileupSrc_;
  edm::InputTag electrontauSrc_;

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
NAME_(iConfig.getParameter<std::string>("NAME" )),
pileupSrc_(iConfig.getParameter<edm::InputTag>("pileupSrc")),
electrontauSrc_(iConfig.getParameter<edm::InputTag>("electrontauSrc"))
{

  produces<std::vector<TupleElectronTauWeight>>(NAME_).setBranchAlias(NAME_);


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

  ///////////////
  // read in electronTaus

  edm::Handle< TupleElectronTauCollection > electronTaus;
  iEvent.getByLabel(electrontauSrc_, electronTaus);


  ////////////////
  // reserve space for
  // the weights

  std::auto_ptr<TupleElectronTauWeightCollection> TupleElectronTauWeights (new TupleElectronTauWeightCollection);

  const int TupleElectronTauWeightsSize = electronTaus->size();
  TupleElectronTauWeights->reserve( TupleElectronTauWeightsSize );



  ////////////////
  // read in pileUpInfo

  edm::Handle<std::vector<PileupSummaryInfo> > PupInfo;
  iEvent.getByLabel(pileupSrc_, PupInfo);


  //////////////////////
  // Since the pileup weight is the same
  // for all pairs compute outside of the loop
  // over pairs

  double puWeight = 1.0;
  double puWeightM1 = 1.0;
  double puWeightP1 = 1.0;
  float NumPileupInt = 1.0;
  float NumTruePileUpInt = 1.0;
  float NumPileupIntM1 = 1.0;
  float NumTruePileUpIntM1 = 1.0;
  float NumPileupIntP1 = 1.0;
  float NumTruePileUpIntP1 = 1.0;

  TupleHelpers::getPileUpWeight(PupInfo, iEvent.isRealData(), puWeight, puWeightM1, puWeightP1,
  NumPileupInt, NumTruePileUpInt, NumPileupIntM1, NumTruePileUpIntM1, NumPileupIntP1, NumTruePileUpIntP1);

  std::cout<<" PU "<<puWeight<<" , "<<puWeightM1<<" , "<<puWeightP1<<" , ";
  std::cout<<NumPileupInt<<" , "<<NumTruePileUpInt<<" , "<<NumPileupIntM1<<" , "<<NumTruePileUpIntM1<<" , ";
  std::cout<<NumPileupIntP1<<" , "<<NumTruePileUpIntP1<<std::endl;




  //////////////////
  // begin loop over electronTaus

  for (std::size_t i = 0; i < electronTaus->size(); ++i)
  {

    const TupleElectronTau electronTau =   ((*electronTaus)[i]);
    TupleElectronTauWeight CurrentElectronTauWeight;

    //////////
    // set pile-up related info

    CurrentElectronTauWeight.set_puWeight(puWeight);
    CurrentElectronTauWeight.set_puWeightM1(puWeightM1);
    CurrentElectronTauWeight.set_puWeightP1(puWeightP1);
    CurrentElectronTauWeight.set_NumPileupInt(NumPileupInt);
    CurrentElectronTauWeight.set_NumTruePileUpInt(NumTruePileUpInt);
    CurrentElectronTauWeight.set_NumPileupIntM1(NumPileupIntM1);
    CurrentElectronTauWeight.set_NumTruePileUpIntM1(NumTruePileUpIntM1);
    CurrentElectronTauWeight.set_NumPileupIntP1(NumPileupIntP1);
    CurrentElectronTauWeight.set_NumTruePileUpIntP1(NumTruePileUpIntP1);

    /////////////
    // add the current pair
    // to the collection



    TupleElectronTauWeights->push_back(CurrentElectronTauWeight);


  }

  iEvent.put( TupleElectronTauWeights, NAME_ );


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
