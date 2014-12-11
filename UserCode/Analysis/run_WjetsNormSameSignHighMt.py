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



###########
# wjets


listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_1_1_Ipi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_8_1_Fnm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_2_1_AWs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_9_1_oXw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_11_1_5JA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_6_1_K0k_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_12_1_lWI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_13_1_uwv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_17_1_vlG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_18_1_IMe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_14_1_PmE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_15_1_94X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_19_1_HPW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_20_1_QUJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_10_1_Qgq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_24_1_nax_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_5_1_GUA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_4_1_6aM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_21_1_yX5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_7_1_dFC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_22_1_MQS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_25_1_XED_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_30_1_prH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_27_1_pDT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_28_1_jgU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_3_1_gS9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_29_1_RWp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_23_1_Bc0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_26_1_AQc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV19v1_v9FlatTuple/FlatTuple_16_1_XZg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_6_1_OdT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_5_1_xFi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_2_1_oMH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_7_1_ISj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_9_1_MXi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_11_1_5LM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_13_1_RkZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_1_1_kj0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_15_1_fRF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_19_1_zvl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_16_1_Pyd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_12_1_aMs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_18_1_rHI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_14_1_vt6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_21_1_YZZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_27_1_zK4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_28_1_68U_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_25_1_IS1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_26_1_cje_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_29_1_SGs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_17_1_cFE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_20_1_C8u_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_24_1_tt9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_3_1_x6q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_4_1_vMn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_10_1_ZLQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_8_1_c5J_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_23_1_ZMB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W1jetsLNuV7Av1_v9FlatTuple/FlatTuple_22_1_LwU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_4_1_NFi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_1_1_1lf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_2_1_UId_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_6_1_Vgw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_9_1_ZUv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_12_1_ZA3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_10_1_gzy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_3_1_45l_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_13_1_B0u_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_16_1_KS5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_15_1_wtu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_17_1_kL8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_5_1_mdM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_19_1_jpA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_20_1_2YL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_18_1_OKv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_22_1_KMM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_23_1_AFb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_24_1_ivx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_7_1_EXQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_8_1_xoi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_11_1_9zY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_14_1_MAb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_27_1_5Gt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_28_1_KoD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_21_1_5UY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_26_1_E5p_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV19v1_v9FlatTuple/FlatTuple_25_1_o2f_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_6_1_OkK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_17_1_4tR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_10_1_NDS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_8_1_L25_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_11_1_PfS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_1_1_wWz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_3_1_Jpp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_9_1_Scm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_4_1_WJ1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_12_1_fvt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_13_1_CEN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_7_1_WRt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_15_1_pwA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_16_1_7YK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_19_1_PjS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_5_1_cgh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_2_1_HnS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_22_1_G9f_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_21_1_n9i_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_24_1_YMs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_18_1_z5O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_25_1_Yyu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_26_1_Ped_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_23_1_vdC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_14_1_1GU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_27_1_n3F_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W2jetsLNuV7Av1_v9FlatTuple/FlatTuple_20_1_VPh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_1_1_lwO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_7_1_LHF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_13_1_MlE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_2_1_tVC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_4_1_B7C_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_6_1_fPk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_8_1_pg8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_10_1_Azg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_14_1_810_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_19_1_l0o_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_15_1_jVC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_3_1_njL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_23_1_ArU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_11_1_0rz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_26_1_Kbh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_17_1_OHT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_16_1_ZS8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_5_1_g2X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_21_1_YQ5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_24_1_uOr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_25_1_DHt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_9_1_i0v_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_22_1_AjU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_18_1_0U1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_27_1_x6q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_12_1_SSG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_28_1_rq4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV19v1_v9FlatTuple/FlatTuple_20_1_r42_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_11_1_r8H_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_12_1_JBJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_1_1_2Wg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_2_1_d0X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_5_1_4Yz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_7_1_dwE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_15_1_QCr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_10_1_VLM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_8_1_7qS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_21_1_cEE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_20_1_cad_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_13_1_Wwf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_9_1_y2o_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_24_1_t0W_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_14_1_WqQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_22_1_mQ4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_19_1_nt9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_26_1_wR6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_23_1_F7p_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_27_1_1Ii_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_4_1_liM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_3_1_4Uh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_6_1_sAI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_17_1_yly_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_18_1_6Bp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_16_1_lzh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W3jetsLNuV7Av1_v9FlatTuple/FlatTuple_25_1_gX9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_6_1_r8q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_18_1_dcJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_11_1_vsM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_12_1_zwm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_17_1_GM0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_14_1_uIL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_8_1_9Oj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_13_1_2I0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_15_1_qzY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_10_1_veM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_9_1_Cg5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_27_1_w8m_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_16_1_pSb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_20_1_yFk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_28_1_Jjg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_24_1_skM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_21_1_SZI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_2_1_AHc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_3_1_zxx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_26_1_pRe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_22_1_CGL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_5_1_8wT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_4_1_QVq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_1_1_pYp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_7_1_CF1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_19_1_nop_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_23_1_NIk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/W4jetsLNuV1_v9FlatTuple/FlatTuple_25_1_7xC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_6_1_pr8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_5_1_PmD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_1_1_Wnh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_22_1_WBB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_2_1_QUG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_4_1_vJv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_3_1_NAu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_28_1_fhn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_7_1_uIN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_9_1_VvQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_12_1_lTg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_11_1_JCa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_10_1_Vtr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_13_1_uTn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_17_1_7tw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_19_1_s4E_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_20_1_yQ0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_21_1_w3h_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_16_1_fkz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_15_1_t3V_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_24_1_Bsc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_23_1_Fhc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_25_1_05Z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_14_1_cE7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_26_1_UrM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_27_1_aed_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_18_1_l1O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV1_v9FlatTuple/FlatTuple_8_1_yFw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_1_1_iJd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_7_1_aLy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_3_1_3rW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_4_1_RFo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_8_1_HNu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_12_1_wUH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_6_1_vPL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_11_1_B33_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_15_1_JPc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_13_1_gu9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_23_1_fqh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_9_1_cas_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_5_1_JtK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_14_1_KFc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_25_1_iu8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_16_1_YS8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_28_1_3uI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_10_1_xWa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_22_1_Y32_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_19_1_W9O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_27_1_PVO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_20_1_BBw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_21_1_yPn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_24_1_Iip_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_26_1_yHZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_18_1_8qY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_2_1_yCV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WjetsLNuV2_v9FlatTuple/FlatTuple_17_1_85i_skimmed.root')


