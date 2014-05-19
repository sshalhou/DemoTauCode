
########################################################################################################
import FWCore.ParameterSet.Config as cms
########################################################################################################

#process = cms.Process("DemoTauAna")

###################################################
# Import skeleton
###################################################
from PhysicsTools.PatAlgos.patTemplate_cfg import *

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


KeepAll = True




runOnMC = True
if runOnMC:
  process.GlobalTag.globaltag = 'START53_V23::All'
else:
  process.GlobalTag.globaltag = 'SOMETHING_FOR_DATA::All'

########################################################################################################
# Setup PF2PAT (for now we will not run both PAT and PF2PAT, everything will be PF2PAT)
########################################################################################################

###################################################
# tau discriminators must be re-run
###################################################
process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")
process.load("PhysicsTools.PatAlgos.patSequences_cff")




###################################################
# setup PF2PAT, empty postfix means
# only PF2PAT and not both PAT + PF2PAT
###################################################
from PhysicsTools.PatAlgos.tools.pfTools import *

###################################################
# use PF isolation
###################################################

usePFIso(process)

# if the sample does not contain value map of PF candidate "particleFlow:electrons", use following line.
# this appears to be the case for our test sample
process.patElectrons.pfElectronSource = 'particleFlow'


postfix = ""
jetAlgo = "AK5"
usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo, runOnMC=runOnMC, postfix=postfix)
switchToPFJets(process)

# needed for MVA met, but need to be here
from JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_PAT_cfi import *
process.load('JetMETCorrections.Configuration.JetCorrectionProducers_cff')
process.load('JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_cff')


##################################################
# specify settings for met mva
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/MVAMet
# recoil corrections should be applied at Ntuple stage
# in later stages isomuons, isoelectrons, and isotaus
# should be replaced by our final selected leptons
###################################################
process.pfMEtMVA = process.pfMEtMVA.clone(srcLeptons = cms.VInputTag("isomuons","isoelectrons","isotaus"),
                                          useType1 = cms.bool(True)
                                          )




###################################################
# rm MC matching if DATA
###################################################

if not runOnMC:
  removeMCMatchingPF2PAT( process, 'All' )


###################################################
# load the PU JetID sequence
###################################################
process.load("CMGTools.External.pujetidsequence_cff")

process.out.outputCommands +=['keep *_selectedPatJets*_*_*']
process.out.outputCommands +=['keep *_puJetId*_*_*']
process.out.outputCommands +=['keep *_puJetMva*_*_*']

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
# Store the Muons
###################################################

# https://twiki.cern.ch/twiki/bin/view/Main/SingleTopHiggsBBEventSel
# setting to 9999 eliminates the default filtering w.r.t the 1st vertex in
# the vertex src list; there is no gaurantee that the 1st vertex is the
# one that we will end up selecting

process.pfMuonsFromVertex.d0Cut = 9999.
process.pfMuonsFromVertex.d0SigCut = 9999.
process.pfMuonsFromVertex.dzCut = 9999.
process.pfMuonsFromVertex.dzSigCut = 9999.

process.out.outputCommands +=['keep *_selectedPatMuons*_*_*']




###################################################
# add in hadronic taus
# based on
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePFTauID#5_3_12_and_higher
###################################################

process.load("Configuration.StandardSequences.GeometryPilot2_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")

switchToPFTauHPS(process)

process.out.outputCommands += ['keep *_selectedPatTaus*_*_*']

###################################################
# store electrons and MVA ID
###################################################


process.load('EgammaAnalysis.ElectronTools.electronIdMVAProducer_cfi')
process.mvaIDelec = cms.Sequence(  process.mvaTrigV0 + process.mvaNonTrigV0 + process.mvaTrigNoIPV0 )
process.patElectrons.electronIDSources.mvaTrigV0    = cms.InputTag("mvaTrigV0")
process.patElectrons.electronIDSources.mvaNonTrigV0 = cms.InputTag("mvaNonTrigV0")
process.patElectrons.electronIDSources.mvaTrigNoIPV0 = cms.InputTag("mvaTrigNoIPV0")

process.patPF2PATSequence.replace( process.patElectrons, process.mvaIDelec * process.patElectrons )

process.out.outputCommands +=['keep *_selectedPatElectrons*_*_*']


###################################################
# keep conversion info and gsf electrons just in
# case they are needed
###################################################

