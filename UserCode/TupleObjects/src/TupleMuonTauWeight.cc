#include "UserCode/TupleObjects/interface/TupleMuonTauWeight.h"
#include "TMath.h"

TupleMuonTauWeight::TupleMuonTauWeight()
{
  m_puWeight = NAN;
  m_puWeightM1 = NAN;
  m_puWeightP1 = NAN;
  m_NumPileupInt = NAN;
  m_NumTruePileUpInt = NAN;
  m_NumPileupIntM1 = NAN;
  m_NumTruePileUpIntM1 = NAN;
  m_NumPileupIntP1 = NAN;
  m_NumTruePileUpIntP1 = NAN;
  m_EffDataISOMU17andISOMU18 = NAN;
  m_EffMcISOMU17andISOMU18 = NAN;
  m_HadronicTauDataTrigEffAntiMuMed = NAN;
  m_HadronicTauMcTrigEffAntiMuMed = NAN;
  m_muonDataIDweight = NAN;
  m_muonMcIDweight = NAN;
  m_muonDataISOLweight = NAN;
  m_muonMcISOLweight = NAN;
  m_EffDataHighPtTauTrigger = NAN;
  m_EffMcHighPtTauTrigger = NAN;
  m_TauFakeCorrection = NAN;
  m_DecayModeCorrectionFactor = NAN;
  m_nominalHIGLUXHQTmhmax = NAN;
  m_upHIGLUXHQTmhmax = NAN;
  m_downHIGLUXHQTmhmax = NAN;
  m_nominalPOWHEGmhmod = NAN;
  m_upPOWHEGmhmod = NAN;
  m_downPOWHEGmhmod = NAN;
  m_etaDepQCDShapeTemplateCorrection = NAN;
  m_inclusiveQCDShapeTemplateCorrection = NAN;
  m_TTbarPtWeight = NAN;



}

//Setting Weights

/////////////
// tt pt reweight

void TupleMuonTauWeight::set_TTbarPtWeight(double TTbarPtWeight_) { m_TTbarPtWeight  =  TTbarPtWeight_;}
double TupleMuonTauWeight::TTbarPtWeight() const { return m_TTbarPtWeight; }

///////////////
// QCD template reweight

void TupleMuonTauWeight::set_etaDepQCDShapeTemplateCorrection(double etaDepQCDShapeTemplateCorrection_) { m_etaDepQCDShapeTemplateCorrection  =  etaDepQCDShapeTemplateCorrection_;}
double TupleMuonTauWeight::etaDepQCDShapeTemplateCorrection() const { return m_etaDepQCDShapeTemplateCorrection; }

void TupleMuonTauWeight::set_inclusiveQCDShapeTemplateCorrection(double inclusiveQCDShapeTemplateCorrection_) { m_inclusiveQCDShapeTemplateCorrection  =  inclusiveQCDShapeTemplateCorrection_;}
double TupleMuonTauWeight::inclusiveQCDShapeTemplateCorrection() const { return m_inclusiveQCDShapeTemplateCorrection; }

///////////////
// higgs pt weight for SUSY signal

void TupleMuonTauWeight::set_nominalHIGLUXHQTmhmax(double nominalHIGLUXHQTmhmax_) { m_nominalHIGLUXHQTmhmax  =  nominalHIGLUXHQTmhmax_;}
double TupleMuonTauWeight::nominalHIGLUXHQTmhmax() const { return m_nominalHIGLUXHQTmhmax; }

void TupleMuonTauWeight::set_upHIGLUXHQTmhmax(double upHIGLUXHQTmhmax_) { m_upHIGLUXHQTmhmax  =  upHIGLUXHQTmhmax_;}
double TupleMuonTauWeight::upHIGLUXHQTmhmax() const { return m_upHIGLUXHQTmhmax; }

void TupleMuonTauWeight::set_downHIGLUXHQTmhmax(double downHIGLUXHQTmhmax_) { m_downHIGLUXHQTmhmax  =  downHIGLUXHQTmhmax_;}
double TupleMuonTauWeight::downHIGLUXHQTmhmax() const { return m_downHIGLUXHQTmhmax; }

void TupleMuonTauWeight::set_nominalPOWHEGmhmod(double nominalPOWHEGmhmod_) { m_nominalPOWHEGmhmod  =  nominalPOWHEGmhmod_;}
double TupleMuonTauWeight::nominalPOWHEGmhmod() const { return m_nominalPOWHEGmhmod; }

void TupleMuonTauWeight::set_upPOWHEGmhmod(double upPOWHEGmhmod_) { m_upPOWHEGmhmod  =  upPOWHEGmhmod_;}
double TupleMuonTauWeight::upPOWHEGmhmod() const { return m_upPOWHEGmhmod; }

void TupleMuonTauWeight::set_downPOWHEGmhmod(double downPOWHEGmhmod_) { m_downPOWHEGmhmod  =  downPOWHEGmhmod_;}
double TupleMuonTauWeight::downPOWHEGmhmod() const { return m_downPOWHEGmhmod; }



////////////////////
// decay mode corr.
// for Z->tau tau
// and signal

void TupleMuonTauWeight::set_DecayModeCorrectionFactor(double DecayModeCorrectionFactor_) { m_DecayModeCorrectionFactor  =  DecayModeCorrectionFactor_;}
double TupleMuonTauWeight::DecayModeCorrectionFactor() const { return m_DecayModeCorrectionFactor; }



///////////////////
// jet to tau fake weight
// for w+jets

void TupleMuonTauWeight::set_TauFakeCorrection(double TauFakeCorrection_) { m_TauFakeCorrection  =  TauFakeCorrection_;}
double TupleMuonTauWeight::TauFakeCorrection() const { return m_TauFakeCorrection; }


//////////////////
// hight pt tau trigger bug

