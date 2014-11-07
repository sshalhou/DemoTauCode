import time
import sys
import os



from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TApplication,TTreeCache


################
# some global settings

UseNewTriggers = False
OnlyCheckEmbeddedTriggers = False

Verbose = False
SmallRun = False

PrintEvents = False
check_events = []
#check_events.append('1-287-187567')

print "loading files ..."

chain = TChain('*/FlatTuple')

listOfFiles = []

############
# DATA

listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNA_V7FlatTupleEx/FlatTuple_1_1_I5s.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNA_V7FlatTupleEx/FlatTuple_2_1_emp.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_V7FlatTupleEx/FlatTuple_1_1_KIQ.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_V7FlatTupleEx/FlatTuple_2_1_0S8.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_V7FlatTupleEx/FlatTuple_3_1_ROv.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_V7FlatTupleEx/FlatTuple_4_1_kxi.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_V7FlatTupleEx/FlatTuple_5_1_rtZ.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_V7FlatTupleEx/FlatTuple_6_1_MAi.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_1_1_tJt.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_2_1_fvG.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_3_1_PuD.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_4_1_Qcy.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_5_1_9SD.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_6_1_l5M.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_7_1_tGi.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_8_1_E1H.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_9_1_6jK.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_1_1_Tj1.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_2_1_JIl.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_3_1_tTy.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_4_1_Yg5.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_5_1_2ss.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_6_1_JRW.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_7_1_RoG.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_8_1_jWE.root')
listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_RecoveredJobs.root')

###########
# wjets


listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/wjets_skimmed/FlatTuple_SZS_W1jetsLNuV19v1_v6ntup_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/wjets_skimmed/FlatTuple_SZS_W1jetsLNuV7Av1_v6ntup_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/wjets_skimmed/FlatTuple_SZS_W2jetsLNuV19v1_v6ntup_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/wjets_skimmed/FlatTuple_SZS_W2jetsLNuV7Av1_v6ntup_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/wjets_skimmed/FlatTuple_SZS_W3jetsLNuV19v1_v6ntup_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/wjets_skimmed/FlatTuple_SZS_W3jetsLNuV7Av1_v6ntup_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/wjets_skimmed/FlatTuple_SZS_W4jetsLNuV1_v6ntup_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/wjets_skimmed/FlatTuple_SZS_WjetsLNuV1_v6ntup_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/wjets_skimmed/FlatTuple_SZS_WjetsLNuV2_v6ntup_skimmed.root')


###########
# DY


listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_10_1_2Ih_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_11_1_5YE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_12_1_tLc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_13_1_2wW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_14_1_4b6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_15_1_kx8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_16_1_UI2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_17_1_KHg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_18_1_hKK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_19_1_XMj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_1_1_blg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_2_1_XEG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_3_1_O9X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_4_1_4xG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_5_1_rCz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_6_1_XMN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_7_1_I78_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_8_1_pk7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY1JetsToLL_V7FlatTupleEx/FlatTuple_9_1_8X3_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_10_1_9c7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_11_1_z0I_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_12_1_ZGr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_13_1_XGW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_14_1_FWE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_15_1_byZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_16_1_tUv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_17_1_swU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_18_1_NUu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_1_1_ClI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_2_1_G54_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_3_1_tPo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_4_1_ley_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_5_1_bfs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_6_1_ox0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_7_1_INJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_8_1_QtR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY2JetsToLL_V7FlatTupleEx/FlatTuple_9_1_34f_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_10_1_ge0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_11_1_sgb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_12_1_qx4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_13_1_IOH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_14_1_vEj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_15_1_YGT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_16_1_62i_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_1_1_0Xm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_2_1_7oh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_3_1_8z5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_4_1_iAU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_5_1_iFj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_6_1_LUk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_7_1_jUe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_8_1_WlK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY3JetsToLL_V7FlatTupleEx/FlatTuple_9_1_Z5R_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_10_1_NgC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_11_1_T5r_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_12_1_7ed_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_13_1_BgD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_14_1_rDN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_15_1_U5j_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_16_1_tY0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_1_1_qtj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_2_1_Wo3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_3_1_fuh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_4_1_3ph_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_5_1_3nZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_6_1_sMS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_7_1_BnP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_8_1_8k8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DY4JetsToLL_V7FlatTupleEx/FlatTuple_9_1_Kqb_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_10_1_0dZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_11_1_Fy8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_12_1_Cyl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_13_1_gHI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_14_1_7JL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_15_1_mSd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_16_1_STt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_17_1_aiY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_18_1_nUb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_1_1_lEU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_2_1_nrG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_3_1_LcN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_4_1_LO1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_5_1_GQM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_6_1_wqp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_7_1_ubt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_8_1_awC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/dy_skimmed/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_9_1_reh_skimmed.root')



