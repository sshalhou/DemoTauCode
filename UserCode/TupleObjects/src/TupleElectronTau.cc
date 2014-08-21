#include "UserCode/TupleObjects/interface/TupleElectronTau.h"
#include "DataFormats/Math/interface/deltaR.h"

TupleElectronTau::TupleElectronTau()
{
  m_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_corrected_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_electronIndex = -999;
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


}

void TupleElectronTau::set_passNonTopEmbeddedTriggerAndMass50(bool passNonTopEmbeddedTriggerAndMass50_) { m_passNonTopEmbeddedTriggerAndMass50  =  passNonTopEmbeddedTriggerAndMass50_;}
bool TupleElectronTau::passNonTopEmbeddedTriggerAndMass50() const { return m_passNonTopEmbeddedTriggerAndMass50; }

void TupleElectronTau::set_passSignalGeneratorMass70to130Cut(bool passSignalGeneratorMass70to130Cut_) { m_passSignalGeneratorMass70to130Cut  =  passSignalGeneratorMass70to130Cut_;}
bool TupleElectronTau::passSignalGeneratorMass70to130Cut() const { return m_passSignalGeneratorMass70to130Cut; }


void TupleElectronTau::set_passesTriLeptonVeto(bool passesTriLeptonVeto_) { m_passesTriLeptonVeto = passesTriLeptonVeto_;}
bool TupleElectronTau::passesTriLeptonVeto() const  { return m_passesTriLeptonVeto; }

void TupleElectronTau::set_cov00(double cov00_) {m_cov00 = cov00_;}
double TupleElectronTau::cov00() const {return m_cov00;}

void TupleElectronTau::set_cov01(double cov01_) {m_cov01 = cov01_;}
double TupleElectronTau::cov01() const {return m_cov01;}

void TupleElectronTau::set_cov10(double cov10_) {m_cov10 = cov10_;}
double TupleElectronTau::cov10() const {return m_cov10;}

void TupleElectronTau::set_cov11(double cov11_) {m_cov11 = cov11_;}
double TupleElectronTau::cov11() const {return m_cov11;}

void TupleElectronTau::set_njets(int njets_) {m_njets = njets_;}
int TupleElectronTau::njets() const {return m_njets;}


void TupleElectronTau::set_nbjets(int nbjets_) {m_nbjets = nbjets_;}
int TupleElectronTau::nbjets() const {return m_nbjets;}


void TupleElectronTau::set_jet1P4(LorentzVector jet1P4_) {m_jet1P4 = jet1P4_;}
LorentzVector TupleElectronTau::jet1P4() const {return m_jet1P4;}


void TupleElectronTau::set_jet1RawP4(LorentzVector jet1RawP4_) {m_jet1RawP4 = jet1RawP4_;}
LorentzVector TupleElectronTau::jet1RawP4() const {return m_jet1RawP4;}


void TupleElectronTau::set_jet1IDMVA(double jet1IDMVA_) {m_jet1IDMVA = jet1IDMVA_;}
double TupleElectronTau::jet1IDMVA() const {return m_jet1IDMVA;}


void TupleElectronTau::set_jet1BTAGMVA(double jet1BTAGMVA_) {m_jet1BTAGMVA = jet1BTAGMVA_;}
double TupleElectronTau::jet1BTAGMVA() const {return m_jet1BTAGMVA;}


void TupleElectronTau::set_jet2P4(LorentzVector jet2P4_) {m_jet2P4 = jet2P4_;}
LorentzVector TupleElectronTau::jet2P4() const {return m_jet2P4;}


void TupleElectronTau::set_jet2RawP4(LorentzVector jet2RawP4_) {m_jet2RawP4 = jet2RawP4_;}
LorentzVector TupleElectronTau::jet2RawP4() const {return m_jet2RawP4;}


void TupleElectronTau::set_jet2IDMVA(double jet2IDMVA_) {m_jet2IDMVA = jet2IDMVA_;}
double TupleElectronTau::jet2IDMVA() const {return m_jet2IDMVA;}


