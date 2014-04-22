import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100



process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )


process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/uscms/home/shalhout/1stSteps/Git2/DemoTauCode/CMSSW_5_3_14/src/patTuple_testing.root'
    )
)


process.demo = cms.EDAnalyzer('MuonTestAnalysis',
#muonSrc = cms.untracked.InputTag("cleanPatMuons"),
muonSrc = cms.untracked.InputTag("selectedPatMuons"),
vertexSrc = cms.untracked.InputTag("bestVertex")


                              )



process.p = cms.Path(process.demo)
