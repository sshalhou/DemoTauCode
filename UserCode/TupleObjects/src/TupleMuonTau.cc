#include "UserCode/TupleObjects/interface/TupleMuonTau.h"


TupleMuonTau::TupleMuonTau()
{
  m_p4.SetXYZT(NAN,NAN,NAN,NAN);

}

void TupleMuonTau::set_p4(LorentzVector v4_) { m_p4 = v4_;}
LorentzVector TupleMuonTau::p4() const  { return m_p4; }
