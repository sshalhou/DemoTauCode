#ifndef UserCode_TupleObjects_TupleJet_h
#define UserCode_TupleObjects_TupleJet_h


// system include files
#include <memory>



// needed by ntuple Taus producer
#include <vector>
#include <iostream>
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;


class TupleJet
{



public:
  TupleJet();
  virtual ~TupleJet(){}

  // setters

  void set_p4(LorentzVector);
  void set_JecShift(double);
  void passesPUjetIDLoose(bool);
  void passesPFjetIDLoose(bool);
  void combinedSecondaryVertexBJetTags(double);
  void partonFlavour(int);
  void isBtagged(bool);


  // getters

  LorentzVector p4() const;
  double JecShift() const;
  bool passesPUjetIDLoose() const;
  bool passesPFjetIDLoose() const;
  double combinedSecondaryVertexBJetTags() const;
  int partonFlavour() const;
  bool isBtagged() const;



private:


  LorentzVector m_p4;
  double m_JecShift;
  bool m_passesPUjetIDLoose;
  bool m_passesPFjetIDLoose;
  double m_combinedSecondaryVertexBJetTags;
  int m_partonFlavour;
  bool m_isBtagged;


};

typedef std::vector<TupleJet> TupleJetCollection;

#endif
