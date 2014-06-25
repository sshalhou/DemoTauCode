########################################################################################################
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patTemplate_cfg import *
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("PhysicsTools.PatAlgos.patSequences_cff")
########################################################################################################

FilterEvents = True
DropSelectedPatObjects = True
KeepAll = False
SampleName_='GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'
PhysicsProcess_='gg->H->tautau[SM_125_8TeV]'


###################################################
# Store SampleName and PhysicsProcess
# eventually these should be command line
# options
###################################################

process.UserSpecifiedData = cms.EDProducer('TupleUserSpecifiedDataProducer' ,
                                            SampleName=cms.string(SampleName_),
                                            PhysicsProcess=cms.string(PhysicsProcess_)
                                            )

###################################################
# need to get the correct version of the global
# tag and set JEC to match, also remove MC matching
# for data
###################################################
from PhysicsTools.PatAlgos.tools.coreTools import *

runOnMC = True
if runOnMC:
  process.GlobalTag.globaltag = 'START53_V23::All'
else:
  process.GlobalTag.globaltag = 'FT_53_V21_AN4::All'
  removeMCMatching(process, ['All'])
  runOnData(process)


###################################################
# set the JEC level for MC or DATA
###################################################


jetEnCorr = ['L1FastJet', 'L2Relative', 'L3Absolute']

if not runOnMC:
  jetEnCorr.extend(['L2L3Residual'])

###################################################
# pu jet id requires PF jets as input
###################################################

from PhysicsTools.PatAlgos.tools.jetTools import *

switchJetCollection(process,cms.InputTag('ak5PFJets'),
                 doJTA        = True,
                 doBTagging   = True,
                 jetCorrLabel = ('AK5PF', jetEnCorr),
                 doType1MET   = True,
                 genJetCollection=cms.InputTag("ak5GenJets"),
                 doJetID      = True
                 )

###################################################
# load the PU JetID sequence
###################################################

process.load("RecoJets.JetProducers.pujetidsequence_cff")

###################################################
# keep PU jet id
###################################################

process.out.outputCommands +=['keep *_selectedPatJets*_*_*']
process.out.outputCommands +=['keep *_puJetId*_*_*']
process.out.outputCommands +=['keep *_puJetMva*_*_*']





##################################################
# MVA MET
###################################################
from RecoMET.METPUSubtraction.mvaPFMET_leptons_PAT_cfi import *
process.load('JetMETCorrections.Configuration.JetCorrectionProducers_cff')
process.load('RecoMET.METPUSubtraction.mvaPFMET_leptons_cff')




process.pfMEtMVA = process.pfMEtMVA.clone(srcLeptons = cms.VInputTag("isomuons","isoelectrons","isotaus"))


process.patPFMetByMVA = process.patMETs.clone(
    metSource = cms.InputTag('pfMEtMVA'),
    addMuonCorrections = cms.bool(True),
    genMETSource = cms.InputTag('genMetTrue')
                                                )

process.load("JetMETCorrections.Type1MET.pfMETCorrectionType0_cfi")
process.load("PhysicsTools.PatUtils.patPFMETCorrections_cff")

process.mvametPF2PATsequence = cms.Sequence(
                process.pfMEtMVAsequence*
                # next 2 lines are from
                # https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePATTools#METSysTools
                process.type0PFMEtCorrection*
                process.patPFMETtype0Corr
                                )


process.out.outputCommands +=['keep *_pfMEtMVA*_*_*']
process.out.outputCommands +=['keep *_patPFMetByMVA*_*_*']









###################################################
# needed for JEC
###################################################
process.out.outputCommands +=['keep double_kt6PFJets_rho_RECO']

###################################################
# Store the Vertex Collection
# filtering is possible at this
# stage (currently requiring at least one)
###################################################

from PhysicsTools.PatAlgos.tools.trackTools import *

