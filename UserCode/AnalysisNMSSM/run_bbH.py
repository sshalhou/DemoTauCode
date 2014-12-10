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
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_10_1_bKI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_11_1_U9N_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_12_1_ICo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_13_1_eeB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_14_1_JWc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_15_1_IDh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_16_1_Krf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_17_1_SoF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_18_1_UFb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_19_1_BMm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_1_1_twT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_20_1_XEz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_21_1_BRV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_22_1_XU7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_23_1_b0N_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_24_1_JNP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_25_1_fZ8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_2_1_0gH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_3_1_LxZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_4_1_msD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_5_1_X2h_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_6_1_KfU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_7_1_nIJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_8_1_OJ5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM1000_v9FlatTuple/FlatTuple_9_1_eQt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_10_1_6KO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_11_1_G2G_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_12_1_yLG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_13_1_JjU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_14_1_CUd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_15_1_ppO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_16_1_aTM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_17_1_3JV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_18_1_Gzg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_19_1_ruZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_1_1_sTy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_20_1_fQz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_21_1_8Fa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_22_1_XKG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_23_1_94Y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_24_1_OSZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_25_1_0ZB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_26_1_qg2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_2_1_z34_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_3_1_NXq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_4_1_rMM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_5_1_4fQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_6_1_zGS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_7_1_TyT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_8_1_9ff_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM100_v9FlatTuple/FlatTuple_9_1_mwF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_10_1_x7Y_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_11_1_4kq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_12_1_gWp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_13_1_Ugl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_14_1_jzz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_15_1_WX4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_16_1_Pl4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_17_1_D2K_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_18_1_Gs4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_19_1_yYu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_1_1_iam_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_20_1_9MO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_21_1_mmi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_22_1_SUS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_23_1_Ars_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_24_1_lQ0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_25_1_CG2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_26_1_DmV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_2_1_vwE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_3_1_1DD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_4_1_Rg9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_5_1_yuV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_6_1_luj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_7_1_9wh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_8_1_7AE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM110_v9FlatTuple/FlatTuple_9_1_2zN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_10_1_2W3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_11_1_jT1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_12_1_HQ8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_13_1_mvy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_14_1_Tkq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_15_1_HNq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_16_1_uHJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_17_1_JTn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_18_1_QaA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_19_1_vGS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_1_1_Mx2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_20_1_t5T_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_21_1_EXU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_22_1_Nf9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_23_1_LWF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_24_1_ICw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_25_1_7T8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_26_1_H11_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_2_1_wbj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_3_1_3nI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_4_1_fU8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_5_1_0k0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_6_1_t9f_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_7_1_UST_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_8_1_izT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM120_v9FlatTuple/FlatTuple_9_1_ZEm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_10_1_Qxa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_11_1_wB8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_12_1_3N0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_13_1_3OS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_14_1_85E_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_15_1_HOs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_16_1_pxx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_17_1_MXj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_18_1_Y3V_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_19_1_y41_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_1_1_HDa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_20_1_txa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_21_1_Cke_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_22_1_X3x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_23_1_ESm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_24_1_WEj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_25_1_iV5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_26_1_FH6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_2_1_bDy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_3_1_LN8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_4_1_xvS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_5_1_cki_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_6_1_dbW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_7_1_hM6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_8_1_vGF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM130_v9FlatTuple/FlatTuple_9_1_Du5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_10_1_UMo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_11_1_mr8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_12_1_Rqk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_13_1_cNW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_14_1_NfZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_15_1_BIp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_16_1_eth_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_17_1_mNR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_18_1_brj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_19_1_JDq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_1_1_GEv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_20_1_aQX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_21_1_RK8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_22_1_WEV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_23_1_UwT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_24_1_M0f_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_25_1_ugA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_26_1_MZc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_2_1_OcL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_3_1_ybC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_4_1_DY4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_5_1_D1E_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_6_1_FsL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_7_1_mjN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_8_1_ebP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM140_v9FlatTuple/FlatTuple_9_1_hdf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_10_1_7me_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_11_1_lFT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_12_1_kdD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_13_1_4mA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_14_1_x5V_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_15_1_UUz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_16_1_2Sc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_17_1_yBz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_18_1_Pwj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_19_1_a10_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_1_1_P1K_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_20_1_YTD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_21_1_jTY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_22_1_aIb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_23_1_Ory_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_24_1_2y9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_25_1_kcw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_26_1_XCd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_2_1_0BB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_3_1_NUn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_4_1_qHe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_5_1_bwt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_6_1_88I_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_7_1_4cr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_8_1_1KY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM160_v9FlatTuple/FlatTuple_9_1_52n_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_10_1_KmX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_11_1_oj5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_12_1_XNc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_13_1_G4e_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_14_1_qH2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_15_1_IHF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_16_1_MSI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_17_1_J4U_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_18_1_5Gs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_19_1_uOx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_1_1_9Rw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_20_1_2uz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_21_1_w22_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_22_1_Sdu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_23_1_yZF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_24_1_d9F_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_25_1_4Ns_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_26_1_idY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_2_1_N0h_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_3_1_A8D_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_4_1_N67_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_5_1_mqn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_6_1_QS7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_7_1_FId_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_8_1_5iJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM180_v9FlatTuple/FlatTuple_9_1_Efq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_10_1_ata_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_11_1_IvL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_12_1_XxO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_13_1_2oI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_14_1_46j_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_15_1_ofa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_16_1_KLw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_17_1_bkt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_18_1_Iwl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_19_1_71f_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_1_1_luZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_20_1_WPL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_21_1_YkU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_22_1_j9D_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_23_1_lCF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_24_1_JK8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_25_1_d5C_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_2_1_zjB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_3_1_h89_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_4_1_u8j_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_5_1_PMv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_6_1_mSL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_7_1_Fti_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_8_1_MGg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM200_v9FlatTuple/FlatTuple_9_1_WP1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_10_1_j41_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_11_1_1la_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_12_1_4FK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_13_1_ppU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_14_1_L3s_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_15_1_o3x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_16_1_yBG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_17_1_ZhA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_18_1_ujU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_19_1_6nw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_1_1_CQO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_20_1_TFP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_21_1_jsN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_22_1_EE5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_23_1_HKB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_24_1_nr8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_25_1_AYq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_26_1_vdO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_2_1_eJb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_3_1_avE_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_4_1_6zK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_5_1_VRT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_6_1_iWD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_7_1_26w_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_8_1_5zB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM250_v9FlatTuple/FlatTuple_9_1_qoq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_10_1_p18_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_11_1_6Yz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_12_1_Xg3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_13_1_RMY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_14_1_dpI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_15_1_Ar2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_16_1_xd0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_17_1_iMH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_18_1_ZD6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_19_1_Wc4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_1_1_U2o_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_20_1_pBa_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_21_1_Iz8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_22_1_rFp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_23_1_0Oj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_24_1_okg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_25_1_oan_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_26_1_Cy9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_2_1_3KB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_3_1_X8X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_4_1_AwV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_5_1_MJk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_6_1_Ah0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_7_1_EmK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_8_1_daI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM300_v9FlatTuple/FlatTuple_9_1_3ts_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_10_1_LGX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_11_1_YTI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_12_1_VL2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_13_1_Qzg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_14_1_cUT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_15_1_B6x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_16_1_PvO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_17_1_qip_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_18_1_hIB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_19_1_V3q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_1_1_CzZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_20_1_v9X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_21_1_1WM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_22_1_Zss_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_23_1_XM6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_24_1_sXY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_25_1_Yap_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_26_1_P2E_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_2_1_2lx_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_3_1_lpg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_4_1_2e2_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_5_1_Dux_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_6_1_MMY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_7_1_Sei_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_8_1_hFR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM400_v9FlatTuple/FlatTuple_9_1_H6a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_10_1_0ya_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_11_1_dSp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_12_1_uik_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_13_1_IbO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_14_1_Hbd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_15_1_bd9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_16_1_Bwt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_17_1_BiW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_18_1_LtV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_19_1_pLe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_1_1_AfR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_20_1_fwe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_21_1_HpY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_22_1_ph0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_23_1_OxW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_24_1_kEb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_25_1_YA8_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_26_1_YMp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_2_1_ree_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_3_1_85u_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_4_1_d6M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_5_1_XMc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_6_1_8Hn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_7_1_duQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_8_1_cZg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM450_v9FlatTuple/FlatTuple_9_1_m53_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_10_1_tgW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_11_1_IHU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_12_1_Bj5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_13_1_NsJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_14_1_0e6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_15_1_2Zp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_16_1_Mnb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_17_1_KaQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_18_1_GVp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_19_1_avP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_1_1_c7G_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_20_1_ARu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_21_1_Zk6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_22_1_9Ne_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_23_1_Kwg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_24_1_2RQ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_25_1_QeC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_26_1_0Wr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_2_1_J8i_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_3_1_EuK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_4_1_bOV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_5_1_J5L_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_6_1_3qr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_7_1_Pso_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_8_1_GF9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM500_v9FlatTuple/FlatTuple_9_1_ceK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_10_1_SQl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_11_1_O5l_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_12_1_YZe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_13_1_CNe_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_14_1_sOA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_15_1_dP1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_16_1_2mS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_17_1_EtS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_18_1_pE1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_19_1_tfs_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_1_1_NkF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_20_1_sEd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_21_1_LEl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_22_1_zko_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_23_1_lSU_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_24_1_kc4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_25_1_kEP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_26_1_6qo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_2_1_ofJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_3_1_J8X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_4_1_2St_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_5_1_aS1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_6_1_Igv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_7_1_8HF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_8_1_IKg_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/TEMP_FILEHOLDER/bbH_v9_skim/SUSYBBHToTauTauM90_v9FlatTuple/FlatTuple_9_1_dq0_skimmed.root')


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
