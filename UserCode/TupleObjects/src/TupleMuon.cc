#include "UserCode/TupleObjects/interface/TupleMuon.h"


TupleMuon::TupleMuon()
{
  m_LorentzVector p4(NAN,NAN,NAN,NAN);
  m_isGlobalMuon = 0;
  m_isTightMuon = 0;
  m_isLooseMuon = 0;
  m_sumChargedParticlePt = NAN;
  m_sumPhotonEt = NAN;
  m_sumNeutralHadronEt = NAN;
  m_sumPUPt = NAN;
  m_relativeIso = NAN;
}



void TupleMuon::set_p4(LorentzVector v4_)
{
  m_p4 = v4_;

}


void TupleMuon::set_isGlobalMuon(bool isGlobalMuon_)
{
  m_isGlobalMuon = isGlobalMuon_;

}


void TupleMuon::set_isTightMuon(bool isTightMuon_)
{
  m_isTightMuon = isTightMuon_;

}

void TupleMuon::set_isLooseMuon(bool isLooseMuon_)
{
  m_isLooseMuon = isLooseMuon_;

}

void TupleMuon::set_sumChargedParticlePt (double sumChargedParticlePt_)
{
  m_sumChargedParticlePt  = sumChargedParticlePt_;

}

void TupleMuon::set_sumPhotonEt (double sumPhotonEt_)
{
  m_sumPhotonEt = sumPhotonEt_;

}

void TupleMuon::set_sumNeutralHadronEt (double sumNeutralHadronEt_)
{
  m_sumNeutralHadronEt = sumNeutralHadronEt_;

}

void TupleMuon::set_sumPUPt (double sumPUPt_)
{
  m_sumPUPt = sumPUPt_;

}

void TupleMuon::set_relativeIso (double relativeIso_)
{
  m_relativeIso = relativeIso_;

}

//////////////////


LorentzVector TupleMuon::p4()
{
  return m_p4;

}


bool TupleMuon::isGlobalMuon()
{
  return m_isGlobalMuon;

}


bool TupleMuon::isTightMuon()
{
  return m_isTightMuon;

}

bool TupleMuon::isLooseMuon()
{
  return m_isLooseMuon;

}


double TupleMuon::sumChargedParticlePt()
{
  return m_sumChargedParticlePt;

}

double TupleMuon::sumPhotonEt()
{
  return m_sumPhotonEt;

}

double TupleMuon::sumNeutralHadronEt()
{
  return m_sumNeutralHadronEt;

}

double TupleMuon::sumPUPt()
{
  return m_sumPUPt;

}

double TupleMuon::relativeIso()
{
  return m_relativeIso;

}
