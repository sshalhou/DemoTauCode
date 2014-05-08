#include "UserCode/TupleObjects/interface/TupleMuon.h"


TupleMuon::TupleMuon()
{
  Pt = NAN;
  LorentzVector p4(NAN,NAN,NAN,NAN);
  isGlobalMuon = 0;
  isTightMuon = 0;
  isLooseMuon = 0;
  sumChargedParticlePt = NAN;
  sumPhotonEt = NAN;
  sumNeutralHadronEt = NAN;
  sumPUPt = NAN;
  relativeIso = NAN;
}

void TupleMuon::set_Pt(float Pt_)
{
  Pt = Pt_;

}

void TupleMuon::set_p4(LorentzVector v4_)
{
  p4 = v4_;

}


void TupleMuon::set_isGlobalMuon(bool isGlobalMuon_)
{
  isGlobalMuon = isGlobalMuon_;

}


void TupleMuon::set_isTightMuon(bool isTightMuon_)
{
  isTightMuon = isTightMuon_;

}

void TupleMuon::set_isLooseMuon(bool isLooseMuon_)
{
  isLooseMuon = isLooseMuon_;

}

void TupleMuon::set_sumChargedParticlePt (double sumChargedParticlePt_)
{
  sumChargedParticlePt  = sumChargedParticlePt_;

}

void TupleMuon::set_sumPhotonEt (double sumPhotonEt_)
{
  sumPhotonEt = sumPhotonEt_;

}

void TupleMuon::set_sumNeutralHadronEt (double sumNeutralHadronEt_)
{
  sumNeutralHadronEt = sumNeutralHadronEt_;

}

void TupleMuon::set_sumPUPt (double sumPUPt_)
{
  sumPUPt = sumPUPt_;

}

void TupleMuon::set_relativeIso (double relativeIso_)
{
  relativeIso = relativeIso_;

}

//////////////////

float TupleMuon::get_Pt()
{
  return Pt;

}

LorentzVector TupleMuon::get_p4()
{
  return p4;

}


bool TupleMuon::get_isGlobalMuon()
{
  return isGlobalMuon;

}


bool TupleMuon::get_isTightMuon()
{
  return isTightMuon;

}

bool TupleMuon::get_isLooseMuon()
{
  return isLooseMuon;

}


double TupleMuon::get_sumChargedParticlePt()
{
  return sumChargedParticlePt;

}

double TupleMuon::get_sumPhotonEt()
{
  return sumPhotonEt;

}

double TupleMuon::get_sumNeutralHadronEt()
{
  return sumNeutralHadronEt;

}

double TupleMuon::get_sumPUPt()
{
  return sumPUPt;

}

double TupleMuon::get_relativeIso()
{
  return relativeIso;

}
