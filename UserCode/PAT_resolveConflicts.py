
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



###################################################
# rm MC matching if DATA
###################################################

if not runOnMC:
  removeMCMatchingPF2PAT( process, '' )


###################################################
# load the PU JetID sequence
###################################################
process.load("CMGTools.External.pujetidsequence_cff")

process.out.outputCommands +=['keep *_puJetId*_*_*']
process.out.outputCommands +=['keep *_puJetMva*_*_*']
###################################################
# Store the Vertex Collection
# filtering is possible at this
# stage (currently requiring at least one)
###################################################

from PhysicsTools.PatAlgos.tools.coreTools import *
from PhysicsTools.PatAlgos.tools.trackTools import *

process.VertexPresent = cms.EDFilter("VertexSelector",
                             src = cms.InputTag("offlinePrimaryVertices"),
                             cut = cms.string("!isFake && ndof > 4 && abs(z) < 15 && position.Rho < 2"),
                             filter = cms.bool(True),
                             )

process.out.outputCommands +=['keep *_offlinePrimaryVertices*_*_*']


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

process.out.outputCommands +=['keep *_selectedPatMuons*_*_*']


###################################################
# add in hadronic taus
# based on
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePFTauID#5_3_12_and_higher
###################################################


process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")

switchToPFTauHPS(process)



###################################################
# store electrons and MVA ID
###################################################


process.load('EgammaAnalysis.ElectronTools.electronIdMVAProducer_cfi')
process.mvaIDelec = cms.Sequence(  process.mvaTrigV0 + process.mvaNonTrigV0 + process.mvaTrigNoIPV0 )
process.patElectrons.electronIDSources.mvaTrigV0    = cms.InputTag("mvaTrigV0")
process.patElectrons.electronIDSources.mvaNonTrigV0 = cms.InputTag("mvaNonTrigV0")
process.patElectrons.electronIDSources.mvaTrigNoIPV0 = cms.InputTag("mvaTrigNoIPV0")

process.patPF2PATSequence.replace( process.patElectrons, process.mvaIDelec * process.patElectrons )


###################################################
# keep conversion info and gsf electrons just in
# case they are needed
###################################################

process.patConversions = cms.EDProducer("PATConversionProducer",
                                        electronSource = cms.InputTag("gsfElectrons")
                                        )
process.out.outputCommands +=['keep *_patConversions*_*_*']
process.out.outputCommands +=['keep *_conversions*_*_*']
process.out.outputCommands +=['keep *_gsfElectrons*_*_*']


###################################################
# MVA MET (this must be before muon and electron sequences, don't
# understand why at this point)
###################################################
#from JetMETCorrections.METPUSubtraction.mvaPFMET_leptons_PAT_cfi import *
#process.load('JetMETCorrections.Configuration.JetCorrectionProducers_cff')
#process.load('JetMETCorrections.METPUSubtraction.

#process.mvametseq      = cms.Sequence(process.pfMEtMVAsequence)
#process.mvametpath        = cms.Path(process.mvametseq)




#process.patPFMetByMVA = process.patMETs.clone(
#    metSource = cms.InputTag('pfMEtMVA'),
#    addMuonCorrections = cms.bool(False),
#    genMETSource = cms.InputTag('genMetTrue')
#)


#process.mvamet = cms.Sequence(process.pfMEtMVAsequence*process.patDefaultSequence*process.patPFMetByMVA)

#process.out.outputCommands +=['keep *_pfMEtMVA*_*_*']
#process.out.outputCommands +=['keep *_patPFMetByMVA*_*_*']


###################################################
# using SelectEvents, you can filter on the paths (sequences)
# defined above; there will be a pass/fail report at the
# end of the process
###################################################
#SelectMuonEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('muonSequence') )
#process.out.SelectEvents.SelectEvents = ['muonSequence']

##################################################
# Let it run, note: we absolutely need
# a path called 'p' unless we edit patTemplate_cfg.py
# which expects p in the selector
###################################################
process.pX = cms.Path(       process.VertexPresent+
                             getattr(process,"patPF2PATSequence"+postfix)+
                             process.puJetIdSqeuence+
                             process.PFTau
                             #process.SelectMuonEvents
                                  )



if not postfix == "":
    process.pX += process.recoTauClassicHPSSequence # re-run tau discriminators (new version)
    process.pX += process.patDefaultSequence


########################################################################################################




process.out.fileName = 'patTuple_testing.root'
process.source.fileNames=['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/'+
                          'GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/'+
                          'PU_S10_START53_V7A-v1/0000/00E903E2-9FE9-E111-8B1E-003048FF86CA.root']

process.maxEvents.input = 100
########################################################################################################
