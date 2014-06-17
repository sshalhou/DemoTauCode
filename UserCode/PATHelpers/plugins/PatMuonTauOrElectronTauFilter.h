//
// Filter module to pick only eTau or muTau events
//

#ifndef UserCode_PATHelpers_PatMuonTauOrElectronTauFilter_h
#define UserCode_PATHelpers_PatMuonTauOrElectronTauFilter_h

#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"


namespace pat {


  class PatMuonTauOrElectronTauFilter : public edm::EDFilter {

    public:

      explicit PatMuonTauOrElectronTauFilter(const edm::ParameterSet & iConfig);
      virtual ~PatMuonTauOrElectronTauFilter();

    private:

      virtual bool filter(edm::Event & iEvent, const edm::EventSetup & iSetup);

    private:

      edm::InputTag electronSource_;
      edm::InputTag muonSource_;
      edm::InputTag tauSource_;
      bool          countElectronTaus_;
      bool          countMuonTaus_;
      unsigned int  minNumber_;
      unsigned int  maxNumber_;

  };


}

#endif
