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


listOfFiles.append('./HOLDER/TTFullFlatTuple_5_1_o1S_skimmed.root')
listOfFiles.append('./HOLDER/ZZJets2L2QFlatTuple_10_1_Nh9_skimmed.root')
listOfFiles.append('./HOLDER/T_tWFlatTuple_16_1_odt_skimmed.root')
listOfFiles.append('./HOLDER/VBF125.root')
listOfFiles.append('./HOLDER/WH125.root')
listOfFiles.append('./HOLDER/GGH125.root')

###########
#  SM Higgs @125

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_1_1_CYf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_26_1_IdJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_7_1_KTS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_4_1_DSj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_22_1_1Nq_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_5_1_u2d_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_20_1_J6v_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_11_1_1qY_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_18_1_B0p_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_6_1_1Gn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_14_1_hy9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_15_1_hyB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_10_1_2Gd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_16_1_ObF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_19_1_7Wu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_2_1_J1u_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_9_1_Wze_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_21_1_bnI_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_8_1_Q0A_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_12_1_lsW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_13_1_rp0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_25_1_tLC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_24_1_G3X_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_3_1_6Pj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_17_1_aaJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_23_1_C6q_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_6_1_ltk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_18_1_soR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_20_1_udB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_19_1_AWl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_3_1_1LP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_17_1_UNn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_8_1_ohw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_1_1_vEF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_7_1_IFy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_14_1_pUy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_21_1_l8M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_15_1_RYl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_11_1_aUo_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_26_1_08E_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_12_1_m50_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_16_1_vpA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_13_1_Shm_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_4_1_O69_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_9_1_aIv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_10_1_XHz_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_5_1_Hes_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_23_1_fxr_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_24_1_l7m_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_22_1_72a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_2_1_xDc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/GluGluToHToTauTauM125_v9FlatTuple/FlatTuple_25_1_Qty_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_2_1_blX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_3_1_bF3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_1_1_kSj_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_14_1_3M4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_5_1_kWy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_6_1_Vca_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_15_1_ngi_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_4_1_qGJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_16_1_JH4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_7_1_YSX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_8_1_hDp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_9_1_i2W_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_13_1_U5u_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_11_1_Ulu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_18_1_SbB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_20_1_ktP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_10_1_Ax3_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_21_1_Osu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_19_1_13Z_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_22_1_IgL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_12_1_OPO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_17_1_gib_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_26_1_1l7_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_23_1_Ck9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_24_1_69M_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIM/WHZHTTHHToTauTauM125_v9FlatTuple/FlatTuple_25_1_Ski_skimmed.root')

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
					maxPairTypeAndIndex.append(muTauClassification_forQCD(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(chain.NAMEVAR)
					maxPairTypeAndIndex.append(muTauClassificationJECDOWN(chain, maxPairTypeAndIndex[0]))
					maxPairTypeAndIndex.append(muTauClassificationJECUP(chain, maxPairTypeAndIndex[0]))
				if maxPairTypeAndIndex[1] == 'eleTau':
					maxPairTypeAndIndex.append(eTauClassification_forQCD(chain, maxPairTypeAndIndex[0]))
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

				if (SAMPLE_ADD=='_ZZJetsTo4L_' or
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

				elif SAMPLE_ADD == '_qqH_SM125_':
					wt = 1.0
					CROSSXBR = (1.578 * 0.0632)
					wt = getWeightFor_XSM125(chain, maxPairTypeAndIndex, Verbose, CROSSXBR)
					highPtTauWtSYS =  highPtTauSYS(chain, maxPairTypeAndIndex)
					FILLsm_QQHorVH(maxPairTypeAndIndex,SAMPLE_ADD,wt,highPtTauWtSYS,histogram_dict,eventVariables['SVFitMass'])


				elif SAMPLE_ADD == '_VH_SM125_':
					wt = 1.0
					CROSSXBR = ((0.69669 + 0.3943 + 0.1302) * 0.0632)
					wt = getWeightFor_XSM125(chain, maxPairTypeAndIndex, Verbose, CROSSXBR)
					highPtTauWtSYS =  highPtTauSYS(chain, maxPairTypeAndIndex)
					FILLsm_QQHorVH(maxPairTypeAndIndex,SAMPLE_ADD,wt,highPtTauWtSYS,histogram_dict,eventVariables['SVFitMass'])


				elif SAMPLE_ADD == '_ggH_SM125_':
					wt = 1.0
					CROSSXBR = (19.52 * 0.0632)
					wt = getWeightFor_XSM125(chain, maxPairTypeAndIndex, Verbose, CROSSXBR)
					highPtTauWtSYS =  highPtTauSYS(chain, maxPairTypeAndIndex)
					higgsPtWeightSYSdict = {}
					SM125higgsPtWeightSYS(chain, maxPairTypeAndIndex,higgsPtWeightSYSdict)
					#print SAMPLE_ADD, wt, higgsPtWeightSYSdict, highPtTauWtSYS
					# the function for ggH 125 sm will take care of prop. of the higgsPt weight where needed
					FILLsm_GluGluH125(maxPairTypeAndIndex,SAMPLE_ADD,wt,highPtTauWtSYS,higgsPtWeightSYSdict,histogram_dict,eventVariables['SVFitMass'])






######################
# save filled histograms

WriteEverything()
writeCompFile()
