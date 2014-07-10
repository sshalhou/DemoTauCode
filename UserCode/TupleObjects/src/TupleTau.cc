#include "UserCode/TupleObjects/interface/TupleTau.h"
#include "UserCode/TupleHelpers/interface/TupleHelpers.hh"


TupleTau::TupleTau()
{
  m_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_genP4.SetXYZT(NAN,NAN,NAN,NAN);
  m_corrected_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_pdgId = -999;
  m_pdgIdGEN = -999;
  m_charge = -999;
  m_decayMode = -999;
  m_passFullId_muTau = 0;
  m_passFullId_eTau = 0;

  m_againstElectronDeadECAL = NAN;
  m_againstElectronLoose = NAN;
  m_againstElectronLooseMVA5 = NAN;
  m_againstElectronMVA5category = NAN;
  m_againstElectronMVA5raw = NAN;
  m_againstElectronMedium = NAN;
  m_againstElectronMediumMVA5 = NAN;
  m_againstElectronTight = NAN;
  m_againstElectronTightMVA5 = NAN;
  m_againstElectronVLooseMVA5 = NAN;
  m_againstElectronVTightMVA5 = NAN;
  m_againstMuonLoose = NAN;
  m_againstMuonLoose2 = NAN;
  m_againstMuonLoose3 = NAN;
  m_againstMuonLooseMVA = NAN;
  m_againstMuonMVAraw = NAN;
  m_againstMuonMedium = NAN;
  m_againstMuonMedium2 = NAN;
  m_againstMuonMediumMVA = NAN;
  m_againstMuonTight = NAN;
  m_againstMuonTight2 = NAN;
  m_againstMuonTight3 = NAN;
  m_againstMuonTightMVA = NAN;
  m_byCombinedIsolationDeltaBetaCorrRaw = NAN;
  m_byCombinedIsolationDeltaBetaCorrRaw3Hits = NAN;
  m_byIsolationMVA3newDMwLTraw = NAN;
  m_byIsolationMVA3newDMwoLTraw = NAN;
  m_byIsolationMVA3oldDMwLTraw = NAN;
  m_byIsolationMVA3oldDMwoLTraw = NAN;
  m_byLooseCombinedIsolationDeltaBetaCorr = NAN;
  m_byLooseCombinedIsolationDeltaBetaCorr3Hits = NAN;
  m_byLooseIsolation = NAN;
  m_byLooseIsolationMVA3newDMwLT = NAN;
  m_byLooseIsolationMVA3newDMwoLT = NAN;
  m_byLooseIsolationMVA3oldDMwLT = NAN;
  m_byLooseIsolationMVA3oldDMwoLT = NAN;
  m_byMediumCombinedIsolationDeltaBetaCorr = NAN;
  m_byMediumCombinedIsolationDeltaBetaCorr3Hits = NAN;
  m_byMediumIsolationMVA3newDMwLT = NAN;
  m_byMediumIsolationMVA3newDMwoLT = NAN;
  m_byMediumIsolationMVA3oldDMwLT = NAN;
  m_byMediumIsolationMVA3oldDMwoLT = NAN;
  m_byTightCombinedIsolationDeltaBetaCorr = NAN;
  m_byTightCombinedIsolationDeltaBetaCorr3Hits = NAN;
  m_byTightIsolationMVA3newDMwLT = NAN;
  m_byTightIsolationMVA3newDMwoLT = NAN;
  m_byTightIsolationMVA3oldDMwLT = NAN;
  m_byTightIsolationMVA3oldDMwoLT = NAN;
  m_byVLooseCombinedIsolationDeltaBetaCorr = NAN;
  m_byVLooseIsolationMVA3newDMwLT = NAN;
  m_byVLooseIsolationMVA3newDMwoLT = NAN;
  m_byVLooseIsolationMVA3oldDMwLT = NAN;
  m_byVLooseIsolationMVA3oldDMwoLT = NAN;
  m_byVTightIsolationMVA3newDMwLT = NAN;
  m_byVTightIsolationMVA3newDMwoLT = NAN;
  m_byVTightIsolationMVA3oldDMwLT = NAN;
  m_byVTightIsolationMVA3oldDMwoLT = NAN;
  m_byVVTightIsolationMVA3newDMwLT = NAN;
  m_byVVTightIsolationMVA3newDMwoLT = NAN;
  m_byVVTightIsolationMVA3oldDMwLT = NAN;
  m_byVVTightIsolationMVA3oldDMwoLT = NAN;
  m_chargedIsoPtSum = NAN;
  m_decayModeFinding = NAN;
  m_decayModeFindingNewDMs = NAN;
  m_decayModeFindingOldDMs = NAN;
  m_neutralIsoPtSum = NAN;
  m_puCorrPtSum = NAN;
  m_has_HltMatchEle20 =  0;
  m_has_HltMatchEle22 =  0;
  m_has_HltMatchEle27 =  0;
  m_has_HltMatchMu17 =  0;
  m_has_HltMatchMu18 =  0;
  m_has_HltMatchMu24 =  0;



}


