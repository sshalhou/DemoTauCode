#ifndef UserCode_TupleObjects_TupleTau_h
#define UserCode_TupleObjects_TupleTau_h


// system include files
#include <memory>



// needed by ntuple Taus producer
#include <vector>
#include <iostream>
#include "FWCore/Framework/interface/Event.h"
//#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;
//using namespace std;
//using namespace edm;

class TupleTau
{



public:
  TupleTau();
  virtual ~TupleTau(){}

  // setters

  void set_pfJetRefP4(LorentzVector);
  void set_p4(LorentzVector);
  void set_genP4(LorentzVector);
  void set_genJet(LorentzVector);
  void set_corrected_p4(LorentzVector, std::size_t, std::size_t, double);
  void set_pdgId(int);
  void set_pdgIdGEN(int);

  void set_charge(int);
  void set_decayMode(int);
  void set_passFullId_muTau(bool);
  void set_passFullId_eTau(bool);
  void set_numStrips(int);
  void set_numHadrons(int);


  // Tau Discriminators

  void set_againstElectronDeadECAL(float);
  void set_againstElectronLoose(float);
  void set_againstElectronLooseMVA5(float);
  void set_againstElectronMVA5category(float);
  void set_againstElectronMVA5raw(float);
  void set_againstElectronMedium(float);
  void set_againstElectronMediumMVA5(float);
  void set_againstElectronTight(float);
  void set_againstElectronTightMVA5(float);
  void set_againstElectronVLooseMVA5(float);
  void set_againstElectronVTightMVA5(float);
  void set_againstMuonLoose(float);
  void set_againstMuonLoose2(float);
  void set_againstMuonLoose3(float);
  void set_againstMuonLooseMVA(float);
  void set_againstMuonMVAraw(float);
  void set_againstMuonMedium(float);
  void set_againstMuonMedium2(float);
  void set_againstMuonMediumMVA(float);
  void set_againstMuonTight(float);
  void set_againstMuonTight2(float);
  void set_againstMuonTight3(float);
  void set_againstMuonTightMVA(float);
  void set_byCombinedIsolationDeltaBetaCorrRaw(float);
  void set_byCombinedIsolationDeltaBetaCorrRaw3Hits(float);
  void set_byIsolationMVA3newDMwLTraw(float);
  void set_byIsolationMVA3newDMwoLTraw(float);
  void set_byIsolationMVA3oldDMwLTraw(float);
  void set_byIsolationMVA3oldDMwoLTraw(float);
  void set_byLooseCombinedIsolationDeltaBetaCorr(float);
  void set_byLooseCombinedIsolationDeltaBetaCorr3Hits(float);
  void set_byLooseIsolation(float);
  void set_byLooseIsolationMVA3newDMwLT(float);
  void set_byLooseIsolationMVA3newDMwoLT(float);
  void set_byLooseIsolationMVA3oldDMwLT(float);
  void set_byLooseIsolationMVA3oldDMwoLT(float);
  void set_byMediumCombinedIsolationDeltaBetaCorr(float);
  void set_byMediumCombinedIsolationDeltaBetaCorr3Hits(float);
  void set_byMediumIsolationMVA3newDMwLT(float);
  void set_byMediumIsolationMVA3newDMwoLT(float);
  void set_byMediumIsolationMVA3oldDMwLT(float);
  void set_byMediumIsolationMVA3oldDMwoLT(float);
  void set_byTightCombinedIsolationDeltaBetaCorr(float);
  void set_byTightCombinedIsolationDeltaBetaCorr3Hits(float);
  void set_byTightIsolationMVA3newDMwLT(float);
  void set_byTightIsolationMVA3newDMwoLT(float);
  void set_byTightIsolationMVA3oldDMwLT(float);
  void set_byTightIsolationMVA3oldDMwoLT(float);
  void set_byVLooseCombinedIsolationDeltaBetaCorr(float);
  void set_byVLooseIsolationMVA3newDMwLT(float);
  void set_byVLooseIsolationMVA3newDMwoLT(float);
  void set_byVLooseIsolationMVA3oldDMwLT(float);
  void set_byVLooseIsolationMVA3oldDMwoLT(float);
  void set_byVTightIsolationMVA3newDMwLT(float);
  void set_byVTightIsolationMVA3newDMwoLT(float);
  void set_byVTightIsolationMVA3oldDMwLT(float);
  void set_byVTightIsolationMVA3oldDMwoLT(float);
  void set_byVVTightIsolationMVA3newDMwLT(float);
  void set_byVVTightIsolationMVA3newDMwoLT(float);
  void set_byVVTightIsolationMVA3oldDMwLT(float);
  void set_byVVTightIsolationMVA3oldDMwoLT(float);
  void set_chargedIsoPtSum(float);
  void set_decayModeFinding(float);
  void set_decayModeFindingNewDMs(float);
  void set_decayModeFindingOldDMs(float);
  void set_neutralIsoPtSum(float);
  void set_puCorrPtSum(float);


