// -*- C++ -*-
//
// Package:    TupleMuonTauProducer
// Class:      TupleMuonTauProducer
//
/**\class TupleMuonTauProducer TupleMuonTauProducer.cc TEMP/TupleMuonTauProducer/src/TupleMuonTauProducer.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Thu May 15 06:16:07 CDT 2014
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
#include "DataFormats/Math/interface/LorentzVector.h"
#include "UserCode/TupleObjects/interface/TupleTau.h"
#include "UserCode/TupleObjects/interface/TupleMuon.h"
#include "UserCode/TupleObjects/interface/TupleMuonTau.h"
#include "TauAnalysis/CandidateTools/interface/NSVfitStandaloneAlgorithm.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "DataFormats/Math/interface/LorentzVector.h"

#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETCollection.h"



typedef math::XYZTLorentzVector LorentzVector;
using namespace std;
using namespace edm;


//
// class declaration
//

class TupleMuonTauProducer : public edm::EDProducer {
public:
  explicit TupleMuonTauProducer(const edm::ParameterSet&);
  ~TupleMuonTauProducer();

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
  edm::InputTag muonSrc_;
  edm::InputTag mvametSrc_;
  const int SYS = 1;


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
TupleMuonTauProducer::TupleMuonTauProducer(const edm::ParameterSet& iConfig):
tauSrc_(iConfig.getParameter<edm::InputTag>("tauSrc" )),
muonSrc_(iConfig.getParameter<edm::InputTag>("muonSrc" )),
mvametSrc_(iConfig.getUntrackedParameter<edm::InputTag>("mvametSrc" ))
{



  if(SYS==0) produces< vector<TupleMuonTau> >("TupleMuonTaus_NOM").setBranchAlias("TupleMuonTaus_NOM");
  if(SYS==1) produces< vector<TupleMuonTau> >("TupleMuonTaus_SYS").setBranchAlias("TupleMuonTaus_SYS");


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


TupleMuonTauProducer::~TupleMuonTauProducer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TupleMuonTauProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{



  // get tuple muon and tau collections


  edm::Handle< TupleMuonCollection > muons;
  iEvent.getByLabel(muonSrc_, muons);

  edm::Handle< TupleTauCollection > taus;
  iEvent.getByLabel(tauSrc_, taus);

  // get the mva met

  edm::Handle<std::vector<reco::PFMET> > mvamet;
  iEvent.getByLabel(mvametSrc_, mvamet);




  ////////////

  auto_ptr<TupleMuonTauCollection> TupleMuonTaus (new TupleMuonTauCollection);

  const int TupleMuonTauSize = muons->size();
  TupleMuonTaus->reserve( TupleMuonTauSize );

  for (unsigned int i = 0; i < muons->size(); ++i)
  {

    for (unsigned int j = 0; j < taus->size(); ++j)
    {

      cout<<" i,j = "<<i<<","<<j;
      cout<<" muon PDGID "<<((*muons)[i]).pdgId();
      cout<<" tau PDGID "<<((*taus)[j]).pdgId()<<endl;

      TupleMuonTau CurrentMuonTau;

      CurrentMuonTau.set_p4(  ((*muons)[i]).p4() + ((*taus)[j]).p4() );
      CurrentMuonTau.set_muonIndex(i);
      CurrentMuonTau.set_tauIndex(j);
      CurrentMuonTau.set_corrected_p4( ((*muons)[i]).p4() + ((*taus)[j]).corrected_p4()   );
      CurrentMuonTau.set_scalarSumPt(((*muons)[i]).p4() , ((*taus)[j]).corrected_p4()  );
      CurrentMuonTau.set_DR(((*muons)[i]).p4() , ((*taus)[j]).corrected_p4()  );
      CurrentMuonTau.set_sumCharge(((*muons)[i]).charge() , ((*taus)[j]).charge()  );

      ////////////

      TMatrixD covMET(2, 2); // PFMET significance matrix
      std::vector<NSVfitStandalone::MeasuredTauLepton> measuredTauLeptons;

      ///////
      // it seems the order matters
      // pass the higher pt lepton 1st

      if( ((*muons)[i]).p4().pt() >=  ((*taus)[j]).corrected_p4().pt()  )
      {
        measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kLepDecay, ((*muons)[i]).p4()) );
        measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kHadDecay,
         ((*taus)[j]).corrected_p4()));
      }

      else
      {
        measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kHadDecay,
         ((*taus)[j]).corrected_p4()));
        measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kLepDecay, ((*muons)[i]).p4()) );


      }


      covMET = (*mvamet)[0].getSignificanceMatrix();
      NSVfitStandaloneAlgorithm algo(measuredTauLeptons, (*mvamet)[0].momentum(), covMET, 0);
      algo.addLogM(false);
      algo.integrateMarkovChain();
      //algo.integrateVEGAS(); ////Use this instead for VEGAS integration

      CurrentMuonTau.set_correctedSVFitMass(algo.getMass());

      //cout<<" diTauMassErr "<<algo.getMassUncert();
      //cout<<" diTauPt "<<algo.getPt();
      //cout<<" diTauPtErr "<<algo.getPtUncert();


      measuredTauLeptons.clear();

      ////////////
      // store the MuonTau

      TupleMuonTaus->push_back(CurrentMuonTau);


    }

  }

  if(SYS==0) iEvent.put( TupleMuonTaus, "TupleMuonTaus_NOM" );
  if(SYS==1) iEvent.put( TupleMuonTaus, "TupleMuonTaus_SYS" );


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
TupleMuonTauProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TupleMuonTauProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
TupleMuonTauProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TupleMuonTauProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TupleMuonTauProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TupleMuonTauProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleMuonTauProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleMuonTauProducer);
