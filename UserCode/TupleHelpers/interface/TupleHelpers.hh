// system include files
#include <memory>
#include <string>
#include <stdio.h>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include <vector>
#include <iostream>
#include <math.h>
#include "TF1.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "TauAnalysis/CandidateTools/interface/NSVfitStandaloneAlgorithm.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "Math/GenVector/VectorUtil.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "UserCode/TupleObjects/interface/TupleElectron.h"
#include "UserCode/TupleObjects/interface/TupleMuon.h"
#include "UserCode/TupleObjects/interface/TupleTau.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "UserCode/TupleObjects/interface/TupleUserSpecifiedData.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "TMath.h"
#include "DataFormats/VertexReco/interface/Vertex.h"


#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "DataFormats/RecoCandidate/interface/IsoDepositVetos.h"
#include "DataFormats/PatCandidates/interface/Isolation.h"
#include "EgammaAnalysis/ElectronTools/interface/ElectronEffectiveArea.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Lepton.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/Math/interface/deltaR.h"


typedef math::XYZTLorentzVector LorentzVector;
using namespace reco::isodeposit;

namespace TupleHelpers
{

  void setMuon_dz_dxy_isTight_isPF_isTracker(
                                double & dz, double & dxy,
                                bool & isTight, bool & isPF, bool & isTracker,
                                const reco::Vertex first_vertex,
                                edm::Handle<reco::PFCandidateCollection > pfCandidates,
                                pat::Muon * muon)
  {

    dz = 999.9;
    dxy = 999.9;

    if(!muon->innerTrack().isNull())
    {
      dz = muon->innerTrack()->dz(first_vertex.position());
      dxy = muon->innerTrack()->dxy(first_vertex.position());
    }

    //////////////////////////////
    isTight = 1;
    if(   !(muon->isGlobalMuon())                 ) isTight = 0;
    if(   !(muon->numberOfMatchedStations()>1)    ) isTight = 0;
    if(    muon->innerTrack().isNonnull() && muon->track().isNonnull() && muon->globalTrack().isNonnull() )
    {

      if(   !(muon->globalTrack()->normalizedChi2()<10) ) isTight = 0;
      if(   !((muon->globalTrack()->hitPattern()).numberOfValidMuonHits()>0) ) isTight = 0;
      if(   !((muon->innerTrack()->hitPattern()).numberOfValidPixelHits()>0) ) isTight = 0;
      if(   !((muon->track()->hitPattern()).trackerLayersWithMeasurement()>5) ) isTight = 0;

    } else isTight = 0;
    /////////////////////////////////

    bool isPF = 0;

      for(size_t pf = 0; pf < pfCandidates->size(); pf++)
      {
        if( (*pfCandidates)[pf].particleId() == reco::PFCandidate::mu )
        {
          reco::MuonRef muonRefToPFMuon = (*pfCandidates)[pf].muonRef();

          if( muonRefToPFMuon.isNonnull() )
          {
            if(deltaR( muonRefToPFMuon->p4() , muon->p4()) < 1e-04)
            {
              if(muonRefToPFMuon->isGlobalMuon() || muonRefToPFMuon->isTrackerMuon() ) isPF = 1;
              if (muonRefToPFMuon->isTrackerMuon()) isTracker = 1;
            }
          }
        }
      }


//////////////////
  }


  /////////////////
  // electron veto mva MVALoose


  bool passesMVALoose(double PT, double superClusterEta, double mvaPOGNonTrig)
  {
    bool MVALoose = 0;
    double ETA = fabs(superClusterEta);
    double MVA = mvaPOGNonTrig;

    if(PT<=20 && ETA>=0.0 && ETA<=0.8 && MVA>0.925) MVALoose = 1;
    else if(PT<=20 && ETA>=0.8 && ETA<1.479 && MVA>0.915) MVALoose = 1;
    else if(PT<=20 && ETA>=1.479 && ETA<2.5 && MVA>0.965) MVALoose = 1;
    else if(PT>20 && ETA>=0.0 && ETA<=0.8 && MVA>0.905) MVALoose = 1;
    else if(PT>20 && ETA>=0.8 && ETA<1.479 && MVA>0.955) MVALoose = 1;
    else if(PT>20 && ETA>=1.479 && ETA<2.5 && MVA>0.975) MVALoose = 1;

    return MVALoose;

  }


  bool passesMVALooseNEW(double PT, double superClusterEta, double mvaPOGTrigNoIP)
  {
    bool MVALooseNEW = 0;
    double ETA = fabs(superClusterEta);
    double MVA = mvaPOGTrigNoIP;

    if(PT<=20 && ETA>=0.0 && ETA<=0.8 && MVA>-0.5375) MVALooseNEW = 1;
    else if(PT<=20 && ETA>=0.8 && ETA<1.479 && MVA>-0.375) MVALooseNEW = 1;
    else if(PT<=20 && ETA>=1.479 && ETA<2.5 && MVA>-0.025) MVALooseNEW = 1;
    else if(PT>20 && ETA>=0.0 && ETA<=0.8 && MVA>0.325) MVALooseNEW = 1;
    else if(PT>20 && ETA>=0.8 && ETA<1.479 && MVA>0.775) MVALooseNEW = 1;
    else if(PT>20 && ETA>=1.479 && ETA<2.5 && MVA>0.775) MVALooseNEW = 1;

    return MVALooseNEW;

  }





  ///////////////////
  // helper function for
  // finding PV and storing related
  // info


  void findPrimaryVertexAndGetInfo(
  edm::Handle<edm::View<reco::Vertex> > vertices,
  int & numberOfGoodVertices, int & PVndof, double & PVz, double & PVpositionRho, LorentzVector & PVp4)
  {

    int primary_vertex_indx = -999;
    double max_sumPt = -999.0;
    int numberOfGoodVertices_ = 0;

    edm::View<reco::Vertex>::const_iterator vertex;
    for(vertex=vertices->begin(); vertex!=vertices->end(); ++vertex)
    {
      if(vertex->isValid() && !vertex->isFake() && vertex->ndof() > 4.0)
      {
        if(fabs(vertex->z()) < 24.0 && vertex->position().Rho() < 2)
        {

          numberOfGoodVertices_++;

          if( vertex->p4().pt() > max_sumPt)
          {
            max_sumPt  =     vertex->p4().pt();
            primary_vertex_indx =    vertex - vertices->begin();
          }
        }
      }
    }

    if(primary_vertex_indx!=-999)
    {
      const reco::Vertex & primary_vertex = vertices->at(primary_vertex_indx);
      numberOfGoodVertices = numberOfGoodVertices_;
      PVndof = primary_vertex.ndof();
      PVz = primary_vertex.z();
      PVpositionRho = primary_vertex.position().Rho();
      PVp4 = primary_vertex.p4();
    }

    return;


  }


