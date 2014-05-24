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
  void set_passFullId(bool);

  // getters

  LorentzVector p4() const;
  LorentzVector genP4() const;
  LorentzVector corrected_p4() const;
  int pdgId() const;
  int charge() const;
  int decayMode() const;
  bool passFullId() const;


private:

  LorentzVector m_p4;
  LorentzVector m_genP4;
  LorentzVector m_corrected_p4;
  int m_pdgId;
  int m_charge;
  int m_decayMode;
  bool m_passFullId;


};

typedef std::vector<TupleTau> TupleTauCollection;

#endif
