#ifndef UserCode_TupleObjects_TupleMuonTauVetoes_h
#define UserCode_TupleObjects_TupleMuonTauVetoes_h


// system include files
#include <memory>



// needed by ntuple Taus producer
#include <vector>
#include <iostream>
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;


class TupleMuonTauVetoes
{



public:
  TupleMuonTauVetoes();
  virtual ~TupleMuonTauVetoes(){}

  // setters

  void set_passesThirdLeptonVeto(bool);
  void set_passesSecondLeptonVeto(bool);


  // getters

  bool passesThirdLeptonVeto() const;
  bool passesSecondLeptonVeto() const;



private:

  bool m_passesThirdLeptonVeto;
  bool m_passesSecondLeptonVeto;


};

typedef std::vector<TupleMuonTauVetoes> TupleMuonTauVetoesCollection;

#endif
