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
  void findMaxPtBosonAndDaugters(const reco::GenParticleCollection&, int &, LorentzVector&,
  int &, LorentzVector&,int &, LorentzVector&,bool&);

private:

  static const int higgsBoson = 25;
  static const int zBoson = 23;
  static const int wBoson = 24;
  static const int electron = 11;
  static const int muon = 13;
  static const int tau = 15;

};

///////////////////////////////////////////////////
///////////////////////////////////////////////////



GenBosonDecayFinder::GenBosonDecayFinder(){}


GenBosonDecayFinder::~GenBosonDecayFinder(){}

void GenBosonDecayFinder::findMaxPtBosonAndDaugters (const reco::GenParticleCollection & genparticles,
int& BosonPdgID, LorentzVector& BosonP4, int& DaughterOnePdgID,
LorentzVector& DaughterOneP4,int& DaughterTwoPdgID, LorentzVector& DaughterTwoP4,
bool& ApplyRecoilCorrection)
{


  for(std::size_t mc = 0; mc < genparticles.size(); ++mc)
    {
      cout<<(genparticles)[mc].pdgId()<<" "<<(genparticles)[mc].status()<<endl;

      if( genparticles[mc].pdgId()  == higgsBoson || genparticles[mc].pdgId()  == zBoson )
      {

        cout<<" have a Z or H event "<<endl;

        BosonPdgID = genparticles[mc].pdgId();

        BosonP4 = genparticles[mc].p4();


      }


    }










}
