#include <vector>
#include <sstream>
#include <string>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;

using namespace reco;
using namespace std;



class GenBosonDecayFinder
{

public:
  GenBosonDecayFinder();
  virtual ~GenBosonDecayFinder();
  void findBosonAndDaugters(const reco::GenParticleCollection&, int &, LorentzVector&,
  int &, LorentzVector&,int &, LorentzVector&,bool&);




};

///////////////////////////////////////////////////
///////////////////////////////////////////////////



GenBosonDecayFinder::GenBosonDecayFinder(){}


GenBosonDecayFinder::~GenBosonDecayFinder(){}

void GenBosonDecayFinder::findBosonAndDaugters (const reco::GenParticleCollection & genparticles,
int& BosonPdgID, LorentzVector& BosonP4, int& DaughterOnePdgID,
LorentzVector& DaughterOneP4,int& DaughterTwoPdgID, LorentzVector& DaughterTwoP4,
bool& ApplyRecoilCorrection)
{

  ApplyRecoilCorrection = 0;

  for(std::size_t mc = 0; mc < genparticles.size(); ++mc)
  {


    if( genparticles[mc].pdgId()  == 23 ||
    genparticles[mc].pdgId()  == 24  ||
    genparticles[mc].pdgId()  == 25 )
    {
      // only care about the hard interaction
      if( genparticles[mc].status() == 3)
      {


        BosonPdgID = genparticles[mc].pdgId();
        BosonP4 = genparticles[mc].p4();

        std::size_t nDaughters = genparticles[mc].numberOfDaughters();

        std::cout<<" num dau "<<nDaughters<<endl;
        if(nDaughters>=1)
        {
          DaughterOnePdgID  = genparticles[mc].daughter(0)->pdgId();
          DaughterOneP4  = genparticles[mc].daughter(0)->p4();
          ApplyRecoilCorrection = 1;
          // if we see this again, it means we have a WW, ZZ, or HH event
          if(ApplyRecoilCorrection) {ApplyRecoilCorrection = 0; return;}
        }

        else if(nDaughters>=2)
        {
          DaughterOnePdgID  = genparticles[mc].daughter(0)->pdgId();
          DaughterOneP4  = genparticles[mc].daughter(0)->p4();
          DaughterTwoPdgID  = genparticles[mc].daughter(1)->pdgId();
          DaughterTwoP4  = genparticles[mc].daughter(1)->p4();
          ApplyRecoilCorrection = 1;
          // if we see this again, it means we have a WW, ZZ, or HH event
          if(ApplyRecoilCorrection) {ApplyRecoilCorrection = 0; return;}
        }

      }

    }

  }


}
