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

}

//Setting Weights


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
