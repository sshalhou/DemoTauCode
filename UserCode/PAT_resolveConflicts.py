
########################################################################################################
import FWCore.ParameterSet.Config as cms
########################################################################################################

###################################################
# Import skeleton
###################################################
from PhysicsTools.PatAlgos.patTemplate_cfg import *

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

runOnMC = True
if runOnMC:
  process.GlobalTag.globaltag = 'START53_V23::All'
else:
  process.GlobalTag.globaltag = 'SOMETHING_FOR_DATA::All'

########################################################################################################
# Setup PF2PAT (for now we will not run both PAT and PF2PAT, everything will be PF2PAT)
########################################################################################################

###################################################
# tau discriminators must be re-run
###################################################
process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")
process.load("PhysicsTools.PatAlgos.patSequences_cff")

###################################################
# setup PF2PAT, empty postfix means
# only PF2PAT and not both PAT + PF2PAT
###################################################
from PhysicsTools.PatAlgos.tools.pfTools import *

postfix = ""
jetAlgo = "AK5"
usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo, runOnMC=runOnMC, postfix=postfix)


###################################################
# rm MC matching if DATA
###################################################

if not runOnMC:
  removeMCMatchingPF2PAT( process, '' )
########################################################################################################
# Include a vertex filter and identify the best vertex
########################################################################################################

from PhysicsTools.PatAlgos.tools.trackTools import *

###################################################
# Store the Vertex Collection
# filtering is possible at this
# stage (currently requiring at least one)
###################################################

process.VertexPresent = cms.EDFilter("VertexSelector",
                             src = cms.InputTag("offlinePrimaryVertices"),
                             cut = cms.string("!isFake && ndof > 4 && abs(z) < 15 && position.Rho < 2"),
                             filter = cms.bool(True),
                             )

process.out.outputCommands +=['keep *_offlinePrimaryVertices*_*_*']

###################################################
# select and store the 'best' vertex
###################################################

makeTrackCandidates(process,
    label        = 'TrackCands',
    tracks       = cms.InputTag('generalTracks'),
    particleType = 'pi+',
    preselection = 'pt > 10',
    selection    = 'pt > 10',
    isolation    = {'tracker':0.3, 'ecalTowers':0.3, 'hcalTowers':0.3},
    isoDeposits  = [],
    mcAs         = 'muon'
)

## select best vertex
process.bestVertex = cms.EDFilter(
    "PATSingleVertexSelector",
    mode      = cms.string("nearestToCandidate"),
    fallbacks = cms.vstring("fromCandidate", "beamSpot"),
    vertices              = cms.InputTag("offlinePrimaryVerticesWithBS"),
    vertexPreselection    = cms.vstring("(chi2prob(chi2,ndf) > 0.01) && (trackSize >= 3)"),
    candidates            = cms.VInputTag(cms.InputTag('gsfElectrons'), cms.InputTag('muons')),
    candidatePreselection = cms.string("pt > 5"),
    beamSpot              = cms.InputTag('offlineBeamSpot'),
)

## produce vertex associations
process.patTrackVertexInfo = cms.EDProducer(
    "PATVertexAssociationProducer",
    candidates = cms.VInputTag(
    cms.InputTag('gsfElectrons'),
    cms.InputTag('muons'),
    cms.InputTag('patAODTrackCands'),
    ),
    useTracks = cms.bool(True),
    vertices  = cms.InputTag('bestVertex'),
)


# add modules to the default sequence right after the patAODTrackCands

#process.patDefaultSequence.replace(process.patAODTrackCands,
getattr(process,"patPF2PATSequence"+postfix).replace(process.patAODTrackCands,
                                   process.patAODTrackCands *
                                   process.bestVertex *
                                   process.patTrackVertexInfo
                                   )


## add it to the track candidates
process.patTrackCands.vertexing = cms.PSet(
    vertexAssociations = cms.InputTag("patTrackVertexInfo"),
)

## add generic tracks to the output file
#process.out.outputCommands.append('keep *_selectedPatTrackCands_*_*')
#process.out.outputCommands.append('keep *_patTrackVertexInfo_*_*')
process.out.outputCommands.append('keep *_bestVertex_*_*')





##################################################
# Let it run
###################################################
process.p = cms.Path(        process.VertexPresent
                             *getattr(process,"patPF2PATSequence"+postfix)
                                  )
if not postfix == "":
    process.p += process.recoTauClassicHPSSequence # re-run tau discriminators (new version)
    process.p += process.patDefaultSequence

########################################################################################################


process.out.fileName = 'patTuple_testing.root'
process.source.fileNames=['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/'+
                          'GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/'+
                          'PU_S10_START53_V7A-v1/0000/00E903E2-9FE9-E111-8B1E-003048FF86CA.root']

process.maxEvents.input = 100
########################################################################################################
