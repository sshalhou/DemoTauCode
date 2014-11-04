#include <TROOT.h>
#include <TFile.h>

#include <TMath.h>

#include <TSelector.h>

// Header file for the classes stored in the TTree if any.
#include <string>
#include <vector>
#include <iostream>
#include <TLorentzVector.h>

using namespace std;


bool passesMuTauOrETau(TChain* chain )
{

  deRef();
  bool passes = 1;

  int nMuTauPass = 0;
  int nETauPass = 0;

for(size_t index = 0; index < muT_correctedSVFitMass_.size(); ++index)
  {

    bool localPass = 1;

    TLorentzVector Lvec(0,0,0,0);
    Lvec.SetXYZT(muT_muon_p4_x_[index], muT_muon_p4_y_[index], muT_muon_p4_z_[index],muT_muon_p4_t_[index]);

    if(  !(Lvec.Pt()>20)                            ) localPass = 0;
    if(  !(fabs(Lvec.Eta())<2.1)                    ) localPass = 0;


    if(  !muT_muon_isGlobalMuon_[index]              ) localPass = 0;
    if(  !muT_muon_isTightMuon_[index]               ) localPass = 0;
    if(  !muT_muon_isPFMuon_[index]                  ) localPass = 0;
    if(  muT_muon_relativeIso_DR4_[index] > 0.6     ) localPass = 0;
    if(  !(fabs(muT_muon_dxy_[index])<0.045)         ) localPass = 0;
    if(  !(fabs(muT_muon_dz_[index])<0.2)            ) localPass = 0;

    Lvec.SetXYZT(muT_tau_corrected_p4_x_[index], muT_tau_corrected_p4_y_[index], muT_tau_corrected_p4_z_[index],muT_tau_corrected_p4_t_[index]);

    if(  !(Lvec.Pt()>30)                            ) localPass = 0;
    if(  !(fabs(Lvec.Eta())<2.3)                    ) localPass = 0;
    if( !muT_tau_byTightIsolationMVA3oldDMwLT_[index] && !muT_tau_byLooseIsolationMVA3oldDMwLT_[index]) localPass = 0;
    if( !muT_tau_decayModeFindingOldDMs_[index]      ) localPass = 0;
    if( !muT_tau_againstMuonMediumMVA_[index]        ) localPass = 0;
    if( !muT_tau_againstElectronLoose_[index]        ) localPass = 0;

    if( (muT_DR_[index] <= 0.5)                        ) localPass = 0;
    if( muT_TransverseMass_[index] > 31.00 && muT_TransverseMass_[index] < 69.00 ) localPass = 0;
    if( !muT_passesSecondLeptonVeto_[index]           ) localPass = 0;
    if( !muT_passesThirdLeptonVeto_[index]            ) localPass = 0;

    if(!isNonTopEmbeddedSample_ && !isTopEmbeddedSample_)
      {
        if(!muT_muon_has_HltMatchMu17_[index] && !muT_muon_has_HltMatchMu18_[index]) localPass = 0;
        if(!muT_tau_has_HltMatchMu17_[index] && !muT_tau_has_HltMatchMu18_[index]) localPass = 0;
      }



    if(localPass){ nMuTauPass++;}
    if(nMuTauPass>0) break;
  }


  for(size_t index = 0; index < eT_correctedSVFitMass_.size(); ++index)
    {

      bool localPass = 1;

      TLorentzVector Lvec(0,0,0,0);
      Lvec.SetXYZT(eT_ele_p4_x_[index], eT_ele_p4_y_[index], eT_ele_p4_z_[index],eT_ele_p4_t_[index]);

      if(  !(Lvec.Pt()>24)                            ) localPass = 0;
      if(  !(fabs(Lvec.Eta())<2.1)                    ) localPass = 0;
      if(  eT_ele_numberOfMissingInnerHits_[index]!=0 ) localPass = 0;
      if(  !eT_ele_passConversionVeto_[index]         ) localPass = 0;
      if(  !eT_ele_pass_tight_mvaNonTrigV0_[index]    ) localPass = 0;
      if(  eT_ele_relativeIso_[index] > 0.6           ) localPass = 0;
      if(  !(fabs(eT_ele_dxy_[index])<0.045)          ) localPass = 0;
      if(  !(fabs(eT_ele_dz_[index])<0.2)             ) localPass = 0;


      Lvec.SetXYZT(eT_tau_corrected_p4_x_[index], eT_tau_corrected_p4_y_[index], eT_tau_corrected_p4_z_[index],eT_tau_corrected_p4_t_[index]);

      if(  !(Lvec.Pt()>30)                            ) localPass = 0;
      if(  !(fabs(Lvec.Eta())<2.3)                    ) localPass = 0;
      if( !eT_tau_byTightIsolationMVA3oldDMwLT_[index] && !eT_tau_byLooseIsolationMVA3oldDMwLT_[index]) localPass = 0;
      if( !eT_tau_decayModeFindingOldDMs_[index]      ) localPass = 0;
      if( !eT_tau_againstElectronMediumMVA5_[index]   ) localPass = 0;
      if( !eT_tau_againstMuonLoose3_[index]           ) localPass = 0;

      if( (eT_DR_[index] <= 0.5)                        ) localPass = 0;
      if( eT_TransverseMass_[index] > 31.00 && eT_TransverseMass_[index] < 69.00 ) localPass = 0;
      if( !eT_passesSecondLeptonVeto_[index]           ) localPass = 0;
      if( !eT_passesThirdLeptonVeto_[index]            ) localPass = 0;

      if(!isNonTopEmbeddedSample_ && !isTopEmbeddedSample_)
        {
          if(!eT_ele_has_HltMatchEle20_[index] && !eT_ele_has_HltMatchEle22_[index]) localPass = 0;
          if(!eT_tau_has_HltMatchEle20_[index] && !eT_tau_has_HltMatchEle22_[index]) localPass = 0;
        }


      if(localPass){ nETauPass++;}
      if(nETauPass>0) break;
    }



  if(nMuTauPass==0 && nETauPass==0) passes = 0;
  //std::cout<<" passes "<<passes<<"\n";
  return passes;
}