//////////////////
// has_HltMatchEle20
//////////////////
void TupleTau::set_has_HltMatchEle20(bool has_HltMatchEle20_) { m_has_HltMatchEle20 = has_HltMatchEle20_;}
bool TupleTau::has_HltMatchEle20() const { return m_has_HltMatchEle20; }


//////////////////
// has_HltMatchEle22
//////////////////
void TupleTau::set_has_HltMatchEle22(bool has_HltMatchEle22_) { m_has_HltMatchEle22 = has_HltMatchEle22_;}
bool TupleTau::has_HltMatchEle22() const { return m_has_HltMatchEle22; }


//////////////////
// has_HltMatchEle27
//////////////////
void TupleTau::set_has_HltMatchEle27(bool has_HltMatchEle27_) { m_has_HltMatchEle27 = has_HltMatchEle27_;}
bool TupleTau::has_HltMatchEle27() const { return m_has_HltMatchEle27; }


//////////////////
// has_HltMatchMu17
//////////////////
void TupleTau::set_has_HltMatchMu17(bool has_HltMatchMu17_) { m_has_HltMatchMu17 = has_HltMatchMu17_;}
bool TupleTau::has_HltMatchMu17() const { return m_has_HltMatchMu17; }


//////////////////
// has_HltMatchMu18
//////////////////
void TupleTau::set_has_HltMatchMu18(bool has_HltMatchMu18_) { m_has_HltMatchMu18 = has_HltMatchMu18_;}
bool TupleTau::has_HltMatchMu18() const { return m_has_HltMatchMu18; }


//////////////////
// has_HltMatchMu24
//////////////////
void TupleTau::set_has_HltMatchMu24(bool has_HltMatchMu24_) { m_has_HltMatchMu24 = has_HltMatchMu24_;}
bool TupleTau::has_HltMatchMu24() const { return m_has_HltMatchMu24; }

// will set this in TupleTauProducer, since we can track all cuts
// more easily when calling the producer
void TupleTau::set_passFullId_muTau(bool passFullId_muTau_) { m_passFullId_muTau = passFullId_muTau_;}
bool TupleTau::passFullId_muTau() const  { return m_passFullId_muTau; }

void TupleTau::set_passFullId_eTau(bool passFullId_eTau_) { m_passFullId_eTau = passFullId_eTau_;}
bool TupleTau::passFullId_eTau() const  { return m_passFullId_eTau; }


void TupleTau::set_p4(LorentzVector v4_) { m_p4 = v4_;}
LorentzVector TupleTau::p4() const  { return m_p4; }

void TupleTau::set_genP4(LorentzVector v4_) { m_genP4 = v4_;}
LorentzVector TupleTau::genP4() const  { return m_genP4; }

// the tau discriminators


//////////////////////////////////////////
// againstElectronDeadECAL
//////////////////////////////////////////

void TupleTau::set_againstElectronDeadECAL(float againstElectronDeadECAL_)
{
  m_againstElectronDeadECAL = againstElectronDeadECAL_;
}
float TupleTau::againstElectronDeadECAL() const {return m_againstElectronDeadECAL;}

//////////////////////////////////////////
// againstElectronLoose
//////////////////////////////////////////

void TupleTau::set_againstElectronLoose(float againstElectronLoose_)
{
  m_againstElectronLoose = againstElectronLoose_;
}
float TupleTau::againstElectronLoose() const {return m_againstElectronLoose;}

//////////////////////////////////////////
// againstElectronLooseMVA5
//////////////////////////////////////////

void TupleTau::set_againstElectronLooseMVA5(float againstElectronLooseMVA5_)
{
  m_againstElectronLooseMVA5 = againstElectronLooseMVA5_;
}
float TupleTau::againstElectronLooseMVA5() const {return m_againstElectronLooseMVA5;}

//////////////////////////////////////////
// againstElectronMVA5category
//////////////////////////////////////////

void TupleTau::set_againstElectronMVA5category(float againstElectronMVA5category_)
{
  m_againstElectronMVA5category = againstElectronMVA5category_;
}
float TupleTau::againstElectronMVA5category() const {return m_againstElectronMVA5category;}

//////////////////////////////////////////
// againstElectronMVA5raw
//////////////////////////////////////////

void TupleTau::set_againstElectronMVA5raw(float againstElectronMVA5raw_)
{
  m_againstElectronMVA5raw = againstElectronMVA5raw_;
}
float TupleTau::againstElectronMVA5raw() const {return m_againstElectronMVA5raw;}

//////////////////////////////////////////
// againstElectronMedium
//////////////////////////////////////////

void TupleTau::set_againstElectronMedium(float againstElectronMedium_)
{
  m_againstElectronMedium = againstElectronMedium_;
}
float TupleTau::againstElectronMedium() const {return m_againstElectronMedium;}

