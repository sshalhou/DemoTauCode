// -*- C++ -*-
//
// Package:    DemoAna
// Class:      DemoAna
// 
/**\class DemoAna DemoAna.cc demo_analysis/DemoAna/src/DemoAna.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Wed Apr  9 10:13:25 CDT 2014
// $Id$
//
//


// system include files
#include <memory>
#include <map>
#include <string>

// root includes
#include "TFile.h"
#include "TF1.h"
#include "TH1F.h"

// user include files



#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"


#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

//#include "DataFormats/MuonReco/interface/MuonSelectors.h" // not sure this is needed

//
// class declaration
//

class DemoAna : public edm::EDAnalyzer {
   public:
      explicit DemoAna(const edm::ParameterSet&);
      ~DemoAna();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      // ----------member data ---------------------------

      edm::InputTag tauSrc_;
      edm::InputTag muonSrc_;
      edm::InputTag pvertexSrc_;	

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

TFile myfile("test_ntuple_file.root","RECREATE");

//
// constructors and destructor
//
DemoAna::DemoAna(const edm::ParameterSet& iConfig):
tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("tauSrc" )),
muonSrc_(iConfig.getUntrackedParameter<edm::InputTag>("muonSrc" )),
pvertexSrc_(iConfig.getUntrackedParameter<edm::InputTag>("pvertexSrc" ))

{
   //now do what ever initialization is needed



}


DemoAna::~DemoAna()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

myfile.Close();

}


//
// member functions
//

// ------------ method called for each event  ------------
void
DemoAna::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

   using namespace edm;


  std::cout<<" id,  lumi = "<<iEvent.id()<<std::endl;
  std::cout<<" is it real data "<< iEvent.isRealData() <<std::endl;

//////////////////////
  // get tau collection  
  edm::Handle<edm::View<pat::Tau> > taus;
  iEvent.getByLabel(tauSrc_,taus);

  // get muon collection  
  edm::Handle<edm::View<pat::Muon> > muons;
  iEvent.getByLabel(muonSrc_,muons);


  // get primary vertex collection  
  edm::Handle<edm::View<reco::Vertex> > pvertices;
  iEvent.getByLabel(pvertexSrc_,pvertices);

//////////////////////


  int nmuon = 0;
  for(edm::View<pat::Muon>::const_iterator muon=muons->begin(); muon!=muons->end(); ++muon) {
                
                nmuon++;
   std::cout<<" tight muon ? "<<isTightMuon()<<std::endl;

											     } // muons

		std::cout<<" event had "<<nmuon<<" cleanPatMuons "<<std::endl;



  int ntau = 0;	
  for(edm::View<pat::Tau>::const_iterator tau=taus->begin(); tau!=taus->end(); ++tau) { 

		ntau++; 

	          std::cout<<" isTauIDAvailable againstMuonLoose "<<tau->isTauIDAvailable("againstMuonLoose")<<std::endl;
	          std::cout<<"  againstMuonLoose = "<<tau->tauID("againstMuonLoose")<<std::endl;
	          std::cout<<" byCombinedIsolationDeltaBetaCorrRaw = "<<tau->tauID("byCombinedIsolationDeltaBetaCorrRaw")<<std::endl;
		  std::cout<<" decay mode "<<tau->decayMode()<<std::endl;

											} // tau loop
		std::cout<<" ntau = "<<ntau<<std::endl;


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
DemoAna::beginJob()
{

}

// ------------ method called once each job just after ending the event loop  ------------
void 
DemoAna::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
DemoAna::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
DemoAna::endRun(edm::Run const&, edm::EventSetup const&)
{

}

// ------------ method called when starting to processes a luminosity block  ------------
void 
DemoAna::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
DemoAna::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DemoAna::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DemoAna);
