#include "UserCode/TupleObjects/interface/TupleElectronTauWeight.h"
#include "TMath.h"

TupleElectronTauWeight::TupleElectronTauWeight()
{
  m_puWeight = NAN;
  m_puWeightM1 = NAN;
  m_puWeightP1 = NAN;
  m_NumPileupInt = NAN;
  m_NumTruePileUpInt = NAN;
  m_NumPileupIntM1 = NAN;
  m_NumTruePileUpIntM1 = NAN;
  m_NumPileupIntP1 = NAN;
  m_NumTruePileUpIntP1 = NAN;
  m_EffDataELE20andELE22 = NAN;
  m_EffMcELE20andELE22 = NAN;
  m_HadronicTauDataTrigEffAntiEMed = NAN;
  m_HadronicTauMcTrigEffAntiEMed = NAN;
  m_HadronicTauDataTrigEffAntiETight = NAN;
  m_HadronicTauMcTrigEffAntiETight = NAN;
  m_electronDataIDweight = NAN;
  m_electronMcIDweight = NAN;
  m_electronDataISOLweight = NAN;
  m_electronMcISOLweight = NAN;
  m_EffDataHighPtTauTrigger = NAN;
  m_EffMcHighPtTauTrigger = NAN;
  m_TauFakeCorrection = NAN;
  m_DecayModeCorrectionFactor = NAN;
  m_ZeeScaleFactor = NAN;
  m_nominalHIGLUXHQTmhmax = NAN;
  m_upHIGLUXHQTmhmax = NAN;
  m_downHIGLUXHQTmhmax = NAN;
  m_nominalPOWHEGmhmod = NAN;
  m_upPOWHEGmhmod = NAN;
  m_downPOWHEGmhmod = NAN;
  m_upPOWHEGscale = NAN;
  m_downPOWHEGscale = NAN;
  m_etaDepQCDShapeTemplateCorrection = NAN;
  m_inclusiveQCDShapeTemplateCorrection = NAN;
  m_TTbarPtWeight = NAN;
  m_TauSpinnerWT = NAN;
  m_TauSpinnerWTFlip = NAN;
  m_TauSpinnerWThminus = NAN;
  m_TauSpinnerWThplus = NAN;
  m_hepNUP = -999;
  m_weightHEPNUP_DYJets = NAN;
  m_weightHEPNUP_WJets = NAN;
  m_embedWeight = NAN;


}

//Setting Weights


//////////////////
// embedding weight


void TupleElectronTauWeight::set_embedWeight(double embedWeight_) { m_embedWeight  =  embedWeight_;}
double TupleElectronTauWeight::embedWeight() const { return m_embedWeight; }


//////////////
// tau spinner weights

void TupleElectronTauWeight::set_TauSpinnerWT(double TauSpinnerWT_) { m_TauSpinnerWT  =  TauSpinnerWT_;}
double TupleElectronTauWeight::TauSpinnerWT() const { return m_TauSpinnerWT; }

void TupleElectronTauWeight::set_TauSpinnerWTFlip(double TauSpinnerWTFlip_) { m_TauSpinnerWTFlip  =  TauSpinnerWTFlip_;}
double TupleElectronTauWeight::TauSpinnerWTFlip() const { return m_TauSpinnerWTFlip; }

void TupleElectronTauWeight::set_TauSpinnerWThminus(double TauSpinnerWThminus_) { m_TauSpinnerWThminus  =  TauSpinnerWThminus_;}
double TupleElectronTauWeight::TauSpinnerWThminus() const { return m_TauSpinnerWThminus; }

void TupleElectronTauWeight::set_TauSpinnerWThplus(double TauSpinnerWThplus_) { m_TauSpinnerWThplus  =  TauSpinnerWThplus_;}
double TupleElectronTauWeight::TauSpinnerWThplus() const { return m_TauSpinnerWThplus; }


///////////////
// n parton weights

void TupleElectronTauWeight::set_hepNUP(int hepNUP_) { m_hepNUP  =  hepNUP_;}
int TupleElectronTauWeight::hepNUP() const { return m_hepNUP; }

