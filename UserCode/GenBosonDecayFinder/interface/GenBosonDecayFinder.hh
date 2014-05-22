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


    if( abs(genparticles[mc].pdgId())  == 24 ||
    genparticles[mc].pdgId()  == 23  ||
    genparticles[mc].pdgId()  == 25 )
    {
      // only care about the hard interaction
      if( genparticles[mc].status() == 3)
      {

        // as of yet, we have no correctins for
        // di-Boson events
        // thus, filter those out here
        if(ApplyRecoilCorrection) {ApplyRecoilCorrection = 0; return;}
        else ApplyRecoilCorrection = 1;

        BosonPdgID = genparticles[mc].pdgId();
        BosonP4 = genparticles[mc].p4();

        std::size_t nDaughters = genparticles[mc].numberOfDaughters();
        vector <int> daughter_indices;
        daughter_indices.clear();

        for(std::size_t d = 0; d<nDaughters; ++d )
        {
          int pdgId = abs(genparticles[mc].daughter(d)->pdgId());
          if(pdgId == 11 || pdgId == 13 || pdgId ==15) daughter_indices.push_back(d);
        }


        if(daughter_indices.size()>=1)
        {
          int d1 = daughter_indices[0];
          DaughterOnePdgID  = genparticles[mc].daughter(d1)->pdgId();
          DaughterOneP4  = genparticles[mc].daughter(d1)->p4();

        }

        if(daughter_indices.size()>=1)
        {
          int d2 = daughter_indices[1];
          DaughterTwoPdgID  = genparticles[mc].daughter(d2)->pdgId();
          DaughterTwoP4  = genparticles[mc].daughter(d2)->p4();
        }


        daughter_indices.clear();



        



      }

    }

  }


}
