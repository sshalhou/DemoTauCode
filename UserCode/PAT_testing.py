import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patTemplate_cfg import *
from PhysicsTools.PatAlgos.tools.coreTools import *
from PhysicsTools.PatAlgos.tools.trackTools import *
########################################################################################################



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
process.patDefaultSequence.replace(process.patAODTrackCands,
                                   process.patAODTrackCands *
                                   process.bestVertex *
                                   process.patTrackVertexInfo
                                   )


## add it to the track candidates
process.patTrackCands.vertexing = cms.PSet(
    vertexAssociations = cms.InputTag("patTrackVertexInfo"),
)

## add generic tracks to the output file
process.out.outputCommands.append('keep *_selectedPatTrackCands_*_*')
process.out.outputCommands.append('keep *_patTrackVertexInfo_*_*')
process.out.outputCommands.append('keep *_bestVertex_*_*')




###################################################
# Store the Muons
# default H->tau tau uses
# isTightMuon which I can't figure out
# how to apply at this stage since it
# takes vertex as an argument
# instead will filter on Global and PFmuons
# will require at least 1 on the muon path
###################################################


from PhysicsTools.PatAlgos.cleaningLayer1.muonCleaner_cfi import *
process.GlobalPFMuons = cleanPatMuons.clone(preselection =
                                               'isGlobalMuon &'
                                               'isPFMuon'
                                               )


from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
process.GlobalPFMuonsCount = countPatMuons.clone(src = 'GlobalPFMuons', minNumber = 1)



process.muonSequence = cms.Path(process.VertexPresent *
                                 process.patDefaultSequence *
                                 process.GlobalPFMuons *
                                 process.GlobalPFMuonsCount
                                )




###################################################
# using SelectEvents, you can filter on the paths (sequences)
# defined above; there will be a pass/fail report at the
# end of the process
###################################################
process.out.SelectEvents.SelectEvents = ['muonSequence']

########################################################################################################
process.out.fileName = 'patTuple_testing.root'
process.source.fileNames=['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/'+
                          'GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/'+
                          'PU_S10_START53_V7A-v1/0000/00E903E2-9FE9-E111-8B1E-003048FF86CA.root']

process.maxEvents.input = 100
