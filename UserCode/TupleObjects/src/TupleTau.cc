#include "UserCode/TupleObjects/interface/TupleTau.h"


TupleTau::TupleTau()
{
  m_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_corrected_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_pdgId = -999;
  m_charge = -999;
  m_decayMode = -999;

}

void TupleTau::set_p4(LorentzVector v4_) { m_p4 = v4_;}
LorentzVector TupleTau::p4() { return m_p4; }


void TupleTau::set_corrected_p4(LorentzVector v4_) { m_corrected_p4 = v4_;}
LorentzVector TupleTau::corrected_p4() { return m_corrected_p4; }


void TupleTau::set_pdgId(int pdgId_) { m_pdgId = pdgId_;}
int TupleTau::() { return m_pdgId; }

void TupleTau::set_(int charge_) { m_charge = charge_;}
int TupleTau::() { return m_charge; }

void TupleTau::set_decayMode(int decayMode_) { m_decayMode = decayMode_;}
int TupleTau::() { return m_decayMode; }
