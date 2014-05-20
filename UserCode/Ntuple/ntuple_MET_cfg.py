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


##################
# Set up a recalc
# of the MVA met
# based on stuff in the
# PATtuple
####################

from JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_PAT_cfi import *
process.load('JetMETCorrections.Configuration.JetCorrectionProducers_cff')
#process.load('JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_cff')
from JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_cff import pfMEtMVA


process.pfMEtMVAtuple = pfMEtMVA.clone(
                      srcLeptons = cms.VInputTag("selectedPatMuons","selectedPatElectrons","selectedPatTaus")
                      #srcLeptons = cms.VInputTag("isomuons","isoelectrons","isotaus")
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
      doSmearJets = False,
      addToPatDefaultSequence = False
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








process.out = cms.OutputModule("PoolOutputModule",
fileName = cms.untracked.string('NtupleFile.root'),
outputCommands = cms.untracked.vstring('drop *')
#SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')
)



#################################
# keep everything produced by Ntuple
#################################
process.out.outputCommands +=['keep *_*_*_Ntuple']


process.p = cms.Path(process.myProducerLabel+
                     process.pfMEtMVAtuple+
                     process.TupleMuons*process.TupleTaus*process.TupleMuonTaus
                     +process.metUncertaintySequence
                     )

process.e = cms.EndPath(process.out)