##########
# tt

listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_10_1_a3z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_11_1_xHU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_12_1_t6m_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_13_1_a5v_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_14_1_HYC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_15_1_MkF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_16_1_j8s_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_17_1_anL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_18_1_UuA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_19_1_TZ5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_1_1_4Ih_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_20_1_g3o_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_21_1_px3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_22_1_gur_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_2_1_nUp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_3_1_5bg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_4_1_scU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_5_1_p9q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_6_1_9lb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_7_1_QM6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_8_1_T94_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_9_1_7QY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_10_1_pjM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_11_1_85G_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_12_1_hzL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_13_1_Ziy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_14_1_WGW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_15_1_ync_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_16_1_77T_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_17_1_KvA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_18_1_1n9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_19_1_9rL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_1_1_ZRE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_2_1_8G7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_3_1_x8o_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_4_1_0oK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_5_1_Ofm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_6_1_tr1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_7_1_5KO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_8_1_2eX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_9_1_97A_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_10_1_vL6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_11_1_QHF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_12_1_SIh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_13_1_01R_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_14_1_Y6O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_15_1_bP2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_16_1_tlP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_17_1_cc5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_18_1_fhm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_19_1_SNS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_1_1_Z4r_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_20_1_1i9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_21_1_13s_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_22_1_V2T_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_23_1_p5o_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_2_1_RA8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_3_1_APi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_4_1_1he_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_5_1_nRZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_6_1_cq6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_7_1_6lf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_8_1_ndY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/tt_MC_skimmed/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_9_1_hXo_skimmed.root')

#############
# single t

listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/T_tWchannelDR_V6FlatTuple/FlatTuple_10_1_anP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/T_tWchannelDR_V6FlatTuple/FlatTuple_11_1_y8K_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/T_tWchannelDR_V6FlatTuple/FlatTuple_12_1_cbh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/T_tWchannelDR_V6FlatTuple/FlatTuple_13_1_AUB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/T_tWchannelDR_V6FlatTuple/FlatTuple_14_1_XPW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/T_tWchannelDR_V6FlatTuple/FlatTuple_15_1_8XI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/T_tWchannelDR_V6FlatTuple/FlatTuple_16_1_9Cp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/T_tWchannelDR_V6FlatTuple/FlatTuple_1_1_02Z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/T_tWchannelDR_V6FlatTuple/FlatTuple_2_1_TkZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/T_tWchannelDR_V6FlatTuple/FlatTuple_3_1_Gxa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/T_tWchannelDR_V6FlatTuple/FlatTuple_4_1_Tm1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/T_tWchannelDR_V6FlatTuple/FlatTuple_5_1_2Ny_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/T_tWchannelDR_V6FlatTuple/FlatTuple_6_1_jhY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/T_tWchannelDR_V6FlatTuple/FlatTuple_7_1_b4K_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/T_tWchannelDR_V6FlatTuple/FlatTuple_8_1_MH2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/T_tWchannelDR_V6FlatTuple/FlatTuple_9_1_J5h_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_10_1_Rvw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_11_1_ywq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_12_1_zJM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_13_1_x5D_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_14_1_MBC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_15_1_UKz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_16_1_twl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_1_1_xAj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_2_1_DPy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_3_1_OA0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_4_1_Owt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_5_1_Mvc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_6_1_lwq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_7_1_ecE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_8_1_N6d_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/singleTop_skimmed/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_9_1_xDJ_skimmed.root')


###########
# vv

listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_10_1_SAl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_11_1_mxQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_12_1_0ic_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_13_1_hji_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_14_1_IIO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_15_1_3pv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_16_1_0zm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_1_1_y4A_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_2_1_YKa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_3_1_VuT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_4_1_gtZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_5_1_RMB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_6_1_PDH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_7_1_W3f_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_8_1_Dxs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_9_1_qLn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_10_1_syu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_11_1_dDq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_12_1_Whv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_13_1_Zae_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_14_1_0Hf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_15_1_nB5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_16_1_cfL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_1_1_OSm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_2_1_pWK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_3_1_c9j_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_4_1_HYx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_5_1_tf7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_6_1_is7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_7_1_1yC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_8_1_4o5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_9_1_x3G_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo3LNu_V6FlatTuple/FlatTuple_10_1_pHm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo3LNu_V6FlatTuple/FlatTuple_11_1_ZQH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo3LNu_V6FlatTuple/FlatTuple_12_1_ZXw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo3LNu_V6FlatTuple/FlatTuple_13_1_XGl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo3LNu_V6FlatTuple/FlatTuple_14_1_1zC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo3LNu_V6FlatTuple/FlatTuple_15_1_hOE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo3LNu_V6FlatTuple/FlatTuple_1_1_YxK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo3LNu_V6FlatTuple/FlatTuple_2_1_4uO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo3LNu_V6FlatTuple/FlatTuple_3_1_SXb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo3LNu_V6FlatTuple/FlatTuple_4_1_Voj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo3LNu_V6FlatTuple/FlatTuple_5_1_WZD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo3LNu_V6FlatTuple/FlatTuple_6_1_2gA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo3LNu_V6FlatTuple/FlatTuple_7_1_dFo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo3LNu_V6FlatTuple/FlatTuple_8_1_J04_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/WZJetsTo3LNu_V6FlatTuple/FlatTuple_9_1_0Ap_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_10_1_5Xm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_11_1_TDH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_12_1_gc8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_13_1_d9I_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_14_1_lQB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_15_1_Jmu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_16_1_7oC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_17_1_q9M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_18_1_ctm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_19_1_WZT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_1_1_f3k_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_20_1_7Q9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_21_1_J9t_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_2_1_HzX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_3_1_YrL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_4_1_krf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_5_1_Cjf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_6_1_BZP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_7_1_HZ0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_8_1_yON_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Nu_v8FLATtuple/FlatTuple_9_1_th4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_10_1_gV8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_11_1_YYF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_12_1_mXF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_13_1_FIQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_14_1_b9I_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_15_1_Oij_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_16_1_KVD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_1_1_80G_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_2_1_aBp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_3_1_7fL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_4_1_VGF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_5_1_edl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_6_1_TbJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_7_1_s8b_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_8_1_Mds_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_9_1_Hga_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo4L_V6FlatTuple/FlatTuple_10_1_eWh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo4L_V6FlatTuple/FlatTuple_11_1_J8X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo4L_V6FlatTuple/FlatTuple_12_1_HGJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo4L_V6FlatTuple/FlatTuple_13_1_XsZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo4L_V6FlatTuple/FlatTuple_14_1_aGK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo4L_V6FlatTuple/FlatTuple_15_1_xxG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo4L_V6FlatTuple/FlatTuple_16_1_jKf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo4L_V6FlatTuple/FlatTuple_1_1_18n_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo4L_V6FlatTuple/FlatTuple_2_1_9cY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo4L_V6FlatTuple/FlatTuple_3_1_LLc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo4L_V6FlatTuple/FlatTuple_4_1_ug4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo4L_V6FlatTuple/FlatTuple_5_1_gXo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo4L_V6FlatTuple/FlatTuple_6_1_NIN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo4L_V6FlatTuple/FlatTuple_7_1_Iab_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo4L_V6FlatTuple/FlatTuple_8_1_kZ7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/vv_skimmed/ZZJetsTo4L_V6FlatTuple/FlatTuple_9_1_LNX_skimmed.root')


#listOfFiles.append('./HOLDER/FlatTuple_SZS_W1jetsLNuV19v1_v6ntup.root')
#listOfFiles.append('./HOLDER/TTSemiFlatTuple_21_1_13s.root')
#listOfFiles.append('./HOLDER/WZJetsFlatTuple_3_1_c9j.root')
#listOfFiles.append('./HOLDER/DY2JetsFlatTuple_5_1_bfs.root')
#listOfFiles.append('./HOLDER/DYSpinOffFlatTuple_8_1_awC.root')
#listOfFiles.append('./HOLDER/DATAA_partial_FlatTuple_1_1_I5s.root')

