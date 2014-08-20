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
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "UserCode/TupleObjects/interface/TupleElectron.h"
#include "UserCode/TupleObjects/interface/TupleMuon.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

namespace TupleHelpers
{

  ///////////////////////
  // Integrated Crystal Ball Function

  double IntegratedCrystalBallEfficiencyForElectrons(double m, double m0, double sigma,
  double alpha, double n, double norm) const
  {
    const double sqrtPiOver2 = 1.2533141373;
    const double sqrt2 = 1.4142135624;

    double sig = fabs((double) sigma);

    double t = (m - m0)/sig;

    if (alpha < 0) t = -t;

    double absAlpha = fabs(alpha / sig);
    double a = TMath::Power(n/absAlpha,n)*exp(-0.5*absAlpha*absAlpha);
    double b = absAlpha - n/absAlpha;

    if (a>=std::numeric_limits<double>::max()) return -1. ;

    double ApproxErf ;
    double arg = absAlpha / sqrt2 ;
    if (arg > 5.) ApproxErf = 1 ;
    else if (arg < -5.) ApproxErf = -1 ;
    else ApproxErf = erf(arg) ;

    double leftArea = (1 + ApproxErf) * sqrtPiOver2 ;
    double rightArea = ( a * 1/TMath::Power(absAlpha - b,n-1)) / (n - 1);
    double area = leftArea + rightArea;

    if ( t <= absAlpha )
    {
      arg = t / sqrt2 ;
      if (arg > 5.) ApproxErf = 1 ;
      else if (arg < -5.) ApproxErf = -1 ;
      else ApproxErf = erf(arg) ;
      return norm * (1 + ApproxErf) * sqrtPiOver2 / area ;
    }
    else
    {
      return norm*(leftArea+a*(1/TMath::Power(t-b,n-1)-1/TMath::Power(absAlpha - b,n-1)) / (1 - n))/area;
    }

  }


  /////////////////////////////////
  // fill the trigger weights
  // for the HLT ELE20 and ELE22
  // Triggers
  // based on imp. by Garrett Funk

  void getTriggerWeightsELE20andELE22(bool isRealData,
  double & EffDataELE20andELE22, double & EffMcELE20andELE22,  const TupleElectron electron)
  {

    // return 1.0 if Data, or if trigger not fired
    if(isRealData || !(electron.has_HltMatchEle20() || electron.has_HltMatchEle22()))
    {

      EffDataELE20andELE22 = 1.0;
      EffMcELE20andELE22 = 1.0;
      return;

    }

    // return weights if !Data
    else if((electron.has_HltMatchEle20() || electron.has_HltMatchEle22()))
    {

      double cbELegDataM0 = NAN;
      double cbELegDataSigma = NAN;
      double cbELegDataAlpha = NAN;
      double cbELegDataN = NAN;
      double cbELegDataNorm = NAN;

      double cbELegMCM0 = NAN;
      double cbELegMCSigma = NAN;
      double cbELegMCAlpha = NAN;
      double cbELegMCN = NAN;
      double cbELegMCNorm = NAN;


      if (electron.isEB())
      {
        cbELegDataM0 = 22.9704;
        cbELegDataSigma = 1.0258;
        cbELegDataAlpha = 1.26889;
        cbELegDataN = 1.31024;
        cbELegDataNorm = 1.06409;

        cbELegMCM0 = 21.7243;
        cbELegMCSigma = 0.619015;
        cbELegMCAlpha = 0.739301;
        cbELegMCN = 1.34903;
        cbELegMCNorm = 1.02594;
      }
      else if (electron.isEE())
      {
        cbELegDataM0 = 21.9816;
        cbELegDataSigma = 1.40993;
        cbELegDataAlpha = 0.978597;
        cbELegDataN = 2.33144;
        cbELegDataNorm = 0.937552;

        cbELegMCM0 = 22.1217;
        cbELegMCSigma = 1.34054;
        cbELegMCAlpha = 1.8885;
        cbELegMCN = 1.01855;
        cbELegMCNorm = 4.7241;
      }
      
      EffDataELE20andELE22 = IntegratedCrystalBallEfficiencyForElectrons(electron.p4().pt(),
      cbELegDataM0, cbELegDataSigma, cbELegDataAlpha, cbELegDataN, cbELegDataNorm);
      EffMcELE20andELE22 = IntegratedCrystalBallEfficiencyForElectrons(electron.p4().pt(),
      cbELegMCM0, cbELegMCSigma, cbELegMCAlpha, cbELegMCN, cbELegMCNorm);

      return;
    }

    return;

  }



