import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile

from Configurations.python.electronID import *
from Configurations.python.muonID import *
from Configurations.python.tauID import *
from Configurations.python.triggerRequirements import *
from Configurations.python.eventRequirements import *


#################
# default selection

def passesDefaultSelectionETau(chain,index,UseNewTriggers,Verbose):
    passesCutsETau = True
    if electronID(chain,index,Verbose) is False:
        passesCutsETau = False
    if tauID_eTau(chain, index, Verbose) is False:
        passesCutsETau = False
    if pairCutsETau(chain, index,Verbose) is False:
        passesCutsETau = False
    if electronTrigger(chain,index,UseNewTriggers) is False:
        passesCutsETau = False
    if tauTriggerForETau(chain,index,UseNewTriggers) is False:
        passesCutsETau = False
    if chain.eT_correctedSVFitMass[index] < 50:
        passesCutsETau = False
    return passesCutsETau

def passesDefaultSelectionMuTau(chain,index,UseNewTriggers,Verbose):
    passesCutsMuTau = True
    if muonID(chain,index,Verbose) is False:
        passesCutsMuTau = False
    if tauID_muTau(chain, index, Verbose) is False:
        passesCutsMuTau = False
    if pairCutsMuTau(chain, index,Verbose) is False:
        passesCutsMuTau = False
    if muonTrigger(chain,index,UseNewTriggers) is False:
        passesCutsMuTau = False
    if tauTriggerForMuTau(chain,index,UseNewTriggers) is False:
        passesCutsMuTau = False
    if chain.muT_correctedSVFitMass[index] < 50:
        passesCutsMuTau = False
    return passesCutsMuTau


###################
# passes embedded ZTauTau selection


def passesEmbeddedZTauTauSelectionETau(chain,index,UseNewTriggers,Verbose):
    passesCutsETau = True
    if electronID(chain,index,Verbose) is False:
        passesCutsETau = False
    if tauID_eTau(chain, index, Verbose) is False:
        passesCutsETau = False
    if pairCutsETau(chain, index,Verbose) is False:
        passesCutsETau = False
    if embeddedZTauTauTrigForETau(chain, index, Verbose) is False:
        passesCutsETau = False
    if chain.eT_correctedSVFitMass[index] < 50:
        passesCutsETau = False
    return passesCutsETau

def passesEmbeddedZTauTauSelectionMuTau(chain,index,UseNewTriggers,Verbose):
    passesCutsMuTau = True
    if muonID(chain,index,Verbose) is False:
        passesCutsMuTau = False
    if tauID_muTau(chain, index, Verbose) is False:
        passesCutsMuTau = False
    if pairCutsMuTau(chain, index,Verbose) is False:
        passesCutsMuTau = False
    if embeddedZTauTauTrigForMuTau(chain, index, Verbose) is False:
        passesCutsMuTau = False
    if chain.muT_correctedSVFitMass[index] < 50:
        passesCutsMuTau = False
    return passesCutsMuTau



###################
# passes embedded ZTauTau selection _NoMtCut


def passesEmbeddedZTauTauSelectionETau_NoMtCut(chain,index,UseNewTriggers,Verbose):
    passesCutsETau = True
    if electronID(chain,index,Verbose) is False:
        passesCutsETau = False
    if tauID_eTau(chain, index, Verbose) is False:
        passesCutsETau = False
    if pairCutsETau_NoMtCut(chain, index,Verbose) is False:
        passesCutsETau = False
    if embeddedZTauTauTrigForETau(chain, index, Verbose) is False:
        passesCutsETau = False
    if chain.eT_correctedSVFitMass[index] < 50:
        passesCutsETau = False
    return passesCutsETau

def passesEmbeddedZTauTauSelectionMuTau_NoMtCut(chain,index,UseNewTriggers,Verbose):
    passesCutsMuTau = True
    if muonID(chain,index,Verbose) is False:
        passesCutsMuTau = False
    if tauID_muTau(chain, index, Verbose) is False:
        passesCutsMuTau = False
    if pairCutsMuTau_NoMtCut(chain, index,Verbose) is False:
        passesCutsMuTau = False
    if embeddedZTauTauTrigForMuTau(chain, index, Verbose) is False:
        passesCutsMuTau = False
    if chain.muT_correctedSVFitMass[index] < 50:
        passesCutsMuTau = False
    return passesCutsMuTau

