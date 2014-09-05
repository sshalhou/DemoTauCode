import FWCore.ParameterSet.Config as cms
process = cms.Process("Ntuple")
from PhysicsTools.PatAlgos.tools.helpers import *
#####################
# config parameters
#####################

runOnMC = True
isNonTopEmbeddedSample = False
isTopEmbeddedSample = False
printListOfModules = False
KeepAll = False
CheckMemoryUsage = False

##########################################
# the following 3 parameters set the first X  leptons in the
# lepton collections
# to consider for building the final states, any additional
# leptons will be ignored by the eTau and muTau producers
# all leptons are still considered for the vetos

MAX_ELECTRONS = 10
MAX_MUONS = 10
MAX_TAUS = 10


###########################################
# gen particle sources depend on isNonTopEmbeddedSample
# and isTopEmbeddedSample

InputTag genSrcInputTag = 'genParticles::SIM'
InputTag genTTembeddedSrcInputTag = ''

if isNonTopEmbeddedSample:
  genSrcInputTag = 'genParticles::EmbeddedRECO'
  genTTembeddedSrcInputTag = ''

elif isTopEmbeddedSample:
  genSrcInputTag = 'genParticles::EmbeddedRECO'
  genTTembeddedSrcInputTag = 'genParticles::SIM'


process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

######################
# set the global tag
#######################
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
if runOnMC:
  process.GlobalTag.globaltag = 'START53_V23::All'
else:
  process.GlobalTag.globaltag = 'FT_53_V21_AN4::All'
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')



myfilelist = cms.untracked.vstring()
myfilelist.extend(['file:/uscms/home/shalhout/no_backup/patTuple_testing.root'])

process.source = cms.Source ("PoolSource",
  fileNames=myfilelist,
  skipEvents=cms.untracked.uint32(0)
)




process.myProducerLabel = cms.EDProducer('Ntuple')
#################################




###################################
# create a new primary vertex collection
###################################

process.selectedPrimaryVertices = cms.EDFilter(
    "VertexSelector",
    src = cms.InputTag('offlinePrimaryVertices'),
    cut = cms.string("isValid & ndof >= 4 & z > -24 & z < +24 & position.Rho < 2."),
    filter = cms.bool(False)
)

###################################
# create an ES corrected tau collection
# (only pass this to mva met, since
# trigger matching does not exist)
###################################

process.EsCorrectedTaus = cms.EDProducer('EsCorrectedTauProducer' ,
                tauSrc =cms.InputTag('cleanPatTaus')
                                     )


##########################
# diMuon & diElectron Vetoes
##########################

process.isDiMuonEvent = cms.EDFilter("DiMuonFilter",
  muonSource     = cms.InputTag("cleanPatMuons"),
  vertexSource      = cms.InputTag("selectedPrimaryVertices::Ntuple"),
  filter = cms.bool(True)
)


process.isDiElectronEvent = cms.EDFilter("DiElectronFilter",
  electronSource     = cms.InputTag("cleanPatElectrons"),
  vertexSource      = cms.InputTag("selectedPrimaryVertices::Ntuple"),
  filter = cms.bool(True)
)


####################################
# setup the MVA MET calculation
#####################################

process.load("JetMETCorrections.Configuration.JetCorrectionServicesAllAlgos_cff")
from JetMETCorrections.Configuration.DefaultJEC_cff import *
if runOnMC:
  process.prefer("ak5PFL1FastL2L3")
else:
  process.prefer("ak5PFL1FastL2L3Residual")

process.load('JetMETCorrections.Configuration.JetCorrectionProducers_cff')
#from RecoMET.METPUSubtraction.mvaPFMET_leptons_cff import pfMEtMVA
from RecoMET.METPUSubtraction.mvaPFMET_cff import calibratedAK5PFJetsForPFMEtMVA
process.load("RecoMET.METPUSubtraction.mvaPFMET_cff")
process.calibratedAK5PFJetsForPFMEtMVA = calibratedAK5PFJetsForPFMEtMVA.clone()

if runOnMC:
  process.calibratedAK5PFJetsForPFMEtMVA.correctors = cms.vstring("ak5PFL1FastL2L3")
else:
  process.calibratedAK5PFJetsForPFMEtMVA.correctors = cms.vstring("ak5PFL1FastL2L3Residual")






##############################
# produce the single electron,
# muon, and tau collections
# that will be used for pair-wise
# mvaMet calculation

singlePatLeptons = cms.Sequence()

for eINDEX in range(MAX_ELECTRONS):
  eModuleName = "cleanPatElectrons%i" % (eINDEX)
  eModule = cms.EDProducer('SinglePatElectronProducer' ,
    electronSrc =cms.InputTag('cleanPatElectrons'),
    INDEX = cms.uint32(eINDEX),
    NAME=cms.string(eModuleName))
  setattr(process, eModuleName, eModule)
  singlePatLeptons += eModule

