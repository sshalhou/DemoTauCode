#include "UserCode/TupleObjects/interface/TupleMuon.h"


TupleMuon::TupleMuon()
{
  m_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_pfP4.SetXYZT(NAN,NAN,NAN,NAN);
  m_isGlobalMuon = 0;
  m_isTightMuon = 0;
  m_isLooseMuon = 0;
  m_sumChargedParticlePt_DR4 = NAN;
  m_sumPhotonEt_DR4 = NAN;
  m_sumNeutralHadronEt_DR4 = NAN;
  m_sumPUPt_DR4 = NAN;
  m_relativeIso_DR4 = NAN;
  m_sumChargedParticlePt_DR3 = NAN;
  m_sumPhotonEt_DR3 = NAN;
  m_sumNeutralHadronEt_DR3 = NAN;
  m_sumPUPt_DR3 = NAN;
  m_relativeIso_DR3 = NAN;
  m_isPFIsolationValid = 0;
  m_charge = -999;
  m_pdgId = -999;
  m_normalizedChi2 = NAN;
  m_numberOfValidMuonHits = -999;
  m_numberOfMatchedStations = -999;
  m_numberOfValidPixelHits = -999;
  m_trackerLayersWithMeasurement = -999;
  m_dB = NAN; // aka d0
  m_dz = NAN;
  m_dxy = NAN;
}






void TupleMuon::set_normalizedChi2(double normalizedChi2_){ m_normalizedChi2 = normalizedChi2_;}
void TupleMuon::set_numberOfValidMuonHits(int numberOfValidMuonHits_){ m_numberOfValidMuonHits = numberOfValidMuonHits_;}
void TupleMuon::set_numberOfMatchedStations(int numberOfMatchedStations_)
{
   m_numberOfMatchedStations = numberOfMatchedStations_;
 }
void TupleMuon::set_numberOfValidPixelHits(int numberOfValidPixelHits_){ m_numberOfValidPixelHits = numberOfValidPixelHits_;}
void TupleMuon::set_trackerLayersWithMeasurement(int trackerLayersWithMeasurement_)
{
   m_trackerLayersWithMeasurement = trackerLayersWithMeasurement_;
}
void TupleMuon::set_dB(double dB_){ m_dB = dB_;}
void TupleMuon::set_dz(double dz_){ m_dz = dz_;}
void TupleMuon::set_dxy(double dxy_){ m_dxy = dxy_;}








void TupleMuon::set_p4(LorentzVector v4_)
{
  m_p4 = v4_;

}

void TupleMuon::set_pfP4(LorentzVector v4_)
{
  m_pfP4 = v4_;

}


void TupleMuon::set_isGlobalMuon(bool isGlobalMuon_)
{
  m_isGlobalMuon = isGlobalMuon_;

}


void TupleMuon::set_isTightMuon(bool isTightMuon_)
{
  m_isTightMuon = isTightMuon_;

}

void TupleMuon::set_isLooseMuon(bool isLooseMuon_)
{
  m_isLooseMuon = isLooseMuon_;

}

void TupleMuon::set_sumChargedParticlePt_DR4 (double sumChargedParticlePt_)
{
  m_sumChargedParticlePt_DR4  = sumChargedParticlePt_;

}

void TupleMuon::set_sumPhotonEt_DR4 (double sumPhotonEt_)
{
  m_sumPhotonEt_DR4 = sumPhotonEt_;

}

void TupleMuon::set_sumNeutralHadronEt_DR4 (double sumNeutralHadronEt_)
{
  m_sumNeutralHadronEt_DR4 = sumNeutralHadronEt_;

}

void TupleMuon::set_sumPUPt_DR4 (double sumPUPt_)
{
  m_sumPUPt_DR4 = sumPUPt_;

}

void TupleMuon::set_relativeIso_DR4 (double relativeIso_)
{
  m_relativeIso_DR4 = relativeIso_;

}



void TupleMuon::set_sumChargedParticlePt_DR3 (double sumChargedParticlePt_)
{
  m_sumChargedParticlePt_DR3  = sumChargedParticlePt_;

}

void TupleMuon::set_sumPhotonEt_DR3 (double sumPhotonEt_)
{
  m_sumPhotonEt_DR3 = sumPhotonEt_;

}

void TupleMuon::set_sumNeutralHadronEt_DR3 (double sumNeutralHadronEt_)
{
  m_sumNeutralHadronEt_DR3 = sumNeutralHadronEt_;

}

void TupleMuon::set_sumPUPt_DR3 (double sumPUPt_)
{
  m_sumPUPt_DR3 = sumPUPt_;

}

void TupleMuon::set_relativeIso_DR3 (double relativeIso_)
{
  m_relativeIso_DR3 = relativeIso_;

}


void TupleMuon::set_isPFIsolationValid (bool isPFIsolationValid_)
{
  m_isPFIsolationValid = isPFIsolationValid_;
}

void TupleMuon::set_charge (int charge_)
{
  m_charge = charge_;
}

void TupleMuon::set_pdgId (int pdgId_)
{
  m_pdgId = pdgId_;
}



//////////////////


LorentzVector TupleMuon::p4()
{
  return m_p4;

}

LorentzVector TupleMuon::pfP4()
{
  return m_pfP4;

}


bool TupleMuon::isGlobalMuon()
{
  return m_isGlobalMuon;

}


bool TupleMuon::isTightMuon()
{
  return m_isTightMuon;

}

bool TupleMuon::isLooseMuon()
{
  return m_isLooseMuon;

}


double TupleMuon::sumChargedParticlePt_DR4()
{
  return m_sumChargedParticlePt_DR4;

}

double TupleMuon::sumPhotonEt_DR4()
{
  return m_sumPhotonEt_DR4;

}

double TupleMuon::sumNeutralHadronEt_DR4()
{
  return m_sumNeutralHadronEt_DR4;

}

double TupleMuon::sumPUPt_DR4()
{
  return m_sumPUPt_DR4;

}

double TupleMuon::relativeIso_DR4()
{
  return m_relativeIso_DR4;

}




double TupleMuon::sumChargedParticlePt_DR3()
{
  return m_sumChargedParticlePt_DR3;

}

double TupleMuon::sumPhotonEt_DR3()
{
  return m_sumPhotonEt_DR3;

}

double TupleMuon::sumNeutralHadronEt_DR3()
{
  return m_sumNeutralHadronEt_DR3;

}

double TupleMuon::sumPUPt_DR3()
{
  return m_sumPUPt_DR3;

}

double TupleMuon::relativeIso_DR3()
{
  return m_relativeIso_DR3;

}


bool TupleMuon::isPFIsolationValid()
{
  return m_isPFIsolationValid;
}

int TupleMuon::charge()
{
  return m_charge;
}

int TupleMuon::pdgId()
{
  return m_pdgId;
}

double TupleMuon::normalizedChi2(){ return m_normalizedChi2; }
int TupleMuon::numberOfValidMuonHits(){ return m_numberOfValidMuonHits = numberOfValidMuonHits_; }
int TupleMuon::numberOfMatchedStations(){ return m_numberOfMatchedStations = numberOfMatchedStations_;}
int TupleMuon::numberOfValidPixelHits(){ return m_numberOfValidPixelHits = numberOfValidPixelHits_;}
int TupleMuon::trackerLayersWithMeasurement(){ return m_trackerLayersWithMeasurement;}
double TupleMuon::dB(){ return m_dB;}
double TupleMuon::dz(){ return m_dz;}
double TupleMuon::dxy(){ return m_dxy;}
