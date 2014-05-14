#include "UserCode/TupleObjects/interface/TupleTau.h"


TupleTau::TupleTau()
{
  p4.SetXYZT(NAN,NAN,NAN,NAN);

}













void TupleTau::set_p4(LorentzVector v4_) { p4 = v4_;}

LorentzVector TupleTau::p4() { return p4; }