for mINDEX in range(MAX_MUONS):
  mModuleName = "cleanPatMuons%i" % (mINDEX)
  mModule = cms.EDProducer('SinglePatMuonProducer' ,
    muonSrc =cms.InputTag('cleanPatMuons'),
    INDEX = cms.uint32(mINDEX),
    NAME=cms.string(mModuleName))
  setattr(process, mModuleName, mModule)
  singlePatLeptons += mModule

for tINDEX in range(MAX_TAUS):
  tModuleName = "cleanPatTaus%i" % (tINDEX)
  tModule = cms.EDProducer('SinglePatTauProducer' ,
    tauSrc =cms.InputTag('EsCorrectedTaus::Ntuple'),
    INDEX = cms.uint32(tINDEX),
    NAME=cms.string(tModuleName))
  setattr(process, tModuleName, tModule)
  singlePatLeptons += tModule


################################
# create the pair-wise mva mets
################################

pairWiseMvaMETs = cms.Sequence()


#################################
# set the correct jet en. corr
#################################
corrector_ = cms.string('ak5PFL1FastL2L3')

if runOnMC:
  corrector_ = cms.string('ak5PFL1FastL2L3')
else:
  corrector_ = cms.string('ak5PFL1FastL2L3Residual')


###########
# eTau METs
###########

for eINDEX in range(MAX_ELECTRONS):
  for tINDEX in range(MAX_TAUS):
    metModuleName = "eTauMet%ix%i" % (eINDEX,tINDEX)
    eModuleName = "cleanPatElectrons%i:cleanPatElectrons%i:Ntuple" % (eINDEX,eINDEX)
    tModuleName = "cleanPatTaus%i:cleanPatTaus%i:Ntuple" % (tINDEX,tINDEX)
    metModule = process.pfMEtMVA.clone(
      corrector = corrector_,
      srcLeptons = cms.VInputTag(cms.InputTag(eModuleName),cms.InputTag(tModuleName)),
      useType1 = cms.bool(False),
      loadMVAfromDB = cms.bool(True),
      minCorrJetPt = cms.double(-1),
      inputRecords = cms.PSet(
        U     = cms.string('mvaPFMET_53_Dec2012_U'),
        DPhi  = cms.string('mvaPFMET_53_Dec2012_DPhi'),
        CovU1 = cms.string('mvaPFMET_53_Dec2012_CovU1'),
        CovU2 = cms.string('mvaPFMET_53_Dec2012_CovU2')))
      #inputFileNames = cms.PSet(
      #  U     = cms.FileInPath('RecoMET/METPUSubtraction/data/gbrmet_53_Dec2012.root'),
      #  DPhi  = cms.FileInPath('RecoMET/METPUSubtraction/data/gbrmetphi_53_Dec2012.root'),
      #  CovU1 = cms.FileInPath('RecoMET/METPUSubtraction/data/gbru1cov_53_Dec2012.root'),
      #  CovU2 = cms.FileInPath('RecoMET/METPUSubtraction/data/gbru2cov_53_Dec2012.root')
      #))
    setattr(process, metModuleName, metModule)
    metModule.minNumLeptons = cms.int32(2)
    pairWiseMvaMETs += metModule

###########
# muTau METs
###########

for mINDEX in range(MAX_MUONS):
  for tINDEX in range(MAX_TAUS):
    metModuleName = "muTauMet%ix%i" % (mINDEX,tINDEX)
    mModuleName = "cleanPatMuons%i:cleanPatMuons%i:Ntuple" % (mINDEX,mINDEX)
    tModuleName = "cleanPatTaus%i:cleanPatTaus%i:Ntuple" % (tINDEX,tINDEX)
    metModule = process.pfMEtMVA.clone(
      corrector = corrector_,
      srcLeptons = cms.VInputTag(cms.InputTag(mModuleName),cms.InputTag(tModuleName)),
      useType1 = cms.bool(False),
      loadMVAfromDB = cms.bool(True),
      minCorrJetPt = cms.double(-1),
      inputRecords = cms.PSet(
        U     = cms.string('mvaPFMET_53_Dec2012_U'),
        DPhi  = cms.string('mvaPFMET_53_Dec2012_DPhi'),
        CovU1 = cms.string('mvaPFMET_53_Dec2012_CovU1'),
        CovU2 = cms.string('mvaPFMET_53_Dec2012_CovU2')))
      #inputFileNames = cms.PSet(
      #  U     = cms.FileInPath('RecoMET/METPUSubtraction/data/gbrmet_53_Dec2012.root'),
      #  DPhi  = cms.FileInPath('RecoMET/METPUSubtraction/data/gbrmetphi_53_Dec2012.root'),
      #  CovU1 = cms.FileInPath('RecoMET/METPUSubtraction/data/gbru1cov_53_Dec2012.root'),
      #  CovU2 = cms.FileInPath('RecoMET/METPUSubtraction/data/gbru2cov_53_Dec2012.root')
      #))
    setattr(process, metModuleName, metModule)
    metModule.minNumLeptons = cms.int32(2)
    pairWiseMvaMETs += metModule