//////////////////////////////////////////
// againstElectronMediumMVA5
//////////////////////////////////////////

void TupleTau::set_againstElectronMediumMVA5(float againstElectronMediumMVA5_)
{
  m_againstElectronMediumMVA5 = againstElectronMediumMVA5_;
}
float TupleTau::againstElectronMediumMVA5() const {return m_againstElectronMediumMVA5;}

//////////////////////////////////////////
// againstElectronTight
//////////////////////////////////////////

void TupleTau::set_againstElectronTight(float againstElectronTight_)
{
  m_againstElectronTight = againstElectronTight_;
}
float TupleTau::againstElectronTight() const {return m_againstElectronTight;}

//////////////////////////////////////////
// againstElectronTightMVA5
//////////////////////////////////////////

void TupleTau::set_againstElectronTightMVA5(float againstElectronTightMVA5_)
{
  m_againstElectronTightMVA5 = againstElectronTightMVA5_;
}
float TupleTau::againstElectronTightMVA5() const {return m_againstElectronTightMVA5;}

//////////////////////////////////////////
// againstElectronVLooseMVA5
//////////////////////////////////////////

void TupleTau::set_againstElectronVLooseMVA5(float againstElectronVLooseMVA5_)
{
  m_againstElectronVLooseMVA5 = againstElectronVLooseMVA5_;
}
float TupleTau::againstElectronVLooseMVA5() const {return m_againstElectronVLooseMVA5;}

//////////////////////////////////////////
// againstElectronVTightMVA5
//////////////////////////////////////////

void TupleTau::set_againstElectronVTightMVA5(float againstElectronVTightMVA5_)
{
  m_againstElectronVTightMVA5 = againstElectronVTightMVA5_;
}
float TupleTau::againstElectronVTightMVA5() const {return m_againstElectronVTightMVA5;}

//////////////////////////////////////////
// againstMuonLoose
//////////////////////////////////////////

void TupleTau::set_againstMuonLoose(float againstMuonLoose_)
{
  m_againstMuonLoose = againstMuonLoose_;
}
float TupleTau::againstMuonLoose() const {return m_againstMuonLoose;}

//////////////////////////////////////////
// againstMuonLoose2
//////////////////////////////////////////

void TupleTau::set_againstMuonLoose2(float againstMuonLoose2_)
{
  m_againstMuonLoose2 = againstMuonLoose2_;
}
float TupleTau::againstMuonLoose2() const {return m_againstMuonLoose2;}

//////////////////////////////////////////
// againstMuonLoose3
//////////////////////////////////////////

void TupleTau::set_againstMuonLoose3(float againstMuonLoose3_)
{
  m_againstMuonLoose3 = againstMuonLoose3_;
}
float TupleTau::againstMuonLoose3() const {return m_againstMuonLoose3;}

//////////////////////////////////////////
// againstMuonLooseMVA
//////////////////////////////////////////

void TupleTau::set_againstMuonLooseMVA(float againstMuonLooseMVA_)
{
  m_againstMuonLooseMVA = againstMuonLooseMVA_;
}
float TupleTau::againstMuonLooseMVA() const {return m_againstMuonLooseMVA;}

//////////////////////////////////////////
// againstMuonMVAraw
//////////////////////////////////////////

void TupleTau::set_againstMuonMVAraw(float againstMuonMVAraw_)
{
  m_againstMuonMVAraw = againstMuonMVAraw_;
}
float TupleTau::againstMuonMVAraw() const {return m_againstMuonMVAraw;}

//////////////////////////////////////////
// againstMuonMedium
//////////////////////////////////////////

void TupleTau::set_againstMuonMedium(float againstMuonMedium_)
{
  m_againstMuonMedium = againstMuonMedium_;
}
float TupleTau::againstMuonMedium() const {return m_againstMuonMedium;}

//////////////////////////////////////////
// againstMuonMedium2
//////////////////////////////////////////

void TupleTau::set_againstMuonMedium2(float againstMuonMedium2_)
{
  m_againstMuonMedium2 = againstMuonMedium2_;
}
float TupleTau::againstMuonMedium2() const {return m_againstMuonMedium2;}

//////////////////////////////////////////
// againstMuonMediumMVA
//////////////////////////////////////////

void TupleTau::set_againstMuonMediumMVA(float againstMuonMediumMVA_)
{
  m_againstMuonMediumMVA = againstMuonMediumMVA_;
}
float TupleTau::againstMuonMediumMVA() const {return m_againstMuonMediumMVA;}

//////////////////////////////////////////
// againstMuonTight
//////////////////////////////////////////

void TupleTau::set_againstMuonTight(float againstMuonTight_)
{
  m_againstMuonTight = againstMuonTight_;
}
float TupleTau::againstMuonTight() const {return m_againstMuonTight;}

//////////////////////////////////////////
// againstMuonTight2
//////////////////////////////////////////

