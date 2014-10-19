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
      edm::InputTag triggerEventSrc_;
      vector<string> eTauAndMuTauPaths;




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
triggerEventSrc_(iConfig.getUntrackedParameter<edm::InputTag>("triggerEventSrc" )),

{

  eTauPaths.push_back("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v");
  eTauPaths.push_back("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v");
  eTauPaths.push_back("HLT_Ele27_WP80");
  muTauPaths.push_back("HLT_IsoMu18_eta2p1_LooseIsoPFTau20_v");
  muTauPaths.push_back("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v");
  muTauPaths.push_back("HLT_IsoMu24");

   //now do what ever initialization is needed

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
  edm::Handle<edm::View<pat::Electron> > electrons;
  iEvent.getByLabel(electronSrc_,electrons);


  // get muon collection
  edm::Handle<edm::View<pat::Muon> > muons;
  iEvent.getByLabel(muonSrc_,muons);

  bool RETURN_VALUE = 0;

//  if(mouns->size()+electrons->size()>1) RETURN_VALUE  = 1;




    // get the trigger info

    edm::Handle< TriggerEvent > triggerEvent;
    iEvent.getByLabel( triggerEventSrc_, triggerEvent );

    // trigger helper
    const pat::helper::TriggerMatchHelper matchHelper;



    /////////////////////
    // eTau  path booleans
    bool eTauPath = 0;


    const pat::TriggerPathCollection* paths = triggerEvent->paths();


    for(size_t i = 0; i<eTauPaths.size(); ++i)
    {
      for (size_t ii = 0; ii < paths->size(); ++ii)
      {

        const pat::TriggerPath& path = paths->at(ii);
        if(path.name().find(eTauPaths[i])!= std::string::npos)
        {

          if(path.wasAccept() && path.wasRun())
          {
            //std::cout<<" path "<<eTauPaths[i]<<" found and wasAccept = "<<path.wasAccept();
            //std::cout<<" in form "<<path.name()<<"\n";
            eTauPath = 1;
          }
        }
      }
    }

  /////////////////////
  // muTau path booleans
  bool muTauPath = 0;


  const pat::TriggerPathCollection* paths = triggerEvent->paths();



  for(size_t i = 0; i<muTauPaths.size(); ++i)
  {
    for (size_t ii = 0; ii < paths->size(); ++ii)
    {

      const pat::TriggerPath& path = paths->at(ii);
      if(path.name().find(muTauPaths[i])!= std::string::npos)
      {

        if(path.wasAccept() && path.wasRun())
        {
          //std::cout<<" path "<<muTauPaths[i]<<" found and wasAccept = "<<path.wasAccept();
          //std::cout<<" in form "<<path.name()<<"\n";
          muTauPath = 1;
        }
      }
    }
  }

  if(muTauPath||eTauPath) RETURN_VALUE = 1;


   return RETURN_VALUE;
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
