#include "UserCode/TupleObjects/interface/TupleMuonTau.h"
#include "DataFormats/Math/interface/deltaR.h"

TupleMuonTau::TupleMuonTau()
{
  m_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_corrected_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_muonIndex = -999;
  m_tauIndex = -999;
  m_scalarSumPt = NAN;
  m_DR = NAN;
  m_sumCharge = -999;
  m_correctedSVFitMass = NAN;
  m_rawSVFitMass = NAN;
  m_TransverseMass = NAN;
  m_rawTransverseMass = NAN;
  // probably better to store the vectors later on
  m_mvaMETraw = NAN;
  m_mvaMET = NAN;
  m_mvaMETphiRaw = NAN;
  m_mvaMETphi = NAN;
  m_MAX = 0;
  m_isGoodTriggerPair = 0;
  m_njets = -999;
  m_nbjets = -999;
  m_nbjetsLOOSE = -999;
  m_nbjetsLOOSEUP = -999;
  m_nbjetsLOOSEDOWN = -999;
  m_njetsUP = -999;
  m_nbjetsUP = -999;
  m_njetsDOWN = -999;
  m_nbjetsDOWN = -999;
  m_jet1P4.SetXYZT(NAN,NAN,NAN,NAN);
  m_jet1RawP4.SetXYZT(NAN,NAN,NAN,NAN);
  m_jet1IDMVA = NAN;
  m_jet1BTAGMVA = NAN;
  m_jet2P4.SetXYZT(NAN,NAN,NAN,NAN);
  m_jet2RawP4.SetXYZT(NAN,NAN,NAN,NAN);
  m_jet2IDMVA = NAN;
  m_jet2BTAGMVA = NAN;
  m_cov00 = NAN;
  m_cov01 = NAN;
  m_cov10 = NAN;
  m_cov11 = NAN;
  m_passesTriLeptonVeto = 0;
  m_passNonTopEmbeddedTriggerAndMass50  = 0;
  m_passSignalGeneratorMass70to130Cut = 0;
  m_genBosonP4.SetXYZT(NAN,NAN,NAN,NAN);
  m_genTOPp4.SetXYZT(NAN,NAN,NAN,NAN);
  m_genTOPBARp4.SetXYZT(NAN,NAN,NAN,NAN);
  m_numberOfGoodVertices = -999;
  m_PVndof = -999;
  m_PVz = NAN;
  m_PVpositionRho = NAN;
  m_PVp4.SetXYZT(NAN,NAN,NAN,NAN);



}

void TupleMuonTau::set_numberOfGoodVertices(int numberOfGoodVertices_) { m_numberOfGoodVertices  =  numberOfGoodVertices_;}
int TupleMuonTau::numberOfGoodVertices() const { return m_numberOfGoodVertices; }

void TupleMuonTau::set_PVndof(int PVndof_) { m_PVndof  =  PVndof_;}
int TupleMuonTau::PVndof() const { return m_PVndof; }

void TupleMuonTau::set_PVz(double PVz_) { m_PVz  =  PVz_;}
double TupleMuonTau::PVz() const { return m_PVz; }

void TupleMuonTau::set_PVpositionRho(double PVpositionRho_) { m_PVpositionRho  =  PVpositionRho_;}
double TupleMuonTau::PVpositionRho() const { return m_PVpositionRho; }

void TupleMuonTau::set_PVp4(LorentzVector PVp4_) { m_PVp4  =  PVp4_;}
LorentzVector TupleMuonTau::PVp4() const { return m_PVp4; }



void TupleMuonTau::set_genTOPp4(LorentzVector genTOPp4_) { m_genTOPp4  =  genTOPp4_;}
LorentzVector TupleMuonTau::genTOPp4() const { return m_genTOPp4; }

void TupleMuonTau::set_genTOPBARp4(LorentzVector genTOPBARp4_) { m_genTOPBARp4  =  genTOPBARp4_;}
LorentzVector TupleMuonTau::genTOPBARp4() const { return m_genTOPBARp4; }

void TupleMuonTau::set_genBosonP4(LorentzVector genBosonP4_) { m_genBosonP4  =  genBosonP4_;}
LorentzVector TupleMuonTau::genBosonP4() const { return m_genBosonP4; }

void TupleMuonTau::set_passNonTopEmbeddedTriggerAndMass50(bool passNonTopEmbeddedTriggerAndMass50_) { m_passNonTopEmbeddedTriggerAndMass50  =  passNonTopEmbeddedTriggerAndMass50_;}
bool TupleMuonTau::passNonTopEmbeddedTriggerAndMass50() const { return m_passNonTopEmbeddedTriggerAndMass50; }

