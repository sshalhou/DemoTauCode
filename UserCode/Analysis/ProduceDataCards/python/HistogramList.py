import time
import sys
import os

#######################################################
# list of all possible histograms we want filled      #


HISTLIST = []

HISTLIST.append('QCD')
HISTLIST.append('QCD_CMS_htt_QCDfrShape_etau_8TeVDown')
HISTLIST.append('QCD_CMS_htt_QCDfrShape_etau_8TeVDown_fine_binning')
HISTLIST.append('QCD_CMS_htt_QCDfrShape_etau_8TeVUp')
HISTLIST.append('QCD_CMS_htt_QCDfrShape_etau_8TeVUp_fine_binning')
HISTLIST.append('QCD_CMS_htt_QCDfrShape_mutau_8TeVDown')
HISTLIST.append('QCD_CMS_htt_QCDfrShape_mutau_8TeVDown_fine_binning')
HISTLIST.append('QCD_CMS_htt_QCDfrShape_mutau_8TeVUp')
HISTLIST.append('QCD_CMS_htt_QCDfrShape_mutau_8TeVUp_fine_binning')
HISTLIST.append('QCD_CMS_scale_jDown')
HISTLIST.append('QCD_CMS_scale_jDown_fine_binning')
HISTLIST.append('QCD_CMS_scale_jUp')
HISTLIST.append('QCD_CMS_scale_jUp_fine_binning')
HISTLIST.append('QCD_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('QCD_CMS_scale_t_etau_8TeVDown_fine_binning')
HISTLIST.append('QCD_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('QCD_CMS_scale_t_etau_8TeVUp_fine_binning')
HISTLIST.append('QCD_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('QCD_CMS_scale_t_mutau_8TeVDown_fine_binning')
HISTLIST.append('QCD_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('QCD_CMS_scale_t_mutau_8TeVUp_fine_binning')
HISTLIST.append('QCD_fine_binning')
HISTLIST.append('TT')
HISTLIST.append('TT_CMS_htt_ZLScale_etau_8TeVDown')
HISTLIST.append('TT_CMS_htt_ZLScale_etau_8TeVUp')
HISTLIST.append('TT_CMS_htt_ZLScale_mutau_8TeVDown')
HISTLIST.append('TT_CMS_htt_ZLScale_mutau_8TeVUp')
HISTLIST.append('TT_CMS_htt_ttbarPtReweight_8TeVDown')
HISTLIST.append('TT_CMS_htt_ttbarPtReweight_8TeVUp')
HISTLIST.append('TT_CMS_scale_jDown')
HISTLIST.append('TT_CMS_scale_jDown_fine_binning')
HISTLIST.append('TT_CMS_scale_jUp')
HISTLIST.append('TT_CMS_scale_jUp_fine_binning')
HISTLIST.append('TT_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('TT_CMS_scale_t_etau_8TeVDown_fine_binning')
HISTLIST.append('TT_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('TT_CMS_scale_t_etau_8TeVUp_fine_binning')
HISTLIST.append('TT_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('TT_CMS_scale_t_mutau_8TeVDown_fine_binning')
HISTLIST.append('TT_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('TT_CMS_scale_t_mutau_8TeVUp_fine_binning')
HISTLIST.append('TT_fine_binning')
HISTLIST.append('VH_SM125')
HISTLIST.append('VH_SM125_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('VH_SM125_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('VH_SM125_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('VH_SM125_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('VH_SM125_CMS_scale_jDown')
HISTLIST.append('VH_SM125_CMS_scale_jUp')
HISTLIST.append('VH_SM125_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('VH_SM125_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('VH_SM125_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('VH_SM125_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('VV')
HISTLIST.append('VV_CMS_scale_jDown')
HISTLIST.append('VV_CMS_scale_jDown_fine_binning')
HISTLIST.append('VV_CMS_scale_jUp')
HISTLIST.append('VV_CMS_scale_jUp_fine_binning')
HISTLIST.append('VV_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('VV_CMS_scale_t_etau_8TeVDown_fine_binning')
HISTLIST.append('VV_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('VV_CMS_scale_t_etau_8TeVUp_fine_binning')
HISTLIST.append('VV_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('VV_CMS_scale_t_mutau_8TeVDown_fine_binning')
HISTLIST.append('VV_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('VV_CMS_scale_t_mutau_8TeVUp_fine_binning')
HISTLIST.append('VV_fine_binning')
HISTLIST.append('W')
HISTLIST.append('W_CMS_htt_WShape_etau_btag_8TeVDown')
HISTLIST.append('W_CMS_htt_WShape_etau_btag_8TeVDown_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_etau_btag_8TeVUp')
HISTLIST.append('W_CMS_htt_WShape_etau_btag_8TeVUp_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_etau_btag_high_8TeVDown')
HISTLIST.append('W_CMS_htt_WShape_etau_btag_high_8TeVDown_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_etau_btag_high_8TeVUp')
HISTLIST.append('W_CMS_htt_WShape_etau_btag_high_8TeVUp_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_etau_btag_low_8TeVDown')
HISTLIST.append('W_CMS_htt_WShape_etau_btag_low_8TeVDown_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_etau_btag_low_8TeVUp')
HISTLIST.append('W_CMS_htt_WShape_etau_btag_low_8TeVUp_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_etau_nobtag_8TeVDown')
HISTLIST.append('W_CMS_htt_WShape_etau_nobtag_8TeVDown_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_etau_nobtag_8TeVUp')
HISTLIST.append('W_CMS_htt_WShape_etau_nobtag_8TeVUp_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_etau_nobtag_high_8TeVDown')
HISTLIST.append('W_CMS_htt_WShape_etau_nobtag_high_8TeVDown_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_etau_nobtag_high_8TeVUp')
HISTLIST.append('W_CMS_htt_WShape_etau_nobtag_high_8TeVUp_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_etau_nobtag_low_8TeVDown')
HISTLIST.append('W_CMS_htt_WShape_etau_nobtag_low_8TeVDown_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_etau_nobtag_low_8TeVUp')
HISTLIST.append('W_CMS_htt_WShape_etau_nobtag_low_8TeVUp_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_etau_nobtag_medium_8TeVDown')
HISTLIST.append('W_CMS_htt_WShape_etau_nobtag_medium_8TeVDown_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_etau_nobtag_medium_8TeVUp')
HISTLIST.append('W_CMS_htt_WShape_etau_nobtag_medium_8TeVUp_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_mutau_btag_8TeVDown')
HISTLIST.append('W_CMS_htt_WShape_mutau_btag_8TeVDown_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_mutau_btag_8TeVUp')
HISTLIST.append('W_CMS_htt_WShape_mutau_btag_8TeVUp_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_mutau_btag_high_8TeVDown')
HISTLIST.append('W_CMS_htt_WShape_mutau_btag_high_8TeVDown_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_mutau_btag_high_8TeVUp')
HISTLIST.append('W_CMS_htt_WShape_mutau_btag_high_8TeVUp_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_mutau_btag_low_8TeVDown')
HISTLIST.append('W_CMS_htt_WShape_mutau_btag_low_8TeVDown_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_mutau_btag_low_8TeVUp')
HISTLIST.append('W_CMS_htt_WShape_mutau_btag_low_8TeVUp_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_mutau_nobtag_8TeVDown')
HISTLIST.append('W_CMS_htt_WShape_mutau_nobtag_8TeVDown_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_mutau_nobtag_8TeVUp')
HISTLIST.append('W_CMS_htt_WShape_mutau_nobtag_8TeVUp_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_mutau_nobtag_high_8TeVDown')
HISTLIST.append('W_CMS_htt_WShape_mutau_nobtag_high_8TeVDown_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_mutau_nobtag_high_8TeVUp')
HISTLIST.append('W_CMS_htt_WShape_mutau_nobtag_high_8TeVUp_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_mutau_nobtag_low_8TeVDown')
HISTLIST.append('W_CMS_htt_WShape_mutau_nobtag_low_8TeVDown_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_mutau_nobtag_low_8TeVUp')
HISTLIST.append('W_CMS_htt_WShape_mutau_nobtag_low_8TeVUp_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_mutau_nobtag_medium_8TeVDown')
HISTLIST.append('W_CMS_htt_WShape_mutau_nobtag_medium_8TeVDown_fine_binning')
HISTLIST.append('W_CMS_htt_WShape_mutau_nobtag_medium_8TeVUp')
HISTLIST.append('W_CMS_htt_WShape_mutau_nobtag_medium_8TeVUp_fine_binning')
HISTLIST.append('W_CMS_scale_jDown')
HISTLIST.append('W_CMS_scale_jDown_fine_binning')
HISTLIST.append('W_CMS_scale_jUp')
HISTLIST.append('W_CMS_scale_jUp_fine_binning')
HISTLIST.append('W_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('W_CMS_scale_t_etau_8TeVDown_fine_binning')
HISTLIST.append('W_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('W_CMS_scale_t_etau_8TeVUp_fine_binning')
HISTLIST.append('W_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('W_CMS_scale_t_mutau_8TeVDown_fine_binning')
HISTLIST.append('W_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('W_CMS_scale_t_mutau_8TeVUp_fine_binning')
HISTLIST.append('W_fine_binning')
HISTLIST.append('ZJ')
HISTLIST.append('ZJ_CMS_scale_jDown')
HISTLIST.append('ZJ_CMS_scale_jDown_fine_binning')
HISTLIST.append('ZJ_CMS_scale_jUp')
HISTLIST.append('ZJ_CMS_scale_jUp_fine_binning')
HISTLIST.append('ZJ_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ZJ_CMS_scale_t_etau_8TeVDown_fine_binning')
HISTLIST.append('ZJ_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ZJ_CMS_scale_t_etau_8TeVUp_fine_binning')
HISTLIST.append('ZJ_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ZJ_CMS_scale_t_mutau_8TeVDown_fine_binning')
HISTLIST.append('ZJ_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ZJ_CMS_scale_t_mutau_8TeVUp_fine_binning')
HISTLIST.append('ZJ_fine_binning')
HISTLIST.append('ZL')
HISTLIST.append('ZL_CMS_htt_ZLScale_etau_8TeVDown')
HISTLIST.append('ZL_CMS_htt_ZLScale_etau_8TeVUp')
HISTLIST.append('ZL_CMS_htt_ZLScale_mutau_8TeVDown')
HISTLIST.append('ZL_CMS_htt_ZLScale_mutau_8TeVUp')
HISTLIST.append('ZL_CMS_scale_jDown')
HISTLIST.append('ZL_CMS_scale_jDown_fine_binning')
HISTLIST.append('ZL_CMS_scale_jUp')
HISTLIST.append('ZL_CMS_scale_jUp_fine_binning')
HISTLIST.append('ZL_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ZL_CMS_scale_t_etau_8TeVDown_fine_binning')
HISTLIST.append('ZL_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ZL_CMS_scale_t_etau_8TeVUp_fine_binning')
HISTLIST.append('ZL_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ZL_CMS_scale_t_mutau_8TeVDown_fine_binning')
HISTLIST.append('ZL_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ZL_CMS_scale_t_mutau_8TeVUp_fine_binning')
HISTLIST.append('ZL_fine_binning')
HISTLIST.append('ZTT')
HISTLIST.append('ZTT_CMS_scale_jDown')
HISTLIST.append('ZTT_CMS_scale_jDown_fine_binning')
HISTLIST.append('ZTT_CMS_scale_jUp')
HISTLIST.append('ZTT_CMS_scale_jUp_fine_binning')
HISTLIST.append('ZTT_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ZTT_CMS_scale_t_etau_8TeVDown_fine_binning')
HISTLIST.append('ZTT_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ZTT_CMS_scale_t_etau_8TeVUp_fine_binning')
HISTLIST.append('ZTT_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ZTT_CMS_scale_t_mutau_8TeVDown_fine_binning')
HISTLIST.append('ZTT_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ZTT_CMS_scale_t_mutau_8TeVUp_fine_binning')
HISTLIST.append('ZTT_fine_binning')
HISTLIST.append('bbH100')
HISTLIST.append('bbH1000')
HISTLIST.append('bbH1000_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH1000_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH1000_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH1000_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH1000_CMS_scale_jDown')
HISTLIST.append('bbH1000_CMS_scale_jUp')
HISTLIST.append('bbH1000_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH1000_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH1000_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH1000_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH100_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH100_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH100_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH100_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH100_CMS_scale_jDown')
HISTLIST.append('bbH100_CMS_scale_jUp')
HISTLIST.append('bbH100_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH100_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH100_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH100_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH110')
HISTLIST.append('bbH110_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH110_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH110_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH110_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH110_CMS_scale_jDown')
HISTLIST.append('bbH110_CMS_scale_jUp')
HISTLIST.append('bbH110_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH110_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH110_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH110_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH120')
HISTLIST.append('bbH120_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH120_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH120_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH120_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH120_CMS_scale_jDown')
HISTLIST.append('bbH120_CMS_scale_jUp')
HISTLIST.append('bbH120_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH120_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH120_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH120_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH130')
HISTLIST.append('bbH130_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH130_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH130_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH130_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH130_CMS_scale_jDown')
HISTLIST.append('bbH130_CMS_scale_jUp')
HISTLIST.append('bbH130_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH130_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH130_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH130_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH140')
HISTLIST.append('bbH140_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH140_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH140_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH140_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH140_CMS_scale_jDown')
HISTLIST.append('bbH140_CMS_scale_jUp')
HISTLIST.append('bbH140_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH140_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH140_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH140_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH160')
HISTLIST.append('bbH160_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH160_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH160_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH160_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH160_CMS_scale_jDown')
HISTLIST.append('bbH160_CMS_scale_jUp')
HISTLIST.append('bbH160_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH160_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH160_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH160_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH180')
HISTLIST.append('bbH180_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH180_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH180_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH180_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH180_CMS_scale_jDown')
HISTLIST.append('bbH180_CMS_scale_jUp')
HISTLIST.append('bbH180_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH180_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH180_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH180_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH200')
HISTLIST.append('bbH200_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH200_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH200_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH200_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH200_CMS_scale_jDown')
HISTLIST.append('bbH200_CMS_scale_jUp')
HISTLIST.append('bbH200_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH200_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH200_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH200_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH250')
HISTLIST.append('bbH250_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH250_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH250_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH250_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH250_CMS_scale_jDown')
HISTLIST.append('bbH250_CMS_scale_jUp')
HISTLIST.append('bbH250_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH250_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH250_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH250_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH300')
HISTLIST.append('bbH300_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH300_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH300_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH300_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH300_CMS_scale_jDown')
HISTLIST.append('bbH300_CMS_scale_jUp')
HISTLIST.append('bbH300_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH300_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH300_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH300_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH350')
HISTLIST.append('bbH350_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH350_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH350_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH350_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH350_CMS_scale_jDown')
HISTLIST.append('bbH350_CMS_scale_jUp')
HISTLIST.append('bbH350_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH350_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH350_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH350_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH400')
HISTLIST.append('bbH400_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH400_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH400_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH400_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH400_CMS_scale_jDown')
HISTLIST.append('bbH400_CMS_scale_jUp')
HISTLIST.append('bbH400_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH400_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH400_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH400_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH450')
HISTLIST.append('bbH450_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH450_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH450_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH450_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH450_CMS_scale_jDown')
HISTLIST.append('bbH450_CMS_scale_jUp')
HISTLIST.append('bbH450_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH450_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH450_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH450_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH500')
HISTLIST.append('bbH500_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH500_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH500_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH500_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH500_CMS_scale_jDown')
HISTLIST.append('bbH500_CMS_scale_jUp')
HISTLIST.append('bbH500_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH500_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH500_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH500_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH600')
HISTLIST.append('bbH600_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH600_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH600_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH600_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH600_CMS_scale_jDown')
HISTLIST.append('bbH600_CMS_scale_jUp')
HISTLIST.append('bbH600_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH600_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH600_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH600_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH700')
HISTLIST.append('bbH700_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH700_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH700_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH700_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH700_CMS_scale_jDown')
HISTLIST.append('bbH700_CMS_scale_jUp')
HISTLIST.append('bbH700_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH700_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH700_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH700_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH80')
HISTLIST.append('bbH800')
HISTLIST.append('bbH800_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH800_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH800_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH800_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH800_CMS_scale_jDown')
HISTLIST.append('bbH800_CMS_scale_jUp')
HISTLIST.append('bbH800_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH800_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH800_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH800_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH80_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH80_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH80_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH80_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH80_CMS_scale_jDown')
HISTLIST.append('bbH80_CMS_scale_jUp')
HISTLIST.append('bbH80_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH80_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH80_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH80_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH90')
HISTLIST.append('bbH900')
HISTLIST.append('bbH900_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH900_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH900_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH900_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH900_CMS_scale_jDown')
HISTLIST.append('bbH900_CMS_scale_jUp')
HISTLIST.append('bbH900_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH900_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH900_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH900_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('bbH90_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('bbH90_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('bbH90_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('bbH90_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('bbH90_CMS_scale_jDown')
HISTLIST.append('bbH90_CMS_scale_jUp')
HISTLIST.append('bbH90_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('bbH90_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('bbH90_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('bbH90_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('data_obs')
HISTLIST.append('ggH100')
HISTLIST.append('ggH1000')
HISTLIST.append('ggH1000_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH1000_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH1000_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH1000_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH1000_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH1000_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH1000_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH1000_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH1000_CMS_scale_jDown')
HISTLIST.append('ggH1000_CMS_scale_jUp')
HISTLIST.append('ggH1000_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH1000_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH1000_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH1000_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH100_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH100_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH100_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH100_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH100_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH100_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH100_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH100_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH100_CMS_scale_jDown')
HISTLIST.append('ggH100_CMS_scale_jUp')
HISTLIST.append('ggH100_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH100_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH100_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH100_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH110')
HISTLIST.append('ggH110_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH110_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH110_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH110_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH110_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH110_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH110_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH110_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH110_CMS_scale_jDown')
HISTLIST.append('ggH110_CMS_scale_jUp')
HISTLIST.append('ggH110_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH110_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH110_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH110_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH120')
HISTLIST.append('ggH120_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH120_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH120_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH120_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH120_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH120_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH120_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH120_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH120_CMS_scale_jDown')
HISTLIST.append('ggH120_CMS_scale_jUp')
HISTLIST.append('ggH120_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH120_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH120_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH120_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH130')
HISTLIST.append('ggH130_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH130_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH130_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH130_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH130_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH130_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH130_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH130_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH130_CMS_scale_jDown')
HISTLIST.append('ggH130_CMS_scale_jUp')
HISTLIST.append('ggH130_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH130_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH130_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH130_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH140')
HISTLIST.append('ggH140_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH140_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH140_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH140_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH140_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH140_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH140_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH140_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH140_CMS_scale_jDown')
HISTLIST.append('ggH140_CMS_scale_jUp')
HISTLIST.append('ggH140_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH140_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH140_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH140_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH160')
HISTLIST.append('ggH160_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH160_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH160_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH160_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH160_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH160_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH160_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH160_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH160_CMS_scale_jDown')
HISTLIST.append('ggH160_CMS_scale_jUp')
HISTLIST.append('ggH160_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH160_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH160_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH160_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH180')
HISTLIST.append('ggH180_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH180_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH180_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH180_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH180_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH180_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH180_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH180_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH180_CMS_scale_jDown')
HISTLIST.append('ggH180_CMS_scale_jUp')
HISTLIST.append('ggH180_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH180_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH180_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH180_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH200')
HISTLIST.append('ggH200_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH200_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH200_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH200_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH200_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH200_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH200_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH200_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH200_CMS_scale_jDown')
HISTLIST.append('ggH200_CMS_scale_jUp')
HISTLIST.append('ggH200_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH200_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH200_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH200_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH250')
HISTLIST.append('ggH250_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH250_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH250_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH250_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH250_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH250_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH250_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH250_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH250_CMS_scale_jDown')
HISTLIST.append('ggH250_CMS_scale_jUp')
HISTLIST.append('ggH250_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH250_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH250_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH250_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH300')
HISTLIST.append('ggH300_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH300_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH300_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH300_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH300_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH300_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH300_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH300_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH300_CMS_scale_jDown')
HISTLIST.append('ggH300_CMS_scale_jUp')
HISTLIST.append('ggH300_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH300_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH300_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH300_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH350')
HISTLIST.append('ggH350_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH350_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH350_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH350_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH350_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH350_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH350_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH350_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH350_CMS_scale_jDown')
HISTLIST.append('ggH350_CMS_scale_jUp')
HISTLIST.append('ggH350_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH350_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH350_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH350_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH400')
HISTLIST.append('ggH400_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH400_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH400_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH400_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH400_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH400_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH400_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH400_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH400_CMS_scale_jDown')
HISTLIST.append('ggH400_CMS_scale_jUp')
HISTLIST.append('ggH400_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH400_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH400_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH400_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH450')
HISTLIST.append('ggH450_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH450_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH450_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH450_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH450_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH450_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH450_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH450_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH450_CMS_scale_jDown')
HISTLIST.append('ggH450_CMS_scale_jUp')
HISTLIST.append('ggH450_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH450_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH450_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH450_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH500')
HISTLIST.append('ggH500_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH500_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH500_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH500_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH500_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH500_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH500_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH500_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH500_CMS_scale_jDown')
HISTLIST.append('ggH500_CMS_scale_jUp')
HISTLIST.append('ggH500_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH500_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH500_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH500_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH600')
HISTLIST.append('ggH600_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH600_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH600_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH600_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH600_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH600_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH600_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH600_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH600_CMS_scale_jDown')
HISTLIST.append('ggH600_CMS_scale_jUp')
HISTLIST.append('ggH600_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH600_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH600_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH600_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH700')
HISTLIST.append('ggH700_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH700_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH700_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH700_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH700_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH700_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH700_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH700_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH700_CMS_scale_jDown')
HISTLIST.append('ggH700_CMS_scale_jUp')
HISTLIST.append('ggH700_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH700_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH700_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH700_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH80')
HISTLIST.append('ggH800')
HISTLIST.append('ggH800_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH800_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH800_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH800_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH800_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH800_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH800_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH800_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH800_CMS_scale_jDown')
HISTLIST.append('ggH800_CMS_scale_jUp')
HISTLIST.append('ggH800_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH800_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH800_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH800_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH80_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH80_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH80_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH80_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH80_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH80_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH80_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH80_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH80_CMS_scale_jDown')
HISTLIST.append('ggH80_CMS_scale_jUp')
HISTLIST.append('ggH80_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH80_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH80_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH80_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH90')
HISTLIST.append('ggH900')
HISTLIST.append('ggH900_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH900_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH900_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH900_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH900_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH900_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH900_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH900_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH900_CMS_scale_jDown')
HISTLIST.append('ggH900_CMS_scale_jUp')
HISTLIST.append('ggH900_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH900_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH900_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH900_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH90_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH90_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH90_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH90_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH90_CMS_htt_higgsPtReweight_8TeVDown')
HISTLIST.append('ggH90_CMS_htt_higgsPtReweight_8TeVUp')
HISTLIST.append('ggH90_CMS_htt_higgsPtReweight_scale_8TeVDown')
HISTLIST.append('ggH90_CMS_htt_higgsPtReweight_scale_8TeVUp')
HISTLIST.append('ggH90_CMS_scale_jDown')
HISTLIST.append('ggH90_CMS_scale_jUp')
HISTLIST.append('ggH90_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH90_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH90_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH90_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('ggH_SM125')
HISTLIST.append('ggH_SM125_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('ggH_SM125_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('ggH_SM125_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('ggH_SM125_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('ggH_SM125_CMS_htt_higgsPtReweightSM_8TeVDown')
HISTLIST.append('ggH_SM125_CMS_htt_higgsPtReweightSM_8TeVUp')
HISTLIST.append('ggH_SM125_CMS_scale_jDown')
HISTLIST.append('ggH_SM125_CMS_scale_jUp')
HISTLIST.append('ggH_SM125_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('ggH_SM125_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('ggH_SM125_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('ggH_SM125_CMS_scale_t_mutau_8TeVUp')
HISTLIST.append('qqH_SM125')
HISTLIST.append('qqH_SM125_CMS_eff_t_mssmHigh_etau_8TeVDown')
HISTLIST.append('qqH_SM125_CMS_eff_t_mssmHigh_etau_8TeVUp')
HISTLIST.append('qqH_SM125_CMS_eff_t_mssmHigh_mutau_8TeVDown')
HISTLIST.append('qqH_SM125_CMS_eff_t_mssmHigh_mutau_8TeVUp')
HISTLIST.append('qqH_SM125_CMS_scale_jDown')
HISTLIST.append('qqH_SM125_CMS_scale_jUp')
HISTLIST.append('qqH_SM125_CMS_scale_t_etau_8TeVDown')
HISTLIST.append('qqH_SM125_CMS_scale_t_etau_8TeVUp')
HISTLIST.append('qqH_SM125_CMS_scale_t_mutau_8TeVDown')
HISTLIST.append('qqH_SM125_CMS_scale_t_mutau_8TeVUp')