void TupleElectronTauWeight::set_weightHEPNUP_DYJets(double weightHEPNUP_DYJets_) { m_weightHEPNUP_DYJets  =  weightHEPNUP_DYJets_;}
double TupleElectronTauWeight::weightHEPNUP_DYJets() const { return m_weightHEPNUP_DYJets; }

void TupleElectronTauWeight::set_weightHEPNUP_WJets(double weightHEPNUP_WJets_) { m_weightHEPNUP_WJets  =  weightHEPNUP_WJets_;}
double TupleElectronTauWeight::weightHEPNUP_WJets() const { return m_weightHEPNUP_WJets; }



/////////////
// tt pt reweight

void TupleElectronTauWeight::set_TTbarPtWeight(double TTbarPtWeight_) { m_TTbarPtWeight  =  TTbarPtWeight_;}
double TupleElectronTauWeight::TTbarPtWeight() const { return m_TTbarPtWeight; }

///////////////
// QCD template reweight

void TupleElectronTauWeight::set_etaDepQCDShapeTemplateCorrection(double etaDepQCDShapeTemplateCorrection_) { m_etaDepQCDShapeTemplateCorrection  =  etaDepQCDShapeTemplateCorrection_;}
double TupleElectronTauWeight::etaDepQCDShapeTemplateCorrection() const { return m_etaDepQCDShapeTemplateCorrection; }

void TupleElectronTauWeight::set_inclusiveQCDShapeTemplateCorrection(double inclusiveQCDShapeTemplateCorrection_) { m_inclusiveQCDShapeTemplateCorrection  =  inclusiveQCDShapeTemplateCorrection_;}
double TupleElectronTauWeight::inclusiveQCDShapeTemplateCorrection() const { return m_inclusiveQCDShapeTemplateCorrection; }


///////////////
// higgs pt weight for SUSY signal

void TupleElectronTauWeight::set_nominalHIGLUXHQTmhmax(double nominalHIGLUXHQTmhmax_) { m_nominalHIGLUXHQTmhmax  =  nominalHIGLUXHQTmhmax_;}
double TupleElectronTauWeight::nominalHIGLUXHQTmhmax() const { return m_nominalHIGLUXHQTmhmax; }

void TupleElectronTauWeight::set_upHIGLUXHQTmhmax(double upHIGLUXHQTmhmax_) { m_upHIGLUXHQTmhmax  =  upHIGLUXHQTmhmax_;}
double TupleElectronTauWeight::upHIGLUXHQTmhmax() const { return m_upHIGLUXHQTmhmax; }

void TupleElectronTauWeight::set_downHIGLUXHQTmhmax(double downHIGLUXHQTmhmax_) { m_downHIGLUXHQTmhmax  =  downHIGLUXHQTmhmax_;}
double TupleElectronTauWeight::downHIGLUXHQTmhmax() const { return m_downHIGLUXHQTmhmax; }

void TupleElectronTauWeight::set_nominalPOWHEGmhmod(double nominalPOWHEGmhmod_) { m_nominalPOWHEGmhmod  =  nominalPOWHEGmhmod_;}
double TupleElectronTauWeight::nominalPOWHEGmhmod() const { return m_nominalPOWHEGmhmod; }

void TupleElectronTauWeight::set_upPOWHEGmhmod(double upPOWHEGmhmod_) { m_upPOWHEGmhmod  =  upPOWHEGmhmod_;}
double TupleElectronTauWeight::upPOWHEGmhmod() const { return m_upPOWHEGmhmod; }

void TupleElectronTauWeight::set_downPOWHEGmhmod(double downPOWHEGmhmod_) { m_downPOWHEGmhmod  =  downPOWHEGmhmod_;}
double TupleElectronTauWeight::downPOWHEGmhmod() const { return m_downPOWHEGmhmod; }



