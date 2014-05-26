import FWCore.ParameterSet.Config as cms
process = cms.Process("Ntuple")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )




myfilelist = cms.untracked.vstring()
myfilelist.extend(['file:/uscms/home/shalhout/no_backup/patTuple_testing_first57569.root'])

process.source = cms.Source ("PoolSource",
                      fileNames=myfilelist,
		                  skipEvents=cms.untracked.uint32(0)
			                       )




process.myProducerLabel = cms.EDProducer('Ntuple',
muonSrc = cms.InputTag("selectedPatMuons")
)


##################
# Set up a recalc
# of the MVA met
# based on stuff in the
# PATtuple
####################

#from JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_PAT_cfi import *
process.load('JetMETCorrections.Configuration.JetCorrectionProducers_cff')
#process.load('JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_cff')
from JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_cff import pfMEtMVA


process.pfMEtMVANominal = pfMEtMVA.clone(
                      srcLeptons = cms.VInputTag("selectedPatMuons","selectedPatElectrons","selectedPatTaus")
                                          )



##################################################
# run the MET systematic tool
##################################################

# apply type I/type I + II PFMEt corrections to pat::MET object
# and estimate systematic uncertainties on MET
from PhysicsTools.PatUtils.tools.metUncertaintyTools import runMEtUncertainties
#process.load("PhysicsTools.PatUtils.tools.metUncertaintyTools")


process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START53_V23::All'


##-------------------- Import the JEC services -----------------------
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')

runMEtUncertainties(process,
      electronCollection  = cms.InputTag('selectedPatElectrons'),
      muonCollection  = cms.InputTag('selectedPatMuons'),
      tauCollection  = cms.InputTag('selectedPatTaus'),
      jetCollection  = cms.InputTag('selectedPatJets'),
      makePFMEtByMVA = True,
      doSmearJets = True,
      addToPatDefaultSequence = False
                    )


##########################
# Nominal Systematics    #
##########################
process.TupleMuonsNominal = cms.EDProducer('TupleMuonProducer' ,
                muonSrc =cms.InputTag('selectedPatMuons'),
                vertexSrc =cms.InputTag('offlinePrimaryVertices'),
                NAME=cms.string("TupleMuonsNominal")
                                     )

process.TupleTausNominal = cms.EDProducer('TupleTauProducer' ,
                tauSrc =cms.InputTag('selectedPatTaus'),
                NAME=cms.string("TupleTausNominal")
                                                   )




process.TupleMuonTausNominal = cms.EDProducer('TupleMuonTauProducer' ,
                tauSrc=cms.InputTag('TupleTausNominal','TupleTausNominal','Ntuple'),
                muonSrc=cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','Ntuple'),
                mvametSrc = cms.InputTag("pfMEtMVANominal"),
                genSrc = cms.InputTag("genParticles"),
                iFluc=cms.double(0.0),
                iScale=cms.double(0.0),
                jetSrc = cms.InputTag("selectedPatJets"),
                puJetIdMVASrc = cms.InputTag('puJetMva','full53xDiscriminant','PAT'),
                puJetIdFlagSrc = cms.InputTag('puJetMva','full53xId','PAT'),
                NAME=cms.string("TupleMuonTausNominal")
                                     )
##########################
# Tau Recoil Up Systematics    #
##########################

process.TupleMuonTausRecoilUp = cms.EDProducer('TupleMuonTauProducer' ,
                tauSrc=cms.InputTag('TupleTausNominal','TupleTausNominal','Ntuple'),
                muonSrc=cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','Ntuple'),
                mvametSrc = cms.InputTag("pfMEtMVANominal"),
                genSrc = cms.InputTag("genParticles"),
                iFluc=cms.double(1.0),
                iScale=cms.double(0.0),
                jetSrc = cms.InputTag("selectedPatJets"),
                puJetIdMVASrc = cms.InputTag('puJetMva','full53xDiscriminant','PAT'),
                puJetIdFlagSrc = cms.InputTag('puJetMva','full53xId','PAT'),
                NAME=cms.string("TupleMuonTausRecoilUp")
                                     )

##########################
# Tau Recoil Down Systematics    #
##########################

process.TupleMuonTausRecoilDown = cms.EDProducer('TupleMuonTauProducer' ,
                tauSrc=cms.InputTag('TupleTausNominal','TupleTausNominal','Ntuple'),
                muonSrc=cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','Ntuple'),
                mvametSrc = cms.InputTag("pfMEtMVANominal"),
                genSrc = cms.InputTag("genParticles"),
                iFluc=cms.double(-1.0),
                iScale=cms.double(0.0),
                jetSrc = cms.InputTag("selectedPatJets"),
                puJetIdMVASrc = cms.InputTag('puJetMva','full53xDiscriminant','PAT'),
                puJetIdFlagSrc = cms.InputTag('puJetMva','full53xId','PAT'),
                NAME=cms.string("TupleMuonTausRecoilDown")
                                     )

