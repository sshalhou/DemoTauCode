########################################################################################################
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patTemplate_cfg import *
from PhysicsTools.PatAlgos.tools.helpers import *
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
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
WillRunSVFit_ = False


doNotRequireFullIdForLeptons_ = False # setting to true means more SVFIt calls
printListOfModules_ = False
CheckMemoryUsage_ = False


FilterEvents_ = True
DropSelectedPatObjects_ = True
KeepAll_ = True
PrintProductIDs_ = False


##########################################
# the following 3 parameters set the first X  leptons in the
# lepton collections
# to consider for building the final states, any additional
# leptons will be ignored by the eTau and muTau producers
# all leptons are still considered for the vetos

MAX_ELECTRONS = 7
MAX_MUONS = 7
MAX_TAUS = 7


###########################################
# gen particle sources depend on isNonTopEmbeddedSample
# and isTopEmbeddedSample
# also use alternate pileUp source for tt embedded samples

genSrcInputTag = cms.InputTag('genParticles::SIM')
genTTembeddedSrcInputTag = cms.InputTag('')
pileupSrcInputTag = cms.InputTag('addPileupInfo')


if isNonTopEmbeddedSample_:
  genSrcInputTag = cms.InputTag('genParticles::EmbeddedRECO')
  genTTembeddedSrcInputTag = cms.InputTag('')

elif isTopEmbeddedSample_:
  genSrcInputTag = cms.InputTag('genParticles::EmbeddedRECO')
  genTTembeddedSrcInputTag = cms.InputTag('genParticles::SIM')
  pileupSrcInputTag = cms.InputTag('addPileupInfo::HLT')




###################################
# create a new primary vertex collection
###################################

process.selectedPrimaryVerticesNtuple = cms.EDFilter(
    "VertexSelector",
    src = cms.InputTag('offlinePrimaryVertices'),
    cut = cms.string("isValid & ndof >= 4 & z > -24 & z < +24 & position.Rho < 2."),
    filter = cms.bool(False)
)



##################################################
# will use cleanPatTaus, except for embedded
# where we will set to patTausGenMatched::Ntuple
# below
###################################################

TausToUse = cms.InputTag('cleanPatTaus')

###################################################
# rerun tau - gen matching for embedded samples
###################################################

process.TauGenMatchesForEmbedded = cms.Sequence()
tausToMatch = "cleanPatTaus"

if isNonTopEmbeddedSample_ or isTopEmbeddedSample_:
    print "EMBEDDED STUFF "
    from PhysicsTools.PatAlgos.mcMatchLayer0.tauMatch_cfi import tauMatch, tauGenJetMatch
    process.tauMatchEmbeddedRECO = tauMatch.clone(
    src = cms.InputTag(tausToMatch),
    matched = cms.InputTag("genParticles::EmbeddedRECO")
                 )
    process.TauGenMatchesForEmbedded += process.tauMatchEmbeddedRECO

    from PhysicsTools.JetMCAlgos.TauGenJets_cfi import tauGenJets
    process.tauGenJetsEmbeddedRECO = tauGenJets.clone(
    GenParticles = cms.InputTag("genParticles::EmbeddedRECO")
    )
    process.TauGenMatchesForEmbedded += process.tauGenJetsEmbeddedRECO
    from PhysicsTools.JetMCAlgos.TauGenJetsDecayModeSelectorAllHadrons_cfi import tauGenJetsSelectorAllHadrons
    process.tauGenJetsSelectorAllHadronsEmbeddedRECO = tauGenJetsSelectorAllHadrons.clone(
    src = cms.InputTag("tauGenJetsEmbeddedRECO")
    )
    process.TauGenMatchesForEmbedded += process.tauGenJetsSelectorAllHadronsEmbeddedRECO
    process.tauGenJetMatchEmbeddedRECO = tauGenJetMatch.clone(
    src = cms.InputTag(tausToMatch),
    matched = cms.InputTag("tauGenJetsSelectorAllHadronsEmbeddedRECO")
    )
    process.TauGenMatchesForEmbedded += process.tauGenJetMatchEmbeddedRECO

    process.patTausGenMatched = cms.EDProducer("PATTauGenMatchEmbedder",
    src = cms.InputTag(tausToMatch),
    srcGenParticleMatch = cms.InputTag("tauMatchEmbeddedRECO"),
    srcGenJetMatch = cms.InputTag("tauGenJetMatchEmbeddedRECO")
    )
    process.TauGenMatchesForEmbedded += process.patTausGenMatched
    TausToUse = cms.InputTag('patTausGenMatched')


###################################
# create an ES corrected tau collection
# (only pass this to mva met, since
# trigger matching does not exist)
###################################

