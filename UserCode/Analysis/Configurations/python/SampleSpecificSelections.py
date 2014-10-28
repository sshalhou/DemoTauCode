import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile

from Configurations.python.electronID import *
from Configurations.python.muonID import *
from Configurations.python.tauID import *
from Configurations.python.triggerRequirements import *
from Configurations.python.eventRequirements import *


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
