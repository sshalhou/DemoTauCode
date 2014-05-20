
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


KeepAll = False




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
# in later stages isomuons, isoelectrons are a resonable
# preselection for MET corrections
###################################################
process.pfMEtMVA = process.pfMEtMVA.clone(srcLeptons = cms.VInputTag("isomuons","isoelectrons","isotaus")
                                          )


process.out.outputCommands +=['keep *_isomuons*_*_*']


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


process.load("Configuration.Geometry.GeometryPilot2_cff")
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
                process.patPFMETtype0Corr*
                getattr(process,"patPF2PATSequence"+postfix)*
                process.patPFMetByMVA
                                )


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


##################################################
# run the MET systematic tool
##################################################

# apply type I/type I + II PFMEt corrections to pat::MET object
# and estimate systematic uncertainties on MET
from PhysicsTools.PatUtils.tools.metUncertaintyTools import runMEtUncertainties
runMEtUncertainties(process)


##################################################
# Let it run
###################################################
process.p = cms.Path(        process.VertexPresent+
                             process.mvametPF2PATsequence+
                             process.recoTauClassicHPSSequence+
                             process.puJetIdSqeuence+
                             process.countSelectedLeptons
                                  )



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

process.maxEvents.input = 25
########################################################################################################