##########################
# Nominal Systematics    #
##########################

process.TupleElectronsNominal = cms.EDProducer('TupleElectronProducer' ,
                electronSrc =cms.InputTag('cleanPatElectrons'),
                vertexSrc =cms.InputTag('selectedPrimaryVertices'),
                NAME=cms.string("TupleElectronsNominal"),
                triggerEventSrc = cms.untracked.InputTag("patTriggerEvent"),
                eTrigMatchEle20Src = cms.untracked.string("eTrigMatchEle20"),
                eTrigMatchEle22Src = cms.untracked.string("eTrigMatchEle22"),
                eTrigMatchEle27Src = cms.untracked.string("eTrigMatchEle27")
                                     )

process.TupleMuonsNominal = cms.EDProducer('TupleMuonProducer' ,
                muonSrc =cms.InputTag('cleanPatMuons'),
                vertexSrc =cms.InputTag('selectedPrimaryVertices'),
                NAME=cms.string("TupleMuonsNominal"),
                triggerEventSrc = cms.untracked.InputTag("patTriggerEvent"),
                muTrigMatchMu17Src = cms.untracked.string("muTrigMatchMu17"),
                muTrigMatchMu18Src = cms.untracked.string("muTrigMatchMu18"),
                muTrigMatchMu24Src = cms.untracked.string("muTrigMatchMu24"),
                pfSrc = cms.InputTag('particleFlow')

                                     )

process.TupleTausNominal = cms.EDProducer('TupleTauProducer' ,
                tauSrc =cms.InputTag('cleanPatTaus'),
                NAME=cms.string("TupleTausNominal"),
                triggerEventSrc = cms.untracked.InputTag("patTriggerEvent"),
                tauTrigMatchMu17Src = cms.untracked.string("tauTrigMatchMu17"),
                tauTrigMatchMu18Src = cms.untracked.string("tauTrigMatchMu18"),
                tauTrigMatchMu24Src = cms.untracked.string("tauTrigMatchMu24"),
                tauTrigMatchEle20Src = cms.untracked.string("tauTrigMatchEle20"),
                tauTrigMatchEle22Src = cms.untracked.string("tauTrigMatchEle22"),
                tauTrigMatchEle27Src = cms.untracked.string("tauTrigMatchEle27")
                                                   )


##################
# muTau Final Pairs

allMuTauMETs = cms.VInputTag()

for mINDEX in range(MAX_MUONS):
  for tINDEX in range(MAX_TAUS):
    metModuleName = "muTauMet%ix%i::Ntuple" % (mINDEX,tINDEX)
    metModuleNameTag = cms.InputTag(metModuleName)
    allMuTauMETs.append(metModuleNameTag)


print allMuTauMETs

process.TupleMuonTausNominal = cms.EDProducer('TupleMuonTauProducer' ,
                tauSrc=cms.InputTag('TupleTausNominal','TupleTausNominal','Ntuple'),
                muonSrc=cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','Ntuple'),
                mvametSrc = allMuTauMETs,
                genSrc = genSrcInputTag,
                genTTembeddedSrc = genTTembeddedSrcInputTag,
                iFluc=cms.double(0.0),
                iScale=cms.double(0.0),
                jetSrc = cms.InputTag("cleanPatJets"),
                puJetIdMVASrc = cms.InputTag('puJetMva','full53xDiscriminant','PAT'),
                puJetIdFlagSrc = cms.InputTag('puJetMva','full53xId','PAT'),
                NAME=cms.string("TupleMuonTausNominal"),
                doSVFit=cms.bool(False),
                maxMuons=cms.uint32(MAX_MUONS),
                maxTaus=cms.uint32(MAX_TAUS),
                doNotRequireFullIdForLeptons = cms.bool(True),
                electronSrc=cms.InputTag('TupleElectronsNominal','TupleElectronsNominal','Ntuple'),
                triggerEventSrc = cms.InputTag("patTriggerEvent"),
                userDataSrc=cms.InputTag('UserSpecifiedData','TupleUserSpecifiedData','PAT')



                                     )


