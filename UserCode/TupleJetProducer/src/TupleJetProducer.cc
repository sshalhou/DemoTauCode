// -*- C++ -*-
//
// Package:    TupleJetProducer
// Class:      TupleJetProducer
//
/**\class TupleJetProducer TupleJetProducer.cc TEMP/TupleJetProducer/src/TupleJetProducer.cc

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
#include <stdio.h>
#include <assert.h>

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
#include "UserCode/TupleObjects/interface/TupleJet.h"
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
#include "PhysicsTools/SelectorUtils/interface/PFJetIDSelectionFunctor.h"
#include "UserCode/TupleObjects/interface/TupleUserSpecifiedData.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "JetMETCorrections/Objects/interface/JetCorrector.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "PhysicsTools/PatAlgos/plugins/JetCorrFactorsProducer.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"


typedef math::XYZTLorentzVector LorentzVector;
typedef std::vector<edm::InputTag> vInputTag;



//
// class declaration
//

class TupleJetProducer : public edm::EDProducer {
public:
  explicit TupleJetProducer(const edm::ParameterSet&);
  ~TupleJetProducer();

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
  edm::InputTag jetSrc_;
  string NAME_;
  edm::InputTag puJetIdMVASrc_;
  edm::InputTag puJetIdFlagSrc_;





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
TupleJetProducer::TupleJetProducer(const edm::ParameterSet& iConfig):
jetSrc_(iConfig.getParameter<edm::InputTag>("jetSrc" )),
NAME_(iConfig.getParameter<string>("NAME" )),
puJetIdMVASrc_(iConfig.getParameter<edm::InputTag>("puJetIdMVASrc" )),
puJetIdFlagSrc_(iConfig.getParameter<edm::InputTag>("puJetIdFlagSrc" ))
{





  produces< vector<TupleJet> >(NAME_).setBranchAlias(NAME_);


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


TupleJetProducer::~TupleJetProducer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
TupleJetProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{


  //////////////////
  // get jets

  edm::Handle<edm::View<pat::Jet> > jets;
  iEvent.getByLabel(jetSrc_,jets);



  ///////////////////////////////////////
  // figure out how many of these jets
  // pass the loose WP



  edm::Handle<edm::ValueMap<float> > puJetIdMVA;
  iEvent.getByLabel(puJetIdMVASrc_,puJetIdMVA);


  edm::Handle<edm::ValueMap<int> > puJetIdFlag;
  iEvent.getByLabel(puJetIdFlagSrc_,puJetIdFlag);




  ///////////////////////////////////
  //  set up the PF jet ID (loose)
  PFJetIDSelectionFunctor pfjetIDLoose( PFJetIDSelectionFunctor::FIRSTDATA, PFJetIDSelectionFunctor::LOOSE );
  pat::strbitset retpf = pfjetIDLoose.getBitTemplate();


  ////////////

  auto_ptr<TupleJetCollection> TupleJets (new TupleJetCollection);





  ///////////////
  // init btag scale factor tool

  BtagSF btagSFtool(0);

  ///////////////
  // get the JEC

  edm::ESHandle<JetCorrectorParametersCollection> JetCorParColl;
  iSetup.get<JetCorrectionsRecord>().get("AK5PF",JetCorParColl);
  JetCorrectorParameters const & JetCorPar = (*JetCorParColl)["Uncertainty"];
  JetCorrectionUncertainty jecUnc(JetCorPar);

  //////
  // loop over jets

  for ( unsigned int i=0; i<jets->size(); ++i )
  {
    const pat::Jet & patjet = jets->at(i);

    //////////////////////////////
    // want to obtain the JEC shift
    ///////////////////////////////

    jecUnc.setJetEta(patjet.eta());
    jecUnc.setJetPt(patjet.pt());
    double shift  = jecUnc.getUncertainty( true );

    double lowPt = patjet.pt() * (1.0-shift);

    //std::cout<<" jet pt "<<patjet.pt()<<" low pt "<< lowPt <<" eta: "<<patjet.eta()<<endl;

    if(lowPt<20.0 || fabs(patjet.eta())>5.0) continue;



    float mva   = (*puJetIdMVA)[jets->refAt(i)];
    int    idflag = (*puJetIdFlag)[jets->refAt(i)];


    TupleJet CurrentJet;



    // corrected 4-vector
    CurrentJet.set_p4(patjet.p4());

    // JEC shift
    CurrentJet.set_JecShift(shift);

    // passes PU jet ID Loose, Medium, Tight, and Score
    CurrentJet.set_passesPUjetIDLoose(PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kLoose ));
    CurrentJet.set_passesPUjetIDMedium(PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kMedium ));
    CurrentJet.set_passesPUjetIDTight(PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kTight ));
    CurrentJet.set_PUjetIDScore(mva);
    CurrentJet.set_PUjetIDFlag(idflag);


    // passes PF jet ID loose?
    retpf.set(false);
    CurrentJet.set_passesPFjetIDLoose(pfjetIDLoose( patjet, retpf ) );

    // check the sf-corrected b-tag

    bool isbtagged = btagSFtool.isbtagged(
    patjet.pt(), patjet.eta(),
    patjet.bDiscriminator("combinedSecondaryVertexBJetTags"),
    patjet.partonFlavour(),
    iEvent.isRealData(),
    0,0,1);

    CurrentJet.set_isBtagged(isbtagged);

    // store the b-tag disc. value

    CurrentJet.set_combinedSecondaryVertexBJetTags(patjet.bDiscriminator("combinedSecondaryVertexBJetTags"));

    // store the parton info

    CurrentJet.set_partonFlavour(patjet.partonFlavour());



    ////////////
    // store the Jet

    TupleJets->push_back(CurrentJet);

      }





  iEvent.put( TupleJets, NAME_ );



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
TupleJetProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TupleJetProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
TupleJetProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TupleJetProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TupleJetProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TupleJetProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleJetProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleJetProducer);
