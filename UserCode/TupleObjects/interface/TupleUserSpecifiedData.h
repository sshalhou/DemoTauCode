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
using namespace std;
using namespace edm;

class TupleUserSpecifiedData
{



public:
  TupleUserSpecifiedData();
  virtual ~TupleUserSpecifiedData(){}

  // setters

  void set_SampleName(std::string);
  void set_PhysicsProcess(std::string);

  // getters

  std::string SampleName() const;
  std::string PhysicsProcess() const;

private:

  std::string m_SampleName;
  std::string m_PhysicsProcess;



};

typedef std::vector<TupleUserSpecifiedData> TupleUserSpecifiedDataCollection;

#endif
