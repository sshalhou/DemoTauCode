// -*- C++ -*-
//
// Package:    TestTriggerAna
// Class:      TestTriggerAna
//
/**\class TestTriggerAna TestTriggerAna.cc TEMP/TestTriggerAna/src/TestTriggerAna.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Fri Jun 27 09:58:43 CDT 2014
// $Id$
//
//


// system include files
#include <memory>
#include <string>
#include <vector>


// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "PhysicsTools/PatUtils/interface/TriggerHelper.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "EgammaAnalysis/ElectronTools/interface/EGammaCutBasedEleId.h"
#include "DataFormats/PatCandidates/interface/Conversion.h"
#include "DataFormats/PatCandidates/interface/Lepton.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"

using namespace edm;
using namespace std;
//
// class declaration
//

class TestTriggerAna : public edm::EDAnalyzer {
public:
  explicit TestTriggerAna(const edm::ParameterSet&);
  ~TestTriggerAna();

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
  edm::InputTag triggerEventSrc_;
  edm::InputTag electronMatchSrc_;


  vector<string> myPaths;



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
TestTriggerAna::TestTriggerAna(const edm::ParameterSet& iConfig):
electronSrc_(iConfig.getUntrackedParameter<edm::InputTag>("electronSrc" )),
triggerEventSrc_(iConfig.getUntrackedParameter<edm::InputTag>("triggerEventSrc" )),
electronMatchSrc_(iConfig.getUntrackedParameter<edm::InputTag>("electronMatchSrc" ))
{
  //now do what ever initialization is needed


/*
myPaths.push_back("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v");
myPaths.push_back("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v");
myPaths.push_back("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v");
myPaths.push_back("HLT_IsoMu18_eta2p1_LooseIsoPFTau20_v");
myPaths.push_back("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v");
myPaths.push_back("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v");
myPaths.push_back("HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v");
myPaths.push_back("HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v");
myPaths.push_back("HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v");
myPaths.push_back("HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v");
myPaths.push_back("HLT_DoubleMediumIsoPFTau25_Trk5_eta2p1_Jet30_v");
myPaths.push_back("HLT_DoubleMediumIsoPFTau30_Trk5_eta2p1_Jet30_v");
myPaths.push_back("HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v");
myPaths.push_back("HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v");
myPaths.push_back("HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v");
myPaths.push_back("HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v");
myPaths.push_back("HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v");
myPaths.push_back("HLT_DoubleMediumIsoPFTau30_Trk5_eta2p1_Jet30_v2");
myPaths.push_back("HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v6");
myPaths.push_back("HLT_Mu17_Mu8_v");
myPaths.push_back("HLT_Mu17_Mu8_v");
myPaths.push_back("HLT_Ele17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v");
myPaths.push_back("HLT_Ele17_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v");
myPaths.push_back("HLT_IsoMu24");
myPaths.push_back("HLT_PFJet320");
*/

myPaths.push_back("HLT_Ele27_WP80");




}


TestTriggerAna::~TestTriggerAna()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
TestTriggerAna::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{


  // get electron collection
  edm::Handle<edm::View<pat::Electron> > electrons;
  iEvent.getByLabel(electronSrc_,electrons);

  // get electrons matched to the HLT_Ele27 trigger
  electronMatchSrc_

   matching information
  const pat::helper::TriggerMatchHelper matchHelper;


  edm::Handle< pat::TriggerEvent > triggerEvent;
  iEvent.getByLabel( triggerEventSrc_, triggerEvent );
  if (triggerEvent.failedToGet())
  {
    std::cout << "WARNING: cannot access triggerEvent for matching" << std::endl;
    return;
  }





  const pat::TriggerPathCollection* paths = triggerEvent->paths();

  cout<<" ------------------ \n";

  for(size_t i = 0; i<myPaths.size(); ++i)
  {


    for (size_t ii = 0; ii < paths->size(); ++ii)
    {

      const pat::TriggerPath& path = paths->at(ii);
      if(path.name().find(myPaths[i])!= std::string::npos)
      {

        if(path.wasAccept())
        {
         std::cout<<" path "<<myPaths[i]<<" found and wasAccept = "<<path.wasAccept();
         std::cout<<" in form "<<path.name()<<"\n";



        }

      }


    }




  }





  //  for (size_t i = 0; i < paths->size(); ++i) {
  //    const pat::TriggerPath& path = paths->at(i);
  //    std::cout<< " accept, prescale, name "<< path.wasAccept()<< " , "
  //     << path.prescale() <<" , "
  //   << path.name() << std::endl;
  //}





//std::cout<<" (accept, run) HLT_Ele80_CaloIdVT_GsfTrkIdT_v1 ";
//std::cout<<triggerEvent->path("HLT_Ele80_CaloIdVT_GsfTrkIdT_v1")->wasAccept()<<" , ";
//std::cout<<triggerEvent->path("HLT_Ele80_CaloIdVT_GsfTrkIdT_v1")->wasRun()<<std::endl;

//std::cout<<" (accept, run) x ";
//std::cout<<triggerEvent->path("x")->wasAccept()<<" , ";
//std::cout<<triggerEvent->path("x")->wasRun()<<std::endl;


/*
std::cout<<" path HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_IsoMu18_eta2p1_LooseIsoPFTau20_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_IsoMu18_eta2p1_LooseIsoPFTau20_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_IsoMu18_eta2p1_LooseIsoPFTau20_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_DoubleMediumIsoPFTau25_Trk5_eta2p1_Jet30_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau25_Trk5_eta2p1_Jet30_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau25_Trk5_eta2p1_Jet30_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_DoubleMediumIsoPFTau30_Trk5_eta2p1_Jet30_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau30_Trk5_eta2p1_Jet30_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau30_Trk5_eta2p1_Jet30_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau30_Trk1_eta2p1_Jet30_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_DoubleMediumIsoPFTau30_Trk5_eta2p1_Jet30_v2 : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau30_Trk5_eta2p1_Jet30_v2")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau30_Trk5_eta2p1_Jet30_v2")->wasAccept()<<std::endl;
std::cout<<" path HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v6 : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v6")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v6")->wasAccept()<<std::endl;


std::cout<<" path HLT_Mu17_Mu8_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_Mu17_Mu8_v")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_Mu17_Mu8_v")->wasAccept()<<std::endl;


std::cout<<" path HLT_Mu17_Mu8_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_Mu17_Mu8_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_Mu17_Mu8_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_Ele17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_Ele17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_Ele17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_Ele17_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v* : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_Ele17_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_Ele17_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*")->wasAccept()<<std::endl;
std::cout<<" path HLT_Ele27_WP80 : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_Ele27_WP80")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_Ele27_WP80")->wasAccept()<<std::endl;
std::cout<<" path HLT_IsoMu24 : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_IsoMu24")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_IsoMu24")->wasAccept()<<std::endl;

std::cout<<" path HLT_PFJet320 : ";
std::cout<<"       wasRun = "<<triggerEvent->path("HLT_PFJet320")->wasRun();
std::cout<<"       wasAccept = "<<triggerEvent->path("HLT_PFJet320")->wasAccept()<<std::endl;

*/




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
TestTriggerAna::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TestTriggerAna::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
void
TestTriggerAna::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TestTriggerAna::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TestTriggerAna::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TestTriggerAna::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TestTriggerAna::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TestTriggerAna);
