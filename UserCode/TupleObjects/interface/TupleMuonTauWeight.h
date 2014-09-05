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
  void set_EffDataISOMU17andISOMU18(double);
  void set_EffMcISOMU17andISOMU18(double);
  void set_HadronicTauDataTrigEffAntiMuMed(double);
  void set_HadronicTauMcTrigEffAntiMuMed(double);
  void set_muonDataIDweight(double);
  void set_muonMcIDweight(double);
  void set_muonDataISOLweight(double);
  void set_muonMcISOLweight(double);
  void set_EffDataHighPtTauTrigger(double);
  void set_EffMcHighPtTauTrigger(double);
  void set_TauFakeCorrection(double);
  void set_DecayModeCorrectionFactor(double);
  void set_nominalHIGLUXHQTmhmax(double);
  void set_upHIGLUXHQTmhmax(double);
  void set_downHIGLUXHQTmhmax(double);
  void set_nominalPOWHEGmhmod(double);
  void set_upPOWHEGmhmod(double);
  void set_downPOWHEGmhmod(double);
  void set_etaDepQCDShapeTemplateCorrection(double);
  void set_inclusiveQCDShapeTemplateCorrection(double);
  void set_TTbarPtWeight(double);

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
  double EffDataISOMU17andISOMU18() const;
  double EffMcISOMU17andISOMU18() const;
  double HadronicTauDataTrigEffAntiMuMed() const;
  double HadronicTauMcTrigEffAntiMuMed() const;
  double muonDataIDweight() const;
  double muonMcIDweight() const;
  double muonDataISOLweight() const;
  double muonMcISOLweight() const;
  double EffDataHighPtTauTrigger() const;
  double EffMcHighPtTauTrigger() const;
  double TauFakeCorrection() const;
  double DecayModeCorrectionFactor() const;
  double nominalHIGLUXHQTmhmax() const;
  double upHIGLUXHQTmhmax() const;
  double downHIGLUXHQTmhmax() const;
  double nominalPOWHEGmhmod() const;
  double upPOWHEGmhmod() const;
  double downPOWHEGmhmod() const;
  double etaDepQCDShapeTemplateCorrection() const;
  double inclusiveQCDShapeTemplateCorrection() const;
  double TTbarPtWeight() const;





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
  double m_EffDataISOMU17andISOMU18;
  double m_EffMcISOMU17andISOMU18;
  double m_HadronicTauDataTrigEffAntiMuMed;
  double m_HadronicTauMcTrigEffAntiMuMed;
  double m_muonDataIDweight;
  double m_muonMcIDweight;
  double m_muonDataISOLweight;
  double m_muonMcISOLweight;
  double m_EffDataHighPtTauTrigger;
  double m_EffMcHighPtTauTrigger;
  double m_TauFakeCorrection;
  double m_DecayModeCorrectionFactor;
  double m_nominalHIGLUXHQTmhmax;
  double m_upHIGLUXHQTmhmax;
  double m_downHIGLUXHQTmhmax;
  double m_nominalPOWHEGmhmod;
  double m_upPOWHEGmhmod;
  double m_downPOWHEGmhmod;
  double m_etaDepQCDShapeTemplateCorrection;
  double m_inclusiveQCDShapeTemplateCorrection;
  double m_TTbarPtWeight;






};

typedef std::vector<TupleMuonTauWeight> TupleMuonTauWeightCollection;

#endif
