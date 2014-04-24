// -*- C++ -*-
//
// Package:    JetTestAnalysis
// Class:      JetTestAnalysis
//
/**\class JetTestAnalysis JetTestAnalysis.cc TEMP/JetTestAnalysis/src/JetTestAnalysis.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Thu Apr 24 07:09:45 CDT 2014
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

#include "DataFormats/PatCandidates/interface/Jet.h"
#include "CMGTools/External/interface/PileupJetIdentifier.h"
//
// class declaration
//

class JetTestAnalysis : public edm::EDAnalyzer {
   public:
      explicit JetTestAnalysis(const edm::ParameterSet&);
      ~JetTestAnalysis();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endluminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      // ----------member data ---------------------------

edm::InputTag jetSrc_;
edm::InputTag puJetIdMVASrc_;
edm::InputTag puJetIdFlagSrc_;

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
JetTestAnalysis::JetTestAnalysis(const edm::ParameterSet& iConfig):
jetSrc_(iConfig.getUntrackedParameter<edm::InputTag>("jetSrc" )),
puJetIdMVASrc_(iConfig.getUntrackedParameter<edm::InputTag>("puJetIdMVASrc" )),
puJetIdFlagSrc_(iConfig.getUntrackedParameter<edm::InputTag>("puJetIdFlagSrc" ))
{
   //now do what ever initialization is needed

}


JetTestAnalysis::~JetTestAnalysis()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
JetTestAnalysis::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;







edm::Handle<edm::View<pat::Jet> > jets;
iEvent.getByLabel(jetSrc_,jets);

Handle<ValueMap<float> > puJetIdMVA;
iEvent.getByLabel(puJetIdMVASrc_,puJetIdMVA);

Handle<ValueMap<int> > puJetIdFlag;
iEvent.getByLabel(puJetIdFlagSrc_,puJetIdFlag);



for ( unsigned int i=0; i<jets->size(); ++i ) {
      const pat::Jet & patjet = jets->at(i);
      float mva   = (*puJetIdMVA)[jets->refAt(i)];
      int    idflag = (*puJetIdFlag)[jets->refAt(i)];
      std::cout << "jet " << i << " pt " << patjet.pt() << " eta " << patjet.eta() << " PU JetID MVA " << mva;
//      if( PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kLoose ) {
//           std::cout << " pass loose wp";
//      }
//      if( PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kMedium ) {
//           std::cout << " pass medium wp";
//      }
//      if( PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kTight ) {
//           std::cout << " pass tight wp";
  //    }
  //    std::cout << std::endl;
}




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
JetTestAnalysis::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
JetTestAnalysis::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
void
JetTestAnalysis::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
JetTestAnalysis::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
JetTestAnalysis::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
JetTestAnalysis::endluminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
JetTestAnalysis::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetTestAnalysis);
