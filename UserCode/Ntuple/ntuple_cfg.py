import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
              'file:/uscms/home/shalhout/1stSteps/Git2/DemoTauCode/CMSSW_5_3_14/src/patTuple_testing.root'
    )
)

process.myProducerLabel = cms.EDProducer('Ntuple'
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('NtupleFile.root')
)


process.p = cms.Path(process.myProducerLabel)

process.e = cms.EndPath(process.out)
