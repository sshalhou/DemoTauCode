import time
import sys
import os

#################################
# prefix for final root files

PREFIX = 'davis_combined_htt_mssm_'

####################################
# this list distinguishes channels
# these should be contained somewhere in the name
# of your root files

CHANNELS = []
CHANNELS.append('eleTau')
CHANNELS.append('muTau')


####################
# declare the lists

# histograms in the following list will be summed
# without modification (by channel),
# the should have no duplicates or require any scale factors
# scale factors to adjust normalization will be applied later

FOR_UNMODIFIED_ADDITION = []

############
# some of the signals must be pulled from
# old files as the trigger fix jobs
# are not yet done

OLD_BAD_SIGNALS = []

##############
# for QCD normalization

FOR_QCD_NORM = []

###############
# for ZTT normalization

FOR_ZTT_NORM = []

###############
# for embedded ttbar subtraction
# note these should have tt events
# filling the _ZTT_ templates

FOR_TTEMBEDDED_SUB = []

##########
# for tt embedded no mt cut

FOR_TTEMBEDDED_NoMtCut = []

##########
# for ztt embedded no mt cut

FOR_ZTTEMBEDDED_NoMtCut = []


##########
# for ztt norm no mt cut

FOR_ZTTNORM_NoMtCut = []


###############
# for Wjets normalization (high Mt)

FOR_W_NORM = []

##############
# for Wjets norm. for QCD norm estimate
# high Mt + SameSign

FOR_W_NORM_FOR_QCD = []

###############
# for Wjets under default selection

FOR_W_DEFAULT = []

####################
# populate the lists

