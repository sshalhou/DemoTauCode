import time
import sys
import os
import math
from array import array
from ROOT import *
import ROOT


FLAG_PERCENT_DIFF = 1.0



# populate this ist with 
# name componets you want ignored
# for example 'CMS' deactivates all sytematics
VETO_NAME_CONTENT = []
##########################

#VETO_NAME_CONTENT.append('nobtag')
#VETO_NAME_CONTENT.append('ZJ_')
#VETO_NAME_CONTENT.append('CMS')
#VETO_NAME_CONTENT.append('fine_binning')

# populate this list with 
# name componets you want to see (only)
# for example 'W' shows all W templates
DEMAND_NAME_CONTENT = []
##########################

#DEMAND_NAME_CONTENT.append('CMS')
#DEMAND_NAME_CONTENT.append('nobtag_medium') # for QCD

#DEMAND_NAME_CONTENT.append('btag_high') # for W

########################
COMPARE_SYS_FOR = []
#COMPARE_SYS_FOR.append('muTau_nobtag_low/W')
COMPARE_SYS_FOR.append('muTau_btag_high/bbH120')
# COMPARE_SYS_FOR.append('muTau_nobtag_medium/QCD')
# COMPARE_SYS_FOR.append('muTau_nobtag_high/QCD')
# COMPARE_SYS_FOR.append('muTau_btag_low/QCD')
# COMPARE_SYS_FOR.append('muTau_btag_high/QCD')

