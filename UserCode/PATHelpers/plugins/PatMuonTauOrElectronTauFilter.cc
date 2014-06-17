#include "UserCode/PATHelpers/plugins/PatMuonTauOrElectronTauFilter.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"


using namespace pat;


PatMuonTauOrElectronTauFilter::PatMuonTauOrElectronTauFilter(const edm::ParameterSet & iConfig) {
  electronSource_ = iConfig.getParameter<edm::InputTag>( "electronSource" );
  muonSource_     = iConfig.getParameter<edm::InputTag>( "muonSource" );
  tauSource_      = iConfig.getParameter<edm::InputTag>( "tauSource" );
  countElectronTaus_ = iConfig.getParameter<bool>         ( "countElectronTaus" );
  countMuonTaus_     = iConfig.getParameter<bool>         ( "countMuonTaus" );
}


PatMuonTauOrElectronTauFilter::~PatMuonTauOrElectronTauFilter() {
}


bool PatMuonTauOrElectronTauFilter::filter(edm::Event & iEvent, const edm::EventSetup & iSetup) {
  edm::Handle<edm::View<Electron> > electrons;
  if (countElectronTaus_) iEvent.getByLabel(electronSource_, electrons);
  edm::Handle<edm::View<Muon> > muons;
  if (countMuonTaus_) iEvent.getByLabel(muonSource_, muons);
  edm::Handle<edm::View<Tau> > taus;
  iEvent.getByLabel(tauSource_, taus);


  // return 0 if no hadronic taus
  if(taus->size() == 0 ) return 0;
  else
    {
      // return true if >= 1 electron
      if(countElectronTaus_ && electrons->size()>0) return 1;

      // return true if >= 1 muon 
      if(countMuonTaus_ && muons->size()>0) return 1;
    }

  // return 0 if reach here
   return 0;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(PatMuonTauOrElectronTauFilter);