FOR_UNMODIFIED_ADDITION.append('./2ndTry/data_skimmed_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/data_skimmed_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p1_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p1_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p2_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p2_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p3_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p3_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p4_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p4_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p5_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p5_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p6_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p6_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p7_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p7_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p8_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p8_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p9_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p9_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p10_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('genMatchedTest/ZTTembed_TestGenMatch_skimmed_p10_davis_htt_mssm_muTau.root')


FOR_UNMODIFIED_ADDITION.append('./2ndTry/standardBkg_skimmed_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/standardBkg_skimmed_davis_htt_mssm_muTau.root')



FOR_UNMODIFIED_ADDITION.append('./2ndTry/QCDShape_skimmed_UPDATEWEIGHTS_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/QCDShape_skimmed_UPDATEWEIGHTS_davis_htt_mssm_muTau.root')


FOR_UNMODIFIED_ADDITION.append('./2ndTry/ZLandZJ_skimmed_fixedWtAndClassP1_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/ZLandZJ_skimmed_fixedWtAndClassP2_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/ZLandZJ_skimmed_fixedWtAndClassP1_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/ZLandZJ_skimmed_fixedWtAndClassP2_davis_htt_mssm_muTau.root')


FOR_UNMODIFIED_ADDITION.append('./2ndTry/wjetsShape_skimmed_UPDATEWEIGHTS_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/wjetsShape_skimmed_UPDATEWEIGHTS_davis_htt_mssm_muTau.root')


FOR_UNMODIFIED_ADDITION.append('./2ndTry/bbH_TrigFix_skimmed_p1_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/bbH_TrigFix_skimmed_p1_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/bbH_TrigFix_skimmed_p2_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/bbH_TrigFix_skimmed_p2_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/bbH_TrigFix_skimmed_p3_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/bbH_TrigFix_skimmed_p3_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/bbH_TrigFix_skimmed_p4_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/bbH_TrigFix_skimmed_p4_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/bbH_TrigFix_skimmed_p5_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/bbH_TrigFix_skimmed_p5_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/ggH_TrigFix_skimmed_p1_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/ggH_TrigFix_skimmed_p1_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/ggH_TrigFix_skimmed_p2_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/ggH_TrigFix_skimmed_p2_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/ggH_TrigFix_skimmed_p3_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/ggH_TrigFix_skimmed_p3_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/ggH_TrigFix_skimmed_p4_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/ggH_TrigFix_skimmed_p4_davis_htt_mssm_muTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/ggH_TrigFix_skimmed_p5_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./2ndTry/ggH_TrigFix_skimmed_p5_davis_htt_mssm_muTau.root')


FOR_TTEMBEDDED_SUB.append('genMatchedTest/genMatchTTembeddedFix_skimmed_davis_htt_mssm_eleTau.root')
FOR_TTEMBEDDED_SUB.append('genMatchedTest/genMatchTTembeddedFix_skimmed_davis_htt_mssm_muTau.root')

FOR_W_NORM.append('./2ndTry/wJetsNORM_skimmed_davis_htt_mssm_eleTau.root')
FOR_W_NORM.append('./2ndTry/wJetsNORM_skimmed_davis_htt_mssm_muTau.root')


FOR_W_DEFAULT.append('./2ndTry/wJetsDEFAULT_skimmed_davis_htt_mssm_eleTau.root')
FOR_W_DEFAULT.append('./2ndTry/wJetsDEFAULT_skimmed_davis_htt_mssm_muTau.root')

FOR_ZTT_NORM.append('./2ndTry/ZTTnorm_skimmed_davis_htt_mssm_muTau.root')
FOR_ZTT_NORM.append('./2ndTry/ZTTnorm_skimmed_davis_htt_mssm_eleTau.root')

FOR_QCD_NORM.append('./2ndTry/QCDnorm_skimmedP1_davis_htt_mssm_eleTau.root')
FOR_QCD_NORM.append('./2ndTry/QCDnorm_skimmedP1_davis_htt_mssm_muTau.root')
FOR_QCD_NORM.append('./2ndTry/QCDnorm_skimmedP2_davis_htt_mssm_eleTau.root')
FOR_QCD_NORM.append('./2ndTry/QCDnorm_skimmedP2_davis_htt_mssm_muTau.root')
FOR_QCD_NORM.append('./2ndTry/QCDnorm_skimmedP3_davis_htt_mssm_eleTau.root')
FOR_QCD_NORM.append('./2ndTry/QCDnorm_skimmedP3_davis_htt_mssm_muTau.root')
FOR_QCD_NORM.append('./2ndTry/QCDnorm_skimmedP4_davis_htt_mssm_eleTau.root')
FOR_QCD_NORM.append('./2ndTry/QCDnorm_skimmedP4_davis_htt_mssm_muTau.root')
FOR_QCD_NORM.append('./2ndTry/QCDnorm_skimmedP5_davis_htt_mssm_eleTau.root')
FOR_QCD_NORM.append('./2ndTry/QCDnorm_skimmedP5_davis_htt_mssm_muTau.root')
FOR_QCD_NORM.append('./2ndTry/QCDnorm_skimmedP6_davis_htt_mssm_eleTau.root')
FOR_QCD_NORM.append('./2ndTry/QCDnorm_skimmedP6_davis_htt_mssm_muTau.root')
FOR_QCD_NORM.append('./2ndTry/QCDnorm_skimmedP7_davis_htt_mssm_eleTau.root')
FOR_QCD_NORM.append('./2ndTry/QCDnorm_skimmedP7_davis_htt_mssm_muTau.root')


FOR_W_NORM_FOR_QCD.append('./2ndTry/wjetsNormForQCDnormHighMtSameSign_skimmedP1_davis_htt_mssm_eleTau.root')
FOR_W_NORM_FOR_QCD.append('./2ndTry/wjetsNormForQCDnormHighMtSameSign_skimmedP1_davis_htt_mssm_muTau.root')
FOR_W_NORM_FOR_QCD.append('./2ndTry/wjetsNormForQCDnormHighMtSameSign_skimmedP2_davis_htt_mssm_eleTau.root')
FOR_W_NORM_FOR_QCD.append('./2ndTry/wjetsNormForQCDnormHighMtSameSign_skimmedP2_davis_htt_mssm_muTau.root')
FOR_W_NORM_FOR_QCD.append('./2ndTry/wjetsNormForQCDnormHighMtSameSign_skimmedP3_davis_htt_mssm_eleTau.root')
FOR_W_NORM_FOR_QCD.append('./2ndTry/wjetsNormForQCDnormHighMtSameSign_skimmedP3_davis_htt_mssm_muTau.root')
FOR_W_NORM_FOR_QCD.append('./2ndTry/wjetsNormForQCDnormHighMtSameSign_skimmedP4_davis_htt_mssm_eleTau.root')
FOR_W_NORM_FOR_QCD.append('./2ndTry/wjetsNormForQCDnormHighMtSameSign_skimmedP4_davis_htt_mssm_muTau.root')
FOR_W_NORM_FOR_QCD.append('./2ndTry/wjetsNormForQCDnormHighMtSameSign_skimmedP5_davis_htt_mssm_eleTau.root')
FOR_W_NORM_FOR_QCD.append('./2ndTry/wjetsNormForQCDnormHighMtSameSign_skimmedP5_davis_htt_mssm_muTau.root')



FOR_TTEMBEDDED_NoMtCut.append('./2ndTry/ttEmbeddedNoMtCut_skimmed_davis_htt_mssm_eleTau.root')
FOR_TTEMBEDDED_NoMtCut.append('./2ndTry/ttEmbeddedNoMtCut_skimmed_davis_htt_mssm_muTau.root')


FOR_ZTTNORM_NoMtCut.append('./2ndTry/ZTTNORM_NoMtCut_skimmed_davis_htt_mssm_eleTau.root')
FOR_ZTTNORM_NoMtCut.append('./2ndTry/ZTTNORM_NoMtCut_skimmed_davis_htt_mssm_muTau.root')

FOR_ZTTEMBEDDED_NoMtCut.append('./2ndTry/ZTTEMBEDDED_NoMtCut_skimmed_p1_davis_htt_mssm_eleTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./2ndTry/ZTTEMBEDDED_NoMtCut_skimmed_p1_davis_htt_mssm_muTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./2ndTry/ZTTEMBEDDED_NoMtCut_skimmed_p2_davis_htt_mssm_eleTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./2ndTry/ZTTEMBEDDED_NoMtCut_skimmed_p2_davis_htt_mssm_muTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./2ndTry/ZTTEMBEDDED_NoMtCut_skimmed_p3_davis_htt_mssm_eleTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./2ndTry/ZTTEMBEDDED_NoMtCut_skimmed_p3_davis_htt_mssm_muTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./2ndTry/ZTTEMBEDDED_NoMtCut_skimmed_p4_davis_htt_mssm_eleTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./2ndTry/ZTTEMBEDDED_NoMtCut_skimmed_p4_davis_htt_mssm_muTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./2ndTry/ZTTEMBEDDED_NoMtCut_skimmed_p5_davis_htt_mssm_eleTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./2ndTry/ZTTEMBEDDED_NoMtCut_skimmed_p5_davis_htt_mssm_muTau.root')


OLD_BAD_SIGNALS.append('./2ndTry/bbH_skimmed_davis_htt_mssm_eleTau.root')
OLD_BAD_SIGNALS.append('./2ndTry/bbH_skimmed_davis_htt_mssm_muTau.root')

OLD_BAD_SIGNALS.append('./1stTry/ggHSUSY_fixPtReweight_davis_htt_mssm_eleTau.root')
OLD_BAD_SIGNALS.append('./1stTry/ggHSUSY_fixPtReweight_davis_htt_mssm_muTau.root')
