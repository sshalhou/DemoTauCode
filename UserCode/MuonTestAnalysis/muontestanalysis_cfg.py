import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                          cms.untracked.vstring('file:/uscms/home/shalhout/1stSteps/Git2/'+
                          'DemoTauCode/CMSSW_5_3_14/src/patTuple_testing.root')
                          )

process.demo = cms.EDAnalyzer('MuonTestAnalysis')


process.demo = cms.EDAnalyzer('MuonTestAnalysis',
muonSrc = cms.untracked.InputTag("cleanPatMuons")
                              )



process.p = cms.Path(process.demo)
