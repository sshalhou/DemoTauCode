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
                tauSrc =cms.untracked.InputTag('selectedPatTaus')
                                                   )

process.TupleMuonTaus = cms.EDProducer('TupleMuonTauProducer' ,
                tauSrc=cms.InputTag('TupleTaus','TupleTaus','Ntuple'),
                muonSrc=cms.InputTag('TupleMuons','TupleMuons','Ntuple'),
                mvametSrc = cms.untracked.InputTag("pfMEtMVA"),
                PAR1=cms.double(321.),
                PAR2=cms.string("TupleMuonTaus-Nominal")
                                     )




process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('JetMETCorrections.Configuration.JetCorrectionProducers_cff')
process.load('JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_cff')
process.GlobalTag.globaltag = 'START53_V15::All'


process.calibratedAK5PFJetsForPFMEtMVA = cms.EDProducer('PFJetCorrectionProducer',
    src = cms.InputTag('ak5PFJets'),
    correctors = cms.vstring("ak5PFL1FastL2L3") # NOTE: use "ak5PFL1FastL2L3" for MC / "ak5PFL1FastL2L3Residual" for Data
)


process.pfMEtMVAsequence  = cms.Sequence(
#    (isomuonseq+isotauseq+isoelectronseq)*
    process.calibratedAK5PFJetsForPFMEtMVA*
    pfMEtMVA
    )


process.out = cms.OutputModule("PoolOutputModule",
fileName = cms.untracked.string('NtupleFile.root'),
outputCommands = cms.untracked.vstring('drop *')
#SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')
)



#################################
# keep everything produced by Ntuple
#################################
process.out.outputCommands +=['keep *_*_*_Ntuple']


process.p = cms.Path(process.myProducerLabel+process.TupleMuons*process.TupleTaus*process.TupleMuonTaus+process.pfMEtMVAsequence)

process.e = cms.EndPath(process.out)