###################
# passes embedded TTbar selection


def passesEmbeddedTTbarSelectionETau(chain,index,UseNewTriggers,Verbose):
    passesCutsETau = True
    if electronID(chain,index,Verbose) is False:
        passesCutsETau = False
    if tauID_eTau(chain, index, Verbose) is False:
        passesCutsETau = False
    if pairCutsETau(chain, index,Verbose) is False:
        passesCutsETau = False
    if embeddedTTbarTrigForETau(chain, index, Verbose) is False:
        passesCutsETau = False
    if chain.eT_correctedSVFitMass[index] < 50:
        passesCutsETau = False
    return passesCutsETau

def passesEmbeddedTTbarSelectionMuTau(chain,index,UseNewTriggers,Verbose):
    passesCutsMuTau = True
    if muonID(chain,index,Verbose) is False:
        passesCutsMuTau = False
    if tauID_muTau(chain, index, Verbose) is False:
        passesCutsMuTau = False
    if pairCutsMuTau(chain, index,Verbose) is False:
        passesCutsMuTau = False
    if embeddedTTbarTrigForMuTau(chain, index, Verbose) is False:
        passesCutsMuTau = False
    if chain.muT_correctedSVFitMass[index] < 50:
        passesCutsMuTau = False
    return passesCutsMuTau


###################
# passes embedded TTbar selection _NoMtCut


def passesEmbeddedTTbarSelectionETau_NoMtCut(chain,index,UseNewTriggers,Verbose):
    passesCutsETau = True
    if electronID(chain,index,Verbose) is False:
        passesCutsETau = False
    if tauID_eTau(chain, index, Verbose) is False:
        passesCutsETau = False
    if pairCutsETau_NoMtCut(chain, index,Verbose) is False:
        passesCutsETau = False
    if embeddedTTbarTrigForETau(chain, index, Verbose) is False:
        passesCutsETau = False
    if chain.eT_correctedSVFitMass[index] < 50:
        passesCutsETau = False
    return passesCutsETau

def passesEmbeddedTTbarSelectionMuTau_NoMtCut(chain,index,UseNewTriggers,Verbose):
    passesCutsMuTau = True
    if muonID(chain,index,Verbose) is False:
        passesCutsMuTau = False
    if tauID_muTau(chain, index, Verbose) is False:
        passesCutsMuTau = False
    if pairCutsMuTau_NoMtCut(chain, index,Verbose) is False:
        passesCutsMuTau = False
    if embeddedTTbarTrigForMuTau(chain, index, Verbose) is False:
        passesCutsMuTau = False
    if chain.muT_correctedSVFitMass[index] < 50:
        passesCutsMuTau = False
    return passesCutsMuTau

#################
# default selection but without Mt cut

def passesDefaultSelectionETau_NoMtCut(chain,index,UseNewTriggers,Verbose):
    passesCutsETau = True
    if electronID(chain,index,Verbose) is False:
        passesCutsETau = False
    if tauID_eTau(chain, index, Verbose) is False:
        passesCutsETau = False
    if pairCutsETau_NoMtCut(chain, index,Verbose) is False:
        passesCutsETau = False
    if electronTrigger(chain,index,UseNewTriggers) is False:
        passesCutsETau = False
    if tauTriggerForETau(chain,index,UseNewTriggers) is False:
        passesCutsETau = False
    if chain.eT_correctedSVFitMass[index] < 50:
        passesCutsETau = False
    return passesCutsETau

def passesDefaultSelectionMuTau_NoMtCut(chain,index,UseNewTriggers,Verbose):
    passesCutsMuTau = True
    if muonID(chain,index,Verbose) is False:
        passesCutsMuTau = False
    if tauID_muTau(chain, index, Verbose) is False:
        passesCutsMuTau = False
    if pairCutsMuTau_NoMtCut(chain, index,Verbose) is False:
        passesCutsMuTau = False
    if muonTrigger(chain,index,UseNewTriggers) is False:
        passesCutsMuTau = False
    if tauTriggerForMuTau(chain,index,UseNewTriggers) is False:
        passesCutsMuTau = False
    if chain.muT_correctedSVFitMass[index] < 50:
        passesCutsMuTau = False
    return passesCutsMuTau


