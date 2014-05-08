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

  // getters

  float get_Pt();
  LorentzVector get_p4();
  bool get_isGlobalMuon();
  bool get_isTightMuon();
  bool get_isLooseMuon();

private:

  float Pt;
  LorentzVector p4;
  bool isGlobalMuon;
  bool isTightMuon;
  bool isLooseMuon;

};

typedef std::vector<TupleMuon> TupleMuonCollection;

#endif
