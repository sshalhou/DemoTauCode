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
  void set_HadronicTauDataTrigEffAntiEMed(double);
  void set_HadronicTauMcTrigEffAntiEMed(double);
  void set_HadronicTauDataTrigEffAntiETight(double);
  void set_HadronicTauMcTrigEffAntiETight(double);
  void set_electronDataIDweight(double);
  void set_electronMcIDweight(double);
  void set_electronDataISOLweight(double);
  void set_electronMcISOLweight(double);
  void set_EffDataHighPtTauTrigger(double);
  void set_EffMcHighPtTauTrigger(double);
  void set_TauFakeCorrection(double);
  void set_DecayModeCorrectionFactor(double);
  void set_ZeeScaleFactor(double);
  void set_nominalHIGLUXHQTmhmax(double);
  void set_upHIGLUXHQTmhmax(double);
  void set_downHIGLUXHQTmhmax(double);
  void set_nominalPOWHEGmhmod(double);
  void set_upPOWHEGmhmod(double);
  void set_downPOWHEGmhmod(double);
  void set_upPOWHEGscale(double);
  void set_downPOWHEGscale(double);
  void set_etaDepQCDShapeTemplateCorrection(double);
  void set_inclusiveQCDShapeTemplateCorrection(double);
  void set_TTbarPtWeight(double);
  void set_TauSpinnerWT(double);
  void set_TauSpinnerWTFlip(double);
  void set_TauSpinnerWThminus(double);
  void set_TauSpinnerWThplus(double);
  void set_hepNUP(int);
  void set_weightHEPNUP_DYJets(double);
  void set_weightHEPNUP_WJets(double);


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
  double HadronicTauDataTrigEffAntiEMed() const;
  double HadronicTauMcTrigEffAntiEMed() const;
  double HadronicTauDataTrigEffAntiETight() const;
  double HadronicTauMcTrigEffAntiETight() const;
  double electronDataIDweight() const;
  double electronMcIDweight() const;
  double electronDataISOLweight() const;
  double electronMcISOLweight() const;
  double EffDataHighPtTauTrigger() const;
  double EffMcHighPtTauTrigger() const;
  double TauFakeCorrection() const;
  double DecayModeCorrectionFactor() const;
  double ZeeScaleFactor() const;
  double nominalHIGLUXHQTmhmax() const;
  double upHIGLUXHQTmhmax() const;
  double downHIGLUXHQTmhmax() const;
  double nominalPOWHEGmhmod() const;
  double upPOWHEGmhmod() const;
  double downPOWHEGmhmod() const;
  double upPOWHEGscale() const;
  double downPOWHEGscale() const;
  double etaDepQCDShapeTemplateCorrection() const;
  double inclusiveQCDShapeTemplateCorrection() const;
  double TTbarPtWeight() const;
  double TauSpinnerWT() const;
  double TauSpinnerWTFlip() const;
  double TauSpinnerWThminus() const;
  double TauSpinnerWThplus() const;
  int    hepNUP() const;
  double weightHEPNUP_DYJets() const;
  double weightHEPNUP_WJets() const;


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
  double m_HadronicTauDataTrigEffAntiEMed;
  double m_HadronicTauMcTrigEffAntiEMed;
  double m_HadronicTauDataTrigEffAntiETight;
  double m_HadronicTauMcTrigEffAntiETight;
  double m_electronDataIDweight;
  double m_electronMcIDweight;
  double m_electronDataISOLweight;
  double m_electronMcISOLweight;
  double m_EffDataHighPtTauTrigger;
  double m_EffMcHighPtTauTrigger;
  double m_TauFakeCorrection;
  double m_DecayModeCorrectionFactor;
  double m_ZeeScaleFactor;
  double m_nominalHIGLUXHQTmhmax;
  double m_upHIGLUXHQTmhmax;
  double m_downHIGLUXHQTmhmax;
  double m_nominalPOWHEGmhmod;
  double m_upPOWHEGmhmod;
  double m_downPOWHEGmhmod;
  double m_upPOWHEGscale;
  double m_downPOWHEGscale;
  double m_etaDepQCDShapeTemplateCorrection;
  double m_inclusiveQCDShapeTemplateCorrection;
  double m_TTbarPtWeight;
  double m_TauSpinnerWT;
  double m_TauSpinnerWTFlip;
  double m_TauSpinnerWThminus;
  double m_TauSpinnerWThplus;
  int    m_hepNUP;
  double m_weightHEPNUP_DYJets;
  double m_weightHEPNUP_WJets;



};

typedef std::vector<TupleElectronTauWeight> TupleElectronTauWeightCollection;

#endif
