#include "UserCode/TupleObjects/interface/TupleMuonTauWeight.h"
#include "TMath.h"

TupleMuonTauWeight::TupleMuonTauWeight()
{
  m_puWeight = NAN;

}

//Setting Weights


////////////////////////
// pile-up reweight   //
////////////////////////

void TupleMuonTauWeight::set_puWeight(double puWeight_) { m_puWeight = puWeight_;}
double TupleMuonTauWeight::puWeight() const { return m_puWeight; }
