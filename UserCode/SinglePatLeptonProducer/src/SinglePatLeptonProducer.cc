// -*- C++ -*-
//
// Package:    SinglePatLeptonProducer
// Class:      SinglePatLeptonProducer
//
/**\class SinglePatLeptonProducer SinglePatLeptonProducer.cc TEMP/SinglePatLeptonProducer/src/SinglePatLeptonProducer.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Mon Jul 14 12:35:16 CDT 2014
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

// needed by ntuple electron producer
#include <vector>
#include <iostream>
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "EgammaAnalysis/ElectronTools/interface/EGammaCutBasedEleId.h"
#include "DataFormats/PatCandidates/interface/Conversion.h"
#include "DataFormats/PatCandidates/interface/Lepton.h"
#include "UserCode/TupleObjects/interface/TupleElectron.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "Math/GenVector/VectorUtil.h"
#include "DataFormats/PatCandidates/interface/PFParticle.h"
#include "UserCode/TupleHelpers/interface/TupleHelpers.hh"
#include "PhysicsTools/PatUtils/interface/TriggerHelper.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"


typedef math::XYZTLorentzVector LorentzVector;
using namespace std;
using namespace edm;
using namespace pat;



//
// class declaration
//

class SinglePatLeptonProducer : public edm::EDProducer {
public:
  explicit SinglePatLeptonProducer(const edm::ParameterSet&);
  ~SinglePatLeptonProducer();

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

  // ----------member data ---------------------------

  edm::InputTag electronSrc_;
  edm::InputTag muonSrc_;
  edm::InputTag tauSrc_;
  bool doElectrons_;
  unsigned int electronINDEX_;
  string electronNAME_;
  bool doMuons_;
  unsigned int muonINDEX_;
  string muonNAME_;
  bool doTaus_;
  unsigned int tauINDEX_;
  string tauNAME_;

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
SinglePatLeptonProducer::SinglePatLeptonProducer(const edm::ParameterSet& iConfig):
electronSrc_(iConfig.getParameter<edm::InputTag>("electronSrc" )),
muonSrc_(iConfig.getParameter<edm::InputTag>("muonSrc" )),
tauSrc_(iConfig.getParameter<edm::InputTag>("tauSrc" )),
doElectrons_(iConfig.getParameter<bool>("doElectrons" )),
electronINDEX_(iConfig.getParameter<unsigned int>("electronINDEX" )),
electronNAME_(iConfig.getParameter<string>("electronNAME" )),
doMuons_(iConfig.getParameter<bool>("doMuons" )),
muonINDEX_(iConfig.getParameter<unsigned int>("muonINDEX" )),
muonNAME_(iConfig.getParameter<string>("muonNAME" )),
doTaus_(iConfig.getParameter<bool>("doTaus" )),
tauINDEX_(iConfig.getParameter<unsigned int>("tauINDEX" )),
tauNAME_(iConfig.getParameter<string>("tauNAME" ))
{


  produces<vector<pat::Electron>>(electronNAME_).setBranchAlias(electronNAME_);
  produces<vector<pat::Tau>>(muonNAME_).setBranchAlias(muonNAME_);
  produces<vector<pat::Muon>>(tauNAME_).setBranchAlias(tauNAME_);




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


SinglePatLeptonProducer::~SinglePatLeptonProducer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
SinglePatLeptonProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{


  if(doElectrons_)
  {
    // get electron collection
    edm::Handle<edm::View<pat::Electron> > electrons;
    iEvent.getByLabel(electronSrc_,electrons);

    if(electronINDEX_<electrons->size())
    {


      std::vector<pat::Electron> * storedElectrons = new std::vector<pat::Electron>();
      const pat::Electron & electronToStore = electrons->at(electronINDEX_);
      storedElectrons->push_back(electronToStore);

      // add the electrons to the event output
      std::auto_ptr<std::vector<pat::Electron> > eptr(storedElectrons);
      iEvent.put(eptr,electronNAME_);
    }
  }



  if(doMuons_)
  {
    // get muon collection
    edm::Handle<edm::View<pat::Muon> > muons;
    iEvent.getByLabel(muonSrc_,muons);

    if(muonINDEX_<muons->size())
    {


      std::vector<pat::Muon> * storedMuons = new std::vector<pat::Muon>();
      const pat::Muon & muonToStore = muons->at(muonINDEX_);
      storedMuons->push_back(muonToStore);

      // add the muons to the event output
      std::auto_ptr<std::vector<pat::Muon> > eptr(storedMuons);
      iEvent.put(eptr,muonNAME_);
    }
  }


  if(doTaus_)
  {
    // get tau collection
    edm::Handle<edm::View<pat::Tau> > taus;
    iEvent.getByLabel(tauSrc_,taus);

    if(tauINDEX_<taus->size())
    {


      std::vector<pat::Tau> * storedTaus = new std::vector<pat::Tau>();
      const pat::Tau & tauToStore = taus->at(tauINDEX_);
      storedTaus->push_back(tauToStore);

      // add the taus to the event output
      std::auto_ptr<std::vector<pat::Tau> > eptr(storedTaus);
      iEvent.put(eptr,tauNAME_);
    }
  }



}

// ------------ method called once each job just before starting event loop  ------------
void
SinglePatLeptonProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
SinglePatLeptonProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
SinglePatLeptonProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
SinglePatLeptonProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
SinglePatLeptonProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
SinglePatLeptonProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SinglePatLeptonProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SinglePatLeptonProducer);