#################
# high mT (>70)  selection

def passesHighMtSelectionETau(chain,index,UseNewTriggers,Verbose):
    passesCutsETau = True
    if electronID(chain,index,Verbose) is False:
        passesCutsETau = False
    if tauID_eTau(chain, index, Verbose) is False:
        passesCutsETau = False
    if pairCutsETau_forHighMt(chain, index,Verbose) is False:
        passesCutsETau = False
    if electronTrigger(chain,index,UseNewTriggers) is False:
        passesCutsETau = False
    if tauTriggerForETau(chain,index,UseNewTriggers) is False:
        passesCutsETau = False
    if chain.eT_correctedSVFitMass[index] < 50:
        passesCutsETau = False
    return passesCutsETau

def passesHighMtSelectionMuTau(chain,index,UseNewTriggers,Verbose):
    passesCutsMuTau = True
    if muonID(chain,index,Verbose) is False:
        passesCutsMuTau = False
    if tauID_muTau(chain, index, Verbose) is False:
        passesCutsMuTau = False
    if pairCutsMuTau_forHighMt(chain, index,Verbose) is False:
        passesCutsMuTau = False
    if muonTrigger(chain,index,UseNewTriggers) is False:
        passesCutsMuTau = False
    if tauTriggerForMuTau(chain,index,UseNewTriggers) is False:
        passesCutsMuTau = False
    if chain.muT_correctedSVFitMass[index] < 50:
        passesCutsMuTau = False
    return passesCutsMuTau



#################
# high mT (>70) + Same Sign selection

def passesHighMtSameSignSelectionETau(chain,index,UseNewTriggers,Verbose):
    passesCutsETau = True
    if electronID(chain,index,Verbose) is False:
        passesCutsETau = False
    if tauID_eTau(chain, index, Verbose) is False:
        passesCutsETau = False
    if pairCutsETau_forHighMtSameSign(chain, index,Verbose) is False:
        passesCutsETau = False
    if electronTrigger(chain,index,UseNewTriggers) is False:
        passesCutsETau = False
    if tauTriggerForETau(chain,index,UseNewTriggers) is False:
        passesCutsETau = False
    if chain.eT_correctedSVFitMass[index] < 50:
        passesCutsETau = False
    return passesCutsETau

def passesHighMtSameSignSelectionMuTau(chain,index,UseNewTriggers,Verbose):
    passesCutsMuTau = True
    if muonID(chain,index,Verbose) is False:
        passesCutsMuTau = False
    if tauID_muTau(chain, index, Verbose) is False:
        passesCutsMuTau = False
    if pairCutsMuTau_forHighMtSameSign(chain, index,Verbose) is False:
        passesCutsMuTau = False
    if muonTrigger(chain,index,UseNewTriggers) is False:
        passesCutsMuTau = False
    if tauTriggerForMuTau(chain,index,UseNewTriggers) is False:
        passesCutsMuTau = False
    if chain.muT_correctedSVFitMass[index] < 50:
        passesCutsMuTau = False
    return passesCutsMuTau


##################
# QCD shape selection = anti-iso e/mu, loose iso tau, loose btag, SS

def passesQCDSelectionETau(chain,index,UseNewTriggers,Verbose):
    passesCutsETau = True
    if electronIDforQCD(chain,index,Verbose) is False:
        passesCutsETau = False
    if tauID_eTau_forQCD(chain, index, Verbose) is False:
        passesCutsETau = False
    if pairCutsETau_forQCD(chain, index,Verbose) is False:
        passesCutsETau = False
    if electronTrigger(chain,index,UseNewTriggers) is False:
        passesCutsETau = False
    if tauTriggerForETau(chain,index,UseNewTriggers) is False:
        passesCutsETau = False
    if chain.eT_correctedSVFitMass[index] < 50:
        passesCutsETau = False
    return passesCutsETau

