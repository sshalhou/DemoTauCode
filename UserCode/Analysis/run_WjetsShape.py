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


#listOfFiles.append('./HOLDER/W2jet.root')
#listOfFiles.append('./HOLDER/W2.root')




##########
#wjets


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




for afile in listOfFiles:
	chain.AddFile(afile,0,'TauEsNominal/FlatTuple')
	chain.AddFile(afile,0,'TauEsUp/FlatTuple')
	chain.AddFile(afile,0,'TauEsDown/FlatTuple')


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
	maxEntries = 25000

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
				if passesDefaultSelectionWithLooseOrTightTauIsoETau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				if passesDefaultSelectionWithLooseOrTightTauIsoMuTau(chain,index,UseNewTriggers,Verbose) is False:
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
					maxPairTypeAndIndex.append(muTauClassificationJECDOWN_looseBtag(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(muTauClassificationJECUP_looseBtag(chain, maxPairTypeAndIndex[0]))
				if maxPairTypeAndIndex[1] == 'eleTau':
					maxPairTypeAndIndex.append(eTauClassification_forQCD(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(chain.NAMEVAR)
					maxPairTypeAndIndex.append(eTauClassificationJECDOWN_looseBtag(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(eTauClassificationJECUP_looseBtag(chain, maxPairTypeAndIndex[0]))
				if PrintEvents:
					print maxPairTypeAndIndex[1], maxPairTypeAndIndex[2],eventID[0]+"-"+eventID[1]+"-"+eventID[2]

##################################################################################
# get weights and fill histograms


			if len(maxPairTypeAndIndex)	> 0:
				eventVariables = {}
				fillVariables(chain,eventVariables,maxPairTypeAndIndex,Verbose)
				SAMPLE_ADD = getSAMPLE_ADD(sampleName)
				assert(len(SAMPLE_ADD)>0), " Assert : unknown sample "


				if (SAMPLE_ADD == '_WJetsToLNu_' or
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

					##################
					# inclusive takes only tight isolated taus
					# btagged and non-btagged takes loose isolated taus
					i=maxPairTypeAndIndex[0]
					tauIsoFill = {}
					tauIsoFill['inclusive'] = False
					tauIsoFill['Btag-or-noBtag'] = False
					if maxPairTypeAndIndex[1] == 'muTau':
						if(chain.muT_tau_byLooseIsolationMVA3oldDMwLT[i] > 0.5):
							tauIsoFill['Btag-or-noBtag'] = True
						if(chain.muT_tau_byTightIsolationMVA3oldDMwLT[i] > 0.5):
							tauIsoFill['inclusive'] = True
					if maxPairTypeAndIndex[1] == 'eleTau':
						if(chain.eT_tau_byLooseIsolationMVA3oldDMwLT[i] > 0.5):
							tauIsoFill['Btag-or-noBtag'] = True
						if(chain.eT_tau_byTightIsolationMVA3oldDMwLT[i] > 0.5):
							tauIsoFill['inclusive'] = True
					Fill_WjetsMC_forWjetsShape(tauIsoFill,maxPairTypeAndIndex,classification,wt_dict,histogram_dict,eventVariables['SVFitMass'])




######################
# save filled histograms

WriteEverything()
writeCompFile()
