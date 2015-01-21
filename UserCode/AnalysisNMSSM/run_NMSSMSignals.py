import time
import sys
import os

############
# due to 3 crashing events
# impose the following SF
# bbSUSY900 GEV (997674-2217)/997674.0 = 9.97777831235453716e-01
# ggHSUSY 250 GeV (1000441-2223)/1000441.0 = 9.97777979910859258e-01
# ggHSUSY 900 GeV (975744-2168.)/975744 = 9.97778105732651133e-01

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
#listOfFiles.append('./HOLDER/NMSSM80.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_10_1_evX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_11_1_1Jr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_12_1_rdA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_13_1_VXr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_14_1_yh3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_15_1_7oc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_16_1_kSJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_17_1_lyU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_18_1_8IY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_19_1_0xv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_1_1_WTN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_20_1_26z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_21_1_9Vs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_22_1_SpK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_23_1_zui_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_24_1_K7l_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_25_1_4Ac_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_26_1_SA2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_2_1_23H_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_3_1_mM4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_4_1_qye_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_5_1_oV0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_6_1_4tN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_7_1_Odl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_8_1_G7M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum25_FLATv9Xntup/FlatTuple_9_1_Bin_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_10_1_YHD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_11_1_yU8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_12_1_2sc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_13_1_gxv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_14_1_dta_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_15_1_mio_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_16_1_DPq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_17_1_vmq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_18_1_I9W_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_19_1_eYB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_1_1_lze_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_20_1_DkF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_21_1_0ov_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_22_1_oIV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_23_1_rmc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_24_1_eEI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_25_1_9IW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_26_1_6ax_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_2_1_etm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_3_1_kbo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_4_1_Ik3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_5_1_jNk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_6_1_K8C_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_7_1_h7n_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_8_1_AMp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum30_FLATv9Xntup/FlatTuple_9_1_qXw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_10_1_w1M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_11_1_W8L_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_12_1_vFe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_13_1_8Cs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_14_1_YNH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_15_1_NwZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_16_1_bQI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_17_1_ImN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_18_1_SqE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_19_1_1Kp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_1_1_Sxy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_20_1_Hjn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_21_1_G1B_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_22_1_Dnx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_23_1_Z1c_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_24_1_kbs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_25_1_L3M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_26_1_1RM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_2_1_klu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_3_1_Xul_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_4_1_wQG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_5_1_Kb2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_6_1_AZs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_7_1_dOi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_8_1_xnR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum35_FLATv9Xntup/FlatTuple_9_1_NFD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_10_1_c8e_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_11_1_flB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_12_1_eGO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_13_1_69Z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_14_1_pt4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_15_1_fXn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_16_1_0YW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_17_1_714_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_18_1_rbb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_19_1_nJ4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_1_1_NMd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_20_1_4Ia_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_21_1_faG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_22_1_N7x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_23_1_jzh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_24_1_nCx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_25_1_Tlp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_26_1_Wqa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_2_1_tR3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_3_1_f5T_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_4_1_YMe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_5_1_5Bn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_6_1_8k7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_7_1_q4O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_8_1_hpd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum40_FLATv9Xntup/FlatTuple_9_1_Yzo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_10_1_dUf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_11_1_5zg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_12_1_iuT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_13_1_rRC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_14_1_W4H_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_15_1_fIm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_16_1_Ka7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_17_1_uXl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_18_1_2hS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_19_1_Ani_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_1_1_Vh6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_20_1_fkc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_21_1_l1P_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_22_1_qrd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_23_1_iIm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_24_1_uTt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_25_1_Pi6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_26_1_B8R_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_2_1_VKz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_3_1_368_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_4_1_VCO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_5_1_ZTF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_6_1_7Il_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_7_1_irg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_8_1_KmA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum45_FLATv9Xntup/FlatTuple_9_1_GtV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_10_1_ZVX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_11_1_iUJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_12_1_Kil_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_13_1_SX9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_14_1_K4i_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_15_1_gM4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_16_1_MVd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_17_1_kdj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_18_1_Rz6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_19_1_LYf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_1_1_Ct4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_20_1_8Pd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_21_1_HG0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_22_1_3RD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_23_1_Pv9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_24_1_Em6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_25_1_AEC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_26_1_qmQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_2_1_Mwn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_3_1_zLF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_4_1_bW9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_5_1_f0Z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_6_1_Hir_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_7_1_vZx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_8_1_uZR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum50_FLATv9Xntup/FlatTuple_9_1_rzD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_10_1_hPV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_11_1_Ow1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_12_1_tNp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_13_1_Wqn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_14_1_Skp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_15_1_rXo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_16_1_DJN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_17_1_KGN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_18_1_HKR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_19_1_G2z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_1_1_COI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_20_1_lmF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_21_1_uPl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_22_1_ESH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_23_1_NON_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_24_1_J4U_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_25_1_xxV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_2_1_n3g_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_3_1_1jh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_4_1_yVf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_5_1_51x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_6_1_MWR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_7_1_a90_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_8_1_2gi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum55_FLATv9Xntup/FlatTuple_9_1_E1Y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_10_1_7gd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_11_1_veZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_12_1_Mvt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_13_1_LnI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_14_1_rjH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_15_1_WGd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_16_1_OQR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_17_1_ME1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_18_1_hRH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_19_1_DlU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_1_1_PsX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_20_1_AYm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_21_1_zCc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_22_1_pIW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_23_1_BWO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_24_1_T8V_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_25_1_fVq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_26_1_6vj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_2_1_x4l_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_3_1_Saw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_4_1_2sw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_5_1_wHv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_6_1_O0v_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_7_1_eYS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_8_1_DGs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum60_FLATv9Xntup/FlatTuple_9_1_AVQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_10_1_bkN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_11_1_Z6e_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_12_1_EtI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_13_1_P7C_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_14_1_RN8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_15_1_2zw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_16_1_AIf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_17_1_M7Z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_18_1_EV3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_19_1_3L5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_1_1_ePP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_20_1_8dv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_21_1_Lr6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_22_1_hfL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_23_1_Unp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_24_1_VSq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_25_1_W1U_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_26_1_YKI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_2_1_13p_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_3_1_C1K_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_4_1_60H_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_5_1_ZcM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_6_1_8sk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_7_1_Dti_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_8_1_IIU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum65_FLATv9Xntup/FlatTuple_9_1_Hir_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_10_1_hjT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_11_1_nOu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_12_1_JxI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_13_1_4nB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_14_1_B74_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_15_1_uHG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_16_1_Ksa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_17_1_Jpw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_18_1_JfV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_19_1_pZw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_1_1_hks_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_20_1_1uP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_21_1_ep0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_22_1_AHr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_23_1_jpj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_24_1_lY4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_25_1_YzB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_26_1_vaQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_2_1_5TA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_3_1_wAi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_4_1_ZD9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_5_1_uj7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_6_1_z4N_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_7_1_9Os_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_8_1_KRb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum70_FLATv9Xntup/FlatTuple_9_1_Y6i_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_10_1_dr4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_11_1_sj9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_12_1_N3B_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_13_1_8lC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_14_1_odX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_15_1_tHa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_16_1_bcD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_17_1_Q7y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_18_1_wtX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_19_1_C49_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_1_1_z7i_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_20_1_sz4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_21_1_luu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_22_1_SFV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_23_1_rFd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_24_1_cBj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_25_1_5kk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_26_1_Pix_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_2_1_oh7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_3_1_ryN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_4_1_2W1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_5_1_Uac_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_6_1_5XJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_7_1_ozy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_8_1_nHb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum75_FLATv9Xntup/FlatTuple_9_1_wuM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_10_1_8sR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_11_1_S7e_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_12_1_aGB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_13_1_AKt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_14_1_8wN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_15_1_RLj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_16_1_Yuk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_17_1_SCX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_18_1_qfj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_19_1_3kC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_1_1_aoD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_20_1_VaI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_21_1_xq3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_22_1_DNM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_23_1_sfE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_24_1_lrK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_25_1_k1Z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_26_1_0VQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_2_1_PU3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_3_1_ChZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_4_1_Cok_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_5_1_w5Q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_6_1_MwS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_7_1_8fv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_8_1_5xq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_9_1_KZj_skimmed.root')

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
					#maxPairTypeAndIndex.append(muTauClassificationJECDOWN(chain, maxPairTypeAndIndex[0]))
					#maxPairTypeAndIndex.append(muTauClassificationJECUP(chain, maxPairTypeAndIndex[0]))
				if maxPairTypeAndIndex[1] == 'eleTau':
					maxPairTypeAndIndex.append(eTauClassification(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(chain.NAMEVAR)
					#maxPairTypeAndIndex.append(eTauClassificationJECDOWN(chain, maxPairTypeAndIndex[0]))
					#maxPairTypeAndIndex.append(eTauClassificationJECUP(chain, maxPairTypeAndIndex[0]))
				if PrintEvents:
					print maxPairTypeAndIndex[1], maxPairTypeAndIndex[2],eventID[0]+"-"+eventID[1]+"-"+eventID[2]

##################################################################################
# get weights and fill histograms


			if len(maxPairTypeAndIndex)	> 0:
				eventVariables = {}
				fillVariables(chain,eventVariables,maxPairTypeAndIndex,Verbose)
				finalWt = nMSSMweights(chain, maxPairTypeAndIndex, Verbose)
				SAMPLE_ADD = getSAMPLE_ADD(sampleName)
				assert(len(SAMPLE_ADD)>0), " Assert : unknown sample "
				#print maxPairTypeAndIndex
				FillNMSSMSignals(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,eventVariables['SVFitMass'])


######################
# save filled histograms

WriteEverything()
writeCompFile()
