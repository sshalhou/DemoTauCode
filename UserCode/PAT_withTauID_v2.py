import FWCore.ParameterSet.Config as cms

## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

from PhysicsTools.PatAlgos.tools.coreTools import *


#-------------------------------------------------
# selection step 1: vertex filter
#-------------------------------------------------

# vertex filter
process.Step1VertexPresent = cms.EDFilter("VertexSelector",
                             src = cms.InputTag("offlinePrimaryVertices"),
                             cut = cms.string("!isFake && ndof > 4 && abs(z) < 15 && position.Rho < 2"),
                             filter = cms.bool(True),
                             )

#-------------------------------------------------
# selection steps 2 and 3: muon selection
#-------------------------------------------------

from PhysicsTools.PatAlgos.cleaningLayer1.muonCleaner_cfi import *
process.Step2GlobalPFMuons = cleanPatMuons.clone(preselection =
                                               'isGlobalMuon &'
                                               'isPFMuon'
                                               )





from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
process.Step3GlobalPFMuons1to1000 = countPatMuons.clone(src = 'Step2GlobalPFMuons', minNumber = 1, maxNumber = 1000)

#-------------------------------------------------
# paths
#-------------------------------------------------

process.muonSequence = cms.Path(process.Step1VertexPresent *
                                 process.patDefaultSequence *
                                 process.Step2GlobalPFMuons *
                                 process.Step3GlobalPFMuons1to1000
                                 )


process.out.SelectEvents.SelectEvents = ['muonSequence']



############################
process.source.fileNames=['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/00E903E2-9FE9-E111-8B1E-003048FF86CA.root']

process.maxEvents.input = 100

process.out.fileName = 'patTuple_topSelection.root'
#
#
#
#
#
