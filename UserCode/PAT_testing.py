import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patTemplate_cfg import *
from PhysicsTools.PatAlgos.tools.coreTools import *
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