############
# DATA



listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNA_V9FlatTuple/FlatTuple_1_1_ei7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNA_V9FlatTuple/FlatTuple_2_1_QEE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNB_V9FlatTuple/FlatTuple_6_1_1QH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNB_V9FlatTuple/FlatTuple_5_1_4HP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNB_V9FlatTuple/FlatTuple_3_1_LbR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNB_V9FlatTuple/FlatTuple_1_1_9HT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNB_V9FlatTuple/FlatTuple_2_1_asr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNB_V9FlatTuple/FlatTuple_4_1_7P3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNC_V9FlatTuple/FlatTuple_9_1_EDp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNC_V9FlatTuple/FlatTuple_3_1_qA7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNC_V9FlatTuple/FlatTuple_4_1_Z3v_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNC_V9FlatTuple/FlatTuple_7_1_1di_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNC_V9FlatTuple/FlatTuple_6_1_Clm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNC_V9FlatTuple/FlatTuple_2_1_DS6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNC_V9FlatTuple/FlatTuple_8_1_PU0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNC_V9FlatTuple/FlatTuple_1_1_bbG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUNC_V9FlatTuple/FlatTuple_5_1_nqe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUND_V9FlatTuple/FlatTuple_8_1_UVi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUND_V9FlatTuple/FlatTuple_1_1_4Mn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUND_V9FlatTuple/FlatTuple_3_1_MIU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUND_V9FlatTuple/FlatTuple_5_1_Pef_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUND_V9FlatTuple/FlatTuple_2_1_XZ1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUND_V9FlatTuple/FlatTuple_7_1_wi5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUND_V9FlatTuple/FlatTuple_6_1_9rP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DATA2012RUND_V9FlatTuple/FlatTuple_4_1_fLs_skimmed.root')


