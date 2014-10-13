// -*- C++ -*-
//
// Package:    TupleElectronTauVetoesProducer
// Class:      TupleElectronTauVetoesProducer
//
/**\class TupleElectronTauVetoesProducer TupleElectronTauVetoesProducer.cc TEMP/TupleElectronTauVetoesProducer/src/TupleElectronTauVetoesProducer.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Wed Sep 10 05:27:46 CDT 2014
// $Id$
//
//


// system include files
#include <memory>
#include <string>
#include <TMath.h>
#include <vector>


// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "DataFormats/Math/interface/LorentzVector.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "Math/GenVector/VectorUtil.h"
#include "UserCode/TupleHelpers/interface/TupleHelpers.hh"
#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "DataFormats/RecoCandidate/interface/IsoDepositVetos.h"
#include "DataFormats/PatCandidates/interface/Isolation.h"
#include "EgammaAnalysis/ElectronTools/interface/ElectronEffectiveArea.h"

#include "UserCode/TupleObjects/interface/TupleElectronTauVetoes.h"
#include "UserCode/TupleObjects/interface/TupleElectron.h"
#include "UserCode/TupleObjects/interface/TupleElectronTau.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Lepton.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/Math/interface/deltaR.h"


typedef math::XYZTLorentzVector LorentzVector;
using namespace reco::isodeposit;

//
// class declaration
//

class TupleElectronTauVetoesProducer : public edm::EDProducer {
public:
  explicit TupleElectronTauVetoesProducer(const edm::ParameterSet&);
  ~TupleElectronTauVetoesProducer();

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
  std::string NAME_;
  edm::InputTag patElectronSrc_;
  edm::InputTag patMuonSrc_;
  edm::InputTag tupleElectronTauSrc_;
  edm::InputTag tupleElectronSrc_;
  edm::InputTag vertexSrc_;
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
TupleElectronTauVetoesProducer::TupleElectronTauVetoesProducer(const edm::ParameterSet& iConfig):
NAME_(iConfig.getParameter<std::string>("NAME" )),
patElectronSrc_(iConfig.getParameter<edm::InputTag>("patElectronSrc" )),
patMuonSrc_(iConfig.getParameter<edm::InputTag>("patMuonSrc" )),
tupleElectronTauSrc_(iConfig.getParameter<edm::InputTag>("tupleElectronTauSrc" )),
tupleElectronSrc_(iConfig.getParameter<edm::InputTag>("tupleElectronSrc" )),
vertexSrc_(iConfig.getParameter<edm::InputTag>("vertexSrc" )),
pfSrc_(iConfig.getParameter<edm::InputTag>("pfSrc" ))
{


  produces< std::vector<TupleElectronTauVetoes> >(NAME_).setBranchAlias(NAME_);

}


TupleElectronTauVetoesProducer::~TupleElectronTauVetoesProducer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TupleElectronTauVetoesProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{


  ///////////////////////////
  // get the PAT electrons

  edm::Handle<edm::View<pat::Electron> > PATelectrons;
  iEvent.getByLabel(patElectronSrc_,PATelectrons);

  ///////////////////////////
  // get the PAT Muons

  edm::Handle<edm::View<pat::Muon> > PATmuons;
  iEvent.getByLabel(patMuonSrc_,PATmuons);


  ///////////////
  // read in electronTaus

  edm::Handle< TupleElectronTauCollection > electronTaus;
  iEvent.getByLabel(tupleElectronTauSrc_, electronTaus);

  //////////////
  // read in the TUPLE electrons

  edm::Handle< TupleElectronCollection > electrons;
  iEvent.getByLabel(tupleElectronSrc_, electrons);

  //////////////////
  // read in the vertex collection

  edm::Handle<edm::View<reco::Vertex> > vertices;
  iEvent.getByLabel(vertexSrc_,vertices);

  const reco::Vertex & first_vertex = vertices->at(0);

  // get pfCandidates collection
  edm::Handle<reco::PFCandidateCollection > pfCandidates;
  iEvent.getByLabel(pfSrc_,pfCandidates);



  ////////////

  std::auto_ptr<TupleElectronTauVetoesCollection> TupleElectronTauVetoesVec (new TupleElectronTauVetoesCollection);

  const int TupleElectronTauSize = electronTaus->size();
  TupleElectronTauVetoesVec->reserve( TupleElectronTauSize );


  //////////////
  // begin loop over eTau candidates :

  for (std::size_t i = 0; i < electronTaus->size(); ++i)
  {

    const TupleElectronTau electronTau =   ((*electronTaus)[i]);
    TupleElectronTauVetoes CurrentElectronTauVeto;

    const TupleElectron electron = ((*electrons)[electronTau.electronIndex()]);

    ///////////////////////
    // loop over PATmuons
    // get set the thirdlepton veto to
    // false if there exists an extra muon
    // meeting the veto cuts

    bool KEEP_THIRD = 1;

    edm::View<pat::Muon>::const_iterator muonIter;
    for(muonIter=PATmuons->begin(); muonIter!=PATmuons->end(); ++muonIter)
    {

      if(muonIter->pt() <= 10.0) continue;
      if( fabs(muonIter->eta()) >= 2.4) continue;
      double dz = 1000.0;
      double dxy = 1000.0;
      bool isTightMuon = 0;
      bool isPFMuon = 0;
      double relativeIsolation_DR4 = 999.;
      bool isTracker = 0; // not used

      TupleHelpers::setMuon_dz_dxy_isTight_isPF_isTracker_RelIsol(dz,dxy,isTightMuon,isPFMuon,isTracker,
      relativeIsolation_DR4,
      first_vertex,pfCandidates,&*muonIter);


      ///////////////////////////////////////
      if(fabs(dxy) >= 0.045) continue;
      if(fabs(dz) >= 0.2) continue;
      if(!muonIter->isGlobalMuon()) continue;
      if(!isTightMuon) continue;
      if(!isPFMuon) continue;
      if (relativeIsolation_DR4>=0.3) continue;

      ///////////////
      // if made it here the veto is set
      KEEP_THIRD = 0;

      ////////////////
      // exit the patMuon Loop
      break;

    }

    ///////////////////////////
    // in electron+Tau, the 3rd lepton
    // veto also includes an electron
    // check -- we will only do it if
    // the muons side has not yet set the veto

    if(KEEP_THIRD)
      {

      edm::View<pat::Electron>::const_iterator electronIter1;
      for(electronIter1=PATelectrons->begin(); electronIter1!=PATelectrons->end(); ++electronIter1)
        {

          ////////////////////////////////////
          // basic cuts on the veto electron

          if(electronIter1->pt()< 10) continue;
          if( fabs(electronIter1->eta()) > 2.5) continue;

          // no pairing the candidate with itself!
          //  checked with DR

          if(deltaR(electronIter1->p4(), electron.p4()) <= 0.3) continue;


          double dz = 999.;
          double dxy = 999.;
          int NumMissingHits = 9999;
          double relativeIsolation = 999.9;


          TupleHelpers::setElectron_dz_dxy_NumLostHits_RelIsol(
                                        dz, dxy, NumMissingHits,
                                        relativeIsolation,
                                        first_vertex,
                                        &*electronIter1);
          /////////////////////////////////
          if(fabs(dxy) >= 0.045) continue;
          if(fabs(dz) >= 0.2) continue;
          if(NumMissingHits!=0) continue;
          if(!electronIter1->passConversionVeto()) continue;
          if(relativeIsolation>=0.3) continue;

          /////////////////////////////
          bool MVAOR = 0;
          if(electronIter1->superCluster().isNonnull())
          {
            double mvaNonTrigV0  = electronIter1->electronID("mvaNonTrigV0");
            double mvaTrigNoIPV0 = electronIter1->electronID("mvaTrigNoIPV0");
            double ePT =  electronIter1->pt();
            double eSCETA = electronIter1->superCluster()->position().Eta();

               if(TupleHelpers::passesMVALooseNEW(ePT,eSCETA,mvaTrigNoIPV0)) MVAOR = 1;
               if(TupleHelpers::passesMVALoose(ePT,eSCETA,mvaNonTrigV0)) MVAOR = 1;

          }
          /////////////////////////////
          if(!MVAOR) continue;


          ///////////////
          // if made it here the veto is set
          KEEP_THIRD = 0;

          ////////////////
          // exit the patElectron Loop
          break;

        }
    }




    CurrentElectronTauVeto.set_passesThirdLeptonVeto(KEEP_THIRD);


    ////////////////////////////////////////
    // similarly look for patElectrons
    // that meet the veto requirements, here
    // however there are some cuts related to the
    // actual H candidate electron

    bool KEEP_SECOND = 1;

    edm::View<pat::Electron>::const_iterator electronIter;
    for(electronIter=PATelectrons->begin(); electronIter!=PATelectrons->end(); ++electronIter)
    {

        ////////////////////////////////////
        // basic cuts on the veto electron

        if(electronIter->pt()< 15) continue;
        if( fabs(electronIter->eta()) > 2.5) continue;

        ////////////////////////////
        double dz = 999.;
        double dxy = 999.;
        double relativeIsolation = 999.;
        int NumMissingHits = 999; // not cut on here

        TupleHelpers::setElectron_dz_dxy_NumLostHits_RelIsol(
                                      dz, dxy, NumMissingHits,
                                      relativeIsolation,
                                      first_vertex,
                                      &*electronIter);


        ////////////////////////////

        if( fabs(dxy) >= 0.045) continue;
        if( fabs(dz) >= 0.2) continue;
        if(relativeIsolation>=0.3) continue;


        //////////////////////////////////
        bool TheEBOrEECondition = 1;
        if(electronIter->isEB())
          {
            if( electronIter->sigmaIetaIeta() >= 0.010) TheEBOrEECondition = 0;
            if( electronIter->deltaPhiSuperClusterTrackAtVtx() >= 0.80) TheEBOrEECondition = 0;
            if( electronIter->deltaEtaSuperClusterTrackAtVtx() >= 0.007) TheEBOrEECondition = 0;
            if( electronIter->hadronicOverEm() >= 0.15) TheEBOrEECondition = 0;
          }
        else if(electronIter->isEE())
          {
            if( electronIter->sigmaIetaIeta() >= 0.030) TheEBOrEECondition = 0;
            if( electronIter->deltaPhiSuperClusterTrackAtVtx() >= 0.70) TheEBOrEECondition = 0;
            if( electronIter->deltaEtaSuperClusterTrackAtVtx() >= 0.010) TheEBOrEECondition = 0;
          }
        else TheEBOrEECondition = 0;
        //////////////////////////////////

        if(!TheEBOrEECondition) continue;


        //////////////////////////


        // no pairing the candidate e (electron) with itself!
        //  checked with DR(electronIter,electron)

        if(deltaR(electronIter->p4(), electron.p4()) <= 0.3) continue;

        //////////////////////////////////////////////////////
        // if the patElectron and our H candidate electron
        // electron do not have opp sign, do not veto the event
        // due to current electronIter

        if(electron.charge() == electronIter->charge()) continue;


        ///////////////
        // if made it here the veto is set
        KEEP_SECOND = 0;

        ////////////////
        // exit the patElectron Loop
        break;

    }

   CurrentElectronTauVeto.set_passesSecondLeptonVeto(KEEP_SECOND);






    ///////////////////////////
    // add the current veto
    std::cout<<" Electron Vetoes 2nd and 3rd "<<KEEP_SECOND<<" "<<KEEP_THIRD<<std::endl;
    TupleElectronTauVetoesVec->push_back(CurrentElectronTauVeto);

   }




  iEvent.put( TupleElectronTauVetoesVec, NAME_ );


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
TupleElectronTauVetoesProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TupleElectronTauVetoesProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
TupleElectronTauVetoesProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TupleElectronTauVetoesProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TupleElectronTauVetoesProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TupleElectronTauVetoesProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleElectronTauVetoesProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleElectronTauVetoesProducer);
