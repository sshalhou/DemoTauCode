import time
import sys
import os

#################################
# prefix for final root files

PREFIX = 'davis_combined_htt_nMSSMlowMass_'

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

##################
# for ZTT low mass norm 

FOR_ZTT_LOW_MASSNORM = []

####################
# populate the lists

FOR_UNMODIFIED_ADDITION.append('./NMSSM_1stTry/nMSSM_obsData_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./NMSSM_1stTry/nMSSM_obsData_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./NMSSM_1stTry/nMSSM_Signals_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./NMSSM_1stTry/nMSSM_Signals_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./NMSSM_1stTry/nMSSM_ZTTEMBEDDED_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./NMSSM_1stTry/nMSSM_ZTTEMBEDDED_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./NMSSM_1stTry/nMSSM_stdBkgs_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./NMSSM_1stTry/nMSSM_stdBkgs_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./NMSSM_1stTry/nMSSM_QCDshape_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./NMSSM_1stTry/nMSSM_QCDshape_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./NMSSM_1stTry/nMSSM_ZLandZJ_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./NMSSM_1stTry/nMSSM_ZLandZJ_davis_htt_mssm_muTau.root')


FOR_UNMODIFIED_ADDITION.append('./NMSSM_1stTry/nMSSM_WJETSshape_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./NMSSM_1stTry/nMSSM_WJETSshape_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./NMSSM_1stTry/nMSSM_ZTTlowMassShape_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./NMSSM_1stTry/nMSSM_ZTTlowMassShape_davis_htt_mssm_muTau.root')


FOR_TTEMBEDDED_SUB.append('./NMSSM_1stTry/nMSSM_TTbarEmbedded_davis_htt_mssm_eleTau.root')
FOR_TTEMBEDDED_SUB.append('./NMSSM_1stTry/nMSSM_TTbarEmbedded_davis_htt_mssm_muTau.root')

FOR_W_NORM.append('./NMSSM_1stTry/nMSSM_WJETSnorm_davis_htt_mssm_eleTau.root')
FOR_W_NORM.append('./NMSSM_1stTry/nMSSM_WJETSnorm_davis_htt_mssm_muTau.root')


FOR_W_DEFAULT.append('./NMSSM_1stTry/nMSSM_WjetsDefault_davis_htt_mssm_eleTau.root')
FOR_W_DEFAULT.append('./NMSSM_1stTry/nMSSM_WjetsDefault_davis_htt_mssm_muTau.root')



FOR_QCD_NORM.append('./NMSSM_1stTry/nMSSM_QCDnorm_davis_htt_mssm_eleTau.root')
FOR_QCD_NORM.append('./NMSSM_1stTry/nMSSM_QCDnorm_davis_htt_mssm_muTau.root')

FOR_W_NORM_FOR_QCD.append('./NMSSM_1stTry/nMSSM_WjetsNormSameSignHighMt_davis_htt_mssm_eleTau.root')
FOR_W_NORM_FOR_QCD.append('./NMSSM_1stTry/nMSSM_WjetsNormSameSignHighMt_davis_htt_mssm_muTau.root')


FOR_TTEMBEDDED_NoMtCut.append('./NMSSM_1stTry/nMSSM_TTembedded_noMtCut_davis_htt_mssm_eleTau.root')
FOR_TTEMBEDDED_NoMtCut.append('./NMSSM_1stTry/nMSSM_TTembedded_noMtCut_davis_htt_mssm_muTau.root')


FOR_ZTTNORM_NoMtCut.append('./NMSSM_1stTry/nMSSM_ZTTnorm_noMtCut_davis_htt_mssm_eleTau.root')
FOR_ZTTNORM_NoMtCut.append('./NMSSM_1stTry/nMSSM_ZTTnorm_noMtCut_davis_htt_mssm_muTau.root')

FOR_ZTT_LOW_MASSNORM.append('./NMSSM_1stTry/nMSSM_ZTTlowMass_davis_htt_mssm_eleTau.root')
FOR_ZTT_LOW_MASSNORM.append('./NMSSM_1stTry/nMSSM_ZTTlowMass_davis_htt_mssm_muTau.root')

FOR_ZTTEMBEDDED_NoMtCut.append('./NMSSM_1stTry/nMSSM_ZTTembedded_noMtCut_batch1_davis_htt_mssm_eleTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./NMSSM_1stTry/nMSSM_ZTTembedded_noMtCut_batch1_davis_htt_mssm_muTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./NMSSM_1stTry/nMSSM_ZTTembedded_noMtCut_batch2_davis_htt_mssm_eleTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./NMSSM_1stTry/nMSSM_ZTTembedded_noMtCut_batch2_davis_htt_mssm_muTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./NMSSM_1stTry/nMSSM_ZTTembedded_noMtCut_batch3_davis_htt_mssm_eleTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./NMSSM_1stTry/nMSSM_ZTTembedded_noMtCut_batch3_davis_htt_mssm_muTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./NMSSM_1stTry/nMSSM_ZTTembedded_noMtCut_batch4_davis_htt_mssm_eleTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./NMSSM_1stTry/nMSSM_ZTTembedded_noMtCut_batch4_davis_htt_mssm_muTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./NMSSM_1stTry/nMSSM_ZTTembedded_noMtCut_batch5_davis_htt_mssm_eleTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./NMSSM_1stTry/nMSSM_ZTTembedded_noMtCut_batch5_davis_htt_mssm_muTau.root')

