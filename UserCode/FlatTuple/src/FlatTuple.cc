// -*- C++ -*-
//
// Package:    FlatTree
// Class:      FlatTree
//
/**\class FlatTree FlatTree.cc TEMP/FlatTree/src/FlatTree.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  shalhout shalhout
//         Created:  Tue Jul  1 04:25:53 CDT 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "UserCode/TupleObjects/interface/TupleElectron.h"
#include "UserCode/TupleObjects/interface/TupleMuon.h"
#include "UserCode/TupleObjects/interface/TupleTau.h"
#include "UserCode/TupleObjects/interface/TupleElectronTau.h"
#include "UserCode/TupleObjects/interface/TupleMuonTau.h"


#include <string>
#include "TTree.h"
#include "TFile.h"

using namespace edm;
using namespace std;

typedef math::XYZTLorentzVector LorentzVector;

//
// class declaration
//

class FlatTree : public edm::EDAnalyzer
{
public:
  explicit FlatTree(const edm::ParameterSet&);
  ~FlatTree();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

  // ----------member data ---------------------------


  edm::InputTag electronTauSrc_;
  string NAME_;


  TFile *outFile;
  TTree *lepTauTree;

  //////////////
  // variables for lepTau tree

  std::vector<double> eT_correctedSVFitMass;
  std::vector<LorentzVector> eT_p4;


};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
FlatTree::FlatTree(const edm::ParameterSet& iConfig):
electronTauSrc_(iConfig.getParameter<edm::InputTag>("electronTauSrc" )),
NAME_(iConfig.getParameter<string>("NAME" ))
{
  //now do what ever initialization is needed




  //////////////////
  // create a file based on the name and sample

  char fname[1000];
  sprintf(fname,"FlatTree_%s.root",NAME_.c_str());
  cout<<" creating a file of name "<<fname<<endl;
  outFile = new TFile(fname, "RECREATE");
  outFile->cd();


  ///////////////////
  // create the tree
  lepTauTree = new TTree("FlatTree", "FlatTree");


  //////////////
  // init values

  eT_correctedSVFitMass.clear();
  eT_p4.clear();

  ///////////////
  // add branches

  lepTauTree->Branch("eT_correctedSVFitMass",&eT_correctedSVFitMass);
  lepTauTree->Branch("eT_p4",&eT_p4);









}


FlatTree::~FlatTree()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
FlatTree::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{


  //////////////
  // init values

  eT_correctedSVFitMass.clear();
  eT_p4.clear();


  ///////////////
  // get eTaus

  edm::Handle< TupleElectronTauCollection > eTaus;
  iEvent.getByLabel(electronTauSrc_, eTaus);


  for (std::size_t i = 0; i < eTaus->size(); ++i)
    {

      const TupleElectronTau eTau =   ((*eTaus)[i]);
      eT_correctedSVFitMass.push_back(eTau.correctedSVFitMass());
      eT_p4.push_back(eTau.p4());


    }


    ///////////
    // fill the tree

    lepTauTree->Fill();






















    #ifdef THIS_IS_AN_EVENT_EXAMPLE
    Handle<ExampleData> pIn;
    iEvent.getByLabel("example",pIn);
    #endif

    #ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
    ESHandle<SetupData> pSetup;
    iSetup.get<SetupRecord>().get(pSetup);
    #endif
  }


  // ------------ method called once each job just before starting event loop  ------------
  void
  FlatTree::beginJob()
  {
  }

  // ------------ method called once each job just after ending the event loop  ------------
  void
  FlatTree::endJob()
  {
    lepTauTree->Write();
    outFile->Close();


  }

  // ------------ method called when starting to processes a run  ------------
  void
  FlatTree::beginRun(edm::Run const&, edm::EventSetup const&)
  {
  }

  // ------------ method called when ending the processing of a run  ------------
  void
  FlatTree::endRun(edm::Run const&, edm::EventSetup const&)
  {
  }

  // ------------ method called when starting to processes a luminosity block  ------------
  void
  FlatTree::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
  {
  }

  // ------------ method called when ending the processing of a luminosity block  ------------
  void
  FlatTree::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
  {
  }

  // ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
  void
  FlatTree::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    //The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
  }

  //define this as a plug-in
  DEFINE_FWK_MODULE(FlatTree);
