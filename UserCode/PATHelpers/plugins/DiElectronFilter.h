//
// Filter module to pick only eTau or muTau events
//

#ifndef UserCode_PATHelpers_DiElectronFilter_h
#define UserCode_PATHelpers_DiElectronFilter_h

#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"


namespace pat {


  class DiElectronFilter : public edm::EDFilter {

    public:

      explicit DiElectronFilter(const edm::ParameterSet & iConfig);
      virtual ~DiElectronFilter();

    private:

      virtual bool filter(edm::Event & iEvent, const edm::EventSetup & iSetup);

    private:


      edm::InputTag electronSource_;
      edm::InputTag vertexSource_;


  };


}

#endif
