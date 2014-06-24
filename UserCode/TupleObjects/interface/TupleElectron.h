#ifndef UserCode_TupleObjects_TupleElectron_h
#define UserCode_TupleObjects_TupleElectron_h


// system include files
#include <memory>



// needed by ntuple Electrons producer
#include <vector>
#include <iostream>
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Math/interface/LorentzVector.h"

typedef math::XYZTLorentzVector LorentzVector;
using namespace std;
using namespace edm;

class TupleElectron
{



public:
  TupleElectron();
  virtual ~TupleElectron(){}

  // setters

  void set_p4(LorentzVector);
  void set_genP4(LorentzVector);
  void set_pfP4(LorentzVector);
  void set_charge(int);
  void set_PFpdgId(int);
  void set_GENpdgId(int);
  void set_numberOfMissingInnerHits(int);
  void set_passConversionVeto(bool);
  void set_dz(double);
  void set_SuperClusterEta(double);
  void set_mvaTrigV0(double);
  void set_mvaTrigNoIPV0(double);
  void set_mvaNonTrigV0(double);
  void set_pass_tight_mvaNonTrigV0(double); 
  void set_passFullId(bool);
  void set_isEB(bool);
  void set_isEE(bool);
  void set_isEBEEGap(bool);
  void set_isEBEtaGap(bool);
  void set_isEBPhiGap(bool);
  void set_isEEDeeGap(bool);
  void set_isEERingGap(bool);
  void set_isEB(bool);
  void set_sigmaEtaEta(double);
  void set_sigmaIetaIeta(double);
  void set_sigmaIphiIphic(double);


  // isolation variables
  void set_chargedHadronIso(double);
  void set_photonIso(double);
  void set_neutralHadronIso(double);
  void set_puChargedHadronIso(double);
  void set_relativeIso(double);



  // getters

  LorentzVector p4() const;
  LorentzVector genP4() const;
  LorentzVector pfP4() const;
  int charge() const;
  int PFpdgId() const;
  int GENpdgId() const;
  int numberOfMissingInnerHits() const;
  bool passConversionVeto() const;
  double dz() const;
  double SuperClusterEta() const;
  double mvaTrigV0() const;
  double mvaTrigNoIPV0() const;
  double mvaNonTrigV0() const;
  bool pass_tight_mvaNonTrigV0() const;
  bool passFullId() const;
  double chargedHadronIso() const;
  double photonIso() const;
  double neutralHadronIso() const;
  double puChargedHadronIso() const;
  double relativeIso() const;
  bool isEB() const;
  bool isEE() const;
  bool isEBEEGap() const;
  bool isEBEtaGap() const;
  bool isEBPhiGap() const;
  bool isEEDeeGap() const;
  bool isEERingGap() const;
  bool isEB() const;
  double sigmaEtaEta() const;
  double sigmaIetaIeta() const;
  double sigmaIphiIphi() const;

private:
  LorentzVector m_p4;
  LorentzVector m_genP4;
  LorentzVector m_pfP4;
  int m_charge;
  int m_PFpdgId;
  int m_GENpdgId;
  int m_numberOfMissingInnerHits;
  bool m_passConversionVeto;
  double m_dz;
  double m_SuperClusterEta;
  double m_mvaTrigV0;
  double m_mvaTrigNoIPV0;
  double m_mvaNonTrigV0;
  bool m_pass_tight_mvaNonTrigV0;
  bool m_passFullId;
  double m_chargedHadronIso;
  double m_photonIso;
  double m_neutralHadronIso;
  double m_puChargedHadronIso;
  double m_relativeIso;
  bool m_isEB;
  bool m_isEE;
  bool m_isEBEEGap;
  bool m_isEBEtaGap;
  bool m_isEBPhiGap;
  bool m_isEEDeeGap;
  bool m_isEERingGap;
  bool m_isEB;
  double m_sigmaEtaEta;
  double m_sigmaIetaIeta;
  double m_sigmaIphiIphi;




};

typedef std::vector<TupleElectron> TupleElectronCollection;

#endif
