// -*- C++ -*-
//
// Package:    TupleTauProducer
// Class:      TupleTauProducer
//
/**\class TupleTauProducer TupleTauProducer.cc TEMP/TupleTauProducer/src/TupleTauProducer.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Wed May 14 08:47:40 CDT 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

// needed by ntuple tau producer
#include <vector>
#include <iostream>
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "UserCode/TupleObjects/interface/TupleTau.h"
#include "UserCode/TupleTauProducer/interface/TupleTauProducer.h"

#include "UserCode/TupleObjects/interface/TupleMuon.h"
#include "PhysicsTools/PatUtils/interface/TriggerHelper.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"

typedef math::XYZTLorentzVector LorentzVector;
using namespace std;
using namespace edm;
using namespace pat;


//
// class declaration
//

class TupleTauProducer : public edm::EDProducer {
public:
  explicit TupleTauProducer(const edm::ParameterSet&);
  ~TupleTauProducer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  virtual void beginRun(edm::Run&, edm::EventSetup const&);
  virtual void endRun(edm::Run&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

  // ----------member data ---------------------------
  edm::InputTag tauSrc_;
  string NAME_;
  edm::InputTag triggerEventSrc_;
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
TupleTauProducer::TupleTauProducer(const edm::ParameterSet& iConfig):
tauSrc_(iConfig.getParameter<edm::InputTag>("tauSrc" )),
NAME_(iConfig.getParameter<string>("NAME" )),
triggerEventSrc_(iConfig.getUntrackedParameter<edm::InputTag>("triggerEventSrc" )),
tauTrigMatchMu17Src_(iConfig.getUntrackedParameter<std::string>("tauTrigMatchMu17Src" )),
tauTrigMatchMu18Src_(iConfig.getUntrackedParameter<std::string>("tauTrigMatchMu18Src" )),
tauTrigMatchMu24Src_(iConfig.getUntrackedParameter<std::string>("tauTrigMatchMu24Src" )),
tauTrigMatchEle20Src_(iConfig.getUntrackedParameter<std::string>("tauTrigMatchEle20Src" )),
tauTrigMatchEle22Src_(iConfig.getUntrackedParameter<std::string>("tauTrigMatchEle22Src" )),
tauTrigMatchEle27Src_(iConfig.getUntrackedParameter<std::string>("tauTrigMatchEle27Src" ))
{


  eTauPaths.push_back("HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v");
  eTauPaths.push_back("HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v");
  eTauPaths.push_back("HLT_Ele27_WP80");


  muTauPaths.push_back("HLT_IsoMu18_eta2p1_LooseIsoPFTau20_v");
  muTauPaths.push_back("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v");
  muTauPaths.push_back("HLT_IsoMu24");


  produces< vector<TupleTau> >(NAME_).setBranchAlias(NAME_);



  //register your products
  /* Examples
  produces<ExampleData2>();

  //if do put with a label
  produces<ExampleData2>("label");

  //if you want to put into the Run
  produces<ExampleData2,InRun>();
  */
  //now do what ever other initialization is needed

}


