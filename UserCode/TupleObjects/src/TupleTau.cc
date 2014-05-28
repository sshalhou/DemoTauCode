#include "UserCode/TupleObjects/interface/TupleTau.h"
#include "UserCode/TupleHelpers/interface/TupleHelpers.hh"


TupleTau::TupleTau()
{
  m_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_genP4.SetXYZT(NAN,NAN,NAN,NAN);
  m_corrected_p4.SetXYZT(NAN,NAN,NAN,NAN);
  m_pdgId = -999;
  m_charge = -999;
  m_decayMode = -999;
  m_passFullId = 0;
  float m_byIsolationMVAraw = NAN;
  float m_byLooseIsolationMVA = NAN;
  float m_byMediumIsolationMVA = NAN;
  float m_byTightIsolationMVA = NAN;
  float m_byIsolationMVA2raw = NAN;
  float m_byLooseIsolationMVA2 = NAN;
  float m_byMediumIsolationMVA2 = NAN;
  float m_byTightIsolationMVA2 = NAN;
  float m_byLooseCombinedIsolationDeltaBetaCorr3Hits = NAN;
  float m_byMediumCombinedIsolationDeltaBetaCorr3Hits = NAN;
  float m_byTightCombinedIsolationDeltaBetaCorr3Hits = NAN;
  float m_byCombinedIsolationDeltaBetaCorrRaw3Hits = NAN;
  float m_againstElectronMVA3raw = NAN;
  int   m_againstElectronMVA3category = 0;
  float m_againstElectronLooseMVA3 = NAN;
  float m_againstElectronMediumMVA3 = NAN;
  float m_againstElectronTightMVA3 = NAN;
  float m_againstElectronVTightMVA3 = NAN;
  float m_againstElectronDeadECAL = NAN;
  float m_againstMuonLoose2 = NAN;
  float m_againstMuonMedium2 = NAN;
  float m_againstMuonTight2 = NAN;
  float m_againstMuonLoose3 = NAN;
  float m_againstMuonTight3 = NAN;
  float m_antiEMVA3NewLooseWP = NAN;
  float m_antiEMVA3NewMediumWP = NAN;
  float m_antiEMVA3NewTightWP = NAN;
  float m_antiEMVA3NewVeryTightWP = NAN;

}




// will set this in TupleTauProducer, since we can track all cuts
// more easily when calling the producer
void TupleTau::set_passFullId(bool passFullId_) { m_passFullId = passFullId_;}
bool TupleTau::passFullId() const  { return m_passFullId; }

void TupleTau::set_p4(LorentzVector v4_) { m_p4 = v4_;}
LorentzVector TupleTau::p4() const  { return m_p4; }

void TupleTau::set_genP4(LorentzVector v4_) { m_genP4 = v4_;}
LorentzVector TupleTau::genP4() const  { return m_genP4; }


// the tau discriminators


//////////////////////////////////////////
//byIsolationMVAraw
//////////////////////////////////////////

void TupleTau::set_byIsolationMVAraw(float byIsolationMVAraw_)
{
  m_byIsolationMVAraw = byIsolationMVAraw_;
}
float TupleTau::byIsolationMVAraw() const { return m_byIsolationMVAraw;}

//////////////////////////////////////////
//byLooseIsolationMVA
//////////////////////////////////////////

void TupleTau::set_byLooseIsolationMVA(float byLooseIsolationMVA_)
{
  m_byLooseIsolationMVA = byLooseIsolationMVA_;
}
float TupleTau::byLooseIsolationMVA() const { return m_byLooseIsolationMVA;}

//////////////////////////////////////////
//byMediumIsolationMVA
//////////////////////////////////////////

void TupleTau::set_byMediumIsolationMVA(float byMediumIsolationMVA_)
{
  m_byMediumIsolationMVA = byMediumIsolationMVA_;
}
float TupleTau::byMediumIsolationMVA() const { return m_byMediumIsolationMVA;}

//////////////////////////////////////////
//byTightIsolationMVA
//////////////////////////////////////////

void TupleTau::set_byTightIsolationMVA(float byTightIsolationMVA_)
{
  m_byTightIsolationMVA = byTightIsolationMVA_;
}
float TupleTau::byTightIsolationMVA() const { return m_byTightIsolationMVA;}

//////////////////////////////////////////
//byIsolationMVA2raw
//////////////////////////////////////////

void TupleTau::set_byIsolationMVA2raw(float byIsolationMVA2raw_)
{
  m_byIsolationMVA2raw = byIsolationMVA2raw_;
}
float TupleTau::byIsolationMVA2raw() const { return m_byIsolationMVA2raw;}

//////////////////////////////////////////
//byLooseIsolationMVA2
//////////////////////////////////////////

void TupleTau::set_byLooseIsolationMVA2(float byLooseIsolationMVA2_)
{
  m_byLooseIsolationMVA2 = byLooseIsolationMVA2_;
}
float TupleTau::byLooseIsolationMVA2() const { return m_byLooseIsolationMVA2;}

//////////////////////////////////////////
//byMediumIsolationMVA2
//////////////////////////////////////////

void TupleTau::set_byMediumIsolationMVA2(float byMediumIsolationMVA2_)
{
  m_byMediumIsolationMVA2 = byMediumIsolationMVA2_;
}
float TupleTau::byMediumIsolationMVA2() const { return m_byMediumIsolationMVA2;}

//////////////////////////////////////////
//byTightIsolationMVA2
//////////////////////////////////////////

void TupleTau::set_byTightIsolationMVA2(float byTightIsolationMVA2_)
{
  m_byTightIsolationMVA2 = byTightIsolationMVA2_;
}
float TupleTau::byTightIsolationMVA2() const { return m_byTightIsolationMVA2;}

//////////////////////////////////////////
//byLooseCombinedIsolationDeltaBetaCorr3Hits
//////////////////////////////////////////

void TupleTau::set_byLooseCombinedIsolationDeltaBetaCorr3Hits(float byLooseCombinedIsolationDeltaBetaCorr3Hits_)
{
  m_byLooseCombinedIsolationDeltaBetaCorr3Hits = byLooseCombinedIsolationDeltaBetaCorr3Hits_;
}
float TupleTau::byLooseCombinedIsolationDeltaBetaCorr3Hits() const { return m_byLooseCombinedIsolationDeltaBetaCorr3Hits;}

//////////////////////////////////////////
//byMediumCombinedIsolationDeltaBetaCorr3Hits
//////////////////////////////////////////

void TupleTau::set_byMediumCombinedIsolationDeltaBetaCorr3Hits(float byMediumCombinedIsolationDeltaBetaCorr3Hits_)
{
  m_byMediumCombinedIsolationDeltaBetaCorr3Hits = byMediumCombinedIsolationDeltaBetaCorr3Hits_;
}
float TupleTau::byMediumCombinedIsolationDeltaBetaCorr3Hits() const { return m_byMediumCombinedIsolationDeltaBetaCorr3Hits;}

//////////////////////////////////////////
//byTightCombinedIsolationDeltaBetaCorr3Hits
//////////////////////////////////////////

void TupleTau::set_byTightCombinedIsolationDeltaBetaCorr3Hits(float byTightCombinedIsolationDeltaBetaCorr3Hits_)
{
  m_byTightCombinedIsolationDeltaBetaCorr3Hits = byTightCombinedIsolationDeltaBetaCorr3Hits_;
}
float TupleTau::byTightCombinedIsolationDeltaBetaCorr3Hits() const { return m_byTightCombinedIsolationDeltaBetaCorr3Hits;}

//////////////////////////////////////////
//byCombinedIsolationDeltaBetaCorrRaw3Hits
//////////////////////////////////////////

void TupleTau::set_byCombinedIsolationDeltaBetaCorrRaw3Hits(float byCombinedIsolationDeltaBetaCorrRaw3Hits_)
{
  m_byCombinedIsolationDeltaBetaCorrRaw3Hits = byCombinedIsolationDeltaBetaCorrRaw3Hits_;
}
float TupleTau::byCombinedIsolationDeltaBetaCorrRaw3Hits() const { return m_byCombinedIsolationDeltaBetaCorrRaw3Hits;}

//////////////////////////////////////////
//againstElectronMVA3raw
//////////////////////////////////////////

void TupleTau::set_againstElectronMVA3raw(float againstElectronMVA3raw_)
{
  m_againstElectronMVA3raw = againstElectronMVA3raw_;
}
float TupleTau::againstElectronMVA3raw() const { return m_againstElectronMVA3raw;}

//////////////////////////////////////////
//againstElectronMVA3category
//////////////////////////////////////////

void TupleTau::set_againstElectronMVA3category(int againstElectronMVA3category_)
{
  m_againstElectronMVA3category = againstElectronMVA3category_;
}
int TupleTau::againstElectronMVA3category() const { return m_againstElectronMVA3category;}

//////////////////////////////////////////
//againstElectronLooseMVA3
//////////////////////////////////////////

void TupleTau::set_againstElectronLooseMVA3(float againstElectronLooseMVA3_)
{
  m_againstElectronLooseMVA3 = againstElectronLooseMVA3_;
}
float TupleTau::againstElectronLooseMVA3() const { return m_againstElectronLooseMVA3;}

//////////////////////////////////////////
//againstElectronMediumMVA3
//////////////////////////////////////////

void TupleTau::set_againstElectronMediumMVA3(float againstElectronMediumMVA3_)
{
  m_againstElectronMediumMVA3 = againstElectronMediumMVA3_;
}
float TupleTau::againstElectronMediumMVA3() const { return m_againstElectronMediumMVA3;}

//////////////////////////////////////////
//againstElectronTightMVA3
//////////////////////////////////////////

void TupleTau::set_againstElectronTightMVA3(float againstElectronTightMVA3_)
{
  m_againstElectronTightMVA3 = againstElectronTightMVA3_;
}
float TupleTau::againstElectronTightMVA3() const { return m_againstElectronTightMVA3;}

//////////////////////////////////////////
//againstElectronVTightMVA3
//////////////////////////////////////////

void TupleTau::set_againstElectronVTightMVA3(float againstElectronVTightMVA3_)
{
  m_againstElectronVTightMVA3 = againstElectronVTightMVA3_;
}
float TupleTau::againstElectronVTightMVA3() const { return m_againstElectronVTightMVA3;}

//////////////////////////////////////////
//againstElectronDeadECAL
//////////////////////////////////////////

void TupleTau::set_againstElectronDeadECAL(float againstElectronDeadECAL_)
{
  m_againstElectronDeadECAL = againstElectronDeadECAL_;
}
float TupleTau::againstElectronDeadECAL() const { return m_againstElectronDeadECAL;}

//////////////////////////////////////////
//againstMuonLoose2
//////////////////////////////////////////

void TupleTau::set_againstMuonLoose2(float againstMuonLoose2_)
{
  m_againstMuonLoose2 = againstMuonLoose2_;
}
float TupleTau::againstMuonLoose2() const { return m_againstMuonLoose2;}

//////////////////////////////////////////
//againstMuonMedium2
//////////////////////////////////////////

void TupleTau::set_againstMuonMedium2(float againstMuonMedium2_)
{
  m_againstMuonMedium2 = againstMuonMedium2_;
}
float TupleTau::againstMuonMedium2() const { return m_againstMuonMedium2;}

//////////////////////////////////////////
//againstMuonTight2
//////////////////////////////////////////

void TupleTau::set_againstMuonTight2(float againstMuonTight2_)
{
  m_againstMuonTight2 = againstMuonTight2_;
}
float TupleTau::againstMuonTight2() const { return m_againstMuonTight2;}

//////////////////////////////////////////
//againstMuonLoose3
//////////////////////////////////////////

void TupleTau::set_againstMuonLoose3(float againstMuonLoose3_)
{
  m_againstMuonLoose3 = againstMuonLoose3_;
}
float TupleTau::againstMuonLoose3() const { return m_againstMuonLoose3;}

