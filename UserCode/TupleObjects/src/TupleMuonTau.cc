#include "UserCode/TupleObjects/interface/TupleMuonTau.h"
#include "DataFormats/Math/interface/deltaR.h"

TupleMuonTau::TupleMuonTau()
{
  m_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_corrected_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_muonIndex = -999;
  m_tauIndex = -999;
  m_scalarSumPt = NAN;
  m_DR = NAN;
  m_sumCharge = -999;


}

void TupleMuonTau::set_p4(LorentzVector v4_) { m_p4 = v4_;}
LorentzVector TupleMuonTau::p4() const  { return m_p4; }

void TupleMuonTau::set_corrected_p4(LorentzVector v4_) { m_corrected_p4 = v4_;}
LorentzVector TupleMuonTau::corrected_p4() const  { return m_corrected_p4; }

void TupleMuonTau::set_sumCharge(int chargeA_, int chargeB_) { m_sumCharge = (chargeA_ + chargeB_);}
int TupleMuonTau::sumCharge() const  { return m_sumCharge; }

void TupleMuonTau::set_muonIndex(int muonIndex_) { m_muonIndex = muonIndex_;}
int TupleMuonTau::muonIndex() const  { return m_muonIndex; }

void TupleMuonTau::set_tauIndex(int tauIndex_) { m_tauIndex = tauIndex_;}
int TupleMuonTau::tauIndex() const  { return m_tauIndex; }

void TupleMuonTau::set_scalarSumPt(LorentzVector A_, LorentzVector B_) { m_scalarSumPt = (A_.pt()+B_.pt());}
double TupleMuonTau::scalarSumPt() const  { return m_scalarSumPt; }

void TupleMuonTau::set_DR(LorentzVector A_, LorentzVector B_) { m_DR = deltaR(A_, B_);}
double TupleMuonTau::DR() const  { return m_DR; }