def passesQCDSelectionMuTau(chain,index,UseNewTriggers,Verbose):
    passesCutsMuTau = True
    if muonIDforQCD(chain,index,Verbose) is False:
        passesCutsMuTau = False
    if tauID_muTau_forQCD(chain, index, Verbose) is False:
        passesCutsMuTau = False
    if pairCutsMuTau_forQCD(chain, index,Verbose) is False:
        passesCutsMuTau = False
    if muonTrigger(chain,index,UseNewTriggers) is False:
        passesCutsMuTau = False
    if tauTriggerForMuTau(chain,index,UseNewTriggers) is False:
        passesCutsMuTau = False
    if chain.muT_correctedSVFitMass[index] < 50:
        passesCutsMuTau = False
    return passesCutsMuTau

#############
# SS selection = default except SS

def passesSameSignSelectionETau(chain,index,UseNewTriggers,Verbose):
    passesCutsETau = True
    if electronID(chain,index,Verbose) is False:
        passesCutsETau = False
    if tauID_eTau(chain, index, Verbose) is False:
        passesCutsETau = False
    if pairCutsETau_forQCD(chain, index,Verbose) is False:
        passesCutsETau = False
    if electronTrigger(chain,index,UseNewTriggers) is False:
        passesCutsETau = False
    if tauTriggerForETau(chain,index,UseNewTriggers) is False:
        passesCutsETau = False
    if chain.eT_correctedSVFitMass[index] < 50:
        passesCutsETau = False
    return passesCutsETau

def passesSameSignSelectionMuTau(chain,index,UseNewTriggers,Verbose):
    passesCutsMuTau = True
    if muonID(chain,index,Verbose) is False:
        passesCutsMuTau = False
    if tauID_muTau(chain, index, Verbose) is False:
        passesCutsMuTau = False
    if pairCutsMuTau_forQCD(chain, index,Verbose) is False:
        passesCutsMuTau = False
    if muonTrigger(chain,index,UseNewTriggers) is False:
        passesCutsMuTau = False
    if tauTriggerForMuTau(chain,index,UseNewTriggers) is False:
        passesCutsMuTau = False
    if chain.muT_correctedSVFitMass[index] < 50:
        passesCutsMuTau = False
    return passesCutsMuTau


#################
# default selection with loose or tight Tau Iso (used for btag and nonbtagged W+jets shape)

def passesDefaultSelectionWithLooseOrTightTauIsoETau(chain,index,UseNewTriggers,Verbose):
    passesCutsETau = True
    if electronID(chain,index,Verbose) is False:
        passesCutsETau = False
    if tauID_eTau_looseORtightISO(chain, index, Verbose) is False:
        passesCutsETau = False
    if pairCutsETau(chain, index,Verbose) is False:
        passesCutsETau = False
    if electronTrigger(chain,index,UseNewTriggers) is False:
        passesCutsETau = False
    if tauTriggerForETau(chain,index,UseNewTriggers) is False:
        passesCutsETau = False
    if chain.eT_correctedSVFitMass[index] < 50:
        passesCutsETau = False
    return passesCutsETau

def passesDefaultSelectionWithLooseOrTightTauIsoMuTau(chain,index,UseNewTriggers,Verbose):
    passesCutsMuTau = True
    if muonID(chain,index,Verbose) is False:
        passesCutsMuTau = False
    if tauID_muTau_looseORtightISO(chain, index, Verbose) is False:
        passesCutsMuTau = False
    if pairCutsMuTau(chain, index,Verbose) is False:
        passesCutsMuTau = False
    if muonTrigger(chain,index,UseNewTriggers) is False:
        passesCutsMuTau = False
    if tauTriggerForMuTau(chain,index,UseNewTriggers) is False:
        passesCutsMuTau = False
    if chain.muT_correctedSVFitMass[index] < 50:
        passesCutsMuTau = False
    return passesCutsMuTau

def passesSUSYBBExtraSelectionETau(chain,index):
    if chain.eT_passSignalGeneratorMass70to130Cut[index] is False:
        return False
    else:
        return True
    return False

def passesSUSYBBExtraSelectionMuTau(chain,index):
    if chain.muT_passSignalGeneratorMass70to130Cut[index] is False:
        return False
    else:
        return True
    return False

def passesSUSYGluGluExtraSelectionETau(chain,index):
    if chain.eT_passSignalGeneratorMass70to130Cut[index] is False:
        return False
    else:
        return True
    return False

def passesSUSYGluGluExtraSelectionMuTau(chain,index):
    if chain.muT_passSignalGeneratorMass70to130Cut[index] is False:
        return False
    else:
        return True
    return False
