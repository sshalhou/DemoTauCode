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
  void set_NumPileupInt(double);
  void set_NumTruePileUpInt(double);
  void set_NumPileupIntM1(double);
  void set_NumTruePileUpIntM1(double);
  void set_NumPileupIntP1(double);
  void set_NumTruePileUpIntP1(double);


  // getters
  double puWeight() const;
  double puWeightM1() const;
  double puWeightP1() const;
  double NumPileupInt() const;
  double NumTruePileUpInt() const;
  double NumPileupIntM1() const;
  double NumTruePileUpIntM1() const;
  double NumPileupIntP1() const;
  double NumTruePileUpIntP1() const;

private:

  double m_puWeight;
  double m_puWeightM1;
  double m_puWeightP1;
  double m_NumPileupInt;
  double m_NumTruePileUpInt;
  double m_NumPileupIntM1;
  double m_NumTruePileUpIntM1;
  double m_NumPileupIntP1;
  double m_NumTruePileUpIntP1;





};

typedef std::vector<TupleMuonTauWeight> TupleMuonTauWeightCollection;

#endif
