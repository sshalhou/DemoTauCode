// -*- C++ -*-
//
// Package:    JetTestAnalysis
// Class:      JetTestAnalysis
//
/**\class JetTestAnalysis JetTestAnalysis.cc TEMP/JetTestAnalysis/src/JetTestAnalysis.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Thu Apr 24 07:09:45 CDT 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/PatCandidates/interface/Jet.h"
#include "CMGTools/External/interface/PileupJetIdentifier.h"


#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "DataFormats/JetReco/interface/Jet.h"



//
// class declaration
//

class JetTestAnalysis : public edm::EDAnalyzer {
   public:
      explicit JetTestAnalysis(const edm::ParameterSet&);
      ~JetTestAnalysis();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endluminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      // ----------member data ---------------------------

edm::InputTag jetSrc_;
edm::InputTag puJetIdMVASrc_;
edm::InputTag rhoSrc_;
edm::InputTag pvSrc_;
std::vector<std::string> jecPayloadNames_;
std::string jecUncName_;
boost::shared_ptr<JetCorrectionUncertainty> jecUnc_;
boost::shared_ptr<FactorizedJetCorrector> jec_;

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
JetTestAnalysis::JetTestAnalysis(const edm::ParameterSet& iConfig):
jetSrc_(iConfig.getUntrackedParameter<edm::InputTag>("jetSrc" )),
rhoSrc_   (iConfig.getUntrackedParameter<edm::InputTag>("rhoSrc") ),
pvSrc_    (iConfig.getUntrackedParameter<edm::InputTag>("pvSrc") ),
jecPayloadNames_( iConfig.getUntrackedParameter<std::vector<std::string> >("jecPayloadNames") ),
jecUncName_( iConfig.getUntrackedParameter<std::string>("jecUncName") ),
puJetIdMVASrc_(iConfig.getUntrackedParameter<edm::InputTag>("puJetIdMVASrc" ))
{
   //now do what ever initialization is needed


  //Get the factorized jet corrector parameters.
  std::vector<JetCorrectorParameters> vPar;
  for ( std::vector<std::string>::const_iterator payloadBegin = jecPayloadNames_.begin(),
          payloadEnd = jecPayloadNames_.end(), ipayload = payloadBegin; ipayload != payloadEnd; ++ipayload ) {
    JetCorrectorParameters pars(*ipayload);
    vPar.push_back(pars);
  }

 // Make the FactorizedJetCorrector and Uncertainty
  jec_ = boost::shared_ptr<FactorizedJetCorrector> ( new FactorizedJetCorrector(vPar) );
  jecUnc_ = boost::shared_ptr<JetCorrectionUncertainty>( new JetCorrectionUncertainty(jecUncName_) );




}


JetTestAnalysis::~JetTestAnalysis()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
JetTestAnalysis::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;







edm::Handle<edm::View<pat::Jet> > jets;
iEvent.getByLabel(jetSrc_,jets);

// Get the mean pt per unit area ("rho")
  edm::Handle< double > h_rho;
  iEvent.getByLabel( rhoSrc_, h_rho );

  // Get the primary vertex collection
  edm::Handle< std::vector<reco::Vertex> > h_pv;
  iEvent.getByLabel( pvSrc_, h_pv );


Handle<ValueMap<float> > puJetIdMVA;
iEvent.getByLabel("puJetMva","full53xDiscriminant",puJetIdMVA);

Handle<ValueMap<int> > puJetIdFlag;
iEvent.getByLabel("puJetMva","full53xId",puJetIdFlag);



for ( unsigned int i=0; i<jets->size(); ++i ) {
      const pat::Jet & patjet = jets->at(i);
      float mva   = (*puJetIdMVA)[jets->refAt(i)];
      int    idflag = (*puJetIdFlag)[jets->refAt(i)];
      std::cout << "jet " << i << " pt " << patjet.pt() << " eta " << patjet.eta() << " PU JetID MVA " << mva;


      std::cout<<" loose WP = "<<PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kLoose );
      std::cout<<" medium WP = "<<PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kMedium );
      std::cout<<" tight WP = "<<PileupJetIdentifier::passJetId( idflag, PileupJetIdentifier::kTight );
      std::cout<<" CSV = "<<patjet.bDiscriminator("combinedSecondaryVertexBJetTags");
      std::cout<<" flavor "<<patjet.partonFlavour();
      std::cout<<" currently applied jet correction factor "<<patjet.jecFactor(1);
      std::cout<<std::endl;

/////////////////
// get uncorrected jet, then
// apply JEC 'on the fly'
//////////////////

  reco::Candidate::LorentzVector uncorrJet;
  pat::Jet const * pJet = dynamic_cast<pat::Jet const *>( &*patjet );
  uncorrJet = pJet->correctedP4(0);
  std::cout<<" uncorrect jet pt = " <<uncorrJet.Pt()<<" ";


//      std::cout<<" L1FastJet "<<patjet.jecFactor("L1FastJet")<<" ";
//      std::cout<<" L2Relative "<<patjet.jecFactor("L2Relative")<<" ";
//      std::cout<<" L3Absolute "<<patjet.jecFactor("L3Absolute")<<" ";
//      if(iEvent.isRealData()) {std::cout<<" L2L3Residual "<<patjet.jecFactor("L2L3Residual")<<" ";}
      std::cout << std::endl;
}




#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif

#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif
}


// ------------ method called once each job just before starting event loop  ------------
void
JetTestAnalysis::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
JetTestAnalysis::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
void
JetTestAnalysis::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
JetTestAnalysis::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
JetTestAnalysis::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
JetTestAnalysis::endluminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
JetTestAnalysis::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetTestAnalysis);
