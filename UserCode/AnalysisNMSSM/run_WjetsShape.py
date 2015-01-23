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
