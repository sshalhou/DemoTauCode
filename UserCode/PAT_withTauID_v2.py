import FWCore.ParameterSet.Config as cms

## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

from PhysicsTools.PatAlgos.tools.coreTools import *


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





from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
process.step3b = countPatMuons.clone(src = 'isolatedMuons010', minNumber = 1, maxNumber = 1000)

#-------------------------------------------------
# paths
#-------------------------------------------------

process.looseSequence = cms.Path(process.patDefaultSequence *
                                 process.isolatedMuons010 *
                                 process.step3b
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