##########################
# Tau Recoil Res Up Systematics    #
##########################

process.TupleMuonTausRecoilResUp = cms.EDProducer('TupleMuonTauProducer' ,
                tauSrc=cms.InputTag('TupleTausNominal','TupleTausNominal','Ntuple'),
                muonSrc=cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','Ntuple'),
                mvametSrc = cms.InputTag("pfMEtMVANominal"),
                genSrc = cms.InputTag("genParticles"),
                iFluc=cms.double(0.0),
                iScale=cms.double(1.0),
                jetSrc = cms.InputTag("selectedPatJets"),
                puJetIdMVASrc = cms.InputTag('puJetMva','full53xDiscriminant','PAT'),
                puJetIdFlagSrc = cms.InputTag('puJetMva','full53xId','PAT'),
                NAME=cms.string("TupleMuonTausRecoilResUp")
                                     )

##########################
# Tau Recoil Res Down Systematics    #
##########################

process.TupleMuonTausRecoilResDown = cms.EDProducer('TupleMuonTauProducer' ,
                tauSrc=cms.InputTag('TupleTausNominal','TupleTausNominal','Ntuple'),
                muonSrc=cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','Ntuple'),
                mvametSrc = cms.InputTag("pfMEtMVANominal"),
                genSrc = cms.InputTag("genParticles"),
                iFluc=cms.double(0.0),
                iScale=cms.double(-1.0),
                jetSrc = cms.InputTag("selectedPatJets"),
                puJetIdMVASrc = cms.InputTag('puJetMva','full53xDiscriminant','PAT'),
                puJetIdFlagSrc = cms.InputTag('puJetMva','full53xId','PAT'),
                NAME=cms.string("TupleMuonTausRecoilResDown")
                                     )


##########################
# Tau ES Up Systematics    #
##########################

process.TupleTausTauEnUp = cms.EDProducer('TupleTauProducer' ,
                tauSrc =cms.InputTag('shiftedPatTausEnUp'),
                NAME=cms.string("TupleTausTauEnUp")
                                                   )

process.TupleMuonTausTauEnUp = cms.EDProducer('TupleMuonTauProducer' ,
                tauSrc=cms.InputTag('TupleTausTauEnUp','TupleTausTauEnUp','Ntuple'),
                muonSrc=cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','Ntuple'),
                mvametSrc = cms.InputTag("pfMEtMVATauEnUp"),
                genSrc = cms.InputTag("genParticles"),
                iFluc=cms.double(0.0),
                iScale=cms.double(0.0),
                jetSrc = cms.InputTag("selectedPatJets"),
                puJetIdMVASrc = cms.InputTag('puJetMva','full53xDiscriminant','PAT'),
                puJetIdFlagSrc = cms.InputTag('puJetMva','full53xId','PAT'),
                NAME=cms.string("TupleMuonTausTauEnUp")
                                     )


##########################
# Tau ES Down Systematics    #
##########################


process.TupleTausTauEnDown = cms.EDProducer('TupleTauProducer' ,
                tauSrc =cms.InputTag('shiftedPatTausEnDown'),
                NAME=cms.string("TupleTausTauEnDown")
                                                   )

process.TupleMuonTausTauEnDown = cms.EDProducer('TupleMuonTauProducer' ,
                tauSrc=cms.InputTag('TupleTausTauEnDown','TupleTausTauEnDown','Ntuple'),
                muonSrc=cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','Ntuple'),
                mvametSrc = cms.InputTag("pfMEtMVATauEnDown"),
                genSrc = cms.InputTag("genParticles"),
                iFluc=cms.double(0.0),
                iScale=cms.double(0.0),
                jetSrc = cms.InputTag("selectedPatJets"),
                puJetIdMVASrc = cms.InputTag('puJetMva','full53xDiscriminant','PAT'),
                puJetIdFlagSrc = cms.InputTag('puJetMva','full53xId','PAT'),
                NAME=cms.string("TupleMuonTausTauEnDown")
                                     )


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
      process.pfMEtMVANominal+
      process.TupleMuonsNominal*process.TupleTausNominal*process.TupleMuonTausNominal
      +process.metUncertaintySequence+
      process.TupleTausTauEnDown*process.TupleMuonTausTauEnDown
      +process.TupleMuonTausRecoilUp
      +process.TupleMuonTausRecoilDown
      +process.TupleMuonTausRecoilResUp
      +process.TupleMuonTausRecoilResDown
                     )

process.e = cms.EndPath(process.out)
