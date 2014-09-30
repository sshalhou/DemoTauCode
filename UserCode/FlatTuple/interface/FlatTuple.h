#ifndef UserCode_FlatTuple_h
#define UserCode_FlatTuple_h

/** \class FlatTuple
 *
 * Produce an edm free Ntuple containing info for eTau and muTau pairs
 *
 * \author Shalhout Shalhout, UC Davis
 *
 * \author Christian Veelken, LLR (addBranch and setValue members)
 *
 */

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Utilities/interface/Exception.h"

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

#include <TTree.h>

#include <map>
#include <string>
#include <vector>
#include <ostream>

class FlatTuple : public edm::EDProducer
{
 public:

  FlatTuple(const edm::ParameterSet&);
  ~FlatTuple();

  void produce(edm::Event&, const edm::EventSetup&);
  void beginJob();

 private:

  void addBranchD(const std::string&);
  void addBranchI(const std::string&);
  void addBranchL(const std::string&);
  void addBranch_EnPxPyPz(const std::string&);

  void printBranches(std::ostream&);

  void setValueD(const std::string&, double);
  void setValueI(const std::string&, int);
  void setValueL(const std::string&, long);
  void setValue_EnPxPyPz(const std::string&, const reco::Candidate::LorentzVector&);


  std::string NAME_;
  edm::InputTag electronTauSrc_;

  typedef std::vector<edm::InputTag> vInputTag;

  typedef std::vector<std::string> vstring;

  struct branchEntryType
  {
    Double_t valueD_;
    Int_t valueI_;
    Long_t valueL_;
  };

  typedef std::map<std::string, branchEntryType> branchMap; // key = branch name
  branchMap branches_;

  TTree* lepTauTree_;

  static int verbosity_;
};

#endif
