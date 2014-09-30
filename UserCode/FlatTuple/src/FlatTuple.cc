// -*- C++ -*-
//
// Package:    FlatTuple
// Class:      FlatTuple
//
/**\class FlatTuple FlatTuple.cc TEMP/FlatTuple/src/FlatTuple.cc

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

class FlatTuple : public edm::EDAnalyzer
{
public:
  explicit FlatTuple(const edm::ParameterSet&);
  ~FlatTuple();

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
  edm::InputTag muonTauSrc_;
  std::string NAME_;


  TFile *outFile;
  TTree *lepTauTree;

  //////////////
  // variables for lepTau tree

  std::vector<double> eT_correctedSVFitMass;
  std::vector<double> eT_p4_x;
  std::vector<double> eT_p4_y;
  std::vector<double> eT_p4_z;
  std::vector<double> eT_p4_t;

  std::vector<double> muT_correctedSVFitMass;
  std::vector<double> muT_p4_x;
  std::vector<double> muT_p4_y;
  std::vector<double> muT_p4_z;
  std::vector<double> muT_p4_t;


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
FlatTuple::FlatTuple(const edm::ParameterSet& iConfig):
electronTauSrc_(iConfig.getParameter<edm::InputTag>("electronTauSrc" )),
muonTauSrc_(iConfig.getParameter<edm::InputTag>("muonTauSrc" )),
NAME_(iConfig.getParameter<string>("NAME" ))
{
  //now do what ever initialization is needed




  //////////////////
  // create a file based on the name and sample

  char fname[1000];
  sprintf(fname,"FlatTuple_%s.root",NAME_.c_str());
  cout<<" creating a file of name "<<fname<<endl;
  outFile = new TFile(fname, "RECREATE");
  outFile->cd();


  ///////////////////
  // create the tree
  lepTauTree = new TTree("FlatTuple", "FlatTuple");


  //////////////
  // init values

  eT_correctedSVFitMass.clear();
  eT_p4_x.clear();
  eT_p4_y.clear();
  eT_p4_z.clear();
  eT_p4_t.clear();

  muT_correctedSVFitMass.clear();
  muT_p4_x.clear();
  muT_p4_y.clear();
  muT_p4_z.clear();
  muT_p4_t.clear();


  ///////////////
  // add branches

  lepTauTree->Branch("eT_correctedSVFitMass",&eT_correctedSVFitMass);
  lepTauTree->Branch("eT_p4_x",&eT_p4_x);
  lepTauTree->Branch("eT_p4_y",&eT_p4_y);
  lepTauTree->Branch("eT_p4_z",&eT_p4_z);
  lepTauTree->Branch("eT_p4_t",&eT_p4_t);

  lepTauTree->Branch("muT_correctedSVFitMass",&muT_correctedSVFitMass);
  lepTauTree->Branch("muT_p4_x",&muT_p4_x);
  lepTauTree->Branch("muT_p4_y",&muT_p4_y);
  lepTauTree->Branch("muT_p4_z",&muT_p4_z);
  lepTauTree->Branch("muT_p4_t",&muT_p4_t);







}


FlatTuple::~FlatTuple()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
FlatTuple::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{


  //////////////
  // init values

  eT_correctedSVFitMass.clear();
  eT_p4_x.clear();
  eT_p4_y.clear();
  eT_p4_z.clear();
  eT_p4_t.clear();


  ///////////////
  // get eTaus

  edm::Handle< TupleElectronTauCollection > eTaus;
  iEvent.getByLabel(electronTauSrc_, eTaus);


  for (std::size_t i = 0; i < eTaus->size(); ++i)
    {

      const TupleElectronTau eTau =   ((*eTaus)[i]);
      eT_correctedSVFitMass.push_back(eTau.correctedSVFitMass());
      eT_p4_x.push_back(eTau.p4().x());
      eT_p4_y.push_back(eTau.p4().y());
      eT_p4_z.push_back(eTau.p4().z());
      eT_p4_t.push_back(eTau.p4().t());


    }


  ///////////////
  // get muTaus

  edm::Handle< TupleMuonTauCollection > muTaus;
  iEvent.getByLabel(muonTauSrc_, muTaus);


  for (std::size_t i = 0; i < muTaus->size(); ++i)
    {

      const TupleMuonTau muTau =   ((*muTaus)[i]);
      muT_correctedSVFitMass.push_back(muTau.correctedSVFitMass());
      muT_p4_x.push_back(muTau.p4().x());
      muT_p4_y.push_back(muTau.p4().y());
      muT_p4_z.push_back(muTau.p4().z());
      muT_p4_t.push_back(muTau.p4().t());


    }




    ///////////
    // fill the tree

    if(muTaus->size()+eTaus->size() > 0) lepTauTree->Fill();






















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
  FlatTuple::beginJob()
  {
  }

  // ------------ method called once each job just after ending the event loop  ------------
  void
  FlatTuple::endJob()
  {
    lepTauTree->Write();
    outFile->Close();


  }

  // ------------ method called when starting to processes a run  ------------
  void
  FlatTuple::beginRun(edm::Run const&, edm::EventSetup const&)
  {
  }

  // ------------ method called when ending the processing of a run  ------------
  void
  FlatTuple::endRun(edm::Run const&, edm::EventSetup const&)
  {
  }

  // ------------ method called when starting to processes a luminosity block  ------------
  void
  FlatTuple::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
  {
  }

  // ------------ method called when ending the processing of a luminosity block  ------------
  void
  FlatTuple::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
  {
  }

  // ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
  void
  FlatTuple::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    //The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
  }

  //define this as a plug-in
  DEFINE_FWK_MODULE(FlatTuple);