TupleTauProducer::~TupleTauProducer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TupleTauProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{



  // get tau collection
  edm::Handle<edm::View<pat::Tau> > taus;
  iEvent.getByLabel(tauSrc_,taus);




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








  auto_ptr<TupleTauCollection> TupleTaus (new TupleTauCollection);

  const int TupleTauSize = taus->size();
  TupleTaus->reserve( TupleTauSize );


  edm::View<pat::Tau>::const_iterator tau;
  for(tau=taus->begin(); tau!=taus->end(); ++tau)
  {

    TupleTau CurrentTau;




    /////////////////
    // check the trigger matches

    if(eTauPath==1)
    {
      size_t tau_id =  tau - taus->begin();

      const pat::TriggerObjectRef trigRefEle20(
      matchHelper.triggerMatchObject( taus, tau_id, tauTrigMatchEle20Src_, iEvent, *triggerEvent ) );
      const pat::TriggerObjectRef trigRefEle22(
      matchHelper.triggerMatchObject( taus, tau_id, tauTrigMatchEle22Src_, iEvent, *triggerEvent ) );
      const pat::TriggerObjectRef trigRefEle27(
      matchHelper.triggerMatchObject( taus, tau_id, tauTrigMatchEle27Src_, iEvent, *triggerEvent ) );


      if( trigRefEle20.isAvailable() && trigRefEle20.isNonnull()) CurrentTau.set_has_HltMatchEle20(1);
      if( trigRefEle22.isAvailable() && trigRefEle22.isNonnull()) CurrentTau.set_has_HltMatchEle22(1);

      // I am not sure this trigger even has a tau leg
      //if( trigRefEle27.isAvailable() && trigRefEle27.isNonnull()) CurrentTau.set_has_HltMatchEle27(1);
      CurrentTau.set_has_HltMatchEle27(1);

    }


    if(muTauPath==1)
    {
      size_t tau_id =  tau - taus->begin();

      const pat::TriggerObjectRef trigRefMu17(
      matchHelper.triggerMatchObject( taus, tau_id, tauTrigMatchMu17Src_, iEvent, *triggerEvent ) );
      const pat::TriggerObjectRef trigRefMu18(
      matchHelper.triggerMatchObject( taus, tau_id, tauTrigMatchMu18Src_, iEvent, *triggerEvent ) );
      const pat::TriggerObjectRef trigRefMu24(
      matchHelper.triggerMatchObject( taus, tau_id, tauTrigMatchMu24Src_, iEvent, *triggerEvent ) );


      if( trigRefMu17.isAvailable() && trigRefMu17.isNonnull()) CurrentTau.set_has_HltMatchMu17(1);
      if( trigRefMu18.isAvailable() && trigRefMu18.isNonnull()) CurrentTau.set_has_HltMatchMu18(1);
      // I am not sure this trigger even has a tau leg
      //if( trigRefMu24.isAvailable() && trigRefMu24.isNonnull()) CurrentTau.set_has_HltMatchMu24(1);
      CurrentTau.set_has_HltMatchMu24(1);

    }




    std::cout<<" SETTING TAU PT TO "<<tau->p4().pt()<<std::endl;
    CurrentTau.set_p4(tau->p4());

    //////////////
    // apply tau ES correction
    // we will keep both p4 and corrected p4


    std::cout<<" gen lepton "<<tau->genLepton()<<" is real data "<<iEvent.isRealData()<<std::endl;
    std::cout<<" Warning need to add in a MC sample check "<<std::endl;
    // correct the tau energy
    if(tau->genLepton())
    {
      std::cout<<" embedded gen particle exists, correcting tau energy"<<std::endl;
      CurrentTau.set_corrected_p4(tau->p4(), tau->decayMode(), tau->genLepton()->pdgId());
    }
    else if (iEvent.isRealData())
    {
      std::cout<<" real data, not applying a tau energy correction"<<std::endl;
      CurrentTau.set_corrected_p4(tau->p4(), 0, 0);
    }


    // need to be careful here with pdgIds, as it seems the one accessed
    // below is the pf's pdgId which is filled for data and MC
    // the generator pdgId for MC must be accessed from genParticle
    CurrentTau.set_pdgId(tau->pdgId());

    // store the generator level 4-vector


    if(tau->genLepton())
    {
      CurrentTau.set_genP4(tau->genLepton()->p4());
    }


    CurrentTau.set_charge(tau->charge());
    CurrentTau.set_decayMode(tau->decayMode());


    ////////////////////////
    // fill the tau discriminators
    float disc = 0.0;


    disc=tau->tauID("againstElectronDeadECAL");
    CurrentTau.set_againstElectronDeadECAL(disc);

    //////////////////////
    disc=tau->tauID("againstElectronLoose");
    CurrentTau.set_againstElectronLoose(disc);

    //////////////////////
    disc=tau->tauID("againstElectronLooseMVA5");
    CurrentTau.set_againstElectronLooseMVA5(disc);

    //////////////////////
    disc=tau->tauID("againstElectronMVA5category");
    CurrentTau.set_againstElectronMVA5category(disc);

    //////////////////////
    disc=tau->tauID("againstElectronMVA5raw");
    CurrentTau.set_againstElectronMVA5raw(disc);

    //////////////////////
    disc=tau->tauID("againstElectronMedium");
    CurrentTau.set_againstElectronMedium(disc);

    //////////////////////
    disc=tau->tauID("againstElectronMediumMVA5");
    CurrentTau.set_againstElectronMediumMVA5(disc);

    //////////////////////
    disc=tau->tauID("againstElectronTight");
    CurrentTau.set_againstElectronTight(disc);

    //////////////////////
    disc=tau->tauID("againstElectronTightMVA5");
    CurrentTau.set_againstElectronTightMVA5(disc);

    //////////////////////
    disc=tau->tauID("againstElectronVLooseMVA5");
    CurrentTau.set_againstElectronVLooseMVA5(disc);

    //////////////////////
    disc=tau->tauID("againstElectronVTightMVA5");
    CurrentTau.set_againstElectronVTightMVA5(disc);

    //////////////////////
    disc=tau->tauID("againstMuonLoose");
    CurrentTau.set_againstMuonLoose(disc);

    //////////////////////
    disc=tau->tauID("againstMuonLoose2");
    CurrentTau.set_againstMuonLoose2(disc);

    //////////////////////
    disc=tau->tauID("againstMuonLoose3");
    CurrentTau.set_againstMuonLoose3(disc);

    //////////////////////
    disc=tau->tauID("againstMuonLooseMVA");
    CurrentTau.set_againstMuonLooseMVA(disc);

    //////////////////////
    disc=tau->tauID("againstMuonMVAraw");
    CurrentTau.set_againstMuonMVAraw(disc);

    //////////////////////
    disc=tau->tauID("againstMuonMedium");
    CurrentTau.set_againstMuonMedium(disc);

    //////////////////////
    disc=tau->tauID("againstMuonMedium2");
    CurrentTau.set_againstMuonMedium2(disc);

    //////////////////////
    disc=tau->tauID("againstMuonMediumMVA");
    CurrentTau.set_againstMuonMediumMVA(disc);

    //////////////////////
    disc=tau->tauID("againstMuonTight");
    CurrentTau.set_againstMuonTight(disc);

    //////////////////////
    disc=tau->tauID("againstMuonTight2");
    CurrentTau.set_againstMuonTight2(disc);

    //////////////////////
    disc=tau->tauID("againstMuonTight3");
    CurrentTau.set_againstMuonTight3(disc);

    //////////////////////
    disc=tau->tauID("againstMuonTightMVA");
    CurrentTau.set_againstMuonTightMVA(disc);

    //////////////////////
    disc=tau->tauID("byCombinedIsolationDeltaBetaCorrRaw");
    CurrentTau.set_byCombinedIsolationDeltaBetaCorrRaw(disc);

    //////////////////////
    disc=tau->tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits");
    CurrentTau.set_byCombinedIsolationDeltaBetaCorrRaw3Hits(disc);

    //////////////////////
    disc=tau->tauID("byIsolationMVA3newDMwLTraw");
    CurrentTau.set_byIsolationMVA3newDMwLTraw(disc);

    //////////////////////
    disc=tau->tauID("byIsolationMVA3newDMwoLTraw");
    CurrentTau.set_byIsolationMVA3newDMwoLTraw(disc);

    //////////////////////
    disc=tau->tauID("byIsolationMVA3oldDMwLTraw");
    CurrentTau.set_byIsolationMVA3oldDMwLTraw(disc);

    //////////////////////
    disc=tau->tauID("byIsolationMVA3oldDMwoLTraw");
    CurrentTau.set_byIsolationMVA3oldDMwoLTraw(disc);

    //////////////////////
    disc=tau->tauID("byLooseCombinedIsolationDeltaBetaCorr");
    CurrentTau.set_byLooseCombinedIsolationDeltaBetaCorr(disc);

    //////////////////////
    disc=tau->tauID("byLooseCombinedIsolationDeltaBetaCorr3Hits");
    CurrentTau.set_byLooseCombinedIsolationDeltaBetaCorr3Hits(disc);

    //////////////////////
    disc=tau->tauID("byLooseIsolation");
    CurrentTau.set_byLooseIsolation(disc);

    //////////////////////
    disc=tau->tauID("byLooseIsolationMVA3newDMwLT");
    CurrentTau.set_byLooseIsolationMVA3newDMwLT(disc);

    //////////////////////
    disc=tau->tauID("byLooseIsolationMVA3newDMwoLT");
    CurrentTau.set_byLooseIsolationMVA3newDMwoLT(disc);

    //////////////////////
    disc=tau->tauID("byLooseIsolationMVA3oldDMwLT");
    CurrentTau.set_byLooseIsolationMVA3oldDMwLT(disc);

    //////////////////////
    disc=tau->tauID("byLooseIsolationMVA3oldDMwoLT");
    CurrentTau.set_byLooseIsolationMVA3oldDMwoLT(disc);

    //////////////////////
    disc=tau->tauID("byMediumCombinedIsolationDeltaBetaCorr");
    CurrentTau.set_byMediumCombinedIsolationDeltaBetaCorr(disc);

    //////////////////////
    disc=tau->tauID("byMediumCombinedIsolationDeltaBetaCorr3Hits");
    CurrentTau.set_byMediumCombinedIsolationDeltaBetaCorr3Hits(disc);

    //////////////////////
    disc=tau->tauID("byMediumIsolationMVA3newDMwLT");
    CurrentTau.set_byMediumIsolationMVA3newDMwLT(disc);

    //////////////////////
    disc=tau->tauID("byMediumIsolationMVA3newDMwoLT");
    CurrentTau.set_byMediumIsolationMVA3newDMwoLT(disc);

    //////////////////////
    disc=tau->tauID("byMediumIsolationMVA3oldDMwLT");
    CurrentTau.set_byMediumIsolationMVA3oldDMwLT(disc);

    //////////////////////
    disc=tau->tauID("byMediumIsolationMVA3oldDMwoLT");
    CurrentTau.set_byMediumIsolationMVA3oldDMwoLT(disc);

    //////////////////////
    disc=tau->tauID("byTightCombinedIsolationDeltaBetaCorr");
    CurrentTau.set_byTightCombinedIsolationDeltaBetaCorr(disc);

    //////////////////////
    disc=tau->tauID("byTightCombinedIsolationDeltaBetaCorr3Hits");
    CurrentTau.set_byTightCombinedIsolationDeltaBetaCorr3Hits(disc);

    //////////////////////
    disc=tau->tauID("byTightIsolationMVA3newDMwLT");
    CurrentTau.set_byTightIsolationMVA3newDMwLT(disc);

    //////////////////////
    disc=tau->tauID("byTightIsolationMVA3newDMwoLT");
    CurrentTau.set_byTightIsolationMVA3newDMwoLT(disc);

    //////////////////////
    disc=tau->tauID("byTightIsolationMVA3oldDMwLT");
    CurrentTau.set_byTightIsolationMVA3oldDMwLT(disc);

    //////////////////////
    disc=tau->tauID("byTightIsolationMVA3oldDMwoLT");
    CurrentTau.set_byTightIsolationMVA3oldDMwoLT(disc);

    //////////////////////
    disc=tau->tauID("byVLooseCombinedIsolationDeltaBetaCorr");
    CurrentTau.set_byVLooseCombinedIsolationDeltaBetaCorr(disc);

    //////////////////////
    disc=tau->tauID("byVLooseIsolationMVA3newDMwLT");
    CurrentTau.set_byVLooseIsolationMVA3newDMwLT(disc);

    //////////////////////
    disc=tau->tauID("byVLooseIsolationMVA3newDMwoLT");
    CurrentTau.set_byVLooseIsolationMVA3newDMwoLT(disc);

    //////////////////////
    disc=tau->tauID("byVLooseIsolationMVA3oldDMwLT");
    CurrentTau.set_byVLooseIsolationMVA3oldDMwLT(disc);

    //////////////////////
    disc=tau->tauID("byVLooseIsolationMVA3oldDMwoLT");
    CurrentTau.set_byVLooseIsolationMVA3oldDMwoLT(disc);

    //////////////////////
    disc=tau->tauID("byVTightIsolationMVA3newDMwLT");
    CurrentTau.set_byVTightIsolationMVA3newDMwLT(disc);

    //////////////////////
    disc=tau->tauID("byVTightIsolationMVA3newDMwoLT");
    CurrentTau.set_byVTightIsolationMVA3newDMwoLT(disc);

    //////////////////////
    disc=tau->tauID("byVTightIsolationMVA3oldDMwLT");
    CurrentTau.set_byVTightIsolationMVA3oldDMwLT(disc);

    //////////////////////
    disc=tau->tauID("byVTightIsolationMVA3oldDMwoLT");
    CurrentTau.set_byVTightIsolationMVA3oldDMwoLT(disc);

    //////////////////////
    disc=tau->tauID("byVVTightIsolationMVA3newDMwLT");
    CurrentTau.set_byVVTightIsolationMVA3newDMwLT(disc);

    //////////////////////
    disc=tau->tauID("byVVTightIsolationMVA3newDMwoLT");
    CurrentTau.set_byVVTightIsolationMVA3newDMwoLT(disc);

    //////////////////////
    disc=tau->tauID("byVVTightIsolationMVA3oldDMwLT");
    CurrentTau.set_byVVTightIsolationMVA3oldDMwLT(disc);

    //////////////////////
    disc=tau->tauID("byVVTightIsolationMVA3oldDMwoLT");
    CurrentTau.set_byVVTightIsolationMVA3oldDMwoLT(disc);

    //////////////////////
    disc=tau->tauID("chargedIsoPtSum");
    CurrentTau.set_chargedIsoPtSum(disc);

    //////////////////////
    disc=tau->tauID("decayModeFinding");
    CurrentTau.set_decayModeFinding(disc);

    //////////////////////
    disc=tau->tauID("decayModeFindingNewDMs");
    CurrentTau.set_decayModeFindingNewDMs(disc);

    //////////////////////
    disc=tau->tauID("decayModeFindingOldDMs");
    CurrentTau.set_decayModeFindingOldDMs(disc);

    //////////////////////
    disc=tau->tauID("neutralIsoPtSum");
    CurrentTau.set_neutralIsoPtSum(disc);

    //////////////////////
    disc=tau->tauID("puCorrPtSum");
    CurrentTau.set_puCorrPtSum(disc);





    //////////////////////////
    // set the passFullId summary boolean

    bool passFullId_muTau = 1;
    bool passFullId_eTau = 1;

    ///////////////////////////

    if(!(CurrentTau.p4().pt()>30))
    {
      passFullId_muTau = 0;
      passFullId_eTau = 0;
    }
    if(!(fabs(CurrentTau.p4().eta())<2.3))
    {
      passFullId_muTau = 0;
      passFullId_eTau = 0;
    }


    if(!(tau->tauID("decayModeFindingOldDMs") > 0.5 && tau->tauID("byTightIsolationMVA3oldDMwLT") > 0.5))
    {
      passFullId_muTau = 0;
      passFullId_eTau = 0;
    }

    // muTau specific
    if(!(tau->tauID("againstMuonMediumMVA") > 0.5 && tau->tauID("againstElectronLoose") > 0.5 )) passFullId_muTau = 0;

    // eTau specific
    if(!(tau->tauID("againstElectronMediumMVA5") > 0.5 && tau->tauID("againstMuonLoose3") > 0.5)) passFullId_eTau = 0;

    ///////////////////////////

    CurrentTau.set_passFullId_eTau(passFullId_eTau);
    CurrentTau.set_passFullId_muTau(passFullId_muTau);


    ////////////
    // store the Tau

    TupleTaus->push_back(CurrentTau);

  }


  iEvent.put( TupleTaus, NAME_ );

  /* This is an event example
  //Read 'ExampleData' from the Event
  Handle<ExampleData> pIn;
  iEvent.getByLabel("example",pIn);

  //Use the ExampleData to create an ExampleData2 which
  // is put into the Event
  std::auto_ptr<ExampleData2> pOut(new ExampleData2(*pIn));
  iEvent.put(pOut);
  */

  /* this is an EventSetup example
  //Read SetupData from the SetupRecord in the EventSetup
  ESHandle<SetupData> pSetup;
  iSetup.get<SetupRecord>().get(pSetup);
  */

}

// ------------ method called once each job just before starting event loop  ------------
void
TupleTauProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TupleTauProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
TupleTauProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TupleTauProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TupleTauProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TupleTauProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleTauProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleTauProducer);
