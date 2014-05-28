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
using namespace std;
using namespace edm;

class TupleTau
{



public:
  TupleTau();
  virtual ~TupleTau(){}

  // setters

  void set_p4(LorentzVector);
  void set_genP4(LorentzVector);
  void set_corrected_p4(LorentzVector, int);
  void set_pdgId(int);
  void set_charge(int);
  void set_decayMode(int);
  void set_passFullId(bool); // needs to be changed to take a PSet + muTau specific

  // Tau Discriminators

  void set_againstMuonLoose(float);
  void set_againstMuonTight(float);
  void set_againstElectronLoose(float);
  void set_againstElectronTight(float);
  void set_againstElectronMedium(float);
  void set_againstMuonMedium(float);
  void set_byIsolationMVAraw(float);
  void set_byLooseIsolationMVA(float);
  void set_byMediumIsolationMVA(float);
  void set_byTightIsolationMVA(float);
  void set_byIsolationMVA2raw(float);
  void set_byLooseIsolationMVA2(float);
  void set_byMediumIsolationMVA2(float);
  void set_byTightIsolationMVA2(float);
  void set_byLooseCombinedIsolationDeltaBetaCorr3Hits(float);
  void set_byMediumCombinedIsolationDeltaBetaCorr3Hits(float);
  void set_byTightCombinedIsolationDeltaBetaCorr3Hits(float);
  void set_byCombinedIsolationDeltaBetaCorrRaw3Hits(float);
  void set_againstElectronMVA3raw(float);
  void set_againstElectronMVA3category(int);
  void set_againstElectronLooseMVA3(float);
  void set_againstElectronMediumMVA3(float);
  void set_againstElectronTightMVA3(float);
  void set_againstElectronVTightMVA3(float);
  void set_againstElectronDeadECAL(float);
  void set_againstMuonLoose2(float);
  void set_againstMuonMedium2(float);
  void set_againstMuonTight2(float);
  void set_againstMuonLoose3(float);
  void set_againstMuonTight3(float);
  void set_antiEMVA3NewLooseWP(float,int);
  void set_antiEMVA3NewMediumWP(float,int);
  void set_antiEMVA3NewTightWP(float,int);
  void set_antiEMVA3NewVeryTightWP(float,int);



  // getters

  LorentzVector p4() const;
  LorentzVector genP4() const;
  LorentzVector corrected_p4() const;
  int pdgId() const;
  int charge() const;
  int decayMode() const;
  bool passFullId() const;
  float againstMuonLoose() const;
  float againstMuonTight() const;
  float againstElectronLoose() const;
  float againstElectronTight() const;
  float againstElectronMedium() const;
  float againstMuonMedium() const;
  float byIsolationMVAraw() const;
  float byLooseIsolationMVA() const;
  float byMediumIsolationMVA() const;
  float byTightIsolationMVA() const;
  float byIsolationMVA2raw() const;
  float byLooseIsolationMVA2() const;
  float byMediumIsolationMVA2() const;
  float byTightIsolationMVA2() const;
  float byLooseCombinedIsolationDeltaBetaCorr3Hits() const;
  float byMediumCombinedIsolationDeltaBetaCorr3Hits() const;
  float byTightCombinedIsolationDeltaBetaCorr3Hits() const;
  float byCombinedIsolationDeltaBetaCorrRaw3Hits() const;
  float againstElectronMVA3raw() const;
  int   againstElectronMVA3category() const;
  float againstElectronLooseMVA3() const;
  float againstElectronMediumMVA3() const;
  float againstElectronTightMVA3() const;
  float againstElectronVTightMVA3() const;
  float againstElectronDeadECAL() const;
  float againstMuonLoose2() const;
  float againstMuonMedium2() const;
  float againstMuonTight2() const;
  float againstMuonLoose3() const;
  float againstMuonTight3() const;
  float antiEMVA3NewLooseWP() const;
  float antiEMVA3NewMediumWP() const;
  float antiEMVA3NewTightWP() const;
  float antiEMVA3NewVeryTightWP() const;





private:

  LorentzVector m_p4;
  LorentzVector m_genP4;
  LorentzVector m_corrected_p4;
  int m_pdgId;
  int m_charge;
  int m_decayMode;
  bool m_passFullId;
  float m_againstMuonLoose;
  float m_againstMuonTight;
  float m_againstElectronLoose;
  float m_againstElectronTight;
  float m_againstElectronMedium;
  float m_againstMuonMedium;
  float m_byIsolationMVAraw;
  float m_byLooseIsolationMVA;
  float m_byMediumIsolationMVA;
  float m_byTightIsolationMVA;
  float m_byIsolationMVA2raw;
  float m_byLooseIsolationMVA2;
  float m_byMediumIsolationMVA2;
  float m_byTightIsolationMVA2;
  float m_byLooseCombinedIsolationDeltaBetaCorr3Hits;
  float m_byMediumCombinedIsolationDeltaBetaCorr3Hits;
  float m_byTightCombinedIsolationDeltaBetaCorr3Hits;
  float m_byCombinedIsolationDeltaBetaCorrRaw3Hits;
  float m_againstElectronMVA3raw;
  int   m_againstElectronMVA3category;
  float m_againstElectronLooseMVA3;
  float m_againstElectronMediumMVA3;
  float m_againstElectronTightMVA3;
  float m_againstElectronVTightMVA3;
  float m_againstElectronDeadECAL;
  float m_againstMuonLoose2;
  float m_againstMuonMedium2;
  float m_againstMuonTight2;
  float m_againstMuonLoose3;
  float m_againstMuonTight3;
  float m_antiEMVA3NewLooseWP;
  float m_antiEMVA3NewMediumWP;
  float m_antiEMVA3NewTightWP;
  float m_antiEMVA3NewVeryTightWP;

};

typedef std::vector<TupleTau> TupleTauCollection;

#endif
