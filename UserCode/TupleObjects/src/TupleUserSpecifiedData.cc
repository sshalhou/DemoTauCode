#include "UserCode/TupleObjects/interface/TupleUserSpecifiedData.h"
#include "DataFormats/Math/interface/deltaR.h"

TupleUserSpecifiedData::TupleUserSpecifiedData()
{

  SampleName = "NULL";
  PhysicsProcess = "NULL";

}

void TupleUserSpecifiedData::set_SampleName(std::string astring_) { m_SampleName = astring_;}
std::string TupleUserSpecifiedData::SampleName() const  { return m_SampleName; }

void TupleUserSpecifiedData::set_PhysicsProcess(std::string astring_) { m_PhysicsProcess = astring_;}
std::string TupleUserSpecifiedData::PhysicsProcess() const  { return m_PhysicsProcess; }
