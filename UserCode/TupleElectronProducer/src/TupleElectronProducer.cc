// -*- C++ -*-
//
// Package:    TupleElectronProducer
// Class:      TupleElectronProducer
//
/**\class TupleElectronProducer TupleElectronProducer.cc TEMP/TupleElectronProducer/src/TupleElectronProducer.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Tue Jun 24 09:44:10 CDT 2014
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


typedef math::XYZTLorentzVector LorentzVector;
using namespace std;
using namespace edm;



//
// class declaration
//

class TupleElectronProducer : public edm::EDProducer {
public:
  explicit TupleElectronProducer(const edm::ParameterSet&);
  ~TupleElectronProducer();

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

  edm::InputTag electronSrc_;
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
TupleElectronProducer::TupleElectronProducer(const edm::ParameterSet& iConfig):
electronSrc_(iConfig.getParameter<edm::InputTag>("electronSrc" )),
NAME_(iConfig.getParameter<string>("NAME" ))
{


  produces<vector<TupleElectron>>(NAME_).setBranchAlias(NAME_);


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


TupleElectronProducer::~TupleElectronProducer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TupleElectronProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{



  // get electron collection
  edm::Handle<edm::View<pat::Electron> > electrons;
  iEvent.getByLabel(electronSrc_,electrons);

  auto_ptr<TupleElectronCollection> TupleElectrons (new TupleElectronCollection);

  const int TupleElectronSize = electrons->size();
  TupleElectrons->reserve( TupleElectronSize );


  edm::View<pat::Electron>::const_iterator electron;
  for(electron=electrons->begin(); electron!=electrons->end(); ++electron)
  {

    TupleElectron CurrentElectron;

    ////////////////////////////////////////////
    // set electron quantities



    ////////////////
    //set_p4
    ////////////////
    CurrentElectron.set_p4(electron->p4());


    ////////////////
    //set_charge
    ////////////////
    CurrentElectron.set_charge(electron->charge());


    ////////////////
    //set_pfP4
    ////////////////
    CurrentElectron.set_pfP4(electron->pfP4());


    ////////////////
    //set_PFpdgId
    ////////////////
    CurrentElectron.set_PFpdgId(electron->pdgId());


    if(electron->superCluster().isNonnull())
    {
      ////////////////
      //set_SuperClusterEta
      ////////////////
      CurrentElectron.set_SuperClusterEta(electron->superCluster()->position().Eta());
    }
    ////////////////
    //set_isEB
    ////////////////
    CurrentElectron.set_isEB(electron->isEB());


    ////////////////
    //set_isEE
    ////////////////
    CurrentElectron.set_isEE(electron->isEE());

    ////////////////
    //set_isEBEEGap
    ////////////////
    CurrentElectron.set_isEBEEGap(electron->isEBEEGap());

    ////////////////
    //set_isEBEtaGap
    ////////////////
    CurrentElectron.set_isEBEtaGap(electron->isEBEtaGap());

    ////////////////
    //set_isEBPhiGap
    ////////////////
    CurrentElectron.set_isEBPhiGap(electron->isEBPhiGap());

    ////////////////
    //set_isEEDeeGap
    ////////////////
    CurrentElectron.set_isEEDeeGap(electron->isEEDeeGap());

    ////////////////
    //set_isEERingGap
    ////////////////
    CurrentElectron.set_isEERingGap(electron->isEERingGap());

    ////////////////
    //set_sigmaEtaEta
    ////////////////
    CurrentElectron.set_sigmaEtaEta(electron->sigmaEtaEta());

    ////////////////
    //set_sigmaIetaIeta
    ////////////////
    CurrentElectron.set_sigmaIetaIeta(electron->sigmaIetaIeta());

    ////////////////
    //set_sigmaIphiIphi
    ////////////////
    CurrentElectron.set_sigmaIphiIphi(electron->sigmaIphiIphi());


    if(electron->gsfTrack().isNonnull())
    {

      ////////////////
      //set_numberOfMissingInnerHits
      ////////////////
      CurrentElectron.set_numberOfMissingInnerHits(
      electron->gsfTrack()->trackerExpectedHitsInner().numberOfLostHits()
      );

      ////////////////
      //set_dz
      ////////////////
      CurrentElectron.set_dz(electron->gsfTrack()->dz());

    }

    ////////////////
    //set_passConversionVeto
    ////////////////
    CurrentElectron.set_passConversionVeto(electron->passConversionVeto());





    if(electron->genLepton())
    {
      ////////////////
      //set_genP4
      ////////////////
      CurrentElectron.set_genP4(electron->genLepton()->p4());

      ////////////////
      //set_GENpdgId
      ////////////////
      CurrentElectron.set_GENpdgId(electron->genLepton()->pdgId());
    }


    ////////////////
    //set_chargedHadronIso
    ////////////////
    CurrentElectron.set_chargedHadronIso(electron->chargedHadronIso());

    ////////////////
    //set_photonIso
    ////////////////
    CurrentElectron.set_photonIso(electron->photonIso());

    ////////////////
    //set_neutralHadronIso
    ////////////////
    CurrentElectron.set_neutralHadronIso(electron->neutralHadronIso());

    ////////////////
    //set_puChargedHadronIso
    ////////////////
    CurrentElectron.set_puChargedHadronIso(electron->puChargedHadronIso());

    ////////////////
    //set_relativeIso
    ////////////////

    double irel = 0;
    double i_charged = electron->chargedHadronIso();
    double i_photons = electron->photonIso();
    double i_neutralhadrons = electron->neutralHadronIso();
    double i_deltabeta = electron->puChargedHadronIso();
    irel = i_charged + std::max(i_neutralhadrons+i_photons-0.5*i_deltabeta,0.0);
    if(electron->pt()) irel/=electron->pt();
    else irel = 0.0;

    CurrentElectron.set_relativeIso(irel);



    ////////////////
    //set_mvaTrigV0
    ////////////////
    CurrentElectron.set_mvaTrigV0(electron->electronID("mvaTrigV0"));

    ////////////////
    //set_mvaTrigNoIPV0
    ////////////////
    CurrentElectron.set_mvaTrigNoIPV0(electron->electronID("mvaTrigNoIPV0"));

    ////////////////
    //set_mvaNonTrigV0
    ////////////////
    CurrentElectron.set_mvaNonTrigV0(electron->electronID("mvaNonTrigV0"));


    /*

    ////////////////
    //set_pass_tight_mvaNonTrigV0
    ////////////////
    CurrentElectron.set_pass_tight_mvaNonTrigV0(electron->);

    ////////////////
    //set_passFullId
    ////////////////
    CurrentElectron.set_passFullId(electron->);

    */




    ////////////
    // store the electron

    TupleElectrons->push_back(CurrentElectron);

  }


  iEvent.put( TupleElectrons, NAME_ );




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
TupleElectronProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TupleElectronProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
TupleElectronProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TupleElectronProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TupleElectronProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TupleElectronProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleElectronProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleElectronProducer);