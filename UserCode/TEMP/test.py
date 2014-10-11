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


process.load('JetMETCorrections.Configuration.DefaultJEC_cff')




###################################################
# pu jet id requires PF jets as input
###################################################

from PhysicsTools.PatAlgos.tools.jetTools import *




###################################################
# must rerun b-tagging at PAT creation
# in order to get embedded sample b-tags correct
###################################################

process.patJets.addTagInfos = True
process.load('RecoBTag.Configuration.RecoBTag_cff')
process.load('RecoJets.JetAssociationProducers.ak5JTA_cff')

###################################################
# special case stuff for embedded samples
###################################################

if isNonTopEmbeddedSample_ or isTopEmbeddedSample_:
        print "EMBEDDED SETTING "
        process.ak5JetTracksAssociatorAtVertex.tracks = cms.InputTag("tmfTracks")
        process.ak5JetTracksAssociatorAtVertex.jets = cms.InputTag("ak5PFJets")


switchJetCollection(process,cms.InputTag('ak5PFJets'),
                 doJTA        = True,
                 doBTagging   = True,
                 jetCorrLabel = ('AK5PF', jetEnCorr),
                 doType1MET   = False,
                 genJetCollection=cms.InputTag("ak5GenJets"),
                 doJetID      = True
                 )

###################################################
# load the PU JetID sequence
###################################################

process.load("RecoJets.JetProducers.pujetidsequence_cff")

#####################################
# compute the tau spinner weights
#####################################

process.load("TauSpinnerInterface.TauSpinnerInterface.TauSpinner_cfi")


###################################################
# debug info including productId will be printed
###################################################

process.printEventContent = cms.EDAnalyzer("EventContentAnalyzer")

###################################################
# setup electron pfIsolation, without this the
# standard PAT access via chargedHadronIso etc.
# will return -1
###################################################
from PhysicsTools.PatAlgos.tools.pfTools import *

process.patElectrons.pfElectronSource = 'particleFlow'
process.patElectrons.embedTrack = True
process.eleIsoSequence = setupPFElectronIso(process, 'gsfElectrons', '')
process.muIsoSequence  = setupPFMuonIso(process, 'muons', '')
adaptPFIsoMuons(process, applyPostfix(process,"patMuons",""), '')
adaptPFIsoElectrons(process, applyPostfix(process,"patElectrons",""), '')



usePFIso(process)


###################################################
# the new Tau ID
###################################################
process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")

from PhysicsTools.PatAlgos.tools.tauTools import *
switchToPFTauHPS(process)

#########################
# embedded sample settings
#########################

if isNonTopEmbeddedSample_ or isTopEmbeddedSample_:
  print "EMBEDDED SETTING "
  process.hpsPFTauPrimaryVertexProducer.TrackCollectionTag = cms.InputTag("tmfTracks")

process.cleanPatTaus.preselection = 'pt>17 & abs(eta)<2.4'\
+ '& ( tauID("byLooseCombinedIsolationDeltaBetaCorr3Hits") > 0.5 | tauID("byVLooseIsolationMVA3oldDMwLT") > 0.5 )'\
+ ' & ( tauID("againstElectronLoose")>0.5 | tauID("againstElectronVLooseMVA5")>0.5 )'\
+ ' & ( tauID("againstMuonLoose3")>0.5 | tauID("againstMuonLooseMVA")>0.5 )'


###################################################
# the MVA electron ID
###################################################


process.load('EgammaAnalysis.ElectronTools.electronIdMVAProducer_cfi')
process.mvaID = cms.Sequence(  process.mvaTrigV0 + process.mvaTrigNoIPV0 + process.mvaNonTrigV0 )


process.patElectrons.electronIDSources = cms.PSet(
    mvaTrigV0 = cms.InputTag("mvaTrigV0"),
    mvaNonTrigV0 = cms.InputTag("mvaNonTrigV0"),
    mvaTrigNoIPV0 = cms.InputTag("mvaTrigNoIPV0"),
    )


process.patConversions = cms.EDProducer("PATConversionProducer",
                                        # input collection
                                        # this should be whatever the final analysis-level
                                        # electrons are
                                        electronSource = cms.InputTag("cleanPatElectrons")
                                        )




###################################################
# apply selection cuts on physics objects
# to keep that PATtuple to a reasonable size
###################################################

#from PhysicsTools.PatAlgos.cleaningLayer1.cleanPatCandidates_cff import *
from PhysicsTools.PatAlgos.selectionLayer1.tauSelector_cfi import *
process.countMyPatTaus = selectedPatTaus.clone(src = 'cleanPatTaus',
            cut = cms.string("pt>17 && abs(eta)<2.4"+
            " && ( tauID('byLooseCombinedIsolationDeltaBetaCorr3Hits') > 0.5 || tauID('byVLooseIsolationMVA3oldDMwLT') > 0.5 )"+
            " && ( tauID('againstElectronLoose')>0.5 || tauID('againstElectronVLooseMVA5')>0.5 )"+
            " && ( tauID('againstMuonLoose3')>0.5 || tauID('againstMuonLooseMVA')>0.5 )")
                                                )


from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
process.myCleanPatMuons = selectedPatMuons.clone(src = 'cleanPatMuons',
cut = cms.string("pt > 10"+
                 " && abs(eta) < 2.4"
                +" && isPFMuon"
                +" && isTrackerMuon "
                +" && isGlobalMuon "
                +" && (pfIsolationR04.sumChargedParticlePt +"
                +"max(pfIsolationR04.sumNeutralHadronEt+pfIsolationR04.sumPhotonEt-0.5*pfIsolationR04.sumPUPt,0.0))/pt < 0.3"
                )
                                                  )

#########################################################################
# cleanPatElectron passing selection counter
#########################################################################
# we count those electrons in cleanPatElectrons that pass the following ID,
# but keep the entire collection as we need to veto diElectron
# events using looser cuts (could change this later)

from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
process.countMyPatElectrons = selectedPatElectrons.clone(src = 'cleanPatElectrons',
      cut = cms.string("et > 20 * 0.9"+
                       " && gsfTrack.trackerExpectedHitsInner.numberOfLostHits == 0"+
                       " && abs(eta) < 2.1 * 1.1" +
                       " && electronID('mvaNonTrigV0') >= 0.85 " +
                       " && passConversionVeto " +
                       " && (chargedHadronIso + max(neutralHadronIso+photonIso-0.5*puChargedHadronIso,0.0))/pt < 0.2 "
                      )
                                                        )



###################################################
# require an eTau or MuTau pair in the event
###################################################


process.countGoodPairs = cms.EDFilter("PatMuonTauOrElectronTauFilter",
  electronSource = cms.InputTag("countMyPatElectrons"),
  muonSource     = cms.InputTag("myCleanPatMuons"),
  tauSource      = cms.InputTag("countMyPatTaus"),
  countElectronTaus = cms.bool(True),
  countMuonTaus     = cms.bool(True),
  filter = cms.bool(True)
)


##################################################
# stuff needed for the embedded samples
##################################################

process.load('RecoJets.JetAssociationProducers.ak5JTA_cff')

from PhysicsTools.PatAlgos.tools.trigTools import *
switchOnTrigger( process )


if isNonTopEmbeddedSample_ or isTopEmbeddedSample_:
  print "EMBEDDED SETTING "
  process.patTriggerEvent.processName = 'HLT'



if runOnMC_ and not isNonTopEmbeddedSample_:
    process.load("RecoJets.Configuration.GenJetParticles_cff")
    process.load("RecoJets.Configuration.RecoGenJets_cff")
    process.genJetsNoNu = cms.Sequence(process.genParticlesForJetsNoNu* process.ak5GenJetsNoNu)
    process.patDefaultSequence.replace(process.patJetGenJetMatch, process.genJetsNoNu* process.patJetGenJetMatch)
    process.patJetGenJetMatch.matched = cms.InputTag("ak5GenJetsNoNu")





##################################################
# Let it run
###################################################
process.p = cms.Path(process.UserSpecifiedData)
process.p *= process.VertexPresent
process.p *= process.PFTau
process.p *= process.pfNoPileUpSequence
process.p *= process.pfAllMuons
process.p *= process.pfParticleSelectionSequence
process.p *= process.eleIsoSequence
process.p *= process.muIsoSequence
process.p *= process.recoTauClassicHPSSequence

# always rerun b-tagging before the pat default seq.
process.p *= process.ak5JetTracksAssociatorAtVertex
process.p *= process.btagging

process.p *= process.patDefaultSequence

process.p *= process.patConversions
process.p *= process.puJetIdSqeuence
process.p *= process.countMyPatTaus
process.p *= process.countMyPatElectrons
process.p *= process.myCleanPatMuons



if FilterEvents_:
  process.p *= process.countGoodPairs


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