process.EsCorrectedTausNominal = cms.EDProducer('EsCorrectedTauProducer' ,
                tauSrc = TausToUse,
                TauESshift=cms.double(1.0),
                NAME=cms.string("EsCorrectedTausNominal")
                                     )


process.EsCorrectedTausUp = cms.EDProducer('EsCorrectedTauProducer' ,
                tauSrc = TausToUse,
                TauESshift=cms.double(1.03),
                NAME=cms.string("EsCorrectedTausUp")
                                     )


process.EsCorrectedTausDown = cms.EDProducer('EsCorrectedTauProducer' ,
                tauSrc = TausToUse,
                TauESshift=cms.double(0.97),
                NAME=cms.string("EsCorrectedTausDown")
                                     )



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

###################################################
# Store the Vertex Collection
# filtering is possible at this
# stage (currently requiring at least one)
###################################################

from PhysicsTools.PatAlgos.tools.trackTools import *

process.VertexPresent = cms.EDFilter("VertexSelector",
                             src = cms.InputTag("offlinePrimaryVertices"),
                             cut = cms.string("!isFake && ndof > 4 && abs(z) < 24 && position.Rho < 2"),
                             filter = cms.bool(True)
                             )




####################################
# setup the MVA MET calculation
#####################################

process.load("JetMETCorrections.Configuration.JetCorrectionServicesAllAlgos_cff")
from JetMETCorrections.Configuration.DefaultJEC_cff import *
if runOnMC_ and not isNonTopEmbeddedSample_:
  process.prefer("ak5PFL1FastL2L3")
else:
  process.prefer("ak5PFL1FastL2L3Residual")

process.load('JetMETCorrections.Configuration.JetCorrectionProducers_cff')
#from RecoMET.METPUSubtraction.mvaPFMET_leptons_cff import pfMEtMVA
from RecoMET.METPUSubtraction.mvaPFMET_cff import calibratedAK5PFJetsForPFMEtMVA
process.load("RecoMET.METPUSubtraction.mvaPFMET_cff")
process.calibratedAK5PFJetsForPFMEtMVA = calibratedAK5PFJetsForPFMEtMVA.clone()

if runOnMC_ and not isNonTopEmbeddedSample_:
  process.calibratedAK5PFJetsForPFMEtMVA.correctors = cms.vstring("ak5PFL1FastL2L3")
else:
  process.calibratedAK5PFJetsForPFMEtMVA.correctors = cms.vstring("ak5PFL1FastL2L3Residual")



##############################
# produce the single electron,
# muon, and tau collections
# that will be used for pair-wise
# mvaMet calculation

singlePatLeptons = cms.Sequence()

for eINDEX in range(MAX_ELECTRONS):
  eModuleName = "cleanPatElectrons%i" % (eINDEX)
  eModule = cms.EDProducer('SinglePatElectronProducer' ,
    electronSrc =cms.InputTag('cleanPatElectrons'),
    INDEX = cms.uint32(eINDEX),
    NAME=cms.string(eModuleName))
  setattr(process, eModuleName, eModule)
  singlePatLeptons += eModule

for mINDEX in range(MAX_MUONS):
  mModuleName = "cleanPatMuons%i" % (mINDEX)
  mModule = cms.EDProducer('SinglePatMuonProducer' ,
    muonSrc =cms.InputTag('cleanPatMuons'),
    INDEX = cms.uint32(mINDEX),
    NAME=cms.string(mModuleName))
  setattr(process, mModuleName, mModule)
  singlePatLeptons += mModule

for tINDEX in range(MAX_TAUS):
  tModuleName = "cleanPatTausNominal%i" % (tINDEX)
  tModule = cms.EDProducer('SinglePatTauProducer' ,
    tauSrc =cms.InputTag('EsCorrectedTausNominal:EsCorrectedTausNominal:PAT'),
    INDEX = cms.uint32(tINDEX),
    NAME=cms.string(tModuleName))
  setattr(process, tModuleName, tModule)
  singlePatLeptons += tModule


for tINDEX in range(MAX_TAUS):
  tModuleName = "cleanPatTausUp%i" % (tINDEX)
  tModule = cms.EDProducer('SinglePatTauProducer' ,
    tauSrc =cms.InputTag('EsCorrectedTausUp:EsCorrectedTausUp:PAT'),
    INDEX = cms.uint32(tINDEX),
    NAME=cms.string(tModuleName))
  setattr(process, tModuleName, tModule)
  singlePatLeptons += tModule

