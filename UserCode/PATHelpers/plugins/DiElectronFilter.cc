#include "UserCode/PATHelpers/plugins/DiElectronFilter.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "UserCode/TupleHelpers/interface/TupleHelpers.hh"

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
    if(electron->pt()!=0) relativeIsolation/=electron->pt();

    if(!(electron->p4().pt()>15)) passAllCuts = 0;
    if(!(fabs(electron->p4().eta())<2.5)) passAllCuts = 0;
    if(!(relativeIsolation < 0.3)) passAllCuts = 0;


    if(electron->gsfTrack().isNonnull() && electron->superCluster().isNonnull())
    {

      if(  !( fabs(electron->gsfTrack()->dz(primary_vertex.position())) < 0.2)  ) passAllCuts = 0;

      double superClusterEta = electron->superCluster()->position().Eta();
      double sigIetaIeta = electron->sigmaIetaIeta();
      double deltaEta = electron->deltaEtaSuperClusterTrackAtVtx();
      double deltaPhi = electron->deltaPhiSuperClusterTrackAtVtx();
      double HE=  electron->hadronicOverEm();
      double dZ_vtx = electron->gsfTrack()->dz(primary_vertex.position());

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