void TupleElectronTauWeight::set_upPOWHEGscale(double upPOWHEGscale_) { m_upPOWHEGscale  =  upPOWHEGscale_;}
double TupleElectronTauWeight::upPOWHEGscale() const { return m_upPOWHEGscale; }

void TupleElectronTauWeight::set_downPOWHEGscale(double downPOWHEGscale_) { m_downPOWHEGscale  =  downPOWHEGscale_;}
double TupleElectronTauWeight::downPOWHEGscale() const { return m_downPOWHEGscale; }




/////////////////
// Zee sample e->tau_h
// fake correction

void TupleElectronTauWeight::set_ZeeScaleFactor(double ZeeScaleFactor_) { m_ZeeScaleFactor  =  ZeeScaleFactor_;}
double TupleElectronTauWeight::ZeeScaleFactor() const { return m_ZeeScaleFactor; }


////////////////////
// decay mode corr.
// for Z->tau tau
// and signal

void TupleElectronTauWeight::set_DecayModeCorrectionFactor(double DecayModeCorrectionFactor_) { m_DecayModeCorrectionFactor  =  DecayModeCorrectionFactor_;}
double TupleElectronTauWeight::DecayModeCorrectionFactor() const { return m_DecayModeCorrectionFactor; }




///////////////////
// jet to tau fake weight
// for w+jets

void TupleElectronTauWeight::set_TauFakeCorrection(double TauFakeCorrection_) { m_TauFakeCorrection  =  TauFakeCorrection_;}
double TupleElectronTauWeight::TauFakeCorrection() const { return m_TauFakeCorrection; }



//////////////////
// hight pt tau trigger bug

void TupleElectronTauWeight::set_EffDataHighPtTauTrigger(double EffDataHighPtTauTrigger_) { m_EffDataHighPtTauTrigger  =  EffDataHighPtTauTrigger_;}
double TupleElectronTauWeight::EffDataHighPtTauTrigger() const { return m_EffDataHighPtTauTrigger; }

void TupleElectronTauWeight::set_EffMcHighPtTauTrigger(double EffMcHighPtTauTrigger_) { m_EffMcHighPtTauTrigger  =  EffMcHighPtTauTrigger_;}
double TupleElectronTauWeight::EffMcHighPtTauTrigger() const { return m_EffMcHighPtTauTrigger; }



//////////////////
// electron ID and ISOL


void TupleElectronTauWeight::set_electronDataIDweight(double electronDataIDweight_) { m_electronDataIDweight  =  electronDataIDweight_;}
double TupleElectronTauWeight::electronDataIDweight() const { return m_electronDataIDweight; }

void TupleElectronTauWeight::set_electronMcIDweight(double electronMcIDweight_) { m_electronMcIDweight  =  electronMcIDweight_;}
double TupleElectronTauWeight::electronMcIDweight() const { return m_electronMcIDweight; }

void TupleElectronTauWeight::set_electronDataISOLweight(double electronDataISOLweight_) { m_electronDataISOLweight  =  electronDataISOLweight_;}
double TupleElectronTauWeight::electronDataISOLweight() const { return m_electronDataISOLweight; }

void TupleElectronTauWeight::set_electronMcISOLweight(double electronMcISOLweight_) { m_electronMcISOLweight  =  electronMcISOLweight_;}
double TupleElectronTauWeight::electronMcISOLweight() const { return m_electronMcISOLweight; }






/////////////////
// tau weights for eTau

void TupleElectronTauWeight::set_HadronicTauDataTrigEffAntiEMed(double HadronicTauDataTrigEffAntiEMed_) { m_HadronicTauDataTrigEffAntiEMed  =  HadronicTauDataTrigEffAntiEMed_;}
double TupleElectronTauWeight::HadronicTauDataTrigEffAntiEMed() const { return m_HadronicTauDataTrigEffAntiEMed; }

void TupleElectronTauWeight::set_HadronicTauMcTrigEffAntiEMed(double HadronicTauMcTrigEffAntiEMed_) { m_HadronicTauMcTrigEffAntiEMed  =  HadronicTauMcTrigEffAntiEMed_;}
double TupleElectronTauWeight::HadronicTauMcTrigEffAntiEMed() const { return m_HadronicTauMcTrigEffAntiEMed; }

