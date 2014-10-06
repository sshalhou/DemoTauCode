#ifndef UserCode_TupleObjects_TupleElectronTau_h
#define UserCode_TupleObjects_TupleElectronTau_h


// system include files
#include <memory>



// needed by ntuple ElectronTaus producer
#include <vector>
#include <iostream>
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;
//using namespace std;
//using namespace edm;

class TupleElectronTau
{



public:
  TupleElectronTau();
  virtual ~TupleElectronTau(){}

  // setters

  void set_p4(LorentzVector);
  void set_corrected_p4(LorentzVector);
  void set_electronIndex(int);
  void set_tauIndex(int);
  void set_scalarSumPt(LorentzVector,LorentzVector);
  void set_DR(LorentzVector,LorentzVector);
  void set_sumCharge(int, int);
  void set_correctedSVFitMass(double);
  void set_rawSVFitMass(double);
  void set_TransverseMass(double);
  void set_rawTransverseMass(double);
  void set_mvaMETraw(double);
  void set_mvaMET(double);
  void set_mvaMETphiRaw(double);
  void set_mvaMETphi(double);
  void set_MAX(int);
  void set_isGoodTriggerPair(bool);
  void set_njets(int);
  void set_nbjets(int);
  void set_njetsUP(int);
  void set_nbjetsUP(int);
  void set_njetsDOWN(int);
  void set_nbjetsDOWN(int);
  void set_jet1P4(LorentzVector);
  void set_jet1RawP4(LorentzVector);
  void set_jet1IDMVA(double);
  void set_jet1BTAGMVA(double);
  void set_jet2P4(LorentzVector);
  void set_jet2RawP4(LorentzVector);
  void set_jet2IDMVA(double);
  void set_jet2BTAGMVA(double);
  void set_cov00(double);
  void set_cov01(double);
  void set_cov10(double);
  void set_cov11(double);
  void set_passesTriLeptonVeto(bool);
  // pass trigger + mass cut. gen level mass on DiLeptons
  // always one if not Z->tau tau Embedded
  void set_passNonTopEmbeddedTriggerAndMass50(bool);
  void set_passSignalGeneratorMass70to130Cut(bool);
  void set_genBosonP4(LorentzVector);
  // the next two are needed for tt events
  void set_genTOPp4(LorentzVector);
  void set_genTOPBARp4(LorentzVector);
  void set_numberOfGoodVertices(int); // passing basic qual. cuts
  void set_PVndof(int);
  void set_PVz(double);
  void set_PVpositionRho(double);
  void set_PVp4(LorentzVector);



  // getters

  LorentzVector p4() const;
  LorentzVector corrected_p4() const;
  int electronIndex() const;
  int tauIndex() const;
  double scalarSumPt() const;
  double DR() const;
  int sumCharge() const;
  double correctedSVFitMass() const;
  double rawSVFitMass() const;
  double TransverseMass() const;
  double rawTransverseMass() const;
  double mvaMETraw() const;
  double mvaMET() const;
  double mvaMETphiRaw() const;
  double mvaMETphi()const;
  int MAX() const;
  bool isGoodTriggerPair() const;
  int njets() const;
  int nbjets() const;
  int njetsUP() const;
  int nbjetsUP() const;
  int njetsDOWN() const;
  int nbjetsDOWN() const;
  LorentzVector jet1P4() const;
  LorentzVector jet1RawP4() const;
  double jet1IDMVA() const;
  double jet1BTAGMVA() const;
  LorentzVector jet2P4() const;
  LorentzVector jet2RawP4() const;
  double jet2IDMVA() const;
  double jet2BTAGMVA() const;
  double cov00() const;
  double cov01() const;
  double cov10() const;
  double cov11() const;
  bool passesTriLeptonVeto() const;
  bool passNonTopEmbeddedTriggerAndMass50() const;
  bool passSignalGeneratorMass70to130Cut() const;
  LorentzVector genBosonP4() const;
  LorentzVector genTOPp4() const;
  LorentzVector genTOPBARp4() const;
  int numberOfGoodVertices() const;
  int PVndof() const;
  double PVz() const;
  double PVpositionRho() const;
  LorentzVector PVp4() const;


private:

  LorentzVector m_p4;
  LorentzVector m_corrected_p4;
  int m_electronIndex;
  int m_tauIndex;
  double m_scalarSumPt;
  double m_DR;
  int m_sumCharge;
  double m_correctedSVFitMass;
  double m_rawSVFitMass;
  double m_TransverseMass;
  double m_rawTransverseMass;
  double m_mvaMETraw;
  double m_mvaMET;
  double m_mvaMETphiRaw;
  double m_mvaMETphi;
  int m_MAX;
  bool m_isGoodTriggerPair;
  int m_njets;
  int m_nbjets;
  int m_njetsUP;
  int m_nbjetsUP;
  int m_njetsDOWN;
  int m_nbjetsDOWN;
  LorentzVector m_jet1P4;
  LorentzVector m_jet1RawP4;
  double m_jet1IDMVA;
  double m_jet1BTAGMVA;
  LorentzVector m_jet2P4;
  LorentzVector m_jet2RawP4;
  double m_jet2IDMVA;
  double m_jet2BTAGMVA;
  double m_cov00;
  double m_cov01;
  double m_cov10;
  double m_cov11;
  bool m_passesTriLeptonVeto;
  bool m_passNonTopEmbeddedTriggerAndMass50;
  bool m_passSignalGeneratorMass70to130Cut;
  LorentzVector m_genBosonP4;
  LorentzVector m_genTOPp4;
  LorentzVector m_genTOPBARp4;
  int m_numberOfGoodVertices;
  int m_PVndof;
  double m_PVz;
  double m_PVpositionRho;
  LorentzVector m_PVp4;

};

typedef std::vector<TupleElectronTau> TupleElectronTauCollection;

#endif