  //////////////////////
  // stitching weights
  // DY + jets


  double getWeightHEPNUP_DYJets(int hepNUP)
  {

    int nJets = hepNUP-5;

    if(nJets==0)      return 0.115028141;
    else if(nJets==1) return 0.022330692;
    else if(nJets==2) return 0.009068275;
    else if(nJets==3) return 0.005270592;
    else if(nJets>=4) return 0.004113813;
    else return 1. ;

  }

  double getWeightHEPNUP_WJets(int hepNUP)
  {

    int nJets = hepNUP-5;

    if(nJets==0)      return 0.492871535;
    else if(nJets==1) return 0.100267473;
    else if(nJets==2) return 0.031238278;
    else if(nJets==3) return 0.019961315;
    else if(nJets>=4) return 0.018980202;
    else return 1. ;

  }



  //////////////////////
  // ttBAR sample pt reweight


  double compTopPtWeight(double topPt)
  {
    const double a = 0.156;
    const double b = -0.00137;
    return TMath::Exp(a + b*topPt);
  }

  double getTTbarPtWeight(double ptTOP, double ptTOPBAR)
  {
    double weight = 1.0;

    ////////////
    // check for valid pt

    if(ptTOP==ptTOP && ptTOPBAR==ptTOPBAR)
    {
      weight = compTopPtWeight(ptTOP)*compTopPtWeight(ptTOPBAR);
      return ( weight > 0. ) ? TMath::Sqrt(weight) : 0.;
    }

    else return 1.0;

  }

  ///////////////////////
  // QCD Shape Temp. Correction
  // Weights
  // will be filled for all samples

  void getQCDShapeTemplateCorrections(double & etaDepQCDShapeTemplateCorrection,
  double & inclusiveQCDShapeTemplateCorrection, const TupleTau tau)
  {

    double ABSETA = fabs(tau.corrected_p4().eta());
    double PT = tau.corrected_p4().pt();


    TF1* QCDWeight_mutau_inclusive = new TF1("QCDWeight_mutau_inclusive","1.25E+00+(-6.31E-03)*x",30.,2000.);
    QCDWeight_mutau_inclusive->SetNpx(25600);
    //QCDWeight_mutau_inclusive->Write();
    inclusiveQCDShapeTemplateCorrection = QCDWeight_mutau_inclusive->Eval(PT);
    if(inclusiveQCDShapeTemplateCorrection<0.0) inclusiveQCDShapeTemplateCorrection = 0.0;

    delete QCDWeight_mutau_inclusive;




    if(ABSETA <= 1.2)
    {
      TF1* QCDWeight_mutau_central = new TF1("QCDWeight_mutau_central","1.22E+00+(-5.71E-03)*x",30.,2000.);
      QCDWeight_mutau_central->SetNpx(25600);
      //QCDWeight_mutau_central->Write();

      etaDepQCDShapeTemplateCorrection = QCDWeight_mutau_central->Eval(PT);
      if(etaDepQCDShapeTemplateCorrection<0.0) etaDepQCDShapeTemplateCorrection = 0.0;

      delete QCDWeight_mutau_central;
    }

    else if(ABSETA>1.2 && ABSETA<=1.7)
    {
      TF1* QCDWeight_mutau_medium = new TF1("QCDWeight_mutau_medium","1.52E+00+(-1.34E-02)*x",30.,2000.);
      QCDWeight_mutau_medium->SetNpx(25600);
      //QCDWeight_mutau_medium->Write();

      etaDepQCDShapeTemplateCorrection = QCDWeight_mutau_medium->Eval(PT);
      if(etaDepQCDShapeTemplateCorrection<0.0) etaDepQCDShapeTemplateCorrection = 0.0;


      delete QCDWeight_mutau_medium;
    }

    else if(ABSETA>1.7)
    {
      TF1* QCDWeight_mutau_forward = new TF1("QCDWeight_mutau_forward","1.43E+00+(-1.09E-02)*x",30.,2000.);
      QCDWeight_mutau_forward->SetNpx(25600);
      //QCDWeight_mutau_forward->Write();

      etaDepQCDShapeTemplateCorrection = QCDWeight_mutau_forward->Eval(PT);
      if(etaDepQCDShapeTemplateCorrection<0.0) etaDepQCDShapeTemplateCorrection = 0.0;



      delete QCDWeight_mutau_forward;
    }


    return;
  }




  /////////////////////
  // higgs pt reweight for SUSY
  // signal samples

  // called to set bin within bounds for weight access
  void BoundaryCheckBin(int & bin, int numBins  )
  {
    if ( bin < 1 ) bin = 1;
    if ( bin > numBins ) bin = numBins;
    return;
  }


