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

#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETCollection.h"
#include "UserCode/RecoilCorrector/interface/RecoilCorrector.hh"
#include "UserCode/GenBosonDecayFinder/interface/GenBosonDecayFinder.hh"



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
  double PAR1_;
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
TupleMuonTauProducer::TupleMuonTauProducer(const edm::ParameterSet& iConfig):
tauSrc_(iConfig.getParameter<edm::InputTag>("tauSrc" )),
muonSrc_(iConfig.getParameter<edm::InputTag>("muonSrc" )),
mvametSrc_(iConfig.getParameter<edm::InputTag>("mvametSrc" )),
genSrc_(iConfig.getParameter<edm::InputTag>("genSrc" )),
PAR1_(iConfig.getParameter<double>("PAR1" )),
NAME_(iConfig.getParameter<string>("NAME" ))
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



  // get tuple muon and tau collections


  edm::Handle< TupleMuonCollection > muons;
  iEvent.getByLabel(muonSrc_, muons);

  edm::Handle< TupleTauCollection > taus;
  iEvent.getByLabel(tauSrc_, taus);

  // get the mva met

  edm::Handle<std::vector<reco::PFMET> > mvamet;
  iEvent.getByLabel(mvametSrc_, mvamet);

  edm::Handle<std::vector<reco::GenParticle> > gen;
  iEvent.getByLabel(genSrc_, gen);


  cout<<" PAR1_ "<<PAR1_<<endl;
  cout<<" NAME_ "<<NAME_<<endl;

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
      // apply Phil's recoil
      // corrections to the MET before
      // running SVFit to MC only

      if( !iEvent.isRealData() )
      {
        double met=(*mvamet)[0].pt();
        double metphi=(*mvamet)[0].phi();
        double leptonPt = ( ((*muons)[i]).p4() + ((*taus)[j]).corrected_p4()   ).pt();
        double leptonPhi  = ( ((*muons)[i]).p4() + ((*taus)[j]).corrected_p4()   ).phi();
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
        bool ApplyRecoilCorrection = 0;

        // these need to become argumenst to the producer
        double iFluc  = 0.0;
        double iScale = 0.0;
        int njet = 3;

        GenBosonDecayFinder genDecayFinder;
        genDecayFinder.findBosonAndDaugters(*gen,BosonPdgId,BosonP4,DaughterOnePdgId,
        DaughterOneP4,DaughterTwoPdgId,
        DaughterTwoP4,ApplyRecoilCorrection);

        cout<<BosonPdgId<<" = BosonPdgId "<<endl;
        cout<<DaughterOnePdgId<<" = DaughterOnePdgId "<<endl;
        cout<<DaughterTwoPdgId<<" = DaughterTwoPdgId "<<endl;
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
          iFluc,
          iScale,
          njet);


          //////////////////////
          // print out the corrected value
          cout<<" Post Correction : "<<met<<" "<<metphi<<endl;


        }


      }

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