void TupleTau::set_againstMuonTight2(float againstMuonTight2_)
{
  m_againstMuonTight2 = againstMuonTight2_;
}
float TupleTau::againstMuonTight2() const {return m_againstMuonTight2;}

//////////////////////////////////////////
// againstMuonTight3
//////////////////////////////////////////

void TupleTau::set_againstMuonTight3(float againstMuonTight3_)
{
  m_againstMuonTight3 = againstMuonTight3_;
}
float TupleTau::againstMuonTight3() const {return m_againstMuonTight3;}

//////////////////////////////////////////
// againstMuonTightMVA
//////////////////////////////////////////

void TupleTau::set_againstMuonTightMVA(float againstMuonTightMVA_)
{
  m_againstMuonTightMVA = againstMuonTightMVA_;
}
float TupleTau::againstMuonTightMVA() const {return m_againstMuonTightMVA;}

//////////////////////////////////////////
// byCombinedIsolationDeltaBetaCorrRaw
//////////////////////////////////////////

void TupleTau::set_byCombinedIsolationDeltaBetaCorrRaw(float byCombinedIsolationDeltaBetaCorrRaw_)
{
  m_byCombinedIsolationDeltaBetaCorrRaw = byCombinedIsolationDeltaBetaCorrRaw_;
}
float TupleTau::byCombinedIsolationDeltaBetaCorrRaw() const {return m_byCombinedIsolationDeltaBetaCorrRaw;}

//////////////////////////////////////////
// byCombinedIsolationDeltaBetaCorrRaw3Hits
//////////////////////////////////////////

void TupleTau::set_byCombinedIsolationDeltaBetaCorrRaw3Hits(float byCombinedIsolationDeltaBetaCorrRaw3Hits_)
{
  m_byCombinedIsolationDeltaBetaCorrRaw3Hits = byCombinedIsolationDeltaBetaCorrRaw3Hits_;
}
float TupleTau::byCombinedIsolationDeltaBetaCorrRaw3Hits() const {return m_byCombinedIsolationDeltaBetaCorrRaw3Hits;}

//////////////////////////////////////////
// byIsolationMVA3newDMwLTraw
//////////////////////////////////////////

void TupleTau::set_byIsolationMVA3newDMwLTraw(float byIsolationMVA3newDMwLTraw_)
{
  m_byIsolationMVA3newDMwLTraw = byIsolationMVA3newDMwLTraw_;
}
float TupleTau::byIsolationMVA3newDMwLTraw() const {return m_byIsolationMVA3newDMwLTraw;}

//////////////////////////////////////////
// byIsolationMVA3newDMwoLTraw
//////////////////////////////////////////

void TupleTau::set_byIsolationMVA3newDMwoLTraw(float byIsolationMVA3newDMwoLTraw_)
{
  m_byIsolationMVA3newDMwoLTraw = byIsolationMVA3newDMwoLTraw_;
}
float TupleTau::byIsolationMVA3newDMwoLTraw() const {return m_byIsolationMVA3newDMwoLTraw;}

//////////////////////////////////////////
// byIsolationMVA3oldDMwLTraw
//////////////////////////////////////////

void TupleTau::set_byIsolationMVA3oldDMwLTraw(float byIsolationMVA3oldDMwLTraw_)
{
  m_byIsolationMVA3oldDMwLTraw = byIsolationMVA3oldDMwLTraw_;
}
float TupleTau::byIsolationMVA3oldDMwLTraw() const {return m_byIsolationMVA3oldDMwLTraw;}

//////////////////////////////////////////
// byIsolationMVA3oldDMwoLTraw
//////////////////////////////////////////

void TupleTau::set_byIsolationMVA3oldDMwoLTraw(float byIsolationMVA3oldDMwoLTraw_)
{
  m_byIsolationMVA3oldDMwoLTraw = byIsolationMVA3oldDMwoLTraw_;
}
float TupleTau::byIsolationMVA3oldDMwoLTraw() const {return m_byIsolationMVA3oldDMwoLTraw;}

//////////////////////////////////////////
// byLooseCombinedIsolationDeltaBetaCorr
//////////////////////////////////////////

void TupleTau::set_byLooseCombinedIsolationDeltaBetaCorr(float byLooseCombinedIsolationDeltaBetaCorr_)
{
  m_byLooseCombinedIsolationDeltaBetaCorr = byLooseCombinedIsolationDeltaBetaCorr_;
}
float TupleTau::byLooseCombinedIsolationDeltaBetaCorr() const {return m_byLooseCombinedIsolationDeltaBetaCorr;}

//////////////////////////////////////////
// byLooseCombinedIsolationDeltaBetaCorr3Hits
//////////////////////////////////////////

void TupleTau::set_byLooseCombinedIsolationDeltaBetaCorr3Hits(float byLooseCombinedIsolationDeltaBetaCorr3Hits_)
{
  m_byLooseCombinedIsolationDeltaBetaCorr3Hits = byLooseCombinedIsolationDeltaBetaCorr3Hits_;
}
float TupleTau::byLooseCombinedIsolationDeltaBetaCorr3Hits() const {return m_byLooseCombinedIsolationDeltaBetaCorr3Hits;}

