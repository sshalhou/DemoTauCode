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



listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_10_1_2fA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_11_1_teB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_12_1_Ag1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_13_1_6f0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_14_1_ZPe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_15_1_sK5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_16_1_bGO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_17_1_1cW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_18_1_S7I_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_19_1_hcV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_1_1_XNb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_20_1_4bg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_21_1_5vk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_22_1_hnL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_23_1_67e_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_24_1_ra9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_25_1_bTM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_26_1_QKK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_27_1_Rh1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_28_1_0dW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_29_1_fjM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_2_1_gIt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_30_1_vXj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_3_1_l2b_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_4_1_3vw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_5_1_Y2z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_6_1_J0N_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_7_1_erH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_8_1_Yrh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV19v1_FLATv9Xntup/FlatTuple_9_1_VtF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_10_1_Xh4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_11_1_4HZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_12_1_zm2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_13_1_Olk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_14_1_ehg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_15_1_BxA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_16_1_cn3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_17_1_qXu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_18_1_15a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_19_1_ZJM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_1_1_pak_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_20_1_Y2v_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_21_1_bGN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_22_1_3rW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_23_1_dD3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_24_1_WFO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_25_1_CrR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_26_1_FIl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_27_1_AsY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_28_1_6y0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_29_1_0eb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_2_1_92V_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_3_1_N9q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_4_1_X1A_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_5_1_EdW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_6_1_36d_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_7_1_4Jn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_8_1_SYc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W1jetsLNuV7Av1_FLATv9Xntup/FlatTuple_9_1_GYO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_10_1_GnD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_11_1_PR1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_12_1_CKh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_13_1_0uw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_14_1_k8T_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_15_1_Ttb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_16_1_qBw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_17_1_USz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_18_1_Bt4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_19_1_3Ip_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_1_1_72R_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_20_1_f9k_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_21_1_ucG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_22_1_cOQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_23_1_34L_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_24_1_LVO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_25_1_BLH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_26_1_n1L_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_27_1_Lza_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_28_1_Dqq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_29_1_C7I_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_2_1_JPv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_3_1_gup_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_4_1_hTZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_5_1_AI4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_6_1_MQ2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_7_1_EXj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_8_1_gcv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV19v1_FLATv9Xntup/FlatTuple_9_1_ead_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_10_1_jsM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_11_1_rHc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_12_1_7BQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_13_1_Mtt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_14_1_OLX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_15_1_ZTa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_16_1_Atx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_17_1_M2W_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_18_1_LLZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_19_1_TiI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_1_1_f8a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_20_1_Enb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_21_1_nbO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_22_1_Yq8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_23_1_uZw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_24_1_h6N_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_25_1_Z8K_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_26_1_YTu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_27_1_PCU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_2_1_faG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_3_1_ADP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_4_1_Icg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_5_1_In5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_6_1_zp3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_7_1_uvw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_8_1_QQ0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W2jetsLNuV7Av1_FLATv9Xntup/FlatTuple_9_1_VvI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_10_1_GzR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_11_1_uTp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_12_1_P2i_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_13_1_YK4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_14_1_bqS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_15_1_M4N_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_16_1_BZ6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_17_1_Pcc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_18_1_G2C_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_19_1_Kcd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_1_1_Kn6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_20_1_KD2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_21_1_4qt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_22_1_e13_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_23_1_lEp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_24_1_biM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_25_1_AtX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_26_1_DkO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_27_1_gIu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_28_1_67z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_2_1_PIy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_3_1_74x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_4_1_pNP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_5_1_wTZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_6_1_hd7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_7_1_Cyx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_8_1_yx8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV19v1_FLATv9Xntup/FlatTuple_9_1_FTZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_10_1_aAc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_11_1_smP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_12_1_ATE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_13_1_m0M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_14_1_cAz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_15_1_Jou_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_16_1_pKt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_17_1_zlW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_18_1_8TX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_19_1_gLW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_1_1_GGb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_20_1_DEv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_21_1_7Sx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_22_1_BTw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_23_1_gS5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_24_1_FK2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_25_1_tCb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_26_1_AMT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_27_1_KIs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_2_1_KZF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_3_1_MFg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_4_1_MBG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_5_1_JkT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_6_1_lGJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_7_1_5Nq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_8_1_Af9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W3jetsLNuV7Av1_FLATv9Xntup/FlatTuple_9_1_eFQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_10_1_U3N_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_11_1_pTv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_12_1_Jbc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_13_1_ZKN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_14_1_NvU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_15_1_oSK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_16_1_z2A_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_17_1_NAw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_18_1_ZPz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_19_1_8zf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_1_1_Z5Z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_20_1_6vQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_21_1_OS2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_22_1_3yz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_23_1_uSp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_24_1_8Yc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_25_1_Uvy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_26_1_CFl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_27_1_NpC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_28_1_aGk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_2_1_Hc3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_3_1_kZY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_4_1_M3n_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_5_1_xa5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_6_1_UdS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_7_1_ihf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_8_1_WlY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/W4jetsLNuV1_FLATv9Xntup/FlatTuple_9_1_9Wk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_10_1_usi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_11_1_dZT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_12_1_Jd5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_13_1_MWA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_14_1_KOl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_15_1_pvg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_16_1_KGE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_17_1_13i_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_18_1_wmE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_19_1_X4T_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_1_1_TSR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_20_1_zma_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_21_1_i3S_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_22_1_F59_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_23_1_HhN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_24_1_XNW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_25_1_BTB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_26_1_wcX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_27_1_Q9O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_28_1_BAE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_2_1_Fjy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_3_1_DOA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_4_1_S0X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_5_1_Lsr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_6_1_rnb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_7_1_qI3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_8_1_Jvy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV1_FLATv9Xntup/FlatTuple_9_1_m4q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_10_1_Ati_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_11_1_4ZK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_12_1_R7n_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_13_1_lnC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_14_1_8V3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_15_1_hDW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_16_1_lWb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_17_1_Bbo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_18_1_QiO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_19_1_dbF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_1_1_uuz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_20_1_A8X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_21_1_aUI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_22_1_gsD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_23_1_IvE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_24_1_5Dh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_25_1_O7F_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_26_1_BPk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_27_1_LWA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_28_1_TfQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_2_1_Jy1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_3_1_ggh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_4_1_LJp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_5_1_ysZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_6_1_94q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_7_1_nqE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_8_1_QFM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WjetsLNuV2_FLATv9Xntup/FlatTuple_9_1_3EO_skimmed.root')


