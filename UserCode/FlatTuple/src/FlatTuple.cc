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
  virtual void reInit();

  // ----------member data ---------------------------


  edm::InputTag electronTauSrc_;
  edm::InputTag muonTauSrc_;
  std::string NAME_;


  TFile *outFile;
  TTree *lepTauTree;

  //////////////
  // variables for lepTau tree

  ///////
  // corresponding to electronTau object

  std::vector< double > eT_p4_x , eT_p4_y , eT_p4_z , eT_p4_t ;
  std::vector< double > eT_corrected_p4_x , eT_corrected_p4_y , eT_corrected_p4_z , eT_corrected_p4_t ;
  std::vector< int > eT_electronIndex ;
  std::vector< int > eT_tauIndex ;
  std::vector< double > eT_scalarSumPt ;
  std::vector< double > eT_DR ;
  std::vector< int > eT_sumCharge ;
  std::vector< double > eT_correctedSVFitMass ;
  std::vector< double > eT_rawSVFitMass ;
  std::vector< double > eT_TransverseMass ;
  std::vector< double > eT_rawTransverseMass ;
  std::vector< double > eT_mvaMETraw ;
  std::vector< double > eT_mvaMET ;
  std::vector< double > eT_mvaMETphiRaw ;
  std::vector< double > eT_mvaMETphi ;
  std::vector< int > eT_MAX ;
  std::vector< bool > eT_isGoodTriggerPair ;
  std::vector< int > eT_njets ;
  std::vector< int > eT_nbjets ;
  std::vector< double > eT_jet1P4_x , eT_jet1P4_y , eT_jet1P4_z , eT_jet1P4_t ;
  std::vector< double > eT_jet1RawP4_x , eT_jet1RawP4_y , eT_jet1RawP4_z , eT_jet1RawP4_t ;
  std::vector< double > eT_jet1IDMVA ;
  std::vector< double > eT_jet1BTAGMVA ;
  std::vector< double > eT_jet2P4_x , eT_jet2P4_y , eT_jet2P4_z , eT_jet2P4_t ;
  std::vector< double > eT_jet2RawP4_x , eT_jet2RawP4_y , eT_jet2RawP4_z , eT_jet2RawP4_t ;
  std::vector< double > eT_jet2IDMVA ;
  std::vector< double > eT_jet2BTAGMVA ;
  std::vector< double > eT_cov00 ;
  std::vector< double > eT_cov01 ;
  std::vector< double > eT_cov10 ;
  std::vector< double > eT_cov11 ;
  std::vector< bool > eT_passesTriLeptonVeto ;
  std::vector< bool > eT_passNonTopEmbeddedTriggerAndMass50 ;
  std::vector< bool > eT_passSignalGeneratorMass70to130Cut ;
  std::vector< double > eT_genBosonP4_x , eT_genBosonP4_y , eT_genBosonP4_z , eT_genBosonP4_t ;
  std::vector< double > eT_genTOPp4_x , eT_genTOPp4_y , eT_genTOPp4_z , eT_genTOPp4_t ;
  std::vector< double > eT_genTOPBARp4_x , eT_genTOPBARp4_y , eT_genTOPBARp4_z , eT_genTOPBARp4_t ;
  std::vector< int > eT_numberOfGoodVertices ;
  std::vector< int > eT_PVndof ;
  std::vector< double > eT_PVz ;
  std::vector< double > eT_PVpositionRho ;
  std::vector< double > eT_PVp4_x , eT_PVp4_y , eT_PVp4_z , eT_PVp4_t ;



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

  reInit();




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

  reInit();



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

  void
  FlatTuple::reInit()
  {

    eT_p4_x.clear();
    eT_p4_y.clear();
    eT_p4_z.clear();
    eT_p4_t.clear();
    eT_corrected_p4_x.clear();
    eT_corrected_p4_y.clear();
    eT_corrected_p4_z.clear();
    eT_corrected_p4_t.clear();
    eT_electronIndex.clear();
    eT_tauIndex.clear();
    eT_scalarSumPt.clear();
    eT_DR.clear();
    eT_sumCharge.clear();
    eT_correctedSVFitMass.clear();
    eT_rawSVFitMass.clear();
    eT_TransverseMass.clear();
    eT_rawTransverseMass.clear();
    eT_mvaMETraw.clear();
    eT_mvaMET.clear();
    eT_mvaMETphiRaw.clear();
    eT_mvaMETphi.clear();
    eT_MAX.clear();
    eT_isGoodTriggerPair.clear();
    eT_njets.clear();
    eT_nbjets.clear();
    eT_jet1P4_x.clear();
    eT_jet1P4_y.clear();
    eT_jet1P4_z.clear();
    eT_jet1P4_t.clear();
    eT_jet1RawP4_x.clear();
    eT_jet1RawP4_y.clear();
    eT_jet1RawP4_z.clear();
    eT_jet1RawP4_t.clear();
    eT_jet1IDMVA.clear();
    eT_jet1BTAGMVA.clear();
    eT_jet2P4_x.clear();
    eT_jet2P4_y.clear();
    eT_jet2P4_z.clear();
    eT_jet2P4_t.clear();
    eT_jet2RawP4_x.clear();
    eT_jet2RawP4_y.clear();
    eT_jet2RawP4_z.clear();
    eT_jet2RawP4_t.clear();
    eT_jet2IDMVA.clear();
    eT_jet2BTAGMVA.clear();
    eT_cov00.clear();
    eT_cov01.clear();
    eT_cov10.clear();
    eT_cov11.clear();
    eT_passesTriLeptonVeto.clear();
    eT_passNonTopEmbeddedTriggerAndMass50.clear();
    eT_passSignalGeneratorMass70to130Cut.clear();
    eT_genBosonP4_x.clear();
    eT_genBosonP4_y.clear();
    eT_genBosonP4_z.clear();
    eT_genBosonP4_t.clear();
    eT_genTOPp4_x.clear();
    eT_genTOPp4_y.clear();
    eT_genTOPp4_z.clear();
    eT_genTOPp4_t.clear();
    eT_genTOPBARp4_x.clear();
    eT_genTOPBARp4_y.clear();
    eT_genTOPBARp4_z.clear();
    eT_genTOPBARp4_t.clear();
    eT_numberOfGoodVertices.clear();
    eT_PVndof.clear();
    eT_PVz.clear();
    eT_PVpositionRho.clear();
    eT_PVp4_x.clear();
    eT_PVp4_y.clear();
    eT_PVp4_z.clear();
    eT_PVp4_t.clear();



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