void TupleMuonTau::set_passSignalGeneratorMass70to130Cut(bool passSignalGeneratorMass70to130Cut_) { m_passSignalGeneratorMass70to130Cut  =  passSignalGeneratorMass70to130Cut_;}
bool TupleMuonTau::passSignalGeneratorMass70to130Cut() const { return m_passSignalGeneratorMass70to130Cut; }


void TupleMuonTau::set_passesTriLeptonVeto(bool passesTriLeptonVeto_) { m_passesTriLeptonVeto = passesTriLeptonVeto_;}
bool TupleMuonTau::passesTriLeptonVeto() const  { return m_passesTriLeptonVeto; }

void TupleMuonTau::set_cov00(double cov00_) {m_cov00 = cov00_;}
double TupleMuonTau::cov00() const {return m_cov00;}

void TupleMuonTau::set_cov01(double cov01_) {m_cov01 = cov01_;}
double TupleMuonTau::cov01() const {return m_cov01;}

void TupleMuonTau::set_cov10(double cov10_) {m_cov10 = cov10_;}
double TupleMuonTau::cov10() const {return m_cov10;}

void TupleMuonTau::set_cov11(double cov11_) {m_cov11 = cov11_;}
double TupleMuonTau::cov11() const {return m_cov11;}

void TupleMuonTau::set_njets(int njets_) {m_njets = njets_;}
int TupleMuonTau::njets() const {return m_njets;}


void TupleMuonTau::set_nbjets(int nbjets_) {m_nbjets = nbjets_;}
int TupleMuonTau::nbjets() const {return m_nbjets;}

void TupleMuonTau::set_nbjetsLOOSE(int nbjetsLOOSE_) {m_nbjetsLOOSE = nbjetsLOOSE_;}
int TupleMuonTau::nbjetsLOOSE() const {return m_nbjetsLOOSE;}

void TupleMuonTau::set_nbjetsLOOSEUP(int nbjetsLOOSEUP_) {m_nbjetsLOOSEUP = nbjetsLOOSEUP_;}
int TupleMuonTau::nbjetsLOOSEUP() const {return m_nbjetsLOOSEUP;}

void TupleMuonTau::set_nbjetsLOOSEDOWN(int nbjetsLOOSEDOWN_) {m_nbjetsLOOSEDOWN = nbjetsLOOSEDOWN_;}
int TupleMuonTau::nbjetsLOOSEDOWN() const {return m_nbjetsLOOSEDOWN;}

void TupleMuonTau::set_njetsUP(int njetsUP_) {m_njetsUP = njetsUP_;}
int TupleMuonTau::njetsUP() const {return m_njetsUP;}

void TupleMuonTau::set_nbjetsUP(int nbjetsUP_) {m_nbjetsUP = nbjetsUP_;}
int TupleMuonTau::nbjetsUP() const {return m_nbjetsUP;}

void TupleMuonTau::set_njetsDOWN(int njetsDOWN_) {m_njetsDOWN = njetsDOWN_;}
int TupleMuonTau::njetsDOWN() const {return m_njetsDOWN;}

void TupleMuonTau::set_nbjetsDOWN(int nbjetsDOWN_) {m_nbjetsDOWN = nbjetsDOWN_;}
int TupleMuonTau::nbjetsDOWN() const {return m_nbjetsDOWN;}


void TupleMuonTau::set_jet1P4(LorentzVector jet1P4_) {m_jet1P4 = jet1P4_;}
LorentzVector TupleMuonTau::jet1P4() const {return m_jet1P4;}


void TupleMuonTau::set_jet1RawP4(LorentzVector jet1RawP4_) {m_jet1RawP4 = jet1RawP4_;}
LorentzVector TupleMuonTau::jet1RawP4() const {return m_jet1RawP4;}


void TupleMuonTau::set_jet1IDMVA(double jet1IDMVA_) {m_jet1IDMVA = jet1IDMVA_;}
double TupleMuonTau::jet1IDMVA() const {return m_jet1IDMVA;}


void TupleMuonTau::set_jet1BTAGMVA(double jet1BTAGMVA_) {m_jet1BTAGMVA = jet1BTAGMVA_;}
double TupleMuonTau::jet1BTAGMVA() const {return m_jet1BTAGMVA;}