process.VertexPresent = cms.EDFilter("VertexSelector",
                             src = cms.InputTag("offlinePrimaryVertices"),
                             cut = cms.string("!isFake && ndof > 4 && abs(z) < 24 && position.Rho < 2"),
                             filter = cms.bool(True)
                             )

process.out.outputCommands +=['keep *_offlinePrimaryVertices*_*_*']
process.out.outputCommands +=['keep *_offlinePrimaryVerticesWithBS*_*_*']
process.out.outputCommands +=['keep *_generalTracks_*_*']
process.out.outputCommands +=['keep TupleUserSpecifiedDatas_UserSpecifiedData_TupleUserSpecifiedData_PAT']


###################################################
# add info needed for pile-up reweight
####################################################
process.out.outputCommands +=['keep *_addPileupInfo*_*_*']
###################################################

###################################################
# keep beamspot (may be needed for electron ID)
###################################################

process.out.outputCommands +=['keep *_offlineBeamSpot*_*_*']


###################################################
# need for PDF sys tool
###################################################
if runOnMC:
    process.out.outputCommands +=['keep GenEventInfoProduct_generator__SIM']

###################################################
# the new Tau ID
###################################################
process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")

from PhysicsTools.PatAlgos.tools.tauTools import *
switchToPFTauHPS(process)

###################################################
# the MVA electron ID
###################################################


process.load('EgammaAnalysis.ElectronTools.electronIdMVAProducer_cfi')
process.mvaID = cms.Sequence(  process.mvaTrigV0 + process.mvaTrigNoIPV0 + process.mvaNonTrigV0 )


process.patElectrons.electronIDSources = cms.PSet(
    mvaTrigV0 = cms.InputTag("mvaTrigV0"),
    mvaNonTrigV0 = cms.InputTag("mvaNonTrigV0"),
    mvaTrigNoIPV0 = cms.InputTag("mvaTrigNoIPV0"),
    )


process.patConversions = cms.EDProducer("PATConversionProducer",
                                        # input collection
                                        # this should be whatever the final analysis-level
                                        # electrons are
                                        electronSource = cms.InputTag("cleanPatElectrons")
                                        )


process.out.outputCommands +=['keep *_patConversions*_*_*']
process.out.outputCommands +=['keep *_conversions*_*_*']
#process.out.outputCommands +=['keep *_gsfElectrons*_*_*']




###################################################
# setup electron pfIsolation, without this the
# standard PAT access via chargedHadronIso etc.
# will return -1
###################################################



#from PhysicsTools.PatAlgos.tools.pfTools import *
#usePFIso(process)
#process.patElectrons.pfElectronSource = 'particleFlow'
#process.patMuons.pfMuonSource = 'particleFlow'



from CommonTools.ParticleFlow.Tools.pfIsolation import setupPFElectronIso, setupPFMuonIso

process.eleIsoSequence = setupPFElectronIso(process, 'gsfElectrons')
process.muIsoSequence = setupPFMuonIso(process, 'pfAllMuons')

process.eleIsoSequence.remove(process.elPFIsoValueCharged03NoPFIdPFIso)
process.eleIsoSequence.remove(process.elPFIsoValueChargedAll03NoPFIdPFIso)
process.eleIsoSequence.remove(process.elPFIsoValueGamma03NoPFIdPFIso)
process.eleIsoSequence.remove(process.elPFIsoValueNeutral03NoPFIdPFIso)
process.eleIsoSequence.remove(process.elPFIsoValuePU03NoPFIdPFIso)
process.eleIsoSequence.remove(process.elPFIsoValueCharged04NoPFIdPFIso)
process.eleIsoSequence.remove(process.elPFIsoValueChargedAll04NoPFIdPFIso)
process.eleIsoSequence.remove(process.elPFIsoValueGamma04NoPFIdPFIso)
process.eleIsoSequence.remove(process.elPFIsoValueNeutral04NoPFIdPFIso)
process.eleIsoSequence.remove(process.elPFIsoValuePU04NoPFIdPFIso)
process.elPFIsoValueGamma04PFIdPFIso.deposits[0].vetos      = cms.vstring('EcalEndcaps:ConeVeto(0.08)','EcalBarrel:ConeVeto(0.08)')
process.elPFIsoValueNeutral04PFIdPFIso.deposits[0].vetos    = cms.vstring()
process.elPFIsoValuePU04PFIdPFIso.deposits[0].vetos         = cms.vstring()
process.elPFIsoValueCharged04PFIdPFIso.deposits[0].vetos    = cms.vstring('EcalEndcaps:ConeVeto(0.015)')
process.elPFIsoValueChargedAll04PFIdPFIso.deposits[0].vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)','EcalBarrel:ConeVeto(0.01)')





