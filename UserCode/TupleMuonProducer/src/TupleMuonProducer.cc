// -*- C++ -*-
//
// Package:    TupleMuonProducer
// Class:      TupleMuonProducer
//
/**\class TupleMuonProducer TupleMuonProducer.cc TEMP/TupleMuonProducer/src/TupleMuonProducer.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Thu May  8 06:52:55 CDT 2014
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

// needed by ntuple muons producer
#include <vector>
#include <iostream>
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "UserCode/TupleObjects/interface/TupleMuon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "PhysicsTools/PatUtils/interface/TriggerHelper.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "DataFormats/RecoCandidate/interface/IsoDepositVetos.h"
#include "DataFormats/PatCandidates/interface/Isolation.h"

typedef math::XYZTLorentzVector LorentzVector;
using namespace std;
using namespace edm;
using namespace pat;
using namespace reco::isodeposit;

//
// class declaration
//

class TupleMuonProducer : public edm::EDProducer {
public:
  explicit TupleMuonProducer(const edm::ParameterSet&);
  ~TupleMuonProducer();

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
  edm::InputTag muonSrc_;
  edm::InputTag vertexSrc_;
  string NAME_;
  edm::InputTag triggerEventSrc_;
  std::string muTrigMatchMu17Src_;
  std::string muTrigMatchMu18Src_;
  std::string muTrigMatchMu24Src_;
  vector<string> muTauPaths;
  edm::InputTag pfSrc_;

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
TupleMuonProducer::TupleMuonProducer(const edm::ParameterSet& iConfig):
muonSrc_(iConfig.getParameter<edm::InputTag>("muonSrc" )),
vertexSrc_(iConfig.getParameter<edm::InputTag>("vertexSrc" )),
NAME_(iConfig.getParameter<string>("NAME" )),
triggerEventSrc_(iConfig.getUntrackedParameter<edm::InputTag>("triggerEventSrc" )),
muTrigMatchMu17Src_(iConfig.getUntrackedParameter<std::string>("muTrigMatchMu17Src" )),
muTrigMatchMu18Src_(iConfig.getUntrackedParameter<std::string>("muTrigMatchMu18Src" )),
muTrigMatchMu24Src_(iConfig.getUntrackedParameter<std::string>("muTrigMatchMu24Src" )),
pfSrc_(iConfig.getParameter<edm::InputTag>("pfSrc" ))
{


  muTauPaths.push_back("HLT_IsoMu18_eta2p1_LooseIsoPFTau20_v");
  muTauPaths.push_back("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v");
  muTauPaths.push_back("HLT_IsoMu24");

  produces<vector<TupleMuon>>(NAME_).setBranchAlias(NAME_);

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


TupleMuonProducer::~TupleMuonProducer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TupleMuonProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  // get muon collection
  edm::Handle<edm::View<pat::Muon> > muons;
  iEvent.getByLabel(muonSrc_,muons);

  // get pfCandidates collection
  edm::Handle<reco::PFCandidateCollection > pfCandidates;
  iEvent.getByLabel(pfSrc_,pfCandidates);

  // get vertex collection
  edm::Handle<edm::View<reco::Vertex> > vertices;
  iEvent.getByLabel(vertexSrc_,vertices);

  edm::View<reco::Vertex>::const_iterator vertex;



  // get the trigger info

  edm::Handle< TriggerEvent > triggerEvent;
  iEvent.getByLabel( triggerEventSrc_, triggerEvent );

  // trigger helper
  const pat::helper::TriggerMatchHelper matchHelper;

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




  /////////////////
  // find max sum pt vertex
  // passing quality cuts
  // would really be best to do this
  // at PAT level

  int primary_vertex_indx = -999;
  float max_sumPt = -999;

  //cout<<" ---------- "<<endl;


  for(vertex=vertices->begin(); vertex!=vertices->end(); ++vertex)
  {

    if(!vertex->isFake() && vertex->ndof() > 4.0)
    {
      if(fabs(vertex->z()) < 24.0 && vertex->position().Rho() < 2)
      {

        if( vertex->p4().pt() > max_sumPt)
        {
          max_sumPt  =     vertex->p4().pt();
          primary_vertex_indx =    vertex - vertices->begin();
          //cout<<" current max vertex sumPt = "<<vertex->p4().pt()<<endl;


        }






      }

    }

  }
  const reco::Vertex & primary_vertex = vertices->at(primary_vertex_indx);
  const reco::Vertex & first_vertex = vertices->at(0);

  //cout<<" final max pt "<<primary_vertex.p4().pt()<<endl;














  //auto_ptr<vector<TupleMuon>> TupleMuons (new vector<TupleMuon>);
  auto_ptr<TupleMuonCollection> TupleMuons (new TupleMuonCollection);

  const int TupleMuonSize = muons->size();
  TupleMuons->reserve( TupleMuonSize );


  edm::View<pat::Muon>::const_iterator muon;
  for(muon=muons->begin(); muon!=muons->end(); ++muon)
  {

    TupleMuon CurrentMuon;
    bool isTightMuon   = 1;
    bool isPFMuon = 0;
    /*
    cout<<" muon Pt "<<muon->p4().pt()<<endl;
    cout<<" isGlobal "<<muon->isGlobalMuon()<<endl;
    cout<<" isTightMuon "<<muon->isTightMuon(primary_vertex)<<endl;
    cout<<" isLooseMuon "<<muon->isLooseMuon()<<endl;
    cout<<" charge "<<muon->charge()<<endl;
    cout<<" pfP4.pt "<<muon->pfP4().pt()<<endl;

    /////

    cout<<" normalizedChi2 "<<muon->globalTrack()->normalizedChi2()<<endl;
    cout<<" number valid hits "<<muon->globalTrack()->hitPattern().numberOfValidMuonHits()<<endl;
    cout<<" number matched stations "<<muon->numberOfMatchedStations()<<endl;
    cout<<" number valid pixel hits "<<muon->innerTrack()->hitPattern().numberOfValidPixelHits()<<endl;
    cout<<" tracker layer with measurement "<<muon->track()->hitPattern().trackerLayersWithMeasurement()<<endl;
    cout<<" dB "<<muon->dB()<<endl;
    std::cout<<" dz = "<<muon->muonBestTrack()->dz()<<std::endl;
    std::cout<<"dxy = "<<(muon->muonBestTrack()->dxy())<<std::endl;
    */


    /////////////////
    // check the trigger matches

    if(muTauPath==1)
    {
      size_t muon_id =  muon - muons->begin();

      const pat::TriggerObjectRef trigRefMu17(
      matchHelper.triggerMatchObject( muons, muon_id, muTrigMatchMu17Src_, iEvent, *triggerEvent ) );
      const pat::TriggerObjectRef trigRefMu18(
      matchHelper.triggerMatchObject( muons, muon_id, muTrigMatchMu18Src_, iEvent, *triggerEvent ) );
      const pat::TriggerObjectRef trigRefMu24(
      matchHelper.triggerMatchObject( muons, muon_id, muTrigMatchMu24Src_, iEvent, *triggerEvent ) );


      if( trigRefMu17.isAvailable() && trigRefMu17.isNonnull()) CurrentMuon.set_has_HltMatchMu17(1);
      if( trigRefMu18.isAvailable() && trigRefMu18.isNonnull()) CurrentMuon.set_has_HltMatchMu18(1);
      if( trigRefMu24.isAvailable() && trigRefMu24.isNonnull() && muon->p4().pt()>27)
      {
        CurrentMuon.set_has_HltMatchMu24(1);
      }
    }



    /////
    // set 4-vectors, in our case p4 == pfP4
    // since we use PF2PAT aka PFBRECO

    CurrentMuon.set_p4(muon->p4());
    CurrentMuon.set_pfP4(muon->pfP4());

    // store the generator level 4-vector

    if(muon->genLepton())
    {
      CurrentMuon.set_genP4(muon->genLepton()->p4());

      ////////////////
      //set_GENpdgId
      ////////////////
      CurrentMuon.set_GENpdgId(muon->genLepton()->pdgId());

    }

    // store selection summary booleans

    CurrentMuon.set_isGlobalMuon(muon->isGlobalMuon());
    //  CurrentMuon.set_isTightMuon(muon->isTightMuon(primary_vertex));

    //    CurrentMuon.set_isTightMuon(muon->isGood("GlobalMuonPromptTight"));

    isTightMuon = 1;
    if(   !(muon->isGlobalMuon())                 ) isTightMuon = 0;
    if(   !(muon->numberOfMatchedStations()>1)    ) isTightMuon = 0;
    if(    muon->innerTrack().isNonnull() && muon->track().isNonnull() && muon->globalTrack().isNonnull() )
    {

      if(   !(muon->globalTrack()->normalizedChi2()<10) ) isTightMuon = 0;
      if(   !((muon->globalTrack()->hitPattern()).numberOfValidMuonHits()>0) ) isTightMuon = 0;
      if(   !((muon->innerTrack()->hitPattern()).numberOfValidPixelHits()>0) ) isTightMuon = 0;
      if(   !((muon->track()->hitPattern()).trackerLayersWithMeasurement()>5) ) isTightMuon = 0;

    } else isTightMuon = 0;

    CurrentMuon.set_isTightMuon(isTightMuon);

    isPFMuon = 0;

    for(size_t pf = 0; pf < pfCandidates->size(); pf++)
    {


      if( (*pfCandidates)[pf].particleId() == reco::PFCandidate::mu )
      {
        reco::MuonRef muonRefToPFMuon = (*pfCandidates)[pf].muonRef();


        if( muonRefToPFMuon.isNonnull() )
        {
          if(deltaR( muonRefToPFMuon->p4() , muon->p4()) < 1e-04)
          {
            if(muonRefToPFMuon->isGlobalMuon() || muonRefToPFMuon->isTrackerMuon() )
            {
              isPFMuon = 1;
            }


          }
        }


      }
    }



    CurrentMuon.set_isPFMuon(isPFMuon);
    CurrentMuon.set_isTrackerMuon(muon->isTrackerMuon() );



    CurrentMuon.set_isLooseMuon(muon->isLooseMuon());

    // store the pf isolation valid boolean

    CurrentMuon.set_isPFIsolationValid(muon->isPFIsolationValid());

    // store the charge

    CurrentMuon.set_charge(muon->charge());

    // store the pdgId (from PF)

    CurrentMuon.set_PFpdgId(muon->pdgId());

    // store additional parameters related to track/vertex & tight ID
    // must check for these tracks before calling

    if(!muon->innerTrack().isNull())
    {
      CurrentMuon.set_numberOfValidPixelHits(muon->innerTrack()->hitPattern().numberOfValidPixelHits());
      CurrentMuon.set_dz(muon->innerTrack()->dz(first_vertex.position()));
      CurrentMuon.set_dxy(muon->innerTrack()->dxy(first_vertex.position()));

    }

    if(!muon->globalTrack().isNull())
    {

      CurrentMuon.set_normalizedChi2(muon->globalTrack()->normalizedChi2());
      CurrentMuon.set_numberOfValidMuonHits(muon->globalTrack()->hitPattern().numberOfValidMuonHits());



    }

    if(!muon->track().isNull())
    {
      CurrentMuon.set_trackerLayersWithMeasurement(muon->track()->hitPattern().trackerLayersWithMeasurement());

    }

    //  if(!muon->muonBestTrack().isNull())
    //  {

    //  CurrentMuon.set_dxy(muon->muonBestTrack()->dxy(primary_vertex.position()));

    //}








    CurrentMuon.set_numberOfMatchedStations(muon->numberOfMatchedStations());
    CurrentMuon.set_dB(muon->dB());








    /////////////
    // compute
    // and store
    // isolation parameters
    // @ DR 3
    /////////////

    double relativeIsolation_DR3 = 999.;
    double i_charged_DR3 = muon->pfIsolationR03().sumChargedParticlePt;
    double i_photons_DR3 = muon->pfIsolationR03().sumPhotonEt;
    double i_neutralhadrons_DR3 = muon->pfIsolationR03().sumNeutralHadronEt;
    double i_deltabeta_DR3 = muon->pfIsolationR03().sumPUPt;

    relativeIsolation_DR3 = i_charged_DR3 + std::max(i_neutralhadrons_DR3+i_photons_DR3-0.5*i_deltabeta_DR3,0.0);

    if(muon->pt()!=0) relativeIsolation_DR3/=muon->pt();


    CurrentMuon.set_sumChargedParticlePt_DR3(i_charged_DR3);
    CurrentMuon.set_sumPhotonEt_DR3(i_photons_DR3);
    CurrentMuon.set_sumNeutralHadronEt_DR3(i_neutralhadrons_DR3);
    CurrentMuon.set_sumPUPt_DR3(i_deltabeta_DR3);
    CurrentMuon.set_relativeIso_DR3(relativeIsolation_DR3);


    /////////////
    // compute
    // and store
    // isolation parameters
    // @ DR 4
    /////////////

    double relativeIsolation_DR4 = 999.;




    AbsVetos  vetos2012PFIdCharged;
    AbsVetos  vetos2012PFIdPhotons;
    AbsVetos  vetos2012PFIdNeutral;
    AbsVetos  vetos2012PFIdPUCharged;


    float nhIso04PFId  = 0.0;
    float allChIso04PFId = 0.0;
    float phIso04PFId  = 0.0;
    float nhIsoPU04PFId = 0.0;



    vetos2012PFIdCharged.push_back(new ConeVeto(Direction(muon->eta(),muon->phi()),0.00010));
    vetos2012PFIdCharged.push_back(new ThresholdVeto(0.00));

    vetos2012PFIdPhotons.push_back(new ConeVeto(Direction(muon->eta(),muon->phi()),0.010));
    vetos2012PFIdPhotons.push_back(new ThresholdVeto(0.50));

    vetos2012PFIdNeutral.push_back(new ConeVeto(Direction(muon->eta(),muon->phi()),0.010));
    vetos2012PFIdNeutral.push_back(new ThresholdVeto(0.50));

    vetos2012PFIdPUCharged.push_back(new ConeVeto(Direction(muon->eta(),muon->phi()),0.010));
    vetos2012PFIdPUCharged.push_back(new ThresholdVeto(0.50));




    allChIso04PFId = muon->isoDeposit(pat::PfChargedAllIso)->depositAndCountWithin(0.4, vetos2012PFIdCharged).first;

    nhIso04PFId = muon->isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.4, vetos2012PFIdNeutral).first;

    phIso04PFId = muon->isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.4, vetos2012PFIdPhotons).first;

    nhIsoPU04PFId = muon->isoDeposit(pat::PfPUChargedHadronIso)->depositAndCountWithin(0.4, vetos2012PFIdPUCharged).first;





    relativeIsolation_DR4 = allChIso04PFId + std::max(nhIso04PFId+phIso04PFId-0.5*nhIsoPU04PFId,0.0);
    if(muon->pt()!=0) relativeIsolation_DR4/=muon->pt();


    CurrentMuon.set_sumChargedParticlePt_DR4(allChIso04PFId);
    CurrentMuon.set_sumPhotonEt_DR4(phIso04PFId);
    CurrentMuon.set_sumNeutralHadronEt_DR4(nhIso04PFId);
    CurrentMuon.set_sumPUPt_DR4(nhIsoPU04PFId);
    CurrentMuon.set_relativeIso_DR4(relativeIsolation_DR4);



    for(unsigned int i = 0; i <vetos2012PFIdCharged.size(); i++) delete vetos2012PFIdCharged[i];

    for(unsigned int i = 0; i <vetos2012PFIdNeutral.size(); i++) delete vetos2012PFIdNeutral[i];

    for(unsigned int i = 0; i <vetos2012PFIdPhotons.size(); i++) delete vetos2012PFIdPhotons[i];

    for(unsigned int i = 0; i <vetos2012PFIdPUCharged.size(); i++) delete vetos2012PFIdPUCharged[i];





    /* old
    double i_charged_DR4 = muon->pfIsolationR04().sumChargedParticlePt;
    double i_photons_DR4 = muon->pfIsolationR04().sumPhotonEt;
    double i_neutralhadrons_DR4 = muon->pfIsolationR04().sumNeutralHadronEt;
    double i_deltabeta_DR4 = muon->pfIsolationR04().sumPUPt;

    relativeIsolation_DR4 = i_charged_DR4 + std::max(i_neutralhadrons_DR4+i_photons_DR4-0.5*i_deltabeta_DR4,0.0);

    if(muon->pt()!=0) relativeIsolation_DR4/=muon->pt();

    CurrentMuon.set_sumChargedParticlePt_DR4(i_charged_DR4);
    CurrentMuon.set_sumPhotonEt_DR4(i_photons_DR4);
    CurrentMuon.set_sumNeutralHadronEt_DR4(i_neutralhadrons_DR4);
    CurrentMuon.set_sumPUPt_DR4(i_deltabeta_DR4);
    CurrentMuon.set_relativeIso_DR4(relativeIsolation_DR4);
    */

    ////////////////
    //set_passFullId
    // this is not really the 'full' ID
    // just a way to limit the number of SVFit
    // calculations to a reasonable amount

    bool passFullId = 1;

    ///////////////////////////
    if(!(muon->isGlobalMuon())) passFullId = 0;
    if(!(isTightMuon)) passFullId = 0;
    if(!(isPFMuon)) passFullId = 0;
    if(!(muon->p4().pt()>18)) passFullId = 0;
    if(!(fabs(muon->p4().eta())<2.2)) passFullId = 0;
    if(!muon->innerTrack().isNull())
    {
      if(!(fabs(muon->innerTrack()->dz(first_vertex.position())) < 0.2)) passFullId = 0;
      if(!(fabs(muon->innerTrack()->dxy(first_vertex.position())) < 0.045)) passFullId = 0;

    }
    else passFullId = 0;
    if(!(relativeIsolation_DR4 < 0.6)) passFullId = 0;

    ///////////////////////////

    CurrentMuon.set_passFullId(passFullId);


    ///////////////
    // check if this muon
    // would force event rejection due to the
    // tri-lepton veto if not used in H->tau tau recon.

    bool triLeptonVetoCuts = 1;

    if(!(muon->p4().pt()>10)) triLeptonVetoCuts = 0;
    if(!(fabs(muon->p4().eta())<2.4)) triLeptonVetoCuts = 0;
    if(!(relativeIsolation_DR4 < 0.3)) triLeptonVetoCuts = 0;
    if(!(isTightMuon)) triLeptonVetoCuts = 0;
    if(!(isPFMuon)) triLeptonVetoCuts = 0;
    if(!muon->innerTrack().isNull())
    {
      if(!(fabs(muon->innerTrack()->dz(first_vertex.position())) < 0.2)) triLeptonVetoCuts = 0;
      if(!(fabs(muon->innerTrack()->dxy(first_vertex.position())) < 0.045)) triLeptonVetoCuts = 0;

    }
    else triLeptonVetoCuts = 0;

    CurrentMuon.set_isTriLeptonVetoCandidate(triLeptonVetoCuts);



    ////////////
    // store the muon

    TupleMuons->push_back(CurrentMuon);

  }


  iEvent.put( TupleMuons, NAME_ );


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
TupleMuonProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TupleMuonProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
TupleMuonProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TupleMuonProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TupleMuonProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TupleMuonProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleMuonProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleMuonProducer);
