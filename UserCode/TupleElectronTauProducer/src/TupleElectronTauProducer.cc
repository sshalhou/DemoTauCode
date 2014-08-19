// -*- C++ -*-
//
// Package:    TupleElectronTauProducer
// Class:      TupleElectronTauProducer
//
/**\class TupleElectronTauProducer TupleElectronTauProducer.cc TEMP/TupleElectronTauProducer/src/TupleElectronTauProducer.cc

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
#include "UserCode/TupleObjects/interface/TupleElectron.h"
#include "UserCode/TupleObjects/interface/TupleElectronTau.h"
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
#include "UserCode/TupleHelpers/interface/BtagSF.hh"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/PileupJetIdentifier.h"
#include "DataFormats/Math/interface/deltaR.h"


//#include "PhysicsTools/SelectorUtils/interface/EventSelector.h"
//#include "PhysicsTools/SelectorUtils/interface/JetIDSelectionFunctor.h"
//#include "PhysicsTools/SelectorUtils/interface/PFJetIDSelectionFunctor.h"







typedef math::XYZTLorentzVector LorentzVector;
typedef std::vector<edm::InputTag> vInputTag;
using namespace std;
using namespace edm;


//
// class declaration
//

class TupleElectronTauProducer : public edm::EDProducer {
public:
  explicit TupleElectronTauProducer(const edm::ParameterSet&);
  ~TupleElectronTauProducer();

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
  edm::InputTag electronSrc_;
  vInputTag mvametSrc_;
  edm::InputTag genSrc_;
  edm::InputTag jetSrc_;
  double iFluc_;
  double iScale_;
  string NAME_;
  edm::InputTag puJetIdMVASrc_;
  edm::InputTag puJetIdFlagSrc_;
  bool doSVFit_;
  unsigned int maxElectrons_;
  unsigned int maxTaus_;
  bool doNotRequireFullIdForLeptons_;
  edm::InputTag muonSrc_;



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
TupleElectronTauProducer::TupleElectronTauProducer(const edm::ParameterSet& iConfig):
tauSrc_(iConfig.getParameter<edm::InputTag>("tauSrc" )),
electronSrc_(iConfig.getParameter<edm::InputTag>("electronSrc" )),
mvametSrc_(iConfig.getParameter<vInputTag>("mvametSrc" )),
genSrc_(iConfig.getParameter<edm::InputTag>("genSrc" )),
jetSrc_(iConfig.getParameter<edm::InputTag>("jetSrc" )),
iFluc_(iConfig.getParameter<double>("iFluc" )),
iScale_(iConfig.getParameter<double>("iScale" )),
NAME_(iConfig.getParameter<string>("NAME" )),
puJetIdMVASrc_(iConfig.getParameter<edm::InputTag>("puJetIdMVASrc" )),
puJetIdFlagSrc_(iConfig.getParameter<edm::InputTag>("puJetIdFlagSrc" )),
doSVFit_(iConfig.getParameter<bool>("doSVFit" )),
maxElectrons_(iConfig.getParameter<unsigned int>("maxElectrons" )),
maxTaus_(iConfig.getParameter<unsigned int>("maxTaus" )),
doNotRequireFullIdForLeptons_(iConfig.getParameter<bool>("doNotRequireFullIdForLeptons" )),
muonSrc_(iConfig.getParameter<edm::InputTag>("muonSrc" ))
{





  produces< vector<TupleElectronTau> >(NAME_).setBranchAlias(NAME_);


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


TupleElectronTauProducer::~TupleElectronTauProducer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TupleElectronTauProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{


  // get the muons for tri-lepton veto
  edm::Handle< TupleMuonCollection > muons;
  iEvent.getByLabel(muonSrc_, muons);



  // get tuple electron and tau and jet collections


  edm::Handle< TupleElectronCollection > electrons;
  iEvent.getByLabel(electronSrc_, electrons);




  edm::Handle< TupleTauCollection > taus;
  iEvent.getByLabel(tauSrc_, taus);

  edm::Handle<edm::View<pat::Jet> > jets;
  iEvent.getByLabel(jetSrc_,jets);




  ////////////////////////////////
  // get a list of jet indices that filters
  // those that overlap other jets

  vector <unsigned int> goodIndices;
  TupleHelpers::getNonOverlappingJetIndices(jets,goodIndices,0.01);



  ///////////////////////////////////////
  // figure out how many of these jets
  // pass the loose WP



  edm::Handle<ValueMap<float> > puJetIdMVA;
  //iEvent.getByLabel("puJetMva","full53xDiscriminant",puJetIdMVA);
  iEvent.getByLabel(puJetIdMVASrc_,puJetIdMVA);


  edm::Handle<ValueMap<int> > puJetIdFlag;
  //iEvent.getByLabel("puJetMva","full53xId",puJetIdFlag);
  iEvent.getByLabel(puJetIdFlagSrc_,puJetIdFlag);


  ///////////////////////////////////
  //  set up the PF jet ID (loose)
//  PFJetIDSelectionFunctor pfjetIDLoose( PFJetIDSelectionFunctor::FIRSTDATA, PFJetIDSelectionFunctor::LOOSE );
  //pat::strbitset retpf = pfjetIDLoose.getBitTemplate();



  // get the gen particles

  edm::Handle<std::vector<reco::GenParticle> > gen;
  iEvent.getByLabel(genSrc_, gen);





  ////////////

  auto_ptr<TupleElectronTauCollection> TupleElectronTaus (new TupleElectronTauCollection);

  const int TupleElectronTauSize = electrons->size();
  TupleElectronTaus->reserve( TupleElectronTauSize );




  ///////////////
  // init btag scale factor tool

  BtagSF btagSFtool(0);

  ///////////////////
  // find max pt pair

  std::size_t max_i = -999;
  std::size_t max_j = -999;
  int max_pt = -999;

  for (std::size_t i = 0; i < electrons->size(); ++i)
  {

    const TupleElectron electron =   ((*electrons)[i]);

    for (std::size_t j = 0; j < taus->size(); ++j)
    {

      const TupleTau tau =   ((*taus)[j]);

      if((tau.passFullId_muTau() && electron.passFullId()) || doNotRequireFullIdForLeptons_)
      {

        if(tau.p4().pt()+electron.p4().pt() >= max_pt)
        {


          if(tau.p4().pt()==tau.p4().pt() && electron.p4().pt()==electron.p4().pt())
          {
            max_pt = (tau.p4().pt()+electron.p4().pt());
            max_i = i;
            max_j = j;
          }

        }

      }
    }
  }

  ///////////////////////////////////////
  // instead of looping over all electron+tau
  // pairs, only consider those for which
  // we have attempted to produce
  // mva met, print a warning if not all are
  // considerd

  std::size_t lastTauIndex = min(std::size_t(maxTaus_),taus->size());
  std::size_t lastElectronIndex = min(std::size_t(maxElectrons_),electrons->size());

  /////////////////////////////
  // Print the warning
  if(lastTauIndex<taus->size() || lastElectronIndex<electrons->size())
  {

    std::cout<<" --------------- \n";
    std::cout<<" WARNING : \n";
    std::cout<<" WARNING considering "<<lastTauIndex<<" of "<<taus->size()<<" taus \n";
    std::cout<<" WARNING considering "<<lastElectronIndex<<" of "<<electrons->size()<<" electrons \n";
    std::cout<<" --------------- \n";

  }

  for (std::size_t i = 0; i < lastElectronIndex; ++i)
  {

    const TupleElectron electron =   ((*electrons)[i]);

    for (std::size_t j = 0; j < lastTauIndex; ++j)
    {

      const TupleTau tau =   ((*taus)[j]);


      // get the mva met corrected for electron i and tau j

      unsigned int n = (i*maxTaus_)+j;



      edm::Handle <std::vector<reco::PFMET> >  mvamet;
      iEvent.getByLabel(mvametSrc_[n], mvamet);
      const reco::PFMET mvaMETpf =  (*mvamet)[0];


      //reco::PFMET mvaMETpf  = mvaMETpfVec[n];

      // declare & init to raw value before applying recoil corrections
      NSVfitStandalone::Vector NSVcorrectedMET = mvaMETpf.momentum();
      math::PtEtaPhiMLorentzVector correctedMET(mvaMETpf.pt(),0.0,mvaMETpf.phi(),0.0);

      // store raw value without applying recoil corrections for use with
      // raw versions of SVFit and Transverse mass
      NSVfitStandalone::Vector NSVrawMET = mvaMETpf.momentum();
      math::PtEtaPhiMLorentzVector rawMET(mvaMETpf.pt(),0.0,mvaMETpf.phi(),0.0);

      if((tau.passFullId_muTau() && electron.passFullId()) || doNotRequireFullIdForLeptons_)
      {




        TupleElectronTau CurrentElectronTau;

        if(max_i == i && max_j == j) CurrentElectronTau.set_MAX(1);
        else CurrentElectronTau.set_MAX(0);




        //////////////////
        // check triggers

        if(electron.has_HltMatchEle20()==1 && tau.has_HltMatchEle20()==1)
        {
          CurrentElectronTau.set_isGoodTriggerPair(1);
        }
        else if(electron.has_HltMatchEle22()==1 && tau.has_HltMatchEle22()==1)
        {
          CurrentElectronTau.set_isGoodTriggerPair(1);
        }
        //        else if(electron.has_HltMatchEle27()==1 && tau.has_HltMatchEle27()==1)
        //      {
        //      CurrentElectronTau.set_isGoodTriggerPair(1);
        //  }


        CurrentElectronTau.set_p4(  electron.p4() + tau.p4() );
        CurrentElectronTau.set_electronIndex(i);
        CurrentElectronTau.set_tauIndex(j);
        CurrentElectronTau.set_mvaMETraw(mvaMETpf.pt());
        CurrentElectronTau.set_mvaMETphiRaw(mvaMETpf.phi());
        CurrentElectronTau.set_corrected_p4( electron.p4() + tau.corrected_p4()   );
        CurrentElectronTau.set_scalarSumPt(electron.p4() , tau.corrected_p4()  );
        CurrentElectronTau.set_DR(electron.p4() , tau.corrected_p4()  );
        CurrentElectronTau.set_sumCharge(electron.charge() , tau.charge()  );


        /////////////////
        // check triLepton Veto

        bool passVeto = TupleHelpers::pairPassesTriLeptonVeto(i, 9999, electrons, muons);
        CurrentElectronTau.set_passesTriLeptonVeto(passVeto);


        ////////////
        // apply Phil's recoil
        // corrections to the MET before
        // running SVFit to MC only

        if( !iEvent.isRealData() )
        {
          double met=mvaMETpf.pt();
          double metphi=mvaMETpf.phi();
          //        double leptonPt = ( electron.p4() + tau.corrected_p4()   ).pt();
          //        double leptonPhi  = ( electron.p4() + tau.corrected_p4()   ).phi();

          double leptonPt = ( electron.p4() + tau.corrected_p4()   ).pt();
          double leptonPhi  = ( electron.p4() + tau.corrected_p4()   ).phi();

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




          if(ApplyRecoilCorrection)
          {

            //GenZPt = (DaughterOneP4+DaughterTwoP4).pt();
            //GenZPhi = (DaughterOneP4+DaughterTwoP4).phi();
            GenZPt = BosonP4.pt();
            GenZPhi = BosonP4.phi();


            std::string DataFile;
            std::string MCFile;
            std::string ProcessFile;



            whichRecoilCorrectionFiles(BosonPdgId, DaughterOnePdgId,
            DaughterTwoPdgId, 100, ProcessFile, DataFile, MCFile);






            RecoilCorrector corrector(ProcessFile);
            corrector.addMCFile(MCFile);
            corrector.addDataFile(DataFile);




            /////////////////
            int number_of_passingJets_ForRecoil = 0;

            ///////////////////////
            // determine gen - reco overlap
            // for leptons





            for ( unsigned int ii = 0; ii<goodIndices.size(); ++ii)
            {

              unsigned int i = goodIndices[ii];

              const pat::Jet & patjet = jets->at(i);
              float mva   = (*puJetIdMVA)[jets->refAt(i)];
              int    idflag = (*puJetIdFlag)[jets->refAt(i)];

              bool passes_id = 1;



              LorentzVector compareLeg1(0,0,0,0);
              LorentzVector compareLeg2(0,0,0,0);


              if( 11 == abs(DaughterOnePdgId) && (deltaR(electron.p4(), DaughterOneP4) < 0.3) ) compareLeg1 = electron.p4();
              else  compareLeg1 = DaughterOneP4;

              if( 15 == abs(DaughterOnePdgId) && (deltaR(tau.corrected_p4(), DaughterOneP4) < 0.3) ) compareLeg1 = tau.corrected_p4();
              else  compareLeg1 = DaughterOneP4;


              if( 11 == abs(DaughterTwoPdgId) && (deltaR(electron.p4(), DaughterTwoP4) < 0.3) ) compareLeg2 = electron.p4();
              else  compareLeg2 = DaughterTwoP4;

              if( 15 == abs(DaughterTwoPdgId) && (deltaR(tau.corrected_p4(), DaughterTwoP4) < 0.3) ) compareLeg2 = tau.corrected_p4();
              else  compareLeg2 = DaughterTwoP4;






              /////////////////

              if( !( fabs(patjet.eta())<4.5) ) passes_id = 0;
              //if( !(PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kLoose ))) passes_id = 0;
              if( !(deltaR(compareLeg1, patjet.p4()) > 0.3)) passes_id = 0;
              if( !(deltaR(compareLeg2, patjet.p4()) > 0.3)) passes_id = 0;
              if(passes_id == 1)
              {

                if(patjet.pt()>30)
                {
                  number_of_passingJets_ForRecoil++;

                }

              }
            }
            /////////////////




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
            TMath::Min(int(number_of_passingJets_ForRecoil),2));




            correctedMET.SetPt(met);
            correctedMET.SetEta(0.0);
            correctedMET.SetPhi(metphi);
            correctedMET.SetM(0.0);
            NSVcorrectedMET.SetXYZ(correctedMET.x(),correctedMET.y(),correctedMET.z());

          }


        }

        ////////////////
        double Mt = TupleHelpers::GetTransverseMass(electron.p4(), NSVcorrectedMET);
        CurrentElectronTau.set_TransverseMass(Mt);

        double rawMt = TupleHelpers::GetTransverseMass(electron.p4(), NSVrawMET);
        CurrentElectronTau.set_rawTransverseMass(rawMt);


        ////////////////

        TMatrixD covMET(2, 2); // PFMET significance matrix
        std::vector<NSVfitStandalone::MeasuredTauLepton> measuredTauLeptons;

        ///////
        // it seems the order matters
        // pass the higher pt lepton 1st


        //if( electron.p4().pt() >=  tau.corrected_p4().pt()  )
        //{
        measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kLepDecay,
        electron.p4()) );
        measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kHadDecay,
        tau.corrected_p4()));
        //}

        //else
        //{
        //measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kHadDecay,
        //tau.corrected_p4()));
        //measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kLepDecay,
        //electron.p4()) );


        //}

        // store the met
        CurrentElectronTau.set_mvaMET(correctedMET.pt());
        CurrentElectronTau.set_mvaMETphi(correctedMET.phi());

        covMET = mvaMETpf.getSignificanceMatrix();
        CurrentElectronTau.set_cov00(mvaMETpf.getSignificanceMatrix()(0,0));
        CurrentElectronTau.set_cov01(mvaMETpf.getSignificanceMatrix()(0,1));
        CurrentElectronTau.set_cov10(mvaMETpf.getSignificanceMatrix()(1,0));
        CurrentElectronTau.set_cov11(mvaMETpf.getSignificanceMatrix()(1,1));


        if(doSVFit_)
        {
          // last argument is verbosity
          NSVfitStandaloneAlgorithm algo(measuredTauLeptons, NSVcorrectedMET, covMET, 1);
          algo.addLogM(false);
          //algo.integrateMarkovChain();

          algo.integrateVEGAS(); ////Use this instead for VEGAS integration

          CurrentElectronTau.set_correctedSVFitMass(algo.getMass());


          // calculate SVFit mass without recoil met corr.
          NSVfitStandaloneAlgorithm algoRaw(measuredTauLeptons, NSVrawMET, covMET, 0);
          algoRaw.addLogM(false);
          //algoRaw.integrateMarkovChain();
          algoRaw.integrateVEGAS();
          CurrentElectronTau.set_rawSVFitMass(algoRaw.getMass());




        }
        else CurrentElectronTau.set_correctedSVFitMass(0.0);
        measuredTauLeptons.clear();



        ////////////////////////////////
        // store jet related variables
        // the jet ID we are using here is
        // Et > 30, | eta | < 4.7, DR(jet,lep) > 0.5
        // DR(jet,tau)>0.5, passes PF jet ID

        int jet1_index = -999;
        double jet1_pt = -999.;
        int jet2_index = -999;
        double jet2_pt = -999.;

        int number_of_passingJets = 0;
        int number_of_btagged_passingJets = 0;

        for ( unsigned int ii = 0; ii<goodIndices.size(); ++ii)
        //for ( unsigned int i=0; i<jets->size(); ++i )
        {
          unsigned int i = goodIndices[ii];
          const pat::Jet & patjet = jets->at(i);
          float mva   = (*puJetIdMVA)[jets->refAt(i)];
          int    idflag = (*puJetIdFlag)[jets->refAt(i)];

          bool passes_id = 1;

//          retpf.set(false);
//          if( !pfjetIDLoose( *patjet, retpf ) ) passes_id = 0;
          if( !(patjet.pt()>20) ) passes_id = 0;
          if( !( fabs(patjet.eta())<4.7) ) passes_id = 0;
          if( !(PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kLoose ))) passes_id = 0;
          if( !(deltaR(electron.p4(), patjet.p4()) > 0.3)) passes_id = 0;
          if( !(deltaR(tau.pfJetRefP4(), patjet.p4()) > 0.3)) passes_id = 0;
          if(passes_id == 1)
          {

            if(patjet.pt()>30)
            {
              number_of_passingJets++;

            }
            /////////////
            // figure out the 1st and 2nd ranked jets
            // by pt

            if(patjet.pt() > jet1_pt)
            {
              jet1_pt =   patjet.pt();
              jet1_index  = i;
            }

            else if(patjet.pt() > jet2_pt)
            {

              jet2_pt =   patjet.pt();
              jet2_index  = i;

            }


            bool isbtagged = btagSFtool.isbtagged(
            patjet.pt(), patjet.eta(),
            patjet.bDiscriminator("combinedSecondaryVertexBJetTags"),
            patjet.partonFlavour(),
            iEvent.isRealData(),
            0,0,1);




            if(fabs(patjet.eta())<2.4 && isbtagged)
            {
              number_of_btagged_passingJets++;
            }


          }



        }



        /////////////////////
        // store the jet related quantities


        CurrentElectronTau.set_njets(number_of_passingJets);
        CurrentElectronTau.set_nbjets(number_of_btagged_passingJets);



        if(jet1_index!=-999)
        //if(jets->size()>0)
        {

          //jet1_index = 0;

          const pat::Jet & patjet = jets->at(jet1_index);
          float mva   = (*puJetIdMVA)[jets->refAt(jet1_index)];
          int    idflag = (*puJetIdFlag)[jets->refAt(jet1_index)];


          CurrentElectronTau.set_jet1P4(patjet.p4());
          CurrentElectronTau.set_jet1RawP4(patjet.p4());
          CurrentElectronTau.set_jet1IDMVA(mva);
          CurrentElectronTau.set_jet1BTAGMVA(patjet.bDiscriminator("combinedSecondaryVertexBJetTags"));


        }

        if(jet2_index!=-999)
        //if(jets->size()>1)
        {

          //jet2_index = 1;
          const pat::Jet & patjet = jets->at(jet2_index);
          float mva   = (*puJetIdMVA)[jets->refAt(jet2_index)];
          int    idflag = (*puJetIdFlag)[jets->refAt(jet2_index)];


          CurrentElectronTau.set_jet2P4(patjet.p4());
          CurrentElectronTau.set_jet2RawP4(patjet.p4());
          CurrentElectronTau.set_jet2IDMVA(mva);
          CurrentElectronTau.set_jet2BTAGMVA(patjet.bDiscriminator("combinedSecondaryVertexBJetTags"));


        }




        ////////////
        // store the ElectronTau

        TupleElectronTaus->push_back(CurrentElectronTau);

      }

    }

  }

  iEvent.put( TupleElectronTaus, NAME_ );


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
TupleElectronTauProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TupleElectronTauProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
TupleElectronTauProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TupleElectronTauProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TupleElectronTauProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TupleElectronTauProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleElectronTauProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleElectronTauProducer);
