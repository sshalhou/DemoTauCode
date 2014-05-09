#include "UserCode/TupleObjects/interface/TupleMuon.h"


TupleMuon::TupleMuon()
{
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


LorentzVector TupleMuon::p4()
{
  return p4;

}


bool TupleMuon::isGlobalMuon()
{
  return isGlobalMuon;

}


bool TupleMuon::isTightMuon()
{
  return isTightMuon;

}

bool TupleMuon::isLooseMuon()
{
  return isLooseMuon;

}


double TupleMuon::sumChargedParticlePt()
{
  return sumChargedParticlePt;

}

double TupleMuon::sumPhotonEt()
{
  return sumPhotonEt;

}

double TupleMuon::sumNeutralHadronEt()
{
  return sumNeutralHadronEt;

}

double TupleMuon::sumPUPt()
{
  return sumPUPt;

}

double TupleMuon::relativeIso()
{
  return relativeIso;

}
