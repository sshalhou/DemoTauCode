#include <vector>
#include <sstream>
#include <string>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

using namespace reco;
using namespace std;

class GenBosonDecayFinder
{

public:
    GenBosonDecayFinder(const reco::GenParticleCollection &);
    ~GenBosonDecayFinder();


};

GenBosonDecayFinder::GenBosonDecayFinder(const reco::GenParticleCollection & genparticles)
{

  cout<<genparticles.size()<<endl;

}


GenBosonDecayFinder::~GenBosonDecayFinder(){}
