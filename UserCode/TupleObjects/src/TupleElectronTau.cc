#include "UserCode/TupleObjects/interface/TupleElectronTau.h"
#include "DataFormats/Math/interface/deltaR.h"

TupleElectronTau::TupleElectronTau()
{
  m_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_corrected_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_electronIndex = -999;
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
  m_MAX = 0;

}

// temp MAX pt check
void TupleElectronTau::set_MAX(int MAX_) { m_MAX = MAX_;}
int TupleElectronTau::MAX() const  { return m_MAX; }

void TupleElectronTau::set_mvaMETraw(double mvaMETraw_) { m_mvaMETraw = mvaMETraw_;}
double TupleElectronTau::mvaMETraw() const  { return m_mvaMETraw; }

void TupleElectronTau::set_mvaMET(double mvaMET_) { m_mvaMET = mvaMET_;}
double TupleElectronTau::mvaMET() const  { return m_mvaMET; }

void TupleElectronTau::set_mvaMETphiRaw(double mvaMETphiRaw_) { m_mvaMETphiRaw = mvaMETphiRaw_;}
double TupleElectronTau::mvaMETphiRaw() const  { return m_mvaMETphiRaw; }

void TupleElectronTau::set_mvaMETphi(double mvaMETphi_) { m_mvaMETphi = mvaMETphi_;}
double TupleElectronTau::mvaMETphi() const  { return m_mvaMETphi; }

void TupleElectronTau::set_TransverseMass(double TransverseMass_) { m_TransverseMass = TransverseMass_;}
double TupleElectronTau::TransverseMass() const  { return m_TransverseMass; }

void TupleElectronTau::set_p4(LorentzVector v4_) { m_p4 = v4_;}
LorentzVector TupleElectronTau::p4() const  { return m_p4; }

void TupleElectronTau::set_corrected_p4(LorentzVector v4_) { m_corrected_p4 = v4_;}
LorentzVector TupleElectronTau::corrected_p4() const  { return m_corrected_p4; }

void TupleElectronTau::set_sumCharge(int chargeA_, int chargeB_) { m_sumCharge = (chargeA_ + chargeB_);}
int TupleElectronTau::sumCharge() const  { return m_sumCharge; }

void TupleElectronTau::set_electronIndex(int electronIndex_) { m_electronIndex = electronIndex_;}
int TupleElectronTau::electronIndex() const  { return m_electronIndex; }

void TupleElectronTau::set_tauIndex(int tauIndex_) { m_tauIndex = tauIndex_;}
int TupleElectronTau::tauIndex() const  { return m_tauIndex; }

void TupleElectronTau::set_scalarSumPt(LorentzVector A_, LorentzVector B_) { m_scalarSumPt = (A_.pt()+B_.pt());}
double TupleElectronTau::scalarSumPt() const  { return m_scalarSumPt; }

void TupleElectronTau::set_DR(LorentzVector A_, LorentzVector B_) { m_DR = deltaR(A_, B_);}
double TupleElectronTau::DR() const  { return m_DR; }

void TupleElectronTau::set_correctedSVFitMass(double correctedSVFitMass_) { m_correctedSVFitMass = correctedSVFitMass_;}
double TupleElectronTau::correctedSVFitMass() const  { return m_correctedSVFitMass; }
