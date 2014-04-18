// -*- C++ -*-
//
// Package:    PUTestAnalysis
// Class:      PUTestAnalysis
//
/**\class PUTestAnalysis PUTestAnalysis.cc TEMP/PUTestAnalysis/src/PUTestAnalysis.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Fri Apr 18 06:03:16 CDT 2014
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
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
//
// class declaration
//

class PUTestAnalysis : public edm::EDAnalyzer {
   public:
      explicit PUTestAnalysis(const edm::ParameterSet&);
      ~PUTestAnalysis();

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
      edm::InputTag pileupSrc_;

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
PUTestAnalysis::PUTestAnalysis(const edm::ParameterSet& iConfig):
pileupSrc_(iConfig.getUntrackedParameter<edm::InputTag>("pileupSrc" ))

{
   //now do what ever initialization is needed

}


PUTestAnalysis::~PUTestAnalysis()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
PUTestAnalysis::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

//////////////////////
// following https://twiki.cern.ch/twiki/bin/viewauth/CMS/PileupMCReweightingUtilities

LumiReWeighting LumiWeights_;
//std::string data_pileup_root_file =

//const std::string data_pileup_root_file = "/afs/cern.ch/user/a/agilbert/public/HTT_Pileup/13-09-13/Data_Pileup_2012_ReRecoPixel-600bins.root";

//std::string mc_pileup_root_file = "/afs/cern.ch/user/a/agilbert/public/HTT_Pileup/13-09-13/MC_Summer12_PU_S10-600bins.root";

LumiWeights_ = LumiReWeighting("mc_pileup_root_file", "data_pileup_root_file", "pileup", "pileup");

////////////////////////


edm::Handle<std::vector<PileupSummaryInfo> > PupInfo;
iEvent.getByLabel(pileupSrc_, PupInfo);

std::vector<PileupSummaryInfo>::const_iterator PVI;

float Tnpv = -1;
for(PVI = PupInfo->begin(); PVI != PupInfo->end(); ++PVI) {

   int BX = PVI->getBunchCrossing();

   if(BX == 0) {
     Tnpv = PVI->getTrueNumInteractions();
     continue;
   }

}
double MyWeight = 1.0;//LumiWeights_.weight( Tnpv );


std::cout<<" True number of interactions = "<<Tnpv<<" pile-up reweight sf = "<<MyWeight<<std::endl;



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
PUTestAnalysis::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
PUTestAnalysis::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
void
PUTestAnalysis::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
PUTestAnalysis::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
PUTestAnalysis::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
PUTestAnalysis::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PUTestAnalysis::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PUTestAnalysis);
