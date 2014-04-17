import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patTemplate_cfg import *
from PhysicsTools.PatAlgos.tools.coreTools import *
from PhysicsTools.PatAlgos.tools.trackTools import *
from PhysicsTools.PatAlgos.tools.pfTools import *
from PhysicsTools.PatAlgos.tools.tauTools import *
########################################################################################################
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(5)
########################################################################################################


###################################################
# use PF isolation
###################################################

usePFIso(process)

# if the sample does not contain value map of PF candidate "particleFlow:electrons", use following line.
# this appears to be the case for our test sample
process.patElectrons.pfElectronSource = 'particleFlow'

###################################################
# keep beamspot (may be needed for electron ID)
###################################################

process.out.outputCommands +=['keep *_offlineBeamSpot*_*_*']


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
# store electrons, filter if needed
###################################################


process.load('EgammaAnalysis.ElectronTools.electronIdMVAProducer_cfi')
process.mvaID = cms.Sequence(  process.mvaTrigV0 + process.mvaNonTrigV0 + process.mvaTrigNoIPV0 )

process.patElectrons.electronIDSources = cms.PSet(mvaTrigV0 = cms.InputTag("mvaTrigV0"),
                                                  mvaNonTrigV0 = cms.InputTag("mvaNonTrigV0"),
                                                  mvaTrigNoIPV0 = cms.InputTag("mvaTrigNoIPV0"),
                                                  )

#add pat conversions
process.patConversions = cms.EDProducer("PATConversionProducer",
                                        electronSource = cms.InputTag("gsfElectrons")
                                        )

# just here for demo purposes
from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
process.FilterElectron = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                                   cut = 'et > 0.0'
                                                    )


from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
process.FilterElectronCount  = countPatElectrons.clone(src = 'FilterElectron', minNumber = 1, maxNumber = 1000)


## define the MVA+Filter sequence
process.electronSequence = cms.Path(
    process.mvaID *
    process.patDefaultSequence*
    process.patConversions*
    process.VertexPresent*
    process.FilterElectron *
    process.FilterElectronCount
    )

process.out.outputCommands +=['keep *_patConversions*_*_*']
# not sure the electron cut ID works with patConversions
# so am including the next line just to be safe
process.out.outputCommands +=['keep *_conversions*_*_*']

# while the 2013 H->tau tau page says "only use the MVA for the ID"
# it also lists selection cuts that seem to be applicable to
# the GsfElectron collection, therefore we keep them
process.out.outputCommands +=['keep *_gsfElectrons*_*_*']



###################################################
# Store the Muons (for some reason these need to be
# after the Electrons or I get problems ...)
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
# add in hadronic taus
# based on
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePFTauID#5_3_12_and_higher
###################################################


process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")

switchToPFTauHPS(process)

## define the path

#process.tauStep6 = cms.Path(process.recoTauClassicHPSSequence+process.PFTau+process.patDefaultSequence)

# not really sure this is doing anything; may just want to omit it
from PhysicsTools.PatAlgos.selectionLayer1.tauCountFilter_cfi import *
process.TauCount  = countPatTaus.clone(src = 'selectedPatTaus', minNumber = 1, maxNumber = 10000)


process.tauSequence = cms.Path(process.VertexPresent *
                              process.recoTauClassicHPSSequence*
                              process.PFTau*
                              process.patDefaultSequence*
                              process.TauCount
                               )


###################################################
# MVA MET
###################################################


process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('JetMETCorrections.Configuration.JetCorrectionProducers_cff')
process.load('JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_cff')
process.GlobalTag.globaltag = 'START53_V15::All'

process.mvamet = cms.Sequence(process.pfMEtMVAsequence)

### To add the Jet Id
#+process.pileupJetIdProducer)

process.load('RecoMET.METProducers.mvaPFMET_cff_leptons')
cms.Sequence(process.pfMEtMVAequence*...)
#This will produce 1 object of type reco::PFMET for each event.
#pat::MET objects can be produced by the following configuration:
process.patPFMetByMVA = process.patMETs.clone(
    metSource = cms.InputTag('pfMEtMVA'),
    addMuonCorrections = cms.bool(False),
    genMETSource = cms.InputTag('genMetTrue')
)


process.mvametpath   = cms.Path(process.mvamet*process.patPFMetByMVA)
process.out.outputCommands +=['keep *_pfMEtMVA*_*_*']



###################################################
# using SelectEvents, you can filter on the paths (sequences)
# defined above; there will be a pass/fail report at the
# end of the process
###################################################
process.out.SelectEvents.SelectEvents = ['tauSequence','muonSequence','electronSequence']

########################################################################################################
process.out.fileName = 'patTuple_testing.root'
process.source.fileNames=['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/'+
                          'GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/'+
                          'PU_S10_START53_V7A-v1/0000/00E903E2-9FE9-E111-8B1E-003048FF86CA.root']

process.maxEvents.input = 100
