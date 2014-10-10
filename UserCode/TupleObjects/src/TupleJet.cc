#include "UserCode/TupleObjects/interface/TupleJet.h"


TupleJet::TupleJet()
{

  m_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_JecShift = NAN;
  m_passesPUjetIDLoose = 0;
  m_passesPFjetIDLoose = 0;
  m_combinedSecondaryVertexBJetTags = NAN;
  m_partonFlavour = -999;
  m_isBtagged = 0;

}



void TupleJet::set_isBtagged(bool isBtagged_) { m_isBtagged = isBtagged_;}
bool TupleJet::isBtagged() const  { return m_isBtagged; }


void TupleJet::set_p4(LorentzVector v4_) { m_p4 = v4_;}
LorentzVector TupleJet::p4() const  { return m_p4; }


void TupleJet::set_partonFlavour(int partonFlavour_) { m_partonFlavour = partonFlavour_;}
int TupleJet::partonFlavour() const  { return m_partonFlavour; }


void TupleJet::set_combinedSecondaryVertexBJetTags(double combinedSecondaryVertexBJetTags_) { m_combinedSecondaryVertexBJetTags = combinedSecondaryVertexBJetTags_;}
double TupleJet::combinedSecondaryVertexBJetTags() const  { return m_combinedSecondaryVertexBJetTags; }



void TupleJet::set_passesPUjetIDLoose(bool passesPUjetIDLoose_) { m_passesPUjetIDLoose = passesPUjetIDLoose_;}
bool TupleJet::passesPUjetIDLoose() const  { return m_passesPUjetIDLoose; }

void TupleJet::set_passesPFjetIDLoose(bool passesPFjetIDLoose_) { m_passesPFjetIDLoose = passesPFjetIDLoose_;}
bool TupleJet::passesPFjetIDLoose() const  { return m_passesPFjetIDLoose; }

void TupleJet::set_JecShift(double JecShift_) { m_JecShift = JecShift_;}
double TupleJet::JecShift() const  { return m_JecShift; }
