import FWCore.ParameterSet.Config as cms

process = cms.Process("analysis")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(10)
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('JetMETCorrections.Configuration.JetCorrectionProducers_cff')
process.load('JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_cff')

#process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
#process.load('pharris.MVAMet.metProducerSequence_cff')
#process.load('JetMETCorrections.METPUSubtraction.pileupJetIdMVASequence_cff')

#process.GlobalTag.globaltag = 'GR_R_42_V23::All'
#process.GlobalTag.globaltag = 'MC_44_V12::All'
#process.GlobalTag.globaltag = 'MC_44_V12::All'
process.GlobalTag.globaltag = 'START53_V15::All'



############################
process.source.fileNames=['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/00E903E2-9FE9-E111-8B1E-003048FF86CA.root']



process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )


process.output = cms.OutputModule("PoolOutputModule",
                                  outputCommands = cms.untracked.vstring('keep *'),
                                  fileName = cms.untracked.string("testMETMVA.root")
                                  )

process.ana      = cms.Sequence(process.pfMEtMVAsequence)
process.p        = cms.Path(process.ana)
process.outpath  = cms.EndPath(process.output)

### To add the Jet Id
#+process.pileupJetIdProducer)
