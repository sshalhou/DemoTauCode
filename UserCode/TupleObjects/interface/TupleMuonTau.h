#ifndef UserCode_TupleObjects_TupleMuonTau_h
#define UserCode_TupleObjects_TupleMuonTau_h


// system include files
#include <memory>



// needed by ntuple MuonTaus producer
#include <vector>
#include <iostream>
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;
using namespace std;
using namespace edm;

class TupleMuonTau
{



public:
  TupleMuonTau();
  virtual ~TupleMuonTau(){}

  // setters

  void set_p4(LorentzVector);


  // getters

  LorentzVector p4() const;


private:

  LorentzVector m_p4;


};

typedef std::vector<TupleMuonTau> TupleMuonTauCollection;

#endif