process.TupleMuonTausNominalWeights = cms.EDProducer('TupleMuonTauWeightProducer' ,
                NAME=cms.string("TupleMuonTausNominalWeights"),
                pileupSrc = cms.InputTag("addPileupInfo"),
                muontauSrc=cms.InputTag('TupleMuonTausNominal','TupleMuonTausNominal','Ntuple'),
                muonSrc=cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','Ntuple'),
                tauSrc=cms.InputTag('TupleTausNominal','TupleTausNominal','Ntuple'),
                userDataSrc=cms.InputTag('UserSpecifiedData','TupleUserSpecifiedData','PAT')
                                     )

##################
# eTau Final Pairs

allElecTauMETs = cms.VInputTag()

for eINDEX in range(MAX_ELECTRONS):
  for tINDEX in range(MAX_TAUS):
    metModuleName = "eTauMet%ix%i::Ntuple" % (eINDEX,tINDEX)
    metModuleNameTag = cms.InputTag(metModuleName)
    allElecTauMETs.append(metModuleNameTag)


print allElecTauMETs


process.TupleElectronTausNominal = cms.EDProducer('TupleElectronTauProducer' ,
                tauSrc=cms.InputTag('TupleTausNominal','TupleTausNominal','Ntuple'),
                electronSrc=cms.InputTag('TupleElectronsNominal','TupleElectronsNominal','Ntuple'),
                mvametSrc = allElecTauMETs,
                genSrc = genSrcInputTag,
                genTTembeddedSrc = genTTembeddedSrcInputTag,
                iFluc=cms.double(0.0),
                iScale=cms.double(0.0),
                jetSrc = cms.InputTag("cleanPatJets"),
                puJetIdMVASrc = cms.InputTag('puJetMva','full53xDiscriminant','PAT'),
                puJetIdFlagSrc = cms.InputTag('puJetMva','full53xId','PAT'),
                NAME=cms.string("TupleElectronTausNominal"),
                doSVFit=cms.bool(False),
                maxElectrons=cms.uint32(MAX_ELECTRONS),
                maxTaus=cms.uint32(MAX_TAUS),
                doNotRequireFullIdForLeptons = cms.bool(True),
                muonSrc=cms.InputTag('TupleMuonsNominal','TupleMuonsNominal','Ntuple'),
                triggerEventSrc = cms.InputTag("patTriggerEvent"),
                userDataSrc=cms.InputTag('UserSpecifiedData','TupleUserSpecifiedData','PAT')


                                     )

process.TupleElectronTausNominalWeights = cms.EDProducer('TupleElectronTauWeightProducer' ,
                NAME=cms.string("TupleElectronTausNominalWeights"),
                pileupSrc = cms.InputTag("addPileupInfo"),
                electrontauSrc=cms.InputTag('TupleElectronTausNominal','TupleElectronTausNominal','Ntuple'),
                electronSrc=cms.InputTag('TupleElectronsNominal','TupleElectronsNominal','Ntuple'),
                tauSrc=cms.InputTag('TupleTausNominal','TupleTausNominal','Ntuple'),
                userDataSrc=cms.InputTag('UserSpecifiedData','TupleUserSpecifiedData','PAT')
                                     )


#################################
process.out = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string('NtupleFile.root'),
  outputCommands = cms.untracked.vstring('drop *')
  #SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')
)



#################################
# keep everything produced by Tuepl-Ntuple
#################################
process.out.outputCommands +=['keep Tuple*_*_*_Ntuple']

if KeepAll:
  process.out.outputCommands +=['keep *_*_*_*']

#################################
# keep UserSpecifiedData
#################################
process.out.outputCommands +=['keep TupleUserSpecifiedDatas_UserSpecifiedData_TupleUserSpecifiedData_PAT']

if CheckMemoryUsage:
  process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",ignoreTotal = cms.untracked.int32(1) )

process.p = cms.Path(
  process.myProducerLabel*
  process.selectedPrimaryVertices*
  process.EsCorrectedTaus*
  process.isDiMuonEvent*
  process.isDiElectronEvent*
  singlePatLeptons*
  pairWiseMvaMETs*
#process.pfMEtMVANominal+
      process.TupleElectronsNominal*
      process.TupleMuonsNominal*
      process.TupleTausNominal*
      process.TupleMuonTausNominal*
      process.TupleElectronTausNominal*
      process.TupleMuonTausNominalWeights*
      process.TupleElectronTausNominalWeights
#+process.metUncertaintySequence+
#process.TupleTausTauEnDown*process.TupleMuonTausTauEnDown
#+process.TupleMuonTausRecoilUp
#+process.TupleMuonTausRecoilDown
#+process.TupleMuonTausRecoilResUp
#+process.TupleMuonTausRecoilResDown
)

process.e = cms.EndPath(process.out)


if printListOfModules:
  print listModules(process.p)
