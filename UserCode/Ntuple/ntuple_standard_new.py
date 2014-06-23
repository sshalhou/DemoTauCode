import FWCore.ParameterSet.Config as cms
process = cms.Process("Ntuple")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )




myfilelist = cms.untracked.vstring()
myfilelist.extend(['file:/uscms/home/shalhout/no_backup/patTuple_testing.root'])

process.source = cms.Source ("PoolSource",
                      fileNames=myfilelist,
                      skipEvents=cms.untracked.uint32(0)
                             )




process.myProducerLabel = cms.EDProducer('Ntuple')
#################################


##########################
# diMuon Veto
##########################

process.isDiMuonEvent = cms.EDFilter("DiMuonFilter",
  muonSource     = cms.InputTag("myCleanPatMuons"),
  vertexSource      = cms.InputTag("offlinePrimaryVertices"),
  filter = cms.bool(True)
)



##########################
# Nominal Systematics    #
##########################
process.TupleMuonsNominal = cms.EDProducer('TupleMuonProducer' ,
                muonSrc =cms.InputTag('myCleanPatMuons'),
                vertexSrc =cms.InputTag('offlinePrimaryVertices'),
                NAME=cms.string("TupleMuonsNominal")
                                     )

process.TupleTausNominal = cms.EDProducer('TupleTauProducer' ,
                tauSrc =cms.InputTag('cleanPatTaus'),
                NAME=cms.string("TupleTausNominal")
                                                   )




process.TupleMuonTausNominal = cms.EDProducer('TupleMuonTauProducer' ,
                tauSrc=cms.InputTag('TupleTausNominal','TupleTausNominal','Ntuple'),
                muonSrc=cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','Ntuple'),
                mvametSrc = cms.InputTag("pfMEtMVA"),
                genSrc = cms.InputTag("genParticles"),
                iFluc=cms.double(0.0),
                iScale=cms.double(0.0),
                jetSrc = cms.InputTag("cleanPatJets"),
                puJetIdMVASrc = cms.InputTag('puJetMva','full53xDiscriminant','PAT'),
                puJetIdFlagSrc = cms.InputTag('puJetMva','full53xId','PAT'),
                NAME=cms.string("TupleMuonTausNominal"),
                doSVFit=cms.bool(True)
                                     )


#################################
process.out = cms.OutputModule("PoolOutputModule",
fileName = cms.untracked.string('NtupleFile.root'),
outputCommands = cms.untracked.vstring('drop *')
#SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')
)



#################################
# keep everything produced by Tuepl-Ntuple
#################################
process.out.outputCommands +=['keep Tuple*_*_*_Ntuple']


#################################
# keep UserSpecifiedData
#################################
process.out.outputCommands +=['keep TupleUserSpecifiedDatas_UserSpecifiedData_TupleUserSpecifiedData_PAT']



process.p = cms.Path(process.myProducerLabel+
      #process.pfMEtMVANominal+
      process.TupleMuonsNominal*process.TupleTausNominal*process.TupleMuonTausNominal
      #+process.metUncertaintySequence+
      #process.TupleTausTauEnDown*process.TupleMuonTausTauEnDown
      #+process.TupleMuonTausRecoilUp
      #+process.TupleMuonTausRecoilDown
      #+process.TupleMuonTausRecoilResUp
      #+process.TupleMuonTausRecoilResDown
                     )

process.e = cms.EndPath(process.out)
