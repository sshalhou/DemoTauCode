#include "UserCode/TupleObjects/interface/TupleElectron.h"


TupleElectron::TupleElectron()
{
  m_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_genP4.SetXYZT(NAN,NAN,NAN,NAN);
  m_pfP4.SetXYZT(NAN,NAN,NAN,NAN);
  m_charge = -999;
  m_PFpdgId = -999;
  m_GENpdgId = -999;
  m_numberOfMissingInnerHits = -999;
  m_passConversionVeto = 0;
  m_dz = NAN;
  m_dxy = NAN;
  m_dB = NAN;
  m_SuperClusterEta = NAN;
  m_mvaTrigV0 = NAN;
  m_mvaTrigNoIPV0 = NAN;
  m_mvaNonTrigV0 = NAN;
  m_pass_tight_mvaNonTrigV0 = 0;
  m_passFullId = 0;
  m_chargedHadronIso = NAN;
  m_photonIso = NAN;
  m_neutralHadronIso = NAN;
  m_puChargedHadronIso = NAN;
  m_relativeIso = NAN;
  m_isEB = 0;
  m_isEE = 0;
  m_isEBEEGap = 0;
  m_isEBEtaGap = 0;
  m_isEBPhiGap = 0;
  m_isEEDeeGap = 0;
  m_isEERingGap = 0;
  m_sigmaEtaEta = NAN;
  m_sigmaIetaIeta = NAN;
  m_sigmaIphiIphi = NAN;
  m_has_HltMatchEle20 =  0;
  m_has_HltMatchEle22 =  0;
  m_has_HltMatchEle27 =  0;
  m_isTriLeptonVetoCandidate = 0;


}

///////////////////
// isTriLeptonVetoCandidate
////////////////////

void TupleElectron::set_isTriLeptonVetoCandidate(bool isTriLeptonVetoCandidate_) { m_isTriLeptonVetoCandidate = isTriLeptonVetoCandidate_;}
bool TupleElectron::isTriLeptonVetoCandidate() const { return m_isTriLeptonVetoCandidate; }


//////////////////
// has_HltMatchEle20
//////////////////
void TupleElectron::set_has_HltMatchEle20(bool has_HltMatchEle20_) { m_has_HltMatchEle20 = has_HltMatchEle20_;}
bool TupleElectron::has_HltMatchEle20() const { return m_has_HltMatchEle20; }


//////////////////
// has_HltMatchEle22
//////////////////
void TupleElectron::set_has_HltMatchEle22(bool has_HltMatchEle22_) { m_has_HltMatchEle22 = has_HltMatchEle22_;}
bool TupleElectron::has_HltMatchEle22() const { return m_has_HltMatchEle22; }


//////////////////
// has_HltMatchEle27
//////////////////
void TupleElectron::set_has_HltMatchEle27(bool has_HltMatchEle27_) { m_has_HltMatchEle27 = has_HltMatchEle27_;}
bool TupleElectron::has_HltMatchEle27() const { return m_has_HltMatchEle27; }


//////////////////
// p4
//////////////////
void TupleElectron::set_p4(LorentzVector p4_) { m_p4 = p4_;}
LorentzVector TupleElectron::p4() const { return m_p4; }


//////////////////
// genP4
//////////////////
void TupleElectron::set_genP4(LorentzVector genP4_) { m_genP4 = genP4_;}
LorentzVector TupleElectron::genP4() const { return m_genP4; }


//////////////////
// pfP4
//////////////////
void TupleElectron::set_pfP4(LorentzVector pfP4_) { m_pfP4 = pfP4_;}
LorentzVector TupleElectron::pfP4() const { return m_pfP4; }


//////////////////
// charge
//////////////////
void TupleElectron::set_charge(int charge_) { m_charge = charge_;}
int TupleElectron::charge() const { return m_charge; }


//////////////////
// PFpdgId
//////////////////
void TupleElectron::set_PFpdgId(int PFpdgId_) { m_PFpdgId = PFpdgId_;}
int TupleElectron::PFpdgId() const { return m_PFpdgId; }


//////////////////
// GENpdgId
//////////////////
void TupleElectron::set_GENpdgId(int GENpdgId_) { m_GENpdgId = GENpdgId_;}
int TupleElectron::GENpdgId() const { return m_GENpdgId; }


//////////////////
// numberOfMissingInnerHits
//////////////////
void TupleElectron::set_numberOfMissingInnerHits(int numberOfMissingInnerHits_) { m_numberOfMissingInnerHits = numberOfMissingInnerHits_;}
int TupleElectron::numberOfMissingInnerHits() const { return m_numberOfMissingInnerHits; }


//////////////////
// passConversionVeto
//////////////////
void TupleElectron::set_passConversionVeto(bool passConversionVeto_) { m_passConversionVeto = passConversionVeto_;}
bool TupleElectron::passConversionVeto() const { return m_passConversionVeto; }


//////////////////
// dz
//////////////////
void TupleElectron::set_dz(double dz_) { m_dz = dz_;}
double TupleElectron::dz() const { return m_dz; }

//////////////////
// dB
//////////////////
void TupleElectron::set_dB(double dB_) { m_dB = dB_;}
double TupleElectron::dB() const { return m_dB; }

//////////////////
// dxy
//////////////////
void TupleElectron::set_dxy(double dxy_) { m_dxy= dxy_;}
double TupleElectron::dxy() const { return m_dxy; }


//////////////////
// SuperClusterEta
//////////////////
void TupleElectron::set_SuperClusterEta(double SuperClusterEta_) { m_SuperClusterEta = SuperClusterEta_;}
double TupleElectron::SuperClusterEta() const { return m_SuperClusterEta; }


