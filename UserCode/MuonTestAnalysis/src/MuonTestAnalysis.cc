// -*- C++ -*-
//
// Package:    MuonTestAnalysis
// Class:      MuonTestAnalysis
//
/**\class MuonTestAnalysis MuonTestAnalysis.cc TEMP/MuonTestAnalysis/src/MuonTestAnalysis.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Tue Apr 15 10:35:02 CDT 2014
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

#include "DataFormats/PatCandidates/interface/Muon.h"


#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"



//
// class declaration
//

class MuonTestAnalysis : public edm::EDAnalyzer {
   public:
      explicit MuonTestAnalysis(const edm::ParameterSet&);
      ~MuonTestAnalysis();

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

      edm::InputTag muonSrc_;
      edm::InputTag vertexSrc_;

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
MuonTestAnalysis::MuonTestAnalysis(const edm::ParameterSet& iConfig):
muonSrc_(iConfig.getUntrackedParameter<edm::InputTag>("muonSrc" ))
{
   //now do what ever initialization is needed

}


MuonTestAnalysis::~MuonTestAnalysis()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
MuonTestAnalysis::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

// get muon collection
edm::Handle<edm::View<pat::Muon> > muons;
iEvent.getByLabel(muonSrc_,muons);










//  if( primaryvertex->size() )  pvPtr = pv->ptrAt(0);



  for(edm::View<pat::Muon>::const_iterator muon=muons->begin(); muon!=muons->end(); ++muon) {





std::cout<<" is loose "<<muon->isLooseMuon()<<std::endl;
std::cout<<" is global prompt tight muon "<<muon->isGood("GlobalMuonPromptTight")<<std::endl;
std::cout<<" fabs(dz) = "<<fabs(muon->muonBestTrack()->dz())<<std::endl;

std::cout<<" dxy = "<<(muon->muonBestTrack()->dxy())<<std::endl;


/////// isolation info

double irel = 0;
double i_charged = muon->pfIsolationR04().sumChargedParticlePt;
double i_photons = muon->pfIsolationR04().sumPhotonEt;
double i_neutralhadrons = muon->pfIsolationR04().sumNeutralHadronEt;
double i_deltabeta = muon->pfIsolationR04().sumPUPt;

irel = i_charged + std::max(i_neutralhadrons+i_photons-0.5*i_deltabeta,0.0);

if(muon->pt()) irel/=muon->pt();
else irel = 0.0;

std::cout<<" isolation = "<<irel<<std::endl;



                           } // muons









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
MuonTestAnalysis::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
MuonTestAnalysis::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
void
MuonTestAnalysis::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
MuonTestAnalysis::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
MuonTestAnalysis::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
MuonTestAnalysis::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MuonTestAnalysis::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(MuonTestAnalysis);
