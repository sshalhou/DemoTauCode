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
  m_correctedSVFitMass = NAN;
  m_TransverseMass = NAN;
  // probably better to store the vectors later on
  m_mvaMETraw = NAN;
  m_mvaMET = NAN;
  m_mvaMETphiRaw = NAN;
  m_mvaMETphi = NAN;
  m_MAX = -999;

}

// temp MAX pt check
void TupleMuonTau::set_MAX(int MAX_) { m_MAX = MAX_;}
int TupleMuonTau::MAX() const  { return m_MAX; }

void TupleMuonTau::set_mvaMETraw(double mvaMETraw_) { m_mvaMETraw = mvaMETraw_;}
double TupleMuonTau::mvaMETraw() const  { return m_mvaMETraw; }

void TupleMuonTau::set_mvaMET(double mvaMET_) { m_mvaMET = mvaMET_;}
double TupleMuonTau::mvaMET() const  { return m_mvaMET; }

void TupleMuonTau::set_mvaMETphiRaw(double mvaMETphiRaw_) { m_mvaMETphiRaw = mvaMETphiRaw_;}
double TupleMuonTau::mvaMETphiRaw() const  { return m_mvaMETphiRaw; }

void TupleMuonTau::set_mvaMETphi(double mvaMETphi_) { m_mvaMETphi = mvaMETphi_;}
double TupleMuonTau::mvaMETphi() const  { return m_mvaMETphi; }

void TupleMuonTau::set_TransverseMass(double TransverseMass_) { m_TransverseMass = TransverseMass_;}
double TupleMuonTau::TransverseMass() const  { return m_TransverseMass; }

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

void TupleMuonTau::set_correctedSVFitMass(double correctedSVFitMass_) { m_correctedSVFitMass = correctedSVFitMass_;}
double TupleMuonTau::correctedSVFitMass() const  { return m_correctedSVFitMass; }