  void getHiggsPtWeights(const TupleUserSpecifiedData userData0, LorentzVector BosonP4,
  double & nominalHIGLUXHQTmhmax,
  double & upHIGLUXHQTmhmax,
  double & downHIGLUXHQTmhmax,
  double & nominalPOWHEGmhmod,
  double & upPOWHEGmhmod,
  double & downPOWHEGmhmod)
  {

    ///////////
    // check if a valid SUSY sample
    // and if valid boson 4-vector

    bool SUSY = 0;
    bool VALIDVEC = 0;
    double MASS = userData0.MASS();

    if(userData0.SampleName().find("SUSY") != std::string::npos) SUSY = 1;
    if(userData0.SampleName().find("susy") != std::string::npos) SUSY = 1;
    if(userData0.SampleName().find("Susy") != std::string::npos) SUSY = 1;

    if(BosonP4.px() == BosonP4.px() && BosonP4.pt()>0.0) VALIDVEC = 1;

    //////////
    // return with 1.0 if invalid

    if(!SUSY || !VALIDVEC)
    {
      nominalHIGLUXHQTmhmax = 1.0;
      upHIGLUXHQTmhmax  = 1.0;
      downHIGLUXHQTmhmax  = 1.0;
      nominalPOWHEGmhmod  = 1.0;
      upPOWHEGmhmod  = 1.0;
      downPOWHEGmhmod  = 1.0;
      return;

    }

    ////////////////
    // set weights otherwise

    else
    {

      std::string file1Name = "RunTimeDataInput/data/HiggsPtReweightFiles/mssmHiggsPtReweightGluGlu_mhmax.root";
      std::string file2Name = "RunTimeDataInput/data/HiggsPtReweightFiles/mssmHiggsPtReweightGluGlu_mhmod_POWHEG.root";
      edm::FileInPath fileInPath1 = edm::FileInPath(file1Name);
      edm::FileInPath fileInPath2 = edm::FileInPath(file2Name);

      TFile* file1 = new TFile(fileInPath1.fullPath().c_str());
      TFile* file2 = new TFile(fileInPath2.fullPath().c_str());

      /////////////
      // load in the histograms (3 per file)
      // and get the weights

      int bin = 0;
      double PT = BosonP4.pt();
      char histName[100];

      ////////
      // nominal

      sprintf(histName,"A_mA%1.0f_mu200/mssmHiggsPtReweight_A_mA%1.0f_mu200_central", MASS, MASS);

      TH1 * file1HistNom = dynamic_cast<TH1*>(file1->Get(histName));
      bin = file1HistNom->FindBin(PT);
      BoundaryCheckBin(bin, file1HistNom->GetNbinsX());
      nominalHIGLUXHQTmhmax = file1HistNom->GetBinContent(bin);

      TH1 * file2HistNom = dynamic_cast<TH1*>(file2->Get(histName));
      bin = file2HistNom->FindBin(PT);
      BoundaryCheckBin(bin, file2HistNom->GetNbinsX());
      nominalPOWHEGmhmod = file2HistNom->GetBinContent(bin);

      ////////
      // high

      sprintf(histName,"A_mA%1.0f_mu200/mssmHiggsPtReweight_A_mA%1.0f_mu200_tanBetaHigh", MASS, MASS);

      TH1 * file1HistUp = dynamic_cast<TH1*>(file1->Get(histName));
      bin = file1HistUp->FindBin(PT);
      BoundaryCheckBin(bin, file1HistUp->GetNbinsX());
      upHIGLUXHQTmhmax = file1HistUp->GetBinContent(bin);

      TH1 * file2HistUp = dynamic_cast<TH1*>(file2->Get(histName));
      bin = file2HistUp->FindBin(PT);
      BoundaryCheckBin(bin, file2HistUp->GetNbinsX());
      upPOWHEGmhmod = file2HistUp->GetBinContent(bin);

      ////////
      // low

      sprintf(histName,"A_mA%1.0f_mu200/mssmHiggsPtReweight_A_mA%1.0f_mu200_tanBetaLow", MASS, MASS);

      TH1 * file1HistDown = dynamic_cast<TH1*>(file1->Get(histName));
      bin = file1HistDown->FindBin(PT);
      BoundaryCheckBin(bin, file1HistDown->GetNbinsX());
      downHIGLUXHQTmhmax = file1HistDown->GetBinContent(bin);

      TH1 * file2HistDown = dynamic_cast<TH1*>(file2->Get(histName));
      bin = file2HistDown->FindBin(PT);
      BoundaryCheckBin(bin, file2HistDown->GetNbinsX());
      downPOWHEGmhmod = file2HistDown->GetBinContent(bin);

      delete file1;
      delete file2;
      delete file1HistNom;
      delete file1HistUp;
      delete file1HistDown;
      delete file2HistNom;
      delete file2HistUp;
      delete file2HistDown;


    }


    return;

  }


  //////////////////////
  // Z->ee e->tau_h scale
  // factors for eTau channels
  // will store for all samples

  double getZeeScaleFactor(const TupleTau tau)
  {

    double correction = 1.0;
    double ABSETA = fabs(tau.corrected_p4().eta());
    int strips  = tau.numStrips();
    int hadrons = tau.numHadrons();

    ////////////////
    // barrel
    if(ABSETA<1.5)
    {

      if(hadrons==1 && strips>0)          correction = 1.84;
      else if(hadrons==1 && strips==0)    correction = 1.37;
      else if(hadrons==3)                 correction = 1.0;


    }

    ///////////////
    // endcap
    if(ABSETA>=1.5)
    {

      if(hadrons==1 && strips>0)          correction = 0.83;
      else if(hadrons==1 && strips==0)    correction = 0.72;
      else if(hadrons==3)                 correction = 1.0;


    }

    return correction;


  }

  //////////////////////
  // decay mode correction
  // for Z->tau tau and
  // signal samples (will store for all if needed)

  double getDecayModeCorrectionFactor(const TupleTau tau)
  {

    double correction = 1.0;
    double ABSETA = fabs(tau.corrected_p4().eta());
    int strips  = tau.numStrips();
    int hadrons = tau.numHadrons();

    ////////////////
    // barrel
    if(ABSETA<1.5)
    {

      if(hadrons==1 && strips>0)          correction = 1.06;
      else if(hadrons==1 && strips==0)    correction = 0.87;
      else if(hadrons==3)                 correction = 1.02;


    }

    ///////////////
    // endcap
    if(ABSETA>=1.5)
    {

      if(hadrons==1 && strips>0)          correction = 1.0;
      else if(hadrons==1 && strips==0)    correction = 0.96;
      else if(hadrons==3)                 correction = 1.06;


    }

    return correction;

  }

  /////////////////
  // Jet-to-Tau Fake correction
  // intended for W+jets, but will
  // be computed for all samples just in case

  double getTauFakeCorrection(double pt)
  {
    //new corrections (Mar14, new T-ES correction)
    double correction = 0;
    double p0 =  0.787452;
    double p1 = -0.146412;
    double p2 = -0.0276803;
    double p3 = -0.0824184;
    double X = (pt-149.832)/100;//(x-meanPt)/100
    correction = p0+p1*X+p2*X*X+p3*X*X*X;

    return correction;
  }


  //////////////////
  // muon ID scale factor

  void muonIDSF(bool isRealData, const TupleMuon muon,
  const TupleUserSpecifiedData userData0, double & muonDataIDweight,
  double & muonMcIDweight)
  {



    //////////////
    // compute sf if MC, data, or embedded samples


    double ABSETA = fabs(muon.p4().eta());
    double PT = muon.p4().pt();

    int nEta = 0;
    int nPt = 0;

    if(PT<30) nPt = 0;
    else nPt = 1;

    if(ABSETA<0.8) nEta = 0;
    else if(0.8<=ABSETA && ABSETA<1.2) nEta = 1;
    else if(1.2<=ABSETA && ABSETA<2.1) nEta = 2;


    /////////////////////
    // weights matrix with [nRun][nEta][nPt]

    double muonID[2][3][2]
    = { { { 0.947122 , 0.94881} , { 0.942154 , 0.943422} , { 0.938653 , 0.938045} } , // ABCD
    { { 0.964696 , 0.963092} , { 0.958555 , 0.957613} , { 0.951103 , 0.949022} } }; // MC ABCD




    muonDataIDweight = muonID[0][nEta][nPt];
    muonMcIDweight = muonID[1][nEta][nPt];
    return;
  }


  //////////////////
  // muon ISOL scale factor

  void muonISOLSF(bool isRealData, const TupleMuon muon,
  const TupleUserSpecifiedData userData0, double & muonDataISOLweight,
  double & muonMcISOLweight)
  {



    //////////////
    // compute sf if MC, data, or embedded samples


    double ABSETA = fabs(muon.p4().eta());
    double PT = muon.p4().pt();

    int nEta = 0;
    int nPt = 0;

    if(PT<30) nPt = 0;
    else nPt = 1;

    if(ABSETA<0.8) nEta = 0;
    else if(0.8<=ABSETA && ABSETA<1.2) nEta = 1;
    else if(1.2<=ABSETA && ABSETA<2.1) nEta = 2;


    /////////////////////
    // weights matrix with [nRun][nEta][nPt]

    double muonISOL[2][3][2]
    =  { { { 0.74406 , 0.902759} , { 0.806595 , 0.923013} , { 0.844972 , 0.937799} } , // ABCD
    { { 0.783752 , 0.913384} , { 0.820126 , 0.928884} , { 0.851507 , 0.938155} } }; // MC ABCD



    muonDataISOLweight = muonISOL[0][nEta][nPt];
    muonMcISOLweight = muonISOL[1][nEta][nPt];
    return;
  }

  //////////////////
  // electron ID scale factor

  void electronIDSF(bool isRealData, const TupleElectron electron,
  const TupleUserSpecifiedData userData0, double & electronDataIDweight,
  double & electronMcIDweight )
  {



    //////////////
    // compute sf if MC, data, or embedded samples


    double ABSETA = fabs(electron.p4().eta());
    double PT = electron.p4().pt();

    int nEta = 0;
    int nPt = 0;

    if(PT<30) nPt = 0;
    else nPt = 1;

    if(ABSETA<1.479) nEta = 0;
    else nEta = 1;


    /////////////////////
    // weights matrix with [nRun][nEta][nPt]

    double electronID[2][2][2]
    = { { { 0.737978 , 0.849993} , { 0.331858 , 0.534207} } ,  // ABCD
    { { 0.82005 , 0.896069} , { 0.41771 , 0.602545} } };  // MC ABCD


    electronDataIDweight = electronID[0][nEta][nPt];
    electronMcIDweight = electronID[1][nEta][nPt];
    return;
  }


  //////////////////
  // electron ISOL scale factor

  void electronISOLSF(bool isRealData, const TupleElectron electron,
  const TupleUserSpecifiedData userData0, double & electronDataISOLweight,
  double & electronMcISOLweight )
  {



    //////////////
    // compute sf if MC, data,  or embedded samples


    double ABSETA = fabs(electron.p4().eta());
    double PT = electron.p4().pt();

    int nEta = 0;
    int nPt = 0;

    if(PT<30) nPt = 0;
    else nPt = 1;

    if(ABSETA<1.479) nEta = 0;
    else nEta = 1;


    /////////////////////
    // weights matrix with [nRun][nEta][nPt]

    double electronISOL[2][2][2]
    =  { { { 0.732434 , 0.888954} , { 0.807757 , 0.915259} } , // ABCD
    { { 0.777811 , 0.906771} , { 0.852909 , 0.924465} } }; // MC ABCD

    electronDataISOLweight = electronISOL[0][nEta][nPt];
    electronMcISOLweight = electronISOL[1][nEta][nPt];
    return;
  }





  ///////////////////////
  // Integrated Crystal Ball Function

  double IntegratedCrystalBallEfficiency(double m, double m0, double sigma,
  double alpha, double n, double norm)
  {
    const double sqrtPiOver2 = 1.2533141373;
    const double sqrt2 = 1.4142135624;

    double sig = fabs((double) sigma);

    double t = (m - m0)/sig;

    if (alpha < 0) t = -t;

    double absAlpha = fabs(alpha / sig);
    double a = TMath::Power(n/absAlpha,n)*exp(-0.5*absAlpha*absAlpha);
    double b = absAlpha - n/absAlpha;

    if (a>=std::numeric_limits<double>::max()) return -1. ;

    double ApproxErf ;
    double arg = absAlpha / sqrt2 ;
    if (arg > 5.) ApproxErf = 1 ;
    else if (arg < -5.) ApproxErf = -1 ;
    else ApproxErf = erf(arg) ;

    double leftArea = (1 + ApproxErf) * sqrtPiOver2 ;
    double rightArea = ( a * 1/TMath::Power(absAlpha - b,n-1)) / (n - 1);
    double area = leftArea + rightArea;

    if ( t <= absAlpha )
    {
      arg = t / sqrt2 ;
      if (arg > 5.) ApproxErf = 1 ;
      else if (arg < -5.) ApproxErf = -1 ;
      else ApproxErf = erf(arg) ;
      return norm * (1 + ApproxErf) * sqrtPiOver2 / area ;
    }
    else
    {
      return norm*(leftArea+a*(1/TMath::Power(t-b,n-1)-1/TMath::Power(absAlpha - b,n-1)) / (1 - n))/area;
    }

  }

  ///////////////////////
  // for non-tt embedded samples, the normal trigger paths
  // and matching is not done
  // instead we check that the gen level lepton mass is > 50
  // and check the DoubleMu trigger wasAccept()

  bool passNonTopEmbeddedTriggerAndMass50(const TupleUserSpecifiedData userData0,
  const reco::GenParticleCollection & genparticles, const pat::TriggerPathCollection* paths)
  {
    bool pass = 1;

    /////////////
    // check if it is not
    // a non-tt embedded sample
    // return 1 for anything other than
    // nonTop embedded


    if(userData0.isNonTopEmbeddedSample()!=1)
    {
      pass = 1;
      return pass;
    }


    if(userData0.isNonTopEmbeddedSample()==1)
    {

      bool triggerOK = 0;

      std::vector<std::string> doubleMuPaths;
      doubleMuPaths.clear();
      doubleMuPaths.push_back("HLT_Mu17_Mu8_v16");
      doubleMuPaths.push_back("HLT_Mu17_Mu8_v17");
      doubleMuPaths.push_back("HLT_Mu17_Mu8_v18");
      doubleMuPaths.push_back("HLT_Mu17_Mu8_v19");
      doubleMuPaths.push_back("HLT_Mu17_Mu8_v20");
      doubleMuPaths.push_back("HLT_Mu17_Mu8_v21");
      doubleMuPaths.push_back("HLT_Mu17_Mu8_v22");

      for(size_t i = 0; i<doubleMuPaths.size(); ++i)
      {
        for (size_t ii = 0; ii < paths->size(); ++ii)
        {

          const pat::TriggerPath& path = paths->at(ii);
          if(path.name().find(doubleMuPaths[i])!= std::string::npos)
          {

            if(path.wasAccept() && path.wasRun())
            {
              std::cout<<" path "<<doubleMuPaths[i]<<" found and wasAccept = "<<path.wasAccept();
              std::cout<<" in form "<<path.name()<<"\n";
              triggerOK = 1;
            }
          }
        }
      }

      // now check if the gen level dilepton
      // mass is > 50

      bool passesGenLevelMassCut = 0;
      LorentzVector LegPlus, LegMinus;

      for(std::size_t mc = 0; mc < genparticles.size(); ++mc)
      {

        if(genparticles[mc].status()==2)
        {

          if(genparticles[mc].pdgId()==-15) LegMinus = genparticles[mc].p4();
          if(genparticles[mc].pdgId()==15) LegPlus = genparticles[mc].p4();


        }


      }
      if( (LegMinus+LegPlus).M() > 50.0) passesGenLevelMassCut = 1;


      if(triggerOK && passesGenLevelMassCut) pass = 1;
      else pass = 0;


    }



    return pass;
  }


