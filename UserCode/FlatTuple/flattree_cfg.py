import FWCore.ParameterSet.Config as cms

process = cms.Process("FlatTuple")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

myfilelist = cms.untracked.vstring()
myfilelist.extend(['file:./NtupleFile.root'])



process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
	                      fileNames=myfilelist
    )


process.demo = cms.EDAnalyzer('FlatTuple',
electronTauSrc = cms.InputTag('TupleElectronTausNominal','TupleElectronTausNominal','Ntuple'),
electronTauWtSrc = cms.InputTag('TupleElectronTausNominalWeights','TupleElectronTausNominalWeights','Ntuple'),
electronSrc = cms.InputTag('TupleElectronsNominal','TupleElectronsNominal','Ntuple'),
tauSrc = cms.InputTag('TupleTausNominal','TupleTausNominal','Ntuple'),
muonTauSrc = cms.InputTag('TupleMuonTausNominal','TupleMuonTausNominal','Ntuple'),
muonSrc = cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','Ntuple'),
muonTauWtSrc = cms.InputTag('TupleMuonTausNominalWeights','TupleMuonTausNominalWeights','Ntuple'),
NAME = cms.string("eTau") # only muTau or eTau
)




# the following is needed
# because not all events have both eTau and muTau
process.options = cms.untracked.PSet(
SkipEvent = cms.untracked.vstring('ProductNotFound')
)


process.p = cms.Path(process.demo)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("FlatTuple_eTau.root")
)
