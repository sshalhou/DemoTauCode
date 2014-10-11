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
  void set_crossSection(double);
  void set_branchingFraction(double);
  void set_numberEvents(int);

  // getters

  std::string SampleName() const;
  std::string PhysicsProcess() const;
  bool isNonTopEmbeddedSample() const;
  bool isTopEmbeddedSample() const;
  double MASS() const;
  double crossSection() const;
  double branchingFraction() const;
  int numberEvents() const;

private:

  std::string m_SampleName;
  std::string m_PhysicsProcess;
  bool m_isNonTopEmbeddedSample;
  bool m_isTopEmbeddedSample;
  double m_MASS;
  double m_crossSection;
  double m_branchingFraction;
  int m_numberEvents;

};

typedef std::vector<TupleUserSpecifiedData> TupleUserSpecifiedDataCollection;

#endif