process.patConversions = cms.EDProducer("PATConversionProducer",
                                        electronSource = cms.InputTag("gsfElectrons")
                                        )
#process.out.outputCommands +=['keep *_patConversions*_*_*']
#process.out.outputCommands +=['keep *_conversions*_*_*']
#process.out.outputCommands +=['keep *_gsfElectrons*_*_*']


###################################################
# MVA MET (this must be before muon and electron sequences, don't
# understand why at this point)
###################################################





#process.mvamet = cms.Sequence(process.pfMEtMVAsequence*process.patDefaultSequence*process.patPFMetByMVA)
#process.patPF2PATSequence.replace( process.pfMET, process.mvamet)
#process.mvametseq      = cms.Sequence(process.pfMEtMVAsequence)
#process.mvametpath        = cms.Path(process.mvametseq)




#process.mvametseq      = cms.Sequence(process.pfMEtMVAsequence)
#process.mvametpath        = cms.Path(process.mvametseq)
process.patPFMetByMVA = process.patMETs.clone(
    metSource = cms.InputTag('pfMEtMVA'),
    addMuonCorrections = cms.bool(False),
    genMETSource = cms.InputTag('genMetTrue')
)
#process.mvamet = cms.Sequence(process.pfMEtMVAsequence*getattr(process,"patPF2PATSequence"+postfix)*process.patPFMetByMVA)
process.out.outputCommands +=['keep *_pfMEtMVA*_*_*']
process.out.outputCommands +=['keep *_patPFMetByMVA*_*_*']







# keep CSV info
process.out.outputCommands +=['keep *_combinedSecondaryVertexBJetTagsAOD_*_*']

###################################################
# apply selection cuts on physics objects
# to keep that PATtuple to a reasonable kB/event
###################################################


from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
process.selectedPatJets = selectedPatJets.clone(src = 'patJets', cut = 'correctedP4(0).pt > 10. && abs(eta)<4.7')

from PhysicsTools.PatAlgos.selectionLayer1.tauSelector_cfi import *
process.selectedPatTaus = selectedPatTaus.clone(src = 'patTaus', cut = 'pt >18. && decayMode>-1')


from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
process.selectedPatMuons = selectedPatMuons.clone(src = 'patMuons', cut = 'pt >3.')


from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
process.selectedPatElectrons = selectedPatElectrons.clone(src = 'patElectrons', cut = 'et >8.')

###################################################
# drop some large unused collections
###################################################

process.out.outputCommands +=['drop patPFParticles_selectedPatPFParticles__PAT']
process.out.outputCommands +=['drop recoPFCandidates_selectedPatJets_pfCandidates_PAT']

###################################################
# require at least two lepton candidates
# in the event
###################################################


# module to filter on the number of Electrons
process.countSelectedLeptons = cms.EDFilter("PATLeptonCountFilter",
  electronSource = cms.InputTag("selectedPatElectrons"),
  muonSource     = cms.InputTag("selectedPatMuons"),
  tauSource      = cms.InputTag("selectedPatTaus"),
  countElectrons = cms.bool(True),
  countMuons     = cms.bool(True),
  countTaus      = cms.bool(True),
  minNumber = cms.uint32(2),
  maxNumber = cms.uint32(999999),
  filter = cms.bool(True)
)




#from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
#process.selectedPatElectrons = selectedPatElectrons.clone(src = 'patElectrons', cut = 'et >8.')

##################################################
# run the MET systematic tool
##################################################


#############################
# need to create PAT versions
# of the iso-leptons for use with
# the met uncertainty tool
#############################



#from PhysicsTools.PatAlgos.producersLayer1.electronProducer_cfi import *
#process.patIsoElec = process.patElectrons.clone(electronSource = cms.InputTag("isoelectrons"))
#from PhysicsTools.PatAlgos.producersLayer1.muonProducer_cfi import *
#process.patIsoMuon = process.patMuons.clone(muonSource = cms.InputTag("isomuons"))
#from PhysicsTools.PatAlgos.producersLayer1.tauProducer_cfi import *
#process.patIsoTau = process.patTaus.clone(tauSource = cms.InputTag("isotaus")
#                                          )


# apply type I/type I + II PFMEt corrections to pat::MET object
# and estimate systematic uncertainties on MET
from PhysicsTools.PatUtils.tools.metUncertaintyTools import runMEtUncertainties


