#ifndef UserCode_TupleObjects_TupleUserSpecifiedData_h
#define UserCode_TupleObjects_TupleUserSpecifiedData_h


// system include files
#include <memory>



// needed by ntuple UserSpecifiedDatas producer
#include <vector>
#include <iostream>
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;
//using namespace std;
//using namespace edm;

class TupleUserSpecifiedData
{



public:
  TupleUserSpecifiedData();
  virtual ~TupleUserSpecifiedData(){}

  // setters

  void set_SampleName(std::string);
  void set_PhysicsProcess(std::string);
  void set_isNonTopEmbeddedSample(bool);
  void set_isTopEmbeddedSample(bool);
  void set_MASS(double);

  // getters

  std::string SampleName() const;
  std::string PhysicsProcess() const;
  bool isNonTopEmbeddedSample() const;
  bool isTopEmbeddedSample() const;
  bool MASS() const;
private:

  std::string m_SampleName;
  std::string m_PhysicsProcess;
  bool m_isNonTopEmbeddedSample;
  bool m_isTopEmbeddedSample;
  bool m_MASS;

};

typedef std::vector<TupleUserSpecifiedData> TupleUserSpecifiedDataCollection;

#endif
