// -*- C++ -*-
//
// Package:    TauTestAnalysis
// Class:      TauTestAnalysis
//
/**\class TauTestAnalysis TauTestAnalysis.cc TEMP/TauTestAnalysis/src/TauTestAnalysis.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Wed Apr 16 11:48:01 CDT 2014
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
#include "DataFormats/PatCandidates/interface/Tau.h"


bool passAntiEMVA(int iCat, float raw, int WP=1) {

  if(iCat<0) return false;
  if(iCat>15) return true;

  float cutsLoose[16]={0.835,0.831,0.849,0.859,0.873,0.823,0.85,0.855,0.816,0.861,0.862,0.847,0.893,0.82,0.845,0.851};
  float cutsMedium[16]={0.933,0.921,0.944,0.945,0.918,0.941,0.981,0.943,0.956,0.947,0.951,0.95,0.897,0.958,0.955,0.942};
  float cutsTight[16]={ 0.96,0.968,0.971,0.972,0.969,0.959,0.981,0.965,0.975,0.972,0.974,0.971,0.897,0.971,0.961,0.97};
  float cutsVeryTight[16]={0.978,0.98,0.982,0.985,0.977,0.974,0.989,0.977,0.986,0.983,0.984,0.983,0.971,0.987,0.977,0.981};
  float cut=0;
  if(WP==0) cut = cutsLoose[iCat];
  if(WP==1) cut = cutsMedium[iCat];
  if(WP==2) cut = cutsTight[iCat];
  if(WP==3) cut = cutsVeryTight[iCat];
  return (raw>cut);
}


//
// class declaration
//

class TauTestAnalysis : public edm::EDAnalyzer {
   public:
      explicit TauTestAnalysis(const edm::ParameterSet&);
      ~TauTestAnalysis();

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
TauTestAnalysis::TauTestAnalysis(const edm::ParameterSet& iConfig):
tauSrc_(iConfig.getUntrackedParameter<edm::InputTag>("tauSrc" ))
{
   //now do what ever initialization is needed

}


TauTestAnalysis::~TauTestAnalysis()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
TauTestAnalysis::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;


// get tau collection
edm::Handle<edm::View<pat::Tau> > taus;
iEvent.getByLabel(tauSrc_,taus);


int ntau = 0;
for(edm::View<pat::Tau>::const_iterator tau=taus->begin(); tau!=taus->end(); ++tau) {

  ntau++;





          std::cout<<" isTauIDAvailable againstMuonLoose "<<tau->isTauIDAvailable("againstMuonLoose")<<std::endl;
          std::cout<<"  againstMuonLoose = "<<tau->tauID("againstMuonLoose")<<std::endl;

          std::cout<<"againstElectronMVA5raw = "<<tau->tauID("againstElectronMVA5raw")<<std::endl;

          std::cout<<" againstElectronLoose = "<<tau->tauID("againstElectronLoose")<<std::endl;
          std::cout<<" againstMuonTight = "<<tau->tauID("againstMuonTight")<<std::endl;
          std::cout<<" againstElectronLooseMVA5 = "<<tau->tauID("againstElectronLooseMVA5")<<std::endl;

          std::cout<<" byMediumCombinedIsolationDeltaBetaCorr3Hits = ";
          std::cout<<tau->tauID("byMediumCombinedIsolationDeltaBetaCorr3Hits")<<std::endl;


          std::cout<<" byCombinedIsolationDeltaBetaCorrRaw = ";
          std::cout<<tau->tauID("byCombinedIsolationDeltaBetaCorrRaw")<<std::endl;
          std::cout<<" decay mode "<<tau->decayMode()<<std::endl;


std::cout<<" dB, dz "<<tau->dB()<<","<<tau->dz()<<std::endl;

std::cout<<" iEvent.id() "<<iEvent.id();
std::cout<<" againstElectronLoose "<<tau->tauID("againstElectronLoose");
std::cout<<" againstElectronLooseMVA5 "<<tau->tauID("againstElectronLooseMVA5");
std::cout<<" againstElectronMVA5raw  "<<tau->tauID("againstElectronMVA5raw");
std::cout<<" againstElectronMVA5category "<<tau->tauID("againstElectronMVA5category");
//std::cout<<" newLOOSEWP "<<passAntiEMVA(tau->tauID("againstElectronMVA3category"), tau->tauID("againstElectronLooseMVA3"), 0);
std::cout<<" decay mode "<<tau->decayMode();
//std::cout<<" newMEDWP "<<passAntiEMVA(tau->tauID("againstElectronMVA3category"), tau->tauID("againstElectronLooseMVA3raw"), 1)<<std::endl;


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


/* WANT TO KEEP ALL THIS IN NTUPLE

The available IDs are: 'againstElectronDeadECAL' 'againstElectronLoose' 'againstElectronLooseMVA5' 'againstElectronMVA5category' 'againstElectronMVA5raw' 'againstElectronMedium' 'againstElectronMediumMVA5' 'againstElectronTight' 'againstElectronTightMVA5' 'againstElectronVLooseMVA5' 'againstElectronVTightMVA5' 'againstMuonLoose' 'againstMuonLoose2' 'againstMuonLoose3' 'againstMuonLooseMVA' 'againstMuonMVAraw' 'againstMuonMedium' 'againstMuonMedium2' 'againstMuonMediumMVA' 'againstMuonTight' 'againstMuonTight2' 'againstMuonTight3' 'againstMuonTightMVA' 'byCombinedIsolationDeltaBetaCorrRaw' 'byCombinedIsolationDeltaBetaCorrRaw3Hits' 'byIsolationMVA3newDMwLTraw' 'byIsolationMVA3newDMwoLTraw' 'byIsolationMVA3oldDMwLTraw' 'byIsolationMVA3oldDMwoLTraw' 'byLooseCombinedIsolationDeltaBetaCorr' 'byLooseCombinedIsolationDeltaBetaCorr3Hits' 'byLooseIsolation' 'byLooseIsolationMVA3newDMwLT' 'byLooseIsolationMVA3newDMwoLT' 'byLooseIsolationMVA3oldDMwLT' 'byLooseIsolationMVA3oldDMwoLT' 'byMediumCombinedIsolationDeltaBetaCorr' 'byMediumCombinedIsolationDeltaBetaCorr3Hits' 'byMediumIsolationMVA3newDMwLT' 'byMediumIsolationMVA3newDMwoLT' 'byMediumIsolationMVA3oldDMwLT' 'byMediumIsolationMVA3oldDMwoLT' 'byTightCombinedIsolationDeltaBetaCorr' 'byTightCombinedIsolationDeltaBetaCorr3Hits' 'byTightIsolationMVA3newDMwLT' 'byTightIsolationMVA3newDMwoLT' 'byTightIsolationMVA3oldDMwLT' 'byTightIsolationMVA3oldDMwoLT' 'byVLooseCombinedIsolationDeltaBetaCorr' 'byVLooseIsolationMVA3newDMwLT' 'byVLooseIsolationMVA3newDMwoLT' 'byVLooseIsolationMVA3oldDMwLT' 'byVLooseIsolationMVA3oldDMwoLT' 'byVTightIsolationMVA3newDMwLT' 'byVTightIsolationMVA3newDMwoLT' 'byVTightIsolationMVA3oldDMwLT' 'byVTightIsolationMVA3oldDMwoLT' 'byVVTightIsolationMVA3newDMwLT' 'byVVTightIsolationMVA3newDMwoLT' 'byVVTightIsolationMVA3oldDMwLT' 'byVVTightIsolationMVA3oldDMwoLT' 'chargedIsoPtSum' 'decayModeFinding' 'decayModeFindingNewDMs' 'decayModeFindingOldDMs' 'neutralIsoPtSum' 'puCorrPtSum' .

*/

// ------------ method called once each job just before starting event loop  ------------
void
TauTestAnalysis::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TauTestAnalysis::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
void
TauTestAnalysis::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
TauTestAnalysis::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
TauTestAnalysis::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
TauTestAnalysis::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TauTestAnalysis::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TauTestAnalysis);
