#ifndef UserCode_TupleObjects_TupleGen_h
#define UserCode_TupleObjects_TupleGen_h


// system include files
#include <memory>



// needed by ntuple Taus producer
#include <vector>
#include <iostream>
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;


class TupleGen
{



public:
  TupleGen();
  virtual ~TupleGen(){}

  // setters

  void set_p4(LorentzVector);
  void set_pdgId(int);
  void set_status(int);




  // getters

  LorentzVector p4() const;
  int pdgId() const;
  int status() const;



private:

  LorentzVector m_p4;
  int m_pdgId;
  int m_status;


};

typedef std::vector<TupleGen> TupleGenCollection;

#endif
