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
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "TMath.h"
#include "PhysicsTools/PatUtils/interface/TriggerHelper.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"


#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "EgammaAnalysis/ElectronTools/interface/EGammaCutBasedEleId.h"
#include "DataFormats/PatCandidates/interface/Conversion.h"
#include "DataFormats/PatCandidates/interface/Lepton.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"

using namespace edm;
using namespace std;
using namespace pat;

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
  edm::InputTag muonSrc_;
  edm::InputTag tauSrc_;
  edm::InputTag triggerEventSrc_;

  std::string eTrigMatchEle20Src_;
  std::string eTrigMatchEle22Src_;
  std::string eTrigMatchEle27Src_;
  std::string muTrigMatchMu17Src_;
  std::string muTrigMatchMu18Src_;
  std::string muTrigMatchMu24Src_;
  std::string tauTrigMatchMu17Src_;
  std::string tauTrigMatchMu18Src_;
  std::string tauTrigMatchMu24Src_;
  std::string tauTrigMatchEle20Src_;
  std::string tauTrigMatchEle22Src_;
  std::string tauTrigMatchEle27Src_;

  vector<string> eTauPaths;
  vector<string> muTauPaths;



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
muonSrc_(iConfig.getUntrackedParameter<edm::InputTag>("muonSrc" )),
tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("tauSrc" )),
triggerEventSrc_(iConfig.getUntrackedParameter<edm::InputTag>("triggerEventSrc" )),
eTrigMatchEle20Src_(iConfig.getUntrackedParameter<std::string>("eTrigMatchEle20Src" )),
eTrigMatchEle22Src_(iConfig.getUntrackedParameter<std::string>("eTrigMatchEle22Src" )),
eTrigMatchEle27Src_(iConfig.getUntrackedParameter<std::string>("eTrigMatchEle27Src" )),
muTrigMatchMu17Src_(iConfig.getUntrackedParameter<std::string>("muTrigMatchMu17Src" )),
muTrigMatchMu18Src_(iConfig.getUntrackedParameter<std::string>("muTrigMatchMu18Src" )),
muTrigMatchMu24Src_(iConfig.getUntrackedParameter<std::string>("muTrigMatchMu24Src" )),
tauTrigMatchMu17Src_(iConfig.getUntrackedParameter<std::string>("tauTrigMatchMu17Src" )),
tauTrigMatchMu18Src_(iConfig.getUntrackedParameter<std::string>("tauTrigMatchMu18Src" )),
tauTrigMatchMu24Src_(iConfig.getUntrackedParameter<std::string>("tauTrigMatchMu24Src" )),
tauTrigMatchEle20Src_(iConfig.getUntrackedParameter<std::string>("tauTrigMatchEle20Src" )),
tauTrigMatchEle22Src_(iConfig.getUntrackedParameter<std::string>("tauTrigMatchEle22Src" )),
tauTrigMatchEle27Src_(iConfig.getUntrackedParameter<std::string>("tauTrigMatchEle27Src" ))
{
  //now do what ever initialization is needed


  eTauPaths.push_back("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v");
  eTauPaths.push_back("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v");
  eTauPaths.push_back("HLT_Ele27_WP80");


  muTauPaths.push_back("HLT_IsoMu18_eta2p1_LooseIsoPFTau20_v");
  muTauPaths.push_back("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v");
  muTauPaths.push_back("HLT_IsoMu24");





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


  // get electron, muon, and tau collections

  edm::Handle< ElectronCollection > electrons;
  iEvent.getByLabel( electronSrc_, electrons );

  edm::Handle< MuonCollection > muons;
  iEvent.getByLabel( muonSrc_, muons );

  edm::Handle< TauCollection > taus;
  iEvent.getByLabel( tauSrc_, taus );

  // get the trigger info

  edm::Handle< TriggerEvent > triggerEvent;
  iEvent.getByLabel( triggerEventSrc_, triggerEvent );



  // trigger helper
  const pat::helper::TriggerMatchHelper matchHelper;




  /////////////////////
  // eTau and muTau path booleans
  bool eTauPath = 0;
  bool muTauPath = 0;


  const pat::TriggerPathCollection* paths = triggerEvent->paths();

  cout<<" --------checking eTau Paths ---------- \n";

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

  cout<<" --------checking muTau Paths ---------- \n";

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



  std::cout<<" muTauPath, eTauPath = "<<muTauPath<<" , "<<eTauPath<<std::endl;


  //////////////////////////////////
  // if eTauPath find the electron!
  ///////////////////////////////////



  for(size_t electron_id = 0; electron_id < electrons->size(); ++electron_id)
  {

    const pat::TriggerObjectRef trigRefEle20(
    matchHelper.triggerMatchObject( electrons, electron_id, eTrigMatchEle20Src_, iEvent, *triggerEvent ) );
    const pat::TriggerObjectRef trigRefEle22(
    matchHelper.triggerMatchObject( electrons, electron_id, eTrigMatchEle22Src_, iEvent, *triggerEvent ) );
    const pat::TriggerObjectRef trigRefEle27(
    matchHelper.triggerMatchObject( electrons, electron_id, eTrigMatchEle27Src_, iEvent, *triggerEvent ) );


    if( trigRefEle20.isAvailable() )
    {
      cout<<" e trig ref 20 available \n";
    }

    if( trigRefEle22.isAvailable() )
    {
      cout<<" e trig ref 22 available \n";
    }

    if( trigRefEle27.isAvailable() )
    {
      cout<<" e trig ref 27 available \n";
    }

  }


  for(size_t muon_id = 0; muon_id < muons->size(); ++muon_id)
  {

    const pat::TriggerObjectRef trigRefMu17(
    matchHelper.triggerMatchObject( muons, muon_id, muTrigMatchMu17Src_, iEvent, *triggerEvent ) );
    const pat::TriggerObjectRef trigRefMu28(
    matchHelper.triggerMatchObject( muons, muon_id, muTrigMatchMu18Src_, iEvent, *triggerEvent ) );
    const pat::TriggerObjectRef trigRefMu24(
    matchHelper.triggerMatchObject( muons, muon_id, muTrigMatchMu24Src_, iEvent, *triggerEvent ) );


    if( trigRefMu17.isAvailable() )
    {
      cout<<" muon trig ref 17 available \n";
    }

    if( trigRefMu18.isAvailable() )
    {
      cout<<" muon trig ref 18 available \n";
    }

    if( trigRefMu24.isAvailable() )
    {
      cout<<" muon trig ref 24 available \n";
    }

  }



  for(size_t tau_id = 0; tau_id < taus->size(); ++tau_id)
  {

    const pat::TriggerObjectRef tauTrigRefEle20(
    matchHelper.triggerMatchObject( taus, tau_id, tauTrigMatchEle20Src_, iEvent, *triggerEvent ) );
    const pat::TriggerObjectRef tauTrigRefEle22(
    matchHelper.triggerMatchObject( taus, tau_id, tauTrigMatchEle22Src_, iEvent, *triggerEvent ) );
    const pat::TriggerObjectRef tauTrigRefEle27(
    matchHelper.triggerMatchObject( taus, tau_id, tauTrigMatchEle27Src_, iEvent, *triggerEvent ) );
    const pat::TriggerObjectRef tauTrigRefMu17(
    matchHelper.triggerMatchObject( muons, muon_id, tauTrigMatchMu17Src_, iEvent, *triggerEvent ) );
    const pat::TriggerObjectRef tauTrigRefMu28(
    matchHelper.triggerMatchObject( muons, muon_id, tauTrigMatchMu18Src_, iEvent, *triggerEvent ) );
    const pat::TriggerObjectRef tauTrigRefMu24(
    matchHelper.triggerMatchObject( muons, muon_id, tauTrigMatchMu24Src_, iEvent, *triggerEvent ) );


    if( tauTrigRefMu17.isAvailable() )
    {
      cout<<" tau trig ref 17 available \n";
    }

    if( tauTrigRefMu18.isAvailable() )
    {
      cout<<" tau trig ref 18 available \n";
    }

    if( tauTrigRefMu24.isAvailable() )
    {
      cout<<" tau trig ref 24 available \n";
    }


    if( tauTrigRefEle20.isAvailable() )
    {
      cout<<" tau trig ref 20 available \n";
    }

    if( tauTrigRefEle22.isAvailable() )
    {
      cout<<" tau trig ref 22 available \n";
    }

    if( tauTrigRefEle27.isAvailable() )
    {
      cout<<" tau trig ref 27 available \n";
    }


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
