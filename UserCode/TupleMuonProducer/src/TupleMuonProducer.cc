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
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "UserCode/TupleObjects/interface/TupleMuon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

typedef math::XYZTLorentzVector LorentzVector;
using namespace std;
using namespace edm;

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
muonSrc_(iConfig.getUntrackedParameter<edm::InputTag>("muonSrc" )),
vertexSrc_(iConfig.getUntrackedParameter<edm::InputTag>("vertexSrc" ))
{

  produces<vector<TupleMuon>>("TupleMuons").setBranchAlias("TupleMuons");


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

  // get vertex collection
  edm::Handle<edm::View<reco::Vertex> > vertices;
  iEvent.getByLabel(vertexSrc_,vertices);

  edm::View<reco::Vertex>::const_iterator vertex;


  /////////////////
  // find max sum pt vertex
  // passing quality cuts
  // would really be best to do this
  // at PAT level

  int primary_vertex_indx = -999;
  float max_sumPt = -999;

  cout<<" ---------- "<<endl;


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
          cout<<" current max vertex sumPt = "<<vertex->p4().pt()<<endl;


        }






      }

    }


    cout<<" final max pt "<<vertices[primary_vertex_indx]->p4().pt()<<endl;





  }







  //auto_ptr<vector<TupleMuon>> TupleMuons (new vector<TupleMuon>);
  auto_ptr<TupleMuonCollection> TupleMuons (new TupleMuonCollection);

  const int TupleMuonSize = muons->size();
  TupleMuons->reserve( TupleMuonSize );


  edm::View<pat::Muon>::const_iterator muon;
  for(muon=muons->begin(); muon!=muons->end(); ++muon)
  {

    TupleMuon CurrentMuon;


    CurrentMuon.set_Pt(muon->p4().pt());
    CurrentMuon.set_p4(muon->p4());

    //CurrentMuon.set_Pt(muon->p4().pt());
    cout<<" muon Pt "<<muon->p4().pt()<<endl;
    cout<<" isGlobal "<<muon->isGlobalMuon()<<endl;
    //  cout<<" isTightMuon "<<muon->isTightMuon()<<endl;



    TupleMuons->push_back(CurrentMuon);

  }


  iEvent.put( TupleMuons, "TupleMuons" );


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