//////////////////////////////////////////
// byLooseIsolation
//////////////////////////////////////////

void TupleTau::set_byLooseIsolation(float byLooseIsolation_)
{
  m_byLooseIsolation = byLooseIsolation_;
}
float TupleTau::byLooseIsolation() const {return m_byLooseIsolation;}

//////////////////////////////////////////
// byLooseIsolationMVA3newDMwLT
//////////////////////////////////////////

void TupleTau::set_byLooseIsolationMVA3newDMwLT(float byLooseIsolationMVA3newDMwLT_)
{
  m_byLooseIsolationMVA3newDMwLT = byLooseIsolationMVA3newDMwLT_;
}
float TupleTau::byLooseIsolationMVA3newDMwLT() const {return m_byLooseIsolationMVA3newDMwLT;}

//////////////////////////////////////////
// byLooseIsolationMVA3newDMwoLT
//////////////////////////////////////////

void TupleTau::set_byLooseIsolationMVA3newDMwoLT(float byLooseIsolationMVA3newDMwoLT_)
{
  m_byLooseIsolationMVA3newDMwoLT = byLooseIsolationMVA3newDMwoLT_;
}
float TupleTau::byLooseIsolationMVA3newDMwoLT() const {return m_byLooseIsolationMVA3newDMwoLT;}

//////////////////////////////////////////
// byLooseIsolationMVA3oldDMwLT
//////////////////////////////////////////

void TupleTau::set_byLooseIsolationMVA3oldDMwLT(float byLooseIsolationMVA3oldDMwLT_)
{
  m_byLooseIsolationMVA3oldDMwLT = byLooseIsolationMVA3oldDMwLT_;
}
float TupleTau::byLooseIsolationMVA3oldDMwLT() const {return m_byLooseIsolationMVA3oldDMwLT;}

//////////////////////////////////////////
// byLooseIsolationMVA3oldDMwoLT
//////////////////////////////////////////

void TupleTau::set_byLooseIsolationMVA3oldDMwoLT(float byLooseIsolationMVA3oldDMwoLT_)
{
  m_byLooseIsolationMVA3oldDMwoLT = byLooseIsolationMVA3oldDMwoLT_;
}
float TupleTau::byLooseIsolationMVA3oldDMwoLT() const {return m_byLooseIsolationMVA3oldDMwoLT;}

//////////////////////////////////////////
// byMediumCombinedIsolationDeltaBetaCorr
//////////////////////////////////////////

void TupleTau::set_byMediumCombinedIsolationDeltaBetaCorr(float byMediumCombinedIsolationDeltaBetaCorr_)
{
  m_byMediumCombinedIsolationDeltaBetaCorr = byMediumCombinedIsolationDeltaBetaCorr_;
}
float TupleTau::byMediumCombinedIsolationDeltaBetaCorr() const {return m_byMediumCombinedIsolationDeltaBetaCorr;}

//////////////////////////////////////////
// byMediumCombinedIsolationDeltaBetaCorr3Hits
//////////////////////////////////////////

void TupleTau::set_byMediumCombinedIsolationDeltaBetaCorr3Hits(float byMediumCombinedIsolationDeltaBetaCorr3Hits_)
{
  m_byMediumCombinedIsolationDeltaBetaCorr3Hits = byMediumCombinedIsolationDeltaBetaCorr3Hits_;
}
float TupleTau::byMediumCombinedIsolationDeltaBetaCorr3Hits() const {return m_byMediumCombinedIsolationDeltaBetaCorr3Hits;}

//////////////////////////////////////////
// byMediumIsolationMVA3newDMwLT
//////////////////////////////////////////

void TupleTau::set_byMediumIsolationMVA3newDMwLT(float byMediumIsolationMVA3newDMwLT_)
{
  m_byMediumIsolationMVA3newDMwLT = byMediumIsolationMVA3newDMwLT_;
}
float TupleTau::byMediumIsolationMVA3newDMwLT() const {return m_byMediumIsolationMVA3newDMwLT;}

//////////////////////////////////////////
// byMediumIsolationMVA3newDMwoLT
//////////////////////////////////////////

void TupleTau::set_byMediumIsolationMVA3newDMwoLT(float byMediumIsolationMVA3newDMwoLT_)
{
  m_byMediumIsolationMVA3newDMwoLT = byMediumIsolationMVA3newDMwoLT_;
}
float TupleTau::byMediumIsolationMVA3newDMwoLT() const {return m_byMediumIsolationMVA3newDMwoLT;}

//////////////////////////////////////////
// byMediumIsolationMVA3oldDMwLT
//////////////////////////////////////////

