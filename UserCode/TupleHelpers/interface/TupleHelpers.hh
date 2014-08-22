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
#include "TF1.h"
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
#include "UserCode/TupleObjects/interface/TupleTau.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "UserCode/TupleObjects/interface/TupleUserSpecifiedData.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"


namespace TupleHelpers
{

  ///////////////////////
  // Integrated Crystal Ball Function

  double IntegratedCrystalBallEfficiency(double m, double m0, double sigma,
  double alpha, double n, double norm)
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

  ///////////////////////
  // for non-tt embedded samples, the normal trigger paths
  // and matching is not done
  // instead we check that the gen level lepton mass is > 50
  // and check the DoubleMu trigger wasAccept()

  bool passNonTopEmbeddedTriggerAndMass50(const TupleUserSpecifiedData userData0,
  const reco::GenParticleCollection & genparticles, const pat::TriggerPathCollection* paths)
  {
    bool pass = 1;

    /////////////
    // check if it is not
    // a non-tt embedded sample
    // return 1 for anything other than
    // nonTop embedded

    if(userData0.isNonTopEmbeddedSample()!=1 && 1==11)
    {
      pass = 1;
      return pass;
    }


    if(userData0.isNonTopEmbeddedSample()==1 || 1==1)
    {

      bool triggerOK = 0;

      std::vector<std::string> doubleMuPaths;
      doubleMuPaths.clear();
      doubleMuPaths.push_back("HLT_Mu17_Mu8_v16");
      doubleMuPaths.push_back("HLT_Mu17_Mu8_v17");
      doubleMuPaths.push_back("HLT_Mu17_Mu8_v18");
      doubleMuPaths.push_back("HLT_Mu17_Mu8_v19");
      doubleMuPaths.push_back("HLT_Mu17_Mu8_v20");
      doubleMuPaths.push_back("HLT_Mu17_Mu8_v21");
      doubleMuPaths.push_back("HLT_Mu17_Mu8_v22");

      for(size_t i = 0; i<doubleMuPaths.size(); ++i)
      {
        for (size_t ii = 0; ii < paths->size(); ++ii)
        {

          const pat::TriggerPath& path = paths->at(ii);
          if(path.name().find(doubleMuPaths[i])!= std::string::npos)
          {

            if(path.wasAccept() && path.wasRun())
            {
              std::cout<<" path "<<doubleMuPaths[i]<<" found and wasAccept = "<<path.wasAccept();
              std::cout<<" in form "<<path.name()<<"\n";
              triggerOK = 1;
            }
          }
        }
      }




    }



    return pass;
  }


  ///////////////////////
  // for SUSY signal samples,
  // must reject events outside of
  // 70% to 130% of the nominal
  // generator mass


  bool passSignalGeneratorMass70to130Cut(const TupleUserSpecifiedData userData0,
  const reco::GenParticleCollection & genparticles)
  {
    bool pass = 1;


    return pass;
  }


  ////////////////////////////////////////////////////////////////
  // IMPORTANT NOTE: should be applied to events
  // with pT(tau) > 140 GeV (barrel) and pT(tau)>60 GeV in end caps.
  // Should not be applied otherwise.
  // For barrel (end caps), weight for tau with pT > 800 (400)
  // is weight for pT = 800 (400) GeV.



  void getHighPtHadronicTauTriggerWeights(const TupleTau tau, double & EffDataHighPtTauTrigger,
  double & EffMcHighPtTauTrigger)
  {

    double ABSETA = fabs(tau.p4().eta());
    double PT = tau.p4().pt();

    ///////////////////////
    // if PT < 140 in the barrel
    // or if  PT < 60 in the endcaps
    // the weights should be set to
    // 1.0

    if((ABSETA<1.5 && PT<140) || (ABSETA>=1.5 && PT<60))
    {
      EffDataHighPtTauTrigger = 1.0;
      EffMcHighPtTauTrigger = 1.0;
      return;
    }

    ////////////////////////
    // compute weights for high
    // pt barrel muon, max valid
    // PT is 800

    if((ABSETA<1.5 && PT>=140))
    {
      double PTx = PT;
      if(PT>800) PTx = 800;

      TF1 *TWBarrel = new TF1("AddTWBarrel","1-9.01280e-04*(x-140) + 4.81592e-07*(x-140)*(x-140)",0.,800.);

      EffDataHighPtTauTrigger  = 0.3+0.7*TWBarrel->Eval(PTx);
      EffMcHighPtTauTrigger    = TWBarrel->Eval(PTx);

      delete TWBarrel;

    }

    ////////////////////////
    // compute weights for high
    // pt endcap muon, max valid
    // PT is 400

    if((ABSETA>=1.5 && PT>=60))
    {
      double PTx = PT;
      if(PT>400) PTx = 400;

      TF1 *TWEndcaps = new TF1("AddTWEndcaps","1-1.81148e-03*(x-60) + 5.44335e-07*(x-60)*(x-60)",0.,800.);

      EffDataHighPtTauTrigger  = 0.3+0.7*TWEndcaps->Eval(PTx);
      EffMcHighPtTauTrigger    = TWEndcaps->Eval(PTx);

      delete TWEndcaps;

    }

    ///////////
    // default to 1.0

    EffDataHighPtTauTrigger = 1.0;
    EffMcHighPtTauTrigger = 1.0;
    return;




  }


  /////////////////////////////////
  // fill the trigger weights
  // for the HLT ISOMU and ISOMU17
  // Triggers
  // based on imp. by Garrett Funk
  // important to keep the ratio sep.
  // since for embedded samples
  // we only apply the Data Value as the weight
  // instead of the ratio as for MC

