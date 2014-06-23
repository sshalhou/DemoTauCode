#include "UserCode/PATHelpers/plugins/DiMuonFilter.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

/////////////////////////
// return 1 for events
// with a dimuon pair

using namespace pat;


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

  std::cout<<" FOUND VERTEX AT INDEX "<<primary_vertex_indx<<std::endl;
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

    double irel_DR4 = 0;
    double i_charged_DR4 = muon->pfIsolationR04().sumChargedParticlePt;
    double i_photons_DR4 = muon->pfIsolationR04().sumPhotonEt;
    double i_neutralhadrons_DR4 = muon->pfIsolationR04().sumNeutralHadronEt;
    double i_deltabeta_DR4 = muon->pfIsolationR04().sumPUPt;
    irel_DR4 = i_charged_DR4 + std::max(i_neutralhadrons_DR4+i_photons_DR4-0.5*i_deltabeta_DR4,0.0);
    if(muon->pt()) irel_DR4/=muon->pt();
    else irel_DR4 = 0.0;


    if(!(muon->isGlobalMuon())) passAllCuts = 0;
    if(!(muon->isPFMuon())) passAllCuts = 0;
    if(!(muon->isTrackerMuon())) passAllCuts = 0;
    if(!(muon->p4().pt()>15)) passAllCuts = 0;
    if(!(fabs(muon->p4().eta())<2.4)) passAllCuts = 0;
    if(!(fabs(muon->muonBestTrack()->dz(primary_vertex.position())) < 0.2)) passAllCuts = 0;
    if(!(irel_DR4 < 0.3)) passAllCuts = 0;


    if(passAllCuts)
    {
      if(muon->charge()==1) positive_pass = 1;
      else if(muon->charge()==-1) negative_pass = 1;
    }


    ///////////////////////////

  }

  std::cout<<" DiMuon Filter returns "<<!(positive_pass && negative_pass) << std::endl;
  return !(positive_pass && negative_pass);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DiMuonFilter);
