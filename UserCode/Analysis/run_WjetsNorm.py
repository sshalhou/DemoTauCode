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

#listOfFiles.append('./HOLDER/DATAA_partial_FlatTuple_1_1_I5s.root')




###########
# wjets

listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/wjets/FlatTuple_SZS_W1jetsLNuV19v1_v6ntup.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/wjets/FlatTuple_SZS_W1jetsLNuV7Av1_v6ntup.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/wjets/FlatTuple_SZS_W2jetsLNuV19v1_v6ntup.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/wjets/FlatTuple_SZS_W2jetsLNuV7Av1_v6ntup.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/wjets/FlatTuple_SZS_W3jetsLNuV19v1_v6ntup.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/wjets/FlatTuple_SZS_W3jetsLNuV7Av1_v6ntup.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/wjets/FlatTuple_SZS_W4jetsLNuV1_v6ntup.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/wjets/FlatTuple_SZS_WjetsLNuV1_v6ntup.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/wjets/FlatTuple_SZS_WjetsLNuV2_v6ntup.root')


############
# DATA

listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_1_1_I5s.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_1_1_KIQ.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_1_1_Tj1.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_1_1_tJt.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_2_1_0S8.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_2_1_JIl.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_2_1_emp.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_2_1_fvG.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_3_1_PuD.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_3_1_ROv.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_3_1_tTy.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_4_1_Qcy.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_4_1_Yg5.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_4_1_kxi.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_5_1_2ss.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_5_1_9SD.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_5_1_rtZ.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_6_1_JRW.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_6_1_MAi.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_6_1_l5M.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_7_1_RoG.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_7_1_tGi.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_8_1_E1H.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_8_1_jWE.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_9_1_6jK.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/data/FlatTuple_RecoveredJobs.root')


###########
# DY

listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_10_1_2Ih.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_11_1_5YE.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_12_1_tLc.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_13_1_2wW.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_14_1_4b6.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_15_1_kx8.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_16_1_UI2.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_17_1_KHg.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_18_1_hKK.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_19_1_XMj.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_1_1_blg.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_2_1_XEG.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_3_1_O9X.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_4_1_4xG.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_5_1_rCz.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_6_1_XMN.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_7_1_I78.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_8_1_pk7.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY1JetsToLL_V7FlatTupleEx/FlatTuple_9_1_8X3.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_10_1_9c7.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_11_1_z0I.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_12_1_ZGr.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_13_1_XGW.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_14_1_FWE.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_15_1_byZ.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_16_1_tUv.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_17_1_swU.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_18_1_NUu.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_1_1_ClI.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_2_1_G54.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_3_1_tPo.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_4_1_ley.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_5_1_bfs.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_6_1_ox0.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_7_1_INJ.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_8_1_QtR.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY2JetsToLL_V7FlatTupleEx/FlatTuple_9_1_34f.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY3JetsToLL_V7FlatTupleEx/FlatTuple_10_1_ge0.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY3JetsToLL_V7FlatTupleEx/FlatTuple_11_1_sgb.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY3JetsToLL_V7FlatTupleEx/FlatTuple_12_1_qx4.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY3JetsToLL_V7FlatTupleEx/FlatTuple_13_1_IOH.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY3JetsToLL_V7FlatTupleEx/FlatTuple_14_1_vEj.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY3JetsToLL_V7FlatTupleEx/FlatTuple_15_1_YGT.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY3JetsToLL_V7FlatTupleEx/FlatTuple_16_1_62i.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY3JetsToLL_V7FlatTupleEx/FlatTuple_1_1_0Xm.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY3JetsToLL_V7FlatTupleEx/FlatTuple_2_1_7oh.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY3JetsToLL_V7FlatTupleEx/FlatTuple_3_1_8z5.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY3JetsToLL_V7FlatTupleEx/FlatTuple_4_1_iAU.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY3JetsToLL_V7FlatTupleEx/FlatTuple_5_1_iFj.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY3JetsToLL_V7FlatTupleEx/FlatTuple_6_1_LUk.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY3JetsToLL_V7FlatTupleEx/FlatTuple_7_1_jUe.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY3JetsToLL_V7FlatTupleEx/FlatTuple_8_1_WlK.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY3JetsToLL_V7FlatTupleEx/FlatTuple_9_1_Z5R.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY4JetsToLL_V7FlatTupleEx/FlatTuple_10_1_NgC.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY4JetsToLL_V7FlatTupleEx/FlatTuple_11_1_T5r.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY4JetsToLL_V7FlatTupleEx/FlatTuple_12_1_7ed.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY4JetsToLL_V7FlatTupleEx/FlatTuple_13_1_BgD.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY4JetsToLL_V7FlatTupleEx/FlatTuple_14_1_rDN.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY4JetsToLL_V7FlatTupleEx/FlatTuple_15_1_U5j.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY4JetsToLL_V7FlatTupleEx/FlatTuple_16_1_tY0.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY4JetsToLL_V7FlatTupleEx/FlatTuple_1_1_qtj.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY4JetsToLL_V7FlatTupleEx/FlatTuple_2_1_Wo3.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY4JetsToLL_V7FlatTupleEx/FlatTuple_3_1_fuh.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY4JetsToLL_V7FlatTupleEx/FlatTuple_4_1_3ph.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY4JetsToLL_V7FlatTupleEx/FlatTuple_5_1_3nZ.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY4JetsToLL_V7FlatTupleEx/FlatTuple_6_1_sMS.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY4JetsToLL_V7FlatTupleEx/FlatTuple_7_1_BnP.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY4JetsToLL_V7FlatTupleEx/FlatTuple_8_1_8k8.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DY4JetsToLL_V7FlatTupleEx/FlatTuple_9_1_Kqb.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_10_1_0dZ.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_11_1_Fy8.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_12_1_Cyl.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_13_1_gHI.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_14_1_7JL.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_15_1_mSd.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_16_1_STt.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_17_1_aiY.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_18_1_nUb.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_1_1_lEU.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_2_1_nrG.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_3_1_LcN.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_4_1_LO1.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_5_1_GQM.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_6_1_wqp.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_7_1_ubt.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_8_1_awC.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/dy/DYJetsToLLTauSpin_V7FlatTupleEx/FlatTuple_9_1_reh.root')

##########
# tt/single t

listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_10_1_a3z.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_11_1_xHU.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_12_1_t6m.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_13_1_a5v.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_14_1_HYC.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_15_1_MkF.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_16_1_j8s.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_17_1_anL.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_18_1_UuA.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_19_1_TZ5.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_1_1_4Ih.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_20_1_g3o.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_21_1_px3.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_22_1_gur.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_2_1_nUp.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_3_1_5bg.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_4_1_scU.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_5_1_p9q.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_6_1_9lb.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_7_1_QM6.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_8_1_T94.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_FullLeptMGDecaysMC_V6FlatTuple/FlatTuple_9_1_7QY.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_10_1_pjM.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_11_1_85G.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_12_1_hzL.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_13_1_Ziy.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_14_1_WGW.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_15_1_ync.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_16_1_77T.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_17_1_KvA.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_18_1_1n9.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_19_1_9rL.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_1_1_ZRE.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_2_1_8G7.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_3_1_x8o.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_4_1_0oK.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_5_1_Ofm.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_6_1_tr1.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_7_1_5KO.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_8_1_2eX.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_HadronicMGDecaysMC_V6FlatTuple/FlatTuple_9_1_97A.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_10_1_vL6.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_11_1_QHF.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_12_1_SIh.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_13_1_01R.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_14_1_Y6O.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_15_1_bP2.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_16_1_tlP.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_17_1_cc5.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_18_1_fhm.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_19_1_SNS.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_1_1_Z4r.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_20_1_1i9.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_21_1_13s.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_22_1_V2T.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_23_1_p5o.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_2_1_RA8.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_3_1_APi.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_4_1_1he.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_5_1_nRZ.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_6_1_cq6.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_7_1_6lf.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_8_1_ndY.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/TTJets_SemiLeptMGDecaysMC_V6FlatTuple/FlatTuple_9_1_hXo.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/T_tWchannelDR_V6FlatTuple/FlatTuple_10_1_anP.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/T_tWchannelDR_V6FlatTuple/FlatTuple_11_1_y8K.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/T_tWchannelDR_V6FlatTuple/FlatTuple_12_1_cbh.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/T_tWchannelDR_V6FlatTuple/FlatTuple_13_1_AUB.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/T_tWchannelDR_V6FlatTuple/FlatTuple_14_1_XPW.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/T_tWchannelDR_V6FlatTuple/FlatTuple_15_1_8XI.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/T_tWchannelDR_V6FlatTuple/FlatTuple_16_1_9Cp.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/T_tWchannelDR_V6FlatTuple/FlatTuple_1_1_02Z.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/T_tWchannelDR_V6FlatTuple/FlatTuple_2_1_TkZ.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/T_tWchannelDR_V6FlatTuple/FlatTuple_3_1_Gxa.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/T_tWchannelDR_V6FlatTuple/FlatTuple_4_1_Tm1.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/T_tWchannelDR_V6FlatTuple/FlatTuple_5_1_2Ny.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/T_tWchannelDR_V6FlatTuple/FlatTuple_6_1_jhY.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/T_tWchannelDR_V6FlatTuple/FlatTuple_7_1_b4K.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/T_tWchannelDR_V6FlatTuple/FlatTuple_8_1_MH2.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/T_tWchannelDR_V6FlatTuple/FlatTuple_9_1_J5h.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_10_1_Rvw.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_11_1_ywq.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_12_1_zJM.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_13_1_x5D.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_14_1_MBC.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_15_1_UKz.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_16_1_twl.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_1_1_xAj.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_2_1_DPy.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_3_1_OA0.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_4_1_Owt.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_5_1_Mvc.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_6_1_lwq.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_7_1_ecE.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_8_1_N6d.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/tt_and_singlet/Tbar_tWchannelDR_V6FlatTuple/FlatTuple_9_1_xDJ.root')

###########
# vv

listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_10_1_SAl.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_11_1_mxQ.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_12_1_0ic.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_13_1_hji.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_14_1_IIO.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_15_1_3pv.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_16_1_0zm.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_1_1_y4A.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_2_1_YKa.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_3_1_VuT.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_4_1_gtZ.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_5_1_RMB.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_6_1_PDH.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_7_1_W3f.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_8_1_Dxs.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WWJetsTo2L2Nu_V6FlatTuple/FlatTuple_9_1_qLn.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_10_1_syu.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_11_1_dDq.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_12_1_Whv.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_13_1_Zae.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_14_1_0Hf.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_15_1_nB5.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_16_1_cfL.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_1_1_OSm.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_2_1_pWK.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_3_1_c9j.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_4_1_HYx.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_5_1_tf7.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_6_1_is7.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_7_1_1yC.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_8_1_4o5.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo2L2Q_V6FlatTuple/FlatTuple_9_1_x3G.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo3LNu_V6FlatTuple/FlatTuple_10_1_pHm.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo3LNu_V6FlatTuple/FlatTuple_11_1_ZQH.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo3LNu_V6FlatTuple/FlatTuple_12_1_ZXw.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo3LNu_V6FlatTuple/FlatTuple_13_1_XGl.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo3LNu_V6FlatTuple/FlatTuple_14_1_1zC.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo3LNu_V6FlatTuple/FlatTuple_15_1_hOE.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo3LNu_V6FlatTuple/FlatTuple_1_1_YxK.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo3LNu_V6FlatTuple/FlatTuple_2_1_4uO.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo3LNu_V6FlatTuple/FlatTuple_3_1_SXb.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo3LNu_V6FlatTuple/FlatTuple_4_1_Voj.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo3LNu_V6FlatTuple/FlatTuple_5_1_WZD.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo3LNu_V6FlatTuple/FlatTuple_6_1_2gA.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo3LNu_V6FlatTuple/FlatTuple_7_1_dFo.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo3LNu_V6FlatTuple/FlatTuple_8_1_J04.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/WZJetsTo3LNu_V6FlatTuple/FlatTuple_9_1_0Ap.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Nu_V6FlatTuple/FlatTuple_10_1_sLo.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Nu_V6FlatTuple/FlatTuple_11_1_2rx.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Nu_V6FlatTuple/FlatTuple_12_1_oQM.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Nu_V6FlatTuple/FlatTuple_13_1_iEz.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Nu_V6FlatTuple/FlatTuple_14_1_5Iz.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Nu_V6FlatTuple/FlatTuple_15_1_jEa.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Nu_V6FlatTuple/FlatTuple_16_1_AHM.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Nu_V6FlatTuple/FlatTuple_1_1_nka.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Nu_V6FlatTuple/FlatTuple_2_1_1Bf.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Nu_V6FlatTuple/FlatTuple_3_1_jsu.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Nu_V6FlatTuple/FlatTuple_4_1_DOv.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Nu_V6FlatTuple/FlatTuple_5_1_lDE.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Nu_V6FlatTuple/FlatTuple_6_1_Qsa.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Nu_V6FlatTuple/FlatTuple_7_1_Sb4.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Nu_V6FlatTuple/FlatTuple_8_1_UxH.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Nu_V6FlatTuple/FlatTuple_9_1_rNi.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_10_1_gV8.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_11_1_YYF.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_12_1_mXF.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_13_1_FIQ.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_14_1_b9I.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_15_1_Oij.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_16_1_KVD.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_1_1_80G.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_2_1_aBp.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_3_1_7fL.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_4_1_VGF.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_5_1_edl.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_6_1_TbJ.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_7_1_s8b.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_8_1_Mds.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo2L2Q_V6FlatTuple/FlatTuple_9_1_Hga.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo4L_V6FlatTuple/FlatTuple_10_1_eWh.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo4L_V6FlatTuple/FlatTuple_11_1_J8X.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo4L_V6FlatTuple/FlatTuple_12_1_HGJ.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo4L_V6FlatTuple/FlatTuple_13_1_XsZ.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo4L_V6FlatTuple/FlatTuple_14_1_aGK.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo4L_V6FlatTuple/FlatTuple_15_1_xxG.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo4L_V6FlatTuple/FlatTuple_16_1_jKf.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo4L_V6FlatTuple/FlatTuple_1_1_18n.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo4L_V6FlatTuple/FlatTuple_2_1_9cY.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo4L_V6FlatTuple/FlatTuple_3_1_LLc.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo4L_V6FlatTuple/FlatTuple_4_1_ug4.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo4L_V6FlatTuple/FlatTuple_5_1_gXo.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo4L_V6FlatTuple/FlatTuple_6_1_NIN.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo4L_V6FlatTuple/FlatTuple_7_1_Iab.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo4L_V6FlatTuple/FlatTuple_8_1_kZ7.root')
listOfFiles.append('/uscms_data/d3/shalhout/TEMP_FILEHOLDER/vv/ZZJetsTo4L_V6FlatTuple/FlatTuple_9_1_LNX.root')


