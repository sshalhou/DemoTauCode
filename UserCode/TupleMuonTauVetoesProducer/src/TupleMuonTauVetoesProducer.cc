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
patMuonSrc_(iConfig.getParameter<edm::InputTag>("patMuonSrc" )),
tupleMuonTauSrc_(iConfig.getParameter<edm::InputTag>("tupleMuonTauSrc" )),
tupleMuonSrc_(iConfig.getParameter<edm::InputTag>("tupleMuonSrc" )),
vertexSrc_(iConfig.getParameter<edm::InputTag>("vertexSrc" )),
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
      bool isTightMuon = 0;
      bool isPFMuon = 0;
      double relativeIsolation_DR4 = 999.;
      bool isTracker = 0; // not used

      TupleHelpers::setMuon_dz_dxy_isTight_isPF_isTracker_RelIsol(dz,dxy,isTightMuon,isPFMuon,isTracker,
      relativeIsolation_DR4,
      first_vertex,pfCandidates,&*muonIter);

      if(fabs(dxy) >= 0.045) continue;
      if(fabs(dz) >= 0.2) continue;
      if(!muonIter->isGlobalMuon()) continue;
      if(!isTightMuon) continue;
      if(!isPFMuon) continue;
      if (relativeIsolation_DR4>=0.3) continue;

      ///////////////////////////////////
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


          double dz = 999.;
          double dxy = 999.;
          int NumMissingHits = 9999;
          double relativeIsolation = 999.9;


          TupleHelper::setElectron_dz_dxy_NumLostHits_RelIsol(
                                        dz, dxy, NumMissingHits,
                                        relativeIsolation,
                                        first_vertex,
                                        &*electronIter)


          TupleHelpers::setMuon_dz_dxy_isTight_isPF_isTracker_RelIsol(dz,dxy,isTightMuon,isPFMuon,isTracker,
          relativeIsolation_DR4,
          first_vertex,pfCandidates,&*muonIter);


          //////////////////
          if( fabs(dxy) >= 0.045) continue;
          if( fabs(dz) >= 0.2) continue;
          if(NumMissingHits!=0) continue;
          if(!electronIter->passConversionVeto()) continue;
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


      edm::View<pat::Muon>::const_iterator muonIter2;
      for(muonIter2=PATmuons->begin(); muonIter2!=PATmuons->end(); ++muonIter2)
      {

        if(muonIter2->pt() <= 15.0) continue;
        if( fabs(muonIter2->eta()) >= 2.4) continue;
        double dz = 1000.0;
        double dxy = 1000.0;
        bool isTightMuon = 0;
        bool isPFMuon = 0;
        double relativeIsolation_DR4 = 999.;
        bool isTracker = 0; // not used

        TupleHelpers::setMuon_dz_dxy_isTight_isPF_isTracker_RelIsol(dz,dxy,isTightMuon,isPFMuon,isTracker,
        relativeIsolation_DR4,
        first_vertex,pfCandidates,&*muonIter);

        if(fabs(dxy) >= 0.045) continue;
        if(fabs(dz) >= 0.2) continue;
        if(!muonIter2->isGlobalMuon()) continue;
        if(!isPFMuon) continue;
        if (relativeIsolation_DR4>=0.3) continue;

        // no pairing the candidate with itself!
        //  checked with DR

        if(deltaR(muonIter2->p4(), muon.p4()) <= 0.3) continue;

        //////////////////////////////////////////////////////
        // if the patMuon and our H candidate muon
        //  do not have opp sign, do not veto the event


        if(muon.charge() == muonIter2->charge()) continue;

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


  iEvent.put( TupleMuonTauVetoesVec, NAME_ );


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
