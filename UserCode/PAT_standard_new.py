########################################################################################################
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patTemplate_cfg import *
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
########################################################################################################


RunMETUnc = False
KeepAll = True
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

runOnMC = True
if runOnMC:
  process.GlobalTag.globaltag = 'START53_V23::All'
else:
  process.GlobalTag.globaltag = 'FT_53_V21_AN4::All'
  removeMCMatching(process, 'All')
  runOnData(process)


###################################################
# load the PU JetID sequence
###################################################
#from PhysicsTools.PatAlgos.tools.jetTools import *

#switchJetCollection(process,cms.InputTag('ak5PFJets'),
#                 doJTA        = True,
#                 doBTagging   = True,
#                 jetCorrLabel = ('AK5PF', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute'])),
#                 doType1MET   = True,
#                 genJetCollection=cms.InputTag("ak5GenJets"),
#                 doJetID      = True
#                 )



process.load("RecoJets.JetProducers.pujetidsequence_cff")

#from RecoJets.JetProducers.pujetidsequence_cff import puJetId, puJetMva

#process.puJetId = puJetId.clone()

#process.puJetMva = puJetMva.clone()

#process.puJetIdSqeuence = cms.Sequence(process.puJetMva)


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

from PhysicsTools.PatAlgos.tools.coreTools import *
from PhysicsTools.PatAlgos.tools.trackTools import *

process.VertexPresent = cms.EDFilter("VertexSelector",
                             src = cms.InputTag("offlinePrimaryVertices"),
                             cut = cms.string("!isFake && ndof > 4 && abs(z) < 24 && position.Rho < 2"),
                             filter = cms.bool(True)
                             )

process.out.outputCommands +=['keep *_offlinePrimaryVertices*_*_*']
process.out.outputCommands +=['drop *_offlinePrimaryVerticesWithBS*_*_*']
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






##################################################
# Let it run
###################################################
process.p = cms.Path(
                             process.UserSpecifiedData*
                             process.VertexPresent*
                             process.mvaID*
                             process.PFTau*
                             process.recoTauClassicHPSSequence *
                             process.mvametPF2PATsequence*
                             process.patDefaultSequence*
                             process.patPFMetByMVA*
                             process.patConversions*
                             process.puJetIdSqeuence

                                                              )



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


process.maxEvents.input = 10
########################################################################################################
