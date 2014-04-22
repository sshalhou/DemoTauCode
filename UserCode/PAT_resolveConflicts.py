
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
########################################################################################################
# Include a vertex filter and identify the best vertex
########################################################################################################

from PhysicsTools.PatAlgos.tools.trackTools import *
from PhysicsTools.PatAlgos.tools.tauTools import *

###################################################
# Store the Vertex Collection
# filtering is possible at this
# stage (currently requiring at least one)
###################################################

#process.VertexPresent = cms.EDFilter("VertexSelector",
#                             src = cms.InputTag("offlinePrimaryVertices"),
#                             cut = cms.string("!isFake && ndof > 4 && abs(z) < 15 && position.Rho < 2"),
#                             filter = cms.bool(True),
#                             )

process.out.outputCommands +=['keep *_offlinePrimaryVertices*_*_*']






##################################################
# Let it run
###################################################
process.DemoTauAna = cms.Path(
                             getattr(process,"patPF2PATSequence"+postfix)
                                  )

#process.p+= process.VertexPresent

if not postfix == "":
    process.DemoTauAna += process.recoTauClassicHPSSequence # re-run tau discriminators (new version)
    process.DemoTauAna += process.patDefaultSequence

########################################################################################################


process.out.fileName = 'patTuple_testing.root'
process.source.fileNames=['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/'+
                          'GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/'+
                          'PU_S10_START53_V7A-v1/0000/00E903E2-9FE9-E111-8B1E-003048FF86CA.root']

process.maxEvents.input = 100
########################################################################################################