  ///////////////////////
  // for SUSY signal samples,
  // must reject events outside of
  // 70% to 130% of the nominal
  // generator mass


  bool passSignalGeneratorMass70to130Cut(const TupleUserSpecifiedData userData0,
  const reco::GenParticleCollection & genparticles)
  {
    bool pass = 1;
    bool SUSY = 0;




    if(userData0.SampleName().find("SUSY") != std::string::npos) SUSY = 1;
    if(userData0.SampleName().find("susy") != std::string::npos) SUSY = 1;
    if(userData0.SampleName().find("Susy") != std::string::npos) SUSY = 1;

    if(!SUSY)
    {
      pass = 1;
      return pass;
    }

    else
    {
      double low = 0.7 * userData0.MASS();
      double high = 1.30 * userData0.MASS();


      for(std::size_t mc = 0; mc < genparticles.size(); ++mc)
      {

        if(genparticles[mc].status()==3)
        {

          if( abs(genparticles[mc].pdgId())  == 25 || abs(genparticles[mc].pdgId())  == 36 ||
          abs(genparticles[mc].pdgId())  == 35 || abs(genparticles[mc].pdgId())  == 37)
          {


            if(genparticles[mc].p4().M()<low || genparticles[mc].p4().M()>high)
            {
              pass  = 0;
              return pass;
            }

            else if(genparticles[mc].p4().M()>=low && genparticles[mc].p4().M()<=high)
            {
              pass  = 1;
              return pass;
            }


          }

        }

      }
    }

    return pass;
  }

  /////////////////////////////////////////
  // compute hadronic tau trigger weights
  //

  /////////////////////////////////
  // fill the trigger weights
  // for hadronic taus in eTau

  void getTriggerWeightsHadTauETAU(bool isRealData,
  double & HadronicTauDataTrigEffAntiEMed, double & HadronicTauMcTrigEffAntiEMed,
  double & HadronicTauDataTrigEffAntiETight, double & HadronicTauMcTrigEffAntiETight,
  const TupleTau tau, const TupleUserSpecifiedData userData0)
  {

    double medMCpar[5] = {NAN,NAN,NAN,NAN,NAN};
    double medDATApar[5] = {NAN,NAN,NAN,NAN,NAN};
    double tightMCpar[5] = {NAN,NAN,NAN,NAN,NAN};
    double tightDATApar[5] = {NAN,NAN,NAN,NAN,NAN};

    double ABSETA = fabs(tau.corrected_p4().eta());






    if(ABSETA<1.5)
    {
      medDATApar[0] = 1.83211e+01;     medMCpar[0] = 1.83709e+01;
      medDATApar[1] = -1.89051e+00;    medMCpar[1] = 1.37806e-01;
      medDATApar[2] = 3.71081e+00;     medMCpar[2] = 1.64478e-01;
      medDATApar[3] = 1.06628e+00;     medMCpar[3] = 1.44798e+00;
      medDATApar[4] = 1.28559e+00;     medMCpar[4] = 9.92673e-01;

      tightDATApar[0] = 18.895025;     tightMCpar[0] = 18.520018;
      tightDATApar[1] = 1.695306;      tightMCpar[1] = 0.294271;
      tightDATApar[2] = 1.922852;      tightMCpar[2] = 0.127877;
      tightDATApar[3] = 34.020744;     tightMCpar[3] = 5.275917;
      tightDATApar[4] = 0.903446;      tightMCpar[4] = 0.918806;


    }
    else if(ABSETA>1.5)
    {

      medDATApar[0] = 1.80812e+01;     medMCpar[0] = 1.83074e+01;
      medDATApar[1] = 1.39482e+00;     medMCpar[1] = 1.43406e+00;
      medDATApar[2] = 1.14305e+00;     medMCpar[2] = 1.40743e+00;
      medDATApar[3] = 1.08989e+01;     medMCpar[3] = 1.41501e+02;
      medDATApar[4] = 8.97087e-01;     medMCpar[4] = 9.19457e-01;

      tightDATApar[0] = 18.711233;     tightMCpar[0] = 18.657221;
      tightDATApar[1] = 0.255624;      tightMCpar[1] = 0.770777;
      tightDATApar[2] = 0.131574;      tightMCpar[2] = 0.648889;
      tightDATApar[3] = 3.648101;      tightMCpar[3] = 138.380600;
      tightDATApar[4] = 0.857139;      tightMCpar[4] = 0.870723;

    }





    HadronicTauDataTrigEffAntiEMed = IntegratedCrystalBallEfficiency(tau.corrected_p4().pt(),
    medDATApar[0], medDATApar[1], medDATApar[2], medDATApar[3], medDATApar[4]);

    HadronicTauMcTrigEffAntiEMed = IntegratedCrystalBallEfficiency(tau.corrected_p4().pt(),
    medMCpar[0], medMCpar[1], medMCpar[2], medMCpar[3], medMCpar[4]);

    HadronicTauDataTrigEffAntiETight = IntegratedCrystalBallEfficiency(tau.corrected_p4().pt(),
    tightDATApar[0], tightDATApar[1], tightDATApar[2], tightDATApar[3], tightDATApar[4]);

    HadronicTauMcTrigEffAntiETight = IntegratedCrystalBallEfficiency(tau.corrected_p4().pt(),
    tightMCpar[0], tightMCpar[1], tightMCpar[2], tightMCpar[3], tightMCpar[4]);




    /////////
    // even if embedded or data, keep both values
    // although final weight for embedded is just  EffDataELE20andELE22
    // and not the ratio

    return;







  }


  /////////////
  // fill the trigger weights for hadronic taus
  // for muTau