############
# DATA


listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNA_V9XFlatTuple/FlatTuple_1_1_BF5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNA_V9XFlatTuple/FlatTuple_2_1_dLg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNB_V9XFlatTuple/FlatTuple_1_1_2iz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNB_V9XFlatTuple/FlatTuple_2_1_9ar_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNB_V9XFlatTuple/FlatTuple_3_1_jah_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNB_V9XFlatTuple/FlatTuple_4_1_Dlv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNB_V9XFlatTuple/FlatTuple_5_1_wtf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNB_V9XFlatTuple/FlatTuple_6_1_HoI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNB_recover_V9XFlatTuple/FlatTuple_1_1_9in_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNC_V9XFlatTuple/FlatTuple_1_1_i89_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNC_V9XFlatTuple/FlatTuple_2_1_mFV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNC_V9XFlatTuple/FlatTuple_3_1_dTp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNC_V9XFlatTuple/FlatTuple_4_1_JFh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNC_V9XFlatTuple/FlatTuple_5_1_9yI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNC_V9XFlatTuple/FlatTuple_6_1_9tl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNC_V9XFlatTuple/FlatTuple_7_1_zaN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNC_V9XFlatTuple/FlatTuple_8_1_8YI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUNC_V9XFlatTuple/FlatTuple_9_1_lY6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUND_V9XFlatTuple/FlatTuple_1_1_J0n_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUND_V9XFlatTuple/FlatTuple_2_1_F1W_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUND_V9XFlatTuple/FlatTuple_3_1_LTO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUND_V9XFlatTuple/FlatTuple_4_1_tgn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUND_V9XFlatTuple/FlatTuple_5_1_Ax8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUND_V9XFlatTuple/FlatTuple_6_1_rfl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUND_V9XFlatTuple/FlatTuple_7_1_3Dw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/DATA2012RUND_V9XFlatTuple/FlatTuple_8_1_CHr_skimmed.root')



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




