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
#listOfFiles.append('./HOLDER/FlatTuple_SZS_SUSYBBHToTauTauM80_v5ntup.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_10_1_wrN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_11_1_jpU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_12_1_mZS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_13_1_vz2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_14_1_KLS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_15_1_9Aw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_16_1_7Xd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_17_1_MkA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_18_1_dxC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_19_1_s0n_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_1_1_wKN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_20_1_Ibg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_21_1_5VD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_22_1_09b_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_23_1_9jx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_24_1_pk0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_25_1_KKD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_26_1_cTl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_2_1_qQy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_3_1_Moc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_4_1_fu5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_5_1_pcZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_6_1_IZv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_7_1_vbS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_8_1_jfy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum25_v9FlatTuple/FlatTuple_9_1_m7S_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_10_1_AWI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_11_1_EmN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_12_1_iVo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_13_1_Hno_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_14_1_SXz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_15_1_Dq1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_16_1_M67_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_17_1_CS6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_18_1_x9c_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_19_1_mCG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_1_1_DCR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_20_1_qum_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_21_1_XJf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_22_1_Ql1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_23_1_QEQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_24_1_MKJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_25_1_C6Z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_26_1_Xd9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_2_1_i9j_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_3_1_F9A_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_4_1_oEl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_5_1_2VV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_6_1_1xh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_7_1_xjm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_8_1_mqO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum30_v9FlatTuple/FlatTuple_9_1_3GF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_10_1_nY2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_11_1_1p2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_12_1_alg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_13_1_57H_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_14_1_PAB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_15_1_4o0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_16_1_7mt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_17_1_2Ax_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_18_1_t4p_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_19_1_5Sc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_1_1_O4T_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_20_1_ysJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_21_1_V0P_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_22_1_cLz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_23_1_55I_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_24_1_F1S_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_25_1_mWO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_26_1_CQ9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_2_1_02r_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_3_1_RQb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_4_1_Kjx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_5_1_CCO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_6_1_nmD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_7_1_fXi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_8_1_iEE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum35_v9FlatTuple/FlatTuple_9_1_OF7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_10_1_Bsa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_11_1_BrD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_12_1_pip_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_13_1_fdH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_14_1_5Wp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_15_1_uNp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_16_1_xd5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_17_1_n56_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_18_1_EP6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_19_1_uiX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_1_1_aJc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_20_1_5wm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_21_1_ld0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_22_1_C0o_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_23_1_In7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_24_1_ikp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_25_1_SZ0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_26_1_1u8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_2_1_mlu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_3_1_x8m_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_4_1_EGT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_5_1_L4P_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_6_1_IMu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_7_1_JDB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_8_1_9QB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum40_v9FlatTuple/FlatTuple_9_1_mJl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_10_1_Wwd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_11_1_KN0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_12_1_bXO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_13_1_UnE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_14_1_M3r_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_15_1_CW3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_16_1_m60_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_17_1_gn3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_18_1_crT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_19_1_h58_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_1_1_Vt6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_20_1_6wK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_21_1_wuP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_22_1_7bh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_23_1_U45_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_24_1_G6P_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_25_1_FgZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_26_1_H6a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_2_1_vq9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_3_1_qOa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_4_1_Nz7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_5_1_8wK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_6_1_J7J_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_7_1_8PT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_8_1_5RR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum45_v9FlatTuple/FlatTuple_9_1_TSY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_10_1_bJD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_11_1_ojw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_12_1_lLP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_13_1_khM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_14_1_A1n_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_15_1_zHV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_16_1_dgN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_17_1_lZj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_18_1_7HL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_19_1_kdu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_1_1_8Jn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_20_1_66A_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_21_1_nbS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_22_1_WEL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_23_1_AwE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_24_1_WgM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_25_1_RJM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_26_1_KvU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_2_1_Ke3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_3_1_jKX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_4_1_bup_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_5_1_MM7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_6_1_hVI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_7_1_4zC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_8_1_kIY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum50_v9FlatTuple/FlatTuple_9_1_tVC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_10_1_CCL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_11_1_oiE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_12_1_fIP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_13_1_4Xp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_14_1_2MB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_15_1_HKZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_16_1_bKP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_17_1_Y3C_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_18_1_ziH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_19_1_qLl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_1_1_qA5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_20_1_XNd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_21_1_Jfy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_22_1_Za9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_23_1_m7L_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_24_1_WtN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_25_1_VU8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_2_1_F9V_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_3_1_aTQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_4_1_hYT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_5_1_7jE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_6_1_nJn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_7_1_nvB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_8_1_utp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum55_v9FlatTuple/FlatTuple_9_1_a4K_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_10_1_BYj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_11_1_e61_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_12_1_FAt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_13_1_gca_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_14_1_x0k_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_15_1_Sza_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_16_1_m1X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_17_1_mMb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_18_1_Am3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_19_1_5vk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_1_1_V5Z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_20_1_Wdv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_21_1_HXn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_22_1_raD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_23_1_5Mc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_24_1_iqK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_25_1_4l7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_26_1_Vew_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_2_1_XLg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_3_1_MXn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_4_1_nZ6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_5_1_9Wg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_6_1_94M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_7_1_9Ut_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_8_1_uYx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum60_v9FlatTuple/FlatTuple_9_1_Yt3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_10_1_248_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_11_1_fuF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_12_1_Edm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_13_1_ZFK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_14_1_ebj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_15_1_mBW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_16_1_wQT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_17_1_JL5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_18_1_Uhj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_19_1_7Sw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_1_1_J9G_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_20_1_fu5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_21_1_4ne_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_22_1_X5s_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_23_1_56X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_24_1_pGU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_25_1_RoK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_26_1_TzI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_2_1_wO7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_3_1_6lb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_4_1_UuK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_5_1_4fx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_6_1_bQU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_7_1_ePv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_8_1_Twa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum65_v9FlatTuple/FlatTuple_9_1_cuK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_10_1_Er8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_11_1_wEN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_12_1_vuU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_13_1_v1a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_14_1_VTS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_15_1_JvP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_16_1_Ll3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_17_1_SXa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_18_1_VmZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_19_1_HNY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_1_1_vip_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_20_1_7LE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_21_1_XwQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_22_1_jGM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_23_1_sJf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_24_1_GvT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_25_1_uYx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_26_1_fTi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_2_1_HaX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_3_1_Iuh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_4_1_Fs7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_5_1_Fmk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_6_1_4pI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_7_1_4Sx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_8_1_Sxh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum70_v9FlatTuple/FlatTuple_9_1_ZsC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_10_1_B9T_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_11_1_2QD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_12_1_lL5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_13_1_qCX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_14_1_YFh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_15_1_ExL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_16_1_YSW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_17_1_q2x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_18_1_Lzz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_19_1_PDb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_1_1_zSz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_20_1_1wX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_21_1_zEH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_22_1_oZK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_23_1_uBn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_24_1_Jts_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_25_1_lkk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_26_1_h9p_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_2_1_PSF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_3_1_zAm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_4_1_Ft6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_5_1_le3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_6_1_f2A_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_7_1_jI8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_8_1_byN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum75_v9FlatTuple/FlatTuple_9_1_2os_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_10_1_enM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_11_1_0Eo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_12_1_GWb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_13_1_1o6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_14_1_LjX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_15_1_rt8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_16_1_SLW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_17_1_43R_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_18_1_kcV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_19_1_YKC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_1_1_UYF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_20_1_m6j_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_21_1_SGm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_22_1_n3F_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_23_1_Sf8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_24_1_vKp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_25_1_P6U_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_26_1_MNJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_2_1_uUy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_3_1_jcW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_4_1_lxl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_5_1_BZs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_6_1_ID6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_7_1_juA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_8_1_vCZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/nMSSM_bba1tautaum80_v9FlatTuple/FlatTuple_9_1_5Ri_skimmed.root')

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
				if passesSUSYBBExtraSelectionETau(chain,index) is False:
					passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				if passesDefaultSelectionMuTau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesSUSYBBExtraSelectionMuTau(chain,index) is False:
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
				finalWt = signalSUSYweightBB(chain, maxPairTypeAndIndex, Verbose)
				highPtTauWtSYS =  highPtTauSYS(chain, maxPairTypeAndIndex)
				SAMPLE_ADD = getSAMPLE_ADD(sampleName)
				assert(len(SAMPLE_ADD)>0), " Assert : unknown sample "
				#print maxPairTypeAndIndex
				FillSUSYBB(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,highPtTauWtSYS,histogram_dict,eventVariables['SVFitMass'])


######################
# save filled histograms

WriteEverything()
writeCompFile()
