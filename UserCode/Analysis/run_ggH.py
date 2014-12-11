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
listOfFiles.append('./HOLDER/SUSYGluGlu350.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_26_1_IDA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_1_1_BkO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_3_1_2pB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_6_1_XB1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_5_1_0J2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_4_1_rlo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_2_1_H35_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_10_1_1HY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_8_1_vvS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_14_1_XTp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_9_1_Sm5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_20_1_eJL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_16_1_q0b_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_13_1_MQ6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_19_1_9Z8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_18_1_4Vv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_15_1_kC9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_24_1_3Bc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_25_1_iWJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_21_1_F3C_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_23_1_w2Q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_7_1_LVl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_17_1_geR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_22_1_20Y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_12_1_4I0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM1000_v9FlatTuple/FlatTuple_11_1_XlB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_3_1_v8f_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_7_1_sFq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_2_1_Nts_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_5_1_SdW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_10_1_jjH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_1_1_7ZA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_11_1_G63_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_9_1_TGW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_14_1_G6R_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_12_1_9yr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_26_1_i9p_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_15_1_p7b_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_4_1_ZPC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_18_1_Wdx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_8_1_egz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_21_1_Brt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_22_1_ABz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_20_1_R2F_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_24_1_vm6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_16_1_oue_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_19_1_0ZQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_23_1_JKN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_25_1_3ZC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_13_1_FzD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_17_1_kza_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM100_v9FlatTuple/FlatTuple_6_1_Tff_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_10_1_azE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_11_1_FsK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_5_1_WZR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_26_1_86u_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_3_1_ULZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_13_1_iG8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_16_1_S3X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_12_1_fxm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_6_1_oZm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_17_1_XPj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_8_1_S00_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_14_1_KHQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_25_1_5u3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_24_1_XGW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_7_1_H1Z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_19_1_erp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_23_1_TbD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_9_1_uvw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_18_1_Oky_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_21_1_14D_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_20_1_QMH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_15_1_Yt8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_2_1_o3J_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_1_1_TBB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_22_1_umz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM110_v9FlatTuple/FlatTuple_4_1_YGx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_4_1_0OW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_1_1_xwb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_3_1_Qkk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_13_1_sc4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_5_1_KIm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_9_1_ek1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_10_1_ukO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_24_1_GmA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_8_1_40G_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_12_1_Ug3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_19_1_6SP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_6_1_aq6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_22_1_ttZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_15_1_nEB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_20_1_LLp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_2_1_9At_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_11_1_5q7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_18_1_o9s_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_23_1_jiX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_17_1_Hwf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_21_1_jBY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_7_1_r4p_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_14_1_kFf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_16_1_Ha8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_25_1_XLI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM120_v9FlatTuple/FlatTuple_26_1_wJy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_10_1_Q8V_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_24_1_wdj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_26_1_zaD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_25_1_bFa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_4_1_A38_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_1_1_yD3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_6_1_DDd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_19_1_ea3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_18_1_Jna_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_9_1_jgk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_23_1_n7p_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_20_1_rag_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_16_1_R6g_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_7_1_1p0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_13_1_RmV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_21_1_VH7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_15_1_Qcw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_17_1_kQR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_22_1_gDS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_14_1_lv8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_5_1_Uj7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_3_1_fdk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_12_1_QQp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_11_1_6K9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_2_1_pV1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM130_v9FlatTuple/FlatTuple_8_1_Npk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_3_1_Lpp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_4_1_DeY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_5_1_7XM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_26_1_4CS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_1_1_XA3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_2_1_Mlv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_9_1_ZcD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_10_1_nHo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_18_1_gYU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_14_1_R2D_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_6_1_IpV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_19_1_xUv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_17_1_xYK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_12_1_Bsx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_23_1_pek_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_15_1_PGP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_8_1_UXl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_24_1_sWY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_25_1_Gp5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_16_1_imT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_22_1_IjA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_21_1_gjc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_13_1_Pm2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_20_1_oYo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_11_1_7JK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM140_v9FlatTuple/FlatTuple_7_1_JxX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_26_1_EGn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_7_1_G27_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_1_1_IQm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_26_1_wdL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_16_1_yQf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_18_1_MH4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_13_1_43M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_26_1_uSl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_2_1_Z7V_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_8_1_jV9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_7_1_IEf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_25_1_SEk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_6_1_lCE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_1_1_lay_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_19_1_Abp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_5_1_uMH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_16_1_tKd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_7_1_ja3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_3_1_hBw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_10_1_Nel_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_4_1_sU2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_24_1_o4P_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_4_1_aP3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_9_1_kay_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_8_1_iIA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_18_1_YHT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_13_1_nx3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_19_1_i7J_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_21_1_AME_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_14_1_bxm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_5_1_QYc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_11_1_Q1Q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_21_1_ZJF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_17_1_jKS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_12_1_inA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_12_1_21l_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_23_1_ys0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_22_1_p9F_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_9_1_8Su_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_25_1_GDL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_11_1_Jyx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_22_1_UrE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_2_1_yD8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_15_1_OSX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_24_1_wWS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_23_1_pl7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_6_1_dO1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_17_1_oSd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_21_1_BFC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_20_1_qih_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_11_1_36F_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_4_1_LL3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_10_1_tvf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_14_1_i87_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM800_v9FlatTuple/FlatTuple_3_1_rPX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_6_1_FA2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_7_1_rjS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_14_1_vZ6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_18_1_nwQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_26_1_w5X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_8_1_Ih0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_1_1_p49_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_16_1_sF4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_5_1_uuI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_22_1_5UW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_2_1_Ste_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_11_1_LHy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_6_1_lj3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_12_1_tt9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_17_1_KtI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_15_1_fLc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_21_1_yhA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_15_1_Gbx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_20_1_zxt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_2_1_Py6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_23_1_0yI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_22_1_Nsj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_20_1_ZUW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_13_1_WS9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_4_1_4OI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_16_1_5d8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM160_v9FlatTuple/FlatTuple_12_1_hmx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_25_1_K9a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_10_1_ar6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_1_1_gcA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_3_1_ox6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_19_1_YYh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_9_1_Jlw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_24_1_bLh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_26_1_byG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM80_v9FlatTuple/FlatTuple_14_1_TPb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_26_1_RM0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_1_1_QHM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_3_1_SYB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_1_1_Wu0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_2_1_Yab_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_4_1_opP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_8_1_5lC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_3_1_48i_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_8_1_bbo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_23_1_VkV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_7_1_vf8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_5_1_GVZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_15_1_Dq2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_10_1_4NF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_11_1_E1d_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_5_1_QBI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_5_1_EZP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_16_1_ipP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_9_1_t40_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_13_1_Jbm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_12_1_LL7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_20_1_Spt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_9_1_R0I_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_14_1_n1C_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_10_1_z6L_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_17_1_OM9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_19_1_P6l_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_21_1_nat_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_15_1_MHN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_17_1_qHk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_11_1_BA0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_14_1_bqu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_24_1_ORN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_23_1_FYs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_8_1_Ul7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_18_1_chc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_19_1_i8t_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_20_1_EcU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_22_1_Qo4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_2_1_znS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_6_1_AE4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_9_1_ziU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_17_1_V5C_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_4_1_3ZC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM900_v9FlatTuple/FlatTuple_25_1_I3V_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_24_1_FKO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_13_1_f4L_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_19_1_mkF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_18_1_Vhr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_20_1_mWb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_21_1_TOf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_18_1_bEZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_5_1_0uP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_23_1_wsI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_26_1_rDm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_6_1_cpJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_18_1_KfY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_7_1_0N4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_22_1_POs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_22_1_uKo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_23_1_fWn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_8_1_0gT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_24_1_AAk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_12_1_S2l_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_12_1_Ns4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_24_1_8nb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_11_1_Z2l_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_4_1_VAP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_21_1_MSv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_16_1_657_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_15_1_APU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_2_1_h1P_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_7_1_ALa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_25_1_1Bj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_25_1_Gye_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_9_1_FPt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_13_1_ccA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_10_1_yoo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_25_1_J9i_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_14_1_f0I_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_3_1_CRf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_1_1_gf8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_20_1_pLE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_16_1_vca_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM90_v9FlatTuple/FlatTuple_17_1_7m4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_10_1_2kM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_19_1_Qft_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_13_1_tzF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_3_1_hdM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM400_v9FlatTuple/FlatTuple_15_1_dtV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM180_v9FlatTuple/FlatTuple_6_1_9HP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_1_1_0j9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_26_1_RtL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_26_1_OzU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_3_1_FBF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_2_1_aI9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_20_1_vXc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_22_1_Wjx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_3_1_QEk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_13_1_TeE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_1_1_zuT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_25_1_TNE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_19_1_c4r_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_4_1_CIV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_8_1_xB5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_5_1_zOo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_7_1_IQP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_17_1_4RL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_16_1_T3C_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_5_1_gqZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_10_1_iFH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_12_1_08l_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_9_1_e25_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_7_1_h9R_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_16_1_QY1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_18_1_iMF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_15_1_VSE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_25_1_W9z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_23_1_E3V_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_15_1_P53_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_6_1_9v9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_11_1_Sxk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_20_1_VCu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_4_1_hUQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_21_1_2Iq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_14_1_L9j_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_24_1_7WN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_23_1_3ix_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_2_1_42k_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_21_1_I06_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_14_1_Y8h_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM200_v9FlatTuple/FlatTuple_12_1_ltt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_6_1_kTq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_24_1_YPx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_1_1_8Aa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_3_1_YF9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_11_1_oeh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_5_1_8R8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_10_1_xJz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_2_1_PI5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_12_1_3wO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_8_1_WgL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_10_1_Vtu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_19_1_UdI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_16_1_S6Q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_13_1_orx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_22_1_Lt4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_9_1_s08_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_18_1_8nc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_17_1_woa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_17_1_WZC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_20_1_ESu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_24_1_4EU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_9_1_DUR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_22_1_toA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM450_v9FlatTuple/FlatTuple_13_1_14O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_14_1_8ID_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_6_1_JDX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_1_1_dRK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_25_1_Msh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_26_1_gaX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_23_1_LbN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_11_1_9XJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_19_1_zcO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_7_1_ZYW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_15_1_UPB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_11_1_nFu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_12_1_Rmw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_7_1_Klo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_22_1_HSp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_4_1_hcv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_17_1_Y9e_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_18_1_CqG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_21_1_7pJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_21_1_wxM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_10_1_G6E_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM250_v9FlatTuple/FlatTuple_8_1_BLA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_26_1_ttG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_19_1_Kcw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_3_1_tW0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_8_1_h7a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_9_1_9AU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_25_1_SPW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_13_1_8bw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_16_1_gIn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_10_1_fB9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_13_1_dLD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_1_1_CfB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_15_1_72V_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_4_1_MPJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_6_1_ncv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_2_1_s5T_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_19_1_N7R_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_4_1_grw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_5_1_6VH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_20_1_3fi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_14_1_Pme_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_14_1_ViY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_12_1_y8U_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_24_1_USJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_23_1_owf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_5_1_P1W_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_7_1_Yhr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_25_1_ein_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_9_1_ZAs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_24_1_0Nr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_18_1_jKX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_15_1_ocJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_23_1_ViN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_16_1_KJy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_2_1_ogy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_20_1_bpK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM500_v9FlatTuple/FlatTuple_3_1_vmb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_21_1_l3Y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_26_1_xIP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_11_1_wVL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_23_1_q2H_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_24_1_rZM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_17_1_Bgi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_5_1_C5C_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_7_1_ZYu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_22_1_6WR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_2_1_EG8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_18_1_s9J_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_1_1_vQS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_3_1_IUo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_6_1_SKw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_13_1_Fw3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM300_v9FlatTuple/FlatTuple_8_1_L7n_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_12_1_BXE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_14_1_COA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_16_1_CDe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_3_1_uUz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_6_1_7uK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_12_1_I94_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_8_1_1ZY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_19_1_Urb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_1_1_5t4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_15_1_Y7p_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_2_1_gPn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_26_1_dtw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_25_1_26y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_20_1_8Cg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_8_1_oNy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_22_1_Lh7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_6_1_MH1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_4_1_Tpm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_17_1_juJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_9_1_I6O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_18_1_qbo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_17_1_bGJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_10_1_PaT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_4_1_7nU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_21_1_BId_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_9_1_Yph_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_23_1_2Jq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM600_v9FlatTuple/FlatTuple_11_1_vLH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_14_1_MAd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_26_1_usr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_1_1_bay_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_18_1_FJ3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_25_1_lOT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_16_1_XcV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_5_1_RRU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_9_1_db7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_7_1_hyd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_7_1_ydT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_17_1_Rxg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_24_1_Ptk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_18_1_9Yn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_11_1_pcu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_5_1_2wC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_2_1_t5u_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_10_1_LP9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_14_1_nGD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_8_1_L9D_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_19_1_KOX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_21_1_6Tz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_10_1_x4Y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_21_1_bMF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_13_1_Caf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_22_1_Pbn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_15_1_A97_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_19_1_40s_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_25_1_egt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_12_1_JBR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_23_1_CIQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_15_1_paG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_20_1_2gD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_16_1_wtp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_20_1_5BN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_22_1_dxR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_13_1_Rml_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_4_1_OCY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_6_1_qIK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM350_v9FlatTuple/FlatTuple_11_1_G6z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_3_1_GSL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/SUSYGluGluToHToTauTauM700_v9FlatTuple/FlatTuple_24_1_1xS_skimmed.root')


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
