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
  void set_puWeightM1(double);
  void set_puWeightP1(double);
  void set_NumPileupInt(float);
  void set_NumTruePileUpInt(float);
  void set_NumPileupIntM1(float);
  void set_NumTruePileUpIntM1(float);
  void set_NumPileupIntP1(float);
  void set_NumTruePileUpIntP1(float);
  void set_EffDataELE20andELE22(double);
  void set_EffMcELE20andELE22(double);
  void set_HadronicTauDataTrigEff_antiEMed(double);
  void set_HadronicTauMcTrigEff_antiEMed(double);
  void set_HadronicTauDataTrigEff_antiETight(double);
  void set_HadronicTauMcTrigEff_antiETight(double);

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
  double EffDataELE20andELE22() const;
  double EffMcELE20andELE22() const;
  double set_HadronicTauDataTrigEff_antiEMed() const;
  double set_HadronicTauMcTrigEff_antiEMed() const;
  double set_HadronicTauDataTrigEff_antiETight() const;
  double set_HadronicTauMcTrigEff_antiETight() const;

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
  double m_EffDataELE20andELE22;
  double m_EffMcELE20andELE22;
  double m_HadronicTauDataTrigEff_antiEMed;
  double m_HadronicTauMcTrigEff_antiEMed;
  double m_HadronicTauDataTrigEff_antiETight;
  double m_HadronicTauMcTrigEff_antiETight;



};

typedef std::vector<TupleElectronTauWeight> TupleElectronTauWeightCollection;

#endif
