import time
import sys
import os


from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile

gROOT.Reset()

check_events = []
# unique LLR events
# check_events.append('191277-105-105919806')
# check_events.append('191226-923-1227448970')
# check_events.append('193336-390-285003049')
# check_events.append('190738-17-12737871')

# unique Davis events
check_events.append('190738-306-277596820')
check_events.append('190945-134-50122617')
check_events.append('190705-324-418658560')
check_events.append('191834-315-370805656')
check_events.append('193336-222-171029414')
check_events.append('193575-93-53888933')
check_events.append('190733-117-84722174')
check_events.append('191226-1361-1676378176')
check_events.append('193575-414-320768249')
check_events.append('190782-257-315880666')
check_events.append('190733-267-286150312')
check_events.append('193557-50-47512097')
check_events.append('190782-132-135978922')
check_events.append('191226-367-511051051')
check_events.append('191247-87-135651914')
check_events.append('190906-132-100154403')
check_events.append('193336-224-172473336')
check_events.append('191810-42-63785992')
check_events.append('193541-250-146946718')
check_events.append('191226-798-1080385992')
check_events.append('191837-37-34452680')
check_events.append('190782-113-107573508')
check_events.append('190736-122-125873929')
check_events.append('193336-791-562573098')
check_events.append('191226-669-925154505')
check_events.append('193575-307-237687182')
check_events.append('193575-596-452137277')
check_events.append('193575-529-405463754')
check_events.append('190895-417-451779082')
check_events.append('191247-428-602300890')
check_events.append('190733-293-318188883')
check_events.append('191062-271-297892050')
check_events.append('191834-110-134719609')
check_events.append('190679-33-19451811')
check_events.append('191247-319-462063952')
check_events.append('190895-512-548103547')
check_events.append('190895-639-664347116')
check_events.append('191720-167-149190129')
check_events.append('191834-40-46716291')
check_events.append('191226-1523-1823302179')
check_events.append('193193-95-63595515')
check_events.append('191226-1047-1363662830')
check_events.append('191062-81-91120841')
check_events.append('193621-1530-1165907569')
check_events.append('191718-69-72070917')
check_events.append('191247-311-450817211')
check_events.append('191271-137-126561760')
check_events.append('193575-381-296023591')
check_events.append('191247-636-851038105')
check_events.append('191226-732-1000627052')
check_events.append('191264-176-189431520')
check_events.append('191833-98-127391764')
check_events.append('191226-1193-1513674420')
check_events.append('193621-319-294960272')
check_events.append('193336-296-222474882')
check_events.append('191277-72-72046764')
check_events.append('191247-579-784662107')
check_events.append('191837-50-47587289')
check_events.append('191271-150-142967775')
check_events.append('193541-333-207709391')
check_events.append('193207-66-17160948')


################
# some global settings

UseNewTriggers = False
OnlyCheckEmbeddedTriggers = True

Verbose = False
SmallRun = False

chain = TChain('demo/FlatTuple')

listOfFiles = []
listOfFiles.append('./FlatTuple_eTau.root')
#listOfFiles.append('FlatTupleHold/FlatTuple_ggH.root')

for afile in listOfFiles:
	chain.AddFile(afile,0,'demo/FlatTuple')




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


maxEntries = chain.GetEntries()

if SmallRun is True:
	maxEntries = 300

for entry in range(0,maxEntries):
		entryNumber = chain.GetEntryNumber(entry);
		localEntry = chain.LoadTree(entryNumber);
		if (localEntry >= 0):
			selector.Process(localEntry)
			passingETauIndices = []
			passingMuTauIndices = []
			maxPairTypeAndIndex = []

			#########################################################
			# get event ID

			eventID = [str(chain.run), str(chain.luminosityBlock), str(chain.event)]
			eventString = str(chain.run)+"-"+str(chain.luminosityBlock)+"-"+str(chain.event)
			if eventString in check_events:
				Verbose = True
				print "**********************************************"
				print "*********", eventString, "**************"
			else:
				Verbose = False

			## temp
			#print "---------- checking Event",eventID[0],eventID[1],eventID[2],"-----------------------"



#########################################################
# loop over eTau pairs and store all that pass in list

			for index in range(0, chain.eT_correctedSVFitMass.size()):
				passesCuts = True

				if electronID(chain,index,Verbose) is False:
					passesCuts = False
				if tauID_eTau(chain, index, Verbose) is False:
					passesCuts = False
				if pairCutsETau(chain, index,Verbose) is False:
					passesCuts = False
				if OnlyCheckEmbeddedTriggers is True and embeddedZTauTauTrigForETau(chain, index, Verbose) is False:
					passesCuts = False
				if OnlyCheckEmbeddedTriggers is False and electronTrigger(chain,index,UseNewTriggers) is False:
					passesCuts = False
				if OnlyCheckEmbeddedTriggers is False and tauTriggerForETau(chain,index,UseNewTriggers) is False:
					passesCuts = False

				if passesCuts is True:
					passingETauIndices.append(index)


#########################################################
# loop over muTau pairs and store all that pass in list

			for index in range(0, chain.muT_correctedSVFitMass.size()):
				passesCuts = True

				if muonID(chain,index,Verbose) is False:
					passesCuts = False
				if tauID_muTau(chain, index, Verbose) is False:
					passesCuts = False
				if pairCutsMuTau(chain, index,Verbose) is False:
					passesCuts = False
				#if OnlyCheckEmbeddedTriggers is True and embeddedZTauTauTrigForMuTau(chain, index, Verbose) is False:
				#	passesCuts = False
				#if OnlyCheckEmbeddedTriggers is False and muonTrigger(chain,index,UseNewTriggers) is False:
				#	passesCuts = False
				#if OnlyCheckEmbeddedTriggers is False and tauTriggerForMuTau(chain,index,UseNewTriggers) is False:
				#	passesCuts = False

				if passesCuts is True:
					passingMuTauIndices.append(index)


#########################################################
# if have multiple passing H candidates in the same event
# find the highest sumPt pair


			if (len(passingETauIndices) + len(passingMuTauIndices)) == 1:
				if len(passingETauIndices) == 1 :
					maxPairTypeAndIndex.append(passingETauIndices[0])
					maxPairTypeAndIndex.append('electronTau')
				elif len(passingMuTauIndices) == 1:
					maxPairTypeAndIndex.append(passingMuTauIndices[0])
					maxPairTypeAndIndex.append('muonTau')
			if (len(passingETauIndices) + len(passingMuTauIndices)) > 1:
					getMaxPtPairIndex(chain, maxPairTypeAndIndex, passingMuTauIndices, passingETauIndices)
			if len(maxPairTypeAndIndex)	> 0 and False:
				print maxPairTypeAndIndex[1], eventID[0]+"-"+eventID[1]+"-"+eventID[2]

#########################################################
# now classify the event based on tauPt and nbtags
# add run, event, lumi to FlatTree