  // trigger match checks

  void set_has_HltMatchEle20(bool);
  void set_has_HltMatchEle22(bool);
  void set_has_HltMatchEle27(bool);
  void set_has_HltMatchMu17(bool);
  void set_has_HltMatchMu18(bool);
  void set_has_HltMatchMu24(bool);


  // getters

  LorentzVector pfJetRefP4() const;
  LorentzVector p4() const;
  LorentzVector genP4() const;
  LorentzVector genJet() const;
  LorentzVector corrected_p4() const;
  int pdgId() const;
  int pdgIdGEN() const;
  int charge() const;
  int decayMode() const;
  bool passFullId_muTau() const;
  bool passFullId_eTau() const;
  int numStrips() const;
  int numHadrons() const;


  float againstElectronDeadECAL() const;
  float againstElectronLoose() const;
  float againstElectronLooseMVA5() const;
  float againstElectronMVA5category() const;
  float againstElectronMVA5raw() const;
  float againstElectronMedium() const;
  float againstElectronMediumMVA5() const;
  float againstElectronTight() const;
  float againstElectronTightMVA5() const;
  float againstElectronVLooseMVA5() const;
  float againstElectronVTightMVA5() const;
  float againstMuonLoose() const;
  float againstMuonLoose2() const;
  float againstMuonLoose3() const;
  float againstMuonLooseMVA() const;
  float againstMuonMVAraw() const;
  float againstMuonMedium() const;
  float againstMuonMedium2() const;
  float againstMuonMediumMVA() const;
  float againstMuonTight() const;
  float againstMuonTight2() const;
  float againstMuonTight3() const;
  float againstMuonTightMVA() const;
  float byCombinedIsolationDeltaBetaCorrRaw() const;
  float byCombinedIsolationDeltaBetaCorrRaw3Hits() const;
  float byIsolationMVA3newDMwLTraw() const;
  float byIsolationMVA3newDMwoLTraw() const;
  float byIsolationMVA3oldDMwLTraw() const;
  float byIsolationMVA3oldDMwoLTraw() const;
  float byLooseCombinedIsolationDeltaBetaCorr() const;
  float byLooseCombinedIsolationDeltaBetaCorr3Hits() const;
  float byLooseIsolation() const;
  float byLooseIsolationMVA3newDMwLT() const;
  float byLooseIsolationMVA3newDMwoLT() const;
  float byLooseIsolationMVA3oldDMwLT() const;
  float byLooseIsolationMVA3oldDMwoLT() const;
  float byMediumCombinedIsolationDeltaBetaCorr() const;
  float byMediumCombinedIsolationDeltaBetaCorr3Hits() const;
  float byMediumIsolationMVA3newDMwLT() const;
  float byMediumIsolationMVA3newDMwoLT() const;
  float byMediumIsolationMVA3oldDMwLT() const;
  float byMediumIsolationMVA3oldDMwoLT() const;
  float byTightCombinedIsolationDeltaBetaCorr() const;
  float byTightCombinedIsolationDeltaBetaCorr3Hits() const;
  float byTightIsolationMVA3newDMwLT() const;
  float byTightIsolationMVA3newDMwoLT() const;
  float byTightIsolationMVA3oldDMwLT() const;
  float byTightIsolationMVA3oldDMwoLT() const;
  float byVLooseCombinedIsolationDeltaBetaCorr() const;
  float byVLooseIsolationMVA3newDMwLT() const;
  float byVLooseIsolationMVA3newDMwoLT() const;
  float byVLooseIsolationMVA3oldDMwLT() const;
  float byVLooseIsolationMVA3oldDMwoLT() const;
  float byVTightIsolationMVA3newDMwLT() const;
  float byVTightIsolationMVA3newDMwoLT() const;
  float byVTightIsolationMVA3oldDMwLT() const;
  float byVTightIsolationMVA3oldDMwoLT() const;
  float byVVTightIsolationMVA3newDMwLT() const;
  float byVVTightIsolationMVA3newDMwoLT() const;
  float byVVTightIsolationMVA3oldDMwLT() const;
  float byVVTightIsolationMVA3oldDMwoLT() const;
  float chargedIsoPtSum() const;
  float decayModeFinding() const;
  float decayModeFindingNewDMs() const;
  float decayModeFindingOldDMs() const;
  float neutralIsoPtSum() const;
  float puCorrPtSum() const;
  bool has_HltMatchEle20() const;
  bool has_HltMatchEle22() const;
  bool has_HltMatchEle27() const;
  bool has_HltMatchMu17() const;
  bool has_HltMatchMu18() const;
  bool has_HltMatchMu24() const;



private:

