import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
import math

##############
# helper to check div

def divisionHelp(num, den):
  returnVal = 1.0
  if den > 0.00:
    returnVal = num/den
  else:
    print 'bad division attempted setting to 1.0 ', num, den
    returnVal = 1.0
  return returnVal

##############
# pileUp weight

def PUweight(chain, maxPairTypeAndIndex):
  returnWeight = 1.0
  i = maxPairTypeAndIndex[0]
  if maxPairTypeAndIndex[1] == 'eleTau':
    returnWeight = chain.eT_puWeight[i]
  elif maxPairTypeAndIndex[1] == 'muTau':
    returnWeight = chain.muT_puWeight[i]
  return returnWeight

##################
# high pt tau ID sf

def highPtTauSYS(chain, maxPairTypeAndIndex):
  returnWeight = 1.0
  tauPt = 0.0
  i = maxPairTypeAndIndex[0]
  if maxPairTypeAndIndex[1] == 'eleTau':
    Tvec = TLorentzVector(0,0,0,0)
    Tvec.SetXYZT(chain.eT_tau_genP4_x[i], chain.eT_tau_genP4_y[i], chain.eT_tau_genP4_z[i],chain.eT_tau_genP4_t[i])
    tauPt = Tvec.Pt()
  elif maxPairTypeAndIndex[1] == 'muTau':
    Tvec = TLorentzVector(0,0,0,0)
    Tvec.SetXYZT(chain.muT_tau_genP4_x[i], chain.muT_tau_genP4_y[i], chain.muT_tau_genP4_z[i],chain.muT_tau_genP4_t[i])
    tauPt = Tvec.Pt()
  if math.isnan(tauPt) is True:
     returnWeight = 1.0
  else:
    returnWeight = (0.20*tauPt/1000.0)
  print tauPt,   returnWeight
  return returnWeight




##################################
# trigger weights for 'regular MC'

def mcTriggerWeight(chain, maxPairTypeAndIndex):
  returnWeight = 1.0
  i = maxPairTypeAndIndex[0]
  if maxPairTypeAndIndex[1] == 'eleTau':
    returnWeight *= divisionHelp(chain.eT_EffDataELE20andELE22[i], chain.eT_EffMcELE20andELE22[i])
    returnWeight *= divisionHelp(chain.eT_HadronicTauDataTrigEffAntiEMed[i], chain.eT_HadronicTauMcTrigEffAntiEMed[i])
  elif maxPairTypeAndIndex[1] == 'muTau':
    returnWeight *= divisionHelp(chain.muT_EffDataISOMU17andISOMU18[i], chain.muT_EffMcISOMU17andISOMU18[i])
    returnWeight *= divisionHelp(chain.muT_HadronicTauDataTrigEffAntiMuMed[i], chain.muT_HadronicTauMcTrigEffAntiMuMed[i])
  return returnWeight


################################
# lepton ID eff weights

def leptonIDweights(chain, maxPairTypeAndIndex):
  returnWeight = 1.0
  i = maxPairTypeAndIndex[0]
  if maxPairTypeAndIndex[1] == 'eleTau':
    returnWeight *= divisionHelp(chain.eT_electronDataIDweight[i], chain.eT_electronMcIDweight[i])
  elif maxPairTypeAndIndex[1] == 'muTau':
    returnWeight *= divisionHelp(chain.muT_muonDataIDweight[i], chain.muT_muonMcIDweight[i])
  return returnWeight

################################
# lepton Isolation eff weights

def leptonISOLweights(chain, maxPairTypeAndIndex):
  returnWeight = 1.0
  i = maxPairTypeAndIndex[0]
  if maxPairTypeAndIndex[1] == 'eleTau':
    returnWeight *= divisionHelp(chain.eT_electronDataISOLweight[i], chain.eT_electronMcISOLweight[i])
  elif maxPairTypeAndIndex[1] == 'muTau':
    returnWeight *= divisionHelp(chain.muT_muonDataISOLweight[i], chain.muT_muonMcISOLweight[i])
  return returnWeight

#################################
#  high pT tau trigger Bug
#  warning EMBEDDED should use data only

def highPtTauTriggerBugWeights(chain, maxPairTypeAndIndex):
  returnWeight = 1.0
  i = maxPairTypeAndIndex[0]
  if maxPairTypeAndIndex[1] == 'eleTau':
    returnWeight *= divisionHelp(chain.eT_EffDataHighPtTauTrigger[i], chain.eT_EffMcHighPtTauTrigger[i])
  elif maxPairTypeAndIndex[1] == 'muTau':
    returnWeight *= divisionHelp(chain.muT_EffDataHighPtTauTrigger[i], chain.muT_EffMcHighPtTauTrigger[i])
  return returnWeight

##########################
# Decay Mode Correction
# only for signal and Z->tau tau