###################################################
# apply selection cuts on physics objects
# to keep that PATtuple to a reasonable size
###################################################

#from PhysicsTools.PatAlgos.cleaningLayer1.cleanPatCandidates_cff import *
from PhysicsTools.PatAlgos.selectionLayer1.tauSelector_cfi import *
process.countMyPatTaus = selectedPatTaus.clone(src = 'cleanPatTaus',
            cut = cms.string("pt>17 && abs(eta)<2.4"+
            " && ( tauID('byLooseCombinedIsolationDeltaBetaCorr3Hits') > 0.5 || tauID('byVLooseIsolationMVA3oldDMwLT') > 0.5 )"+
            " && ( tauID('againstElectronLoose')>0.5 || tauID('againstElectronVLooseMVA5')>0.5 )"+
            " && ( tauID('againstMuonLoose3')>0.5 || tauID('againstMuonLooseMVA')>0.5 )")
                                                )


from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
process.myCleanPatMuons = selectedPatMuons.clone(src = 'cleanPatMuons',
cut = cms.string("pt > 10"+
                 " && abs(eta) < 2.4"
                +" && isPFMuon"
                +" && isTrackerMuon "
                +" && isGlobalMuon "
                +" && (pfIsolationR04.sumChargedParticlePt +"
                +"max(pfIsolationR04.sumNeutralHadronEt+pfIsolationR04.sumPhotonEt-0.5*pfIsolationR04.sumPUPt,0.0))/pt < 0.3"
                )
                                                  )



from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
process.countMyPatElectrons = selectedPatElectrons.clone(src = 'cleanPatElectrons',
      cut = cms.string("et > 24 * 0.9"+
                       " && gsfTrack.trackerExpectedHitsInner.numberOfLostHits == 0"+
                       " && abs(eta) < 2.1 * 1.1" +
                       " && electronID('mvaNonTrigV0') >= 0.85 " +
                       " && passConversionVeto " +
                       " && (chargedHadronIso + max(neutralHadronIso+photonIso-0.5*puChargedHadronIso,0.0))/pt < 0.2 "
                      )
                                                        )



###################################################
# require an eTau or MuTau pair in the event
###################################################


process.countGoodPairs = cms.EDFilter("PatMuonTauOrElectronTauFilter",
  electronSource = cms.InputTag("countMyPatElectrons"),
  muonSource     = cms.InputTag("myCleanPatMuons"),
  tauSource      = cms.InputTag("countMyPatTaus"),
  countElectronTaus = cms.bool(True),
  countMuonTaus     = cms.bool(True),
  filter = cms.bool(True)
)




###################################################
# keep selected and clean collections
###################################################

process.out.outputCommands +=['keep *_selectedPat*_*_*']
process.out.outputCommands +=['keep *_cleanPat*_*_*']

###################################################
# keeps for MET Unc. Tool
###################################################