void TupleTau::set_byMediumIsolationMVA3oldDMwLT(float byMediumIsolationMVA3oldDMwLT_)
{
  m_byMediumIsolationMVA3oldDMwLT = byMediumIsolationMVA3oldDMwLT_;
}
float TupleTau::byMediumIsolationMVA3oldDMwLT() const {return m_byMediumIsolationMVA3oldDMwLT;}

//////////////////////////////////////////
// byMediumIsolationMVA3oldDMwoLT
//////////////////////////////////////////

void TupleTau::set_byMediumIsolationMVA3oldDMwoLT(float byMediumIsolationMVA3oldDMwoLT_)
{
  m_byMediumIsolationMVA3oldDMwoLT = byMediumIsolationMVA3oldDMwoLT_;
}
float TupleTau::byMediumIsolationMVA3oldDMwoLT() const {return m_byMediumIsolationMVA3oldDMwoLT;}

//////////////////////////////////////////
// byTightCombinedIsolationDeltaBetaCorr
//////////////////////////////////////////

void TupleTau::set_byTightCombinedIsolationDeltaBetaCorr(float byTightCombinedIsolationDeltaBetaCorr_)
{
  m_byTightCombinedIsolationDeltaBetaCorr = byTightCombinedIsolationDeltaBetaCorr_;
}
float TupleTau::byTightCombinedIsolationDeltaBetaCorr() const {return m_byTightCombinedIsolationDeltaBetaCorr;}

//////////////////////////////////////////
// byTightCombinedIsolationDeltaBetaCorr3Hits
//////////////////////////////////////////

void TupleTau::set_byTightCombinedIsolationDeltaBetaCorr3Hits(float byTightCombinedIsolationDeltaBetaCorr3Hits_)
{
  m_byTightCombinedIsolationDeltaBetaCorr3Hits = byTightCombinedIsolationDeltaBetaCorr3Hits_;
}
float TupleTau::byTightCombinedIsolationDeltaBetaCorr3Hits() const {return m_byTightCombinedIsolationDeltaBetaCorr3Hits;}

//////////////////////////////////////////
// byTightIsolationMVA3newDMwLT
//////////////////////////////////////////

void TupleTau::set_byTightIsolationMVA3newDMwLT(float byTightIsolationMVA3newDMwLT_)
{
  m_byTightIsolationMVA3newDMwLT = byTightIsolationMVA3newDMwLT_;
}
float TupleTau::byTightIsolationMVA3newDMwLT() const {return m_byTightIsolationMVA3newDMwLT;}

//////////////////////////////////////////
// byTightIsolationMVA3newDMwoLT
//////////////////////////////////////////

void TupleTau::set_byTightIsolationMVA3newDMwoLT(float byTightIsolationMVA3newDMwoLT_)
{
  m_byTightIsolationMVA3newDMwoLT = byTightIsolationMVA3newDMwoLT_;
}
float TupleTau::byTightIsolationMVA3newDMwoLT() const {return m_byTightIsolationMVA3newDMwoLT;}

//////////////////////////////////////////
// byTightIsolationMVA3oldDMwLT
//////////////////////////////////////////

void TupleTau::set_byTightIsolationMVA3oldDMwLT(float byTightIsolationMVA3oldDMwLT_)
{
  m_byTightIsolationMVA3oldDMwLT = byTightIsolationMVA3oldDMwLT_;
}
float TupleTau::byTightIsolationMVA3oldDMwLT() const {return m_byTightIsolationMVA3oldDMwLT;}

//////////////////////////////////////////
// byTightIsolationMVA3oldDMwoLT
//////////////////////////////////////////

void TupleTau::set_byTightIsolationMVA3oldDMwoLT(float byTightIsolationMVA3oldDMwoLT_)
{
  m_byTightIsolationMVA3oldDMwoLT = byTightIsolationMVA3oldDMwoLT_;
}
float TupleTau::byTightIsolationMVA3oldDMwoLT() const {return m_byTightIsolationMVA3oldDMwoLT;}

//////////////////////////////////////////
// byVLooseCombinedIsolationDeltaBetaCorr
//////////////////////////////////////////

void TupleTau::set_byVLooseCombinedIsolationDeltaBetaCorr(float byVLooseCombinedIsolationDeltaBetaCorr_)
{
  m_byVLooseCombinedIsolationDeltaBetaCorr = byVLooseCombinedIsolationDeltaBetaCorr_;
}
float TupleTau::byVLooseCombinedIsolationDeltaBetaCorr() const {return m_byVLooseCombinedIsolationDeltaBetaCorr;}

//////////////////////////////////////////
// byVLooseIsolationMVA3newDMwLT
//////////////////////////////////////////

void TupleTau::set_byVLooseIsolationMVA3newDMwLT(float byVLooseIsolationMVA3newDMwLT_)
{
  m_byVLooseIsolationMVA3newDMwLT = byVLooseIsolationMVA3newDMwLT_;
}
float TupleTau::byVLooseIsolationMVA3newDMwLT() const {return m_byVLooseIsolationMVA3newDMwLT;}

