#include "UserCode/TupleObjects/interface/TupleTau.h"


TupleTau::TupleTau()
{
  m_p4.SetXYZT(NAN,NAN,NAN,NAN);

}













void TupleTau::set_p4(LorentzVector v4_) { m_p4 = v4_;}

LorentzVector TupleTau::p4() { return m_p4; }
