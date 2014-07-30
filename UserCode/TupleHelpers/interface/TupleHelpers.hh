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
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "UserCode/TupleObjects/interface/TupleElectron.h"
#include "UserCode/TupleObjects/interface/TupleMuon.h"



namespace TupleHelpers
{


  ////////////////////////////////
  // set the pair-wise TriLepton Veto


  bool pairPassesTriLeptonVeto(int eIndex,
  int muIndex,
  edm::Handle< TupleElectronCollection > electrons,
  edm::Handle< TupleMuonCollection > muons)
  {


    /////////
    // loop over the electrons

    for (std::size_t i = 0; i < electrons->size(); ++i)
    {

      if(i!=eIndex)
      {

      const TupleElectron electron =   ((*electrons)[i]);
      if(electron->isTriLeptonVetoCandidate()) return 0;

      }

    }

    /////////
    // loop over the muons


    for (std::size_t i = 0; i < muons->size(); ++i)
    {
      if(i!=muIndex)
      {
      const TupleMuon muon =   ((*muons)[i]);
      if(muon->isTriLeptonVetoCandidate()) return 0;




      }
    }
    return 1;

  }



  ////////////////////////////////////////////////////

  ///////////////////
  // create a transverse mass
  // calculator given any
  // combination of the various
  // vector types floating around here

  template <class SomeVector, class AnotherVector>
  inline double GetTransverseMass(SomeVector V1, AnotherVector V2)
  {

    double pTxMET = sqrt(V1.x()*V1.x()+V1.y()*V1.y())*sqrt(V2.x()*V2.x()+V2.y()*V2.y());
    double CosDphi = cos(deltaPhi(V1.phi(), V2.phi()));
    double MtSq = (2 * pTxMET*(1-CosDphi));
    return sqrt(MtSq);

  }


  ///////////////
  // new working points
  // for tau anti-e mva


  bool passAntiEMVA(int iCat, float raw, int WP=1)
  {

    if(iCat<0) return false;
    if(iCat>15) return true;

    float cutsLoose[16] =
    {0.835,0.831,0.849,0.859,0.873,0.823,0.85,0.855,0.816,0.861,0.862,0.847,0.893,0.82,0.845,0.851};
    float cutsMedium[16] =
    {0.933,0.921,0.944,0.945,0.918,0.941,0.981,0.943,0.956,0.947,0.951,0.95,0.897,0.958,0.955,0.942};
    float cutsTight[16] =
    {0.96,0.968,0.971,0.972,0.969,0.959,0.981,0.965,0.975,0.972,0.974,0.971,0.897,0.971,0.961,0.97};
    float cutsVeryTight[16] =
    {0.978,0.98,0.982,0.985,0.977,0.974,0.989,0.977,0.986,0.983,0.984,0.983,0.971,0.987,0.977,0.981};

    float cut=0;
    if(WP==0) cut = cutsLoose[iCat];
    if(WP==1) cut = cutsMedium[iCat];
    if(WP==2) cut = cutsTight[iCat];
    if(WP==3) cut = cutsVeryTight[iCat];
    return (raw>cut);

  }


  ///////////////
  // get electron
  // category as defined
  // here https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingSummer2013#Electron_ID

  int getMVAElectronIdCategory(double pt, double superClusterEta, std::string LOOSE_TIGHT="TIGHT")
  {

    int category = -1;

    // LOOSE ID

    if(LOOSE_TIGHT.compare("LOOSE")==0)
    {

      if( !(pt>20) )
      {

        if(fabs(superClusterEta) <= 0.8) category = 1;
        else if(fabs(superClusterEta) > 0.8 && fabs(superClusterEta) <= 1.479) category = 2;
        else if(fabs(superClusterEta) > 1.479) category = 3;

      }
      else
      {

        if(fabs(superClusterEta) <= 0.8) category = 4;
        else if(fabs(superClusterEta) > 0.8 && fabs(superClusterEta) <= 1.479) category = 5;
        else if(fabs(superClusterEta) > 1.479) category = 6;


      }

    }

    // TIGHT ID

    if(LOOSE_TIGHT.compare("TIGHT")==0)
    {

      if( (pt>20) )
      {

        if(fabs(superClusterEta) <= 0.8) category = 4;
        else if(fabs(superClusterEta) > 0.8 && fabs(superClusterEta) <= 1.479) category = 5;
        else if(fabs(superClusterEta) > 1.479) category = 6;

      }

    }


    return category;
  }


  //////////////////
  // check if passes mvaNonTrigV0 'tight ID'
  // as defined
  // here https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingSummer2013#Electron_ID

  bool doesItPassTightMVANonTrigV0(int category, double mva)
  {

    if(category == 4 && mva > 0.925 ) return 1;
    if(category == 5 && mva > 0.975 ) return 1;
    if(category == 6 && mva > 0.985 ) return 1;

    std::cout<<" WARNING electron category = "<<category<<" -- it should be 4,5, or 6"<<std::endl;
    return 0;

  }



  ///////////////
  // WP95 cut based electron
  // ID (return true if passes)


  bool passWP95(double superClusterEta,double sigIetaIeta,double deltaEta, double deltaPhi, double HE, double dZ_vtx)
  {

    bool passesAllCuts = 1;

    /////////
    // barrel

    if( fabs(superClusterEta) <= 1.479 )
    {

      if(! (sigIetaIeta<0.01) ) passesAllCuts = 0;
      if(! (deltaEta<0.007) ) passesAllCuts = 0;
      if(! (deltaPhi<0.8) ) passesAllCuts = 0;
      if(! (HE<0.15) ) passesAllCuts = 0;
      if(! (dZ_vtx<0.2) ) passesAllCuts = 0;
      if(passesAllCuts) return 1;

    }

    ////////
    // endcap


    else if( fabs(superClusterEta) > 1.479  && fabs(superClusterEta) < 2.5 )
    {

      if(! (sigIetaIeta<0.03) ) passesAllCuts = 0;
      if(! (deltaEta<0.01) ) passesAllCuts = 0;
      if(! (deltaPhi<0.7) ) passesAllCuts = 0;
      if(! (HE<999) ) passesAllCuts = 0;
      if(! (dZ_vtx<0.2) ) passesAllCuts = 0;
      if(passesAllCuts) return 1;

    }


    return 0;

  }



  ////////////////////////////////////////////////////
}