for tINDEX in range(MAX_TAUS):
  tModuleName = "cleanPatTausDown%i" % (tINDEX)
  tModule = cms.EDProducer('SinglePatTauProducer' ,
    tauSrc =cms.InputTag('EsCorrectedTausDown:EsCorrectedTausDown:PAT'),
    INDEX = cms.uint32(tINDEX),
    NAME=cms.string(tModuleName))
  setattr(process, tModuleName, tModule)
  singlePatLeptons += tModule




##################################################
# Let it run
###################################################
process.p = cms.Path(process.UserSpecifiedData)
process.p *= process.VertexPresent
process.p *= process.mvaID
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


###################################################
# add in Trigger Info
###################################################

# Trigger Object Matching

process.load( "PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cff" )

###################################################

process.eTrigMatchEle27 = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                                       src = cms.InputTag( 'cleanPatElectrons' ),
                                                       matched = cms.InputTag( 'patTrigger' ),
                                                       andOr          = cms.bool( False ),
                                                       matchedCuts = cms.string( 'path( "HLT_Ele27*" )' ),
                                                       maxDeltaR = cms.double( 0.5 ),
                                                       resolveAmbiguities = cms.bool( True ),
                                                       resolveByMatchQuality = cms.bool( True )
                                                       )

###################################################

process.eTrigMatchEle20 = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                                       src = cms.InputTag( 'cleanPatElectrons' ),
                                                       matched = cms.InputTag( 'patTrigger' ),
                                                       andOr          = cms.bool( False ),
            matchedCuts = cms.string( 'path( "HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*" )' ),
                                                       maxDeltaR = cms.double( 0.5 ),
                                                       resolveAmbiguities = cms.bool( True ),
                                                       resolveByMatchQuality = cms.bool( True )
                                                       )


###################################################

process.eTrigMatchEle22 = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                                       src = cms.InputTag( 'cleanPatElectrons' ),
                                                       matched = cms.InputTag( 'patTrigger' ),
                                                       andOr          = cms.bool( False ),
            matchedCuts = cms.string( 'path( "HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*" )' ),
                                                       maxDeltaR = cms.double( 0.5 ),
                                                       resolveAmbiguities = cms.bool( True ),
                                                       resolveByMatchQuality = cms.bool( True )
                                                       )

###################################################


process.muTrigMatchMu17 = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                                       src = cms.InputTag( 'cleanPatMuons' ),
                                                       matched = cms.InputTag( 'patTrigger' ),
                                                       andOr          = cms.bool( False ),
            matchedCuts = cms.string( 'path( "HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v*" )' ),
                                                       maxDeltaR = cms.double( 0.5 ),
                                                       resolveAmbiguities = cms.bool( True ),
                                                       resolveByMatchQuality = cms.bool( True )
                                                       )

###################################################

process.muTrigMatchMu18 = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                                       src = cms.InputTag( 'cleanPatMuons' ),
                                                       matched = cms.InputTag( 'patTrigger' ),
                                                       andOr          = cms.bool( False ),
            matchedCuts = cms.string( 'path( "HLT_IsoMu18_eta2p1_LooseIsoPFTau20_v*" )' ),
                                                       maxDeltaR = cms.double( 0.5 ),
                                                       resolveAmbiguities = cms.bool( True ),
                                                       resolveByMatchQuality = cms.bool( True )
                                                       )

###################################################


process.muTrigMatchMu24 = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                                       src = cms.InputTag( 'cleanPatMuons' ),
                                                       matched = cms.InputTag( 'patTrigger' ),
                                                       andOr          = cms.bool( False ),
            matchedCuts = cms.string( 'path( "HLT_IsoMu24*" )' ),
                                                       maxDeltaR = cms.double( 0.5 ),
                                                       resolveAmbiguities = cms.bool( True ),
                                                       resolveByMatchQuality = cms.bool( True )
                                                       )


####################################################

###################################################

process.tauTrigMatchEle20 = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                                       src = cms.InputTag( 'cleanPatTaus' ),
                                                       matched = cms.InputTag( 'patTrigger' ),
                                                       andOr          = cms.bool( False ),
            matchedCuts = cms.string( 'path( "HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*" )' ),
                                                       maxDeltaR = cms.double( 0.5 ),
                                                       resolveAmbiguities = cms.bool( True ),
                                                       resolveByMatchQuality = cms.bool( True )
                                                       )


###################################################

process.tauTrigMatchEle22 = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                                       src = cms.InputTag( 'cleanPatTaus' ),
                                                       matched = cms.InputTag( 'patTrigger' ),
                                                       andOr          = cms.bool( False ),
            matchedCuts = cms.string( 'path( "HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*" )' ),
                                                       maxDeltaR = cms.double( 0.5 ),
                                                       resolveAmbiguities = cms.bool( True ),
                                                       resolveByMatchQuality = cms.bool( True )
                                                       )