def decayModeCorrection(chain, maxPairTypeAndIndex):
  returnWeight = 1.0
  i = maxPairTypeAndIndex[0]
  if maxPairTypeAndIndex[1] == 'eleTau':
    returnWeight *= chain.eT_DecayModeCorrectionFactor[i]
  elif maxPairTypeAndIndex[1] == 'muTau':
    returnWeight *= chain.muT_DecayModeCorrectionFactor[i]
  return returnWeight

#########################
# tau polarization


def tauPolarizationWeight(chain, maxPairTypeAndIndex):
  returnWeight = 1.0
  i = maxPairTypeAndIndex[0]
  if maxPairTypeAndIndex[1] == 'eleTau':
    returnWeight *= chain.eT_TauSpinnerWT[i]
  elif maxPairTypeAndIndex[1] == 'muTau':
    returnWeight *= chain.muT_TauSpinnerWT[i]
  return returnWeight



#################################
#  higgs pt reweight
#  option for old or new, as well as sys

def higgsPtReWeight(chain, maxPairTypeAndIndex, USENEWorUSEOLD, UPorDOWNorNOMINAL):
  returnWeight = 1.0
  if USENEWorUSEOLD == 'USENEW':
    returnWeight  = higgsPtReWeightNEW(chain, maxPairTypeAndIndex, UPorDOWNorNOMINAL)
  elif USENEWorUSEOLD == 'USEOLD':
    returnWeight  = higgsPtReWeightOLD(chain, maxPairTypeAndIndex, UPorDOWNorNOMINAL)
  else:
    print 'not USENEW or USEOLD, HpT wt set to 1.0'
  return returnWeight

def higgsPtReWeightOLD(chain, maxPairTypeAndIndex, UPorDOWNorNOMINAL):
  i = maxPairTypeAndIndex[0]
  if maxPairTypeAndIndex[1] == 'eleTau':
    if UPorDOWNorNOMINAL == 'UP':
      return chain.eT_upHIGLUXHQTmhmax[i]
    elif UPorDOWNorNOMINAL == 'DOWN':
      return chain.eT_downHIGLUXHQTmhmax[i]
    elif UPorDOWNorNOMINAL == 'NOMINAL':
      return chain.eT_nominalHIGLUXHQTmhmax[i]
  if maxPairTypeAndIndex[1] == 'muTau':
    if UPorDOWNorNOMINAL == 'UP':
      return chain.muT_upHIGLUXHQTmhmax[i]
    elif UPorDOWNorNOMINAL == 'DOWN':
      return chain.muT_downHIGLUXHQTmhmax[i]
    elif UPorDOWNorNOMINAL == 'NOMINAL':
      return chain.muT_nominalHIGLUXHQTmhmax[i]
  print 'BAD higgsPt weight', maxPairTypeAndIndex[1], 'OR', UPorDOWNorNOMINAL, 'set weight to 1.0'
  return 1.0

def higgsPtReWeightNEW(chain, maxPairTypeAndIndex, UPorDOWNorNOMINAL):
  i = maxPairTypeAndIndex[0]
  if maxPairTypeAndIndex[1] == 'eleTau':
    if UPorDOWNorNOMINAL == 'UP':
      return chain.eT_upPOWHEGmhmod[i]
    elif UPorDOWNorNOMINAL == 'DOWN':
      return chain.eT_downPOWHEGmhmod[i]
    elif UPorDOWNorNOMINAL == 'NOMINAL':
      return chain.eT_nominalPOWHEGmhmod[i]
  if maxPairTypeAndIndex[1] == 'muTau':
    if UPorDOWNorNOMINAL == 'UP':
      return chain.muT_upPOWHEGmhmod[i]
    elif UPorDOWNorNOMINAL == 'DOWN':
      return chain.muT_downPOWHEGmhmod[i]
    elif UPorDOWNorNOMINAL == 'NOMINAL':
      return chain.muT_nominalPOWHEGmhmod[i]
  print 'BAD higgsPt weight', maxPairTypeAndIndex[1], 'OR', UPorDOWNorNOMINAL, 'set weight to 1.0'
  return 1.0





def signalSUSYweight(chain, maxPairTypeAndIndex, Verbose):
  returnWeight = 1.0
  allWeights = {}
  allWeights['PU'] = PUweight(chain, maxPairTypeAndIndex)
  allWeights['regularTrigger'] = mcTriggerWeight(chain, maxPairTypeAndIndex)
  allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
  allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
  allWeights['TriggerBug'] =  highPtTauTriggerBugWeights(chain, maxPairTypeAndIndex)
  allWeights['higgsPtNEW'] = higgsPtReWeight(chain, maxPairTypeAndIndex, 'USENEW', 'NOMINAL')
  allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
  #allWeights['tauPolarization'] = tauPolarizationWeight(chain, maxPairTypeAndIndex)
  # this is a SYS allWeights['highPtTauEff'] = highPtTauSF(chain, maxPairTypeAndIndex)
  for key, value in allWeights.iteritems():
    returnWeight*=value
  if Verbose:
    print allWeights
  return returnWeight
