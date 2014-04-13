import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100



process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/uscms/home/shalhout/1stSteps/TauID/CMSSW_5_3_12/src/MC_1.root'
    )
)

process.demo = cms.EDAnalyzer('DemoAna',
tauSrc = cms.untracked.InputTag("cleanPatTaus"),
muonSrc = cms.untracked.InputTag("cleanPatMuons"),
pvertexSrc = cms.untracked.InputTag("cleanPatMuons")
)


process.p = cms.Path(process.demo)
