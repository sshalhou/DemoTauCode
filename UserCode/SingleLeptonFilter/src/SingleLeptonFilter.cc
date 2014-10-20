// -*- C++ -*-
//
// Package:    SingleLeptonFilter
// Class:      SingleLeptonFilter
//
/**\class SingleLeptonFilter SingleLeptonFilter.cc TEST/SingleLeptonFilter/src/SingleLeptonFilter.cc

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

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "PhysicsTools/PatUtils/interface/TriggerHelper.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"

#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"

//
// class declaration
//

class SingleLeptonFilter : public edm::EDFilter {
   public:
      explicit SingleLeptonFilter(const edm::ParameterSet&);
      ~SingleLeptonFilter();

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
      double minPt_;


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
SingleLeptonFilter::SingleLeptonFilter(const edm::ParameterSet& iConfig):
electronSrc_(iConfig.getParameter<edm::InputTag>("electronSrc" )),
muonSrc_(iConfig.getParameter<edm::InputTag>("muonSrc" )),
minPt_(iConfig.getParameter<double>("minPt" ))
{


}


SingleLeptonFilter::~SingleLeptonFilter()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
SingleLeptonFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  // get electron collection
  edm::Handle<edm::View<reco::GsfElectron> > electrons;
  iEvent.getByLabel(electronSrc_,electrons);


  // get muon collection
  edm::Handle<edm::View<reco::Muon> > muons;
  iEvent.getByLabel(muonSrc_,muons);

  bool MUON_PASS = 0;
  bool ELECTRON_PASS = 0;


//  if(muons->size()+electrons->size()>0) RETURN_VALUE  = 1;

  edm::View<reco::GsfElectron>::const_iterator electron;
  for(electron=electrons->begin(); electron!=electrons->end(); ++electron)
  {
    if(electron->p4().pt()>minPt_)
      {
        ELECTRON_PASS = 1;
        break;
      }
  }

  edm::View<reco::Muon>::const_iterator muon;
  for(muon=muons->begin(); muon!=muons->end(); ++muon)
  {
    if(muon->p4().pt()>minPt_)
      {
        MUON_PASS = 1;
        break;
      }
  }


   return (MUON_PASS||ELECTRON_PASS);
}

// ------------ method called once each job just before starting event loop  ------------
void
SingleLeptonFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
SingleLeptonFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool
SingleLeptonFilter::beginRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool
SingleLeptonFilter::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool
SingleLeptonFilter::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool
SingleLeptonFilter::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SingleLeptonFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(SingleLeptonFilter);
