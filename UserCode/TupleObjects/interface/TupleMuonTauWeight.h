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
  void set_puWeightM1(double);
  void set_puWeightP1(double);
  void set_NumPileupInt(float);
  void set_NumTruePileUpInt(float);
  void set_NumPileupIntM1(float);
  void set_NumTruePileUpIntM1(float);
  void set_NumPileupIntP1(float);
  void set_NumTruePileUpIntP1(float);


  // getters
  double puWeight() const;
  double puWeightM1() const;
  double puWeightP1() const;
  float NumPileupInt() const;
  float NumTruePileUpInt() const;
  float NumPileupIntM1() const;
  float NumTruePileUpIntM1() const;
  float NumPileupIntP1() const;
  float NumTruePileUpIntP1() const;

private:

  double m_puWeight;
  double m_puWeightM1;
  double m_puWeightP1;
  float m_NumPileupInt;
  float m_NumTruePileUpInt;
  float m_NumPileupIntM1;
  float m_NumTruePileUpIntM1;
  float m_NumPileupIntP1;
  float m_NumTruePileUpIntP1;





};

typedef std::vector<TupleMuonTauWeight> TupleMuonTauWeightCollection;

#endif
