import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/uscms/home/shalhout/1stSteps/Git2/DemoTauCode/CMSSW_5_3_14/src/patTuple_testing.root'
                                      )
                            )



isMC = True


if isMC:
  jecLevels = [
    'GR_R_53_V10_L1FastJet_AK5PFchs.txt',
    'GR_R_53_V10_L2Relative_AK5PFchs.txt',
    'GR_R_53_V10_L3Absolute_AK5PFchs.txt'
  ]
else :
  jecLevels = [
    'GR_R_53_V10_L1FastJet_AK5PFchs.txt',
    'GR_R_53_V10_L2Relative_AK5PFchs.txt',
    'GR_R_53_V10_L3Absolute_AK5PFchs.txt',
    'GR_R_53_V10_L2L3Residual_AK5PFchs.txt'
  ]



process.demo = cms.EDAnalyzer('JetTestAnalysis',
  jetSrc = cms.untracked.InputTag("selectedPatJets"),
  rhoSrc = cms.untracked.InputTag('ak5PFJets', 'rho'),
  pvSrc  = cms.untracked.InputTag('offlinePrimaryVertices'),
  jecPayloadNames = cms.untracked.vstring( jecLevels),
  jecUncName = cms.untracked.string('GR_R_53_V10_Uncertainty_AK5PFchs.txt'),
  puJetIdMVASrc = cms.untracked.InputTag("puJetMva")
)


process.p = cms.Path(process.demo)
