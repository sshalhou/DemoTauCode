#include "UserCode/TupleObjects/interface/TupleUserSpecifiedData.h"
#include "DataFormats/Math/interface/deltaR.h"

TupleUserSpecifiedData::TupleUserSpecifiedData()
{

  m_SampleName = "NULL";
  m_PhysicsProcess = "NULL";
  m_isNonTopEmbeddedSample = 0;
  m_isTopEmbeddedSample = 0;
  m_MASS = -1.0;

}

void TupleUserSpecifiedData::set_SampleName(std::string astring_) { m_SampleName = astring_;}
std::string TupleUserSpecifiedData::SampleName() const  { return m_SampleName; }

void TupleUserSpecifiedData::set_PhysicsProcess(std::string astring_) { m_PhysicsProcess = astring_;}
std::string TupleUserSpecifiedData::PhysicsProcess() const  { return m_PhysicsProcess; }


void TupleUserSpecifiedData::set_isNonTopEmbeddedSample(bool isNonTopEmbeddedSample_) { m_isNonTopEmbeddedSample = isNonTopEmbeddedSample_;}
bool TupleUserSpecifiedData::isNonTopEmbeddedSample() const  { return m_isNonTopEmbeddedSample; }

void TupleUserSpecifiedData::set_isTopEmbeddedSample(bool isTopEmbeddedSample_) { m_isTopEmbeddedSample = isTopEmbeddedSample_;}
bool TupleUserSpecifiedData::isTopEmbeddedSample() const  { return m_isTopEmbeddedSample; }

void TupleUserSpecifiedData::set_MASS(double MASS_) { m_MASS = MASS_;}
double TupleUserSpecifiedData::MASS() const  { return m_MASS; }