###################################################


process.tauTrigMatchMu17 = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                                       src = cms.InputTag( 'cleanPatTaus' ),
                                                       matched = cms.InputTag( 'patTrigger' ),
                                                       andOr          = cms.bool( False ),
            matchedCuts = cms.string( 'path( "HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v*" )' ),
                                                       maxDeltaR = cms.double( 0.5 ),
                                                       resolveAmbiguities = cms.bool( True ),
                                                       resolveByMatchQuality = cms.bool( True )
                                                       )

###################################################

process.tauTrigMatchMu18 = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                                       src = cms.InputTag( 'cleanPatTaus' ),
                                                       matched = cms.InputTag( 'patTrigger' ),
                                                       andOr          = cms.bool( False ),
            matchedCuts = cms.string( 'path( "HLT_IsoMu18_eta2p1_LooseIsoPFTau20_v*" )' ),
                                                       maxDeltaR = cms.double( 0.5 ),
                                                       resolveAmbiguities = cms.bool( True ),
                                                       resolveByMatchQuality = cms.bool( True )
                                                       )

###################################################


process.tauTrigMatchJet320 = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                                       src = cms.InputTag( 'cleanPatTaus' ),
                                                       matched = cms.InputTag( 'patTrigger' ),
                                                       andOr          = cms.bool( False ),
            matchedCuts = cms.string( 'path( "HLT_PFJet320*" )' ),
                                                       maxDeltaR = cms.double( 0.5 ),
                                                       resolveAmbiguities = cms.bool( True ),
                                                       resolveByMatchQuality = cms.bool( True )
                                                       )


###################################################


process.tauTrigMatchEle27 = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                                       src = cms.InputTag( 'cleanPatTaus' ),
                                                       matched = cms.InputTag( 'patTrigger' ),
                                                       andOr          = cms.bool( False ),
                                                       matchedCuts = cms.string( 'path( "HLT_Ele27*" )' ),
                                                       maxDeltaR = cms.double( 0.5 ),
                                                       resolveAmbiguities = cms.bool( True ),
                                                       resolveByMatchQuality = cms.bool( True )
                                                       )

###################################################


process.tauTrigMatchMu24 = cms.EDProducer( "PATTriggerMatcherDRLessByR",
                                                       src = cms.InputTag( 'cleanPatTaus' ),
                                                       matched = cms.InputTag( 'patTrigger' ),
                                                       andOr          = cms.bool( False ),
                                                       matchedCuts = cms.string( 'path( "HLT_IsoMu24*" )' ),
                                                       maxDeltaR = cms.double( 0.5 ),
                                                       resolveAmbiguities = cms.bool( True ),
                                                       resolveByMatchQuality = cms.bool( True )
                                                       )


triggerMatchers = cms.vstring()
triggerMatchers.extend(['eTrigMatchEle20'])
triggerMatchers.extend(['eTrigMatchEle22'])
triggerMatchers.extend(['eTrigMatchEle27'])
triggerMatchers.extend(['muTrigMatchMu17'])
triggerMatchers.extend(['muTrigMatchMu18'])
triggerMatchers.extend(['muTrigMatchMu24'])
triggerMatchers.extend(['tauTrigMatchEle20'])
triggerMatchers.extend(['tauTrigMatchEle22'])
triggerMatchers.extend(['tauTrigMatchEle27'])
triggerMatchers.extend(['tauTrigMatchMu17'])
triggerMatchers.extend(['tauTrigMatchMu18'])
triggerMatchers.extend(['tauTrigMatchMu24'])
triggerMatchers.extend(['tauTrigMatchJet320'])



switchOnTriggerMatching( process, triggerMatchers )
process.out.outputCommands +=['keep *_*patTrigger*_*_*']
process.out.outputCommands +=['keep *_*TriggerResults*_*_*']
process.out.outputCommands +=['keep *_*patTriggerEvent*_*_*']
process.out.outputCommands +=['keep *_*TriggerMatch*_*_*']
##########################


if FilterEvents_:
  process.p *= process.countGoodPairs


if PrintProductIDs_:
  process.p *= process.printEventContent

if runOnMC_:
  process.p *= process.TauSpinnerReco

#####################################
# things formerly in the Ntuple

process.p *= process.selectedPrimaryVerticesNtuple
process.p *= process.TauGenMatchesForEmbedded # will do nothing unless embedded
process.p *= process.EsCorrectedTausNominal
process.p *= process.EsCorrectedTausUp # needed here even for data
process.p *= process.EsCorrectedTausDown # needed here even for data
process.p *= singlePatLeptons




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
