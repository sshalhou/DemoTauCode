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



}

//Setting Weights


////////////////////////
// pile-up reweight   //
////////////////////////

void TupleElectronTauWeight::set_puWeight(double puWeight_) { m_puWeight  =  puWeight_;}
double TupleElectronTauWeight::puWeight() const { return m_puWeight; }

void TupleElectronTauWeight::set_puWeightM1(double puWeightM1_) { m_puWeightM1  =  puWeightM1_;}
double TupleElectronTauWeight::puWeightM1() const { return m_puWeightM1; }

void TupleElectronTauWeight::set_puWeightP1(double puWeightP1_) { m_puWeightP1  =  puWeightP1_;}
double TupleElectronTauWeight::puWeightP1() const { return m_puWeightP1; }

void TupleElectronTauWeight::set_NumPileupInt(double NumPileupInt_) { m_NumPileupInt  =  NumPileupInt_;}
double TupleElectronTauWeight::NumPileupInt() const { return m_NumPileupInt; }

void TupleElectronTauWeight::set_NumTruePileUpInt(double NumTruePileUpInt_) { m_NumTruePileUpInt  =  NumTruePileUpInt_;}
double TupleElectronTauWeight::NumTruePileUpInt() const { return m_NumTruePileUpInt; }

void TupleElectronTauWeight::set_NumPileupIntM1(double NumPileupIntM1_) { m_NumPileupIntM1  =  NumPileupIntM1_;}
double TupleElectronTauWeight::NumPileupIntM1() const { return m_NumPileupIntM1; }

void TupleElectronTauWeight::set_NumTruePileUpIntM1(double NumTruePileUpIntM1_) { m_NumTruePileUpIntM1  =  NumTruePileUpIntM1_;}
double TupleElectronTauWeight::NumTruePileUpIntM1() const { return m_NumTruePileUpIntM1; }

void TupleElectronTauWeight::set_NumPileupIntP1(double NumPileupIntP1_) { m_NumPileupIntP1  =  NumPileupIntP1_;}
double TupleElectronTauWeight::NumPileupIntP1() const { return m_NumPileupIntP1; }

void TupleElectronTauWeight::set_NumTruePileUpIntP1(double NumTruePileUpIntP1_) { m_NumTruePileUpIntP1  =  NumTruePileUpIntP1_;}
double TupleElectronTauWeight::NumTruePileUpIntP1() const { return m_NumTruePileUpIntP1; }