for afile in listOfFiles:
	chain.AddFile(afile,0,'TauEsNominal/FlatTuple')
	#chain.AddFile(afile,0,'TauEsUp/FlatTuple')
	#chain.AddFile(afile,0,'TauEsDown/FlatTuple')


print "finished loading ttrees (es nominal only) from files ..."


theselector = "./scripts/FlatTreeSel.C+"
selector = TSelector.GetSelector(theselector)

chain.SetNotify(selector)
selector.Init(chain)
selector.Begin(chain)

####################################################################
# read in electronID, muonID, tauID, trigger, and event selections

from Configurations.python.electronID import *
from Configurations.python.muonID import *
from Configurations.python.tauID import *
from Configurations.python.triggerRequirements import *
from Configurations.python.eventRequirements import *
from Configurations.python.eventClassification import *
from Plotting.python.EventVariables import *
from Plotting.python.DataCardHistograms import *
from EventWeights.python.eventWeightFunctions import *
from Plotting.python.ComparisonPlots import *
from Configurations.python.SampleSpecificSelections import *
from Plotting.python.FillHistogramsBySample import *

print 'getting n events'

maxEntries = chain.GetEntries()



print 'starting loop ...'

if SmallRun is True:
	maxEntries = 15000

for entry in range(0,maxEntries):
		entryNumber = chain.GetEntryNumber(entry);
		localEntry = chain.LoadTree(entryNumber);
		if (localEntry >= 0):
			#print "NAMEVAR = ", chain.NAMEVAR
			if(entryNumber%1000==0):
				print 'processing entry ',entryNumber, 'of', maxEntries
				sys.stdout.flush()
			selector.Process(localEntry)
			passingETauIndices = []
			passingMuTauIndices = []
			maxPairTypeAndIndex = []

			#########################################################
			# get event ID

			eventID = [str(chain.run), str(chain.luminosityBlock), str(chain.event)]
			eventString = str(chain.run)+"-"+str(chain.luminosityBlock)+"-"+str(chain.event)
			sampleName =  str(chain.SampleName)



#########################################################
# loop over eTau pairs and store all that pass in list

			for index in range(0, chain.eT_correctedSVFitMass.size()):
				passesCuts = True
				if passesSameSignSelectionETau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				if passesSameSignSelectionMuTau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesCuts is True:
					passingMuTauIndices.append(index)



#########################################################
# if have multiple passing H candidates in the same event
# find the highest sumPt pair


			if (len(passingETauIndices) + len(passingMuTauIndices)) == 1:
				if len(passingETauIndices) == 1 :
					maxPairTypeAndIndex.append(passingETauIndices[0])
					maxPairTypeAndIndex.append('eleTau')
				elif len(passingMuTauIndices) == 1:
					maxPairTypeAndIndex.append(passingMuTauIndices[0])
					maxPairTypeAndIndex.append('muTau')
			if (len(passingETauIndices) + len(passingMuTauIndices)) > 1:
					getMaxPtPairIndex(chain, maxPairTypeAndIndex, passingMuTauIndices, passingETauIndices)