//////////////////////////////////////////
// byVLooseIsolationMVA3newDMwoLT
//////////////////////////////////////////

void TupleTau::set_byVLooseIsolationMVA3newDMwoLT(float byVLooseIsolationMVA3newDMwoLT_)
{
  m_byVLooseIsolationMVA3newDMwoLT = byVLooseIsolationMVA3newDMwoLT_;
}
float TupleTau::byVLooseIsolationMVA3newDMwoLT() const {return m_byVLooseIsolationMVA3newDMwoLT;}

//////////////////////////////////////////
// byVLooseIsolationMVA3oldDMwLT
//////////////////////////////////////////

void TupleTau::set_byVLooseIsolationMVA3oldDMwLT(float byVLooseIsolationMVA3oldDMwLT_)
{
  m_byVLooseIsolationMVA3oldDMwLT = byVLooseIsolationMVA3oldDMwLT_;
}
float TupleTau::byVLooseIsolationMVA3oldDMwLT() const {return m_byVLooseIsolationMVA3oldDMwLT;}

//////////////////////////////////////////
// byVLooseIsolationMVA3oldDMwoLT
//////////////////////////////////////////

void TupleTau::set_byVLooseIsolationMVA3oldDMwoLT(float byVLooseIsolationMVA3oldDMwoLT_)
{
  m_byVLooseIsolationMVA3oldDMwoLT = byVLooseIsolationMVA3oldDMwoLT_;
}
float TupleTau::byVLooseIsolationMVA3oldDMwoLT() const {return m_byVLooseIsolationMVA3oldDMwoLT;}

//////////////////////////////////////////
// byVTightIsolationMVA3newDMwLT
//////////////////////////////////////////

void TupleTau::set_byVTightIsolationMVA3newDMwLT(float byVTightIsolationMVA3newDMwLT_)
{
  m_byVTightIsolationMVA3newDMwLT = byVTightIsolationMVA3newDMwLT_;
}
float TupleTau::byVTightIsolationMVA3newDMwLT() const {return m_byVTightIsolationMVA3newDMwLT;}

//////////////////////////////////////////
// byVTightIsolationMVA3newDMwoLT
//////////////////////////////////////////

void TupleTau::set_byVTightIsolationMVA3newDMwoLT(float byVTightIsolationMVA3newDMwoLT_)
{
  m_byVTightIsolationMVA3newDMwoLT = byVTightIsolationMVA3newDMwoLT_;
}
float TupleTau::byVTightIsolationMVA3newDMwoLT() const {return m_byVTightIsolationMVA3newDMwoLT;}

//////////////////////////////////////////
// byVTightIsolationMVA3oldDMwLT
//////////////////////////////////////////

void TupleTau::set_byVTightIsolationMVA3oldDMwLT(float byVTightIsolationMVA3oldDMwLT_)
{
  m_byVTightIsolationMVA3oldDMwLT = byVTightIsolationMVA3oldDMwLT_;
}
float TupleTau::byVTightIsolationMVA3oldDMwLT() const {return m_byVTightIsolationMVA3oldDMwLT;}

//////////////////////////////////////////
// byVTightIsolationMVA3oldDMwoLT
//////////////////////////////////////////

void TupleTau::set_byVTightIsolationMVA3oldDMwoLT(float byVTightIsolationMVA3oldDMwoLT_)
{
  m_byVTightIsolationMVA3oldDMwoLT = byVTightIsolationMVA3oldDMwoLT_;
}
float TupleTau::byVTightIsolationMVA3oldDMwoLT() const {return m_byVTightIsolationMVA3oldDMwoLT;}

//////////////////////////////////////////
// byVVTightIsolationMVA3newDMwLT
//////////////////////////////////////////

void TupleTau::set_byVVTightIsolationMVA3newDMwLT(float byVVTightIsolationMVA3newDMwLT_)
{
  m_byVVTightIsolationMVA3newDMwLT = byVVTightIsolationMVA3newDMwLT_;
}
float TupleTau::byVVTightIsolationMVA3newDMwLT() const {return m_byVVTightIsolationMVA3newDMwLT;}

//////////////////////////////////////////
// byVVTightIsolationMVA3newDMwoLT
//////////////////////////////////////////

void TupleTau::set_byVVTightIsolationMVA3newDMwoLT(float byVVTightIsolationMVA3newDMwoLT_)
{
  m_byVVTightIsolationMVA3newDMwoLT = byVVTightIsolationMVA3newDMwoLT_;
}
float TupleTau::byVVTightIsolationMVA3newDMwoLT() const {return m_byVVTightIsolationMVA3newDMwoLT;}

//////////////////////////////////////////
// byVVTightIsolationMVA3oldDMwLT
//////////////////////////////////////////

