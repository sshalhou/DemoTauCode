#include "UserCode/TupleObjects/interface/TupleElectronTauWeight.h"
#include "TMath.h"

TupleElectronTauWeight::TupleElectronTauWeight()
{
  m_puWeight = NAN;

}

//Setting Weights


////////////////////////
// pile-up reweight   //
////////////////////////

void TupleElectronTauWeight::set_puWeight(double puWeight_) { m_puWeight = puWeight_;}
double TupleElectronTauWeight::puWeight() const { return m_puWeight; }
