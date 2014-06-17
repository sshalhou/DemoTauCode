import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/uscms/home/shalhout/no_backup/patTuple_testing.root'
                                      )
                            )



isMC = True


###########
# JEC for MC

jecLevels = [
    './RecoJets/JetAnalyzers/test/START53_V23_L1FastJet_AK5PFchs.txt',
    './RecoJets/JetAnalyzers/test/START53_V23_L2Relative_AK5PFchs.txt',
    './RecoJets/JetAnalyzers/test/START53_V23_L3Absolute_AK5PFchs.txt'
  ]
jecUncNameFile = './RecoJets/JetAnalyzers/test/START53_V23_Uncertainty_AK5PFchs.txt'

##############
# JEC for Data

if not isMC:
  jecLevels = [
    './RecoJets/JetAnalyzers/test/FT_53_V21_AN4_L1FastJet_AK5PFchs.txt',
    './RecoJets/JetAnalyzers/test/FT_53_V21_AN4_L2Relative_AK5PFchs.txt',
    './RecoJets/JetAnalyzers/test/FT_53_V21_AN4_L3Absolute_AK5PFchs.txt',
    './RecoJets/JetAnalyzers/test/FT_53_V21_AN4_L2L3Residual_AK5PFchs.txt'
  ]
  jecUncNameFile = './RecoJets/JetAnalyzers/test/FT_53_V21_AN4_Uncertainty_AK5PFchs.txt'



process.demo = cms.EDAnalyzer('JetTestAnalysis',
  jetSrc = cms.untracked.InputTag("selectedPatJets"),
  rhoSrc = cms.untracked.InputTag('kt6PFJets', 'rho'),
  pvSrc  = cms.untracked.InputTag('offlinePrimaryVertices'),
  jecPayloadNames = cms.untracked.vstring(jecLevels),
  jecUncName = cms.untracked.string(jecUncNameFile),
  puJetIdMVASrc = cms.InputTag('puJetMva','full53xDiscriminant','PAT'),
  puJetIdFlagSrc = cms.InputTag('puJetMva','full53xId','PAT')
  )


process.p = cms.Path(process.demo)
