#ifndef UserCode_TupleObjects_TupleMuon_h
#define UserCode_TupleObjects_TupleMuon_h


// system include files
#include <memory>



// needed by ntuple muons producer
#include <vector>
#include <iostream>
#include "FWCore/Framework/interface/Event.h"
//#include "DataFormats/PatCandidates/interface/Muon.h"
//#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;
using namespace std;
using namespace edm;

class TupleMuon
{



public:
  TupleMuon();
  virtual ~TupleMuon(){}

  // setters

  void set_p4(LorentzVector);
  void set_pfP4(LorentzVector);

  void set_isGlobalMuon(bool);
  void set_isTightMuon(bool);
  void set_isLooseMuon(bool);
  void set_isPFIsolationValid(bool);
  void set_charge(int);
  void set_pdgId(int);

  void set_normalizedChi2(double);
  void set_numberOfValidMuonHits(int);
  void set_numberOfMatchedStations(int);
  void set_numberOfValidPixelHits(int);
  void set_trackerLayersWithMeasurement(int);
  void set_dB(double); // aka d0
  void set_dz(double);
  void set_dxy(double);

  // R = 0.4 isolation
  void set_sumChargedParticlePt_DR4(double);
  void set_sumPhotonEt_DR4(double);
  void set_sumNeutralHadronEt_DR4(double);
  void set_sumPUPt_DR4(double);
  void set_relativeIso_DR4(double);

  // R = 0.3 isolation
  void set_sumChargedParticlePt_DR3(double);
  void set_sumPhotonEt_DR3(double);
  void set_sumNeutralHadronEt_DR3(double);
  void set_sumPUPt_DR3(double);
  void set_relativeIso_DR3(double);


  // getters

  LorentzVector p4();
  LorentzVector pfP4();
  bool isGlobalMuon();
  bool isTightMuon();
  bool isLooseMuon();
  double sumChargedParticlePt_DR4();
  double sumPhotonEt_DR4();
  double sumNeutralHadronEt_DR4();
  double sumPUPt_DR4();
  double relativeIso_DR4();
  double sumChargedParticlePt_DR3();
  double sumPhotonEt_DR3();
  double sumNeutralHadronEt_DR3();
  double sumPUPt_DR3();
  double relativeIso_DR3();
  bool   isPFIsolationValid();
  int    charge();
  int    pdgId() const;
  double normalizedChi2();
  int    numberOfValidMuonHits();
  int    numberOfMatchedStations();
  int    numberOfValidPixelHits();
  int    trackerLayersWithMeasurement();
  double dB(); // aka d0
  double dz();
  double dxy();


private:

  LorentzVector m_p4;
  LorentzVector m_pfP4;
  bool   m_isGlobalMuon;
  bool   m_isTightMuon;
  bool   m_isLooseMuon;
  double m_sumChargedParticlePt_DR4;
  double m_sumPhotonEt_DR4;
  double m_sumNeutralHadronEt_DR4;
  double m_sumPUPt_DR4;
  double m_relativeIso_DR4;
  double m_sumChargedParticlePt_DR3;
  double m_sumPhotonEt_DR3;
  double m_sumNeutralHadronEt_DR3;
  double m_sumPUPt_DR3;
  double m_relativeIso_DR3;
  bool   m_isPFIsolationValid;
  int    m_charge;
  int    m_pdgId;
  double m_normalizedChi2;
  int    m_numberOfValidMuonHits;
  int    m_numberOfMatchedStations;
  int    m_numberOfValidPixelHits;
  int    m_trackerLayersWithMeasurement;
  double m_dB; // aka d0
  double m_dz;
  double m_dxy;




};

typedef std::vector<TupleMuon> TupleMuonCollection;

#endif
