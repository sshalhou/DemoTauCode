// -*- C++ -*-
//
// Package:    TupleMuonTauWeightProducer
// Class:      TupleMuonTauWeightProducer
//
/**\class TupleMuonTauWeightProducer TupleMuonTauWeightProducer.cc TempDirect/TupleMuonTauWeightProducer/src/TupleMuonTauWeightProducer.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  Garrett Funk
//         Created:  Fri Jul 25 15:04:29 CDT 2014
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

//required for event weight producer

#include <vector>
#include <iostream>
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/PatCandidates/interface/Conversion.h"
#include "DataFormats/PatCandidates/interface/Lepton.h"
#include "UserCode/TupleObjects/interface/TupleTau.h"
#include "UserCode/TupleObjects/interface/TupleMuon.h"
#include "UserCode/TupleObjects/interface/TupleMuonTau.h"
#include "UserCode/TupleObjects/interface/TupleMuonTauWeight.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "Math/GenVector/VectorUtil.h"
#include "DataFormats/PatCandidates/interface/PFParticle.h"
#include "UserCode/TupleHelpers/interface/TupleHelpers.hh"
#include "PhysicsTools/PatUtils/interface/TriggerHelper.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "TF1.h"
#include "TH1.h"
#include "TMath.h"
#include "UserCode/TupleObjects/interface/TupleUserSpecifiedData.h"


typedef math::XYZTLorentzVector LorentzVector;

//
// class declaration
//

class TupleMuonTauWeightProducer : public edm::EDProducer
{
public:
  explicit TupleMuonTauWeightProducer(const edm::ParameterSet&);
  ~TupleMuonTauWeightProducer();
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
  edm::InputTag pileupSrc_;
  edm::InputTag muontauSrc_;
  edm::InputTag muonSrc_;
  edm::InputTag tauSrc_;
  edm::InputTag userDataSrc_;
  edm::InputTag TauSpinnerWTisValidSrc_;
  edm::InputTag TauSpinnerWTSrc_;
  edm::InputTag TauSpinnerWTFlipSrc_;
  edm::InputTag TauSpinnerWThminusSrc_;
  edm::InputTag TauSpinnerWThplusSrc_;

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

TupleMuonTauWeightProducer::TupleMuonTauWeightProducer(const edm::ParameterSet& iConfig):
NAME_(iConfig.getParameter<std::string>("NAME" )),
pileupSrc_(iConfig.getParameter<edm::InputTag>("pileupSrc")),
muontauSrc_(iConfig.getParameter<edm::InputTag>("muontauSrc")),
muonSrc_(iConfig.getParameter<edm::InputTag>("muonSrc")),
tauSrc_(iConfig.getParameter<edm::InputTag>("tauSrc")),
userDataSrc_(iConfig.getParameter<edm::InputTag>("userDataSrc")),
TauSpinnerWTisValidSrc_(iConfig.getParameter<bool>("TauSpinnerWTisValidSrc")),
TauSpinnerWTSrc_(iConfig.getParameter<double>("TauSpinnerWTSrc")),
TauSpinnerWTFlipSrc_(iConfig.getParameter<double>("TauSpinnerWTFlipSrc")),
TauSpinnerWThminusSrc_(iConfig.getParameter<double>("TauSpinnerWThminusSrc")),
TauSpinnerWThplusSrc_(iConfig.getParameter<double>("TauSpinnerWThplusSrc"))
{

  produces<std::vector<TupleMuonTauWeight>>(NAME_).setBranchAlias(NAME_);



}


TupleMuonTauWeightProducer::~TupleMuonTauWeightProducer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}

//
// member functions
//


// ------------ method called to produce the data  ------------
void
TupleMuonTauWeightProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  ////////////////
  // read in the UserSpecifiedData

  edm::Handle< TupleUserSpecifiedDataCollection > userData;
  iEvent.getByLabel(userDataSrc_, userData);

  const TupleUserSpecifiedData userData0 =   ((*userData)[0]);


  ///////////////
  // read in muonTaus

  edm::Handle< TupleMuonTauCollection > muonTaus;
  iEvent.getByLabel(muontauSrc_, muonTaus);


  //////////////////
  // read in the muons


  edm::Handle< TupleMuonCollection > muons;
  iEvent.getByLabel(muonSrc_, muons);

  //////////////
  // read in the taus

  edm::Handle< TupleTauCollection > taus;
  iEvent.getByLabel(tauSrc_, taus);

  ////////////////
  // reserve space for
  // the weights

  std::auto_ptr<TupleMuonTauWeightCollection> TupleMuonTauWeights (new TupleMuonTauWeightCollection);

  const int TupleMuonTauWeightsSize = muonTaus->size();
  TupleMuonTauWeights->reserve( TupleMuonTauWeightsSize );



  ////////////////
  // read in pileUpInfo

  edm::Handle<std::vector<PileupSummaryInfo> > PupInfo;
  iEvent.getByLabel(pileupSrc_, PupInfo);

  //////////////////////
  // Since the pileup weight is the same
  // for all pairs compute outside of the loop
  // over pairs

  double puWeight = 1.0;
  double puWeightM1 = 1.0;
  double puWeightP1 = 1.0;
  float NumPileupInt = 1.0;
  float NumTruePileUpInt = 1.0;
  float NumPileupIntM1 = 1.0;
  float NumTruePileUpIntM1 = 1.0;
  float NumPileupIntP1 = 1.0;
  float NumTruePileUpIntP1 = 1.0;

  TupleHelpers::getPileUpWeight(PupInfo, iEvent.isRealData(), puWeight, puWeightM1, puWeightP1,
  NumPileupInt, NumTruePileUpInt, NumPileupIntM1, NumTruePileUpIntM1, NumPileupIntP1, NumTruePileUpIntP1);

  //std::cout<<" PU "<<puWeight<<" , "<<puWeightM1<<" , "<<puWeightP1<<" , ";
  //std::cout<<NumPileupInt<<" , "<<NumTruePileUpInt<<" , "<<NumPileupIntM1<<" , "<<NumTruePileUpIntM1<<" , ";
  //std::cout<<NumPileupIntP1<<" , "<<NumTruePileUpIntP1<<std::endl;


  ////////////////////////
  // read in and set the tau
  // spinnor weights (if valid)

  edm::Handle<edm::InputTag> TauSpinnerWTisValidSrc;
  iEvent.getByLabel(TauSpinnerWTisValidSrc_, TauSpinnerWTisValidSrc);

  edm::Handle<edm::InputTag> TauSpinnerWTSrc;
  iEvent.getByLabel(TauSpinnerWTSrc_, TauSpinnerWTSrc);

  edm::Handle<edm::InputTag> TauSpinnerWTFlipSrc;
  iEvent.getByLabel(TauSpinnerWTFlipSrc_, TauSpinnerWTFlipSrc);

  edm::Handle<edm::InputTag> TauSpinnerWThminusSrc;
  iEvent.getByLabel(TauSpinnerWThminusSrc_, TauSpinnerWThminusSrc);

  edm::Handle<edm::InputTag> TauSpinnerWThplusSrc;
  iEvent.getByLabel(TauSpinnerWThplusSrc_, TauSpinnerWThplusSrc);

  // init weights to 1.0

  double TauSpinnerWT = 1.0;
  double TauSpinnerWTFlip = 1.0;
  double TauSpinnerWThminus = 1.0;
  double TauSpinnerWThplus = 1.0;

  if(TauSpinnerWTisValidSrc.isValid())
  {
    if(TauSpinnerWTisValidSrc)
    {
      /////////////
      // change if valid values
      // will store in the pair loop
      // below

      TauSpinnerWT = TauSpinnerWTSrc;
      TauSpinnerWTFlip = TauSpinnerWTFlipSrc;
      TauSpinnerWThminus = TauSpinnerWThminusSrc;
      TauSpinnerWThplus = TauSpinnerWThplusSrc;
    }
  }




  //////////////////
  // begin loop over muonTaus

  for (std::size_t i = 0; i < muonTaus->size(); ++i)
  {

    const TupleMuonTau muonTau =   ((*muonTaus)[i]);
    TupleMuonTauWeight CurrentMuonTauWeight;

    const TupleMuon muon = ((*muons)[muonTau.muonIndex()]);
    const TupleTau tau = ((*taus)[muonTau.tauIndex()]);

    ////////////////
    // set the tau spinnor weights

    CurrentMuonTauWeight.set_TauSpinnerWT(TauSpinnerWT);
    CurrentMuonTauWeight.set_TauSpinnerWTFlip(TauSpinnerWTFlip);
    CurrentMuonTauWeight.set_TauSpinnerWThminus(TauSpinnerWThminus);
    CurrentMuonTauWeight.set_TauSpinnerWThplus(TauSpinnerWThplus);


    //////////
    // set pile-up related info

    CurrentMuonTauWeight.set_puWeight(puWeight);
    CurrentMuonTauWeight.set_puWeightM1(puWeightM1);
    CurrentMuonTauWeight.set_puWeightP1(puWeightP1);
    CurrentMuonTauWeight.set_NumPileupInt(NumPileupInt);
    CurrentMuonTauWeight.set_NumTruePileUpInt(NumTruePileUpInt);
    CurrentMuonTauWeight.set_NumPileupIntM1(NumPileupIntM1);
    CurrentMuonTauWeight.set_NumTruePileUpIntM1(NumTruePileUpIntM1);
    CurrentMuonTauWeight.set_NumPileupIntP1(NumPileupIntP1);
    CurrentMuonTauWeight.set_NumTruePileUpIntP1(NumTruePileUpIntP1);


    ////////////////
    // get the muon trigger weights
    double EffDataISOMU17andISOMU18 = 1.0;
    double EffMcISOMU17andISOMU18 = 1.0;


    TupleHelpers::getTriggerWeightsISOMU17andISOMU18(iEvent.isRealData(),
    EffDataISOMU17andISOMU18, EffMcISOMU17andISOMU18, muon, userData0);

    CurrentMuonTauWeight.set_EffDataISOMU17andISOMU18(EffDataISOMU17andISOMU18);
    CurrentMuonTauWeight.set_EffMcISOMU17andISOMU18(EffMcISOMU17andISOMU18);

    //////////////////
    // get the decay mode correction
    // factor, used for Z->tau tau + signal

    double DecayModeCorrectionFactor = TupleHelpers::getDecayModeCorrectionFactor(tau);
    CurrentMuonTauWeight.set_DecayModeCorrectionFactor(DecayModeCorrectionFactor);



    //////////////////
    // get the W+jets jet to tau fake correction

    double TauFakeCorrection = TupleHelpers::getTauFakeCorrection(tau.corrected_p4().pt());
    CurrentMuonTauWeight.set_TauFakeCorrection(TauFakeCorrection);

    ///////////////////
    // get the tau high Pt bug fix weights

    double EffDataHighPtTauTrigger = 1.0;
    double EffMcHighPtTauTrigger = 1.0;

    TupleHelpers::getHighPtHadronicTauTriggerWeights(tau, EffDataHighPtTauTrigger,EffMcHighPtTauTrigger);

    CurrentMuonTauWeight.set_EffDataHighPtTauTrigger(EffDataHighPtTauTrigger);
    CurrentMuonTauWeight.set_EffMcHighPtTauTrigger(EffMcHighPtTauTrigger);

    //////////////////
    // get the tau trigger weights for muTau

    double HadronicTauDataTrigEffAntiMuMed = 1.0;
    double HadronicTauMcTrigEffAntiMuMed = 1.0;

    TupleHelpers::getTriggerWeightsHadTauMUTAU(iEvent.isRealData(),
    HadronicTauDataTrigEffAntiMuMed, HadronicTauMcTrigEffAntiMuMed,
    tau, userData0);

    CurrentMuonTauWeight.set_HadronicTauDataTrigEffAntiMuMed(HadronicTauDataTrigEffAntiMuMed);
    CurrentMuonTauWeight.set_HadronicTauMcTrigEffAntiMuMed(HadronicTauMcTrigEffAntiMuMed);

    /////////////
    // get the muon ID and ISOL weights

    double muonDataIDweight = 1.0;
    double muonMcIDweight = 1.0;
    double muonDataISOLweight = 1.0;
    double muonMcISOLweight = 1.0;

    TupleHelpers::muonIDSF(iEvent.isRealData(), muon,
    userData0, muonDataIDweight, muonMcIDweight );

    TupleHelpers::muonISOLSF(iEvent.isRealData(), muon,
    userData0, muonDataISOLweight, muonMcISOLweight );

    CurrentMuonTauWeight.set_muonDataIDweight(muonDataIDweight);
    CurrentMuonTauWeight.set_muonMcIDweight(muonMcIDweight);
    CurrentMuonTauWeight.set_muonDataISOLweight(muonDataISOLweight);
    CurrentMuonTauWeight.set_muonMcISOLweight(muonMcISOLweight);


    //////////////
    // get the higgs pt reweight
    // for SUSY samples

    double nominalHIGLUXHQTmhmax = 1.0;
    double upHIGLUXHQTmhmax = 1.0;
    double downHIGLUXHQTmhmax = 1.0;
    double nominalPOWHEGmhmod = 1.0;
    double upPOWHEGmhmod = 1.0;
    double downPOWHEGmhmod = 1.0;

    TupleHelpers::getHiggsPtWeights(userData0, muonTau.genBosonP4(),
    nominalHIGLUXHQTmhmax,
    upHIGLUXHQTmhmax,
    downHIGLUXHQTmhmax,
    nominalPOWHEGmhmod,
    upPOWHEGmhmod,
    downPOWHEGmhmod);

    CurrentMuonTauWeight.set_nominalHIGLUXHQTmhmax(nominalHIGLUXHQTmhmax);
    CurrentMuonTauWeight.set_upHIGLUXHQTmhmax(upHIGLUXHQTmhmax);
    CurrentMuonTauWeight.set_downHIGLUXHQTmhmax(downHIGLUXHQTmhmax);
    CurrentMuonTauWeight.set_nominalPOWHEGmhmod(nominalPOWHEGmhmod);
    CurrentMuonTauWeight.set_upPOWHEGmhmod(upPOWHEGmhmod);
    CurrentMuonTauWeight.set_downPOWHEGmhmod(downPOWHEGmhmod);


    ////////////////
    // QCD template
    // reweights

    double etaDepQCDShapeTemplateCorrection = 1.0;
    double inclusiveQCDShapeTemplateCorrection = 1.0;

    TupleHelpers::getQCDShapeTemplateCorrections(etaDepQCDShapeTemplateCorrection,
    inclusiveQCDShapeTemplateCorrection, tau);

    CurrentMuonTauWeight.set_etaDepQCDShapeTemplateCorrection(etaDepQCDShapeTemplateCorrection);
    CurrentMuonTauWeight.set_inclusiveQCDShapeTemplateCorrection(inclusiveQCDShapeTemplateCorrection);


    /////////////
    // tt Pt reweight

    double TTbarPtWeight = TupleHelpers::getTTbarPtWeight(
    muonTau.genTOPp4().pt(), muonTau.genTOPBARp4().pt());

    CurrentMuonTauWeight.set_TTbarPtWeight(TTbarPtWeight);

    /////////////
    // add the current pair
    // to the collection



    TupleMuonTauWeights->push_back(CurrentMuonTauWeight);



  }



  iEvent.put( TupleMuonTauWeights, NAME_ );

}

// ------------ method called once each job just before starting event loop  ------------
void
TupleMuonTauWeightProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TupleMuonTauWeightProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
TupleMuonTauWeightProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TupleMuonTauWeightProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TupleMuonTauWeightProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TupleMuonTauWeightProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleMuonTauWeightProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleMuonTauWeightProducer);
