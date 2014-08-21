#include "UserCode/TupleObjects/interface/TupleUserSpecifiedData.h"
#include "DataFormats/Math/interface/deltaR.h"

TupleUserSpecifiedData::TupleUserSpecifiedData()
{

  m_SampleName = "NULL";
  m_PhysicsProcess = "NULL";
  m_isNonTopEmbeddedSample = 0;
  m_isTopEmbeddedSample = 0;


}

void TupleUserSpecifiedData::set_SampleName(std::string astring_) { m_SampleName = astring_;}
std::string TupleUserSpecifiedData::SampleName() const  { return m_SampleName; }

void TupleUserSpecifiedData::set_PhysicsProcess(std::string astring_) { m_PhysicsProcess = astring_;}
std::string TupleUserSpecifiedData::PhysicsProcess() const  { return m_PhysicsProcess; }


void TupleUserSpecifiedData::set_isNonTopEmbeddedSample(bool astring_) { m_isNonTopEmbeddedSample = isNonTopEmbeddedSample_;}
bool TupleUserSpecifiedData::isNonTopEmbeddedSample() const  { return m_isNonTopEmbeddedSample; }

void TupleUserSpecifiedData::set_isTopEmbeddedSample(bool astring_) { m_isTopEmbeddedSample = astring_;}
bool TupleUserSpecifiedData::isTopEmbeddedSample() const  { return m_isTopEmbeddedSample; }
