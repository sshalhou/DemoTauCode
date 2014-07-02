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
#include <string>

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
#include "Math/GenVector/VectorUtil.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETCollection.h"
#include "UserCode/RecoilCorrector/interface/RecoilCorrector.hh"
#include "UserCode/GenBosonDecayFinder/interface/GenBosonDecayFinder.hh"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "UserCode/TupleHelpers/interface/TupleHelpers.hh"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/PileupJetIdentifier.h"


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
  edm::InputTag genSrc_;
  edm::InputTag jetSrc_;
  double iFluc_;
  double iScale_;
  string NAME_;
  edm::InputTag puJetIdMVASrc_;
  edm::InputTag puJetIdFlagSrc_;
  bool doSVFit_;

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
mvametSrc_(iConfig.getParameter<edm::InputTag>("mvametSrc" )),
genSrc_(iConfig.getParameter<edm::InputTag>("genSrc" )),
jetSrc_(iConfig.getParameter<edm::InputTag>("jetSrc" )),
iFluc_(iConfig.getParameter<double>("iFluc" )),
iScale_(iConfig.getParameter<double>("iScale" )),
NAME_(iConfig.getParameter<string>("NAME" )),
puJetIdMVASrc_(iConfig.getParameter<edm::InputTag>("puJetIdMVASrc" )),
puJetIdFlagSrc_(iConfig.getParameter<edm::InputTag>("puJetIdFlagSrc" )),
doSVFit_(iConfig.getParameter<bool>("doSVFit" ))
{





  produces< vector<TupleMuonTau> >(NAME_).setBranchAlias(NAME_);


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



  // get tuple muon and tau and jet collections


  edm::Handle< TupleMuonCollection > muons;
  iEvent.getByLabel(muonSrc_, muons);

  edm::Handle< TupleTauCollection > taus;
  iEvent.getByLabel(tauSrc_, taus);

  edm::Handle<edm::View<pat::Jet> > jets;
  iEvent.getByLabel(jetSrc_,jets);

  std::size_t njet = jets->size();

  ///////////////////////////////////////
  // figure out how many of these jets
  // pass the loose WP



  edm::Handle<ValueMap<float> > puJetIdMVA;
  //iEvent.getByLabel("puJetMva","full53xDiscriminant",puJetIdMVA);
  iEvent.getByLabel(puJetIdMVASrc_,puJetIdMVA);


  edm::Handle<ValueMap<int> > puJetIdFlag;
  //iEvent.getByLabel("puJetMva","full53xId",puJetIdFlag);
  iEvent.getByLabel(puJetIdFlagSrc_,puJetIdFlag);


  njet = 0;

  for ( unsigned int i=0; i<jets->size(); ++i )
  {
    const pat::Jet & patjet = jets->at(i);
    float mva   = (*puJetIdMVA)[jets->refAt(i)];
    int    idflag = (*puJetIdFlag)[jets->refAt(i)];
//    std::cout << "jet " << i << " pt " << patjet.pt() << " eta " << patjet.eta() << " PUJetIDMVA " << mva;
//    std::cout<<" loose WP = "<<PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kLoose );
    if(PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kLoose )) njet++;
  }


  ///////////////////////////////////



  // get the mva met

  edm::Handle<std::vector<reco::PFMET> > mvamet;
  iEvent.getByLabel(mvametSrc_, mvamet);

  // get the gen particles

  edm::Handle<std::vector<reco::GenParticle> > gen;
  iEvent.getByLabel(genSrc_, gen);

  // print the parameters passed by the config file

  cout<<" NAME_, iFluc_, iScale_ "<<NAME_<<" "<<iFluc_<<" "<<iScale_<<endl;

  ////////////

  auto_ptr<TupleMuonTauCollection> TupleMuonTaus (new TupleMuonTauCollection);

  const int TupleMuonTauSize = muons->size();
  TupleMuonTaus->reserve( TupleMuonTauSize );
  const reco::PFMET mvaMETpf =  (*mvamet)[0];




  // declare & init to raw value before applying recoil corrections
  NSVfitStandalone::Vector NSVcorrectedMET = mvaMETpf.momentum();
  math::PtEtaPhiMLorentzVector correctedMET(mvaMETpf.pt(),0.0,mvaMETpf.phi(),0.0);

  ///////////////////
  // find max pt pair

  std::size_t max_i = 0;
  std::size_t max_j = 0;
  int max_pt = -999;

  for (std::size_t i = 0; i < muons->size(); ++i)
  {

    const TupleMuon muon =   ((*muons)[i]);

    for (std::size_t j = 0; j < taus->size(); ++j)
    {

      const TupleTau tau =   ((*taus)[j]);

      if(tau.passFullId_muTau() && muon.passFullId())
      { // temp

        if(tau.p4().pt()+muon.p4().pt() >= max_pt)
        {
          max_pt = (tau.p4().pt()+muon.p4().pt());
          max_i = i;
          max_j = j;
        }

      }
    }
  }



  for (std::size_t i = 0; i < muons->size(); ++i)
  {

    const TupleMuon muon =   ((*muons)[i]);

    for (std::size_t j = 0; j < taus->size(); ++j)
    {

      const TupleTau tau =   ((*taus)[j]);

      if(tau.passFullId_muTau() && muon.passFullId())
      { // temp


        cout<<" i,j = "<<i<<","<<j;
        cout<<" muon PDGID "<<muon.pdgId();
        cout<<" tau PDGID "<<tau.pdgId()<<endl;


        TupleMuonTau CurrentMuonTau;

        if(max_i == i && max_j == j) CurrentMuonTau.set_MAX(1);
        else CurrentMuonTau.set_MAX(0);


        //////////////////
        // check triggers

        if(muon.has_HltMatchMu17()==1 && tau.has_HltMatchMu17()==1) CurrentMuonTau.set_isGoodTriggerPair(1);
        else if(muon.has_HltMatchMu18()==1 && tau.has_HltMatchMu18()==1) CurrentMuonTau.set_isGoodTriggerPair(1);
        else if(muon.has_HltMatchMu24()==1 && tau.has_HltMatchMu24()==1) CurrentMuonTau.set_isGoodTriggerPair(1);


        CurrentMuonTau.set_p4(  muon.p4() + tau.p4() );
        CurrentMuonTau.set_muonIndex(i);
        CurrentMuonTau.set_tauIndex(j);
        CurrentMuonTau.set_corrected_p4( muon.p4() + tau.p4()   );
        CurrentMuonTau.set_scalarSumPt(muon.p4() , tau.p4()  );
        CurrentMuonTau.set_DR(muon.p4() , tau.p4()  );
        CurrentMuonTau.set_mvaMETraw(mvaMETpf.pt());
        CurrentMuonTau.set_mvaMETphiRaw(mvaMETpf.phi());


        //      CurrentMuonTau.set_corrected_p4( muon.p4() + tau.corrected_p4()   );
        //      CurrentMuonTau.set_scalarSumPt(muon.p4() , tau.corrected_p4()  );
        //      CurrentMuonTau.set_DR(muon.p4() , tau.corrected_p4()  );
        CurrentMuonTau.set_sumCharge(muon.charge() , tau.charge()  );

        ////////////
        // apply Phil's recoil
        // corrections to the MET before
        // running SVFit to MC only

        if( !iEvent.isRealData() )
        {
          double met=mvaMETpf.pt();
          double metphi=mvaMETpf.phi();
          //        double leptonPt = ( muon.p4() + tau.corrected_p4()   ).pt();
          //        double leptonPhi  = ( muon.p4() + tau.corrected_p4()   ).phi();
          cout<<" turned off tau ES correction"<<endl;
          double leptonPt = ( muon.p4() + tau.p4()   ).pt();
          double leptonPhi  = ( muon.p4() + tau.p4()   ).phi();

          double GenZPt = 0.0;
          double GenZPhi = 0.0;
          double iU1 = 0.0;
          double iU2 = 0.0;

          ////////////////
          // There are specific corrections
          // for H->tau tau, W, Z, and Zmm.
          // As of Summer 2013, H,W, and Z use 53X_20pv
          // while Zmm uses 53X_2012 for the process.
          // For data Zmm and simulated Zmm, we use 53X_2012.
          // The function genDecayFinder can figure out the process
          // while whichRecoilCorrectionFiles will return the
          // correct set of files for the correction

          int BosonPdgId = 0;
          LorentzVector BosonP4(0,0,0,0);
          int DaughterOnePdgId = 0;
          LorentzVector DaughterOneP4(0,0,0,0);
          int DaughterTwoPdgId = 0;
          LorentzVector DaughterTwoP4(0,0,0,0);
          bool ApplyRecoilCorrection = 1;


          GenBosonDecayFinder genDecayFinder;
          genDecayFinder.findBosonAndDaugters(*gen,BosonPdgId,BosonP4,DaughterOnePdgId,
          DaughterOneP4,DaughterTwoPdgId,
          DaughterTwoP4,ApplyRecoilCorrection);

          cout<<BosonPdgId<<" = BosonPdgId "<<endl;
          cout<<DaughterOnePdgId<<" = DaughterOnePdgId "<<endl;
          cout<<DaughterTwoPdgId<<" = DaughterTwoPdgId "<<endl;
          ApplyRecoilCorrection = 0;
          cout<<ApplyRecoilCorrection<<" = ApplyRecoilCorrection "<<endl;


          if(ApplyRecoilCorrection)
          {

            GenZPt = (DaughterOneP4+DaughterTwoP4).pt();
            GenZPhi = (DaughterOneP4+DaughterTwoP4).phi();

            std::string DataFile;
            std::string MCFile;
            std::string ProcessFile;



            whichRecoilCorrectionFiles(BosonPdgId, DaughterOnePdgId,
            DaughterTwoPdgId, njet, ProcessFile, DataFile, MCFile);

            cout<<" files = "<<ProcessFile<<" "<<DataFile<<" "<<MCFile<<endl;

            // not sure what random seed we should be using?
            // do we really want it to be random?
            cout<<" applying recoil corrections with random seed : 0xDEADBEEF"<<endl;

            RecoilCorrector corrector(ProcessFile,0xDEADBEEF);
            corrector.addDataFile(DataFile);
            corrector.addMCFile(MCFile);

            //////////////////////
            // print out the uncorrected value
            cout<<" Before Correction : "<<met<<" "<<metphi<<endl;

            corrector.CorrectType1(  met,
            metphi,
            GenZPt,
            GenZPhi,
            leptonPt,
            leptonPhi,
            iU1,
            iU2,
            iFluc_,
            iScale_,
            njet);

            correctedMET.SetPt(met);
            correctedMET.SetEta(0.0);
            correctedMET.SetPhi(metphi);
            correctedMET.SetM(0.0);
            NSVcorrectedMET.SetXYZ(correctedMET.x(),correctedMET.y(),correctedMET.z());

            //////////////////////
            // print out the corrected value
            cout<<" Post Correction : "<<met<<" "<<metphi<<endl;
          }


        }

        ////////////////
        double Mt = TupleHelpers::GetTransverseMass(muon.p4(), NSVcorrectedMET);
        CurrentMuonTau.set_TransverseMass(Mt);

        cout<<" transverse mass  = "<<Mt<<endl;
        ////////////////

        TMatrixD covMET(2, 2); // PFMET significance matrix
        std::vector<NSVfitStandalone::MeasuredTauLepton> measuredTauLeptons;

        ///////
        // it seems the order matters
        // pass the higher pt lepton 1st

        if( muon.p4().pt() >=  tau.p4().pt()  )
        //      if( muon.p4().pt() >=  tau.corrected_p4().pt()  )
        {
          measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kLepDecay,
          muon.p4()) );
          measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kHadDecay,
          tau.p4()));
          //        tau.corrected_p4()));
        }

        else
        {
          measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kHadDecay,
          tau.p4()));
          //        tau.corrected_p4()));
          measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kLepDecay,
          muon.p4()) );


        }

        // store the met
        CurrentMuonTau.set_mvaMET(correctedMET.pt());
        CurrentMuonTau.set_mvaMETphi(correctedMET.phi());

        covMET = mvaMETpf.getSignificanceMatrix();


        if(doSVFit_)
        {
          // last argument is verbosity
          NSVfitStandaloneAlgorithm algo(measuredTauLeptons, NSVcorrectedMET, covMET, 0);
          algo.addLogM(false);
          algo.integrateMarkovChain();

          //algo.integrateVEGAS(); ////Use this instead for VEGAS integration

          CurrentMuonTau.set_correctedSVFitMass(algo.getMass());

          //cout<<" diTauMassErr "<<algo.getMassUncert();
          //cout<<" diTauPt "<<algo.getPt();
          //cout<<" diTauPtErr "<<algo.getPtUncert();
        }
        else CurrentMuonTau.set_correctedSVFitMass(0.0);
        measuredTauLeptons.clear();

        ////////////
        // store the MuonTau

        TupleMuonTaus->push_back(CurrentMuonTau);

    } //temp

    }

  }

  iEvent.put( TupleMuonTaus, NAME_ );


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
