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




###############
# for Wjets normalization

FOR_W_NORM = []


####################
# populate the lists

FOR_UNMODIFIED_ADDITION.append('./1stTry/obsDATA_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./1stTry/obsDATA_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./1stTry/bbHSUSY_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./1stTry/bbHSUSY_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./1stTry/ggHSUSY_fixPtReweight_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./1stTry/ggHSUSY_fixPtReweight_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./1stTry/standardBKG_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./1stTry/standardBKG_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./1stTry/ZJandZL_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./1stTry/ZJandZL_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./1stTry/shapeWJETS_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./1stTry/shapeWJETS_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./1stTry/qcdShapes_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./1stTry/qcdShapes_davis_htt_mssm_muTau.root')

FOR_UNMODIFIED_ADDITION.append('./1stTry/embeddedZTT_davis_htt_mssm_eleTau.root')
FOR_UNMODIFIED_ADDITION.append('./1stTry/embeddedZTT_davis_htt_mssm_muTau.root')

FOR_QCD_NORM.append('./1stTry/qcdNORMpart1_davis_htt_mssm_eleTau.root')
FOR_QCD_NORM.append('./1stTry/qcdNORMpart1_davis_htt_mssm_muTau.root')

FOR_QCD_NORM.append('./1stTry/qcdNORMpart2_davis_htt_mssm_eleTau.root')
FOR_QCD_NORM.append('./1stTry/qcdNORMpart2_davis_htt_mssm_muTau.root')

FOR_QCD_NORM.append('./1stTry/qcdNORMpart3_davis_htt_mssm_eleTau.root')
FOR_QCD_NORM.append('./1stTry/qcdNORMpart3_davis_htt_mssm_muTau.root')



FOR_W_NORM.append('./1stTry/normWJETS_tightCSVp1_davis_htt_mssm_eleTau.root')
FOR_W_NORM.append('./1stTry/normWJETS_tightCSVp1_davis_htt_mssm_muTau.root')

FOR_W_NORM.append('./1stTry/normWJETS_tightCSVp2_davis_htt_mssm_eleTau.root')
FOR_W_NORM.append('./1stTry/normWJETS_tightCSVp2_davis_htt_mssm_muTau.root')

FOR_W_NORM.append('./1stTry/normWJETS_tightCSVp3_davis_htt_mssm_eleTau.root')
FOR_W_NORM.append('./1stTry/normWJETS_tightCSVp3_davis_htt_mssm_muTau.root')

FOR_ZTT_NORM.append('./1stTry/normZTT_p1_davis_htt_mssm_eleTau.root')
FOR_ZTT_NORM.append('./1stTry/normZTT_p1_davis_htt_mssm_muTau.root')
FOR_ZTT_NORM.append('./1stTry/normZTT_p2_davis_htt_mssm_eleTau.root')
FOR_ZTT_NORM.append('./1stTry/normZTT_p2_davis_htt_mssm_muTau.root')
FOR_ZTT_NORM.append('./1stTry/normZTT_p3_davis_htt_mssm_eleTau.root')
FOR_ZTT_NORM.append('./1stTry/normZTT_p3_davis_htt_mssm_muTau.root')
FOR_ZTT_NORM.append('./1stTry/normZTT_p4_davis_htt_mssm_eleTau.root')
FOR_ZTT_NORM.append('./1stTry/normZTT_p4_davis_htt_mssm_muTau.root')


FOR_TTEMBEDDED_SUB.append('./1stTry/embeddedTTbar_davis_htt_mssm_eleTau.root')
FOR_TTEMBEDDED_SUB.append('./1stTry/embeddedTTbar_davis_htt_mssm_muTau.root')
