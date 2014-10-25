#include "UserCode/TupleObjects/interface/TupleGen.h"


TupleGen::TupleGen()
{

  m_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_pdgId = -999;
  m_pdgIdmother = -999;
  m_status = -999;
}

///////////////////
// number of strips
/////////////////////


void TupleGen::set_p4(LorentzVector v4_) { m_p4 = v4_;}
LorentzVector TupleGen::p4() const  { return m_p4; }

void TupleGen::set_pdgIdmother(int pdgIdmother_) { m_pdgIdmother = pdgIdmother_;}
int TupleGen::pdgIdmother() const  { return m_pdgIdmother; }


void TupleGen::set_pdgId(int pdgId_) { m_pdgId = pdgId_;}
int TupleGen::pdgId() const  { return m_pdgId; }

void TupleGen::set_status(int status_) { m_status = status_;}
int TupleGen::status() const  { return m_status; }
