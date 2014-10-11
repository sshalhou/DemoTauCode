#include "UserCode/TupleObjects/interface/TupleMuonTauVetoes.h"


TupleMuonTauVetoes::TupleMuonTauVetoes()
{


  m_passesThirdLeptonVeto = 0;
  m_passesSecondLeptonVeto = 0;

}

///////////////////
// functions
/////////////////////


void TupleMuonTauVetoes::set_passesThirdLeptonVeto(bool passesThirdLeptonVeto_) { m_passesThirdLeptonVeto = passesThirdLeptonVeto_;}
bool TupleMuonTauVetoes::passesThirdLeptonVeto() const  { return m_passesThirdLeptonVeto; }


void TupleMuonTauVetoes::set_passesSecondLeptonVeto(bool passesSecondLeptonVeto_) { m_passesSecondLeptonVeto = passesSecondLeptonVeto_;}
bool TupleMuonTauVetoes::passesSecondLeptonVeto() const  { return m_passesSecondLeptonVeto; }
