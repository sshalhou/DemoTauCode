#ifndef UserCode_TupleObjects_TupleMuonTauWeight_h
#define UserCode_TupleObjects_TupleMuonTauWeight_h


// system include files
#include <memory>

// needed by ntuple muons producer
#include <vector>
#include <iostream>
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;


class TupleMuonTauWeight
{

public:
  TupleMuonTauWeight();
  virtual ~TupleMuonTauWeight(){}

  // setters
  void set_puWeight(double);


  // getters
  double puWeight() const;

private:

  double m_puWeight;

};

typedef std::vector<TupleMuonTauWeight> TupleMuonTauWeightCollection;

#endif
