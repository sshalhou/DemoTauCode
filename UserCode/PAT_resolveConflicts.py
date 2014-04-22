
########################################################################################################
import FWCore.ParameterSet.Config as cms
########################################################################################################

#process = cms.Process("DemoTauAna")

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


###################################################
# load the PU JetID sequence
###################################################
process.load("CMGTools.External.pujetidsequence_cff")

process.out.outputCommands +=['keep *_puJetId*_*_*']
process.out.outputCommands +=['keep *_puJetMva*_*_*']
###################################################
# Store the Vertex Collection
# filtering is possible at this
# stage (currently requiring at least one)
###################################################

from PhysicsTools.PatAlgos.tools.coreTools import *
from PhysicsTools.PatAlgos.tools.trackTools import *

process.VertexPresent = cms.EDFilter("VertexSelector",
                             src = cms.InputTag("offlinePrimaryVertices"),
                             cut = cms.string("!isFake && ndof > 4 && abs(z) < 15 && position.Rho < 2"),
                             filter = cms.bool(True),
                             )

process.out.outputCommands +=['keep *_offlinePrimaryVertices*_*_*']


###################################################
# add info needed for pile-up reweight
####################################################
process.out.outputCommands +=['keep *_addPileupInfo*_*_*']
###################################################

###################################################
# keep beamspot (may be needed for electron ID)
###################################################

process.out.outputCommands +=['keep *_offlineBeamSpot*_*_*']



###################################################
# Store the Muons
###################################################


from PhysicsTools.PatAlgos.cleaningLayer1.muonCleaner_cfi import *
process.GlobalPFMuons = cleanPatMuons.clone(preselection =
                                               'isGlobalMuon &'
                                               'isPFMuon'
                                               )


from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
process.GlobalPFMuonsCount = countPatMuons.clone(src = 'GlobalPFMuons', minNumber = 1)



process.muonSequence = cms.Path(process.VertexPresent *
                                 #process.patDefaultSequence *
                                 getattr(process,"patPF2PATSequence"+postfix)*
                                 process.GlobalPFMuons *
                                 process.GlobalPFMuonsCount
                                )


###################################################
# using SelectEvents, you can filter on the paths (sequences)
# defined above; there will be a pass/fail report at the
# end of the process
###################################################
SelectMuonEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('muonSequence') )
#process.out.SelectEvents.SelectEvents = ['muonSequence']

##################################################
# Let it run, note: we absolutely need
# a path called 'p' unless we edit patTemplate_cfg.py
# which expects p in the selector
###################################################
process.pX = cms.Path(        process.VertexPresent*
                             getattr(process,"patPF2PATSequence"+postfix)*
                             process.puJetIdSqeuence*
                             SelectMuonEvents
                                  )



if not postfix == "":
    process.pX += process.recoTauClassicHPSSequence # re-run tau discriminators (new version)
    process.pX += process.patDefaultSequence


########################################################################################################


process.out.fileName = 'patTuple_testing.root'
process.source.fileNames=['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/'+
                          'GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/'+
                          'PU_S10_START53_V7A-v1/0000/00E903E2-9FE9-E111-8B1E-003048FF86CA.root']

process.maxEvents.input = 100
########################################################################################################