  void getTriggerWeightsHadTauMUTAU(bool isRealData,
  double & HadronicTauDataTrigEffAntiMuMed, double & HadronicTauMcTrigEffAntiMuMed,
  const TupleTau tau, const TupleUserSpecifiedData userData0)
  {



    double medMCpar[5] = {NAN,NAN,NAN,NAN,NAN};
    double medDATApar[5] = {NAN,NAN,NAN,NAN,NAN};
    double ABSETA = fabs(tau.corrected_p4().eta());

    if(ABSETA<1.5)
    {
      medDATApar[0] = 1.83211e+01;     medMCpar[0] = 1.83709e+01;
      medDATApar[1] = -1.89051e+00;    medMCpar[1] = 1.37806e-01;
      medDATApar[2] = 3.71081e+00;     medMCpar[2] = 1.64478e-01;
      medDATApar[3] = 1.06628e+00;     medMCpar[3] = 1.44798e+00;
      medDATApar[4] = 1.28559e+00;     medMCpar[4] = 9.92673e-01;

    }
    else if(ABSETA>1.5)
    {

      medDATApar[0] = 1.80812e+01;     medMCpar[0] = 1.83074e+01;
      medDATApar[1] = 1.39482e+00;     medMCpar[1] = 1.43406e+00;
      medDATApar[2] = 1.14305e+00;     medMCpar[2] = 1.40743e+00;
      medDATApar[3] = 1.08989e+01;     medMCpar[3] = 1.41501e+02;
      medDATApar[4] = 8.97087e-01;     medMCpar[4] = 9.19457e-01;

    }





    HadronicTauDataTrigEffAntiMuMed = IntegratedCrystalBallEfficiency(tau.corrected_p4().pt(),
    medDATApar[0], medDATApar[1], medDATApar[2], medDATApar[3], medDATApar[4]);

    HadronicTauMcTrigEffAntiMuMed = IntegratedCrystalBallEfficiency(tau.corrected_p4().pt(),
    medMCpar[0], medMCpar[1], medMCpar[2], medMCpar[3], medMCpar[4]);


    /////////
    // even if embedded, keep both values
    // although final weight for embedded is just  EffDataELE20andELE22
    // and not the ratio

    return;






  }



  ////////////////////////////////////////////////////////////////
  // IMPORTANT NOTE: should be applied to events
  // with pT(tau) > 140 GeV (barrel) and pT(tau)>60 GeV in end caps.
  // Should not be applied otherwise.
  // For barrel (end caps), weight for tau with pT > 800 (400)
  // is weight for pT = 800 (400) GeV.



  void getHighPtHadronicTauTriggerWeights(const TupleTau tau, double & EffDataHighPtTauTrigger,
  double & EffMcHighPtTauTrigger)
  {

    double ABSETA = fabs(tau.corrected_p4().eta());
    double PT = tau.corrected_p4().pt();

    ///////////////////////
    // if PT < 140 in the barrel
    // or if  PT < 60 in the endcaps
    // the weights should be set to
    // 1.0

    if((ABSETA<1.5 && PT<140) || (ABSETA>=1.5 && PT<60))
    {
      EffDataHighPtTauTrigger = 1.0;
      EffMcHighPtTauTrigger = 1.0;
      return;
    }

    ////////////////////////
    // compute weights for high
    // pt barrel muon, max valid
    // PT is 800

    if((ABSETA<1.5 && PT>=140))
    {
      double PTx = PT;
      if(PT>800) PTx = 800;

      TF1 *TWBarrel = new TF1("AddTWBarrel","1-9.01280e-04*(x-140) + 4.81592e-07*(x-140)*(x-140)",0.,800.);

      EffDataHighPtTauTrigger  = 0.3+0.7*TWBarrel->Eval(PTx);
      EffMcHighPtTauTrigger    = TWBarrel->Eval(PTx);

      delete TWBarrel;
      return;

    }

    ////////////////////////
    // compute weights for high
    // pt endcap muon, max valid
    // PT is 400

    if((ABSETA>=1.5 && PT>=60))
    {
      double PTx = PT;
      if(PT>400) PTx = 400;

      TF1 *TWEndcaps = new TF1("AddTWEndcaps","1-1.81148e-03*(x-60) + 5.44335e-07*(x-60)*(x-60)",0.,800.);

      EffDataHighPtTauTrigger  = 0.3+0.7*TWEndcaps->Eval(PTx);
      EffMcHighPtTauTrigger    = TWEndcaps->Eval(PTx);

      delete TWEndcaps;
      return;

    }

    ///////////
    // default to 1.0

    EffDataHighPtTauTrigger = 1.0;
    EffMcHighPtTauTrigger = 1.0;
    return;




  }


  /////////////////////////////////
  // fill the trigger weights
  // for the HLT ISOMU and ISOMU17
  // Triggers
  // based on imp. by Garrett Funk
  // important to keep the ratio sep.
  // since for embedded samples
  // we only apply the Data Value as the weight
  // instead of the ratio as for MC

  void getTriggerWeightsISOMU17andISOMU18(bool isRealData,
  double & EffDataISOMU17andISOMU18, double & EffMcISOMU17andISOMU18,  const TupleMuon muon,
  const TupleUserSpecifiedData userData0)
  {





    double MCpar[5] = {NAN,NAN,NAN,NAN,NAN};
    double DATApar[5] = {NAN,NAN,NAN,NAN,NAN};
    double ETA = muon.p4().eta();

    if(ETA<-1.2)
    {
      DATApar[0] = 15.9977;     MCpar[0] = 16.0051;
      DATApar[1] = 7.64004e-05; MCpar[1] = 2.45144e-05;
      DATApar[2] = 6.4951e-08;  MCpar[2] = 4.3335e-09;
      DATApar[3] = 1.57403;     MCpar[3] = 1.66134;
      DATApar[4] = 0.865325;    MCpar[4] = 0.87045;
    }
    else if(-1.2 <= ETA && ETA < -0.8 )
    {
      DATApar[0] = 17.3974;     MCpar[0] = 17.3135;
      DATApar[1] = 0.804001;    MCpar[1] = 0.747636;
      DATApar[2] = 1.47145;     MCpar[2] = 1.21803;
      DATApar[3] = 1.24295;     MCpar[3] = 1.40611;
      DATApar[4] = 0.928198;    MCpar[4] = 0.934983;
    }
    else if(-0.8 <= ETA && ETA < 0)
    {
      DATApar[0] = 16.4307;     MCpar[0] = 15.9556;
      DATApar[1] = 0.226312;    MCpar[1] = 0.0236127;
      DATApar[2] = 0.265553;    MCpar[2] = 0.00589832;
      DATApar[3] = 1.55756;     MCpar[3] = 1.75409;
      DATApar[4] = 0.974462;    MCpar[4] = 0.981338;
    }
    else if(0.0 <= ETA && ETA < 0.8)
    {

      DATApar[0] = 17.313;     MCpar[0] = 15.9289;
      DATApar[1] = 0.662731;   MCpar[1] = 0.0271317;
      DATApar[2] = 1.3412;     MCpar[2] = 0.00448573;
      DATApar[3] = 1.05778;    MCpar[3] = 1.92101;
      DATApar[4] = 1.26624;    MCpar[4] = 0.978625;

    }
    else if(0.8 <= ETA && ETA < 1.2)
    {

      DATApar[0] = 16.9966;     MCpar[0] = 16.5678;
      DATApar[1] = 0.550532;    MCpar[1] = 0.328333;
      DATApar[2] = 0.807863;    MCpar[2] = 0.354533;
      DATApar[3] = 1.55402;     MCpar[3] = 1.67085;
      DATApar[4] = 0.885134;    MCpar[4] = 0.916992;
    }
    else if(1.2 <= ETA)
    {
      DATApar[0] = 15.9962;    MCpar[0] = 15.997;
      DATApar[1] = 0.000106195;    MCpar[1] = 7.90069e-05;
      DATApar[2] = 4.95058e-08;    MCpar[2] = 4.40036e-08;
      DATApar[3] = 1.9991;    MCpar[3] = 1.66272;
      DATApar[4] = 0.851294;    MCpar[4] = 0.884502;
    }





    EffDataISOMU17andISOMU18 = IntegratedCrystalBallEfficiency(muon.p4().pt(),
    DATApar[0], DATApar[1], DATApar[2], DATApar[3], DATApar[4]);
    EffMcISOMU17andISOMU18 = IntegratedCrystalBallEfficiency(muon.p4().pt(),
    MCpar[0], MCpar[1], MCpar[2], MCpar[3], MCpar[4]);


    /////////
    // even if embedded or data, keep both values
    // although final weight for embedded is just  EffDataELE20andELE22
    // and not the ratio


    return;





  }


