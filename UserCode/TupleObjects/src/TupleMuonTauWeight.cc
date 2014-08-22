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

}

//Setting Weights

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
