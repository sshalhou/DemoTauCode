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



listOfFiles.append('./HOLDER/DYTauPolOff.root')
listOfFiles.append('./HOLDER/DYTauPolOff2.root')
listOfFiles.append('./HOLDER/DY2jet.root')

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
				if passesDefaultSelectionETau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				if passesDefaultSelectionMuTau(chain,index,UseNewTriggers,Verbose) is False:
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
				if SAMPLE_ADD == '_DYTauPolOff_':
					classification = classifyZDecay_Final(chain,maxPairTypeAndIndex)
					print classification
					wt = 1.0
					if classification == '_ZL_':
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
					if classification == '_ZL_':
						wt = getWeightForRegularDY_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose)
						# contains an internal check for e->tau
						wt = wt * getFakeZeeWeight(chain,maxPairTypeAndIndex)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					elif classification == '_ZJ_':
						wt = getWeightForRegularDY_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])



######################
# save filled histograms

WriteEverything()
writeCompFile()
