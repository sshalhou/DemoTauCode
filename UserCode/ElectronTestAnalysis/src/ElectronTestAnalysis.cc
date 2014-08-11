// -*- C++ -*-
//
// Package:    ElectronTestAnalysis
// Class:      ElectronTestAnalysis
//
/**\class ElectronTestAnalysis ElectronTestAnalysis.cc TEMP/ElectronTestAnalysis/src/ElectronTestAnalysis.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Wed Apr 16 07:24:59 CDT 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "EgammaAnalysis/ElectronTools/interface/EGammaCutBasedEleId.h"
#include "DataFormats/PatCandidates/interface/Conversion.h"
#include "DataFormats/PatCandidates/interface/Lepton.h"


//
// class declaration
//

class ElectronTestAnalysis : public edm::EDAnalyzer {
   public:
      explicit ElectronTestAnalysis(const edm::ParameterSet&);
      ~ElectronTestAnalysis();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      // ----------member data ---------------------------

      edm::InputTag electronSrc_;
      edm::InputTag gsfelectronSrc_;
      edm::InputTag beamspotSrc_;
      edm::InputTag patconversionSrc_;
      edm::InputTag recoconversionSrc_;

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
ElectronTestAnalysis::ElectronTestAnalysis(const edm::ParameterSet& iConfig):
electronSrc_(iConfig.getUntrackedParameter<edm::InputTag>("electronSrc" )),
gsfelectronSrc_(iConfig.getUntrackedParameter<edm::InputTag>("gsfelectronSrc" )),
beamspotSrc_(iConfig.getUntrackedParameter<edm::InputTag>("beamspotSrc" )),
patconversionSrc_(iConfig.getUntrackedParameter<edm::InputTag>("patconversionSrc" )),
recoconversionSrc_(iConfig.getUntrackedParameter<edm::InputTag>("recoconversionSrc" ))
{
   //now do what ever initialization is needed

}


ElectronTestAnalysis::~ElectronTestAnalysis()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
ElectronTestAnalysis::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;


// get electron collection
edm::Handle<edm::View<pat::Electron> > electrons;
iEvent.getByLabel(electronSrc_,electrons);




// get beamspot
edm::Handle < reco::BeamSpot > beamspot;
iEvent.getByLabel(beamspotSrc_, beamspot);

// get conversions (try pat and reco both)

edm::Handle < edm::View<pat::Conversion> > patconversion;
iEvent.getByLabel(patconversionSrc_, patconversion);

edm::Handle < reco::Conversion > recoconversion;
iEvent.getByLabel(recoconversionSrc_, recoconversion);


std::cout<<" beamspot is valid ? "<<beamspot.isValid()<<std::endl;


int nelectrons = 0;

reco::isodeposit::AbsVetos vetos2012EBPFIdCharged;
reco::isodeposit::AbsVetos vetos2012EBPFIdPhotons;
reco::isodeposit::AbsVetos vetos2012EEPFIdCharged;
reco::isodeposit::AbsVetos vetos2012EEPFIdPhotons;



for(edm::View<pat::Electron>::const_iterator electron=electrons->begin(); electron!=electrons->end(); ++electron) {






            nelectrons++;

std::cout<<" number missing inner hits ";
std::cout<<electron->gsfTrack()->trackerExpectedHitsInner().numberOfLostHits()<<std::endl;

std::cout<<" dxy ";
std::cout<<electron->gsfTrack()->dxy()<<std::endl;

std::cout<<" dz ";
std::cout<<electron->gsfTrack()->dz()<<std::endl;

std::cout<<" eta ";
std::cout<<electron->superCluster()->eta()<<std::endl;

std::cout<<" electronID(mvaNonTrigV0) ";
std::cout<<electron->electronID("mvaNonTrigV0")<<std::endl;

std::cout<<" h/e "<<electron->hadronicOverEm()<<std::endl;


/////// isolation info

double irel = 0;
double i_charged = electron->chargedHadronIso();
double i_photons = electron->photonIso();
double i_neutralhadrons = electron->neutralHadronIso();
double i_deltabeta = electron->puChargedHadronIso();

irel = i_charged + std::max(i_neutralhadrons+i_photons-0.5*i_deltabeta,0.0);

if(electron->pt()) irel/=electron->pt();
else irel = 0.0;

std::cout<<" isolation = "<<irel<<std::endl;
std::cout<<" iso inputs "<<i_charged<<" "<<i_photons<<" "<<i_neutralhadrons<<" "<<i_deltabeta<<std::endl;

////////////
// conversions

  //   bool matchesConv = false;
		//	if (recoconversion.isValid() && beamspot.isValid()) {
			//	matchesConv = ConversionTools::hasMatchedConversion(*electron, recoconversion, beamspot->position());
			//}


std::cout<<" PassConversionVeto = "<<electron->passConversionVeto()<<std::endl;


double inew = 0;



std::cout<<"EB, EE "<<electron->isEB()<<" , "<< electron->isEE() <<std::endl;

std::cout<<" xyz "<<iEvent.id();
std::cout<<" old isolation "<<irel;
std::cout<<" new isolation "<<inew<<std::endl;



          }

std::cout<<" event has "<<nelectrons<<" cleanPatElectrons "<<std::endl;


#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif

#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif
}


// ------------ method called once each job just before starting event loop  ------------
void
ElectronTestAnalysis::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
ElectronTestAnalysis::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
void
ElectronTestAnalysis::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
ElectronTestAnalysis::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
ElectronTestAnalysis::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
ElectronTestAnalysis::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
ElectronTestAnalysis::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(ElectronTestAnalysis);