process.smearedUncorrectedJetsForPFMEtByMVA = cms.EDProducer("SmearedPFJetProducer",
    jetResolutions = cms.PSet(
        resolutionsEra = cms.string('Spring10'),
        HB_EtResPar = cms.vdouble(0.0, 1.22, 0.05),
        EE_PhiResPar = cms.vdouble(0.02511),
        jdpt9 = cms.vdouble(0.843, 0.885, 1.245, 1.665, 1.944,
            1.981, 1.972, 2.875, 3.923, 7.51),
        jdpt8 = cms.vdouble(0.889, 0.939, 1.166, 1.365, 1.553,
            1.805, 2.06, 2.22, 2.268, 2.247),
        jdpt7 = cms.vdouble(1.094, 1.139, 1.436, 1.672, 1.831,
            2.05, 2.267, 2.549, 2.785, 2.86),
        jdpt6 = cms.vdouble(1.213, 1.298, 1.716, 2.015, 2.191,
            2.612, 2.863, 2.879, 2.925, 2.902),
        jdpt5 = cms.vdouble(1.049, 1.149, 1.607, 1.869, 2.012,
            2.219, 2.289, 2.412, 2.695, 2.865),
        jdpt4 = cms.vdouble(0.85, 0.961, 1.337, 1.593, 1.854,
            2.005, 2.209, 2.533, 2.812, 3.047),
        jdpt3 = cms.vdouble(0.929, 1.04, 1.46, 1.74, 2.042,
            2.289, 2.639, 2.837, 2.946, 2.971),
        jdpt2 = cms.vdouble(0.841, 0.937, 1.316, 1.605, 1.919,
            2.295, 2.562, 2.722, 2.943, 3.293),
        jdpt1 = cms.vdouble(0.718, 0.813, 1.133, 1.384, 1.588,
            1.841, 2.115, 2.379, 2.508, 2.772),
        jdpt0 = cms.vdouble(0.749, 0.829, 1.099, 1.355, 1.584,
            1.807, 2.035, 2.217, 2.378, 2.591),
        HE_EtResPar = cms.vdouble(0.0, 1.3, 0.05),
        HF_PhiResPar = cms.vdouble(0.05022),
        PF_PhiResType7 = cms.vdouble(0.02511),
        HE_PhiResPar = cms.vdouble(0.02511),
        EE_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
        PF_PhiResType2 = cms.vdouble(0.002),
        PF_PhiResType3 = cms.vdouble(0.002),
        HF_EtResPar = cms.vdouble(0.0, 1.82, 0.09),
        resolutionsAlgo = cms.string('AK5PF'),
        PF_PhiResType6 = cms.vdouble(0.02511),
        HB_PhiResPar = cms.vdouble(0.02511),
        PF_PhiResType4 = cms.vdouble(0.0028, 0.0, 0.0022),
        PF_PhiResType5 = cms.vdouble(0.1, 0.1, 0.13),
        ptresolthreshold = cms.double(10.0),
        EB_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
        jdphi8 = cms.vdouble(0.059, 0.057, 0.051, 0.044, 0.038,
            0.035, 0.037, 0.032, 0.028, 0.028),
        EB_PhiResPar = cms.vdouble(0.00502),
        jdphi9 = cms.vdouble(0.062, 0.059, 0.053, 0.047, 0.042,
            0.045, 0.036, 0.032, 0.034, 0.044),
        PF_PhiResType1 = cms.vdouble(0.002),
        jdphi4 = cms.vdouble(0.042, 0.042, 0.043, 0.042, 0.038,
            0.036, 0.036, 0.033, 0.031, 0.031),
        HO_PhiResPar = cms.vdouble(0.02511),
        jdphi2 = cms.vdouble(0.04, 0.04, 0.04, 0.04, 0.04,
            0.038, 0.036, 0.035, 0.034, 0.033),
        jdphi1 = cms.vdouble(0.034, 0.035, 0.035, 0.035, 0.035,
            0.034, 0.031, 0.03, 0.029, 0.027),
        jdphi0 = cms.vdouble(0.034, 0.034, 0.034, 0.034, 0.032,
            0.031, 0.028, 0.027, 0.027, 0.027),
        jdphi7 = cms.vdouble(0.077, 0.072, 0.059, 0.05, 0.045,
            0.042, 0.039, 0.039, 0.037, 0.031),
        jdphi6 = cms.vdouble(0.084, 0.08, 0.072, 0.065, 0.066,
            0.06, 0.051, 0.049, 0.045, 0.045),
        jdphi5 = cms.vdouble(0.069, 0.069, 0.064, 0.058, 0.053,
            0.049, 0.049, 0.043, 0.039, 0.04),
        HO_EtResPar = cms.vdouble(0.0, 1.3, 0.005),
        jdphi3 = cms.vdouble(0.042, 0.043, 0.044, 0.043, 0.041,
            0.039, 0.039, 0.036, 0.034, 0.031),
        PF_EtResType5 = cms.vdouble(0.41, 0.52, 0.25),
        PF_EtResType4 = cms.vdouble(0.042, 0.1, 0.0),
        PF_EtResType7 = cms.vdouble(0.0, 1.22, 0.05),
        PF_EtResType6 = cms.vdouble(0.0, 1.22, 0.05),
        PF_EtResType1 = cms.vdouble(0.05, 0, 0),
        PF_EtResType3 = cms.vdouble(0.05, 0, 0),
        PF_EtResType2 = cms.vdouble(0.05, 0, 0)
    ),
    src = cms.InputTag("ak5PFJets"),
    srcGenJets = cms.InputTag("ak5GenJetsNoNu"),
    skipCorrJetPtThreshold = cms.double(0.01),
    skipRawJetPtThreshold = cms.double(10.0),
    inputFileName = cms.FileInPath('PhysicsTools/PatUtils/data/pfJetResolutionMCtoDataCorrLUT.root'),
    dRmaxGenJetMatch = cms.string('TMath::Min(0.5, 0.1 + 0.3*TMath::Exp(-0.05*(genJetPt - 10.)))'),
    lutName = cms.string('pfJetResolutionMCtoDataCorrLUT'),
    sigmaMaxGenJetMatch = cms.double(5.0),
    jetCorrLabel = cms.string('ak5PFL1FastL2L3'),
    skipJetSelection = cms.string('((neutralEmEnergy()+ chargedEmEnergy())/(max(neutralEmEnergy(), HFEMEnergy()) + neutralHadronEnergy() + chargedHadronEnergy() + HFHadronEnergy() + chargedEmEnergy())) > 0.8')
)


