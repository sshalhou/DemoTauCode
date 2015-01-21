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

# data

FOR_UNMODIFIED_ADDITION.append('./3rdTry/MSSM_obsDATA_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./3rdTry/MSSM_obsDATA_davis_htt_mssm_muTau.root')

# signal 

FOR_UNMODIFIED_ADDITION.append('./3rdTry/MSSM_bbHSUSY_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./3rdTry/MSSM_bbHSUSY_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./3rdTry/MSSM_GluGluHSUSY_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./3rdTry/MSSM_GluGluHSUSY_davis_htt_mssm_muTau.root')

# embedded ztt 

FOR_UNMODIFIED_ADDITION.append('./3rdTry/MSSM_ZTT_EMBEDDED_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./3rdTry/MSSM_ZTT_EMBEDDED_davis_htt_mssm_muTau.root')


# standard bkg

FOR_UNMODIFIED_ADDITION.append('./3rdTry/MSSM_StandardBkgs_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./3rdTry/MSSM_StandardBkgs_davis_htt_mssm_muTau.root')

# qcd shape

FOR_UNMODIFIED_ADDITION.append('./3rdTry/MSSM_QCDshapes_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./3rdTry/MSSM_QCDshapes_davis_htt_mssm_muTau.root')

# zl and zj

FOR_UNMODIFIED_ADDITION.append('./3rdTry/MSSM_ZLandZJ_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./3rdTry/MSSM_ZLandZJ_davis_htt_mssm_muTau.root')

# wjets shape

FOR_UNMODIFIED_ADDITION.append('./3rdTry/MSSM_WJetsShape_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./3rdTry/MSSM_WJetsShape_davis_htt_mssm_muTau.root')


# tt embedded

FOR_TTEMBEDDED_SUB.append('./3rdTry/MSSM_TTembedded_davis_htt_mssm_eleTau.root')
FOR_TTEMBEDDED_SUB.append('./3rdTry/MSSM_TTembedded_davis_htt_mssm_muTau.root')

# w norm

FOR_W_NORM.append('./3rdTry/MSSM_WJetsNorm_davis_htt_mssm_eleTau.root')
FOR_W_NORM.append('./3rdTry/MSSM_WJetsNorm_davis_htt_mssm_muTau.root')

# w default

FOR_W_DEFAULT.append('./3rdTry/MSSM_WjetsDefault_davis_htt_mssm_eleTau.root')
FOR_W_DEFAULT.append('./3rdTry/MSSM_WjetsDefault_davis_htt_mssm_muTau.root')

# for qcd norm 

FOR_QCD_NORM.append('./3rdTry/MSSM_QCDnorm_davis_htt_mssm_eleTau.root')
FOR_QCD_NORM.append('./3rdTry/MSSM_QCDnorm_davis_htt_mssm_muTau.root')

# w norm for high mt same sign


FOR_W_NORM_FOR_QCD.append('./3rdTry/MSSM_WjetsNormSameSignHighMt_davis_htt_mssm_eleTau.root')
FOR_W_NORM_FOR_QCD.append('./3rdTry/MSSM_WjetsNormSameSignHighMt_davis_htt_mssm_muTau.root')

# tt embedded no mt cut



FOR_TTEMBEDDED_NoMtCut.append('./3rdTry/MSSM_TTembeddedNoMtCut_davis_htt_mssm_eleTau.root')
FOR_TTEMBEDDED_NoMtCut.append('./3rdTry/MSSM_TTembeddedNoMtCut_davis_htt_mssm_muTau.root')

# ztt norm no mt cut

FOR_ZTTNORM_NoMtCut.append('./3rdTry/MSSM_ZTTnormNoMtCut_davis_htt_mssm_eleTau.root')
FOR_ZTTNORM_NoMtCut.append('./3rdTry/MSSM_ZTTnormNoMtCut_davis_htt_mssm_muTau.root')

# ztt embedded no mt cut

FOR_ZTTEMBEDDED_NoMtCut.append('./3rdTry/MSSM_ZTTembedded_noMtCut_davis_htt_mssm_eleTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./3rdTry/MSSM_ZTTembedded_noMtCut_davis_htt_mssm_muTau.root')