#########################################################
# now classify the event based on tauPt and nbtags

			if len(maxPairTypeAndIndex)	> 0:
				if maxPairTypeAndIndex[1] == 'muTau':
					maxPairTypeAndIndex.append(muTauClassification_forQCD(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(chain.NAMEVAR)
					maxPairTypeAndIndex.append(muTauClassificationJECDOWN(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(muTauClassificationJECUP(chain, maxPairTypeAndIndex[0]))
				if maxPairTypeAndIndex[1] == 'eleTau':
					maxPairTypeAndIndex.append(eTauClassification_forQCD(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(chain.NAMEVAR)
					maxPairTypeAndIndex.append(eTauClassificationJECDOWN(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(eTauClassificationJECUP(chain, maxPairTypeAndIndex[0]))
				if PrintEvents:
					print maxPairTypeAndIndex[1], maxPairTypeAndIndex[2],eventID[0]+"-"+eventID[1]+"-"+eventID[2]

##################################################################################
# get weights and fill histograms


			if len(maxPairTypeAndIndex)	> 0:
				eventVariables = {}
				fillVariables(chain,eventVariables,maxPairTypeAndIndex,Verbose)
				SAMPLE_ADD = getSAMPLE_ADD(sampleName)
				assert(len(SAMPLE_ADD)>0), " Assert : unknown sample "
				if SAMPLE_ADD == '_data_obs_':
					SAMPLE_ADD = '_QCD_'
					QCDShapeWeightsDownNominalUp_dict = {}
					QCDShapeWeightsDownNominalUp_dict['Nominal'] = 1.0
					QCDShapeWeightsDownNominalUp_dict['Up'] = 1.0
					QCDShapeWeightsDownNominalUp_dict['Down'] = 1.0
					FillQCDShapes(maxPairTypeAndIndex,SAMPLE_ADD,
										histogram_dict,
										QCDShapeWeightsDownNominalUp_dict,
										eventVariables['SVFitMass'])
				elif SAMPLE_ADD == '_DYTauPolOff_':
					classification = classifyZDecay_Final(chain,maxPairTypeAndIndex)
					print classification
					wt = 1.0
					if classification == '_ZTT_':
						wt = getWeightForTauPolOffDY_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					elif classification == '_ZL_':
						wt = getWeightForTauPolOffDY_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose)
						# contains an internal check for e->tau
						wt = wt * getFakeZeeWeight(chain,maxPairTypeAndIndex)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					elif classification == '_ZJ_':
						wt = getWeightForTauPolOffDY_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])

				elif (SAMPLE_ADD=='_DY1Jet_' or
					SAMPLE_ADD=='_DY2Jet_' or
					SAMPLE_ADD=='_DY3Jet_' or
					SAMPLE_ADD=='_DY4Jet_'):
					classification = classifyZDecay_Final(chain,maxPairTypeAndIndex)
					print classification
					wt = 1.0
					if classification == '_ZTT_':
						wt = getWeightForRegularDY_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					elif classification == '_ZL_':
						wt = getWeightForRegularDY_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose)
						# contains an internal check for e->tau
						wt = wt * getFakeZeeWeight(chain,maxPairTypeAndIndex)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					elif classification == '_ZJ_':
						wt = getWeightForRegularDY_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])

				elif (SAMPLE_ADD=='_ZZJetsTo4L_' or
					SAMPLE_ADD=='_ZZJetsTo2L2Nu_' or
					SAMPLE_ADD=='_ZZJetsTo2L2Q_' or
					SAMPLE_ADD=='_WWJetsTo2L2Nu_' or
					SAMPLE_ADD=='_WZJetsTo2L2Q_' or
					SAMPLE_ADD=='_WZJetsTo3LNu_' or
					SAMPLE_ADD=='_SingleTopBar_' or
					SAMPLE_ADD=='_SingleTop_'):
					classification = '_VV_'
					wt = 1.0
					wt = getWeightForVV(chain,maxPairTypeAndIndex,Verbose)
					Fill_VVandSingleTop(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])

				elif (SAMPLE_ADD=='_TTJetsFullLept_' or
					SAMPLE_ADD=='_TTJetsSemiLept_' or
					SAMPLE_ADD=='_TTJetsHadronic_'):
					classification = '_TT_'
					wt_dict = {}
					wt_dict['topPtDown'] = 1.0
					wt_dict['topPtNominal'] = 1.0
					wt_dict['topPtUp'] = 1.0

					getWeightForTTmc(chain,maxPairTypeAndIndex,wt_dict,Verbose)
					Fill_TTbarMC(maxPa



				elif (SAMPLE_ADD == '_WJetsToLNu_' or
					  SAMPLE_ADD == '_W1JetsToLNu_' or
					  SAMPLE_ADD == '_W2JetsToLNu_' or
					  SAMPLE_ADD == '_W3JetsToLNu_' or
					  SAMPLE_ADD == '_W4JetsToLNu_'):
					classification = '_W_'
					wt_dict = {}
					wt_dict['jetTauFakeDown'] = 1.0
					wt_dict['jetTauFakeNominal'] = 1.0
					wt_dict['jetTauFakeUp'] = 1.0
					getWeightForW(chain,maxPairTypeAndIndex,wt_dict,Verbose)
					Fill_WjetsMC(maxPairTypeAndIndex,classification,wt_dict,histogram_dict,eventVariables['SVFitMass'])




######################
# save filled histograms

WriteEverything()
writeCompFile()
