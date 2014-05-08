#include "UserCode/TupleObjects/interface/TupleMuon.h"


TupleMuon::TupleMuon()
{
  Pt = NAN;
  LorentzVector p4(NAN,NAN,NAN,NAN);
}

void TupleMuon::set_Pt(float Pt_)
{
  Pt = Pt_;

}

void TupleMuon::set_p4(LorentzVector v4_)
{
  p4 = v4_;

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
