import FWCore.ParameterSet.Config as cms

process = cms.Process("FlatTuple")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

from FileLists.python.DUMMYNAMEOFFILE import myfilelist



 

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
	                      fileNames=myfilelist
    )


process.demo = cms.EDAnalyzer('FlatTuple',
electronTauSrc = cms.InputTag('TupleElectronTausNominal','TupleElectronTausNominal','PAT'),
electronTauWtSrc = cms.InputTag('TupleElectronTausNominalWeights','TupleElectronTausNominalWeights','PAT'),
electronTauVetoSrc = cms.InputTag('TupleElectronTauNominalVetoes','TupleElectronTausNominalVetoes','PAT'),
electronSrc = cms.InputTag('TupleElectronsNominal','TupleElectronsNominal','PAT'),
tauSrc = cms.InputTag('TupleTausNominal','TupleTausNominal','PAT'),
muonTauSrc = cms.InputTag('TupleMuonTausNominal','TupleMuonTausNominal','PAT'),
muonSrc = cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','PAT'),
muonTauWtSrc = cms.InputTag('TupleMuonTausNominalWeights','TupleMuonTausNominalWeights','PAT'),
muonTauVetoSrc = cms.InputTag('TupleMuonTauNominalVetoes','TupleMuonTausNominalVetoes','PAT'),
NAME = cms.string("Nominal"), # only muTau or eTau
userDataSrc = cms.InputTag('UserSpecifiedData','TupleUserSpecifiedData','PAT')
)




# the following is needed
# because not all events have both eTau and muTau
process.options = cms.untracked.PSet(
SkipEvent = cms.untracked.vstring('ProductNotFound')
)


process.p = cms.Path(process.demo)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("FlatTuple_DUMMYFILEOUT_nominalTauES.root")
)