  LorentzVector m_pfJetRefP4;
  LorentzVector m_p4;
  LorentzVector m_genP4;
  LorentzVector m_genJet;
  LorentzVector m_corrected_p4;
  int m_pdgId;
  int m_pdgIdGEN;
  int m_charge;
  int m_decayMode;
  bool m_passFullId_muTau;
  bool m_passFullId_eTau;
  int m_numStrips;
  int m_numHadrons;

  float m_againstElectronDeadECAL;
  float m_againstElectronLoose;
  float m_againstElectronLooseMVA5;
  float m_againstElectronMVA5category;
  float m_againstElectronMVA5raw;
  float m_againstElectronMedium;
  float m_againstElectronMediumMVA5;
  float m_againstElectronTight;
  float m_againstElectronTightMVA5;
  float m_againstElectronVLooseMVA5;
  float m_againstElectronVTightMVA5;
  float m_againstMuonLoose;
  float m_againstMuonLoose2;
  float m_againstMuonLoose3;
  float m_againstMuonLooseMVA;
  float m_againstMuonMVAraw;
  float m_againstMuonMedium;
  float m_againstMuonMedium2;
  float m_againstMuonMediumMVA;
  float m_againstMuonTight;
  float m_againstMuonTight2;
  float m_againstMuonTight3;
  float m_againstMuonTightMVA;
  float m_byCombinedIsolationDeltaBetaCorrRaw;
  float m_byCombinedIsolationDeltaBetaCorrRaw3Hits;
  float m_byIsolationMVA3newDMwLTraw;
  float m_byIsolationMVA3newDMwoLTraw;
  float m_byIsolationMVA3oldDMwLTraw;
  float m_byIsolationMVA3oldDMwoLTraw;
  float m_byLooseCombinedIsolationDeltaBetaCorr;
  float m_byLooseCombinedIsolationDeltaBetaCorr3Hits;
  float m_byLooseIsolation;
  float m_byLooseIsolationMVA3newDMwLT;
  float m_byLooseIsolationMVA3newDMwoLT;
  float m_byLooseIsolationMVA3oldDMwLT;
  float m_byLooseIsolationMVA3oldDMwoLT;
  float m_byMediumCombinedIsolationDeltaBetaCorr;
  float m_byMediumCombinedIsolationDeltaBetaCorr3Hits;
  float m_byMediumIsolationMVA3newDMwLT;
  float m_byMediumIsolationMVA3newDMwoLT;
  float m_byMediumIsolationMVA3oldDMwLT;
  float m_byMediumIsolationMVA3oldDMwoLT;
  float m_byTightCombinedIsolationDeltaBetaCorr;
  float m_byTightCombinedIsolationDeltaBetaCorr3Hits;
  float m_byTightIsolationMVA3newDMwLT;
  float m_byTightIsolationMVA3newDMwoLT;
  float m_byTightIsolationMVA3oldDMwLT;
  float m_byTightIsolationMVA3oldDMwoLT;
  float m_byVLooseCombinedIsolationDeltaBetaCorr;
  float m_byVLooseIsolationMVA3newDMwLT;
  float m_byVLooseIsolationMVA3newDMwoLT;
  float m_byVLooseIsolationMVA3oldDMwLT;
  float m_byVLooseIsolationMVA3oldDMwoLT;
  float m_byVTightIsolationMVA3newDMwLT;
  float m_byVTightIsolationMVA3newDMwoLT;
  float m_byVTightIsolationMVA3oldDMwLT;
  float m_byVTightIsolationMVA3oldDMwoLT;
  float m_byVVTightIsolationMVA3newDMwLT;
  float m_byVVTightIsolationMVA3newDMwoLT;
  float m_byVVTightIsolationMVA3oldDMwLT;
  float m_byVVTightIsolationMVA3oldDMwoLT;
  float m_chargedIsoPtSum;
  float m_decayModeFinding;
  float m_decayModeFindingNewDMs;
  float m_decayModeFindingOldDMs;
  float m_neutralIsoPtSum;
  float m_puCorrPtSum;
  bool m_has_HltMatchEle20;
  bool m_has_HltMatchEle22;
  bool m_has_HltMatchEle27;
  bool m_has_HltMatchMu17;
  bool m_has_HltMatchMu18;
  bool m_has_HltMatchMu24;

};

typedef std::vector<TupleTau> TupleTauCollection;

#endif
