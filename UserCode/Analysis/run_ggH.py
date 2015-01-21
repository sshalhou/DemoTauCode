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




chain = TChain('*/FlatTuple')

listOfFiles = []

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_10_1_dF1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_11_1_YWC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_12_1_nD1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_13_1_x5S_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_14_1_Ll2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_15_1_iNe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_16_1_IaA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_17_1_qBz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_18_1_VGJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_19_1_ZiH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_1_1_reU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_20_1_WLy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_21_1_9yD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_22_1_f1b_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_23_1_DZc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_24_1_c21_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_25_1_WHg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_26_1_yxb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_2_1_UxJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_3_1_NlW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_4_1_NlY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_5_1_YZd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_6_1_9dK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_7_1_Yz8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_8_1_FDo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM1000_FLATv9Xntup/FlatTuple_9_1_ADa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_10_1_7PQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_11_1_YaT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_12_1_Cxi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_13_1_gAr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_14_1_whs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_15_1_VRb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_16_1_vf2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_17_1_k0O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_18_1_pJF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_19_1_0FU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_1_1_a9O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_20_1_j8w_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_21_1_5xk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_22_1_nqB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_23_1_Y71_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_24_1_FNV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_25_1_fgw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_26_1_oMa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_2_1_8Ww_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_3_1_Bjp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_4_1_U6S_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_5_1_lqO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_6_1_gkF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_7_1_UNE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_8_1_He3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM100_FLATv9Xntup/FlatTuple_9_1_TPs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_10_1_Tkr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_11_1_JfA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_12_1_K48_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_13_1_5Sy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_14_1_mYR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_15_1_i1n_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_16_1_IPY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_17_1_J5R_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_18_1_5iY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_19_1_mFi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_1_1_igq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_20_1_edA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_21_1_yny_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_22_1_t2s_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_23_1_HfS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_24_1_fac_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_25_1_4HJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_26_1_q4j_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_2_1_zGs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_3_1_0Yc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_4_1_AUm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_5_1_zPA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_6_1_baQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_7_1_sao_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_8_1_P65_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM110_FLATv9Xntup/FlatTuple_9_1_ojV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_10_1_nuW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_11_1_G6m_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_12_1_HBX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_13_1_pmI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_14_1_7uP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_15_1_JCp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_16_1_GTm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_17_1_Wci_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_18_1_7Yg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_19_1_1ZE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_1_1_Tjv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_20_1_P75_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_21_1_fy7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_22_1_rVL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_23_1_3yn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_24_1_Fy7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_25_1_0Z0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_26_1_2L8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_2_1_ahw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_3_1_ZPq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_4_1_Mqf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_5_1_qfJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_6_1_SIl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_7_1_EXI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_8_1_UYH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM120_FLATv9Xntup/FlatTuple_9_1_pQL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_10_1_195_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_11_1_5be_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_12_1_VDv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_13_1_9tb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_14_1_pHr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_15_1_rWM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_16_1_NbZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_17_1_Cxy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_18_1_iOp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_19_1_8cU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_1_1_Foj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_20_1_Mjx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_21_1_SHG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_22_1_7Nq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_23_1_yyp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_24_1_gGY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_25_1_NVu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_26_1_ZKC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_2_1_Lfa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_3_1_7Gh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_4_1_IQ1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_5_1_SIy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_6_1_TwY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_7_1_GzP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_8_1_8wg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM130_FLATv9Xntup/FlatTuple_9_1_lRg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_10_1_nMY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_11_1_ABH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_12_1_Yf9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_13_1_91c_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_14_1_20j_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_15_1_AyB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_16_1_U37_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_17_1_zrX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_18_1_Fqm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_19_1_hAY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_1_1_VGh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_20_1_B08_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_21_1_A3i_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_22_1_WIG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_23_1_E2b_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_24_1_I4J_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_25_1_xny_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_26_1_mfd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_2_1_5O3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_3_1_wrC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_4_1_FjX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_5_1_LaT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_6_1_ui1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_7_1_SsE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_8_1_mQ3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM140_FLATv9Xntup/FlatTuple_9_1_D6z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_10_1_KuU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_11_1_lQ6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_12_1_6EU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_13_1_4cf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_14_1_0P6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_15_1_INK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_16_1_w4X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_17_1_XgV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_18_1_Z6x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_19_1_FOY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_1_1_XIu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_20_1_Oba_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_21_1_jpD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_22_1_Mys_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_23_1_PoK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_24_1_qdb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_25_1_HtN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_26_1_JdC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_2_1_UBC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_3_1_kER_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_4_1_dPL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_5_1_pov_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_6_1_urI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_7_1_mWn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_8_1_1Iw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM160_FLATv9Xntup/FlatTuple_9_1_Usx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_10_1_rQA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_11_1_icR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_12_1_6xJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_13_1_dN6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_14_1_RjK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_15_1_nrw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_16_1_Uu0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_17_1_DzE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_18_1_xWm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_19_1_8c0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_1_1_gTV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_20_1_b4S_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_21_1_2fM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_22_1_tZJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_23_1_iCO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_24_1_Ceg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_25_1_ZhX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_26_1_PyM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_2_1_Lit_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_3_1_00A_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_4_1_2xp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_5_1_3Zj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_6_1_PfS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_7_1_OqD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_8_1_8nJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM180_FLATv9Xntup/FlatTuple_9_1_piR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_10_1_zMF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_11_1_Iml_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_12_1_B9I_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_13_1_O0P_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_14_1_Itz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_15_1_xmy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_16_1_Dpk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_17_1_kjC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_18_1_YJu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_19_1_76f_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_1_1_xnG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_20_1_0lD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_21_1_NOA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_22_1_2JF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_23_1_W6a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_24_1_Pj3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_25_1_nw4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_26_1_avY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_2_1_wW4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_3_1_mex_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_4_1_7w9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_5_1_SEx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_6_1_DSn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_7_1_Lbf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_8_1_ikW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM200_FLATv9Xntup/FlatTuple_9_1_xhU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_10_1_Bxd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_11_1_xUh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_12_1_Xq4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_13_1_W4c_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_14_1_wl6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_15_1_T3w_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_16_1_hGg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_17_1_jGC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_18_1_Wg2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_19_1_GkR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_1_1_reV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_20_1_ZCR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_21_1_otU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_22_1_nNH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_23_1_Wpx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_24_1_u5M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_25_1_bu0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_2_1_fgd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_3_1_JfT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_4_1_IH6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_5_1_EPt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_6_1_hO5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_7_1_7SQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_8_1_y85_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM250_FLATv9Xntup/FlatTuple_9_1_89w_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_10_1_Sp5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_11_1_gwd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_12_1_iiP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_13_1_uAG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_14_1_Ail_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_15_1_8c9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_16_1_duH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_17_1_eFB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_18_1_khA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_19_1_g3O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_1_1_3Ye_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_20_1_F7C_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_21_1_FZk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_22_1_LnY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_23_1_ahS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_24_1_l5N_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_25_1_Fco_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_26_1_a9d_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_2_1_ZZQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_3_1_msm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_4_1_kih_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_5_1_yux_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_6_1_55n_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_7_1_uL5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_8_1_Xyl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM300_FLATv9Xntup/FlatTuple_9_1_MIl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_10_1_Qkt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_11_1_giB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_12_1_gJb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_13_1_qpz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_14_1_IbZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_15_1_1Sb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_16_1_hMQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_17_1_zqF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_18_1_LLo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_19_1_YQt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_1_1_sPC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_20_1_L7w_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_21_1_kbE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_22_1_stl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_23_1_Spv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_24_1_Bzi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_25_1_wi7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_26_1_Kg7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_2_1_IYz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_3_1_n1v_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_4_1_4gT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_5_1_sVG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_6_1_HIW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_7_1_ilP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_8_1_Q2y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM350_FLATv9Xntup/FlatTuple_9_1_zCx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_10_1_4pC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_11_1_hGX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_12_1_gf5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_13_1_UfV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_14_1_6uT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_15_1_uGD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_16_1_xX6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_17_1_9iJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_18_1_oN6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_19_1_4Bt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_1_1_ZaV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_20_1_mR6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_21_1_RTE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_22_1_d63_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_23_1_F5M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_24_1_vEw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_25_1_BYM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_26_1_DX2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_2_1_Whn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_3_1_i3a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_4_1_8Z5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_5_1_L85_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_6_1_6jn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_7_1_IX7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_8_1_STM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM400_FLATv9Xntup/FlatTuple_9_1_d2l_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_10_1_Emw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_11_1_JIe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_12_1_3oG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_13_1_Tjf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_14_1_iR4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_15_1_OyZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_16_1_j2l_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_17_1_BAW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_18_1_kOh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_19_1_tpb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_1_1_wMX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_20_1_tPp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_21_1_GUA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_22_1_Sym_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_23_1_dIf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_24_1_EPF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_25_1_yej_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_26_1_FGD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_2_1_HiJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_3_1_DE2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_4_1_twy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_5_1_qm4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_6_1_q8B_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_7_1_vmj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_8_1_Hm3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM450_FLATv9Xntup/FlatTuple_9_1_JOZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_10_1_mub_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_11_1_4ks_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_12_1_9So_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_13_1_v0D_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_14_1_Tdz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_15_1_rcH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_16_1_fn5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_17_1_3ev_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_18_1_3qc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_19_1_Dqe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_1_1_DcJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_20_1_Pda_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_21_1_fjU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_22_1_2Dx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_23_1_TqH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_24_1_Ttn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_25_1_4A4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_26_1_8cT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_2_1_TMe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_3_1_uUW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_4_1_hox_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_5_1_4IA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_6_1_mww_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_7_1_q9L_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_8_1_GGe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM500_FLATv9Xntup/FlatTuple_9_1_QEf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_10_1_cs3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_11_1_dBU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_12_1_suh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_13_1_PoC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_14_1_C8U_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_15_1_MrX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_16_1_qOo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_17_1_cyw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_18_1_r4u_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_19_1_RDm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_1_1_NCf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_20_1_V6O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_21_1_Fvb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_22_1_QO4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_23_1_okB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_24_1_S4g_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_25_1_6N5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_26_1_ynx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_2_1_8Ys_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_3_1_nBI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_4_1_Ism_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_5_1_Foe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_6_1_9rC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_7_1_SBz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_8_1_bcl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM600_FLATv9Xntup/FlatTuple_9_1_Vaj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_10_1_jzI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_11_1_PSx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_12_1_jCT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_13_1_gbe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_14_1_iFq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_15_1_V3x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_16_1_lVv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_17_1_rHH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_18_1_gU9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_19_1_55K_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_1_1_3UE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_20_1_209_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_21_1_pv3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_22_1_hRO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_23_1_NfA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_24_1_OKh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_25_1_9hx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_26_1_exs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_2_1_3zv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_3_1_IQp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_4_1_6RG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_5_1_LwJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_6_1_vDR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_7_1_4gF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_8_1_nR1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM700_FLATv9Xntup/FlatTuple_9_1_afo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_10_1_RN8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_11_1_8V5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_12_1_Bcc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_13_1_6OH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_14_1_A9a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_15_1_hIv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_16_1_ppD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_17_1_TJM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_18_1_36C_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_19_1_2GH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_1_1_AIW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_20_1_6QG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_21_1_Bif_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_22_1_qrV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_23_1_Jbf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_24_1_Ijp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_25_1_5iL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_26_1_Bx1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_2_1_w0m_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_3_1_NP5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_4_1_ibq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_5_1_ieL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_6_1_uOw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_7_1_SLy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_8_1_BEs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM800_FLATv9Xntup/FlatTuple_9_1_Zcv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_10_1_XLl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_11_1_Oco_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_12_1_m1L_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_13_1_yvq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_14_1_xni_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_15_1_hON_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_16_1_yUZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_17_1_8dA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_18_1_gFL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_19_1_ZUl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_1_1_e94_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_20_1_HkM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_21_1_A3w_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_22_1_ZJ0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_23_1_NK1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_24_1_eV5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_25_1_dYT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_26_1_fps_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_2_1_eqs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_3_1_Z4d_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_4_1_Uu6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_5_1_iYh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_6_1_TFi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_7_1_GXk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_8_1_zzf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM80_FLATv9Xntup/FlatTuple_9_1_LNl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_10_1_v0D_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_11_1_I1g_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_12_1_GIw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_13_1_3kZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_14_1_p66_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_15_1_cso_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_16_1_MvW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_17_1_qXr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_18_1_drO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_19_1_2zn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_1_1_HQJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_20_1_keS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_21_1_PRo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_22_1_V5N_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_23_1_0wm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_24_1_m8t_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_25_1_Qct_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_26_1_Ox5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_2_1_2UU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_3_1_FEs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_4_1_l0j_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_5_1_b73_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_6_1_ab6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_7_1_API_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_8_1_Qwo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM900_FLATv9Xntup/FlatTuple_9_1_Lym_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_10_1_96n_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_11_1_ZRT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_12_1_ey8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_13_1_eKL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_14_1_ne9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_15_1_BBB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_16_1_13m_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_17_1_t4D_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_18_1_oIp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_19_1_Ue3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_1_1_o4g_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_20_1_oyT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_21_1_IZ0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_22_1_30W_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_23_1_aX5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_24_1_e6m_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_25_1_Dy5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_26_1_0x6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_2_1_USw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_3_1_0Bj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_4_1_m3R_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_5_1_56Z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_6_1_Q8O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_7_1_aBz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_8_1_tjN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/SUSYGluGluToHToTauTauM90_FLATv9Xntup/FlatTuple_9_1_6II_skimmed.root')