  /////////////////////////////////
  // fill the trigger weights
  // for the HLT ELE20 and ELE22
  // Triggers
  // based on imp. by Garrett Funk
  // important to keep the ratio sep.
  // since for embedded samples
  // we only apply the Data Value as the weight
  // instead of the ratio as for MC

  void getTriggerWeightsELE20andELE22(bool isRealData,
  double & EffDataELE20andELE22, double & EffMcELE20andELE22,  const TupleElectron electron,
  const TupleUserSpecifiedData userData0)
  {




    double cbELegDataM0 = NAN;
    double cbELegDataSigma = NAN;
    double cbELegDataAlpha = NAN;
    double cbELegDataN = NAN;
    double cbELegDataNorm = NAN;

    double cbELegMCM0 = NAN;
    double cbELegMCSigma = NAN;
    double cbELegMCAlpha = NAN;
    double cbELegMCN = NAN;
    double cbELegMCNorm = NAN;


    if ( fabs(electron.p4().eta()) < 1.479) // barrel
    {
      cbELegDataM0 = 22.9704;
      cbELegDataSigma = 1.0258;
      cbELegDataAlpha = 1.26889;
      cbELegDataN = 1.31024;
      cbELegDataNorm = 1.06409;

      cbELegMCM0 = 21.7243;
      cbELegMCSigma = 0.619015;
      cbELegMCAlpha = 0.739301;
      cbELegMCN = 1.34903;
      cbELegMCNorm = 1.02594;
    }
    else // endcap
    {
      cbELegDataM0 = 21.9816;
      cbELegDataSigma = 1.40993;
      cbELegDataAlpha = 0.978597;
      cbELegDataN = 2.33144;
      cbELegDataNorm = 0.937552;

      cbELegMCM0 = 22.1217;
      cbELegMCSigma = 1.34054;
      cbELegMCAlpha = 1.8885;
      cbELegMCN = 1.01855;
      cbELegMCNorm = 4.7241;
    }

    EffDataELE20andELE22 = IntegratedCrystalBallEfficiency(electron.p4().pt(),
    cbELegDataM0, cbELegDataSigma, cbELegDataAlpha, cbELegDataN, cbELegDataNorm);
    EffMcELE20andELE22 = IntegratedCrystalBallEfficiency(electron.p4().pt(),
    cbELegMCM0, cbELegMCSigma, cbELegMCAlpha, cbELegMCN, cbELegMCNorm);

    /////////
    // even if embedded or data, keep both values
    // although final weight for embedded is just  EffDataELE20andELE22
    // and not the ratio


    return;

  }



  /////////////////////////////////
  // fill the event's pile-up
  // weight;  returns 1.0 if data

  void getPileUpWeight(edm::Handle<std::vector<PileupSummaryInfo> > PupInfo,
  bool isRealData, double & puWeight, double & puWeightM1, double & puWeightP1,
  float & NumPileupInt, float & NumTruePileUpInt,
  float & NumPileupIntM1, float & NumTruePileUpIntM1,
  float & NumPileupIntP1, float & NumTruePileUpIntP1  )
  {


    ///////////////
    // non-valid PU Collection


    if(!PupInfo.isValid())
    {

      puWeight = 1.0;
      puWeightM1 = 1.0;
      puWeightP1 = 1.0;
      NumPileupInt = 1.0;
      NumTruePileUpInt = 1.0;
      NumPileupIntM1 = 1.0;
      NumTruePileUpIntM1 = 1.0;
      NumPileupIntP1 = 1.0;
      NumTruePileUpIntP1 = 1.0;

      return;
    }


    /////////////////
    // for non-data, return a pileup weight

    edm::FileInPath mcFilePath = edm::FileInPath("RunTimeDataInput/data/PileUpReWeightFiles/MC_Summer12_PU_S10-600bins.root");
    edm::FileInPath dataFilePath = edm::FileInPath("RunTimeDataInput/data/PileUpReWeightFiles/Data_Pileup_2012_ReRecoPixel-600bins.root");



    edm::LumiReWeighting LumiWeights_(
    mcFilePath.fullPath().c_str(),
    dataFilePath.fullPath().c_str(),
    "pileup",
    "pileup");


    std::vector<PileupSummaryInfo>::const_iterator PVI;


    for(PVI = PupInfo->begin(); PVI != PupInfo->end(); ++PVI)
    {

      int BX = PVI->getBunchCrossing();



      if(BX==0)
      {
        NumTruePileUpInt = PVI->getTrueNumInteractions();
        NumPileupInt = PVI->getPU_NumInteractions();
      }
      else if(BX == -1)
      {
        NumTruePileUpIntM1 = PVI->getTrueNumInteractions();
        NumPileupIntM1 = PVI->getPU_NumInteractions();
      }
      else if(BX == 1)
      {
        NumTruePileUpIntP1 = PVI->getTrueNumInteractions();
        NumPileupIntP1 = PVI->getPU_NumInteractions();
      }
    }


    puWeight = LumiWeights_.weight( NumTruePileUpInt );
    puWeightM1 = LumiWeights_.weight( NumTruePileUpIntM1 );
    puWeightP1 = LumiWeights_.weight( NumTruePileUpIntP1 );

    return;

  }


  ////////////////////////////////
  // fill a vector with
  // indices of jets that
  // have DR > 0.1 overlap eliminated