process.out.outputCommands +=['keep recoPFCandidates_particleFlow__RECO']
process.out.outputCommands +=['keep recoPFJets_calibratedAK5PFJetsForPFMEtMVA__PAT']
process.out.outputCommands +=['keep recoPFJets_ak5PFJets__RECO']
process.out.outputCommands +=['keep recoPFMETs_pfMet__RECO']
process.out.outputCommands +=['keep recoGenMETs_genMetTrue__SIM']
process.out.outputCommands +=['keep recoPFCandidates_selectedPatJets_pfCandidates_PAT']
process.out.outputCommands +=['keep recoMuons_muons__RECO']
process.out.outputCommands +=['keep recoGsfTracks_electronGsfTracks__RECO']
process.out.outputCommands +=['keep *_ak5GenJetsNoNu_*_PAT']
process.out.outputCommands +=['keep *_*genParticlesForJetsNoNu*_*_PAT']
process.out.outputCommands +=['keep *_*iterativeCone5GenJetsNoNu*_*_PAT']
process.out.outputCommands +=['keep recoGenParticles*_*_*_*']

if runOnMC:
    process.out.outputCommands +=['keep GenEventInfoProduct_generator__SIM']
  # the above is needed for the PDF sys. tool

##################################################
# Let it run
###################################################
process.p = cms.Path(
                             process.UserSpecifiedData*
                             process.VertexPresent*
                             process.mvaID*
                             process.PFTau*
  +process.pfAllMuons
  +process.pfParticleSelectionSequence
  +process.eleIsoSequence
  +process.muIsoSequence+
                               process.recoTauClassicHPSSequence *
                             process.mvametPF2PATsequence*
                             process.patDefaultSequence*
                             process.patPFMetByMVA*
                             process.patConversions
                             *process.puJetIdSqeuence
                             *process.countMyPatTaus
                             *process.countMyPatElectrons
                             *process.myCleanPatMuons
                                                              )


if FilterEvents:
  process.p *= process.countGoodPairs

if DropSelectedPatObjects:
  process.out.outputCommands +=['drop *_selectedPatElectrons*_*_*']
  process.out.outputCommands +=['drop *_selectedPatMuons*_*_*']
  process.out.outputCommands +=['drop *_selectedPatTaus*_*_*']
  process.out.outputCommands +=['drop *_selectedPatJets*_*_*']
  process.out.outputCommands +=['keep *_cleanPatElectrons*_*_*']
  process.out.outputCommands +=['drop *_cleanPatMuons*_*_*']
  process.out.outputCommands +=['keep *_myCleanPatMuons*_*_*']
  process.out.outputCommands +=['keep *_cleanPatTaus*_*_*']
  process.out.outputCommands +=['keep *_cleanPatJets*_*_*']




###################################################
# require all paths to pass
###################################################

process.out.SelectEvents.SelectEvents = ['p']



########################################################################################################
if KeepAll:
  process.out.outputCommands +=['keep *_*_*_*']
########################################################################################################
process.out.fileName = '/uscms/home/shalhout/no_backup/patTuple_testing.root'

########################################################################################################
myfilelist = cms.untracked.vstring()

#myfilelist.extend(['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/DY1JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/0000/001318CD-C5F4-E111-AAD9-001E67398D72.root'])
myfilelist.extend(['file:/uscms/home/shalhout/no_backup/5000.root'])
myfilelist.extend(['file:/uscms/home/shalhout/1stSteps/Git2/DemoTauCode/CMSSW_5_3_14/src/MyOutputFile.root'])
myfilelist.extend(['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/00E903E2-9FE9-E111-8B1E-003048FF86CA.root'])
myfilelist.extend(['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/085027A0-63E9-E111-BA2C-0018F3D09670.root'])
myfilelist.extend(['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/0E3688C3-98E9-E111-8FC6-003048FFCBB0.root'])
myfilelist.extend(['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/1289637A-69E9-E111-B26D-003048678F84.root'])
myfilelist.extend(['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/12A21961-B3E9-E111-AA11-00261894394D.root'])

process.source = cms.Source ("PoolSource",
                      fileNames=myfilelist,
                        dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
                        inputCommands = cms.untracked.vstring(
                        'keep *',
                        'drop recoPFTaus_*_*_*'
                        ),
                      skipEvents=cms.untracked.uint32(0)
                             )
########################################################################################################


process.maxEvents.input = 100
########################################################################################################