for afile in listOfFiles:
	chain.AddFile(afile,0,'TauEsNominal/FlatTuple')
	chain.AddFile(afile,0,'TauEsUp/FlatTuple')
	chain.AddFile(afile,0,'TauEsDown/FlatTuple')




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


maxEntries = chain.GetEntries()


if SmallRun is True:
	maxEntries = 1000

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
				if passesDefaultSelectionETau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesSUSYGluGluExtraSelectionETau(chain,index) is False:
					passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				if passesDefaultSelectionMuTau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesSUSYGluGluExtraSelectionMuTau(chain,index) is False:
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
					maxPairTypeAndIndex.append(muTauClassification(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(chain.NAMEVAR)
					maxPairTypeAndIndex.append(muTauClassificationJECDOWN(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(muTauClassificationJECUP(chain, maxPairTypeAndIndex[0]))
				if maxPairTypeAndIndex[1] == 'eleTau':
					maxPairTypeAndIndex.append(eTauClassification(chain, maxPairTypeAndIndex[0]))
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
				finalWt = signalSUSYweightGluGlu(chain, maxPairTypeAndIndex, Verbose)
				###############
				# the above weight contains nominal pt re-weigh
				# also pass it sep. so it can be stripped off

				nominalPtReweight = higgsPtReWeight(chain, maxPairTypeAndIndex, 'USENEW', 'NOMINAL')

				highPtTauWtSYS =  highPtTauSYS(chain, maxPairTypeAndIndex)
				higgsPtWeightSYSdict = {}
				higgsPtWeightSYS(chain, maxPairTypeAndIndex,higgsPtWeightSYSdict)
				SAMPLE_ADD = getSAMPLE_ADD(sampleName)
				assert(len(SAMPLE_ADD)>0), " Assert : unknown sample "
				#print maxPairTypeAndIndex
				#print higgsPtWeightSYSdict
				FillSUSYGluGlu(maxPairTypeAndIndex,SAMPLE_ADD,
					finalWt,highPtTauWtSYS,
					histogram_dict,
					higgsPtWeightSYSdict,
					eventVariables['SVFitMass'],nominalPtReweight)


######################
# save filled histograms

WriteEverything()
writeCompFile()