##########
# tt


listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_10_1_hw6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_11_1_V27_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_12_1_xXx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_13_1_xsF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_14_1_UTY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_15_1_CCl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_16_1_JgG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_17_1_Wwi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_18_1_LOw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_19_1_h9Y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_1_1_jsP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_20_1_SIB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_21_1_0kX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_22_1_PxW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_23_1_IGg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_24_1_gvD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_25_1_IfC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_26_1_mqr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_27_1_X1v_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_28_1_vsV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_29_1_RmM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_2_1_pfd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_3_1_oiL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_4_1_qLS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_5_1_4nF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_6_1_jEQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_7_1_ijV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_8_1_t7F_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_FullLeptMGDecays_FLATv9Xntup/FlatTuple_9_1_E4q_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_10_1_PBD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_11_1_ET6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_12_1_9av_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_13_1_PqN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_14_1_pWU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_15_1_enV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_16_1_adR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_17_1_Eqj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_18_1_LbW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_19_1_S3H_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_1_1_LsI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_20_1_XIP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_21_1_epo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_22_1_kdV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_23_1_bRK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_24_1_d6b_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_25_1_MJl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_26_1_XdR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_27_1_P3P_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_28_1_Jow_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_29_1_Gux_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_2_1_1Fu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_3_1_zny_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_4_1_2QA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_5_1_7b3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_6_1_nuw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_7_1_TEO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_8_1_fVf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_HadronicMGDecays_FLATv9Xntup/FlatTuple_9_1_thY_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_10_1_aiP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_11_1_3yD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_12_1_KmZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_13_1_JI3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_14_1_YYw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_15_1_FkY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_16_1_aFf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_17_1_r3d_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_18_1_xa2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_19_1_PIi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_1_1_jw7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_20_1_taM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_21_1_Pdn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_22_1_ryR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_23_1_tRe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_24_1_eyw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_25_1_q9q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_26_1_ToD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_27_1_Q4P_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_28_1_IJT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_2_1_j9r_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_3_1_tFv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_4_1_Q5K_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_5_1_XLD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_6_1_Zpz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_7_1_fMh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_8_1_4vU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/TTJets_SemiLeptMGDecays_FLATv9Xntup/FlatTuple_9_1_4BS_skimmed.root')



#############
# single t


listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_10_1_X45_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_11_1_w9z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_12_1_QTL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_13_1_RRU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_14_1_AXC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_15_1_BHs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_16_1_Ghc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_17_1_6Pa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_18_1_bC8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_19_1_ybL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_1_1_0qJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_20_1_JL1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_21_1_Tii_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_22_1_pjM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_23_1_Xg9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_24_1_f7a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_25_1_iXw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_26_1_Lhj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_2_1_hIn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_3_1_cGk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_4_1_yVs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_5_1_Kbi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_6_1_veh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_7_1_lSG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_8_1_Hge_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/T_tWchannel_FLATv9Xntup/FlatTuple_9_1_L5P_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_10_1_ufr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_11_1_8HS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_12_1_xsO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_13_1_5ow_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_14_1_cS3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_15_1_DKI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_16_1_ws9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_17_1_XjD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_18_1_r3j_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_19_1_vQH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_1_1_rT3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_20_1_2aK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_21_1_RGj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_22_1_m6X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_23_1_yRv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_24_1_nbj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_25_1_MkN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_26_1_rIH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_2_1_6jb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_3_1_Zk8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_4_1_ai6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_5_1_bvo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_6_1_3Fb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_7_1_zYJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_8_1_nWH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/Tbar_tWchannel_FLATv9Xntup/FlatTuple_9_1_LAn_skimmed.root')


###########
# vv


listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_10_1_ryJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_11_1_Uwk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_12_1_Ilq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_13_1_AJ6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_14_1_cJA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_15_1_OXV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_16_1_4QF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_17_1_Z23_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_18_1_5D7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_19_1_4YW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_1_1_fPn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_20_1_0fv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_21_1_Juq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_22_1_gIf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_23_1_0ga_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_24_1_nl3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_25_1_72K_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_26_1_ihL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_2_1_4mq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_3_1_NWi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_4_1_om7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_5_1_Xfw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_6_1_b0V_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_7_1_9PH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_8_1_C8x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Nu_FLATv9Xntup/FlatTuple_9_1_qW5_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_10_1_bZ7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_11_1_JAi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_12_1_WTj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_13_1_q1W_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_14_1_oOa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_15_1_Jh8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_16_1_upt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_17_1_XTW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_18_1_PU2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_19_1_90T_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_1_1_P4O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_20_1_iMC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_21_1_d21_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_22_1_2pM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_23_1_bSa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_24_1_4ri_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_25_1_prC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_26_1_4KC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_2_1_kKe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_3_1_q9Z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_4_1_2FI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_5_1_bOO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_6_1_4av_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_7_1_r7b_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_8_1_Ayt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo2L2Q_FLATv9Xntup/FlatTuple_9_1_JYv_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_10_1_T6f_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_11_1_hAh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_12_1_3SO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_13_1_yHa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_14_1_phO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_15_1_EJm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_16_1_0Ju_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_17_1_Ezn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_18_1_F3K_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_19_1_nIH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_1_1_JWb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_20_1_f4g_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_21_1_UGG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_22_1_6xc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_23_1_kzl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_24_1_UKU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_25_1_ZuE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_26_1_76e_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_27_1_cBG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_28_1_TCh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_2_1_SK9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_3_1_1bF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_4_1_QdB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_5_1_Tss_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_6_1_OhQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_7_1_f9N_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_8_1_I8Z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/ZZJetsTo4L_FLATv9Xntup/FlatTuple_9_1_0lg_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_10_1_z5t_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_11_1_aKf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_12_1_YG6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_13_1_1vk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_14_1_mtM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_15_1_KCK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_16_1_72O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_17_1_uva_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_18_1_G5J_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_19_1_43v_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_1_1_3li_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_20_1_pct_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_21_1_MQx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_22_1_bKP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_23_1_T4U_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_24_1_NcW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_25_1_LiW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_26_1_W1p_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_27_1_2VT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_2_1_2bO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_3_1_gYU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_4_1_6XC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_5_1_1fw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_6_1_awE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_7_1_COM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_8_1_rA2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo2L2Q_FLATv9Xntup/FlatTuple_9_1_Okz_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_10_1_L7D_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_11_1_uXt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_12_1_7R5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_13_1_N6q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_14_1_Xep_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_15_1_X4D_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_16_1_P9T_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_17_1_flh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_18_1_OKW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_19_1_BLK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_1_1_B2J_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_20_1_Kbl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_21_1_S8U_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_22_1_itV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_23_1_Tdp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_24_1_FBj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_25_1_nun_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_26_1_t0Y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_2_1_pXf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_3_1_tfJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_4_1_A5c_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_5_1_sAE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_6_1_iSe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_7_1_bJW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_8_1_OCh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WZJetsTo3LNu_FLATv9Xntup/FlatTuple_9_1_UX2_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_10_1_HoA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_11_1_Cu6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_12_1_O3P_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_13_1_Ks2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_14_1_7LF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_15_1_pr3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_16_1_VKx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_17_1_L1x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_18_1_zCx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_19_1_naA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_1_1_1kO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_20_1_2vp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_21_1_qT7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_22_1_cjL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_23_1_FwS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_24_1_pzh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_25_1_fvn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_26_1_FrL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_2_1_SwA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_3_1_fKQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_4_1_3wL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_5_1_TSx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_6_1_K6Z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_7_1_zaf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_8_1_5Ew_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WWJetsTo2L2Nu_FLATv9Xntup/FlatTuple_9_1_bNC_skimmed.root')



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
				elif (SAMPLE_ADD=='_DY1Jet_' or
				      SAMPLE_ADD=='_DYJetsInclusive_' or
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
