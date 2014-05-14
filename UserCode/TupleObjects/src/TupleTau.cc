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
LorentzVector TupleTau::p4() const  { return m_p4; }


void TupleTau::set_corrected_p4(LorentzVector v4_, int decayMode_)
{

  double v4_sf = 1.0;

  ///////////////////
  // corrections from
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingSummer2013
  // #TauES_and_decay_mode_scale_facto

// one prong, 1 pi0
if(decayMode_==1)   v4_sf = (1.025 + 0.001 * std::min(std::max(v4_.pt()-45.,0.),10.));

// 3 prong, 0 to N pi0
if(decayMode_>=10 && decayMode_<=14)   v4_sf = (1.012 + 0.001 * std::min(std::max(v4_.pt()-32.,0.),18.));




  m_corrected_p4 = v4_*v4_sf;


}



LorentzVector TupleTau::corrected_p4() const  { return m_corrected_p4; }


void TupleTau::set_pdgId(int pdgId_) { m_pdgId = pdgId_;}
int TupleTau::pdgId() const  { return m_pdgId; }

void TupleTau::set_charge(int charge_) { m_charge = charge_;}
int TupleTau::charge() const  { return m_charge; }

void TupleTau::set_decayMode(int decayMode_) { m_decayMode = decayMode_;}
int TupleTau::decayMode() const  { return m_decayMode; }
