#include "UserCode/PATHelpers/plugins/DiMuonFilter.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "DataFormats/RecoCandidate/interface/IsoDepositVetos.h"
#include "DataFormats/PatCandidates/interface/Isolation.h"

/////////////////////////
// return 0 for events
// with a dimuon pair

using namespace pat;
using namespace reco::isodeposit;


DiMuonFilter::DiMuonFilter(const edm::ParameterSet & iConfig) {
  muonSource_     = iConfig.getParameter<edm::InputTag>( "muonSource" );
  vertexSource_ = iConfig.getParameter<edm::InputTag>("vertexSource" );
}


DiMuonFilter::~DiMuonFilter() {
}


bool DiMuonFilter::filter(edm::Event & iEvent, const edm::EventSetup & iSetup) {

  // get muon collection
  edm::Handle<edm::View<Muon> > muons;
  iEvent.getByLabel(muonSource_, muons);

  // get vertex collection
  edm::Handle<edm::View<reco::Vertex> > vertices;
  iEvent.getByLabel(vertexSource_,vertices);

  edm::View<reco::Vertex>::const_iterator vertex;

  //////////////////////////
  // this needs to be replaced by a function
  // as it is used here and in MuonTau producer
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



  ///////////////////////
  // reject events with 2 opposite sign muons
  // passing the specified cuts

  bool positive_pass = 0;
  bool negative_pass = 0;

  edm::View<pat::Muon>::const_iterator muon;
  for(muon=muons->begin(); muon!=muons->end(); ++muon)
  {

    bool passAllCuts = 1;


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






for(unsigned int i = 0; i <vetos2012PFIdCharged.size(); i++) delete vetos2012PFIdCharged[i];

for(unsigned int i = 0; i <vetos2012PFIdNeutral.size(); i++) delete vetos2012PFIdNeutral[i];

for(unsigned int i = 0; i <vetos2012PFIdPhotons.size(); i++) delete vetos2012PFIdPhotons[i];

for(unsigned int i = 0; i <vetos2012PFIdPUCharged.size(); i++) delete vetos2012PFIdPUCharged[i];








    if(!(muon->isGlobalMuon())) passAllCuts = 0;
    if(!(muon->isPFMuon())) passAllCuts = 0;
    if(!(muon->isTrackerMuon())) passAllCuts = 0;
    if(!(muon->p4().pt()>15)) passAllCuts = 0;
    if(!(fabs(muon->p4().eta())<2.4)) passAllCuts = 0;
    if(!(fabs(muon->muonBestTrack()->dz(primary_vertex.position())) < 0.2)) passAllCuts = 0;
    if(!(relativeIsolation_DR4 < 0.3)) passAllCuts = 0;


    if(passAllCuts)
    {
      if(muon->charge()==1) positive_pass = 1;
      else if(muon->charge()==-1) negative_pass = 1;
    }


    ///////////////////////////

  }

  return !(positive_pass && negative_pass);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DiMuonFilter);
