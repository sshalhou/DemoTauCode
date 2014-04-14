# goal is to create a PATtuple following
# a fairly tight H->tau tau ID, eventually
# leading to a looser version useful for analysis

import FWCore.ParameterSet.Config as cms

## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

#------------------
# CutLevel_1 : vertex filter (taking defaulst from top selection for now)
#------------------
process.CutLevel_1_vertex = cms.EDFilter("VertexSelector",
                             src = cms.InputTag("offlinePrimaryVertices"),
                             cut = cms.string("!isFake && ndof > 4 && abs(z) < 15 && position.Rho < 2"),
                             filter = cms.bool(True),
                             )

from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
process.cut1 = countPatMuons.clone(src = 'isolatedMuons010', minNumber = 1, maxNumber = 1)

#------------------
# CutLevel_2 : muon selection (just a test for now)
#------------------

from PhysicsTools.PatAlgos.cleaningLayer1.muonCleaner_cfi import *
process.NonIsolatedTightMuons = cleanPatMuons.clone(preselection =
                                               'pt > 20'
                                               )
process.step2 = countPatMuons.clone(src = 'NonIsolatedTightMuons', minNumber = 1, maxNumber = 100)


process.muonSequence = cms.Path(process.step2 *
                                process.patDefaultSequence
                                 )

process.out.SelectEvents.SelectEvents = ['muonSequence']

process.GlobalTag.globaltag = 'START53_V7G::All' ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)


process.source.fileNames = ['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/00E903E2-9FE9-E111-8B1E-003048FF86CA.root']
process.maxEvents.input = 100
process.out.fileName = 'patTuple_testSelection.root'