  /////////////////////////////////
  // fill the event's pile-up
  // weight;  returns 1.0 if data

  void getPileUpWeight(edm::Handle<std::vector<PileupSummaryInfo> > PupInfo,
  bool isRealData, double & puWeight, double & puWeightM1, double & puWeightP1,
  float & NumPileupInt, float & NumTruePileUpInt,
  float & NumPileupIntM1, float & NumTruePileUpIntM1,
  float & NumPileupIntP1, float & NumTruePileUpIntP1  )
  {


    ///////////////
    // non-valid PU Collection


    if(!PupInfo.isValid())
    {

      puWeight = 1.0;
      puWeightM1 = 1.0;
      puWeightP1 = 1.0;
      NumPileupInt = 1.0;
      NumTruePileUpInt = 1.0;
      NumPileupIntM1 = 1.0;
      NumTruePileUpIntM1 = 1.0;
      NumPileupIntP1 = 1.0;
      NumTruePileUpIntP1 = 1.0;

      return;
    }


    /////////////////
    // for non-data, return a pileup weight


    edm::LumiReWeighting LumiWeights_(
    "UserCode/PileUpReWeightFiles/MC_Summer12_PU_S10-600bins.root",
    "UserCode/PileUpReWeightFiles/Data_Pileup_2012_ReRecoPixel-600bins.root",
    "pileup",
    "pileup");


    std::vector<PileupSummaryInfo>::const_iterator PVI;


    for(PVI = PupInfo->begin(); PVI != PupInfo->end(); ++PVI)
    {

      int BX = PVI->getBunchCrossing();



      if(BX==0)
      {
        NumTruePileUpInt = PVI->getTrueNumInteractions();
        NumPileupInt = PVI->getPU_NumInteractions();
      }
      else if(BX == -1)
      {
        NumTruePileUpIntM1 = PVI->getTrueNumInteractions();
        NumPileupIntM1 = PVI->getPU_NumInteractions();
      }
      else if(BX == 1)
      {
        NumTruePileUpIntP1 = PVI->getTrueNumInteractions();
        NumPileupIntP1 = PVI->getPU_NumInteractions();
      }
    }

    if(isRealData==1)
    {
      puWeight = 1.0;
      puWeightM1 = 1.0;
      puWeightP1 = 1.0;
    }
    else
    {
      puWeight = LumiWeights_.weight( NumTruePileUpInt );
      puWeightM1 = LumiWeights_.weight( NumTruePileUpIntM1 );
      puWeightP1 = LumiWeights_.weight( NumTruePileUpIntP1 );
    }
    return;

  }


  ////////////////////////////////
  // fill a vector with
  // indices of jets that
  // have DR > 0.1 overlap eliminated

  void getNonOverlappingJetIndices(edm::Handle<edm::View<pat::Jet> > jets,
  std::vector <unsigned int> & goodIndices, double DRcut)
  {

    /////////////////////
    // store the jets that do not overlap
    // with other jets, in case of overlap
    // remove the lower pt jet's index
    bool keep_jet_index = 1;
    goodIndices.clear();


    for (std::size_t i = 0; i < jets->size(); ++i)
    {

      const pat::Jet & patjet_i = jets->at(i);


      for (std::size_t ii = 0; ii < jets->size(); ++ii)
      {

        const pat::Jet & patjet_ii = jets->at(ii);
        if(patjet_i.pt() <= patjet_ii.pt() && deltaR(patjet_i.p4(),patjet_ii.p4())<DRcut && i!=ii)
        {

          keep_jet_index = 0;

        }




      }

      /////////
      // check if we should store
      // the jet's index

      if(keep_jet_index) goodIndices.push_back(i);

    }


    return;




  }



  ////////////////////////////////
  // set the pair-wise TriLepton Veto


  bool pairPassesTriLeptonVeto(unsigned int eIndex,
  unsigned int muIndex,
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
        if(electron.isTriLeptonVetoCandidate()) return 0;

      }

    }

    /////////
    // loop over the muons


    for (std::size_t i = 0; i < muons->size(); ++i)
    {
      if(i!=muIndex)
      {
        const TupleMuon muon =   ((*muons)[i]);
        if(muon.isTriLeptonVetoCandidate()) return 0;




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

    //    std::cout<<" WARNING electron category = "<<category<<" -- it should be 4,5, or 6"<<std::endl;
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
