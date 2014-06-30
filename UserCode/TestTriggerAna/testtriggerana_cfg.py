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


process.demo = cms.EDAnalyzer('TestTriggerAna',
electronSrc = cms.untracked.InputTag("cleanPatElectrons"),
muonSrc = cms.untracked.InputTag("cleanPatMuons"),
tauSrc = cms.untracked.InputTag("cleanPatTaus"),
triggerEventSrc = cms.untracked.InputTag("patTriggerEvent"),
eTrigMatchEle20Src = cms.untracked.string("eTrigMatchEle20"),
eTrigMatchEle22Src = cms.untracked.string("eTrigMatchEle22"),
eTrigMatchEle27Src = cms.untracked.string("eTrigMatchEle27"),
muTrigMatchMu17Src = cms.untracked.string("muTrigMatchMu17"),
muTrigMatchMu18Src = cms.untracked.string("muTrigMatchMu18"),
muTrigMatchMu24Src = cms.untracked.string("muTrigMatchMu24"),
tauTrigMatchMu17Src = cms.untracked.string("tauTrigMatchMu17"),
tauTrigMatchMu18Src = cms.untracked.string("tauTrigMatchMu18"),
tauTrigMatchMu24Src = cms.untracked.string("tauTrigMatchMu24"),
tauTrigMatchEle20Src = cms.untracked.string("tauTrigMatchEle20"),
tauTrigMatchEle22Src = cms.untracked.string("tauTrigMatchEle22"),
tauTrigMatchEle27Src = cms.untracked.string("tauTrigMatchEle27"),

                              )


process.p = cms.Path(process.demo)
