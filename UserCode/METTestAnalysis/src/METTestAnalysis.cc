// -*- C++ -*-
//
// Package:    METTestAnalysis
// Class:      METTestAnalysis
//
/**\class METTestAnalysis METTestAnalysis.cc TEMP/METTestAnalysis/src/METTestAnalysis.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Thu Apr 17 07:41:34 CDT 2014
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
#include "DataFormats/PatCandidates/interface/MET.h"
//#include "DataFormats/METReco/interface/MET.h"
//#include "DataFormats/METReco/interface/PFMET.h"
//
// class declaration
//





class METTestAnalysis : public edm::EDAnalyzer {
   public:
      explicit METTestAnalysis(const edm::ParameterSet&);
      ~METTestAnalysis();

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

      edm::InputTag mvametSrc_;
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
METTestAnalysis::METTestAnalysis(const edm::ParameterSet& iConfig):
mvametSrc_(iConfig.getUntrackedParameter<edm::InputTag>("mvametSrc" ))

{
   //now do what ever initialization is needed

}


METTestAnalysis::~METTestAnalysis()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
METTestAnalysis::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;



// get mvamet collection
//edm::Handle<edm::View<pat::MET> > mvamet;
//iEvent.getByLabel(mvametSrc_,mvamet);

    edm::Handle<std::vector<pat::MET> > mvamet;
    iEvent.getByLabel(mvametSrc_, mvamet);

  for( std::vector<pat::MET>::const_iterator it = mvamet->begin(); it != mvamet->end(); ++it )
    {

  std::cout<<" met pt : "<<it->pt()<<std::endl;
  std::cout<<" met phi : "<<it->phi()<<std::endl;
  std::cout<<" met sumEt : "<<it->sumEt()<<std::endl;
  std::cout<<it->getSignificanceMatrix()(0,0)<<" ";
  std::cout<<it->getSignificanceMatrix()(0,1);
  std::cout<<it->getSignificanceMatrix()(1,0)<<" ";
  std::cout<<it->getSignificanceMatrix()(0,1)<<std::endl;


    }

/*
std::cout<<" mva pf met = "<<(*mvamet)[0].pt()<<std::endl;
std::cout<<" [0,0] "<<(*mvamet)[0].getSignificanceMatrix()(0,0)<<" ";
std::cout<<" [0,1] "<<(*mvamet)[0].getSignificanceMatrix()(0,1)<<" ";
std::cout<<" [1,0] "<<(*mvamet)[0].getSignificanceMatrix()(1,0)<<" ";
std::cout<<" [1,1] "<<(*mvamet)[0].getSignificanceMatrix()(1,1)<<" ";
*/

//histContainer_["met"  ]->Fill(mets->empty() ? 0 : (*mets)[0].et());

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
METTestAnalysis::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
METTestAnalysis::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
void
METTestAnalysis::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
METTestAnalysis::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
METTestAnalysis::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
METTestAnalysis::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
METTestAnalysis::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(METTestAnalysis);