  void getNonOverlappingJetIndices(edm::Handle<edm::View<pat::Jet> > jets,
  std::vector <unsigned int> & goodIndices, double DRcut)
  {

    /////////////////////
    // store the jets that do not overlap
    // with other jets, in case of overlap
    // remove the lower pt jet's index
    bool keep_jet_index = 1;
    goodIndices.clear();


    for (std::size_t i = 0; i < jets->size(); ++i)
    {

      const pat::Jet & patjet_i = jets->at(i);


      for (std::size_t ii = 0; ii < jets->size(); ++ii)
      {

        const pat::Jet & patjet_ii = jets->at(ii);
        if(patjet_i.pt() <= patjet_ii.pt() && deltaR(patjet_i.p4(),patjet_ii.p4())<DRcut && i!=ii)
        {

          keep_jet_index = 0;

        }




      }

      /////////
      // check if we should store
      // the jet's index

      if(keep_jet_index) goodIndices.push_back(i);

    }


    return;




  }



  ////////////////////////////////
  // set the pair-wise TriLepton Veto


  bool pairPassesTriLeptonVeto(unsigned int eIndex,
  unsigned int muIndex,
  edm::Handle< TupleElectronCollection > electrons,
  edm::Handle< TupleMuonCollection > muons)
  {


    /////////
    // loop over the electrons

    for (std::size_t i = 0; i < electrons->size(); ++i)
    {

      if(i!=eIndex)
      {

        const TupleElectron electron =   ((*electrons)[i]);
        if(electron.isTriLeptonVetoCandidate()) return 0;

      }

    }

    /////////
    // loop over the muons


    for (std::size_t i = 0; i < muons->size(); ++i)
    {
      if(i!=muIndex)
      {
        const TupleMuon muon =   ((*muons)[i]);
        if(muon.isTriLeptonVetoCandidate()) return 0;




      }
    }
    return 1;

  }



  ////////////////////////////////////////////////////

  ///////////////////
  // create a transverse mass
  // calculator given any
  // combination of the various
  // vector types floating around here

  template <class SomeVector, class AnotherVector>
  inline double GetTransverseMass(SomeVector V1, AnotherVector V2)
  {

    double pTxMET = sqrt(V1.x()*V1.x()+V1.y()*V1.y())*sqrt(V2.x()*V2.x()+V2.y()*V2.y());
    double CosDphi = cos(deltaPhi(V1.phi(), V2.phi()));
    double MtSq = (2 * pTxMET*(1-CosDphi));
    return sqrt(MtSq);

  }


  ///////////////
  // new working points
  // for tau anti-e mva


  bool passAntiEMVA(int iCat, float raw, int WP=1)
  {

    if(iCat<0) return false;
    if(iCat>15) return true;

    float cutsLoose[16] =
    {0.835,0.831,0.849,0.859,0.873,0.823,0.85,0.855,0.816,0.861,0.862,0.847,0.893,0.82,0.845,0.851};
    float cutsMedium[16] =
    {0.933,0.921,0.944,0.945,0.918,0.941,0.981,0.943,0.956,0.947,0.951,0.95,0.897,0.958,0.955,0.942};
    float cutsTight[16] =
    {0.96,0.968,0.971,0.972,0.969,0.959,0.981,0.965,0.975,0.972,0.974,0.971,0.897,0.971,0.961,0.97};
    float cutsVeryTight[16] =
    {0.978,0.98,0.982,0.985,0.977,0.974,0.989,0.977,0.986,0.983,0.984,0.983,0.971,0.987,0.977,0.981};

    float cut=0;
    if(WP==0) cut = cutsLoose[iCat];
    if(WP==1) cut = cutsMedium[iCat];
    if(WP==2) cut = cutsTight[iCat];
    if(WP==3) cut = cutsVeryTight[iCat];
    return (raw>cut);

  }


  ///////////////
  // get electron
  // category as defined
  // here https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingSummer2013#Electron_ID

  int getMVAElectronIdCategory(double pt, double superClusterEta, std::string LOOSE_TIGHT="TIGHT")
  {

    int category = -1;

    // LOOSE ID

    if(LOOSE_TIGHT.compare("LOOSE")==0)
    {

      if( !(pt>20) )
      {

        if(fabs(superClusterEta) <= 0.8) category = 1;
        else if(fabs(superClusterEta) > 0.8 && fabs(superClusterEta) <= 1.479) category = 2;
        else if(fabs(superClusterEta) > 1.479) category = 3;

      }
      else
      {

        if(fabs(superClusterEta) <= 0.8) category = 4;
        else if(fabs(superClusterEta) > 0.8 && fabs(superClusterEta) <= 1.479) category = 5;
        else if(fabs(superClusterEta) > 1.479) category = 6;


      }

    }

    // TIGHT ID

    if(LOOSE_TIGHT.compare("TIGHT")==0)
    {

      if( (pt>20) )
      {

        if(fabs(superClusterEta) <= 0.8) category = 4;
        else if(fabs(superClusterEta) > 0.8 && fabs(superClusterEta) <= 1.479) category = 5;
        else if(fabs(superClusterEta) > 1.479) category = 6;

      }

    }


    return category;
  }


  //////////////////
  // check if passes mvaNonTrigV0 'tight ID'
  // as defined
  // here https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingSummer2013#Electron_ID

  bool doesItPassTightMVANonTrigV0(int category, double mva)
  {

    if(category == 4 && mva > 0.925 ) return 1;
    if(category == 5 && mva > 0.975 ) return 1;
    if(category == 6 && mva > 0.985 ) return 1;

    //    std::cout<<" WARNING electron category = "<<category<<" -- it should be 4,5, or 6"<<std::endl;
    return 0;

  }



  ///////////////
  // WP95 cut based electron
  // ID (return true if passes)


  bool passWP95(double superClusterEta,double sigIetaIeta,double deltaEta, double deltaPhi, double HE, double dZ_vtx)
  {

    bool passesAllCuts = 1;

    /////////
    // barrel

    if( fabs(superClusterEta) <= 1.479 )
    {

      if(! (sigIetaIeta<0.01) ) passesAllCuts = 0;
      if(! (deltaEta<0.007) ) passesAllCuts = 0;
      if(! (deltaPhi<0.8) ) passesAllCuts = 0;
      if(! (HE<0.15) ) passesAllCuts = 0;
      if(! (dZ_vtx<0.2) ) passesAllCuts = 0;
      if(passesAllCuts) return 1;

    }

    ////////
    // endcap


    else if( fabs(superClusterEta) > 1.479  && fabs(superClusterEta) < 2.5 )
    {

      if(! (sigIetaIeta<0.03) ) passesAllCuts = 0;
      if(! (deltaEta<0.01) ) passesAllCuts = 0;
      if(! (deltaPhi<0.7) ) passesAllCuts = 0;
      if(! (HE<999) ) passesAllCuts = 0;
      if(! (dZ_vtx<0.2) ) passesAllCuts = 0;
      if(passesAllCuts) return 1;

    }


    return 0;

  }



  ////////////////////////////////////////////////////
}
