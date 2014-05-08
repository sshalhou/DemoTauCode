#include "UserCode/TupleObjects/interface/TupleMuon.h"


TupleMuon::TupleMuon()
{
  Pt = NAN;

}

void TupleMuon::set_Pt(float Pt_)
{
  Pt = Pt_;

}

float TupleMuon::get_Pt()
{
  return Pt;

}
