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
listOfFiles.append('./HOLDER/WZJetsFlatTuple_3_1_c9j.root')
#listOfFiles.append('./HOLDER/DY2JetsFlatTuple_5_1_bfs.root')
#listOfFiles.append('./HOLDER/DYSpinOffFlatTuple_8_1_awC.root')
#listOfFiles.append('./HOLDER/DATAA_partial_FlatTuple_1_1_I5s.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNA_V7FlatTupleEx/FlatTuple_1_1_I5s.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNA_V7FlatTupleEx/FlatTuple_2_1_emp.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_V7FlatTupleEx/FlatTuple_1_1_KIQ.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_V7FlatTupleEx/FlatTuple_2_1_0S8.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_V7FlatTupleEx/FlatTuple_3_1_ROv.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_V7FlatTupleEx/FlatTuple_4_1_kxi.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_V7FlatTupleEx/FlatTuple_5_1_rtZ.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNB_V7FlatTupleEx/FlatTuple_6_1_MAi.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_1_1_tJt.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_2_1_fvG.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_3_1_PuD.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_4_1_Qcy.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_5_1_9SD.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_6_1_l5M.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_7_1_tGi.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_8_1_E1H.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUNC_V7FlatTupleEx/FlatTuple_9_1_6jK.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_1_1_Tj1.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_2_1_JIl.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_3_1_tTy.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_4_1_Yg5.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_5_1_2ss.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_6_1_JRW.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_7_1_RoG.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_8_1_jWE.root')
# listOfFiles.append('/eos/uscms/store/user/shalhout/DATA2012RUND_V7FlatTupleEx/FlatTuple_RecoveredJobs.root')

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
	maxEntries = 1000

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
				if passesSameSignSelectionETau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				if passesSameSignSelectionMuTau(chain,index,UseNewTriggers,Verbose) is False:
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
					SAMPLE_ADD = '_QCD_'
					QCDShapeWeightsDownNominalUp_dict = {}
					QCDShapeWeightsDownNominalUp_dict['Nominal'] = 1.0
					QCDShapeWeightsDownNominalUp_dict['Up'] = 1.0
					QCDShapeWeightsDownNominalUp_dict['Down'] = 1.0
					FillQCDShapes(maxPairTypeAndIndex,SAMPLE_ADD,
										histogram_dict,
										QCDShapeWeightsDownNominalUp_dict,
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
				elif SAMPLE_ADD=='_DY1Jet_' or SAMPLE_ADD=='_DY2Jet_' or SAMPLE_ADD=='_DY3Jet_' or SAMPLE_ADD=='_DY4Jet_':
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
					wt = getWeightForVV(chain,maxPairTypeAndIndex,False)
					Fill_VV(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])


######################
# save filled histograms

WriteEverything()
writeCompFile()
