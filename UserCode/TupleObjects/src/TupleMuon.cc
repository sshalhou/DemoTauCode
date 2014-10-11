#include "UserCode/TupleObjects/interface/TupleMuon.h"


TupleMuon::TupleMuon()
{
  m_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_genP4.SetXYZT(NAN,NAN,NAN,NAN);
  m_pfP4.SetXYZT(NAN,NAN,NAN,NAN);
  m_isGlobalMuon = 0;
  m_isTightMuon = 0;
  m_isPFMuon = 0;
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
  m_PFpdgId = -999;
  m_GENpdgId = -999;
  m_normalizedChi2 = NAN;
  m_numberOfValidMuonHits = -999;
  m_numberOfMatchedStations = -999;
  m_numberOfValidPixelHits = -999;
  m_trackerLayersWithMeasurement = -999;
  m_dB = NAN; // aka d0
  m_dz = NAN;
  m_dxy = NAN;
  m_passFullId = 0;

  m_has_HltMatchMu17 =  0;
  m_has_HltMatchMu18 =  0;
  m_has_HltMatchMu24 =  0;
  m_isTriLeptonVetoCandidate = 0;

}


///////////////////
// isTriLeptonVetoCandidate
////////////////////

void TupleMuon::set_isTriLeptonVetoCandidate(bool isTriLeptonVetoCandidate_) { m_isTriLeptonVetoCandidate = isTriLeptonVetoCandidate_;}
bool TupleMuon::isTriLeptonVetoCandidate() const { return m_isTriLeptonVetoCandidate; }

//////////////////
// has_HltMatchMu17
//////////////////
void TupleMuon::set_has_HltMatchMu17(bool has_HltMatchMu17_) { m_has_HltMatchMu17 = has_HltMatchMu17_;}
bool TupleMuon::has_HltMatchMu17() const { return m_has_HltMatchMu17; }


//////////////////
// has_HltMatchMu18
//////////////////
void TupleMuon::set_has_HltMatchMu18(bool has_HltMatchMu18_) { m_has_HltMatchMu18 = has_HltMatchMu18_;}
bool TupleMuon::has_HltMatchMu18() const { return m_has_HltMatchMu18; }


//////////////////
// has_HltMatchMu24
//////////////////
void TupleMuon::set_has_HltMatchMu24(bool has_HltMatchMu24_) { m_has_HltMatchMu24 = has_HltMatchMu24_;}
bool TupleMuon::has_HltMatchMu24() const { return m_has_HltMatchMu24; }



// will set this in TupleMuonProducer, since we can track all cuts
// more easily when calling the producer
void TupleMuon::set_passFullId(bool passFullId_) { m_passFullId = passFullId_;}
bool TupleMuon::passFullId() const  { return m_passFullId; }


void TupleMuon::set_genP4(LorentzVector v4_) { m_genP4 = v4_;}
LorentzVector TupleMuon::genP4() const  { return m_genP4; }



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

void TupleMuon::set_isPFMuon(bool isPFMuon_)
{
  m_isPFMuon = isPFMuon_;

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

void TupleMuon::set_PFpdgId (int PFpdgId_)
{
  m_PFpdgId = PFpdgId_;
}

void TupleMuon::set_GENpdgId (int GENpdgId_)
{
  m_GENpdgId = GENpdgId_;
}


//////////////////


LorentzVector TupleMuon::p4() const
{
  return m_p4;

}

LorentzVector TupleMuon::pfP4() const
{
  return m_pfP4;

}


bool TupleMuon::isGlobalMuon() const
{
  return m_isGlobalMuon;

}


bool TupleMuon::isTightMuon() const
{
  return m_isTightMuon;

}

bool TupleMuon::isPFMuon() const
{
  return m_isPFMuon;

}

bool TupleMuon::isLooseMuon() const
{
  return m_isLooseMuon;

}


double TupleMuon::sumChargedParticlePt_DR4() const
{
  return m_sumChargedParticlePt_DR4;

}

double TupleMuon::sumPhotonEt_DR4() const
{
  return m_sumPhotonEt_DR4;

}

double TupleMuon::sumNeutralHadronEt_DR4() const
{
  return m_sumNeutralHadronEt_DR4;

}

double TupleMuon::sumPUPt_DR4() const
{
  return m_sumPUPt_DR4;

}

double TupleMuon::relativeIso_DR4() const
{
  return m_relativeIso_DR4;

}




double TupleMuon::sumChargedParticlePt_DR3() const
{
  return m_sumChargedParticlePt_DR3;

}

double TupleMuon::sumPhotonEt_DR3() const
{
  return m_sumPhotonEt_DR3;

}

double TupleMuon::sumNeutralHadronEt_DR3() const
{
  return m_sumNeutralHadronEt_DR3;

}

double TupleMuon::sumPUPt_DR3() const
{
  return m_sumPUPt_DR3;

}

double TupleMuon::relativeIso_DR3() const
{
  return m_relativeIso_DR3;

}


bool TupleMuon::isPFIsolationValid() const
{
  return m_isPFIsolationValid;
}

int TupleMuon::charge() const
{
  return m_charge;
}

int TupleMuon::PFpdgId() const
{
  return m_PFpdgId;
}

int TupleMuon::GENpdgId() const
{
  return m_GENpdgId;
}


double TupleMuon::normalizedChi2() const { return m_normalizedChi2; }
int TupleMuon::numberOfValidMuonHits() const { return m_numberOfValidMuonHits; }
int TupleMuon::numberOfMatchedStations() const { return m_numberOfMatchedStations;}
int TupleMuon::numberOfValidPixelHits() const { return m_numberOfValidPixelHits;}
int TupleMuon::trackerLayersWithMeasurement() const { return m_trackerLayersWithMeasurement;}
double TupleMuon::dB() const { return m_dB;}
double TupleMuon::dz() const { return m_dz;}
double TupleMuon::dxy() const { return m_dxy;}
