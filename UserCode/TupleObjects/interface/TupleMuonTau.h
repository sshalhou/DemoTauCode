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
  void set_corrected_p4(LorentzVector);
  void set_muonIndex(int);
  void set_tauIndex(int);
  void set_scalarSumPt(LorentzVector,LorentzVector);
  void set_DR(LorentzVector,LorentzVector);
  void set_sumCharge(int, int);
  void set_correctedSVFitMass(double);
  void set_TransverseMass(double);
  void set_mvaMETraw(double);
  void set_mvaMET(double);
  void set_mvaMETphiRaw(double);
  void set_mvaMETphi(double);
  void set_MAX(int);

  // getters

  LorentzVector p4() const;
  LorentzVector corrected_p4() const;
  int muonIndex() const;
  int tauIndex() const;
  double scalarSumPt() const;
  double DR() const;
  int sumCharge() const;
  double correctedSVFitMass() const;
  double TransverseMass() const;
  double mvaMETraw() const;
  double mvaMET() const;
  double mvaMETphiRaw() const;
  double mvaMETphi()const;
  int MAX() const;

private:

  LorentzVector m_p4;
  LorentzVector m_corrected_p4;
  int m_muonIndex;
  int m_tauIndex;
  double m_scalarSumPt;
  double m_DR;
  int m_sumCharge;
  double m_correctedSVFitMass;
  double m_TransverseMass;
  double m_mvaMETraw;
  double m_mvaMET;
  double m_mvaMETphiRaw;
  double m_mvaMETphi;
  int m_MAX;

};

typedef std::vector<TupleMuonTau> TupleMuonTauCollection;

#endif
