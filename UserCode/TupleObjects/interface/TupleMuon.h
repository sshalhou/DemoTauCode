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
  void set_Pt(float);
  float get_Pt();

private:

  float Pt;
};



#endif
