#ifndef UserCode_TupleObjects_TupleElectronTauWeight_h
#define UserCode_TupleObjects_TupleElectronTauWeight_h


// system include files
#include <memory>

// needed by ntuple electron producer
#include <vector>
#include <iostream>
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;


class TupleElectronTauWeight
{

public:
  TupleElectronTauWeight();
  virtual ~TupleElectronTauWeight(){}

  // setters
  void set_puWeight(double);


  // getters
  double puWeight() const;

private:

  double m_puWeight;

};

typedef std::vector<TupleElectronTauWeight> TupleElectronTauWeightCollection;

#endif
