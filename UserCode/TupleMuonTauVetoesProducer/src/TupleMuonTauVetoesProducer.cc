// -*- C++ -*-
//
// Package:    TupleMuonTauVetoesProducer
// Class:      TupleMuonTauVetoesProducer
//
/**\class TupleMuonTauVetoesProducer TupleMuonTauVetoesProducer.cc TEMP/TupleMuonTauVetoesProducer/src/TupleMuonTauVetoesProducer.cc

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
#include "UserCode/TupleObjects/interface/TupleMuonTauVetoes.h"


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

#include "UserCode/TupleObjects/interface/TupleMuonTau.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Lepton.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/Math/interface/deltaR.h"


using namespace reco::isodeposit;
typedef math::XYZTLorentzVector LorentzVector;


//
// class declaration
//

class TupleMuonTauVetoesProducer : public edm::EDProducer {
public:
  explicit TupleMuonTauVetoesProducer(const edm::ParameterSet&);
  ~TupleMuonTauVetoesProducer();

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
edm::InputTag tupleMuonTauSrc_;
edm::InputTag tupleMuonSrc_;
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
TupleMuonTauVetoesProducer::TupleMuonTauVetoesProducer(const edm::ParameterSet& iConfig):
NAME_(iConfig.getParameter<std::string>("NAME" )),
patElectronSrc_(iConfig.getParameter<edm::InputTag>("patElectronSrc" )),
patMuonSrc_(iConfig.getParameter<edm::InputTag>("patMuonSrc_" )),
tupleMuonTauSrc_(iConfig.getParameter<edm::InputTag>("tupleMuonTauSrc_" )),
tupleMuonSrc_(iConfig.getParameter<edm::InputTag>("tupleMuonSrc_" )),
vertexSrc_(iConfig.getParameter<edm::InputTag>("vertexSrc_" )),
pfSrc_(iConfig.getParameter<edm::InputTag>("pfSrc" ))
{


  produces< std::vector<TupleMuonTauVetoes> >(NAME_).setBranchAlias(NAME_);


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


TupleMuonTauVetoesProducer::~TupleMuonTauVetoesProducer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TupleMuonTauVetoesProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  ///////////////////////////
  // get the PAT Muons

  edm::Handle<edm::View<pat::Muon> > PATmuons;
  iEvent.getByLabel(patMuonSrc_,PATmuons);


  ///////////////////////////
  // get the PAT electrons

  edm::Handle<edm::View<pat::Electron> > PATelectrons;
  iEvent.getByLabel(patElectronSrc_,PATelectrons);




  ///////////////
  // read in muonTaus

  edm::Handle< TupleMuonTauCollection > muonTaus;
  iEvent.getByLabel(tupleMuonTauSrc_, muonTaus);

  //////////////
  // read in the TUPLE muons

  edm::Handle< TupleMuonCollection > muons;
  iEvent.getByLabel(tupleMuonSrc_, muons);

  //////////////////
  // read in the vertex collection

  edm::Handle<edm::View<reco::Vertex> > vertices;
  iEvent.getByLabel(vertexSrc_,vertices);

  const reco::Vertex & first_vertex = vertices->at(0);

  // get pfCandidates collection
  edm::Handle<reco::PFCandidateCollection > pfCandidates;
  iEvent.getByLabel(pfSrc_,pfCandidates);



  ////////////

  std::auto_ptr<TupleMuonTauVetoesCollection> TupleMuonTauVetoesVec (new TupleMuonTauVetoesCollection);

  const int TupleMuonTauSize = muonTaus->size();
  TupleMuonTauVetoesVec->reserve( TupleMuonTauSize );


  //////////////
  // begin loop over muonTau candidates :

  for (std::size_t i = 0; i < muonTaus->size(); ++i)
  {

    const TupleMuonTau muonTau =   ((*muonTaus)[i]);
    TupleMuonTauVetoes CurrentMuonTauVeto;

    const TupleMuon muon = ((*muons)[muonTau.muonIndex()]);


    bool KEEP_THIRD = 1;


    ///////////////////////
    // loop over PATmuons
    // get set the thirdlepton veto to
    // false if there exists an extra muon
    // meeting the veto cuts

    edm::View<pat::Muon>::const_iterator muonIter;
    for(muonIter=PATmuons->begin(); muonIter!=PATmuons->end(); ++muonIter)
    {

      if(muonIter->pt() <= 10.0) continue;
      if( fabs(muonIter->eta()) >= 2.4) continue;
      double dz = 1000.0;
      double dxy = 1000.0;

      if(!muonIter->innerTrack().isNull())
      {
        dz = muonIter->innerTrack()->dz(first_vertex.position());
        dxy = muonIter->innerTrack()->dxy(first_vertex.position());

      }

      if(fabs(dxy) >= 0.045) continue;
      if(fabs(dz) >= 0.2) continue;
      if(!muonIter->isGlobalMuon()) continue;

      //////////////////////////////
      bool isTightMuon = 1;
      if(   !(muonIter->isGlobalMuon())                 ) isTightMuon = 0;
      if(   !(muonIter->numberOfMatchedStations()>1)    ) isTightMuon = 0;
      if(    muonIter->innerTrack().isNonnull() && muonIter->track().isNonnull() && muonIter->globalTrack().isNonnull() )
      {

        if(   !(muonIter->globalTrack()->normalizedChi2()<10) ) isTightMuon = 0;
        if(   !((muonIter->globalTrack()->hitPattern()).numberOfValidMuonHits()>0) ) isTightMuon = 0;
        if(   !((muonIter->innerTrack()->hitPattern()).numberOfValidPixelHits()>0) ) isTightMuon = 0;
        if(   !((muonIter->track()->hitPattern()).trackerLayersWithMeasurement()>5) ) isTightMuon = 0;

      } else isTightMuon = 0;
      /////////////////////////////////

      if(!isTightMuon) continue;


      /////////////////////////////

        bool isPFMuon = 0;

          for(size_t pf = 0; pf < pfCandidates->size(); pf++)
          {


            if( (*pfCandidates)[pf].particleId() == reco::PFCandidate::mu )
            {
              reco::MuonRef muonRefToPFMuon = (*pfCandidates)[pf].muonRef();


              if( muonRefToPFMuon.isNonnull() )
              {
                if(deltaR( muonRefToPFMuon->p4() , muonIter->p4()) < 1e-04)
                {
                  if(muonRefToPFMuon->isGlobalMuon() || muonRefToPFMuon->isTrackerMuon() )
                  {
                    isPFMuon = 1;
                  }
                }
              }


            }
          }

      /////////////////////////////
        if(!isPFMuon) continue;


      /////////////
      // compute
      // isol
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



      vetos2012PFIdCharged.push_back(new ConeVeto(Direction(muonIter->eta(),muonIter->phi()),0.00010));
      vetos2012PFIdCharged.push_back(new ThresholdVeto(0.00));

      vetos2012PFIdPhotons.push_back(new ConeVeto(Direction(muonIter->eta(),muonIter->phi()),0.010));
      vetos2012PFIdPhotons.push_back(new ThresholdVeto(0.50));

      vetos2012PFIdNeutral.push_back(new ConeVeto(Direction(muonIter->eta(),muonIter->phi()),0.010));
      vetos2012PFIdNeutral.push_back(new ThresholdVeto(0.50));

      vetos2012PFIdPUCharged.push_back(new ConeVeto(Direction(muonIter->eta(),muonIter->phi()),0.010));
      vetos2012PFIdPUCharged.push_back(new ThresholdVeto(0.50));

      allChIso04PFId = muonIter->isoDeposit(pat::PfChargedAllIso)->depositAndCountWithin(0.4, vetos2012PFIdCharged).first;
      nhIso04PFId = muonIter->isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.4, vetos2012PFIdNeutral).first;
      phIso04PFId = muonIter->isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.4, vetos2012PFIdPhotons).first;
      nhIsoPU04PFId = muonIter->isoDeposit(pat::PfPUChargedHadronIso)->depositAndCountWithin(0.4, vetos2012PFIdPUCharged).first;

      relativeIsolation_DR4 = allChIso04PFId + std::max(nhIso04PFId+phIso04PFId-0.5*nhIsoPU04PFId,0.0);
      if(muonIter->pt()!=0) relativeIsolation_DR4/=muonIter->pt();

      for(unsigned int i = 0; i <vetos2012PFIdCharged.size(); i++) delete vetos2012PFIdCharged[i];
      for(unsigned int i = 0; i <vetos2012PFIdNeutral.size(); i++) delete vetos2012PFIdNeutral[i];
      for(unsigned int i = 0; i <vetos2012PFIdPhotons.size(); i++) delete vetos2012PFIdPhotons[i];
      for(unsigned int i = 0; i <vetos2012PFIdPUCharged.size(); i++) delete vetos2012PFIdPUCharged[i];

      ////////////
      if (relativeIsolation_DR4>=0.3) continue;

      // in the muon leg of the muonTau 3rd Lep veto
      // there is a DR cut too

      if(deltaR(muonIter->p4(), muon.p4()) <= 0.3) continue;


      ///////////////
      // if made it here the veto is set
      KEEP_THIRD = 0;

      ////////////////
      // exit the patMuon Loop
      break;

    }

    ///////////////////////////
    // in muon+Tau, the 3rd lepton
    // veto also includes an electron
    // check -- we will only do it if
    // the muons side has not yet set the veto

    if(KEEP_THIRD)
      {

      edm::View<pat::Electron>::const_iterator electronIter;
      for(electronIter=PATelectrons->begin(); electronIter!=PATelectrons->end(); ++electronIter)
        {

          ////////////////////////////////////
          // basic cuts on the veto electron

          if(electronIter->pt()< 10) continue;
          if( fabs(electronIter->eta()) > 2.5) continue;

          ////////////////////////////
          double dz = 999.;
          double dxy = 999.;

          if(electronIter->gsfTrack().isNonnull())
            {
              dz = electronIter->gsfTrack()->dz(first_vertex.position());
              dxy = electronIter->gsfTrack()->dxy(first_vertex.position());
            }
          else if(electronIter->track().isNonnull())
          {

            dz = electronIter->track()->dz(first_vertex.position());
            dxy = electronIter->gsfTrack()->dxy(first_vertex.position());
          }
          ////////////////////////////

          if( fabs(dxy) >= 0.045) continue;
          if( fabs(dz) >= 0.2) continue;

          //////////////////////////
          bool nHitsZero = 1;
          if(electronIter->gsfTrack().isNonnull())
          {
            if(electronIter->gsfTrack()->trackerExpectedHitsInner().numberOfLostHits()!=0) nHitsZero = 0;
          }
          else nHitsZero = 0;
          //////////////////////////
          if(!nHitsZero) continue;

          if(!electronIter->passConversionVeto()) continue;

          /////////////////////////
          // now compute the isolation

          double relativeIsolation = 999.;

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

          vetos2012EBPFIdCharged.push_back(new ConeVeto(Direction(electronIter->eta(),electronIter->phi()),0.010));
          vetos2012EBPFIdPhotons.push_back(new ConeVeto(Direction(electronIter->eta(),electronIter->phi()),0.08));
          vetos2012EEPFIdCharged.push_back(new ConeVeto(Direction(electronIter->eta(),electronIter->phi()),0.015));
          vetos2012EEPFIdPhotons.push_back(new ConeVeto(Direction(electronIter->eta(),electronIter->phi()),0.08));

          float allChIso04EBPFId =    electronIter->isoDeposit(pat::PfChargedAllIso)->depositAndCountWithin(0.4, vetos2012EBPFIdCharged).first;
          float allChIso04EEPFId =  electronIter->isoDeposit(pat::PfChargedAllIso)->depositAndCountWithin(0.4, vetos2012EEPFIdCharged).first;
          allChIso04PFId =  (electronIter->isEB())*allChIso04EBPFId + (electronIter->isEE())*allChIso04EEPFId ;

          float nhIso04EBPFId = electronIter->isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.4, vetos2012EBPFIdNeutral).first;
          float nhIso04EEPFId = electronIter->isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.4, vetos2012EEPFIdNeutral).first;
          nhIso04PFId =  (electronIter->isEB())*nhIso04EBPFId + (electronIter->isEE())*nhIso04EEPFId ;

          float phIso04EBPFId =   electronIter->isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.4, vetos2012EBPFIdPhotons).first;
          float phIso04EEPFId = electronIter->isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.4, vetos2012EEPFIdPhotons).first;
          phIso04PFId =  (electronIter->isEB())*phIso04EBPFId + (electronIter->isEE())*phIso04EEPFId ;

          float nhIsoPU04EBPFId =   electronIter->isoDeposit(pat::PfPUChargedHadronIso)->depositAndCountWithin(0.4, vetos2012EBPFIdNeutral).first;
          float nhIsoPU04EEPFId =   electronIter->isoDeposit(pat::PfPUChargedHadronIso)->depositAndCountWithin(0.4, vetos2012EEPFIdNeutral).first;
          nhIsoPU04PFId =     (electronIter->isEB())*nhIsoPU04EBPFId + (electronIter->isEE())*nhIsoPU04EEPFId ;

          relativeIsolation = allChIso04PFId + std::max(nhIso04PFId+phIso04PFId-0.5*nhIsoPU04PFId,0.0);
          if(electronIter->pt()!=0) relativeIsolation/=electronIter->pt();

          for(unsigned int i = 0; i <vetos2012EBPFIdCharged.size(); i++) delete vetos2012EBPFIdCharged[i];
          for(unsigned int i = 0; i <vetos2012EBPFIdPhotons.size(); i++) delete vetos2012EBPFIdPhotons[i];
          for(unsigned int i = 0; i <vetos2012EBPFIdNeutral.size(); i++) delete vetos2012EBPFIdNeutral[i];
          for(unsigned int i = 0; i <vetos2012EEPFIdCharged.size(); i++) delete vetos2012EEPFIdCharged[i];
          for(unsigned int i = 0; i <vetos2012EEPFIdPhotons.size(); i++) delete vetos2012EEPFIdPhotons[i];
          for(unsigned int i = 0; i <vetos2012EEPFIdNeutral.size(); i++) delete vetos2012EEPFIdNeutral[i];
          //////////////////////////
          if(relativeIsolation>=0.3) continue;


          /////////////////////////////
          bool MVAOR = 0;
          if(electronIter->superCluster().isNonnull())
          {
            double mvaNonTrigV0  = electronIter->electronID("mvaNonTrigV0");
            double mvaTrigNoIPV0 = electronIter->electronID("mvaTrigNoIPV0");
            double ePT =  electronIter->pt();
            double eSCETA = electronIter->superCluster()->position().Eta();

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

      CurrentMuonTauVeto.set_passesThirdLeptonVeto(KEEP_THIRD);



      ////////////////////////////////////////
      // The Second Lepton Veto for MuonTau
      // involves looking for an additional muon

      bool KEEP_SECOND = 1;


      edm::View<pat::Muon>::const_iterator muonIter;
      for(muonIter=PATmuons->begin(); muonIter!=PATmuons->end(); ++muonIter)
      {

        if(muonIter->pt() <= 15.0) continue;
        if( fabs(muonIter->eta()) >= 2.4) continue;
        double dz = 1000.0;
        double dxy = 1000.0;

        if(!muonIter->innerTrack().isNull())
        {
          dz = muonIter->innerTrack()->dz(first_vertex.position());
          dxy = muonIter->innerTrack()->dxy(first_vertex.position());

        }

        if(fabs(dxy) >= 0.045) continue;
        if(fabs(dz) >= 0.2) continue;
        if(!muonIter->isGlobalMuon()) continue;

        /////////////////////////////

          bool isPFMuon = 0;

            for(size_t pf = 0; pf < pfCandidates->size(); pf++)
            {


              if( (*pfCandidates)[pf].particleId() == reco::PFCandidate::mu )
              {
                reco::MuonRef muonRefToPFMuon = (*pfCandidates)[pf].muonRef();


                if( muonRefToPFMuon.isNonnull() )
                {
                  if(deltaR( muonRefToPFMuon->p4() , muonIter->p4()) < 1e-04)
                  {
                    if(muonRefToPFMuon->isGlobalMuon() || muonRefToPFMuon->isTrackerMuon() )
                    {
                      isPFMuon = 1;
                    }
                  }
                }


              }
            }

        /////////////////////////////
          if(!isPFMuon) continue;
        /////////////
        // compute
        // isol
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



        vetos2012PFIdCharged.push_back(new ConeVeto(Direction(muonIter->eta(),muonIter->phi()),0.00010));
        vetos2012PFIdCharged.push_back(new ThresholdVeto(0.00));

        vetos2012PFIdPhotons.push_back(new ConeVeto(Direction(muonIter->eta(),muonIter->phi()),0.010));
        vetos2012PFIdPhotons.push_back(new ThresholdVeto(0.50));

        vetos2012PFIdNeutral.push_back(new ConeVeto(Direction(muonIter->eta(),muonIter->phi()),0.010));
        vetos2012PFIdNeutral.push_back(new ThresholdVeto(0.50));

        vetos2012PFIdPUCharged.push_back(new ConeVeto(Direction(muonIter->eta(),muonIter->phi()),0.010));
        vetos2012PFIdPUCharged.push_back(new ThresholdVeto(0.50));

        allChIso04PFId = muonIter->isoDeposit(pat::PfChargedAllIso)->depositAndCountWithin(0.4, vetos2012PFIdCharged).first;
        nhIso04PFId = muonIter->isoDeposit(pat::PfNeutralHadronIso)->depositAndCountWithin(0.4, vetos2012PFIdNeutral).first;
        phIso04PFId = muonIter->isoDeposit(pat::PfGammaIso)->depositAndCountWithin(0.4, vetos2012PFIdPhotons).first;
        nhIsoPU04PFId = muonIter->isoDeposit(pat::PfPUChargedHadronIso)->depositAndCountWithin(0.4, vetos2012PFIdPUCharged).first;

        relativeIsolation_DR4 = allChIso04PFId + std::max(nhIso04PFId+phIso04PFId-0.5*nhIsoPU04PFId,0.0);
        if(muonIter->pt()!=0) relativeIsolation_DR4/=muonIter->pt();

        for(unsigned int i = 0; i <vetos2012PFIdCharged.size(); i++) delete vetos2012PFIdCharged[i];
        for(unsigned int i = 0; i <vetos2012PFIdNeutral.size(); i++) delete vetos2012PFIdNeutral[i];
        for(unsigned int i = 0; i <vetos2012PFIdPhotons.size(); i++) delete vetos2012PFIdPhotons[i];
        for(unsigned int i = 0; i <vetos2012PFIdPUCharged.size(); i++) delete vetos2012PFIdPUCharged[i];

        ////////////
        if (relativeIsolation_DR4>=0.3) continue;

        // no pairing the candidate with itself!
        //  checked with DR

        if(deltaR(muonIter->p4(), muon.p4()) <= 0.3) continue;

        //////////////////////////////////////////////////////
        // if the patMuon and our H candidate muon
        //  do not have opp sign, do not veto the event


        if(muon.charge() == MuonIter->charge()) continue;

        ///////////////
        // if made it here the veto is set
        KEEP_SECOND = 0;

        ////////////////
        // exit the  Loop
        break;

      }

      CurrentMuonTauVeto.set_passesSecondLeptonVeto(KEEP_SECOND);


     ///////////////////////////
     // add the current veto
     std::cout<<" Muon Vetoes 2nd and 3rd "<<KEEP_SECOND<<" "<<KEEP_THIRD<<std::endl;
     TupleMuonTauVetoesVec->push_back(CurrentMuonTauVeto);



  }


  iEvent.put( TupleMuonTauVetoess, NAME_ );


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
TupleMuonTauVetoesProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TupleMuonTauVetoesProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
TupleMuonTauVetoesProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TupleMuonTauVetoesProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TupleMuonTauVetoesProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TupleMuonTauVetoesProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleMuonTauVetoesProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleMuonTauVetoesProducer);
