#include "UserCode/TupleObjects/interface/TupleMuon.h"


TupleMuon::TupleMuon()
{
  Pt = NAN;
  LorentzVector p4(NAN,NAN,NAN,NAN);
  bool isGlobalMuon = FALSE;
  bool isTightMuon = FALSE;
  bool isLooseMuon = FALSE;
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