void TupleTau::set_byVVTightIsolationMVA3oldDMwLT(float byVVTightIsolationMVA3oldDMwLT_)
{
  m_byVVTightIsolationMVA3oldDMwLT = byVVTightIsolationMVA3oldDMwLT_;
}
float TupleTau::byVVTightIsolationMVA3oldDMwLT() const {return m_byVVTightIsolationMVA3oldDMwLT;}

//////////////////////////////////////////
// byVVTightIsolationMVA3oldDMwoLT
//////////////////////////////////////////

void TupleTau::set_byVVTightIsolationMVA3oldDMwoLT(float byVVTightIsolationMVA3oldDMwoLT_)
{
  m_byVVTightIsolationMVA3oldDMwoLT = byVVTightIsolationMVA3oldDMwoLT_;
}
float TupleTau::byVVTightIsolationMVA3oldDMwoLT() const {return m_byVVTightIsolationMVA3oldDMwoLT;}

//////////////////////////////////////////
// chargedIsoPtSum
//////////////////////////////////////////

void TupleTau::set_chargedIsoPtSum(float chargedIsoPtSum_)
{
  m_chargedIsoPtSum = chargedIsoPtSum_;
}
float TupleTau::chargedIsoPtSum() const {return m_chargedIsoPtSum;}

//////////////////////////////////////////
// decayModeFinding
//////////////////////////////////////////

void TupleTau::set_decayModeFinding(float decayModeFinding_)
{
  m_decayModeFinding = decayModeFinding_;
}
float TupleTau::decayModeFinding() const {return m_decayModeFinding;}

//////////////////////////////////////////
// decayModeFindingNewDMs
//////////////////////////////////////////

void TupleTau::set_decayModeFindingNewDMs(float decayModeFindingNewDMs_)
{
  m_decayModeFindingNewDMs = decayModeFindingNewDMs_;
}
float TupleTau::decayModeFindingNewDMs() const {return m_decayModeFindingNewDMs;}

//////////////////////////////////////////
// decayModeFindingOldDMs
//////////////////////////////////////////

void TupleTau::set_decayModeFindingOldDMs(float decayModeFindingOldDMs_)
{
  m_decayModeFindingOldDMs = decayModeFindingOldDMs_;
}
float TupleTau::decayModeFindingOldDMs() const {return m_decayModeFindingOldDMs;}

//////////////////////////////////////////
// neutralIsoPtSum
//////////////////////////////////////////

void TupleTau::set_neutralIsoPtSum(float neutralIsoPtSum_)
{
  m_neutralIsoPtSum = neutralIsoPtSum_;
}
float TupleTau::neutralIsoPtSum() const {return m_neutralIsoPtSum;}

//////////////////////////////////////////
// puCorrPtSum
//////////////////////////////////////////

void TupleTau::set_puCorrPtSum(float puCorrPtSum_)
{
  m_puCorrPtSum = puCorrPtSum_;
}
float TupleTau::puCorrPtSum() const {return m_puCorrPtSum;}


/////////////////////
/////////////////////

void TupleTau::set_corrected_p4(LorentzVector v4_, int decayMode_, int generatorPdgId_)
{

  double v4_sf = 1.0;





  ///////////////////
  // corrections from
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingSummer2013
  // #TauES_and_decay_mode_scale_facto

  // caution, these corrections should only be applied
  // for certain MC samples
  //cout<<" Warning correcting energy of all Taus, add in a sample & MC check!!!!!"<<endl;

  // one prong, 1 pi0
  //if(decayMode_==1)   v4_sf = (1.025 + 0.001 * std::min(std::max(v4_.pt()-45.,0.),10.));

  // 3 prong, 0 to N pi0
  //if(decayMode_>=10 && decayMode_<=14)   v4_sf = (1.012 + 0.001 * std::min(std::max(v4_.pt()-32.,0.),18.));


  /////////////////////
  // 1% correction for improved
  // MSSM analysis if matched to generator
  // level hadronic tau decay

  if(generatorPdgId_ == 15 || generatorPdgId_==-15)
  {

  // Following AN_2014_074, correct for the following taus
  // Three Hadrons
  // Hadron plus one Strip or Hadron plus two Strips
  // Single hadron

    v4_sf *= 1.01;

  }

  m_corrected_p4 = v4_*v4_sf;





}



LorentzVector TupleTau::corrected_p4() const  { return m_corrected_p4; }


void TupleTau::set_pdgId(int pdgId_) { m_pdgId = pdgId_;}
int TupleTau::pdgId() const  { return m_pdgId; }

void TupleTau::set_pdgIdGEN(int pdgIdGEN_) { m_pdgIdGEN = pdgIdGEN_;}
int TupleTau::pdgIdGEN() const  { return m_pdgIdGEN; }

void TupleTau::set_charge(int charge_) { m_charge = charge_;}
int TupleTau::charge() const  { return m_charge; }

void TupleTau::set_decayMode(int decayMode_) { m_decayMode = decayMode_;}
int TupleTau::decayMode() const  { return m_decayMode; }
