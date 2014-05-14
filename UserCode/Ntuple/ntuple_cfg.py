import FWCore.ParameterSet.Config as cms

process = cms.Process("Ntuple")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
# replace 'myfile.root' with the source file you want to use
fileNames = cms.untracked.vstring(
'file:/uscms/home/shalhout/1stSteps/Git2/DemoTauCode/CMSSW_5_3_14/src/patTuple_testing.root'
)
)

process.myProducerLabel = cms.EDProducer('Ntuple',
muonSrc = cms.untracked.InputTag("selectedPatMuons")
)


#process.NtupleMuons = cms.EDProducer('NtupleMuons' ,muonSrc =cms.untracked.InputTag('selectedPatMuons') )
process.TupleMuons = cms.EDProducer('TupleMuonProducer' ,
                muonSrc =cms.untracked.InputTag('selectedPatMuons'),
                vertexSrc =cms.untracked.InputTag('offlinePrimaryVertices')
                                     )

process.TupleTaus = cms.EDProducer('TupleTauProducer' ,
                tauSrc =cms.untracked.InputTag('selectedPatTaus'),
                #muonSrc =cms.untracked.InputTag('TupleMuons')
                muonSrc=cms.InputTag(“TupleMuons”)

                                     )


#process.TrackTrackPoints = cms.EDProducer('TrackAndPointsProducer' ,src =cms.InputTag('generalTracks') )


process.out = cms.OutputModule("PoolOutputModule",
fileName = cms.untracked.string('NtupleFile.root'),
outputCommands = cms.untracked.vstring('drop *')
#SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')
)



#################################
# keep everything produced by Ntuple
#################################
process.out.outputCommands +=['keep *_*_*_Ntuple']


process.p = cms.Path(process.myProducerLabel+process.TupleMuons*process.TupleTaus)

process.e = cms.EndPath(process.out)
