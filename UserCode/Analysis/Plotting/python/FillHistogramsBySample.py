import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TDirectoryFile
from array import array


##################
# for bbSUSY have :
# bbH80 ---> nominal template
# bbH80_CMS_scale_t_etau_8TeVDown  ----> TAU ES DOWN for Etau
# bbH80_CMS_scale_t_etau_8TeVUp  ----> TAU ES UP for Etau
# bbH80_CMS_scale_t_mutau_8TeVDown  ---->TAU ES DOWN for Mutau
# bbH80_CMS_scale_t_mutau_8TeVUp  ---->TAU ES UP for Mutau


# bbH80_CMS_eff_t_mssmHigh_etau_8TeVDown ---> high pt tau eff 1- (0.20*tauPt/1000.0)
# bbH80_CMS_eff_t_mssmHigh_etau_8TeVUp ----> same but up 1+ (0.20*tauPt/1000.0)
# bbH80_CMS_eff_t_mssmHigh_mutau_8TeVDown   ----> same but for muTau
# bbH80_CMS_eff_t_mssmHigh_mutau_8TeVUp  ----> same but for muTau



# bbH80_CMS_scale_jDown ---> JEC down
# bbH80_CMS_scale_jUp ----> JEC UP


####################################
# treatment for tau ES variants
# also fills nominal shapes

def fillNominalSapesAndTauEsVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value):
    SUFFIX = ''
    if maxPairTypeAndIndex[1] =='eleTau' and maxPairTypeAndIndex[3]=='TauEsUp' :
        SUFFIX = 'CMS_scale_t_etau_8TeVUp_'
    if maxPairTypeAndIndex[1] =='muTau' and maxPairTypeAndIndex[3]=='TauEsUp' :
        SUFFIX = 'CMS_scale_t_mutau_8TeVUp_'
    if maxPairTypeAndIndex[1] =='eleTau' and maxPairTypeAndIndex[3]=='TauEsDown' :
        SUFFIX = 'CMS_scale_t_etau_8TeVDown_'
    if maxPairTypeAndIndex[1] =='muTau' and maxPairTypeAndIndex[3]=='TauEsDown' :
        SUFFIX = 'CMS_scale_t_mutau_8TeVDown_'
    tauEsVariantToFill = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIX+maxPairTypeAndIndex[2]
    tauEsVariantToFillinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIX+'inclusive'
    #print tauEsVariantToFill, tauEsVariantToFillinc
    histogram_dict[tauEsVariantToFillinc].Fill(Value,finalWt)
    if maxPairTypeAndIndex[2] != 'Reject':
         histogram_dict[tauEsVariantToFill].Fill(Value,finalWt)
    return


###################################
# treatement for Tau high Pt Efficiecny variants
# note these are weight variants off of nominal tau ES

def fillTauEffVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,highPtTauWtSYS,histogram_dict,Value):
    SUFFIXUP = ''
    SUFFIXDOWN = ''
    if maxPairTypeAndIndex[3]=='TauEsNominal':
        if maxPairTypeAndIndex[1] =='eleTau':
            SUFFIXUP = 'CMS_eff_t_mssmHigh_etau_8TeVUp_'
            SUFFIXDOWN = 'CMS_eff_t_mssmHigh_etau_8TeVDown_'
        if maxPairTypeAndIndex[1] =='muTau':
            SUFFIXUP = 'CMS_eff_t_mssmHigh_mutau_8TeVUp_'
            SUFFIXDOWN = 'CMS_eff_t_mssmHigh_mutau_8TeVDown_'
    if len(SUFFIXUP)>0 and len(SUFFIXDOWN)>0:
        tauEffVariantToFillUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXUP+maxPairTypeAndIndex[2]
        tauEffVariantToFillDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXDOWN+maxPairTypeAndIndex[2]
        tauEffVariantToFillUpinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXUP+'inclusive'
        tauEffVariantToFillDowninc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXDOWN+'inclusive'
        finalWtUp =  finalWt*(1.0+highPtTauWtSYS)
        finalWtDown =  finalWt*(1.0-highPtTauWtSYS)
        if(finalWtDown<0):
            finalWtDown = 0.0
        #print tauEffVariantToFillUp, tauEffVariantToFillDown, tauEffVariantToFillUpinc, tauEffVariantToFillDowninc
        histogram_dict[tauEffVariantToFillUpinc].Fill(Value,finalWtUp)
        histogram_dict[tauEffVariantToFillDowninc].Fill(Value,finalWtDown)
        if maxPairTypeAndIndex[2] != 'Reject':
            histogram_dict[tauEffVariantToFillUp].Fill(Value,finalWtUp)
            histogram_dict[tauEffVariantToFillDown].Fill(Value,finalWtDown)
    return


#####################################
# Fill JEC histogram variants       #
# based off of TauEsNominal tree
# note here event only categorization changes due to migration
def fillJECvariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value):
    SUFFIXJECUP = ''
    SUFFIXJECDOWN = ''
    if maxPairTypeAndIndex[3]=='TauEsNominal':
        SUFFIXJECUP = 'CMS_scale_jDown_'
        SUFFIXJECDOWN = 'CMS_scale_jUp_'
    if len(SUFFIXJECUP)>0 and len(SUFFIXJECDOWN)>0:
        tauJECVariantToFillUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXJECUP+maxPairTypeAndIndex[5]
        tauJECVariantToFillDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXJECDOWN+maxPairTypeAndIndex[4]
        tauJECVariantToFillUpinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXJECUP+'inclusive'
        tauJECVariantToFillDowninc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXJECDOWN+'inclusive'
        histogram_dict[tauJECVariantToFillUpinc].Fill(Value,finalWt)
        histogram_dict[tauJECVariantToFillDowninc].Fill(Value,finalWt)
        if maxPairTypeAndIndex[5] != 'Reject':
            histogram_dict[tauJECVariantToFillUp].Fill(Value,finalWt)
        if maxPairTypeAndIndex[4] != 'Reject':
            histogram_dict[tauJECVariantToFillDown].Fill(Value,finalWt)
    return



def FillSUSYBB(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,highPtTauWtSYS,histogram_dict,Value):
    fillNominalSapesAndTauEsVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    fillJECvariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    fillTauEffVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,highPtTauWtSYS,histogram_dict,Value)
    return
