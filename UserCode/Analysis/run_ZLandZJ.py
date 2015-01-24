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
# DY

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_10_1_17X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_11_1_hgk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_12_1_HIh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_13_1_MiR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_14_1_4le_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_15_1_kYT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_16_1_WSP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_17_1_RTk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_18_1_x7L_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_19_1_kQf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_1_1_scX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_20_1_Cji_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_21_1_svA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_22_1_5Um_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_23_1_5Sg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_24_1_cRS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_25_1_3hj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_26_1_FP7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_27_1_Zbq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_28_1_KgU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_2_1_l4e_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_3_1_Spa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_4_1_HRV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_5_1_Fx0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_6_1_Gkr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_7_1_Kts_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_8_1_2tO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY1JetsToLL_FLATv9Xntup/FlatTuple_9_1_R0D_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_10_1_vzo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_11_1_U5p_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_12_1_O6A_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_13_1_PC0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_14_1_Cgz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_15_1_DaS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_16_1_Qky_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_17_1_aFu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_18_1_Ff5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_19_1_vOO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_1_1_JaG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_20_1_HcV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_21_1_Ym8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_22_1_K8x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_23_1_7Xx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_24_1_uCX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_25_1_MpJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_26_1_MOg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_27_1_eJH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_2_1_P8p_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_3_1_ncs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_4_1_poc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_5_1_M9O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_6_1_jHh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_7_1_Z0P_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_8_1_pRt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY2JetsToLL_FLATv9Xntup/FlatTuple_9_1_I8T_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_10_1_RhZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_11_1_eKj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_12_1_Byi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_13_1_vBn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_14_1_ErT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_15_1_6m4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_16_1_Ivm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_17_1_z5G_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_18_1_sgq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_19_1_NKf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_1_1_Jsf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_20_1_l03_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_21_1_fMH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_22_1_0dZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_23_1_fJC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_24_1_3JZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_25_1_w9F_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_26_1_vvB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_27_1_PAS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_28_1_g1f_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_29_1_zfx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_2_1_NnD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_3_1_Zlh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_4_1_aTf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_5_1_0wA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_6_1_eal_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_7_1_GUV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_8_1_qmU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY3JetsToLL_FLATv9Xntup/FlatTuple_9_1_U71_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_10_1_0F3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_11_1_QjQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_12_1_aSE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_13_1_EHq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_14_1_na3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_15_1_S20_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_16_1_sXc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_17_1_Tyy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_18_1_VM5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_19_1_pbK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_1_1_2qa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_20_1_zVO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_21_1_W8e_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_22_1_w1L_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_23_1_u9i_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_24_1_00y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_25_1_YiI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_26_1_PWN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_27_1_TNr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_28_1_X6t_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_2_1_3SQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_3_1_ZKD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_4_1_2gV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_5_1_Ss5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_6_1_h8G_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_7_1_gBi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_8_1_kxn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DY4JetsToLL_FLATv9Xntup/FlatTuple_9_1_dgp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_10_1_5aA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_11_1_1yB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_12_1_4pe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_13_1_EFt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_14_1_cI7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_15_1_mM9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_16_1_s1H_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_17_1_weK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_18_1_4lx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_19_1_7tO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_1_1_l6a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_20_1_Zif_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_21_1_yx8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_22_1_E1I_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_23_1_Cov_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_24_1_Apf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_25_1_b22_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_26_1_ksg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_27_1_0sv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_28_1_8u1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_29_1_GYJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_2_1_kiN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_3_1_tev_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_4_1_qsD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_5_1_mY9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_6_1_lbR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_7_1_AkU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_8_1_HQl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DYJetsToLL_FLATv9Xntup/FlatTuple_9_1_hv4_skimmed.root')


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
				if (SAMPLE_ADD=='_DYJetsInclusive_' or
					SAMPLE_ADD=='_DY1Jet_' or
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
