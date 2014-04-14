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

#------------------
# CutLevel_2 : muon selection (just a test for now)
#------------------

#-------------------------------------------------
# selection steps 3 and 4: muon selection
#-------------------------------------------------

from PhysicsTools.PatAlgos.cleaningLayer1.muonCleaner_cfi import *
process.isolatedMuons010 = cleanPatMuons.clone(preselection =
                                               'isGlobalMuon & isTrackerMuon &'
                                               'pt > 20. &'
                                               'abs(eta) < 2.1 &'
                                               '(trackIso+caloIso)/pt < 0.1 &'
                                               'innerTrack.numberOfValidHits > 10 &'
                                               'globalTrack.normalizedChi2 < 10.0 &'
                                               'globalTrack.hitPattern.numberOfValidMuonHits > 0 &'
                                               'abs(dB) < 0.02'
                                               )

process.isolatedMuons010.checkOverlaps = cms.PSet(
        jets = cms.PSet(src       = cms.InputTag("goodJets"),
                        algorithm = cms.string("byDeltaR"),
                        preselection        = cms.string(""),
                        deltaR              = cms.double(0.3),
                        checkRecoComponents = cms.bool(False),
                        pairCut             = cms.string(""),
                        requireNoOverlaps   = cms.bool(True),
                        )
            )
process.isolatedMuons005 = cleanPatMuons.clone(src = 'isolatedMuons010',
                                               preselection = '(trackIso+caloIso)/pt < 0.05'
                                               )

process.vetoMuons = cleanPatMuons.clone(preselection =
                                        'isGlobalMuon &'
                                        'pt > 10. &'
                                        'abs(eta) < 2.5 &'
                                        '(trackIso+caloIso)/pt < 0.2'
                                        )

from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
process.step3a = countPatMuons.clone(src = 'isolatedMuons005', minNumber = 1, maxNumber = 1)
process.step3b = countPatMuons.clone(src = 'isolatedMuons010', minNumber = 1, maxNumber = 1)
process.step4  = countPatMuons.clone(src = 'vetoMuons', maxNumber = 1)

process.muonSequence = cms.Path(process.step3b *
                                process.patDefaultSequence
                                 )

process.out.SelectEvents.SelectEvents = ['muonSequence']

process.GlobalTag.globaltag = 'START53_V7G::All' ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)


process.source.fileNames = ['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/00E903E2-9FE9-E111-8B1E-003048FF86CA.root']
process.maxEvents.input = 100
process.out.fileName = 'patTuple_testSelection.root'
