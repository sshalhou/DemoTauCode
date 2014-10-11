########################################################################################################
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patTemplate_cfg import *
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
########################################################################################################


SampleName_='SUSYGluGluToHToTauTau_M-120_8TeV-pythia6-tauola/AODSIM/PU_S10_START53_V7A-v1/AODSIM'
PhysicsProcess_='ggA0tautau[SUSY_120_8TeV]'
MASS_=120.0
isNonTopEmbeddedSample_ = False
isTopEmbeddedSample_ = False
runOnMC_ = True # true for MC, and all topTopBar and Ztautau embedded samples
branchingFraction_ = 999.99
crossSection_ = 999.99
numberEvents_ = 999

FilterEvents_ = True
DropSelectedPatObjects_ = True
KeepAll_ = False
PrintProductIDs_ = False

###################################################
# Store SampleName and PhysicsProcess
# eventually these should be command line
# options
###################################################

process.UserSpecifiedData = cms.EDProducer('TupleUserSpecifiedDataProducer',
                                            SampleName=cms.string(SampleName_),
                                            PhysicsProcess=cms.string(PhysicsProcess_),
                                            isNonTopEmbeddedSample=cms.bool(isNonTopEmbeddedSample_),
                                            isTopEmbeddedSample=cms.bool(isTopEmbeddedSample_),
                                            MASS=cms.double(MASS_),
                                            crossSection=cms.double(crossSection_),
                                            branchingFraction=cms.double(branchingFraction_),
                                            numberEvents=cms.int32(numberEvents_)
                                            )



##################################################
# Jet Energy Corrections and Global Tags
###################################################

from PhysicsTools.PatAlgos.tools.coreTools import *


if runOnMC_:
  process.GlobalTag.globaltag = 'START53_V23::All'
else:
  process.GlobalTag.globaltag = 'FT_53_V21_AN4::All'
  removeMCMatching(process, ['All'])
  runOnData(process)

if isNonTopEmbeddedSample_:
  process.GlobalTag.globaltag = 'FT_53_V21_AN4::All'


#################################
# set the correct jet en. corr
#################################
jetEnCorr = ['L1FastJet', 'L2Relative', 'L3Absolute']
corrector_ = cms.string('ak5PFL1FastL2L3')

if runOnMC_ and not isNonTopEmbeddedSample_:
  corrector_ = cms.string('ak5PFL1FastL2L3')
  jetEnCorr.extend(['L2L3Residual'])

else:
  corrector_ = cms.string('ak5PFL1FastL2L3Residual')
  jetEnCorr.extend(['L2L3Residual'])


#####################################
# compute the tau spinner weights
#####################################

process.load("TauSpinnerInterface.TauSpinnerInterface.TauSpinner_cfi")


###################################################
# debug info including productId will be printed
###################################################

process.printEventContent = cms.EDAnalyzer("EventContentAnalyzer")



##################################################
# Let it run
###################################################
process.p = cms.Path(process.UserSpecifiedData)

if PrintProductIDs_:
  process.p *= process.printEventContent

if runOnMC_:
  process.p *= process.TauSpinnerReco

########################################################################################################

#################################
# keep everything produced by Tuepl-Code
#################################
process.out.outputCommands +=['keep Tuple*_*_*_*']

if KeepAll_:
  process.out.outputCommands +=['keep *_*_*_*']
########################################################################################################
process.out.fileName = '/uscms/home/shalhout/no_backup/JOINTpatTuple_testing.root'

########################################################################################################
myfilelist = cms.untracked.vstring()
myfilelist.extend(['file:/uscms/home/shalhout/no_backup/oneThousand_selectedEventsRaw.root'])

process.source = cms.Source ("PoolSource",
                      fileNames=myfilelist,
                        dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
                        inputCommands = cms.untracked.vstring(
                        'keep *',
                        'drop recoPFTaus_*_*_*'
                        ),
                      skipEvents=cms.untracked.uint32(0)
                             )
########################################################################################################


process.maxEvents.input = 20
########################################################################################################
