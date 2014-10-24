// -*- C++ -*-
//
// Package:    SVFitPairFilter
// Class:      SVFitPairFilter
//
/**\class SVFitPairFilter SVFitPairFilter.cc TEST/SVFitPairFilter/src/SVFitPairFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Sun Oct 19 14:26:22 CDT 2014
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
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "UserCode/TupleObjects/interface/TupleMuonTauVetoes.h"


#include "DataFormats/Math/interface/LorentzVector.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "Math/GenVector/VectorUtil.h"
#include "UserCode/TupleHelpers/interface/TupleHelpers.hh"
#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "DataFormats/RecoCandidate/interface/IsoDepositVetos.h"
#include "DataFormats/PatCandidates/interface/Isolation.h"
#include "EgammaAnalysis/ElectronTools/interface/ElectronEffectiveArea.h"

#include "UserCode/TupleObjects/interface/TupleMuonTau.h"
#include "UserCode/TupleObjects/interface/TupleMuon.h"
#include "UserCode/TupleObjects/interface/TupleTau.h"
#include "UserCode/TupleObjects/interface/TupleElectron.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Lepton.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/Math/interface/deltaR.h"


using namespace reco::isodeposit;
typedef math::XYZTLorentzVector LorentzVector;


//
// class declaration
//

class SVFitPairFilter : public edm::EDFilter {
   public:
      explicit SVFitPairFilter(const edm::ParameterSet&);
      ~SVFitPairFilter();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual bool beginRun(edm::Run&, edm::EventSetup const&);
      virtual bool endRun(edm::Run&, edm::EventSetup const&);
      virtual bool beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual bool endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

      // ----------member data ---------------------------
      edm::InputTag electronSrc_;
      edm::InputTag muonSrc_;
      edm::InputTag tauSrcNominal_;
      unsigned int maxElectrons_;
      unsigned int maxMuons_;
      unsigned int maxTaus_;



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
SVFitPairFilter::SVFitPairFilter(const edm::ParameterSet& iConfig):
electronSrc_(iConfig.getParameter<edm::InputTag>("electronSrc" )),
muonSrc_(iConfig.getParameter<edm::InputTag>("muonSrc" )),
tauSrcNominal_(iConfig.getParameter<edm::InputTag>("tauSrcNominal" )),
maxElectrons_(iConfig.getParameter<unsigned int>("maxElectrons" )),
maxMuons_(iConfig.getParameter<unsigned int>("maxMuons" )),
maxTaus_(iConfig.getParameter<unsigned int>("maxTaus" ))

{


}


SVFitPairFilter::~SVFitPairFilter()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
SVFitPairFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  std::size_t lastElectronIndex = min(std::size_t(maxElectrons_),electrons->size());
  std::size_t lastMuonIndex = min(std::size_t(maxMuons_),muons->size());
  std::size_t lastTauIndex = min(std::size_t(maxTaus_),taus->size());


  //////////////
  // read in the TUPLE electrons

  edm::Handle< TupleElectronCollection > electrons;
  iEvent.getByLabel(electronSrc_, electrons);

  //////////////
  // read in the TUPLE muons

  edm::Handle< TupleMuonCollection > muons;
  iEvent.getByLabel(muonSrc_, muons);

  //////////////
  // read in the TUPLE taus

  edm::Handle< TupleTauCollection > taus;
  iEvent.getByLabel(tauSrcNominal_, taus);

  bool ReturnValue = 0;

  int MUON_PASS = 0;
  int ELECTRON_PASS = 0;
  int TAU_eID_PASS = 0;
  int TAU_muID_PASS = 0;

  // loop over tuple electrons
  // and cound number of passing

  for (std::size_t i = 0; i < lastElectronIndex; ++i)
  {
    const TupleElectron electron =   ((*electrons)[i]);
    if(electron.passFullId()) ELECTRON_PASS++;
  }

  // loop over tuple muons
  // and cound number of passing

  for (std::size_t i = 0; i < lastMuonIndex; ++i)
  {
    const TupleMuon muon =   ((*muons)[i]);
    if(muon.passFullId()) MUON_PASS++;
  }

  // loop over tuple taus
  // count number passing eTauId
  // and number passing muTauId

  for (std::size_t j = 0; j < lastTauIndex; ++j)
  {

    const TupleTau tau =   ((*taus)[j]);
    if(tau.passFullId_eTau()) TAU_eID_PASS++;
    if(tau.passFullId_muTau()) TAU_muID_PASS++;

  }



  if(MUON_PASS>0 && TAU_muID_PASS>0) ReturnValue = 1;
  if(ELECTRON_PASS>0 && TAU_eID_PASS>0) ReturnValue = 1;



   return ReturnValue;
}

// ------------ method called once each job just before starting event loop  ------------
void
SVFitPairFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
SVFitPairFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool
SVFitPairFilter::beginRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool
SVFitPairFilter::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool
SVFitPairFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool
SVFitPairFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SVFitPairFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(SVFitPairFilter);
