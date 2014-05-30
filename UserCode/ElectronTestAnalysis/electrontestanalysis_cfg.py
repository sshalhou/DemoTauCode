import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/uscms/home/shalhout/no_backup/patTuple_testing.root'
    )
)

#process.demo = cms.EDAnalyzer('ElectronTestAnalysis'
#)


process.demo = cms.EDAnalyzer('ElectronTestAnalysis',
electronSrc = cms.untracked.InputTag("cleanPatElectrons"),
gsfelectronSrc = cms.untracked.InputTag("gsfElectrons"),
beamspotSrc = cms.untracked.InputTag("offlineBeamSpot"),
patconversionSrc = cms.untracked.InputTag("patConversions"),
recoconversionSrc = cms.untracked.InputTag("conversions")

                              )


process.p = cms.Path(process.demo)
