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
# diMuon & diElectron Vetoes
##########################

process.isDiMuonEvent = cms.EDFilter("DiMuonFilter",
  muonSource     = cms.InputTag("myCleanPatMuons"),
  vertexSource      = cms.InputTag("offlinePrimaryVerticesWithBS"),
  filter = cms.bool(True)
)


process.isDiElectronEvent = cms.EDFilter("DiElectronFilter",
  electronSource     = cms.InputTag("cleanPatElectrons"),
  vertexSource      = cms.InputTag("offlinePrimaryVerticesWithBS"),
  filter = cms.bool(True)
)


##########################
# Nominal Systematics    #
##########################

process.TupleElectronsNominal = cms.EDProducer('TupleElectronProducer' ,
                electronSrc =cms.InputTag('cleanPatElectrons'),
                vertexSrc =cms.InputTag('offlinePrimaryVerticesWithBS'),
                NAME=cms.string("TupleElectronsNominal"),
                triggerEventSrc = cms.untracked.InputTag("patTriggerEvent"),
                eTrigMatchEle20Src = cms.untracked.string("eTrigMatchEle20"),
                eTrigMatchEle22Src = cms.untracked.string("eTrigMatchEle22"),
                eTrigMatchEle27Src = cms.untracked.string("eTrigMatchEle27")
                                     )

process.TupleMuonsNominal = cms.EDProducer('TupleMuonProducer' ,
                muonSrc =cms.InputTag('myCleanPatMuons'),
                vertexSrc =cms.InputTag('offlinePrimaryVerticesWithBS'),
                NAME=cms.string("TupleMuonsNominal"),
                triggerEventSrc = cms.untracked.InputTag("patTriggerEvent"),
                muTrigMatchMu17Src = cms.untracked.string("muTrigMatchMu17"),
                muTrigMatchMu18Src = cms.untracked.string("muTrigMatchMu18"),
                muTrigMatchMu24Src = cms.untracked.string("muTrigMatchMu24")
                                     )

process.TupleTausNominal = cms.EDProducer('TupleTauProducer' ,
                tauSrc =cms.InputTag('cleanPatTaus'),
                NAME=cms.string("TupleTausNominal"),
                triggerEventSrc = cms.untracked.InputTag("patTriggerEvent"),
                tauTrigMatchMu17Src = cms.untracked.string("tauTrigMatchMu17"),
                tauTrigMatchMu18Src = cms.untracked.string("tauTrigMatchMu18"),
                tauTrigMatchMu24Src = cms.untracked.string("tauTrigMatchMu24"),
                tauTrigMatchEle20Src = cms.untracked.string("tauTrigMatchEle20"),
                tauTrigMatchEle22Src = cms.untracked.string("tauTrigMatchEle22"),
                tauTrigMatchEle27Src = cms.untracked.string("tauTrigMatchEle27")
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


process.TupleElectronTausNominal = cms.EDProducer('TupleElectronTauProducer' ,
                tauSrc=cms.InputTag('TupleTausNominal','TupleTausNominal','Ntuple'),
                electronSrc=cms.InputTag('TupleElectronsNominal','TupleElectronsNominal','Ntuple'),
                mvametSrc = cms.InputTag("pfMEtMVA"),
                genSrc = cms.InputTag("genParticles"),
                iFluc=cms.double(0.0),
                iScale=cms.double(0.0),
                jetSrc = cms.InputTag("cleanPatJets"),
                puJetIdMVASrc = cms.InputTag('puJetMva','full53xDiscriminant','PAT'),
                puJetIdFlagSrc = cms.InputTag('puJetMva','full53xId','PAT'),
                NAME=cms.string("TupleElectronTausNominal"),
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



process.p = cms.Path(
      process.myProducerLabel*
      process.isDiMuonEvent*
      process.isDiElectronEvent*
      #process.pfMEtMVANominal+
      process.TupleElectronsNominal*
      process.TupleMuonsNominal*
      process.TupleTausNominal*
      process.TupleMuonTausNominal*
      process.TupleElectronTausNominal
      #+process.metUncertaintySequence+
      #process.TupleTausTauEnDown*process.TupleMuonTausTauEnDown
      #+process.TupleMuonTausRecoilUp
      #+process.TupleMuonTausRecoilDown
      #+process.TupleMuonTausRecoilResUp
      #+process.TupleMuonTausRecoilResDown
                     )

process.e = cms.EndPath(process.out)
