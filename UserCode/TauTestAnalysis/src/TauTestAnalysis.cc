// -*- C++ -*-
//
// Package:    TauTestAnalysis
// Class:      TauTestAnalysis
//
/**\class TauTestAnalysis TauTestAnalysis.cc TEMP/TauTestAnalysis/src/TauTestAnalysis.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Wed Apr 16 11:48:01 CDT 2014
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
#include "DataFormats/PatCandidates/interface/Tau.h"
//
// class declaration
//

class TauTestAnalysis : public edm::EDAnalyzer {
   public:
      explicit TauTestAnalysis(const edm::ParameterSet&);
      ~TauTestAnalysis();

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
      edm::InputTag tauSrc_;
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
TauTestAnalysis::TauTestAnalysis(const edm::ParameterSet& iConfig):
tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("tauSrc" ))
{
   //now do what ever initialization is needed

}


TauTestAnalysis::~TauTestAnalysis()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
TauTestAnalysis::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;


// get tau collection
edm::Handle<edm::View<pat::Tau> > taus;
iEvent.getByLabel(tauSrc_,taus);


int ntau = 0;
for(edm::View<pat::Tau>::const_iterator tau=taus->begin(); tau!=taus->end(); ++tau) {

  ntau++;

          std::cout<<" isTauIDAvailable againstMuonLoose "<<tau->isTauIDAvailable("againstMuonLoose")<<std::endl;
          std::cout<<"  againstMuonLoose = "<<tau->tauID("againstMuonLoose")<<std::endl;
          std::cout<<" byCombinedIsolationDeltaBetaCorrRaw = ";
          std::cout<<tau->tauID("byCombinedIsolationDeltaBetaCorrRaw")<<std::endl;
          std::cout<<" decay mode "<<tau->decayMode()<<std::endl;

                    } // tau loop
  std::cout<<" ntau = "<<ntau<<std::endl;


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
TauTestAnalysis::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TauTestAnalysis::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
void
TauTestAnalysis::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TauTestAnalysis::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TauTestAnalysis::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TauTestAnalysis::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TauTestAnalysis::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TauTestAnalysis);
