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

#listOfFiles.append('./HOLDER/ZTTEMbedETauFlatTuple_2_1_8zT.root')


##################
#embedded Ztt
##################

listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauA_FlatTuple/FlatTuple_1_1_IGh.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauA_FlatTuple/FlatTuple_2_1_8zT.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauB_FlatTuple/FlatTuple_1_1_kNN.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauB_FlatTuple/FlatTuple_2_1_Syw.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauB_FlatTuple/FlatTuple_3_1_5sv.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauB_FlatTuple/FlatTuple_4_1_jo1.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauB_FlatTuple/FlatTuple_5_1_uY5.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauC_FlatTuple/FlatTuple_1_1_6xw.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauC_FlatTuple/FlatTuple_2_1_y5l.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauC_FlatTuple/FlatTuple_3_1_Wpz.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauC_FlatTuple/FlatTuple_4_1_H63.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauC_FlatTuple/FlatTuple_5_1_xIt.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauC_FlatTuple/FlatTuple_6_1_XVR.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauC_FlatTuple/FlatTuple_7_1_1uy.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauC_FlatTuple/FlatTuple_8_1_7D3.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauC_FlatTuple/FlatTuple_9_1_4fW.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauD_FlatTuple/FlatTuple_1_1_yn4.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauD_FlatTuple/FlatTuple_2_1_8J6.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauD_FlatTuple/FlatTuple_3_1_iNq.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauD_FlatTuple/FlatTuple_4_1_PPO.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauD_FlatTuple/FlatTuple_5_1_LXf.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauD_FlatTuple/FlatTuple_6_1_4uz.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauD_FlatTuple/FlatTuple_7_1_1Rq.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedETauD_FlatTuple/FlatTuple_8_1_ae0.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauA_FlatTuple/FlatTuple_1_1_0YT.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauA_FlatTuple/FlatTuple_2_1_Rxr.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauB_FlatTuple/FlatTuple_1_1_fJr.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauB_FlatTuple/FlatTuple_2_1_UiI.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauB_FlatTuple/FlatTuple_3_1_F4e.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauB_FlatTuple/FlatTuple_4_1_I8l.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauB_FlatTuple/FlatTuple_5_1_Bl1.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauC_FlatTuple/FlatTuple_1_1_0k3.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauC_FlatTuple/FlatTuple_2_1_WM0.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauC_FlatTuple/FlatTuple_3_1_Yop.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauC_FlatTuple/FlatTuple_4_1_MSW.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauC_FlatTuple/FlatTuple_5_1_7xv.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauC_FlatTuple/FlatTuple_6_1_IJM.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauC_FlatTuple/FlatTuple_7_1_QZa.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauC_FlatTuple/FlatTuple_8_1_jZB.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauC_FlatTuple/FlatTuple_9_1_6WZ.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauD_FlatTuple/FlatTuple_1_1_HPe.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauD_FlatTuple/FlatTuple_2_1_jfL.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauD_FlatTuple/FlatTuple_3_1_2gd.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauD_FlatTuple/FlatTuple_4_1_5oR.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauD_FlatTuple/FlatTuple_5_1_n5x.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauD_FlatTuple/FlatTuple_6_1_sYP.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauD_FlatTuple/FlatTuple_7_1_34v.root')
listOfFiles.append('/uscmst1b_scratch/lpc1/3DayLifetime/shalhout/TEMP_DATAFILES/ZTauTauEmbeddedMuTauD_FlatTuple/FlatTuple_8_1_YHF.root')



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
				if passesEmbeddedZTauTauSelectionETau(chain,index,UseNewTriggers,Verbose) is False:
					passesCuts = False
				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True
				if passesEmbeddedZTauTauSelectionMuTau(chain,index,UseNewTriggers,Verbose) is False:
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

				if SAMPLE_ADD == '_embeddedZTT_':
					classification = '_ZTT_'
					wt = getWeightEmbeddedZTT(chain,maxPairTypeAndIndex,Verbose)
					Fill_ZTTembedded(maxPairTypeAndIndex,classification,wt,histogram_dict,eventVariables['SVFitMass'])


######################
# save filled histograms

WriteEverything()
writeCompFile()
