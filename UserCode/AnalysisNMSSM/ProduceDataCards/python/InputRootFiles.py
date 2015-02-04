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


##############
# for ZL and ZJ norm under meduim b-tag
# loose b-tag version for the shapes goes
# into FOR_UNMODIFIED_ADDITION


FOR_ZLandZJ_NORM = []

####################
# populate the lists

FOR_UNMODIFIED_ADDITION.append('./6thTry/nMSSMV10_DATA_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./6thTry/nMSSMV10_DATA_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./6thTry/nMSSMV10_nmssmSignals_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./6thTry/nMSSMV10_nmssmSignals_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./Fix6/nMSSMV10_ZTTembedded_FIX_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./Fix6/nMSSMV10_ZTTembedded_FIX_davis_htt_mssm_muTau.root')

#FOR_UNMODIFIED_ADDITION.append('./6thTry/nMSSMV10_ZTTembedded_davis_htt_mssm_eleTau.root')
#FOR_UNMODIFIED_ADDITION.append('./6thTry/nMSSMV10_ZTTembedded_davis_htt_mssm_muTau.root')

#FOR_UNMODIFIED_ADDITION.append('./6thTry/nMSSMV10_StdBkgs_davis_htt_mssm_eleTau.root')
#FOR_UNMODIFIED_ADDITION.append('./6thTry/nMSSMV10_StdBkgs_davis_htt_mssm_muTau.root')


FOR_UNMODIFIED_ADDITION.append('./Fix6/nMSSMV10_StdBkgs_FIX_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./Fix6/nMSSMV10_StdBkgs_FIX_davis_htt_mssm_muTau.root')


FOR_UNMODIFIED_ADDITION.append('./6thTry/nMSSMV10_QCDshapes_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./6thTry/nMSSMV10_QCDshapes_davis_htt_mssm_muTau.root')

#FOR_UNMODIFIED_ADDITION.append('./6thTry/nMSSMV10_ZLandZJ_davis_htt_mssm_eleTau.root')
#FOR_UNMODIFIED_ADDITION.append('./6thTry/nMSSMV10_ZLandZJ_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./Fix6/nMSSMV10_ZLandZJSHAPE_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./Fix6/nMSSMV10_ZLandZJSHAPE_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./6thTry/nMSSMV10_WjetsShape_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./6thTry/nMSSMV10_WjetsShape_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./6thTry/nMSSMV10_ZTTlowMassShape_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./6thTry/nMSSMV10_ZTTlowMassShape_davis_htt_mssm_muTau.root')


FOR_TTEMBEDDED_SUB.append('./6thTry/nMSSMV10_TTBarEmbedded_davis_htt_mssm_eleTau.root')
FOR_TTEMBEDDED_SUB.append('./6thTry/nMSSMV10_TTBarEmbedded_davis_htt_mssm_muTau.root')

FOR_W_NORM.append('./6thTry/nMSSMV10_WjetsNorm_davis_htt_mssm_eleTau.root')
FOR_W_NORM.append('./6thTry/nMSSMV10_WjetsNorm_davis_htt_mssm_muTau.root')


FOR_W_DEFAULT.append('./6thTry/nMSSMV10_WjetsDefault_davis_htt_mssm_eleTau.root')
FOR_W_DEFAULT.append('./6thTry/nMSSMV10_WjetsDefault_davis_htt_mssm_muTau.root')



FOR_QCD_NORM.append('./6thTry/nMSSMV10_QCDnorm_davis_htt_mssm_eleTau.root')
FOR_QCD_NORM.append('./6thTry/nMSSMV10_QCDnorm_davis_htt_mssm_muTau.root')

FOR_W_NORM_FOR_QCD.append('./6thTry/nMSSMV10_WjetsNormSameSignHighMt_davis_htt_mssm_eleTau.root')
FOR_W_NORM_FOR_QCD.append('./6thTry/nMSSMV10_WjetsNormSameSignHighMt_davis_htt_mssm_muTau.root')


FOR_TTEMBEDDED_NoMtCut.append('./6thTry/nMSSMV10_TTBarEmbedded_noMtCut_davis_htt_mssm_eleTau.root')
FOR_TTEMBEDDED_NoMtCut.append('./6thTry/nMSSMV10_TTBarEmbedded_noMtCut_davis_htt_mssm_muTau.root')


FOR_ZTTNORM_NoMtCut.append('./6thTry/nMSSMV10_ZTTnorm_noMtCut_davis_htt_mssm_eleTau.root')
FOR_ZTTNORM_NoMtCut.append('./6thTry/nMSSMV10_ZTTnorm_noMtCut_davis_htt_mssm_muTau.root')

FOR_ZTT_LOW_MASSNORM.append('./6thTry/nMSSMV10_ZTTlowMass_davis_htt_mssm_eleTau.root')
FOR_ZTT_LOW_MASSNORM.append('./6thTry/nMSSMV10_ZTTlowMass_davis_htt_mssm_muTau.root')

#FOR_ZTTEMBEDDED_NoMtCut.append('./6thTry/nMSSMV10_ZTTEmbeddedNoMtCut_davis_htt_mssm_eleTau.root')
#FOR_ZTTEMBEDDED_NoMtCut.append('./6thTry/nMSSMV10_ZTTEmbeddedNoMtCut_davis_htt_mssm_muTau.root')

FOR_ZTTEMBEDDED_NoMtCut.append('./Fix6/nMSSMV10_ZTTEmbeddedNoMtCut_davis_htt_mssm_eleTau.root')
FOR_ZTTEMBEDDED_NoMtCut.append('./Fix6/nMSSMV10_ZTTEmbeddedNoMtCut_davis_htt_mssm_muTau.root')


FOR_ZLandZJ_NORM.append('./6thTry/nMSSMV10_ZLandZJ_davis_htt_mssm_eleTau.root')
FOR_ZLandZJ_NORM.append('./6thTry/nMSSMV10_ZLandZJ_davis_htt_mssm_muTau.root')