//////////////////
// mvaTrigV0
//////////////////
void TupleElectron::set_mvaTrigV0(double mvaTrigV0_) { m_mvaTrigV0 = mvaTrigV0_;}
double TupleElectron::mvaTrigV0() const { return m_mvaTrigV0; }


//////////////////
// mvaTrigNoIPV0
//////////////////
void TupleElectron::set_mvaTrigNoIPV0(double mvaTrigNoIPV0_) { m_mvaTrigNoIPV0 = mvaTrigNoIPV0_;}
double TupleElectron::mvaTrigNoIPV0() const { return m_mvaTrigNoIPV0; }


//////////////////
// mvaNonTrigV0
//////////////////
void TupleElectron::set_mvaNonTrigV0(double mvaNonTrigV0_) { m_mvaNonTrigV0 = mvaNonTrigV0_;}
double TupleElectron::mvaNonTrigV0() const { return m_mvaNonTrigV0; }


//////////////////
// pass_tight_mvaNonTrigV0
//////////////////
void TupleElectron::set_pass_tight_mvaNonTrigV0(bool pass_tight_mvaNonTrigV0_) { m_pass_tight_mvaNonTrigV0 = pass_tight_mvaNonTrigV0_;}
bool TupleElectron::pass_tight_mvaNonTrigV0() const { return m_pass_tight_mvaNonTrigV0; }


//////////////////
// passFullId
//////////////////
void TupleElectron::set_passFullId(bool passFullId_) { m_passFullId = passFullId_;}
bool TupleElectron::passFullId() const { return m_passFullId; }


//////////////////
// chargedHadronIso
//////////////////
void TupleElectron::set_chargedHadronIso(double chargedHadronIso_) { m_chargedHadronIso = chargedHadronIso_;}
double TupleElectron::chargedHadronIso() const { return m_chargedHadronIso; }


//////////////////
// photonIso
//////////////////
void TupleElectron::set_photonIso(double photonIso_) { m_photonIso = photonIso_;}
double TupleElectron::photonIso() const { return m_photonIso; }


//////////////////
// neutralHadronIso
//////////////////
void TupleElectron::set_neutralHadronIso(double neutralHadronIso_) { m_neutralHadronIso = neutralHadronIso_;}
double TupleElectron::neutralHadronIso() const { return m_neutralHadronIso; }


//////////////////
// puChargedHadronIso
//////////////////
void TupleElectron::set_puChargedHadronIso(double puChargedHadronIso_) { m_puChargedHadronIso = puChargedHadronIso_;}
double TupleElectron::puChargedHadronIso() const { return m_puChargedHadronIso; }


//////////////////
// relativeIso
//////////////////
void TupleElectron::set_relativeIso(double relativeIso_) { m_relativeIso = relativeIso_;}
double TupleElectron::relativeIso() const { return m_relativeIso; }

//////////////////
// isEB
//////////////////
void TupleElectron::set_isEB(bool isEB_) { m_isEB = isEB_;}
bool TupleElectron::isEB() const { return m_isEB; }


//////////////////
// isEE
//////////////////
void TupleElectron::set_isEE(bool isEE_) { m_isEE = isEE_;}
bool TupleElectron::isEE() const { return m_isEE; }


//////////////////
// isEBEEGap
//////////////////
void TupleElectron::set_isEBEEGap(bool isEBEEGap_) { m_isEBEEGap = isEBEEGap_;}
bool TupleElectron::isEBEEGap() const { return m_isEBEEGap; }


//////////////////
// isEBEtaGap
//////////////////
void TupleElectron::set_isEBEtaGap(bool isEBEtaGap_) { m_isEBEtaGap = isEBEtaGap_;}
bool TupleElectron::isEBEtaGap() const { return m_isEBEtaGap; }


//////////////////
// isEBPhiGap
//////////////////
void TupleElectron::set_isEBPhiGap(bool isEBPhiGap_) { m_isEBPhiGap = isEBPhiGap_;}
bool TupleElectron::isEBPhiGap() const { return m_isEBPhiGap; }


//////////////////
// isEEDeeGap
//////////////////
void TupleElectron::set_isEEDeeGap(bool isEEDeeGap_) { m_isEEDeeGap = isEEDeeGap_;}
bool TupleElectron::isEEDeeGap() const { return m_isEEDeeGap; }


//////////////////
// isEERingGap
//////////////////
void TupleElectron::set_isEERingGap(bool isEERingGap_) { m_isEERingGap = isEERingGap_;}
bool TupleElectron::isEERingGap() const { return m_isEERingGap; }


//////////////////
// sigmaEtaEta
//////////////////
void TupleElectron::set_sigmaEtaEta(double sigmaEtaEta_) { m_sigmaEtaEta = sigmaEtaEta_;}
double TupleElectron::sigmaEtaEta() const { return m_sigmaEtaEta; }


//////////////////
// sigmaIetaIeta
//////////////////
void TupleElectron::set_sigmaIetaIeta(double sigmaIetaIeta_) { m_sigmaIetaIeta = sigmaIetaIeta_;}
double TupleElectron::sigmaIetaIeta() const { return m_sigmaIetaIeta; }


//////////////////
// sigmaIphiIphi
//////////////////
void TupleElectron::set_sigmaIphiIphi(double sigmaIphiIphi_) { m_sigmaIphiIphi = sigmaIphiIphi_;}
double TupleElectron::sigmaIphiIphi() const { return m_sigmaIphiIphi; }
