#!/usr/bin/python
import time
import sys
import os
import math
from array import array
from ROOT import *
import ROOT
ROOT.gROOT.Macro( os.path.expanduser( './rootlogon.C'))
from python.Helpers import *
from python.Settings import *


DEBUG = True

if len(sys.argv) == 5 :   
	print "************************************************************************************"
	print "*** Will generate comparison for datacards :"
	print "***", sys.argv[1], 'vs.', sys.argv[3]

else:
	print " usage : python check2Cards.py institution1 datacard1.root institution2 datacard2.root"
	print " for example : python compareTemplates.py Davis Davis.root LLR LLR.root"
	sys.exit()

if str(sys.argv[2]).endswith('.root') is False or str(sys.argv[4]).endswith('.root') is False:
	print " usage : python check2Cards.py institution1 datacard1.root institution2 datacard2.root"
	print " for example : python compareTemplates.py Davis Davis.root LLR LLR.root"
	sys.exit()



CARD1 = TFile(str(sys.argv[2]),"READ")
CARD2 = TFile(str(sys.argv[4]),"READ")


print "*** looking through common channels for list of templates in each file ..."


DICT_ONE = {}
LIST_ONE = []
ScanFile(CARD1, DICT_ONE, LIST_ONE)


DICT_TWO = {}
LIST_TWO = []
ScanFile(CARD2, DICT_TWO, LIST_TWO)


COMMON_LIST = GetCommonList(LIST_ONE,LIST_TWO)
MISSING_CHANNELS = GetDiffList(LIST_ONE,LIST_TWO)



print "*** Found ", len(COMMON_LIST), " TH1F objects identically named in both files "
if len(MISSING_CHANNELS)!=0:
	print '"*** WARNING : ', len(MISSING_CHANNELS), ' TH1F objects not in both files'
print "************************************************************************************"


print "*** Starting comparison of common template's integrals ..."
print "*** will Flag if |% difference| in normalization differs by > ", FLAG_PERCENT_DIFF
print "*** adjust threshold in : python/Settings.py"

FLAGGED_FOR_NORM = CompareNormalizations(COMMON_LIST,DICT_ONE,DICT_TWO,FLAG_PERCENT_DIFF,'GREATER')

print 'considering only cases where both histograms are non-empty :'
print len(FLAGGED_FOR_NORM), 'histograms differer by more than ', FLAG_PERCENT_DIFF, '%'
print 'while ', len(CompareNormalizations(COMMON_LIST,DICT_ONE,DICT_TWO,FLAG_PERCENT_DIFF,'LESS')), ' differe by less '


for i in range(0,len(FLAGGED_FOR_NORM)):
 	print FLAGGED_FOR_NORM[i],ff(DICT_ONE[FLAGGED_FOR_NORM[i]].GetSumOfWeights()), ff(DICT_TWO[FLAGGED_FOR_NORM[i]].GetSumOfWeights())
 	PLOT_HIST_DIFF(sys.argv[1],DICT_ONE[FLAGGED_FOR_NORM[i]],sys.argv[3],DICT_TWO[FLAGGED_FOR_NORM[i]],50,500)



###############
# need some way to compare systematics

# SYS_NAMES_DICT = {}
# SYS_LIST = []

# for i in range(0, len(COMPARE_SYS_FOR)):
# 	for ii in range(0, len(COMMON_LIST)):
# 		if COMPARE_SYS_FOR[i] in COMMON_LIST[ii] and COMPARE_SYS_FOR[i] != COMMON_LIST[ii]:
# 			SYS_LIST.append(COMMON_LIST[ii]) 
# 	SYS_NAMES_DICT[COMPARE_SYS_FOR[i]] = SYS_LIST

# print SYS_NAMES_DICT

# for key,value in SYS_NAMES_DICT.iteritems():
# 	for i in range(0,len(value)):
# 		print "making systematic comparison for ", key, value[i]
# 		PLOT_SYSTEMATCIS(sys.argv[1],sys.argv[3],key,value[i],DICT_ONE,DICT_TWO,50,300)








#print FLAGGED_FOR_NORM


# if DEBUG :
# 	for i in range(0,len(COMMON_LIST)):
# 		print COMMON_LIST[i]




#for key,value in DICT_ONE.iteritems():
# 	print key, DICT_ONE[key].GetSumOfWeights()








# card1_Directories = []
# card2_Directories = []

# print "************************************************************************************"
# print "*** looking through cards ", sys.argv[2], " & ", sys.argv[4], "for list of channels "
# print "************************************************************************************"

# HANNEL_LIST2 = []

# for key in CARD1.GetListOfKeys():
#     card1_Directories.append(key.GetName())

# for key in CARD2.GetListOfKeys():
#     card2_Directories.append(key.GetName())

# if DEBUG : print card1_Directories
# if DEBUG : print card2_Directories

# CHANNEL_LIST = list(set(card1_Directories).intersection(card2_Directories))


# print "-----------------------------------------------"
# print "found ", len(CHANNEL_LIST), "channels in common"
# print "-----------------------------------------------"

# if DEBUG :
# 	for i in range(0,len(CHANNEL_LIST)):
# 		print CHANNEL_LIST[i]

# if DEBUG :
# 	print '** WARNING ** following channels not contained in both files :' 
# 	MISSING_CHANNELS = list(set(card1_Directories).symmetric_difference(card2_Directories))
# 	for i in range(0, len(MISSING_CHANNELS)):
# 		print '** WARNING ** ', MISSING_CHANNELS[i]







