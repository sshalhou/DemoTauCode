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

#listOfFiles.append('./HOLDER/DY2JetsFlatTuple_5_1_bfs.root')



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
	maxEntries = 15000

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
				if SAMPLE_ADD == '_DYTauPolOff_':
					classification = classifyZDecay(chain,maxPairTypeAndIndex)
					print classification
					wt = 1.0
					if classification == '_ZTT_':
						wt = getWeightForTauPolOffDY(chain,maxPairTypeAndIndex,Verbose)
						Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					# elif classification == '_ZL_':
					# 	wt = getWeightForTauPolOffDY(chain,maxPairTypeAndIndex,Verbose)
					# 	# contains an internal check for e->tau
					# 	wt = wt * getFakeZeeWeight(chain,maxPairTypeAndIndex)
					# 	Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					# elif classification == '_ZJ_':
					# 	wt = getWeightForTauPolOffDY(chain,maxPairTypeAndIndex,Verbose)
					# 	Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
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
					# if classification == '_ZL_':
					# 	wt = getWeightForRegularDY(chain,maxPairTypeAndIndex,Verbose)
					# 	# contains an internal check for e->tau
					# 	wt = wt * getFakeZeeWeight(chain,maxPairTypeAndIndex)
					# 	Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])
					# elif classification == '_ZJ_':
					# 	wt = getWeightForRegularDY(chain,maxPairTypeAndIndex,Verbose)
					# 	Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])



######################
# save filled histograms

WriteEverything()
writeCompFile()
