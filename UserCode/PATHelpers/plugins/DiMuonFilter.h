//
// Filter module to pick only eTau or muTau events
//

#ifndef UserCode_PATHelpers_DiMuonFilter_h
#define UserCode_PATHelpers_DiMuonFilter_h

#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"


namespace pat {


  class DiMuonFilter : public edm::EDFilter {

    public:

      explicit DiMuonFilter(const edm::ParameterSet & iConfig);
      virtual ~DiMuonFilter();

    private:

      virtual bool filter(edm::Event & iEvent, const edm::EventSetup & iSetup);

    private:


      edm::InputTag muonSource_;
      edm::InputTag vertexSource_;


  };


}

#endif
