
runOnMC = True

########################################################################################################
# Setup PF2PAT (for now we will not run both PAT and PF2PAT, everything will be PF2PAT)
########################################################################################################

###################################################
# Import skeleton
###################################################

from PhysicsTools.PatAlgos.patTemplate_cfg import *

###################################################
# load the PAT config
###################################################

# tau discriminators must be re-run
process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")
process.load("PhysicsTools.PatAlgos.patSequences_cff")

###################################################
# setup PF2PAT, empty postfix means
# only PF2PAT and not both PAT + PF2PAT
###################################################
from PhysicsTools.PatAlgos.tools.pfTools import *

postfix = ""
jetAlgo = "AK5"
usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo, runOnMC=runOnMC, postfix=postfix)


###################################################
# rm MC matching if DATA
###################################################

if not runOnMC:
  removeMCMatchingPF2PAT( process, '' )
########################################################################################################

##################################################
# Let it run
###################################################
process.createpattuple = cms.Path(
                             getattr(process,"patPF2PATSequence"+postfix)
                                  )
if not postfix == "":
    process.createpattuple += process.recoTauClassicHPSSequence # re-run tau discriminators (new version)
    process.createpattuple += process.patDefaultSequence

########################################################################################################


process.out.fileName = 'patTuple_testing.root'
process.source.fileNames=['root://cmsxrootd-site.fnal.gov//store/mc/Summer12_DR53X/'+
                          'GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/AODSIM/'+
                          'PU_S10_START53_V7A-v1/0000/00E903E2-9FE9-E111-8B1E-003048FF86CA.root']

process.maxEvents.input = 100
########################################################################################################
