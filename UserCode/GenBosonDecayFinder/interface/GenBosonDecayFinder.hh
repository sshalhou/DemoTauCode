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

  const higgsBoson = 25;
  const zBoson = 23;
  const wBoson = 24;
  const electron = 11;
  const muon = 13;
  const tau = 15;

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

  for(std::size_t i = 0; i < genparticles.size(); ++i)
    {

      const GenParticle & mc = (*genParticles)[i];
      cout<<mc.pdgId()<<" "<<mc.status()<<endl;
      cout<< higgsBoson <<endl;



    }










}
