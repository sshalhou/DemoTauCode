import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/uscms/home/shalhout/no_backup/NtupleFile_susy120_first250000.root'
    )
)

process.demo = cms.EDAnalyzer('SyncTree',
tauSrc = cms.InputTag('TupleTausNominal','TupleTausNominal','Ntuple'),
leptonSrc = cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','Ntuple'),
leptonTauSrc = cms.InputTag('TupleMuonTausNominal','TupleMuonTausNominal','Ntuple'),
NAME = cms.string("muTau") # only muTau or eTau
)


process.p = cms.Path(process.demo)
