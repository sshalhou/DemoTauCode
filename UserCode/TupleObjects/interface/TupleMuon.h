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
//using namespace std;
//using namespace edm;

class TupleMuon
{



public:
  TupleMuon();
  virtual ~TupleMuon(){}

  // setters

  void set_p4(LorentzVector);
  void set_genP4(LorentzVector);
  void set_pfP4(LorentzVector);

  void set_isGlobalMuon(bool);
  void set_isTightMuon(bool);
  void set_isPFMuon(bool);
  void set_isLooseMuon(bool);
  void set_isPFIsolationValid(bool);
  void set_charge(int);
  void set_PFpdgId(int);
  void set_GENpdgId(int);

  void set_normalizedChi2(double);
  void set_numberOfValidMuonHits(int);
  void set_numberOfMatchedStations(int);
  void set_numberOfValidPixelHits(int);
  void set_trackerLayersWithMeasurement(int);
  void set_dB(double); // aka d0
  void set_dz(double);
  void set_dxy(double);
  void set_passFullId(bool);

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

  // trigger match checks

  void set_has_HltMatchMu17(bool);
  void set_has_HltMatchMu18(bool);
  void set_has_HltMatchMu24(bool);

// set true if the lepton should cause event rejection, when it is
// not used in the H pair

  void set_isTriLeptonVetoCandidate(bool);


  // getters

  LorentzVector p4() const;
  LorentzVector pfP4() const;
  LorentzVector genP4() const;
  bool isGlobalMuon() const;
  bool isTightMuon() const;
  bool isPFMuon() const;
  bool isLooseMuon() const;
  double sumChargedParticlePt_DR4() const;
  double sumPhotonEt_DR4() const;
  double sumNeutralHadronEt_DR4() const;
  double sumPUPt_DR4() const;
  double relativeIso_DR4() const;
  double sumChargedParticlePt_DR3() const;
  double sumPhotonEt_DR3() const;
  double sumNeutralHadronEt_DR3() const;
  double sumPUPt_DR3() const;
  double relativeIso_DR3() const;
  bool   isPFIsolationValid() const;
  int    charge() const;
  int PFpdgId() const;
  int GENpdgId() const;
  double normalizedChi2() const;
  int    numberOfValidMuonHits() const;
  int    numberOfMatchedStations() const;
  int    numberOfValidPixelHits() const;
  int    trackerLayersWithMeasurement() const;
  double dB() const; // aka d0
  double dz() const;
  double dxy() const;
  bool   passFullId() const;


  bool has_HltMatchMu17() const;
  bool has_HltMatchMu18() const;
  bool has_HltMatchMu24() const;
  bool isTriLeptonVetoCandidate() const;


private:

  LorentzVector m_p4;
  LorentzVector m_pfP4;
  LorentzVector m_genP4;
  bool   m_isGlobalMuon;
  bool   m_isTightMuon;
  bool   m_isPFMuon;
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
  int m_PFpdgId;
  int m_GENpdgId;
  double m_normalizedChi2;
  int    m_numberOfValidMuonHits;
  int    m_numberOfMatchedStations;
  int    m_numberOfValidPixelHits;
  int    m_trackerLayersWithMeasurement;
  double m_dB; // aka d0
  double m_dz;
  double m_dxy;
  bool m_passFullId;
  bool m_has_HltMatchMu17;
  bool m_has_HltMatchMu18;
  bool m_has_HltMatchMu24;
  bool m_isTriLeptonVetoCandidate;


};

typedef std::vector<TupleMuon> TupleMuonCollection;

#endif
