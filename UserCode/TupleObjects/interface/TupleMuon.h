#ifndef UserCode_TupleObjects_TupleMuon_h
#define UserCode_TupleObjects_TupleMuon_h


// system include files
#include <memory>


// needed by ntuple muons producer
#include <vector>
#include <iostream>
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
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

  void set_Pt(float);
  void set_p4(LorentzVector);
  void set_isGlobalMuon(bool);
  void set_isTightMuon(bool);
  void set_isLooseMuon(bool);
  void set_sumChargedParticlePt(double);
  void set_sumPhotonEt(double);
  void set_sumNeutralHadronEt(double);
  void set_sumPUPt(double);
  void set_relativeIso(double);




  // getters

  LorentzVector p4();
  bool isGlobalMuon();
  bool isTightMuon();
  bool isLooseMuon();
  double sumChargedParticlePt();
  double sumPhotonEt();
  double sumNeutralHadronEt();
  double sumPUPt();
  double relativeIso();



private:

  LorentzVector m_p4;
  bool m_isGlobalMuon;
  bool m_isTightMuon;
  bool m_isLooseMuon;
  double m_sumChargedParticlePt;
  double m_sumPhotonEt;
  double m_sumNeutralHadronEt;
  double m_sumPUPt;
  double m_relativeIso;

};

typedef std::vector<TupleMuon> TupleMuonCollection;

#endif
