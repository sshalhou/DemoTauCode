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


process.demo = cms.EDAnalyzer('FlatTuple',
electronTauSrc = cms.InputTag('TupleElectronTausSHIFT','TupleElectronTausSHIFT','PAT'),
electronTauWtSrc = cms.InputTag('TupleElectronTausSHIFTWeights','TupleElectronTausSHIFTWeights','PAT'),
electronTauVetoSrc = cms.InputTag('TupleElectronTauSHIFTVetoes','TupleElectronTausSHIFTVetoes','PAT'),
electronSrc = cms.InputTag('TupleElectronsNominal','TupleElectronsNominal','PAT'),
tauSrc = cms.InputTag('TupleTausSHIFT','TupleTausSHIFT','PAT'),
muonTauSrc = cms.InputTag('TupleMuonTausSHIFT','TupleMuonTausSHIFT','PAT'),
muonSrc = cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','PAT'),
muonTauWtSrc = cms.InputTag('TupleMuonTausSHIFTWeights','TupleMuonTausSHIFTWeights','PAT'),
muonTauVetoSrc = cms.InputTag('TupleMuonTauSHIFTVetoes','TupleMuonTausSHIFTVetoes','PAT'),
NAME = cms.string("TauEsSHIFT"), # only muTau or eTau
userDataSrc = cms.InputTag('UserSpecifiedData','TupleUserSpecifiedData','PAT')
)




# the following is needed
# because not all events have both eTau and muTau
process.options = cms.untracked.PSet(
SkipEvent = cms.untracked.vstring('ProductNotFound')
)


process.p = cms.Path(process.demo)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("/eos/uscms/store/user/shalhout/FlatTuples/FlatTuple_FILEOUTNAME_TauEsSHIFT.root")
)
