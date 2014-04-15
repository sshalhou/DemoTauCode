import FWCore.ParameterSet.Config as cms

## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

from PhysicsTools.PatAlgos.tools.coreTools import *


#-------------------------------------------------
# selection step 1: vertex filter
#-------------------------------------------------

# vertex filter
process.Step1VertexPresent = cms.EDFilter("VertexSelector",
                             src = cms.InputTag("offlinePrimaryVertices"),
                             cut = cms.string("!isFake && ndof > 4 && abs(z) < 15 && position.Rho < 2"),
                             filter = cms.bool(True),
                             )

#-------------------------------------------------
# selection steps 2 and 3: muon selection
#-------------------------------------------------

from PhysicsTools.PatAlgos.cleaningLayer1.muonCleaner_cfi import *
process.Step2GlobalPFMuons = cleanPatMuons.clone(preselection =
                                               'isGlobalMuon &'
                                               'isPFMuon'
                                               )





from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
process.Step3GlobalPFMuonsCount = countPatMuons.clone(src = 'Step2GlobalPFMuons', minNumber = 1, maxNumber = 1000)


#-------------------------------------------------
# selection steps 4 and 5: electron selection
#-------------------------------------------------


######### ELECTRON MVAs -- START


process.load('EgammaAnalysis.ElectronTools.electronIdMVAProducer_cfi')
process.mvaID = cms.Sequence(  process.mvaTrigV0 + process.mvaNonTrigV0 + process.mvaTrigNoIPV0 )

#Electron ID
process.patElectrons.electronIDSources = cms.PSet(
    #MVA
    mvaTrigV0 = cms.InputTag("mvaTrigV0"),
    mvaNonTrigV0 = cms.InputTag("mvaNonTrigV0"),
    mvaTrigNoIPV0 = cms.InputTag("mvaTrigNoIPV0"),
    )

#add pat conversions
process.patConversions = cms.EDProducer("PATConversionProducer",
                                        # input collection
                                        #electronSource = cms.InputTag("gsfElectrons"),
                                        electronSource = cms.InputTag("cleanPatElectrons")
                                        )



######### ELECTRON MVAs -- END


from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
process.Step4Electron = selectedPatElectrons.clone(src = 'selectedPatElectrons',
                                                   cut =
                                                   'et > 0.0'
                                                  )


from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
process.Step5ElectronCount  = countPatElectrons.clone(src = 'Step4Electron', minNumber = 1, maxNumber = 1000)


## define the MVA+Filter sequence
process.electronSequenceMVAcombined = cms.Path(
    process.mvaID *
    process.patDefaultSequence*
    process.patConversions*
    process.Step1VertexPresent*
    process.Step4Electron *
    process.Step5ElectronCount
    )


#------------
# muon path (for some reason this has to be after the electron MVA sequence)
#------------

process.muonSequence = cms.Path(process.Step1VertexPresent *
                                 process.patDefaultSequence *
                                 process.Step2GlobalPFMuons *
                                 process.Step3GlobalPFMuonsCount
                                )


#--------------------------------
# hadronic taus step 6, 7, and 8
#---------------------------------

from PhysicsTools.PatAlgos.tools.tauTools import *

# based on (https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePFTauID#5_3_12_and_higher)
process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")

# based on https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePFTauID#5_3_12_and_higher
# not sure this next line is really needed
switchToPFTauHPS(process)

## define the path

#process.tauStep6 = cms.Path(process.recoTauClassicHPSSequence+process.PFTau+process.patDefaultSequence)


# not really sure this is doing anything; may just want to omit it
from PhysicsTools.PatAlgos.selectionLayer1.tauCountFilter_cfi import *
process.Step8TauCount  = countPatTaus.clone(src = 'selectedPatTaus', minNumber = 1, maxNumber = 10000)


process.tauSequence = cms.Path(process.Step1VertexPresent *
                              process.recoTauClassicHPSSequence*
                              process.PFTau*
                              process.patDefaultSequence*
                              process.Step8TauCount
                               )




process.out.outputCommands +=['keep *_patConversions*_*_*']

process.out.outputCommands +=['keep *_offlinePrimaryVertices*_*_*']

#########################

#process.out.SelectEvents.SelectEvents = ['electronSequenceMVAcombined','muonSequence']

process.out.SelectEvents.SelectEvents = ['tauSequence']

process.out.fileName = 'patTuple_topSelection.root'
#########################


#########################
# MVA MET
# recoil corrections will be done at ntuple stage (I think ..)
#########################

process = cms.Process("analysisX")


#########################
######
######
#########################
############################
process.source.fileNames=['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/00E903E2-9FE9-E111-8B1E-003048FF86CA.root']

process.maxEvents.input = 100



#process.options.wantSummary = False
#
#
#
#
#