###########
# DY


listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_6_1_Jtt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_4_1_qvF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_10_1_C0Y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_17_1_BLT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_11_1_IWL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_13_1_lm4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_23_1_MhF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_16_1_Tdx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_18_1_x7K_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_20_1_kGp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_22_1_yeu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_25_1_q1R_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_27_1_05a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_28_1_agm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_7_1_NJr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_26_1_4LR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_12_1_ctf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_21_1_LRh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_19_1_Db2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_1_1_txh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_3_1_L8L_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_14_1_Siv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_2_1_fuj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_15_1_0SO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_8_1_AZl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_5_1_c7x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_9_1_FGV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DYJetsToLLTauSpin_v9FlatTuple/FlatTuple_24_1_YUp_skimmed.root')


listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_6_1_eFB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_18_1_WVe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_17_1_aFk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_1_1_Fqx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_2_1_WPw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_3_1_lfX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_5_1_Nq2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_10_1_CHd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_4_1_aQH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_14_1_hba_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_8_1_t47_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_12_1_0SN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_22_1_IXp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_19_1_C4R_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_15_1_Cp7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_16_1_tiB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_20_1_ONm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_13_1_FJu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_21_1_rFY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_28_1_t0h_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_27_1_Xb4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_11_1_MUC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_26_1_PNX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_9_1_7Xd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_23_1_es3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_24_1_emp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_25_1_O7Y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY1JetsToLL_v9FlatTuple/FlatTuple_7_1_6MQ_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_6_1_lzQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_12_1_rgP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_17_1_tHK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_7_1_d5b_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_2_1_iJ6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_5_1_0xT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_4_1_tGm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_11_1_9Tu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_14_1_EWn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_15_1_hDS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_16_1_QXH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_13_1_DzO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_9_1_s6S_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_22_1_yhK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_23_1_XEi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_24_1_Lq2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_3_1_2vn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_21_1_wLU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_20_1_Yok_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_8_1_SOP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_10_1_1aH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_27_1_UMS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_18_1_u60_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_26_1_gWn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_25_1_Adk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_19_1_tiK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY2JetsToLL_v9FlatTuple/FlatTuple_1_1_LGa_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_1_1_mIm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_12_1_Wuq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_2_1_ilX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_6_1_FCb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_9_1_ALZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_7_1_pOh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_14_1_LeV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_29_1_WQu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_28_1_vTy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_18_1_uYC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_17_1_tZG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_20_1_wBF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_23_1_QwU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_19_1_7tA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_25_1_Dzq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_15_1_Jsm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_13_1_8DS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_10_1_rtP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_16_1_RB7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_8_1_yUs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_27_1_qmi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_3_1_NER_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_22_1_0p0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_21_1_r2a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_5_1_eRF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_4_1_Ewq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_26_1_uiT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_11_1_ysi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY3JetsToLL_v9FlatTuple/FlatTuple_24_1_ZyM_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_3_1_zKq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_4_1_Lv2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_5_1_2sL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_6_1_WBL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_9_1_rW1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_2_1_1VC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_11_1_Q4c_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_8_1_UvM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_1_1_6Ah_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_7_1_f1V_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_13_1_YN0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_15_1_oqQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_10_1_lNI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_24_1_ftq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_14_1_MbZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_27_1_bcp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_22_1_g2k_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_17_1_YLh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_18_1_Yxk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_19_1_xMn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_12_1_0xo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_21_1_7ZP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_20_1_TNq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_23_1_Fdz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_25_1_tDF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_26_1_eVd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/DY4JetsToLL_v9FlatTuple/FlatTuple_16_1_oZK_skimmed.root')




##########
# tt


listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_5_1_0Q0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_6_1_uEu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_7_1_jYZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_1_1_lkn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_21_1_Att_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_3_1_h4q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_9_1_vfu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_14_1_Nlj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_15_1_Iww_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_19_1_zDQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_17_1_UlU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_16_1_JxJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_23_1_Cov_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_12_1_YJN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_26_1_T5M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_13_1_rnu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_22_1_vMS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_10_1_vLZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_25_1_bIL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_24_1_RFk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_20_1_rWR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_2_1_DC3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_11_1_Aue_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_8_1_zl2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_18_1_lXO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_SemiLeptMGDecays_v9FlatTuple/FlatTuple_4_1_sB2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_1_1_Oih_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_7_1_Z9Y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_2_1_Pg3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_13_1_Isa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_3_1_WgA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_5_1_4EV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_19_1_imM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_4_1_c5b_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_11_1_CJs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_8_1_qyP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_18_1_3dA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_17_1_uGv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_6_1_1iy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_12_1_o0T_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_21_1_GjB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_20_1_Nin_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_16_1_kb9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_14_1_SeW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_24_1_1rT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_26_1_El7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_27_1_Gig_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_22_1_Jjj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_23_1_T4r_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_28_1_zfY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_10_1_bg8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_25_1_X0I_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_9_1_BTc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_15_1_3u0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_HadronicMGDecays_v9FlatTuple/FlatTuple_29_1_nJx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_27_1_Grg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_21_1_0xj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_28_1_uxE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_3_1_KGN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_2_1_gei_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_7_1_jy6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_5_1_o1S_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_8_1_9ps_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_10_1_HTK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_12_1_TXN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_19_1_OWY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_15_1_5SV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_6_1_2w5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_1_1_fRS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_4_1_mXB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_9_1_LVP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_20_1_q05_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_22_1_Rmk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_18_1_EFf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_24_1_dr9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_16_1_jXn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_25_1_xXT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_11_1_pT4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_23_1_QeV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_14_1_JL1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_26_1_5Tq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_13_1_g1M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/TTJets_FullLeptMGDecays_v9FlatTuple/FlatTuple_17_1_eFr_skimmed.root')


#############
# single t


listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_7_1_uDa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_5_1_H7A_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_14_1_x2E_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_15_1_5lJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_6_1_TxG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_3_1_2ah_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_8_1_T7C_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_18_1_ofD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_12_1_B94_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_10_1_QnG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_4_1_dH0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_17_1_w4w_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_11_1_DRU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_24_1_rwL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_9_1_R2M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_21_1_yv4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_16_1_odt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_20_1_xxt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_26_1_muB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_13_1_QKv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_23_1_GAP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_22_1_zxF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_25_1_Vgk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_19_1_vAZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_1_1_aW7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/T_tWchannel_v9FlatTuple/FlatTuple_2_1_lu5_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_4_1_kNu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_1_1_4ij_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_7_1_65t_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_2_1_tVw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_3_1_qCr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_5_1_3gb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_6_1_AeS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_15_1_m90_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_8_1_GIl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_10_1_yZz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_12_1_DCx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_11_1_Il2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_16_1_9fC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_17_1_fJQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_18_1_84F_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_25_1_P4z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_13_1_VM7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_19_1_Ycl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_22_1_XoL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_23_1_CmB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_26_1_5VS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_14_1_NsI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_24_1_mNh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_20_1_E0M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_21_1_Fr6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/Tbar_tWchannel_v9FlatTuple/FlatTuple_9_1_S69_skimmed.root')


###########
# vv


listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_4_1_la2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_1_1_23t_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_2_1_JIh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_5_1_MOi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_9_1_rbm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_13_1_L6m_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_6_1_QpZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_10_1_Z5O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_23_1_86J_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_21_1_PDp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_20_1_zta_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_24_1_poY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_19_1_Z43_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_7_1_N7M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_11_1_Ji0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_26_1_XJ8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_17_1_pJY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_15_1_bDK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_16_1_PIm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_22_1_rUo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_14_1_ZfD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_25_1_Xef_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_8_1_VTa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_3_1_G81_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_18_1_aHS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Nu_v9FlatTuple/FlatTuple_12_1_JRt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_1_1_K4u_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_2_1_2FD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_7_1_pnR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_3_1_xE2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_8_1_Jgv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_26_1_ul0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_5_1_gJ3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_10_1_Nh9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_12_1_ApQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_4_1_qMM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_11_1_qbx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_19_1_wAJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_14_1_ZmB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_9_1_AGo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_22_1_X8g_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_20_1_Yui_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_21_1_vfr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_17_1_JM7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_25_1_00n_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_13_1_Abg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_24_1_5A4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_18_1_4Zl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_16_1_PIq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_15_1_0Wr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_23_1_lSc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo2L2Q_v9FlatTuple/FlatTuple_6_1_3pA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_6_1_HPX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_3_1_2nS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_5_1_jg7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_11_1_ffP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_7_1_q97_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_28_1_GuA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_22_1_W2b_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_1_1_RGf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_12_1_l5S_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_15_1_jnA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_10_1_YtW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_9_1_Fs1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_26_1_lF8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_8_1_I6G_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_2_1_tIH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_18_1_NzY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_16_1_WAH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_17_1_ll7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_25_1_NuV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_14_1_iog_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_20_1_LuA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_23_1_xVA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_13_1_2fm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_4_1_LEP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_21_1_HMi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_27_1_S7I_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_24_1_LXg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/ZZJetsTo4L_v9FlatTuple/FlatTuple_19_1_iL6_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_25_1_4wI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_1_1_Bcq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_2_1_yZh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_6_1_bNY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_7_1_bob_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_8_1_ZQE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_10_1_VE4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_9_1_wHJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_13_1_NCn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_27_1_FvZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_5_1_cRE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_12_1_HMX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_16_1_gf2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_17_1_ouw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_15_1_Vyu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_19_1_dhg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_14_1_2nw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_18_1_vfk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_3_1_xVo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_21_1_GEf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_20_1_0n5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_23_1_RNq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_22_1_2Mx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_26_1_1wq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_11_1_DAs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_24_1_QQS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo2L2Q_v9FlatTuple/FlatTuple_4_1_u39_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_4_1_XkU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_13_1_qAi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_2_1_5It_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_6_1_RXJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_10_1_MzD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_9_1_fmJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_3_1_wbN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_5_1_Ues_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_7_1_Exh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_8_1_7o4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_11_1_4IA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_1_1_RWI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_26_1_Gnk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_19_1_p7m_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_18_1_bHw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_14_1_bPA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_16_1_npJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_12_1_92s_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_17_1_ZmN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_21_1_Hja_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_25_1_WWN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_22_1_ELo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_15_1_5Rc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_23_1_mB5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_24_1_6lh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WZJetsTo3LNu_v9FlatTuple/FlatTuple_20_1_zOq_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_14_1_wtM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_1_1_0s9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_5_1_MHg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_4_1_0xT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_2_1_dLN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_26_1_rVA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_7_1_ZhP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_8_1_u8u_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_9_1_pmh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_11_1_Ofe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_12_1_d3Y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_10_1_e3v_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_23_1_mhS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_16_1_EcB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_15_1_NBp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_6_1_w7x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_20_1_W51_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_3_1_63M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_24_1_w8E_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_18_1_6lT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_19_1_qMy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_21_1_oC2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_25_1_MZI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_13_1_voj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_17_1_fSb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WWJetsTo2L2Nu_v9FlatTuple/FlatTuple_22_1_L0U_skimmed.root')




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
	maxEntries = 5000

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
				if passesHighMtSameSignSelectionETau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				if passesHighMtSameSignSelectionMuTau(chain,index,UseNewTriggers,Verbose) is False:
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
				SAMPLE_ADD = getSAMPLE_ADD(sampleName)
				assert(len(SAMPLE_ADD)>0), " Assert : unknown sample "
				if SAMPLE_ADD == '_data_obs_':
					FillObsDATA(maxPairTypeAndIndex,SAMPLE_ADD,
										histogram_dict,
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
					Fill_TTbarMC(maxPairTypeAndIndex,classification,wt_dict,histogram_dict,eventVariables['SVFitMass'])

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
