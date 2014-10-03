#include "UserCode/PATHelpers/plugins/DiElectronFilter.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "UserCode/TupleHelpers/interface/TupleHelpers.hh"

#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "DataFormats/RecoCandidate/interface/IsoDepositVetos.h"
#include "DataFormats/PatCandidates/interface/Isolation.h"

/////////////////////////
// return 0 for events
// with a dielectron pair

using namespace pat;


DiElectronFilter::DiElectronFilter(const edm::ParameterSet & iConfig) {
  electronSource_     = iConfig.getParameter<edm::InputTag>( "electronSource" );
  vertexSource_ = iConfig.getParameter<edm::InputTag>("vertexSource" );
}


DiElectronFilter::~DiElectronFilter() {
}


bool DiElectronFilter::filter(edm::Event & iEvent, const edm::EventSetup & iSetup) {

  // get electron collection
  edm::Handle<edm::View<Electron> > electrons;
  iEvent.getByLabel(electronSource_, electrons);

  // get vertex collection
  edm::Handle<edm::View<reco::Vertex> > vertices;
  iEvent.getByLabel(vertexSource_,vertices);

  edm::View<reco::Vertex>::const_iterator vertex;

  //////////////////////////
  // this needs to be replaced by a function
  // as it is used here and in ElectronTau producer
  ////////////////////////////

  /////////////////
  // find max sum pt vertex
  // passing quality cuts
  // would really be best to do this
  // at PAT level

  int primary_vertex_indx = -999;
  float max_sumPt = -999;


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
        }
      }
    }
  }

  /////////////////////////

  const reco::Vertex & primary_vertex = vertices->at(primary_vertex_indx);
  const reco::Vertex & first_vertex = vertices->at(0);



  ///////////////////////
  // reject events with 2 opposite sign electrons
  // passing the specified cuts

  bool positive_pass = 0;
  bool negative_pass = 0;

  edm::View<pat::Electron>::const_iterator electron;
  for(electron=electrons->begin(); electron!=electrons->end(); ++electron)
  {

    bool passAllCuts = 1;

    double relativeIsolation = 999.;
    double i_charged = electron->chargedHadronIso();
    double i_photons = electron->photonIso();
    double i_neutralhadrons = electron->neutralHadronIso();
    double i_deltabeta = electron->puChargedHadronIso();
    relativeIsolation = i_charged + std::max(i_neutralhadrons+i_photons-0.5*i_deltabeta,0.0);



    AbsVetos  vetos2012EBPFIdCharged;
    AbsVetos  vetos2012EBPFIdPhotons;
    AbsVetos  vetos2012EBPFIdNeutral;

    AbsVetos  vetos2012EEPFIdCharged;
    AbsVetos  vetos2012EEPFIdPhotons;
    AbsVetos  vetos2012EEPFIdNeutral;

    float nhIso04PFId  = 0.0;
    float allChIso04PFId = 0.0;
    float phIso04PFId  = 0.0;
    float nhIsoPU04PFId = 0.0;

    vetos2012EBPFIdCharged.push_back(new ConeVeto(Direction(electron->eta(),electron->phi()),0.010));
    vetos2012EBPFIdPhotons.push_back(new ConeVeto(Direction(electron->eta(),electron->phi()),0.08));
    vetos2012EEPFIdCharged.push_back(new ConeVeto(Direction(electron->eta(),electron->phi()),0.015));
    vetos2012EEPFIdPhotons.push_back(new ConeVeto(Direction(electron->eta(),electron->phi()),0.08));


    float allChIso04EBPFId =    electron->isoDeposit(pat::PfChargedAllIso)->depositAndCountWithin(0.4, vetos2012EBPFIdCharged).first;
    float allChIso04EEPFId =  electron->isoDeposit(pat::PfChargedAllIso)->depositAndCountWithin(0.4, vetos2012EEPFIdCharged).first;
    allChIso04PFId =  (electron->isEB())*allChIso04EBPFId + (electron->isEE())*allChIso04EEPFId ;


    float nhIso04EBPFId = electron->isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.4, vetos2012EBPFIdNeutral).first;
    float nhIso04EEPFId = electron->isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.4, vetos2012EEPFIdNeutral).first;
    nhIso04PFId =  (electron->isEB())*nhIso04EBPFId + (electron->isEE())*nhIso04EEPFId ;


    float phIso04EBPFId =   electron->isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.4, vetos2012EBPFIdPhotons).first;
    float phIso04EEPFId = electron->isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.4, vetos2012EEPFIdPhotons).first;
    phIso04PFId =  (electron->isEB())*phIso04EBPFId + (electron->isEE())*phIso04EEPFId ;


    float nhIsoPU04EBPFId =   electron->isoDeposit(pat::PfPUChargedHadronIso)->depositAndCountWithin(0.4, vetos2012EBPFIdNeutral).first;
    float nhIsoPU04EEPFId =   electron->isoDeposit(pat::PfPUChargedHadronIso)->depositAndCountWithin(0.4, vetos2012EEPFIdNeutral).first;
    nhIsoPU04PFId =     (electron->isEB())*nhIsoPU04EBPFId + (electron->isEE())*nhIsoPU04EEPFId ;


    relativeIsolation = allChIso04PFId + std::max(nhIso04PFId+phIso04PFId-0.5*nhIsoPU04PFId,0.0);
    if(electron->pt()!=0) relativeIsolation/=electron->pt();


    for(unsigned int i = 0; i <vetos2012EBPFIdCharged.size(); i++) delete vetos2012EBPFIdCharged[i];
    for(unsigned int i = 0; i <vetos2012EBPFIdPhotons.size(); i++) delete vetos2012EBPFIdPhotons[i];
    for(unsigned int i = 0; i <vetos2012EBPFIdNeutral.size(); i++) delete vetos2012EBPFIdNeutral[i];
    for(unsigned int i = 0; i <vetos2012EEPFIdCharged.size(); i++) delete vetos2012EEPFIdCharged[i];
    for(unsigned int i = 0; i <vetos2012EEPFIdPhotons.size(); i++) delete vetos2012EEPFIdPhotons[i];
    for(unsigned int i = 0; i <vetos2012EEPFIdNeutral.size(); i++) delete vetos2012EEPFIdNeutral[i];








    if(!(electron->p4().pt()>15)) passAllCuts = 0;
    if(!(fabs(electron->p4().eta())<2.5)) passAllCuts = 0;
    if(!(relativeIsolation < 0.3)) passAllCuts = 0;


    if(electron->gsfTrack().isNonnull() && electron->superCluster().isNonnull())
    {

      if(  !( fabs(electron->gsfTrack()->dz(first_vertex.position())) < 0.2)  ) passAllCuts = 0;

      double superClusterEta = electron->superCluster()->position().Eta();
      double sigIetaIeta = electron->sigmaIetaIeta();
      double deltaEta = electron->deltaEtaSuperClusterTrackAtVtx();
      double deltaPhi = electron->deltaPhiSuperClusterTrackAtVtx();
      double HE=  electron->hadronicOverEm();
      double dZ_vtx = electron->gsfTrack()->dz(first_vertex.position());

      bool wp95 = TupleHelpers::passWP95(superClusterEta,sigIetaIeta,deltaEta,deltaPhi,HE,dZ_vtx);

      if( !(wp95) ) passAllCuts = 0;



    }
    else passAllCuts = 0;













    if(passAllCuts)
    {
      if(electron->charge()==1) positive_pass = 1;
      else if(electron->charge()==-1) negative_pass = 1;
    }


    ///////////////////////////

  }

  return !(positive_pass && negative_pass);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DiElectronFilter);
