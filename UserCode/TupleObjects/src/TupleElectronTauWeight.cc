#include "UserCode/TupleObjects/interface/TupleElectronTauWeight.h"
#include "TMath.h"

TupleElectronTauWeight::TupleElectronTauWeight()
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
  m_EffDataELE20andELE22 = NAN;
  m_EffMcELE20andELE22 = NAN;

}

//Setting Weights

///////////////////////
// electron trigger
// weights

void TupleElectronTauWeight::set_EffDataELE20andELE22(double EffDataELE20andELE22_) { m_EffDataELE20andELE22  =  EffDataELE20andELE22_;}
double TupleElectronTauWeight::EffDataELE20andELE22() const { return m_EffDataELE20andELE22; }

void TupleElectronTauWeight::set_EffMcELE20andELE22(double EffMcELE20andELE22_) { m_EffMcELE20andELE22  =  EffMcELE20andELE22_;}
double TupleElectronTauWeight::EffMcELE20andELE22() const { return m_EffMcELE20andELE22; }



////////////////////////
// pile-up reweight   //
////////////////////////

void TupleElectronTauWeight::set_puWeight(double puWeight_) { m_puWeight  =  puWeight_;}
double TupleElectronTauWeight::puWeight() const { return m_puWeight; }

void TupleElectronTauWeight::set_puWeightM1(double puWeightM1_) { m_puWeightM1  =  puWeightM1_;}
double TupleElectronTauWeight::puWeightM1() const { return m_puWeightM1; }

void TupleElectronTauWeight::set_puWeightP1(double puWeightP1_) { m_puWeightP1  =  puWeightP1_;}
double TupleElectronTauWeight::puWeightP1() const { return m_puWeightP1; }

void TupleElectronTauWeight::set_NumPileupInt(float NumPileupInt_) { m_NumPileupInt  =  NumPileupInt_;}
float TupleElectronTauWeight::NumPileupInt() const { return m_NumPileupInt; }

void TupleElectronTauWeight::set_NumTruePileUpInt(float NumTruePileUpInt_) { m_NumTruePileUpInt  =  NumTruePileUpInt_;}
float TupleElectronTauWeight::NumTruePileUpInt() const { return m_NumTruePileUpInt; }

void TupleElectronTauWeight::set_NumPileupIntM1(float NumPileupIntM1_) { m_NumPileupIntM1  =  NumPileupIntM1_;}
float TupleElectronTauWeight::NumPileupIntM1() const { return m_NumPileupIntM1; }

void TupleElectronTauWeight::set_NumTruePileUpIntM1(float NumTruePileUpIntM1_) { m_NumTruePileUpIntM1  =  NumTruePileUpIntM1_;}
float TupleElectronTauWeight::NumTruePileUpIntM1() const { return m_NumTruePileUpIntM1; }

void TupleElectronTauWeight::set_NumPileupIntP1(float NumPileupIntP1_) { m_NumPileupIntP1  =  NumPileupIntP1_;}
float TupleElectronTauWeight::NumPileupIntP1() const { return m_NumPileupIntP1; }

void TupleElectronTauWeight::set_NumTruePileUpIntP1(float NumTruePileUpIntP1_) { m_NumTruePileUpIntP1  =  NumTruePileUpIntP1_;}
float TupleElectronTauWeight::NumTruePileUpIntP1() const { return m_NumTruePileUpIntP1; }
