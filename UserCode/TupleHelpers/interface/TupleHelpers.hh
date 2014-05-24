// system include files
#include <memory>
#include <string>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include <vector>
#include <iostream>
#include <math.h>
#include "DataFormats/Math/interface/LorentzVector.h"
#include "TauAnalysis/CandidateTools/interface/NSVfitStandaloneAlgorithm.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "Math/GenVector/VectorUtil.h"
#include "DataFormats/Math/interface/deltaPhi.h"


namespace TupleHelpers
{


  ///////////////////
  // create a transverse mass
  // calculator given any
  // combination of the various
  // vector types floating around here

  template <class SomeVector>
  template <class AnotherVector>

  inline double GetTransverseMass(SomeVector V1, AnotherVector V2)
  {

    double pTxMET = V1.pt()*V2.pt();
    double CosDphi = math::cos(deltaPhi(V1.phi(), V2.phi()));
    double MtSq = 2 * pTxMET(1-CosDphi);
    return math::sqrt(MtSq);

  }



}
