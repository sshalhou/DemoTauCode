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


################


from JetMETCorrections.Configuration.JetCorrectionServicesAllAlgos_cff import *
from JetMETCorrections.Configuration.DefaultJEC_cff import *
##from JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_cfi import *
## CV: importing mvaPFMET_leptons_cfi breaks produceAndDiscriminateHPSPFTaus sequence
##    (hpsPFTauDiscriminationByDecayModeFinding module gets overwritten by None,
##     in case RecoTauTag/Configuration/python/RecoPFTauTag_cff.py is loaded by
##     by top-level cfg.py file before JetMETCorrections/METPUSubtraction/python/mvaPFMET_cff.py gets loaded)
##from RecoJets.JetProducers.PileupJetIDCutParams_cfi import full_53x_wp
from RecoJets.JetProducers.PileupJetIDParams_cfi import JetIdParams
#from JetMETCorrections.METPUSubtraction.mvaPFMET_db_cfi import mvaPFMEtGBRForestsFromDB
from JetMETCorrections.METPUSubtraction.mvaPFMET_db_cfi import *


process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('JetMETCorrections.Configuration.JetCorrectionProducers_cff')
process.load('JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_cff')
process.GlobalTag.globaltag = 'START53_V15::All'


process.calibratedAK5PFJetsForPFMEtMVA = cms.EDProducer('PFJetCorrectionProducer',
    src = cms.InputTag('ak5PFJets'),
    correctors = cms.vstring("ak5PFL1FastL2L3") # NOTE: use "ak5PFL1FastL2L3" for MC / "ak5PFL1FastL2L3Residual" for Data
)


process.pfMEtMVA = cms.EDProducer("PFMETProducerMVA",
    srcCorrJets = cms.InputTag('calibratedAK5PFJetsForPFMEtMVA'),
    srcUncorrJets = cms.InputTag('ak5PFJets'),
    srcPFCandidates = cms.InputTag('particleFlow'),
    srcVertices = cms.InputTag('offlinePrimaryVertices'),
    srcLeptons = cms.VInputTag(),#"isomuons","isoelectrons","isotaus")
    # NOTE: you need to set this to collections of electrons, muons and tau-jets
    #passing the lepton reconstruction & identification criteria applied in your analysis
    minNumLeptons = cms.int32(0),
    srcRho = cms.InputTag('kt6PFJets','rho'),
    globalThreshold = cms.double(-1.),#pfMet.globalThreshold,
    minCorrJetPt = cms.double(-1.),
    ##inputFileNames = cms.PSet(
    ##    U     = cms.FileInPath('JetMETCorrections/METPUSubtraction/data/gbrmet_53_Dec2012.root'),
    ##    DPhi  = cms.FileInPath('JetMETCorrections/METPUSubtraction/data/gbrmetphi_53_Dec2012.root'),
    ##    CovU1 = cms.FileInPath('JetMETCorrections/METPUSubtraction/data/gbru1cov_53_Dec2012.root'),
    ##    CovU2 = cms.FileInPath('JetMETCorrections/METPUSubtraction/data/gbru2cov_53_Dec2012.root')
    ##),
    ##loadMVAfromDB = cms.bool(False),
    inputRecords = cms.PSet(
        U     = cms.string('mvaPFMET_53_Dec2012_U'),
        DPhi  = cms.string('mvaPFMET_53_Dec2012_DPhi'),
        CovU1 = cms.string('mvaPFMET_53_Dec2012_CovU1'),
        CovU2 = cms.string('mvaPFMET_53_Dec2012_CovU2')
    ),
    loadMVAfromDB = cms.bool(True),
    is42 = cms.bool(False), # CV: set this flag to true if you are running mvaPFMET in CMSSW_4_2_x
    corrector = cms.string("ak5PFL1Fastjet"),
    useType1  = cms.bool(False),
    useOld42  = cms.bool(False),
    dZcut     = cms.double(0.1),
    impactParTkThreshold = cms.double(0.),
    tmvaWeights = cms.string("RecoJets/JetProducers/data/TMVAClassificationCategory_JetID_MET_53X_Dec2012.weights.xml"),
    tmvaMethod = cms.string("JetID"),
    version = cms.int32(-1),
    cutBased = cms.bool(False),
    tmvaVariables = cms.vstring(
        "nvtx",
        "jetPt",
        "jetEta",
        "jetPhi",
        "dZ",
        "beta",
        "betaStar",
        "nCharged",
        "nNeutrals",
        "dR2Mean",
        "ptD",
        "frac01",
        "frac02",
        "frac03",
        "frac04",
        "frac05"
    ),
    tmvaSpectators = cms.vstring(),
    ##JetIdParams = full_53x_wp,
    JetIdParams = JetIdParams,
    verbosity = cms.int32(0)
)


process.pfMEtMVAsequence  = cms.Sequence(
#    (isomuonseq+isotauseq+isoelectronseq)*
    process.calibratedAK5PFJetsForPFMEtMVA*
    process.pfMEtMVA
    )
################

process.out = cms.OutputModule("PoolOutputModule",
fileName = cms.untracked.string('NtupleFile.root'),
outputCommands = cms.untracked.vstring('drop *')
#SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')
)



#################################
# keep everything produced by Ntuple
#################################
process.out.outputCommands +=['keep *_*_*_Ntuple']


process.p = cms.Path(process.myProducerLabel+process.TupleMuons*process.TupleTaus*process.TupleMuonTaus+process.pfMEtMVAsequence)

process.e = cms.EndPath(process.out)
