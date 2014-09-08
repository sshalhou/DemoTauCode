// -*- C++ -*-
//
// Package:    TupleElectronTauWeightProducer
// Class:      TupleElectronTauWeightProducer
//
/**\class TupleElectronTauWeightProducer TupleElectronTauWeightProducer.cc TempDirect/TupleElectronTauWeightProducer/src/TupleElectronTauWeightProducer.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  Garrett Funk
//         Created:  Thu Jul 24 14:46:00 CDT 2014
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
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "EgammaAnalysis/ElectronTools/interface/EGammaCutBasedEleId.h"
#include "DataFormats/PatCandidates/interface/Conversion.h"
#include "DataFormats/PatCandidates/interface/Lepton.h"
#include "UserCode/TupleObjects/interface/TupleTau.h"
#include "UserCode/TupleObjects/interface/TupleElectron.h"
#include "UserCode/TupleObjects/interface/TupleElectronTau.h"
#include "UserCode/TupleObjects/interface/TupleElectronTauWeight.h"
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
#include "TauSpinnerInterface/TauSpinnerInterface/interface/TauSpinnerCMS.h"

typedef math::XYZTLorentzVector LorentzVector;


//
// class declaration
//

class TupleElectronTauWeightProducer : public edm::EDProducer
{
public:
  explicit TupleElectronTauWeightProducer(const edm::ParameterSet&);
  ~TupleElectronTauWeightProducer();
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
  edm::InputTag electrontauSrc_;
  edm::InputTag electronSrc_;
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

TupleElectronTauWeightProducer::TupleElectronTauWeightProducer(const edm::ParameterSet& iConfig):
NAME_(iConfig.getParameter<std::string>("NAME" )),
pileupSrc_(iConfig.getParameter<edm::InputTag>("pileupSrc")),
electrontauSrc_(iConfig.getParameter<edm::InputTag>("electrontauSrc")),
electronSrc_(iConfig.getParameter<edm::InputTag>("electronSrc")),
tauSrc_(iConfig.getParameter<edm::InputTag>("tauSrc")),
userDataSrc_(iConfig.getParameter<edm::InputTag>("userDataSrc")),
TauSpinnerWTisValidSrc_(iConfig.getParameter<edm::InputTag>("TauSpinnerWTisValidSrc")),
TauSpinnerWTSrc_(iConfig.getParameter<edm::InputTag>("TauSpinnerWTSrc")),
TauSpinnerWTFlipSrc_(iConfig.getParameter<edm::InputTag>("TauSpinnerWTFlipSrc")),
TauSpinnerWThminusSrc_(iConfig.getParameter<edm::InputTag>("TauSpinnerWThminusSrc")),
TauSpinnerWThplusSrc_(iConfig.getParameter<edm::InputTag>("TauSpinnerWThplusSrc"))
{



  produces<std::vector<TupleElectronTauWeight>>(NAME_).setBranchAlias(NAME_);


}


TupleElectronTauWeightProducer::~TupleElectronTauWeightProducer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}

//
// member functions
//


// ------------ method called to produce the data  ------------
void
TupleElectronTauWeightProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{


  ////////////////
  // read in the UserSpecifiedData

  edm::Handle< TupleUserSpecifiedDataCollection > userData;
  iEvent.getByLabel(userDataSrc_, userData);

  const TupleUserSpecifiedData userData0 =   ((*userData)[0]);



  ///////////////
  // read in electronTaus

  edm::Handle< TupleElectronTauCollection > electronTaus;
  iEvent.getByLabel(electrontauSrc_, electronTaus);

  //////////////
  // read in the electrons

  edm::Handle< TupleElectronCollection > electrons;
  iEvent.getByLabel(electronSrc_, electrons);

  //////////////
  // read in the taus

  edm::Handle< TupleTauCollection > taus;
  iEvent.getByLabel(tauSrc_, taus);

  ////////////////
  // reserve space for
  // the weights

  std::auto_ptr<TupleElectronTauWeightCollection> TupleElectronTauWeights (new TupleElectronTauWeightCollection);

  const int TupleElectronTauWeightsSize = electronTaus->size();
  TupleElectronTauWeights->reserve( TupleElectronTauWeightsSize );



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

  edm::Handle<bool> TauSpinnerWTisValidSrc;
  iEvent.getByLabel(TauSpinnerWTisValidSrc_, TauSpinnerWTisValidSrc);

  edm::Handle<double> TauSpinnerWTSrc;
  iEvent.getByLabel(TauSpinnerWTSrc_, TauSpinnerWTSrc);

  edm::Handle<double> TauSpinnerWTFlipSrc;
  iEvent.getByLabel(TauSpinnerWTFlipSrc_, TauSpinnerWTFlipSrc);

  edm::Handle<double> TauSpinnerWThminusSrc;
  iEvent.getByLabel(TauSpinnerWThminusSrc_, TauSpinnerWThminusSrc);

  edm::Handle<double> TauSpinnerWThplusSrc;
  iEvent.getByLabel(TauSpinnerWThplusSrc_, TauSpinnerWThplusSrc);

  // init weights to 1.0

  double TauSpinnerWT = 1.0;
  double TauSpinnerWTFlip = 1.0;
  double TauSpinnerWThminus = 1.0;
  double TauSpinnerWThplus = 1.0;

  if(TauSpinnerWTisValidSrc.isValid())
  {

    if(*TauSpinnerWTisValidSrc)
    {
      /////////////
      // change if valid values
      // will store in the pair loop
      // below

      TauSpinnerWT = *TauSpinnerWTSrc;
      TauSpinnerWTFlip = *TauSpinnerWTFlipSrc;
      TauSpinnerWThminus = *TauSpinnerWThminusSrc;
      TauSpinnerWThplus = *TauSpinnerWThplusSrc;
    }
  }


  //////////////////
  // begin loop over electronTaus

  for (std::size_t i = 0; i < electronTaus->size(); ++i)
  {

    const TupleElectronTau electronTau =   ((*electronTaus)[i]);
    TupleElectronTauWeight CurrentElectronTauWeight;

    const TupleElectron electron = ((*electrons)[electronTau.electronIndex()]);
    const TupleTau tau = ((*taus)[electronTau.tauIndex()]);


    ////////////////
    // set the tau spinnor weights

    CurrentElectronTauWeight.set_TauSpinnerWT(TauSpinnerWT);
    CurrentElectronTauWeight.set_TauSpinnerWTFlip(TauSpinnerWTFlip);
    CurrentElectronTauWeight.set_TauSpinnerWThminus(TauSpinnerWThminus);
    CurrentElectronTauWeight.set_TauSpinnerWThplus(TauSpinnerWThplus);


    //////////
    // set pile-up related info

    CurrentElectronTauWeight.set_puWeight(puWeight);
    CurrentElectronTauWeight.set_puWeightM1(puWeightM1);
    CurrentElectronTauWeight.set_puWeightP1(puWeightP1);
    CurrentElectronTauWeight.set_NumPileupInt(NumPileupInt);
    CurrentElectronTauWeight.set_NumTruePileUpInt(NumTruePileUpInt);
    CurrentElectronTauWeight.set_NumPileupIntM1(NumPileupIntM1);
    CurrentElectronTauWeight.set_NumTruePileUpIntM1(NumTruePileUpIntM1);
    CurrentElectronTauWeight.set_NumPileupIntP1(NumPileupIntP1);
    CurrentElectronTauWeight.set_NumTruePileUpIntP1(NumTruePileUpIntP1);


    ///////////
    // get the Electron Trigger Weights
    double EffDataELE20andELE22 = 1.0;
    double EffMcELE20andELE22 = 1.0;


    TupleHelpers::getTriggerWeightsELE20andELE22(iEvent.isRealData(),
    EffDataELE20andELE22, EffMcELE20andELE22, electron, userData0);

    CurrentElectronTauWeight.set_EffDataELE20andELE22(EffDataELE20andELE22);
    CurrentElectronTauWeight.set_EffMcELE20andELE22(EffMcELE20andELE22);


    ////////////////
    // get the Zee e->tau_h fake
    // rate correction

    double ZeeScaleFactor = TupleHelpers::getZeeScaleFactor(tau);
    CurrentElectronTauWeight.set_ZeeScaleFactor(ZeeScaleFactor);

    //////////////////
    // get the decay mode correction
    // factor, used for Z->tau tau + signal

    double DecayModeCorrectionFactor = TupleHelpers::getDecayModeCorrectionFactor(tau);
    CurrentElectronTauWeight.set_DecayModeCorrectionFactor(DecayModeCorrectionFactor);




    //////////////////
    // get the W+jets jet to tau fake correction

    double TauFakeCorrection = TupleHelpers::getTauFakeCorrection(tau.corrected_p4().pt());
    CurrentElectronTauWeight.set_TauFakeCorrection(TauFakeCorrection);



    ///////////////////
    // get the tau high Pt bug fix weights

    double EffDataHighPtTauTrigger = 1.0;
    double EffMcHighPtTauTrigger = 1.0;

    TupleHelpers::getHighPtHadronicTauTriggerWeights(tau, EffDataHighPtTauTrigger,EffMcHighPtTauTrigger);

    CurrentElectronTauWeight.set_EffDataHighPtTauTrigger(EffDataHighPtTauTrigger);
    CurrentElectronTauWeight.set_EffMcHighPtTauTrigger(EffMcHighPtTauTrigger);


    //////////////
    // get the hadronic tau trigger weights

    double HadronicTauDataTrigEffAntiEMed = 1.0;
    double HadronicTauMcTrigEffAntiEMed = 1.0;
    double HadronicTauDataTrigEffAntiETight = 1.0;
    double HadronicTauMcTrigEffAntiETight = 1.0;

    TupleHelpers::getTriggerWeightsHadTauETAU(iEvent.isRealData(),
    HadronicTauDataTrigEffAntiEMed, HadronicTauMcTrigEffAntiEMed,
    HadronicTauDataTrigEffAntiETight, HadronicTauMcTrigEffAntiETight,
    tau, userData0);

    CurrentElectronTauWeight.set_HadronicTauDataTrigEffAntiEMed(HadronicTauDataTrigEffAntiEMed);
    CurrentElectronTauWeight.set_HadronicTauMcTrigEffAntiEMed(HadronicTauMcTrigEffAntiEMed);
    CurrentElectronTauWeight.set_HadronicTauDataTrigEffAntiETight(HadronicTauDataTrigEffAntiETight);
    CurrentElectronTauWeight.set_HadronicTauMcTrigEffAntiETight(HadronicTauMcTrigEffAntiETight);

    /////////////
    // get the electron ID and ISOL weights

    double electronDataIDweight = 1.0;
    double electronMcIDweight = 1.0;
    double electronDataISOLweight = 1.0;
    double electronMcISOLweight = 1.0;

    TupleHelpers::electronIDSF(iEvent.isRealData(), electron,
    userData0, electronDataIDweight, electronMcIDweight );

    TupleHelpers::electronISOLSF(iEvent.isRealData(), electron,
    userData0, electronDataISOLweight, electronMcISOLweight );

    CurrentElectronTauWeight.set_electronDataIDweight(electronDataIDweight);
    CurrentElectronTauWeight.set_electronMcIDweight(electronMcIDweight);
    CurrentElectronTauWeight.set_electronDataISOLweight(electronDataISOLweight);
    CurrentElectronTauWeight.set_electronMcISOLweight(electronMcISOLweight);

    //////////////
    // get the higgs pt reweight
    // for SUSY samples

    double nominalHIGLUXHQTmhmax = 1.0;
    double upHIGLUXHQTmhmax = 1.0;
    double downHIGLUXHQTmhmax = 1.0;
    double nominalPOWHEGmhmod = 1.0;
    double upPOWHEGmhmod = 1.0;
    double downPOWHEGmhmod = 1.0;

    TupleHelpers::getHiggsPtWeights(userData0, electronTau.genBosonP4(),
    nominalHIGLUXHQTmhmax,
    upHIGLUXHQTmhmax,
    downHIGLUXHQTmhmax,
    nominalPOWHEGmhmod,
    upPOWHEGmhmod,
    downPOWHEGmhmod);

    CurrentElectronTauWeight.set_nominalHIGLUXHQTmhmax(nominalHIGLUXHQTmhmax);
    CurrentElectronTauWeight.set_upHIGLUXHQTmhmax(upHIGLUXHQTmhmax);
    CurrentElectronTauWeight.set_downHIGLUXHQTmhmax(downHIGLUXHQTmhmax);
    CurrentElectronTauWeight.set_nominalPOWHEGmhmod(nominalPOWHEGmhmod);
    CurrentElectronTauWeight.set_upPOWHEGmhmod(upPOWHEGmhmod);
    CurrentElectronTauWeight.set_downPOWHEGmhmod(downPOWHEGmhmod);

    ////////////////
    // QCD template
    // reweights

    double etaDepQCDShapeTemplateCorrection = 1.0;
    double inclusiveQCDShapeTemplateCorrection = 1.0;

    TupleHelpers::getQCDShapeTemplateCorrections(etaDepQCDShapeTemplateCorrection,
    inclusiveQCDShapeTemplateCorrection, tau);

    CurrentElectronTauWeight.set_etaDepQCDShapeTemplateCorrection(etaDepQCDShapeTemplateCorrection);
    CurrentElectronTauWeight.set_inclusiveQCDShapeTemplateCorrection(inclusiveQCDShapeTemplateCorrection);

    /////////////
    // tt Pt reweight

    double TTbarPtWeight = TupleHelpers::getTTbarPtWeight(
    electronTau.genTOPp4().pt(), electronTau.genTOPBARp4().pt());

    CurrentElectronTauWeight.set_TTbarPtWeight(TTbarPtWeight);


    /////////////
    // add the current pair
    // to the collection



    TupleElectronTauWeights->push_back(CurrentElectronTauWeight);


  }

  iEvent.put( TupleElectronTauWeights, NAME_ );


}

// ------------ method called once each job just before starting event loop  ------------
void
TupleElectronTauWeightProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TupleElectronTauWeightProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
TupleElectronTauWeightProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TupleElectronTauWeightProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TupleElectronTauWeightProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TupleElectronTauWeightProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleElectronTauWeightProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleElectronTauWeightProducer);