  void getTriggerWeightsISOMU17andISOMU18(bool isRealData,
  double & EffDataISOMU17andISOMU18, double & EffMcISOMU17andISOMU18,  const TupleMuon muon,
  const TupleUserSpecifiedData userData0)
  {

    //////////////////////////
    // return 1.0 if Data
    // and is not an embedded sample

    if( (isRealData && !(userData0.isTopEmbeddedSample() || userData0.isNonTopEmbeddedSample())) )
    {

      EffDataISOMU17andISOMU18 = 1.0;
      EffMcISOMU17andISOMU18 = 1.0;
      return;

    }


    // return weights if !Data
    else
    {


      double MCpar[5] = {NAN,NAN,NAN,NAN,NAN};
      double DATApar[5] = {NAN,NAN,NAN,NAN,NAN};
      double ETA = muon.p4().eta();

      if(ETA<-1.2)
      {
        DATApar[0] = 15.9977;     MCpar[0] = 16.0051;
        DATApar[1] = 7.64004e-05; MCpar[1] = 2.45144e-05;
        DATApar[2] = 6.4951e-08;  MCpar[2] = 4.3335e-09;
        DATApar[3] = 1.57403;     MCpar[3] = 1.66134;
        DATApar[4] = 0.865325;    MCpar[4] = 0.87045;
      }
      else if(-1.2 <= ETA && ETA < -0.8 )
      {
        DATApar[0] = 17.3974;     MCpar[0] = 17.3135;
        DATApar[1] = 0.804001;    MCpar[1] = 0.747636;
        DATApar[2] = 1.47145;     MCpar[2] = 1.21803;
        DATApar[3] = 1.24295;     MCpar[3] = 1.40611;
        DATApar[4] = 0.928198;    MCpar[4] = 0.934983;
      }
      else if(-0.8 <= ETA && ETA < 0)
      {
        DATApar[0] = 16.4307;     MCpar[0] = 15.9556;
        DATApar[1] = 0.226312;    MCpar[1] = 0.0236127;
        DATApar[2] = 0.265553;    MCpar[2] = 0.00589832;
        DATApar[3] = 1.55756;     MCpar[3] = 1.75409;
        DATApar[4] = 0.974462;    MCpar[4] = 0.981338;
      }
      else if(0.0 <= ETA && ETA < 0.8)
      {

        DATApar[0] = 17.313;     MCpar[0] = 15.9289;
        DATApar[1] = 0.662731;   MCpar[1] = 0.0271317;
        DATApar[2] = 1.3412;     MCpar[2] = 0.00448573;
        DATApar[3] = 1.05778;    MCpar[3] = 1.92101;
        DATApar[4] = 1.26624;    MCpar[4] = 0.978625;

      }
      else if(0.8 <= ETA && ETA < 1.2)
      {

        DATApar[0] = 16.9966;     MCpar[0] = 16.5678;
        DATApar[1] = 0.550532;    MCpar[1] = 0.328333;
        DATApar[2] = 0.807863;    MCpar[2] = 0.354533;
        DATApar[3] = 1.55402;     MCpar[3] = 1.67085;
        DATApar[4] = 0.885134;    MCpar[4] = 0.916992;
      }
      else if(1.2 <= ETA)
      {
        DATApar[0] = 15.9962;    MCpar[0] = 15.997;
        DATApar[1] = 0.000106195;    MCpar[1] = 7.90069e-05;
        DATApar[2] = 4.95058e-08;    MCpar[2] = 4.40036e-08;
        DATApar[3] = 1.9991;    MCpar[3] = 1.66272;
        DATApar[4] = 0.851294;    MCpar[4] = 0.884502;
      }





      EffDataISOMU17andISOMU18 = IntegratedCrystalBallEfficiency(muon.p4().pt(),
      DATApar[0], DATApar[1], DATApar[2], DATApar[3], DATApar[4]);
      EffMcISOMU17andISOMU18 = IntegratedCrystalBallEfficiency(muon.p4().pt(),
      MCpar[0], MCpar[1], MCpar[2], MCpar[3], MCpar[4]);


      /////////
      // even if embedded, keep both values
      // although final weight for embedded is just  EffDataELE20andELE22
      // and not the ratio

      return;
    }

    return;





  }


  /////////////////////////////////
  // fill the trigger weights
  // for the HLT ELE20 and ELE22
  // Triggers
  // based on imp. by Garrett Funk
  // important to keep the ratio sep.
  // since for embedded samples
  // we only apply the Data Value as the weight
  // instead of the ratio as for MC

  void getTriggerWeightsELE20andELE22(bool isRealData,
  double & EffDataELE20andELE22, double & EffMcELE20andELE22,  const TupleElectron electron,
  const TupleUserSpecifiedData userData0)
  {


    //////////////////////////
    // return 1.0 if Data, or if trigger not fired
    // and is not an embedded sample

    if( (isRealData && !(userData0.isTopEmbeddedSample() || userData0.isNonTopEmbeddedSample())) )
    {

      EffDataELE20andELE22 = 1.0;
      EffMcELE20andELE22 = 1.0;
      return;

    }

    // return weights if !Data
    else
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


      if ( fabs(electron.p4().eta()) < 1.479) // barrel
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
      else // endcap
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

      EffDataELE20andELE22 = IntegratedCrystalBallEfficiency(electron.p4().pt(),
      cbELegDataM0, cbELegDataSigma, cbELegDataAlpha, cbELegDataN, cbELegDataNorm);
      EffMcELE20andELE22 = IntegratedCrystalBallEfficiency(electron.p4().pt(),
      cbELegMCM0, cbELegMCSigma, cbELegMCAlpha, cbELegMCN, cbELegMCNorm);

      /////////
      // even if embedded, keep both values
      // although final weight for embedded is just  EffDataELE20andELE22
      // and not the ratio

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
