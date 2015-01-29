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
#  SM Higgs @125


listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_10_1_AWH_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_11_1_uSN_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_12_1_YKk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_13_1_yey_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_14_1_RPX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_15_1_t43_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_16_1_Or9_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_17_1_VZC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_18_1_rti_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_19_1_cIv_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_1_1_ir0_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_20_1_G7o_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_21_1_xUw_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_22_1_nZn_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_23_1_lgl_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_24_1_W7x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_25_1_ctf_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_26_1_xKK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_2_1_WNV_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_3_1_C8L_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_4_1_cQ5_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_5_1_mur_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_6_1_I5v_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_7_1_8kG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_8_1_Gel_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/GluGluToHToTauTauM125_FLATv9Xntup/FlatTuple_9_1_MkV_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_10_1_haX_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_11_1_T7I_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_12_1_k2a_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_13_1_vQT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_14_1_xN6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_15_1_v1x_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_16_1_E4l_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_17_1_9t6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_18_1_9N4_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_19_1_eCM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_1_1_gzC_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_20_1_7dc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_21_1_Zns_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_22_1_mEu_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_23_1_rIt_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_24_1_OsM_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_25_1_yQD_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_26_1_BXS_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_2_1_Qzp_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_3_1_rlA_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_4_1_lZB_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_5_1_pyy_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_6_1_M6H_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_7_1_ZGc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_8_1_QUZ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/VBFHToTauTauM125_FLATv9Xntup/FlatTuple_9_1_50P_skimmed.root')

listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_10_1_Lmh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_11_1_DJK_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_12_1_lUk_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_13_1_pWJ_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_14_1_E3w_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_15_1_apO_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_16_1_Eib_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_17_1_XS1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_18_1_Qh6_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_19_1_UiL_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_1_1_1iP_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_20_1_9ms_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_21_1_UGR_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_22_1_0mW_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_23_1_9eF_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_24_1_9E1_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_25_1_ezG_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_26_1_DLc_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_2_1_lzh_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_3_1_S9O_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_4_1_yIT_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_5_1_yII_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_6_1_5Un_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_7_1_wjb_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_8_1_ELd_skimmed.root')
listOfFiles.append('/uscms/home/shalhout/no_backup/NEWSKIMV9X/WHZHTTHHToTauTauM125_FLATv9Xntup/FlatTuple_9_1_awc_skimmed.root')

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
					FILLsm_QQHorVH(maxPairTypeAndIndex,SAMPLE_ADD,wt,histogram_dict,eventVariables['SVFitMass'])


				elif SAMPLE_ADD == '_VH_SM125_':
					wt = 1.0
					CROSSXBR = ((0.69669 + 0.3943 + 0.1302) * 0.0632)
					wt = getWeightFor_XSM125(chain, maxPairTypeAndIndex, Verbose, CROSSXBR)
					FILLsm_QQHorVH(maxPairTypeAndIndex,SAMPLE_ADD,wt,histogram_dict,eventVariables['SVFitMass'])


				elif SAMPLE_ADD == '_ggH_SM125_':
					wt = 1.0
					CROSSXBR = (19.52 * 0.0632)
					wt = getWeightFor_XSM125(chain, maxPairTypeAndIndex, Verbose, CROSSXBR)					
					FILLsm_GluGluH125(maxPairTypeAndIndex,SAMPLE_ADD,wt,histogram_dict,eventVariables['SVFitMass'])






######################
# save filled histograms

WriteEverything()
writeCompFile()