void TupleElectronTau::set_jet2BTAGMVA(double jet2BTAGMVA_) {m_jet2BTAGMVA = jet2BTAGMVA_;}
double TupleElectronTau::jet2BTAGMVA() const {return m_jet2BTAGMVA;}


void TupleElectronTau::set_isGoodTriggerPair(bool isGoodTriggerPair_) { m_isGoodTriggerPair = isGoodTriggerPair_;}
bool TupleElectronTau::isGoodTriggerPair() const  { return m_isGoodTriggerPair; }


// temp MAX pt check
void TupleElectronTau::set_MAX(int MAX_) { m_MAX = MAX_;}
int TupleElectronTau::MAX() const  { return m_MAX; }

void TupleElectronTau::set_mvaMETraw(double mvaMETraw_) { m_mvaMETraw = mvaMETraw_;}
double TupleElectronTau::mvaMETraw() const  { return m_mvaMETraw; }

void TupleElectronTau::set_mvaMET(double mvaMET_) { m_mvaMET = mvaMET_;}
double TupleElectronTau::mvaMET() const  { return m_mvaMET; }

void TupleElectronTau::set_mvaMETphiRaw(double mvaMETphiRaw_) { m_mvaMETphiRaw = mvaMETphiRaw_;}
double TupleElectronTau::mvaMETphiRaw() const  { return m_mvaMETphiRaw; }

void TupleElectronTau::set_mvaMETphi(double mvaMETphi_) { m_mvaMETphi = mvaMETphi_;}
double TupleElectronTau::mvaMETphi() const  { return m_mvaMETphi; }

void TupleElectronTau::set_TransverseMass(double TransverseMass_) { m_TransverseMass = TransverseMass_;}
double TupleElectronTau::TransverseMass() const  { return m_TransverseMass; }


void TupleElectronTau::set_rawTransverseMass(double rawTransverseMass_) { m_rawTransverseMass = rawTransverseMass_;}
double TupleElectronTau::rawTransverseMass() const  { return m_rawTransverseMass; }

void TupleElectronTau::set_p4(LorentzVector v4_) { m_p4 = v4_;}
LorentzVector TupleElectronTau::p4() const  { return m_p4; }

void TupleElectronTau::set_corrected_p4(LorentzVector v4_) { m_corrected_p4 = v4_;}
LorentzVector TupleElectronTau::corrected_p4() const  { return m_corrected_p4; }

void TupleElectronTau::set_sumCharge(int chargeA_, int chargeB_) { m_sumCharge = (chargeA_ + chargeB_);}
int TupleElectronTau::sumCharge() const  { return m_sumCharge; }

void TupleElectronTau::set_electronIndex(int electronIndex_) { m_electronIndex = electronIndex_;}
int TupleElectronTau::electronIndex() const  { return m_electronIndex; }

void TupleElectronTau::set_tauIndex(int tauIndex_) { m_tauIndex = tauIndex_;}
int TupleElectronTau::tauIndex() const  { return m_tauIndex; }

void TupleElectronTau::set_scalarSumPt(LorentzVector A_, LorentzVector B_) { m_scalarSumPt = (A_.pt()+B_.pt());}
double TupleElectronTau::scalarSumPt() const  { return m_scalarSumPt; }

void TupleElectronTau::set_DR(LorentzVector A_, LorentzVector B_) { m_DR = deltaR(A_, B_);}
double TupleElectronTau::DR() const  { return m_DR; }


void TupleElectronTau::set_rawSVFitMass(double rawSVFitMass_) { m_rawSVFitMass = rawSVFitMass_;}
double TupleElectronTau::rawSVFitMass() const  { return m_rawSVFitMass; }

void TupleElectronTau::set_correctedSVFitMass(double correctedSVFitMass_) { m_correctedSVFitMass = correctedSVFitMass_;}
double TupleElectronTau::correctedSVFitMass() const  { return m_correctedSVFitMass; }