void TupleElectronTauWeight::set_HadronicTauDataTrigEffAntiETight(double HadronicTauDataTrigEffAntiETight_) { m_HadronicTauDataTrigEffAntiETight  =  HadronicTauDataTrigEffAntiETight_;}
double TupleElectronTauWeight::HadronicTauDataTrigEffAntiETight() const { return m_HadronicTauDataTrigEffAntiETight; }

void TupleElectronTauWeight::set_HadronicTauMcTrigEffAntiETight(double HadronicTauMcTrigEffAntiETight_) { m_HadronicTauMcTrigEffAntiETight  =  HadronicTauMcTrigEffAntiETight_;}
double TupleElectronTauWeight::HadronicTauMcTrigEffAntiETight() const { return m_HadronicTauMcTrigEffAntiETight; }



///////////////////////
// electron trigger
// weights

void TupleElectronTauWeight::set_EffDataELE20andELE22(double EffDataELE20andELE22_) { m_EffDataELE20andELE22  =  EffDataELE20andELE22_;}
double TupleElectronTauWeight::EffDataELE20andELE22() const { return m_EffDataELE20andELE22; }

void TupleElectronTauWeight::set_EffMcELE20andELE22(double EffMcELE20andELE22_) { m_EffMcELE20andELE22  =  EffMcELE20andELE22_;}
double TupleElectronTauWeight::EffMcELE20andELE22() const { return m_EffMcELE20andELE22; }



////////////////////////
// pile-up reweight   //
////////////////////////

void TupleElectronTauWeight::set_puWeight(double puWeight_) { m_puWeight  =  puWeight_;}
double TupleElectronTauWeight::puWeight() const { return m_puWeight; }

void TupleElectronTauWeight::set_puWeightM1(double puWeightM1_) { m_puWeightM1  =  puWeightM1_;}
double TupleElectronTauWeight::puWeightM1() const { return m_puWeightM1; }

void TupleElectronTauWeight::set_puWeightP1(double puWeightP1_) { m_puWeightP1  =  puWeightP1_;}
double TupleElectronTauWeight::puWeightP1() const { return m_puWeightP1; }

void TupleElectronTauWeight::set_NumPileupInt(float NumPileupInt_) { m_NumPileupInt  =  NumPileupInt_;}
float TupleElectronTauWeight::NumPileupInt() const { return m_NumPileupInt; }

void TupleElectronTauWeight::set_NumTruePileUpInt(float NumTruePileUpInt_) { m_NumTruePileUpInt  =  NumTruePileUpInt_;}
float TupleElectronTauWeight::NumTruePileUpInt() const { return m_NumTruePileUpInt; }

void TupleElectronTauWeight::set_NumPileupIntM1(float NumPileupIntM1_) { m_NumPileupIntM1  =  NumPileupIntM1_;}
float TupleElectronTauWeight::NumPileupIntM1() const { return m_NumPileupIntM1; }

void TupleElectronTauWeight::set_NumTruePileUpIntM1(float NumTruePileUpIntM1_) { m_NumTruePileUpIntM1  =  NumTruePileUpIntM1_;}
float TupleElectronTauWeight::NumTruePileUpIntM1() const { return m_NumTruePileUpIntM1; }

void TupleElectronTauWeight::set_NumPileupIntP1(float NumPileupIntP1_) { m_NumPileupIntP1  =  NumPileupIntP1_;}
float TupleElectronTauWeight::NumPileupIntP1() const { return m_NumPileupIntP1; }

void TupleElectronTauWeight::set_NumTruePileUpIntP1(float NumTruePileUpIntP1_) { m_NumTruePileUpIntP1  =  NumTruePileUpIntP1_;}
float TupleElectronTauWeight::NumTruePileUpIntP1() const { return m_NumTruePileUpIntP1; }
