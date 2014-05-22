#include <vector>
#include <sstream>
#include <string>

#include "UserCode/GenBosonDecayFinder/interface/GenBosonDecayFinder.h"

GenBosonDecayFinder::GenBosonDecayFinder(const GenParticleCollection genparticles)
{

  std::cout<<genparticles.size()<<endl;

}


GenBosonDecayFinder::~GenBosonDecayFinder(){}