runMEtUncertainties(process,
      electronCollection = cms.InputTag('selectedPatElectrons'),
      photonCollection = '',
      muonCollection = cms.InputTag('selectedPatMuons'),
      tauCollection = cms.InputTag('selectedPatTaus'),
      jetCollection = cms.InputTag('selectedPatJets'),
      jetCorrLabel = "L3Absolute",
      doSmearJets = True,
      makeType1corrPFMEt = True,
      makeType1p2corrPFMEt = True,
      makePFMEtByMVA = True,
      makeNoPileUpPFMEt = False,
      doApplyType0corr = False


                      )




##################################################
# Let it run
###################################################
process.p = cms.Path(        process.VertexPresent+
                             process.pfMEtMVAsequence*
                             getattr(process,"patPF2PATSequence"+postfix)*
                             process.patPFMetByMVA+
                             #getattr(process,"patPF2PATSequence"+postfix)+
                             process.recoTauClassicHPSSequence+
                             process.puJetIdSqeuence+
                             process.countSelectedLeptons
#                             +process.patIsoElec
#                             +process.patIsoMuon
#                             +process.patIsoTau
                             +process.smearedUncorrectedJetsForPFMEtByMVA
                             +process.metUncertaintySequence
                             #process.PFTau
                             #process.SelectMuonEvents
                                  )



##################################################



if not postfix == "":
    process.p += process.recoTauClassicHPSSequence # re-run tau discriminators (new version)
    process.p += process.patDefaultSequence

###################################################
# require all paths to pass
###################################################

process.out.SelectEvents.SelectEvents = ['p']

########################################################################################################






if KeepAll:
  process.out.outputCommands +=['keep *_*_*_*']

#process.out.fileName = 'patTuple_testing.root'
process.out.fileName = '/uscms/home/shalhout/no_backup/patTuple_testing.root'
process.source.fileNames=['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/'+
                          'GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/'+
                          'PU_S10_START53_V7A-v1/0000/00E903E2-9FE9-E111-8B1E-003048FF86CA.root']

process.maxEvents.input = 4
########################################################################################################