void TupleMuonTau::set_jet2P4(LorentzVector jet2P4_) {m_jet2P4 = jet2P4_;}
LorentzVector TupleMuonTau::jet2P4() const {return m_jet2P4;}


void TupleMuonTau::set_jet2RawP4(LorentzVector jet2RawP4_) {m_jet2RawP4 = jet2RawP4_;}
LorentzVector TupleMuonTau::jet2RawP4() const {return m_jet2RawP4;}


void TupleMuonTau::set_jet2IDMVA(double jet2IDMVA_) {m_jet2IDMVA = jet2IDMVA_;}
double TupleMuonTau::jet2IDMVA() const {return m_jet2IDMVA;}


void TupleMuonTau::set_jet2BTAGMVA(double jet2BTAGMVA_) {m_jet2BTAGMVA = jet2BTAGMVA_;}
double TupleMuonTau::jet2BTAGMVA() const {return m_jet2BTAGMVA;}


void TupleMuonTau::set_isGoodTriggerPair(bool isGoodTriggerPair_) { m_isGoodTriggerPair = isGoodTriggerPair_;}
bool TupleMuonTau::isGoodTriggerPair() const  { return m_isGoodTriggerPair; }


// temp MAX pt check
void TupleMuonTau::set_MAX(int MAX_) { m_MAX = MAX_;}
int TupleMuonTau::MAX() const  { return m_MAX; }

void TupleMuonTau::set_mvaMETraw(double mvaMETraw_) { m_mvaMETraw = mvaMETraw_;}
double TupleMuonTau::mvaMETraw() const  { return m_mvaMETraw; }

void TupleMuonTau::set_mvaMET(double mvaMET_) { m_mvaMET = mvaMET_;}
double TupleMuonTau::mvaMET() const  { return m_mvaMET; }

void TupleMuonTau::set_mvaMETphiRaw(double mvaMETphiRaw_) { m_mvaMETphiRaw = mvaMETphiRaw_;}
double TupleMuonTau::mvaMETphiRaw() const  { return m_mvaMETphiRaw; }

void TupleMuonTau::set_mvaMETphi(double mvaMETphi_) { m_mvaMETphi = mvaMETphi_;}
double TupleMuonTau::mvaMETphi() const  { return m_mvaMETphi; }

void TupleMuonTau::set_TransverseMass(double TransverseMass_) { m_TransverseMass = TransverseMass_;}
double TupleMuonTau::TransverseMass() const  { return m_TransverseMass; }


void TupleMuonTau::set_rawTransverseMass(double rawTransverseMass_) { m_rawTransverseMass = rawTransverseMass_;}
double TupleMuonTau::rawTransverseMass() const  { return m_rawTransverseMass; }

void TupleMuonTau::set_p4(LorentzVector v4_) { m_p4 = v4_;}
LorentzVector TupleMuonTau::p4() const  { return m_p4; }

void TupleMuonTau::set_corrected_p4(LorentzVector v4_) { m_corrected_p4 = v4_;}
LorentzVector TupleMuonTau::corrected_p4() const  { return m_corrected_p4; }

void TupleMuonTau::set_sumCharge(int chargeA_, int chargeB_) { m_sumCharge = (chargeA_ + chargeB_);}
int TupleMuonTau::sumCharge() const  { return m_sumCharge; }

void TupleMuonTau::set_muonIndex(int muonIndex_) { m_muonIndex = muonIndex_;}
int TupleMuonTau::muonIndex() const  { return m_muonIndex; }

void TupleMuonTau::set_tauIndex(int tauIndex_) { m_tauIndex = tauIndex_;}
int TupleMuonTau::tauIndex() const  { return m_tauIndex; }

void TupleMuonTau::set_scalarSumPt(LorentzVector A_, LorentzVector B_) { m_scalarSumPt = (A_.pt()+B_.pt());}
double TupleMuonTau::scalarSumPt() const  { return m_scalarSumPt; }

void TupleMuonTau::set_DR(LorentzVector A_, LorentzVector B_) { m_DR = deltaR(A_, B_);}
double TupleMuonTau::DR() const  { return m_DR; }

void TupleMuonTau::set_correctedSVFitMass(double correctedSVFitMass_) { m_correctedSVFitMass = correctedSVFitMass_;}
double TupleMuonTau::correctedSVFitMass() const  { return m_correctedSVFitMass; }

void TupleMuonTau::set_rawSVFitMass(double rawSVFitMass_) { m_rawSVFitMass = rawSVFitMass_;}
double TupleMuonTau::rawSVFitMass() const  { return m_rawSVFitMass; }
