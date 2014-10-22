import FWCore.ParameterSet.Config as cms

process = cms.Process("FlatTuple")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

from FileLists.python.FILELISTNAME import myfilelist





process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
	                      fileNames=myfilelist
    )



process.TauEsNominal = cms.EDAnalyzer('FlatTuple',
electronTauSrc = cms.InputTag('TupleElectronTausNominal','TupleElectronTausNominal','PAT'),
electronTauWtSrc = cms.InputTag('TupleElectronTausNominalWeights','TupleElectronTausNominalWeights','PAT'),
electronTauVetoSrc = cms.InputTag('TupleElectronTauNominalVetoes','TupleElectronTausNominalVetoes','PAT'),
electronSrc = cms.InputTag('TupleElectronsNominal','TupleElectronsNominal','PAT'),
tauSrc = cms.InputTag('TupleTausNominal','TupleTausNominal','PAT'),
muonTauSrc = cms.InputTag('TupleMuonTausNominal','TupleMuonTausNominal','PAT'),
muonSrc = cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','PAT'),
muonTauWtSrc = cms.InputTag('TupleMuonTausNominalWeights','TupleMuonTausNominalWeights','PAT'),
muonTauVetoSrc = cms.InputTag('TupleMuonTauNominalVetoes','TupleMuonTausNominalVetoes','PAT'),
NAME = cms.string("TauEsNominal"), # only muTau or eTau
userDataSrc = cms.InputTag('UserSpecifiedData','TupleUserSpecifiedData','PAT')
)

process.TauEsUp = cms.EDAnalyzer('FlatTuple',
electronTauSrc = cms.InputTag('TupleElectronTausUp','TupleElectronTausUp','PAT'),
electronTauWtSrc = cms.InputTag('TupleElectronTausUpWeights','TupleElectronTausUpWeights','PAT'),
electronTauVetoSrc = cms.InputTag('TupleElectronTauUpVetoes','TupleElectronTausUpVetoes','PAT'),
electronSrc = cms.InputTag('TupleElectronsNominal','TupleElectronsNominal','PAT'),
tauSrc = cms.InputTag('TupleTausUp','TupleTausUp','PAT'),
muonTauSrc = cms.InputTag('TupleMuonTausUp','TupleMuonTausUp','PAT'),
muonSrc = cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','PAT'),
muonTauWtSrc = cms.InputTag('TupleMuonTausUpWeights','TupleMuonTausUpWeights','PAT'),
muonTauVetoSrc = cms.InputTag('TupleMuonTauUpVetoes','TupleMuonTausUpVetoes','PAT'),
NAME = cms.string("TauEsUp"), # only muTau or eTau
userDataSrc = cms.InputTag('UserSpecifiedData','TupleUserSpecifiedData','PAT')
)

process.TauEsDown = cms.EDAnalyzer('FlatTuple',
electronTauSrc = cms.InputTag('TupleElectronTausDown','TupleElectronTausDown','PAT'),
electronTauWtSrc = cms.InputTag('TupleElectronTausDownWeights','TupleElectronTausDownWeights','PAT'),
electronTauVetoSrc = cms.InputTag('TupleElectronTauDownVetoes','TupleElectronTausDownVetoes','PAT'),
electronSrc = cms.InputTag('TupleElectronsNominal','TupleElectronsNominal','PAT'),
tauSrc = cms.InputTag('TupleTausDown','TupleTausDown','PAT'),
muonTauSrc = cms.InputTag('TupleMuonTausDown','TupleMuonTausDown','PAT'),
muonSrc = cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','PAT'),
muonTauWtSrc = cms.InputTag('TupleMuonTausDownWeights','TupleMuonTausDownWeights','PAT'),
muonTauVetoSrc = cms.InputTag('TupleMuonTauDownVetoes','TupleMuonTausDownVetoes','PAT'),
NAME = cms.string("TauEsDown"), # only muTau or eTau
userDataSrc = cms.InputTag('UserSpecifiedData','TupleUserSpecifiedData','PAT')
)




# the following is needed
# because not all events have both eTau and muTau
process.options = cms.untracked.PSet(
SkipEvent = cms.untracked.vstring('ProductNotFound')
)


process.p = cms.Path(process.TauEsNominal+process.TauEsUp+process.TauEsDown)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string("/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_FILEOUTNAME.root")
)
