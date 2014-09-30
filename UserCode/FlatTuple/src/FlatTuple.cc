#include "UserCode/FlatTuple/interface/FlatTuple.h"

#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/TrackReco/interface/HitPattern.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHit.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "UserCode/TupleObjects/interface/TupleElectron.h"
#include "UserCode/TupleObjects/interface/TupleMuon.h"
#include "UserCode/TupleObjects/interface/TupleTau.h"
#include "UserCode/TupleObjects/interface/TupleElectronTau.h"
#include "UserCode/TupleObjects/interface/TupleMuonTau.h"


#include <TMath.h>

int FlatTuple::verbosity_ = 0;

FlatTuple::FlatTuple(const edm::ParameterSet& iConfig):
electronTauSrc_(iConfig.getParameter<edm::InputTag>("electronTauSrc" )),
NAME_(iConfig.getParameter<std::string>("NAME" )),
lepTauTree_(0)
{
}

FlatTuple::~FlatTuple()
{
}

void FlatTuple::beginJob()
{

  ///////////////////
  // create TTree
  edm::Service<TFileService> fs;
  lepTauTree_ = fs->make<TTree>("flatTuple", "flatTuple");

  ///////////////////
  // add branches

  addBranchD("eT_correctedSVFitMass");
  addBranch_EnPxPyPz("eT_p4");



}


void FlatTuple::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  ///////////////
  // get eTaus

  edm::Handle< TupleElectronTauCollection > eTaus;
  iEvent.getByLabel(electronTauSrc_, eTaus);


  for (std::size_t i = 0; i < eTaus->size(); ++i)
    {
      setValeD("eT_correctedSVFitMass" ,eTau.correctedSVFitMass());
      setValue_EnPxPyPz("eT_p4", eTau.p4());



      //////////////////////
      // fill all values into TTree

      assert(lepTauTree_);
      lepTauTree_->Fill();


    }



void FlatTuple::addBranchD(const std::string& name)
{
  assert(branches_.count(name) == 0);
  std::string name_and_format = name + "/F";
  ntuple_->Branch(name.c_str(), &branches_[name].valueD_, name_and_format.c_str());
}

void FlatTuple::addBranchI(const std::string& name)
{
  assert(branches_.count(name) == 0);
  std::string name_and_format = name + "/I";
  ntuple_->Branch(name.c_str(), &branches_[name].valueI_, name_and_format.c_str());
}

void FlatTuple::addBranchL(const std::string& name)
{
  assert(branches_.count(name) == 0);
  std::string name_and_format = name + "/L";
  ntuple_->Branch(name.c_str(), &branches_[name].valueL_, name_and_format.c_str());
}

void FlatTuple::printBranches(std::ostream& stream)
{
  stream << "<FlatTuple::printBranches>:" << std::endl;
  stream << " registered branches for module = " << moduleLabel_ << std::endl;
  for ( branchMap::const_iterator branch = branches_.begin();
	branch != branches_.end(); ++branch ) {
    stream << " " << branch->first << std::endl;
  }
  stream << std::endl;
}

void FlatTuple::setValueD(const std::string& name, double value)
{
  if ( verbosity_ ) std::cout << "branch = " << name << ": value = " << value << std::endl;
  branchMap::iterator branch = branches_.find(name);
  if ( branch != branches_.end() ) {
    branch->second.valueD_ = value;
  } else {
    throw cms::Exception("InvalidParameter")
      << "No branch with name = " << name << " defined !!\n";
  }
}

void FlatTuple::setValueI(const std::string& name, int value)
{
  if ( verbosity_ ) std::cout << "branch = " << name << ": value = " << value << std::endl;
  branchMap::iterator branch = branches_.find(name);
  if ( branch != branches_.end() ) {
    branch->second.valueI_ = value;
  } else {
    throw cms::Exception("InvalidParameter")
      << "No branch with name = " << name << " defined !!\n";
  }
}

void FlatTuple::setValueL(const std::string& name, long value)
{
  if ( verbosity_ ) std::cout << "branch = " << name << ": value = " << value << std::endl;
  branchMap::iterator branch = branches_.find(name);
  if ( branch != branches_.end() ) {
    branch->second.valueL_ = value;
  } else {
    throw cms::Exception("InvalidParameter")
      << "No branch with name = " << name << " defined !!\n";
  }
}

//
//-------------------------------------------------------------------------------
//

void FlatTuple::addBranch_EnPxPyPz(const std::string& name)
{
  addBranchD(std::string(name).append("En"));
  addBranchD(std::string(name).append("P"));
  addBranchD(std::string(name).append("Px"));
  addBranchD(std::string(name).append("Py"));
  addBranchD(std::string(name).append("Pz"));
  addBranchD(std::string(name).append("M"));
  addBranchD(std::string(name).append("Eta"));
  addBranchD(std::string(name).append("Phi"));
  addBranchD(std::string(name).append("Pt"));
}
//
//-------------------------------------------------------------------------------
//

void FlatTuple::setValue_EnPxPyPz(const std::string& name, const reco::Candidate::LorentzVector& p4)
{
  setValueD(std::string(name).append("En"), p4.E());
  setValueD(std::string(name).append("P"), p4.P());
  setValueD(std::string(name).append("Px"), p4.px());
  setValueD(std::string(name).append("Py"), p4.py());
  setValueD(std::string(name).append("Pz"), p4.pz());
  setValueD(std::string(name).append("M"), p4.M());
  setValueD(std::string(name).append("Eta"), p4.eta());
  setValueD(std::string(name).append("Phi"), p4.phi());
  setValueD(std::string(name).append("Pt"), p4.pt());
}

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(FlatTuple);



}
