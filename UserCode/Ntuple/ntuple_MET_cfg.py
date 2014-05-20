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

# needed for MVA met, but need to be here
from JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_PAT_cfi import *
process.load('JetMETCorrections.Configuration.JetCorrectionProducers_cff')
process.load('JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_cff')

process.pfMEtMVAtuple = process.pfMEtMVA.clone(
                          srcLeptons = cms.VInputTag("isomuons","isoelectrons","isotaus")
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
                     process.TupleMuons*process.TupleTaus*process.TupleMuonTaus)

process.e = cms.EndPath(process.out)
