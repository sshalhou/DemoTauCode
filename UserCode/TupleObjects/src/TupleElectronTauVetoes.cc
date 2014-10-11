#include "UserCode/TupleObjects/interface/TupleElectronTauVetoes.h"


TupleElectronTauVetoes::TupleElectronTauVetoes()
{


  m_passesThirdLeptonVeto = 0;
  m_passesSecondLeptonVeto = 0;

}

///////////////////
// functions
/////////////////////


void TupleElectronTauVetoes::set_passesThirdLeptonVeto(bool passesThirdLeptonVeto_) { m_passesThirdLeptonVeto = passesThirdLeptonVeto_;}
bool TupleElectronTauVetoes::passesThirdLeptonVeto() const  { return m_passesThirdLeptonVeto; }


void TupleElectronTauVetoes::set_passesSecondLeptonVeto(bool passesSecondLeptonVeto_) { m_passesSecondLeptonVeto = passesSecondLeptonVeto_;}
bool TupleElectronTauVetoes::passesSecondLeptonVeto() const  { return m_passesSecondLeptonVeto; }