void TupleMuonTauWeight::set_EffDataHighPtTauTrigger(double EffDataHighPtTauTrigger_) { m_EffDataHighPtTauTrigger  =  EffDataHighPtTauTrigger_;}
double TupleMuonTauWeight::EffDataHighPtTauTrigger() const { return m_EffDataHighPtTauTrigger; }

void TupleMuonTauWeight::set_EffMcHighPtTauTrigger(double EffMcHighPtTauTrigger_) { m_EffMcHighPtTauTrigger  =  EffMcHighPtTauTrigger_;}
double TupleMuonTauWeight::EffMcHighPtTauTrigger() const { return m_EffMcHighPtTauTrigger; }

//////////////////
// muon ID and ISOL


void TupleMuonTauWeight::set_muonDataIDweight(double muonDataIDweight_) { m_muonDataIDweight  =  muonDataIDweight_;}
double TupleMuonTauWeight::muonDataIDweight() const { return m_muonDataIDweight; }

void TupleMuonTauWeight::set_muonMcIDweight(double muonMcIDweight_) { m_muonMcIDweight  =  muonMcIDweight_;}
double TupleMuonTauWeight::muonMcIDweight() const { return m_muonMcIDweight; }

void TupleMuonTauWeight::set_muonDataISOLweight(double muonDataISOLweight_) { m_muonDataISOLweight  =  muonDataISOLweight_;}
double TupleMuonTauWeight::muonDataISOLweight() const { return m_muonDataISOLweight; }

void TupleMuonTauWeight::set_muonMcISOLweight(double muonMcISOLweight_) { m_muonMcISOLweight  =  muonMcISOLweight_;}
double TupleMuonTauWeight::muonMcISOLweight() const { return m_muonMcISOLweight; }


////////////////////
// had tau trigger wt

void TupleMuonTauWeight::set_HadronicTauDataTrigEffAntiMuMed(double HadronicTauDataTrigEffAntiMuMed_) { m_HadronicTauDataTrigEffAntiMuMed  =  HadronicTauDataTrigEffAntiMuMed_;}
double TupleMuonTauWeight::HadronicTauDataTrigEffAntiMuMed() const { return m_HadronicTauDataTrigEffAntiMuMed; }

void TupleMuonTauWeight::set_HadronicTauMcTrigEffAntiMuMed(double HadronicTauMcTrigEffAntiMuMed_) { m_HadronicTauMcTrigEffAntiMuMed  =  HadronicTauMcTrigEffAntiMuMed_;}
double TupleMuonTauWeight::HadronicTauMcTrigEffAntiMuMed() const { return m_HadronicTauMcTrigEffAntiMuMed; }


///////////////////////
// muon trigger weights
////////////////////////

void TupleMuonTauWeight::set_EffDataISOMU17andISOMU18(double EffDataISOMU17andISOMU18_) { m_EffDataISOMU17andISOMU18  =  EffDataISOMU17andISOMU18_;}
double TupleMuonTauWeight::EffDataISOMU17andISOMU18() const { return m_EffDataISOMU17andISOMU18; }

void TupleMuonTauWeight::set_EffMcISOMU17andISOMU18(double EffMcISOMU17andISOMU18_) { m_EffMcISOMU17andISOMU18  =  EffMcISOMU17andISOMU18_;}
double TupleMuonTauWeight::EffMcISOMU17andISOMU18() const { return m_EffMcISOMU17andISOMU18; }


////////////////////////
// pile-up reweight   //
////////////////////////


void TupleMuonTauWeight::set_puWeight(double puWeight_) { m_puWeight  =  puWeight_;}
double TupleMuonTauWeight::puWeight() const { return m_puWeight; }

void TupleMuonTauWeight::set_puWeightM1(double puWeightM1_) { m_puWeightM1  =  puWeightM1_;}
double TupleMuonTauWeight::puWeightM1() const { return m_puWeightM1; }

void TupleMuonTauWeight::set_puWeightP1(double puWeightP1_) { m_puWeightP1  =  puWeightP1_;}
double TupleMuonTauWeight::puWeightP1() const { return m_puWeightP1; }

void TupleMuonTauWeight::set_NumPileupInt(float NumPileupInt_) { m_NumPileupInt  =  NumPileupInt_;}
float TupleMuonTauWeight::NumPileupInt() const { return m_NumPileupInt; }

void TupleMuonTauWeight::set_NumTruePileUpInt(float NumTruePileUpInt_) { m_NumTruePileUpInt  =  NumTruePileUpInt_;}
float TupleMuonTauWeight::NumTruePileUpInt() const { return m_NumTruePileUpInt; }

void TupleMuonTauWeight::set_NumPileupIntM1(float NumPileupIntM1_) { m_NumPileupIntM1  =  NumPileupIntM1_;}
float TupleMuonTauWeight::NumPileupIntM1() const { return m_NumPileupIntM1; }

void TupleMuonTauWeight::set_NumTruePileUpIntM1(float NumTruePileUpIntM1_) { m_NumTruePileUpIntM1  =  NumTruePileUpIntM1_;}
float TupleMuonTauWeight::NumTruePileUpIntM1() const { return m_NumTruePileUpIntM1; }

void TupleMuonTauWeight::set_NumPileupIntP1(float NumPileupIntP1_) { m_NumPileupIntP1  =  NumPileupIntP1_;}
float TupleMuonTauWeight::NumPileupIntP1() const { return m_NumPileupIntP1; }

void TupleMuonTauWeight::set_NumTruePileUpIntP1(float NumTruePileUpIntP1_) { m_NumTruePileUpIntP1  =  NumTruePileUpIntP1_;}
float TupleMuonTauWeight::NumTruePileUpIntP1() const { return m_NumTruePileUpIntP1; }
