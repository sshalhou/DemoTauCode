import FWCore.ParameterSet.Config as cms

## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

from PhysicsTools.PatAlgos.tools.coreTools import *


#-------------------------------------------------
# selection step 1: vertex filter
#-------------------------------------------------

# vertex filter
process.step1 = cms.EDFilter("VertexSelector",
                             src = cms.InputTag("offlinePrimaryVertices"),
                             cut = cms.string("!isFake && ndof > 4 && abs(z) < 15 && position.Rho < 2"),
                             filter = cms.bool(True),
                             )

#-------------------------------------------------
# selection steps 2 and 3: muon selection
#-------------------------------------------------

from PhysicsTools.PatAlgos.cleaningLayer1.muonCleaner_cfi import *
process.step2_MyTightMuons = cleanPatMuons.clone(preselection =
                                               'isTightMuon'
                                               )





from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
process.step3 = countPatMuons.clone(src = 'step2_MyTightMuons', minNumber = 1, maxNumber = 1000)

#-------------------------------------------------
# paths
#-------------------------------------------------

process.looseSequence = cms.Path(process.step1 *
                                 process.patDefaultSequence *
                                 process.step2_MyTightMuons *
                                 process.step3
                                 )


process.out.SelectEvents.SelectEvents = ['looseSequence']



############################
process.source.fileNames=['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/00E903E2-9FE9-E111-8B1E-003048FF86CA.root']

process.maxEvents.input = 100

process.out.fileName = 'patTuple_topSelection.root'
#
#
#
#
#
