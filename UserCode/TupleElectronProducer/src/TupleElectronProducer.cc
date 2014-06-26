// -*- C++ -*-
//
// Package:    TupleElectronProducer
// Class:      TupleElectronProducer
//
/**\class TupleElectronProducer TupleElectronProducer.cc TEMP/TupleElectronProducer/src/TupleElectronProducer.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Tue Jun 24 09:44:10 CDT 2014
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

// needed by ntuple electron producer
#include <vector>
#include <iostream>
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "EgammaAnalysis/ElectronTools/interface/EGammaCutBasedEleId.h"
#include "DataFormats/PatCandidates/interface/Conversion.h"
#include "DataFormats/PatCandidates/interface/Lepton.h"
#include "UserCode/TupleObjects/interface/TupleElectron.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "Math/GenVector/VectorUtil.h"
#include "DataFormats/PatCandidates/interface/PFParticle.h"
#include "UserCode/TupleHelpers/interface/TupleHelpers.hh"


typedef math::XYZTLorentzVector LorentzVector;
using namespace std;
using namespace edm;



//
// class declaration
//

class TupleElectronProducer : public edm::EDProducer {
public:
  explicit TupleElectronProducer(const edm::ParameterSet&);
  ~TupleElectronProducer();

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

  edm::InputTag electronSrc_;
  edm::InputTag vertexSrc_;
  string NAME_;


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
TupleElectronProducer::TupleElectronProducer(const edm::ParameterSet& iConfig):
electronSrc_(iConfig.getParameter<edm::InputTag>("electronSrc" )),
vertexSrc_(iConfig.getParameter<edm::InputTag>("vertexSrc" )),
NAME_(iConfig.getParameter<string>("NAME" ))
{


  produces<vector<TupleElectron>>(NAME_).setBranchAlias(NAME_);


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


TupleElectronProducer::~TupleElectronProducer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TupleElectronProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{



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
std::cout<<" FOUND VERTEX AT INDEX "<<primary_vertex_indx<<std::endl;
const reco::Vertex & primary_vertex = vertices->at(primary_vertex_indx);
//cout<<" final max pt "<<primary_vertex.p4().pt()<<endl;



  // get electron collection
  edm::Handle<edm::View<pat::Electron> > electrons;
  iEvent.getByLabel(electronSrc_,electrons);

  auto_ptr<TupleElectronCollection> TupleElectrons (new TupleElectronCollection);

  const int TupleElectronSize = electrons->size();
  TupleElectrons->reserve( TupleElectronSize );


  edm::View<pat::Electron>::const_iterator electron;
  for(electron=electrons->begin(); electron!=electrons->end(); ++electron)
  {

    TupleElectron CurrentElectron;

    //////////////////////
    // some values should be available in this
    // scope

    int numberOfMissingInnerHits = 999;
    bool conversionVetoPass = 0;
    double relativeIsolation = 999.;

    ////////////////////////////////////////////
    // set electron quantities



    ////////////////
    //set_p4
    ////////////////
    CurrentElectron.set_p4(electron->p4());


    ////////////////
    //set_charge
    ////////////////
    CurrentElectron.set_charge(electron->charge());


    /* this does not work
    if(electron->PFParticle().isNonnull())
    {
    ////////////////
    //set_pfP4
    ////////////////
    math::PtEtaPhiMLorentzVector ptEtPhiM(electron->PFParticle()->pt(),electron->PFParticle()->eta(),
    electron->PFParticle()->phi(),electron->PFParticle()->mass());

    LorentzVector xyzt(ptEtPhiM.x(), ptEtPhiM.y(), ptEtPhiM.z(), ptEtPhiM.t());

    CurrentElectron.set_pfP4(xyzt);
  }
  */

  ////////////////
  //set_PFpdgId
  ////////////////
  CurrentElectron.set_PFpdgId(electron->pdgId());



  ////////////////
  //set_isEB
  ////////////////
  CurrentElectron.set_isEB(electron->isEB());


  ////////////////
  //set_isEE
  ////////////////
  CurrentElectron.set_isEE(electron->isEE());

  ////////////////
  //set_isEBEEGap
  ////////////////
  CurrentElectron.set_isEBEEGap(electron->isEBEEGap());

  ////////////////
  //set_isEBEtaGap
  ////////////////
  CurrentElectron.set_isEBEtaGap(electron->isEBEtaGap());

  ////////////////
  //set_isEBPhiGap
  ////////////////
  CurrentElectron.set_isEBPhiGap(electron->isEBPhiGap());

  ////////////////
  //set_isEEDeeGap
  ////////////////
  CurrentElectron.set_isEEDeeGap(electron->isEEDeeGap());

  ////////////////
  //set_isEERingGap
  ////////////////
  CurrentElectron.set_isEERingGap(electron->isEERingGap());

  ////////////////
  //set_sigmaEtaEta
  ////////////////
  CurrentElectron.set_sigmaEtaEta(electron->sigmaEtaEta());

  ////////////////
  //set_sigmaIetaIeta
  ////////////////
  CurrentElectron.set_sigmaIetaIeta(electron->sigmaIetaIeta());

  ////////////////
  //set_sigmaIphiIphi
  ////////////////
  CurrentElectron.set_sigmaIphiIphi(electron->sigmaIphiIphi());



  if(electron->gsfTrack().isNonnull())
  {

    ////////////////
    //set_numberOfMissingInnerHits
    ////////////////
    numberOfMissingInnerHits = electron->gsfTrack()->trackerExpectedHitsInner().numberOfLostHits();
    CurrentElectron.set_numberOfMissingInnerHits(numberOfMissingInnerHits);

    ////////////////
    //set_dz
    ////////////////
    CurrentElectron.set_dz(electron->gsfTrack()->dz(primary_vertex.position()));

    ////////////////
    //set_d0
    ////////////////
    CurrentElectron.set_d0(electron->gsfTrack()->d0(primary_vertex.position()));

  }

  ////////////////
  //set_passConversionVeto
  ////////////////
  conversionVetoPass = electron->passConversionVeto();
  CurrentElectron.set_passConversionVeto(conversionVetoPass);





  if(electron->genLepton())
  {
    ////////////////
    //set_genP4
    ////////////////
    CurrentElectron.set_genP4(electron->genLepton()->p4());

    ////////////////
    //set_GENpdgId
    ////////////////
    CurrentElectron.set_GENpdgId(electron->genLepton()->pdgId());
  }


  ////////////////
  //set_chargedHadronIso
  ////////////////
  CurrentElectron.set_chargedHadronIso(electron->chargedHadronIso());

  ////////////////
  //set_photonIso
  ////////////////
  CurrentElectron.set_photonIso(electron->photonIso());

  ////////////////
  //set_neutralHadronIso
  ////////////////
  CurrentElectron.set_neutralHadronIso(electron->neutralHadronIso());

  ////////////////
  //set_puChargedHadronIso
  ////////////////
  CurrentElectron.set_puChargedHadronIso(electron->puChargedHadronIso());

  ////////////////
  //set_relativeIso
  ////////////////

  relativeIsolation = 999.;
  double i_charged = electron->chargedHadronIso();
  double i_photons = electron->photonIso();
  double i_neutralhadrons = electron->neutralHadronIso();
  double i_deltabeta = electron->puChargedHadronIso();
  relativeIsolation = i_charged + std::max(i_neutralhadrons+i_photons-0.5*i_deltabeta,0.0);
  if(electron->pt()!=0) relativeIsolation/=electron->pt();

  CurrentElectron.set_relativeIso(relativeIsolation);



  ////////////////
  //set_mvaTrigV0
  ////////////////
  CurrentElectron.set_mvaTrigV0(electron->electronID("mvaTrigV0"));

  ////////////////
  //set_mvaTrigNoIPV0
  ////////////////
  CurrentElectron.set_mvaTrigNoIPV0(electron->electronID("mvaTrigNoIPV0"));

  ////////////////
  //set_mvaNonTrigV0
  ////////////////
  CurrentElectron.set_mvaNonTrigV0(electron->electronID("mvaNonTrigV0"));


  if(electron->superCluster().isNonnull())
  {
    ////////////////
    //set_SuperClusterEta
    ////////////////
    CurrentElectron.set_SuperClusterEta(electron->superCluster()->position().Eta());



    /////////////////
    // apply the electron
    // ID MVA

    // get the category for tight MVA id
    int category = -1;
    double Eta = electron->superCluster()->position().Eta();
    double mva = electron->electronID("mvaNonTrigV0");
    bool pass_fail = 0;

    category =  TupleHelpers::getMVAElectronIdCategory(electron->pt(), Eta, "TIGHT");
    pass_fail = TupleHelpers::doesItPassTightMVANonTrigV0(category, mva);

    std::cout<<" Electron category is "<<category<<std::endl;
    std::cout<<" Electron pass_fail is  "<<pass_fail<<std::endl;

    ////////////////
    //set_pass_tight_mvaNonTrigV0
    ////////////////
    CurrentElectron.set_pass_tight_mvaNonTrigV0(pass_fail);

    ////////////////
    //set_passFullId
    ////////////////

    bool passFullId = 1;


    if(  !(electron->pt() > 24)           ) {passFullId = 0; std::cout<<" Electron a "<<std::endl; }
    if(  !( fabs(electron->eta()) < 2.1)  ) {passFullId = 0; std::cout<<" Electron b "<<std::endl; }
    if(  !(pass_fail)                     ) {passFullId = 0; std::cout<<" Electron c "<<std::endl; }
    if(  !(relativeIsolation < 0.1)       ) {passFullId = 0; std::cout<<" Electron d "<<std::endl; }
    if(  !(numberOfMissingInnerHits==0)   ) {passFullId = 0; std::cout<<" Electron e "<<std::endl; }
    if(  !(conversionVetoPass)            ) {passFullId = 0; std::cout<<" Electron f "<<std::endl; }

    if(electron->gsfTrack().isNonnull())
    {

      if(  !( fabs(electron->gsfTrack()->dz(primary_vertex.position())) < 0.2)  ) {passFullId = 0; std::cout<<" Electron g "<<electron->gsfTrack()->dz()<<std::endl; }
      if(  !( fabs(electron->gsfTrack()->d0(primary_vertex.position())) < 0.045)  ) {passFullId = 0; std::cout<<" Electron h "<<electron->gsfTrack()->d0()<<std::endl; }

    }
    else {passFullId = 0; std::cout<<" Electron i "<<std::endl; }

    CurrentElectron.set_passFullId(passFullId);

    std::cout<<" Electron fullIdCheck is  "<<passFullId<<std::endl;




  }








  ////////////
  // store the electron

  TupleElectrons->push_back(CurrentElectron);

}


iEvent.put( TupleElectrons, NAME_ );




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
TupleElectronProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TupleElectronProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
TupleElectronProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TupleElectronProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TupleElectronProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TupleElectronProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleElectronProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleElectronProducer);