#listOfFiles.append('./HOLDER/FlatTuple_SZS_W1jetsLNuV19v1_v6ntup.root')
#listOfFiles.append('./HOLDER/TTSemiFlatTuple_21_1_13s.root')
#listOfFiles.append('./HOLDER/WZJetsFlatTuple_3_1_c9j.root')
#listOfFiles.append('./HOLDER/DY2JetsFlatTuple_5_1_bfs.root')
#listOfFiles.append('./HOLDER/DYSpinOffFlatTuple_8_1_awC.root')
#listOfFiles.append('./HOLDER/DATAA_partial_FlatTuple_1_1_I5s.root')

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
				if passesHighMtSelectionETau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				if passesHighMtSelectionMuTau(chain,index,UseNewTriggers,Verbose) is False:
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
				if SAMPLE_ADD == '_data_obs_':
					FillObsDATA(maxPairTypeAndIndex,SAMPLE_ADD,
										histogram_dict,
										eventVariables['SVFitMass'])
				elif SAMPLE_ADD == '_DYTauPolOff_':
					classification = classifyZDecay(chain,maxPairTypeAndIndex)
					print classification
					wt = 1.0
					if classification == '_ZTT_':
						wt = getWeightForTauPolOffDY(chain,maxPairTypeAndIndex,Verbose)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					elif classification == '_ZL_':
						wt = getWeightForTauPolOffDY(chain,maxPairTypeAndIndex,Verbose)
						# contains an internal check for e->tau
						wt = wt * getFakeZeeWeight(chain,maxPairTypeAndIndex)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					elif classification == '_ZJ_':
						wt = getWeightForTauPolOffDY(chain,maxPairTypeAndIndex,Verbose)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
				elif (SAMPLE_ADD=='_DY1Jet_' or
				      SAMPLE_ADD=='_DY2Jet_' or
					  SAMPLE_ADD=='_DY3Jet_' or
					  SAMPLE_ADD=='_DY4Jet_'):
					classification = classifyZDecay(chain,maxPairTypeAndIndex)
					print classification
					wt = 1.0
					if classification == '_ZTT_':
						wt = getWeightForRegularDY(chain,maxPairTypeAndIndex,Verbose)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					elif classification == '_ZL_':
						wt = getWeightForRegularDY(chain,maxPairTypeAndIndex,Verbose)
						# contains an internal check for e->tau
						wt = wt * getFakeZeeWeight(chain,maxPairTypeAndIndex)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					elif classification == '_ZJ_':
						wt = getWeightForRegularDY(chain,maxPairTypeAndIndex,Verbose)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
				elif (SAMPLE_ADD=='_ZZJetsTo4L_' or
					  SAMPLE_ADD=='_ZZJetsTo2L2Nu_' or
					  SAMPLE_ADD=='_ZZJetsTo2L2Q_' or
					  SAMPLE_ADD=='_WWJetsTo2L2Nu_' or
					  SAMPLE_ADD=='_WZJetsTo2L2Q_' or
					  SAMPLE_ADD=='_WZJetsTo3LNu_'):
					classification = '_VV_'
					wt = 1.0
					wt = getWeightForVV(chain,maxPairTypeAndIndex,Verbose)
					Fill_VV(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
				elif (SAMPLE_ADD=='_TTJetsFullLept_' or
					  SAMPLE_ADD=='_TTJetsSemiLept_' or
					  SAMPLE_ADD=='_TTJetsHadronic_' or
					  SAMPLE_ADD=='_SingleTopBar_' or
					  SAMPLE_ADD=='_SingleTop_'):
					classification = '_TT_'
					wt_dict = {}
					wt_dict['topPtDown'] = 1.0
					wt_dict['topPtNominal'] = 1.0
					wt_dict['topPtUp'] = 1.0

					getWeightForTTmc(chain,maxPairTypeAndIndex,wt_dict,Verbose)

					# pt reweight not applied to singleTop
					# note: the down variant has no pt weight applied
					if SAMPLE_ADD=='_SingleTopBar_' or SAMPLE_ADD=='_SingleTop_':
						wt_dict['topPtNominal']  = wt_dict['topPtDown']
						wt_dict['topPtUp'] = wt_dict['topPtDown']
					Fill_TTbarAndSingleTopMC(maxPairTypeAndIndex,classification,wt_dict,histogram_dict,eventVariables['SVFitMass'])


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