//////////////////////////////////////////
//againstMuonTight3
//////////////////////////////////////////

void TupleTau::set_againstMuonTight3(float againstMuonTight3_)
{
  m_againstMuonTight3 = againstMuonTight3_;
}
float TupleTau::againstMuonTight3() const { return m_againstMuonTight3;}



// modified WP versions of the anitE MVA3

/////////////////////
//  new loose WP
/////////////////////

void TupleTau::set_antiEMVA3NewLooseWP(float againstElectronLooseMVA3raw_,
int againstElectronMVA3category_)
{
  int WorkingPoint = 0;
  m_antiEMVA3NewLooseWP = TupleHelpers::passAntiEMVA(againstElectronMVA3category_,
  againstElectronLooseMVA3raw_,
  WorkingPoint);

}

float TupleTau::antiEMVA3NewLooseWP() const { return m_antiEMVA3NewLooseWP;}

/////////////////////
//  new medium WP
/////////////////////

void TupleTau::set_antiEMVA3NewMediumWP(float againstElectronLooseMVA3raw_,
int againstElectronMVA3category_)
{
  int WorkingPoint = 1;
  m_antiEMVA3NewMediumWP = TupleHelpers::passAntiEMVA(againstElectronMVA3category_,
  againstElectronLooseMVA3raw_,
  WorkingPoint);

}

float TupleTau::antiEMVA3NewMediumWP() const { return m_antiEMVA3NewMediumWP;}

/////////////////////
//  new tight WP
/////////////////////

void TupleTau::set_antiEMVA3NewTightWP(float againstElectronLooseMVA3raw_,
int againstElectronMVA3category_)
{

  int WorkingPoint = 2;
  m_antiEMVA3NewTightWP = TupleHelpers::passAntiEMVA(againstElectronMVA3category_,
  againstElectronLooseMVA3raw_,
  WorkingPoint);

}

float TupleTau::antiEMVA3NewTightWP() const { return m_antiEMVA3NewTightWP;}

/////////////////////
//  new v. tight WP
/////////////////////


void TupleTau::set_antiEMVA3NewVeryTightWP(float againstElectronLooseMVA3raw_,
int againstElectronMVA3category_)
{

  int WorkingPoint = 3;
  m_antiEMVA3NewVeryTightWP = TupleHelpers::passAntiEMVA(againstElectronMVA3category_,
  againstElectronLooseMVA3raw_,
  WorkingPoint);

}


float TupleTau::antiEMVA3NewVeryTightWP() const { return m_antiEMVA3NewVeryTightWP;}


/////////////////////
/////////////////////

void TupleTau::set_corrected_p4(LorentzVector v4_, int decayMode_)
{

  double v4_sf = 1.0;

  ///////////////////
  // corrections from
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingSummer2013
  // #TauES_and_decay_mode_scale_facto

  // caution, these corrections should only be applied
  // for certain MC samples
  cout<<" Warning correcting energy of all Taus, add in a sample & MC check!!!!!"<<endl;

  // one prong, 1 pi0
  if(decayMode_==1)   v4_sf = (1.025 + 0.001 * std::min(std::max(v4_.pt()-45.,0.),10.));

  // 3 prong, 0 to N pi0
  if(decayMode_>=10 && decayMode_<=14)   v4_sf = (1.012 + 0.001 * std::min(std::max(v4_.pt()-32.,0.),18.));




  m_corrected_p4 = v4_*v4_sf;


}



LorentzVector TupleTau::corrected_p4() const  { return m_corrected_p4; }


void TupleTau::set_pdgId(int pdgId_) { m_pdgId = pdgId_;}
int TupleTau::pdgId() const  { return m_pdgId; }

void TupleTau::set_charge(int charge_) { m_charge = charge_;}
int TupleTau::charge() const  { return m_charge; }

void TupleTau::set_decayMode(int decayMode_) { m_decayMode = decayMode_;}
int TupleTau::decayMode() const  { return m_decayMode; }
