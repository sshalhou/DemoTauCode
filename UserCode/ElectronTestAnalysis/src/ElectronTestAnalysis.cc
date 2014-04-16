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
electronSrc_(iConfig.getUntrackedParameter<edm::InputTag>("electronSrc" ))

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


// get muon collection
edm::Handle<edm::View<pat::Electron> > electrons;
iEvent.getByLabel(electronSrc_,electrons);


int nelectrons = 0;

for(edm::View<pat::Electron>::const_iterator electron=electrons->begin(); electron!=electrons->end(); ++electron) {

            nelectrons++;

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
