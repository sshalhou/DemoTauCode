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

##################
# for ggHSusy have all the bbSUSY
# shapes + the higgs pt reweight variants

# sampleTitle.append('ggH80_CMS_htt_higgsPtReweight_8TeVDown')
# sampleTitle.append('ggH80_CMS_htt_higgsPtReweight_8TeVUp')
# sampleTitle.append('ggH80_CMS_htt_higgsPtReweight_scale_8TeVDown')
# sampleTitle.append('ggH80_CMS_htt_higgsPtReweight_scale_8TeVUp')



# for QCD shape evaluation, must fill the following :
# sampleTitle.append('QCD')
# sampleTitle.append('QCD_fine_binning')
# sampleTitle.append('QCD_CMS_htt_QCDfrShape_etau_8TeVDown')
# sampleTitle.append('QCD_CMS_htt_QCDfrShape_etau_8TeVDown_fine_binning')
# sampleTitle.append('QCD_CMS_htt_QCDfrShape_etau_8TeVUp')
# sampleTitle.append('QCD_CMS_htt_QCDfrShape_etau_8TeVUp_fine_binning')
# sampleTitle.append('QCD_CMS_htt_QCDfrShape_mutau_8TeVDown')
# sampleTitle.append('QCD_CMS_htt_QCDfrShape_mutau_8TeVDown_fine_binning')
# sampleTitle.append('QCD_CMS_htt_QCDfrShape_mutau_8TeVUp')
# sampleTitle.append('QCD_CMS_htt_QCDfrShape_mutau_8TeVUp_fine_binning')


######################
# fill all QCD shape variants
# only based on TauEsNominal
def fillQCDShapeVariants(maxPairTypeAndIndex,SAMPLE_ADD,histogram_dict,QCDShapeWeightsDownNominalUp_dict,QCDoSsSWeightsDownNominalUp_dict,Value):
    SUFFIXNominal=''
    SUFFIXchannelUp=''
    SUFFIXchannelDown=''
    if maxPairTypeAndIndex[3]=='TauEsNominal':
        if maxPairTypeAndIndex[1] =='eleTau':
            SUFFIXchannelUp='CMS_htt_QCDfrShape_etau_8TeVUp_'
            SUFFIXchannelDown='CMS_htt_QCDfrShape_etau_8TeVDown_'
        if maxPairTypeAndIndex[1] =='muTau':
            SUFFIXchannelUp='CMS_htt_QCDfrShape_mutau_8TeVUp_'
            SUFFIXchannelDown='CMS_htt_QCDfrShape_mutau_8TeVDown_'
        variantNominal = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXNominal+maxPairTypeAndIndex[2]
        variantUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXchannelUp+maxPairTypeAndIndex[2]
        variantDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXchannelDown+maxPairTypeAndIndex[2]

        INCvariantNominal = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXNominal+'inclusive'
        INCvariantUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXchannelUp+'inclusive'
        INCvariantDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXchannelDown+'inclusive'


        nominalWt = QCDShapeWeightsDownNominalUp_dict['Nominal']*QCDoSsSWeightsDownNominalUp_dict['Nominal']
        downWt = QCDShapeWeightsDownNominalUp_dict['Down']*QCDoSsSWeightsDownNominalUp_dict['Nominal']
        upWt = QCDShapeWeightsDownNominalUp_dict['Up']*QCDoSsSWeightsDownNominalUp_dict['Nominal']

        histogram_dict[INCvariantNominal].Fill(Value,nominalWt)
        histogram_dict[INCvariantUp].Fill(Value,upWt)
        histogram_dict[INCvariantDown].Fill(Value,downWt)
        if maxPairTypeAndIndex[2] != 'Reject':
            histogram_dict[variantNominal].Fill(Value,nominalWt)
            histogram_dict[variantUp].Fill(Value,upWt)
            histogram_dict[variantDown].Fill(Value,downWt)
    return

######################
# fill all QCD OS SS shape variants
# only based on TauEsNominal
def fillQCDOSSSShapeVariants(maxPairTypeAndIndex,SAMPLE_ADD,histogram_dict,QCDShapeWeightsDownNominalUp_dict,QCDoSsSWeightsDownNominalUp_dict,Value):
    SUFFIXNominal=''
    SUFFIXchannelUp=''
    SUFFIXchannelDown=''
    if maxPairTypeAndIndex[3]=='TauEsNominal':
        if maxPairTypeAndIndex[1] =='eleTau':
            SUFFIXchannelUp='CMS_htt_QCDShape_etau_btag_8TeVUp_'
            SUFFIXchannelDown='CMS_htt_QCDShape_etau_btag_8TeVDown_'
        if maxPairTypeAndIndex[1] =='muTau':
            SUFFIXchannelUp='CMS_htt_QCDShape_mutau_btag_8TeVUp_'
            SUFFIXchannelDown='CMS_htt_QCDShape_mutau_btag_8TeVDown_'
        variantNominal = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXNominal+maxPairTypeAndIndex[2]
        variantUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXchannelUp+maxPairTypeAndIndex[2]
        variantDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXchannelDown+maxPairTypeAndIndex[2]

        INCvariantNominal = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXNominal+'inclusive'
        INCvariantUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXchannelUp+'inclusive'
        INCvariantDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXchannelDown+'inclusive'


        nominalWt = QCDoSsSWeightsDownNominalUp_dict['Nominal']*QCDShapeWeightsDownNominalUp_dict['Nominal']
        downWt = QCDoSsSWeightsDownNominalUp_dict['Down']*QCDShapeWeightsDownNominalUp_dict['Nominal']
        upWt = QCDoSsSWeightsDownNominalUp_dict['Up']*QCDShapeWeightsDownNominalUp_dict['Nominal']

        #histogram_dict[INCvariantNominal].Fill(Value,nominalWt)
        histogram_dict[INCvariantUp].Fill(Value,upWt)
        histogram_dict[INCvariantDown].Fill(Value,downWt)
        if maxPairTypeAndIndex[2] != 'Reject':
            #histogram_dict[variantNominal].Fill(Value,nominalWt)
            histogram_dict[variantUp].Fill(Value,upWt)
            histogram_dict[variantDown].Fill(Value,downWt)
    return

##############
# fill the jet->tau fake variants
# these are stored as WShape and are
# split by eTau, muTau, and btag sub-channels
# and also have fine-binned variants

def fillJetTauFakeVariants(maxPairTypeAndIndex,SAMPLE_ADD,wt_dict,histogram_dict,Value):
    SUFFIXUP = ''
    SUFFIXDOWN = ''
    SUFFIXUPsplit = ''
    SUFFIXDOWNsplit = ''
    fineSUFFIXUP = ''
    fineSUFFIXDOWN = ''
    fineSUFFIXUPsplit = ''
    fineSUFFIXDOWNsplit = ''
    BASE = 'CMS_htt_WShape_'
    if maxPairTypeAndIndex[3]!='TauEsNominal':
        return
    elif maxPairTypeAndIndex[1] !='eleTau' and maxPairTypeAndIndex[1] !='muTau':
        return
    elif maxPairTypeAndIndex[1] =='eleTau':
        SUFFIXUP += BASE+'etau_'
        SUFFIXDOWN += BASE+'etau_'
    elif maxPairTypeAndIndex[1] =='muTau':
        SUFFIXUP += BASE+'mutau_'
        SUFFIXDOWN += BASE+'mutau_'

    if 'nobtag' in str(maxPairTypeAndIndex[2]):
        SUFFIXUPsplit = SUFFIXUP
        SUFFIXDOWNsplit = SUFFIXDOWN
        SUFFIXUP+= 'nobtag_8TeVUp_'
        SUFFIXDOWN+= 'nobtag_8TeVDown_'
        SUFFIXUPsplit+=str(maxPairTypeAndIndex[2])+'_8TeVUp_'
        SUFFIXDOWNsplit+=str(maxPairTypeAndIndex[2])+'_8TeVDown_'
    elif 'btag' in str(maxPairTypeAndIndex[2]):
        SUFFIXUPsplit = SUFFIXUP
        SUFFIXDOWNsplit = SUFFIXDOWN
        SUFFIXUP+= 'btag_8TeVUp_'
        SUFFIXDOWN+= 'btag_8TeVDown_'
        SUFFIXUPsplit+=str(maxPairTypeAndIndex[2])+'_8TeVUp_'
        SUFFIXDOWNsplit+=str(maxPairTypeAndIndex[2])+'_8TeVDown_'
    fineSUFFIXUP = SUFFIXUP+'fine_binning_'
    fineSUFFIXDOWN = SUFFIXDOWN+'fine_binning_'
    fineSUFFIXUPsplit = SUFFIXUPsplit+'fine_binning_'
    fineSUFFIXDOWNsplit = SUFFIXDOWNsplit+'fine_binning_'

    #print SUFFIXUP, fineSUFFIXUP, SUFFIXUPsplit, fineSUFFIXUPsplit
    #print SUFFIXDOWN, fineSUFFIXDOWN, SUFFIXDOWNsplit, fineSUFFIXDOWNsplit

    VariantToFillUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXUP+maxPairTypeAndIndex[2]
    VariantToFillUpinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXUP+'inclusive'

    VariantToFillUpsplit = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXUPsplit+maxPairTypeAndIndex[2]
    VariantToFillUpsplitinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXUPsplit+'inclusive'

    VariantToFillDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXDOWN+maxPairTypeAndIndex[2]
    VariantToFillDowninc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXDOWN+'inclusive'

    VariantToFillDownsplit = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXDOWNsplit+maxPairTypeAndIndex[2]
    VariantToFillDownsplitinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXDOWNsplit+'inclusive'

    fineVariantToFillUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXUP+maxPairTypeAndIndex[2]
    fineVariantToFillUpinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXUP+'inclusive'

    fineVariantToFillUpsplit = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXUPsplit+maxPairTypeAndIndex[2]
    fineVariantToFillUpsplitinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXUPsplit+'inclusive'

    fineVariantToFillDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXDOWN+maxPairTypeAndIndex[2]
    fineVariantToFillDowninc = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXDOWN+'inclusive'

    fineVariantToFillDownsplit = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXDOWNsplit+maxPairTypeAndIndex[2]
    fineVariantToFillDownsplitinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXDOWNsplit+'inclusive'

    #print VariantToFillUp, VariantToFillUpinc, VariantToFillDown, VariantToFillDowninc

    #######################################################
    # inclusive versions filled but are not really inclusive since
    # all are split into b-tag or non-btag versions
    # fill the unsplit versions if btagged or non-btagged

    if 'nobtag' in str(maxPairTypeAndIndex[2]) or 'btag' in str(maxPairTypeAndIndex[2]):

        histogram_dict[VariantToFillUpinc].Fill(Value,wt_dict['jetTauFakeUp'])
        histogram_dict[VariantToFillUpsplitinc].Fill(Value,wt_dict['jetTauFakeUp'])
        #histogram_dict[fineVariantToFillUpinc].Fill(Value,wt_dict['jetTauFakeUp'])
        #histogram_dict[fineVariantToFillUpsplitinc].Fill(Value,wt_dict['jetTauFakeUp'])

        histogram_dict[VariantToFillDowninc].Fill(Value,wt_dict['jetTauFakeDown'])
        histogram_dict[VariantToFillDownsplitinc].Fill(Value,wt_dict['jetTauFakeDown'])
        #histogram_dict[fineVariantToFillDowninc].Fill(Value,wt_dict['jetTauFakeDown'])
        #histogram_dict[fineVariantToFillDownsplitinc].Fill(Value,wt_dict['jetTauFakeDown'])

        histogram_dict[VariantToFillUp].Fill(Value,wt_dict['jetTauFakeUp'])
        histogram_dict[VariantToFillUpsplit].Fill(Value,wt_dict['jetTauFakeUp'])
        #histogram_dict[fineVariantToFillUp].Fill(Value,wt_dict['jetTauFakeUp'])
        #histogram_dict[fineVariantToFillUpsplit].Fill(Value,wt_dict['jetTauFakeUp'])

        histogram_dict[VariantToFillDown].Fill(Value,wt_dict['jetTauFakeDown'])
        histogram_dict[VariantToFillDownsplit].Fill(Value,wt_dict['jetTauFakeDown'])
        #histogram_dict[fineVariantToFillDown].Fill(Value,wt_dict['jetTauFakeDown'])
        #histogram_dict[fineVariantToFillDownsplit].Fill(Value,wt_dict['jetTauFakeDown'])


    return




##############
# version which takes a dict to
# decide if should fill inc and/or tagged
# currently used by W+jet shapes


def decide_fillJetTauFakeVariants(FILL_INCorTAG,maxPairTypeAndIndex,SAMPLE_ADD,wt_dict,histogram_dict,Value):
    SUFFIXUP = ''
    SUFFIXDOWN = ''
    SUFFIXUPsplit = ''
    SUFFIXDOWNsplit = ''
    fineSUFFIXUP = ''
    fineSUFFIXDOWN = ''
    fineSUFFIXUPsplit = ''
    fineSUFFIXDOWNsplit = ''
    BASE = 'CMS_htt_WShape_'
    if maxPairTypeAndIndex[3]!='TauEsNominal':
        return
    elif maxPairTypeAndIndex[1] !='eleTau' and maxPairTypeAndIndex[1] !='muTau':
        return
    elif maxPairTypeAndIndex[1] =='eleTau':
        SUFFIXUP += BASE+'etau_'
        SUFFIXDOWN += BASE+'etau_'
    elif maxPairTypeAndIndex[1] =='muTau':
        SUFFIXUP += BASE+'mutau_'
        SUFFIXDOWN += BASE+'mutau_'

    if 'nobtag' in str(maxPairTypeAndIndex[2]):
        SUFFIXUPsplit = SUFFIXUP
        SUFFIXDOWNsplit = SUFFIXDOWN
        SUFFIXUP+= 'nobtag_8TeVUp_'
        SUFFIXDOWN+= 'nobtag_8TeVDown_'
        SUFFIXUPsplit+=str(maxPairTypeAndIndex[2])+'_8TeVUp_'
        SUFFIXDOWNsplit+=str(maxPairTypeAndIndex[2])+'_8TeVDown_'
    elif 'btag' in str(maxPairTypeAndIndex[2]):
        SUFFIXUPsplit = SUFFIXUP
        SUFFIXDOWNsplit = SUFFIXDOWN
        SUFFIXUP+= 'btag_8TeVUp_'
        SUFFIXDOWN+= 'btag_8TeVDown_'
        SUFFIXUPsplit+=str(maxPairTypeAndIndex[2])+'_8TeVUp_'
        SUFFIXDOWNsplit+=str(maxPairTypeAndIndex[2])+'_8TeVDown_'
    fineSUFFIXUP = SUFFIXUP+'fine_binning_'
    fineSUFFIXDOWN = SUFFIXDOWN+'fine_binning_'
    fineSUFFIXUPsplit = SUFFIXUPsplit+'fine_binning_'
    fineSUFFIXDOWNsplit = SUFFIXDOWNsplit+'fine_binning_'

    #print SUFFIXUP, fineSUFFIXUP, SUFFIXUPsplit, fineSUFFIXUPsplit
    #print SUFFIXDOWN, fineSUFFIXDOWN, SUFFIXDOWNsplit, fineSUFFIXDOWNsplit

    VariantToFillUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXUP+maxPairTypeAndIndex[2]
    VariantToFillUpinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXUP+'inclusive'

    VariantToFillUpsplit = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXUPsplit+maxPairTypeAndIndex[2]
    VariantToFillUpsplitinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXUPsplit+'inclusive'

    VariantToFillDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXDOWN+maxPairTypeAndIndex[2]
    VariantToFillDowninc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXDOWN+'inclusive'

    VariantToFillDownsplit = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXDOWNsplit+maxPairTypeAndIndex[2]
    VariantToFillDownsplitinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXDOWNsplit+'inclusive'

    fineVariantToFillUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXUP+maxPairTypeAndIndex[2]
    fineVariantToFillUpinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXUP+'inclusive'

    fineVariantToFillUpsplit = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXUPsplit+maxPairTypeAndIndex[2]
    fineVariantToFillUpsplitinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXUPsplit+'inclusive'

    fineVariantToFillDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXDOWN+maxPairTypeAndIndex[2]
    fineVariantToFillDowninc = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXDOWN+'inclusive'

    fineVariantToFillDownsplit = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXDOWNsplit+maxPairTypeAndIndex[2]
    fineVariantToFillDownsplitinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXDOWNsplit+'inclusive'

    #print VariantToFillUp, VariantToFillUpinc, VariantToFillDown, VariantToFillDowninc

    #######################################################
    # inclusive versions filled but are not really inclusive since
    # all are split into b-tag or non-btag versions
    # fill the unsplit versions if btagged or non-btagged

    if 'nobtag' in str(maxPairTypeAndIndex[2]) or 'btag' in str(maxPairTypeAndIndex[2]):

        if FILL_INCorTAG['inclusive'] is True :
            histogram_dict[VariantToFillUpinc].Fill(Value,wt_dict['jetTauFakeUp'])
            histogram_dict[VariantToFillUpsplitinc].Fill(Value,wt_dict['jetTauFakeUp'])
            #histogram_dict[fineVariantToFillUpinc].Fill(Value,wt_dict['jetTauFakeUp'])
            #histogram_dict[fineVariantToFillUpsplitinc].Fill(Value,wt_dict['jetTauFakeUp'])
            histogram_dict[VariantToFillDowninc].Fill(Value,wt_dict['jetTauFakeDown'])
            histogram_dict[VariantToFillDownsplitinc].Fill(Value,wt_dict['jetTauFakeDown'])
            #histogram_dict[fineVariantToFillDowninc].Fill(Value,wt_dict['jetTauFakeDown'])
            #histogram_dict[fineVariantToFillDownsplitinc].Fill(Value,wt_dict['jetTauFakeDown'])

        if FILL_INCorTAG['Btag-or-noBtag'] is True :
            histogram_dict[VariantToFillUp].Fill(Value,wt_dict['jetTauFakeUp'])
            histogram_dict[VariantToFillUpsplit].Fill(Value,wt_dict['jetTauFakeUp'])
            #histogram_dict[fineVariantToFillUp].Fill(Value,wt_dict['jetTauFakeUp'])
            #histogram_dict[fineVariantToFillUpsplit].Fill(Value,wt_dict['jetTauFakeUp'])
            histogram_dict[VariantToFillDown].Fill(Value,wt_dict['jetTauFakeDown'])
            histogram_dict[VariantToFillDownsplit].Fill(Value,wt_dict['jetTauFakeDown'])
            #histogram_dict[fineVariantToFillDown].Fill(Value,wt_dict['jetTauFakeDown'])
            #histogram_dict[fineVariantToFillDownsplit].Fill(Value,wt_dict['jetTauFakeDown'])


    return




############################
# top pt reweight variants
# for ttMC and ttEmbedded only
# based on TauEsNominal Only

def fillTopPtReweightVariants(maxPairTypeAndIndex,SAMPLE_ADD,wt_dict,histogram_dict,Value):
    SUFFIXUP = ''
    SUFFIXDOWN = ''
    if maxPairTypeAndIndex[3]=='TauEsNominal':
        SUFFIXUP = 'CMS_htt_ttbarPtReweight_8TeVUp_'
        SUFFIXDOWN = 'CMS_htt_ttbarPtReweight_8TeVDown_'
    if len(SUFFIXUP)>0 and len(SUFFIXDOWN)>0:
        VariantToFillUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXUP+maxPairTypeAndIndex[2]
        VariantToFillUpinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXUP+'inclusive'

        VariantToFillDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXDOWN+maxPairTypeAndIndex[2]
        VariantToFillDowninc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXDOWN+'inclusive'

        histogram_dict[VariantToFillUpinc].Fill(Value,wt_dict['topPtUp'])
        histogram_dict[VariantToFillDowninc].Fill(Value,wt_dict['topPtDown'])

        if maxPairTypeAndIndex[2] != 'Reject':
            histogram_dict[VariantToFillUp].Fill(Value,wt_dict['topPtUp'])
            histogram_dict[VariantToFillDown].Fill(Value,wt_dict['topPtDown'])
    return


############################
# top MC jet->tau fake variants

def fillTopJetTauFakeVariants(maxPairTypeAndIndex,SAMPLE_ADD,nominalWt,fakeScale,histogram_dict,Value):
    SUFFIXUP = ''
    SUFFIXDOWN = ''
    if maxPairTypeAndIndex[3]=='TauEsNominal':
        SUFFIXUP = 'CMS_htt_ttbarJetFake_8TeVUp_'
        SUFFIXDOWN = 'CMS_htt_ttbarJetFake_8TeVDown_'
    if len(SUFFIXUP)>0 and len(SUFFIXDOWN)>0:
        upWt = nominalWt
        dnWt = nominalWt
        #print 'jet->tau Fake = ',fakeScale
        if fakeScale > 0.0:
            dnWt = nominalWt/fakeScale
            upWt = nominalWt*fakeScale

        VariantToFillUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXUP+maxPairTypeAndIndex[2]
        VariantToFillUpinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXUP+'inclusive'

        VariantToFillDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXDOWN+maxPairTypeAndIndex[2]
        VariantToFillDowninc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXDOWN+'inclusive'

        histogram_dict[VariantToFillUpinc].Fill(Value,upWt)
        histogram_dict[VariantToFillDowninc].Fill(Value,dnWt)

        if maxPairTypeAndIndex[2] != 'Reject':
            histogram_dict[VariantToFillUp].Fill(Value,upWt)
            histogram_dict[VariantToFillDown].Fill(Value,dnWt)
    return


######################
# higgs pt weight variants
# for ggH sm 125
# based on TES nominal only
# must take the non-higgs pt
# weighted value as finalWt

def fillHiggsPtReweightVariantsSM125(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,higgsPtWeightSYSdict,Value):
    SUFFIXSCALEUP = ''
    SUFFIXSCALEDOWN = ''
    if maxPairTypeAndIndex[3]=='TauEsNominal':
        SUFFIXSCALEUP = 'CMS_htt_higgsPtReweightSM_8TeVUp_'
        SUFFIXSCALEDOWN = 'CMS_htt_higgsPtReweightSM_8TeVDown_'
    if len(SUFFIXSCALEUP)>0 and len(SUFFIXSCALEDOWN)>0:
        tauScaleVariantToFillUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXSCALEUP+maxPairTypeAndIndex[2]
        tauScaleVariantToFillUpinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXSCALEUP+'inclusive'

        tauScaleVariantToFillDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXSCALEDOWN+maxPairTypeAndIndex[2]
        tauScaleVariantToFillDowninc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXSCALEDOWN+'inclusive'

        histogram_dict[tauScaleVariantToFillUpinc].Fill(Value,finalWt*higgsPtWeightSYSdict['Up'])
        histogram_dict[tauScaleVariantToFillDowninc].Fill(Value,finalWt*higgsPtWeightSYSdict['Down'])

        if maxPairTypeAndIndex[2] != 'Reject':
            histogram_dict[tauScaleVariantToFillUp].Fill(Value,finalWt*higgsPtWeightSYSdict['Up'])
            histogram_dict[tauScaleVariantToFillDown].Fill(Value,finalWt*higgsPtWeightSYSdict['Down'])
    return


############################
# higgs pt reweight variants
# for ggHSusy only
# based on TauEsNominal Only

def fillHiggsPtReweightVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,higgsPtWeightSYSdict,Value,nominalPtReweight):
    #################
    # the weight passed to this function
    # should already contain the nominal weight
    # so strip it off

    nominal = nominalPtReweight
    if nominal != 0:
        nonPtreweighted = finalWt/nominal

    SUFFIXTANBUP = ''
    SUFFIXTANBDOWN = ''
    SUFFIXSCALEUP = ''
    SUFFIXSCALEDOWN = ''
    if maxPairTypeAndIndex[3]=='TauEsNominal':
        SUFFIXTANBUP = 'CMS_htt_higgsPtReweight_8TeVUp_'
        SUFFIXTANBDOWN = 'CMS_htt_higgsPtReweight_8TeVDown_'
        SUFFIXSCALEUP = 'CMS_htt_higgsPtReweight_scale_8TeVUp_'
        SUFFIXSCALEDOWN = 'CMS_htt_higgsPtReweight_scale_8TeVDown_'
    if len(SUFFIXTANBUP)>0 and len(SUFFIXTANBDOWN)>0 and len(SUFFIXSCALEUP)>0 and len(SUFFIXSCALEDOWN)>0:
        tauTANbetaVariantToFillUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXTANBUP+maxPairTypeAndIndex[2]
        tauTANbetaVariantToFillUpinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXTANBUP+'inclusive'

        tauTANbetaVariantToFillDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXTANBDOWN+maxPairTypeAndIndex[2]
        tauTANbetaVariantToFillDowninc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXTANBDOWN+'inclusive'

        tauScaleVariantToFillUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXSCALEUP+maxPairTypeAndIndex[2]
        tauScaleVariantToFillUpinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXSCALEUP+'inclusive'

        tauScaleVariantToFillDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXSCALEDOWN+maxPairTypeAndIndex[2]
        tauScaleVariantToFillDowninc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXSCALEDOWN+'inclusive'

        histogram_dict[tauTANbetaVariantToFillUpinc].Fill(Value,nonPtreweighted*higgsPtWeightSYSdict['tanBetaUp'])
        histogram_dict[tauTANbetaVariantToFillDowninc].Fill(Value,nonPtreweighted*higgsPtWeightSYSdict['tanBetaDown'])
        histogram_dict[tauScaleVariantToFillUpinc].Fill(Value,nonPtreweighted*higgsPtWeightSYSdict['scaleUp'])
        histogram_dict[tauScaleVariantToFillDowninc].Fill(Value,nonPtreweighted*higgsPtWeightSYSdict['scaleDown'])

        if maxPairTypeAndIndex[2] != 'Reject':
            histogram_dict[tauTANbetaVariantToFillUp].Fill(Value,nonPtreweighted*higgsPtWeightSYSdict['tanBetaUp'])
            histogram_dict[tauTANbetaVariantToFillDown].Fill(Value,nonPtreweighted*higgsPtWeightSYSdict['tanBetaDown'])
            histogram_dict[tauScaleVariantToFillUp].Fill(Value,nonPtreweighted*higgsPtWeightSYSdict['scaleUp'])
            histogram_dict[tauScaleVariantToFillDown].Fill(Value,nonPtreweighted*higgsPtWeightSYSdict['scaleDown'])
    return


####################################
# treatment for tau ES variants
# also fills nominal shapes
# for samples that *also* use FINE BINNING

def fillNominalSapesAndTauEsVariants_withFineBinToo(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value):
    SUFFIX = ''
    SUFFIXFINE = 'fine_binning_'
    if maxPairTypeAndIndex[1] =='eleTau' and maxPairTypeAndIndex[3]=='TauEsUp' :
        SUFFIX = 'CMS_scale_t_etau_8TeVUp_'
        SUFFIXFINE = 'CMS_scale_t_etau_8TeVUp_fine_binning_'
    if maxPairTypeAndIndex[1] =='muTau' and maxPairTypeAndIndex[3]=='TauEsUp' :
        SUFFIX = 'CMS_scale_t_mutau_8TeVUp_'
        SUFFIXFINE = 'CMS_scale_t_mutau_8TeVUp_fine_binning_'
    if maxPairTypeAndIndex[1] =='eleTau' and maxPairTypeAndIndex[3]=='TauEsDown' :
        SUFFIX = 'CMS_scale_t_etau_8TeVDown_'
        SUFFIXFINE = 'CMS_scale_t_etau_8TeVDown_fine_binning_'
    if maxPairTypeAndIndex[1] =='muTau' and maxPairTypeAndIndex[3]=='TauEsDown' :
        SUFFIX = 'CMS_scale_t_mutau_8TeVDown_'
        SUFFIXFINE = 'CMS_scale_t_mutau_8TeVDown_fine_binning_'
    tauEsVariantToFill = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIX+maxPairTypeAndIndex[2]
    FINEtauEsVariantToFill = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXFINE+maxPairTypeAndIndex[2]
    tauEsVariantToFillinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIX+'inclusive'
    FINEtauEsVariantToFillinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXFINE+'inclusive'
    #print tauEsVariantToFill, tauEsVariantToFillinc, FINEtauEsVariantToFill, FINEtauEsVariantToFillinc
    histogram_dict[tauEsVariantToFillinc].Fill(Value,finalWt)
    histogram_dict[FINEtauEsVariantToFillinc].Fill(Value,finalWt)
    if maxPairTypeAndIndex[2] != 'Reject':
         histogram_dict[tauEsVariantToFill].Fill(Value,finalWt)
         histogram_dict[FINEtauEsVariantToFill].Fill(Value,finalWt)
    return

##############
# version which takes a dict to
# decide if should fill inc and/or tagged
# currently used by W+jet shapes

def decide_fillNominalSapesAndTauEsVariants_withFineBinToo(FILL_INCorTAG,maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value):
    SUFFIX = ''
    SUFFIXFINE = 'fine_binning_'
    if maxPairTypeAndIndex[1] =='eleTau' and maxPairTypeAndIndex[3]=='TauEsUp' :
        SUFFIX = 'CMS_scale_t_etau_8TeVUp_'
        SUFFIXFINE = 'CMS_scale_t_etau_8TeVUp_fine_binning_'
    if maxPairTypeAndIndex[1] =='muTau' and maxPairTypeAndIndex[3]=='TauEsUp' :
        SUFFIX = 'CMS_scale_t_mutau_8TeVUp_'
        SUFFIXFINE = 'CMS_scale_t_mutau_8TeVUp_fine_binning_'
    if maxPairTypeAndIndex[1] =='eleTau' and maxPairTypeAndIndex[3]=='TauEsDown' :
        SUFFIX = 'CMS_scale_t_etau_8TeVDown_'
        SUFFIXFINE = 'CMS_scale_t_etau_8TeVDown_fine_binning_'
    if maxPairTypeAndIndex[1] =='muTau' and maxPairTypeAndIndex[3]=='TauEsDown' :
        SUFFIX = 'CMS_scale_t_mutau_8TeVDown_'
        SUFFIXFINE = 'CMS_scale_t_mutau_8TeVDown_fine_binning_'
    tauEsVariantToFill = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIX+maxPairTypeAndIndex[2]
    FINEtauEsVariantToFill = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXFINE+maxPairTypeAndIndex[2]
    tauEsVariantToFillinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIX+'inclusive'
    FINEtauEsVariantToFillinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXFINE+'inclusive'
    #print tauEsVariantToFill, tauEsVariantToFillinc, FINEtauEsVariantToFill, FINEtauEsVariantToFillinc
    if FILL_INCorTAG['inclusive'] is True:
        histogram_dict[tauEsVariantToFillinc].Fill(Value,finalWt)
        histogram_dict[FINEtauEsVariantToFillinc].Fill(Value,finalWt)
    if maxPairTypeAndIndex[2] != 'Reject':
        if FILL_INCorTAG['Btag-or-noBtag'] is True:
            histogram_dict[tauEsVariantToFill].Fill(Value,finalWt)
            histogram_dict[FINEtauEsVariantToFill].Fill(Value,finalWt)
    return



def decide_fillNominalSapesAndTauEsVariants(FILL_INCorTAG,maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value):
    SUFFIX = ''
    SUFFIXFINE = 'fine_binning_'
    if maxPairTypeAndIndex[1] =='eleTau' and maxPairTypeAndIndex[3]=='TauEsUp' :
        SUFFIX = 'CMS_scale_t_etau_8TeVUp_'
        SUFFIXFINE = 'CMS_scale_t_etau_8TeVUp_fine_binning_'
    if maxPairTypeAndIndex[1] =='muTau' and maxPairTypeAndIndex[3]=='TauEsUp' :
        SUFFIX = 'CMS_scale_t_mutau_8TeVUp_'
        SUFFIXFINE = 'CMS_scale_t_mutau_8TeVUp_fine_binning_'
    if maxPairTypeAndIndex[1] =='eleTau' and maxPairTypeAndIndex[3]=='TauEsDown' :
        SUFFIX = 'CMS_scale_t_etau_8TeVDown_'
        SUFFIXFINE = 'CMS_scale_t_etau_8TeVDown_fine_binning_'
    if maxPairTypeAndIndex[1] =='muTau' and maxPairTypeAndIndex[3]=='TauEsDown' :
        SUFFIX = 'CMS_scale_t_mutau_8TeVDown_'
        SUFFIXFINE = 'CMS_scale_t_mutau_8TeVDown_fine_binning_'
    tauEsVariantToFill = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIX+maxPairTypeAndIndex[2]
    FINEtauEsVariantToFill = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXFINE+maxPairTypeAndIndex[2]
    tauEsVariantToFillinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIX+'inclusive'
    FINEtauEsVariantToFillinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXFINE+'inclusive'
    #print tauEsVariantToFill, tauEsVariantToFillinc, FINEtauEsVariantToFill, FINEtauEsVariantToFillinc
    if FILL_INCorTAG['inclusive'] is True:
        histogram_dict[tauEsVariantToFillinc].Fill(Value,finalWt)
        #histogram_dict[FINEtauEsVariantToFillinc].Fill(Value,finalWt)
    if maxPairTypeAndIndex[2] != 'Reject':
        if FILL_INCorTAG['Btag-or-noBtag'] is True:
            histogram_dict[tauEsVariantToFill].Fill(Value,finalWt)
            #histogram_dict[FINEtauEsVariantToFill].Fill(Value,finalWt)
    return



############################
# fill ZLScale variants
# SVFitmass +/- 2%
#CMS_htt_ZLScale_etau_8TeVDown
#CMS_htt_ZLScale_etau_8TeVUp
#CMS_htt_ZLScale_mutau_8TeVDown
#CMS_htt_ZLScale_mutau_8TeVUp
def fillZLScaleVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value):
    SUFFIXUP=''
    SUFFIXDOWN=''
    if maxPairTypeAndIndex[1] =='eleTau':
        SUFFIXUP = 'CMS_htt_ZLScale_etau_8TeVUp_'
        SUFFIXDOWN = 'CMS_htt_ZLScale_etau_8TeVDown_'
    if maxPairTypeAndIndex[1] =='muTau':
        SUFFIXUP = 'CMS_htt_ZLScale_mutau_8TeVUp_'
        SUFFIXDOWN = 'CMS_htt_ZLScale_mutau_8TeVDown_'
    if len(SUFFIXUP)>0 and len(SUFFIXDOWN)>0:
        upVariantToFill = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXUP+maxPairTypeAndIndex[2]
        upVariantToFillinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXUP+'inclusive'
        downVariantToFill = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXDOWN+maxPairTypeAndIndex[2]
        downVariantToFillinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXDOWN+'inclusive'

        histogram_dict[upVariantToFillinc].Fill(Value*1.02,finalWt)
        histogram_dict[downVariantToFillinc].Fill(Value*0.98,finalWt)

        if maxPairTypeAndIndex[2] != 'Reject':
            histogram_dict[upVariantToFill].Fill(Value*1.02,finalWt)
            histogram_dict[downVariantToFill].Fill(Value*0.98,finalWt)
    return



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
    
    #print maxPairTypeAndIndex
    #print "maxPairTypeAndIndex[1]", maxPairTypeAndIndex[1]
    #print "SAMPLE_ADD", SAMPLE_ADD
    #print "SUFFIX", SUFFIX
    #print "maxPairTypeAndIndex[2]", maxPairTypeAndIndex[2]
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
# for samples that *also* need fine binned variants

def fillJECvariants_withFineBinToo(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value):
    SUFFIXJECUP = ''
    SUFFIXJECDOWN = ''
    fineSUFFIXJECUP = ''
    fineSUFFIXJECDOWN = ''
    if maxPairTypeAndIndex[3]=='TauEsNominal':
        SUFFIXJECUP = 'CMS_scale_jDown_'
        SUFFIXJECDOWN = 'CMS_scale_jUp_'
        fineSUFFIXJECUP = 'CMS_scale_jDown_fine_binning_'
        fineSUFFIXJECDOWN = 'CMS_scale_jUp_fine_binning_'
    if len(SUFFIXJECUP)>0 and len(SUFFIXJECDOWN)>0:
        tauJECVariantToFillUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXJECUP+maxPairTypeAndIndex[5]
        tauJECVariantToFillDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXJECDOWN+maxPairTypeAndIndex[4]
        tauJECVariantToFillUpinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXJECUP+'inclusive'
        tauJECVariantToFillDowninc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXJECDOWN+'inclusive'

        FINEtauJECVariantToFillUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXJECUP+maxPairTypeAndIndex[5]
        FINEtauJECVariantToFillDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXJECDOWN+maxPairTypeAndIndex[4]
        FINEtauJECVariantToFillUpinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXJECUP+'inclusive'
        FINEtauJECVariantToFillDowninc = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXJECDOWN+'inclusive'

        histogram_dict[FINEtauJECVariantToFillUpinc].Fill(Value,finalWt)
        histogram_dict[FINEtauJECVariantToFillDowninc].Fill(Value,finalWt)
        histogram_dict[tauJECVariantToFillUpinc].Fill(Value,finalWt)
        histogram_dict[tauJECVariantToFillDowninc].Fill(Value,finalWt)
        if maxPairTypeAndIndex[5] != 'Reject':
            histogram_dict[tauJECVariantToFillUp].Fill(Value,finalWt)
            histogram_dict[FINEtauJECVariantToFillUp].Fill(Value,finalWt)
        if maxPairTypeAndIndex[4] != 'Reject':
            histogram_dict[tauJECVariantToFillDown].Fill(Value,finalWt)
            histogram_dict[FINEtauJECVariantToFillDown].Fill(Value,finalWt)
    return

##############
# version which takes a dict to
# decide if should fill inc and/or tagged
# currently used by W+jet shapes

def decide_fillJECvariants_withFineBinToo(FILL_INCorTAG,maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value):
    SUFFIXJECUP = ''
    SUFFIXJECDOWN = ''
    fineSUFFIXJECUP = ''
    fineSUFFIXJECDOWN = ''
    if maxPairTypeAndIndex[3]=='TauEsNominal':
        SUFFIXJECUP = 'CMS_scale_jDown_'
        SUFFIXJECDOWN = 'CMS_scale_jUp_'
        fineSUFFIXJECUP = 'CMS_scale_jDown_fine_binning_'
        fineSUFFIXJECDOWN = 'CMS_scale_jUp_fine_binning_'
    if len(SUFFIXJECUP)>0 and len(SUFFIXJECDOWN)>0:
        tauJECVariantToFillUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXJECUP+maxPairTypeAndIndex[5]
        tauJECVariantToFillDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXJECDOWN+maxPairTypeAndIndex[4]
        tauJECVariantToFillUpinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXJECUP+'inclusive'
        tauJECVariantToFillDowninc = maxPairTypeAndIndex[1]+SAMPLE_ADD+SUFFIXJECDOWN+'inclusive'

        FINEtauJECVariantToFillUp = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXJECUP+maxPairTypeAndIndex[5]
        FINEtauJECVariantToFillDown = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXJECDOWN+maxPairTypeAndIndex[4]
        FINEtauJECVariantToFillUpinc = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXJECUP+'inclusive'
        FINEtauJECVariantToFillDowninc = maxPairTypeAndIndex[1]+SAMPLE_ADD+fineSUFFIXJECDOWN+'inclusive'

        if FILL_INCorTAG['inclusive'] is True:
            histogram_dict[FINEtauJECVariantToFillUpinc].Fill(Value,finalWt)
            histogram_dict[FINEtauJECVariantToFillDowninc].Fill(Value,finalWt)
            histogram_dict[tauJECVariantToFillUpinc].Fill(Value,finalWt)
            histogram_dict[tauJECVariantToFillDowninc].Fill(Value,finalWt)
        if maxPairTypeAndIndex[5] != 'Reject':
            if FILL_INCorTAG['Btag-or-noBtag'] is True:
                histogram_dict[tauJECVariantToFillUp].Fill(Value,finalWt)
                histogram_dict[FINEtauJECVariantToFillUp].Fill(Value,finalWt)
        if maxPairTypeAndIndex[4] != 'Reject':
            if FILL_INCorTAG['Btag-or-noBtag'] is True:
                histogram_dict[tauJECVariantToFillDown].Fill(Value,finalWt)
                histogram_dict[FINEtauJECVariantToFillDown].Fill(Value,finalWt)
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
    
def FillNMSSMSignals(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value):
    fillNominalSapesAndTauEsVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    return    
    

def FillSUSYGluGlu(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,highPtTauWtSYS,histogram_dict,higgsPtWeightSYSdict,Value,nominalPtReweight):
    fillNominalSapesAndTauEsVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    fillJECvariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    fillTauEffVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,highPtTauWtSYS,histogram_dict,Value)
    fillHiggsPtReweightVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,higgsPtWeightSYSdict,Value,nominalPtReweight)
    return

def FillObsDATA(maxPairTypeAndIndex,SAMPLE_ADD,histogram_dict,Value):
    fillNominalSapesAndTauEsVariants(maxPairTypeAndIndex,SAMPLE_ADD,1.0,histogram_dict,Value)
    return

def FillQCDShapes(maxPairTypeAndIndex,SAMPLE_ADD,histogram_dict,QCDShapeWeightsDownNominalUp_dict,QCDoSsSWeightsDownNominalUp_dict,Value):
    fillQCDShapeVariants(maxPairTypeAndIndex,SAMPLE_ADD,histogram_dict,QCDShapeWeightsDownNominalUp_dict,QCDoSsSWeightsDownNominalUp_dict,Value)
    fillQCDOSSSShapeVariants(maxPairTypeAndIndex,SAMPLE_ADD,histogram_dict,QCDShapeWeightsDownNominalUp_dict,QCDoSsSWeightsDownNominalUp_dict,Value)
    return

def Fill_DY_ZTTorZLorZJ(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value):
    fillNominalSapesAndTauEsVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    #fillJECvariants_withFineBinToo(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    if SAMPLE_ADD == '_ZL_':
        fillZLScaleVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    return

def Fill_ZTTlowMass(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value):
	fillNominalSapesAndTauEsVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
	return


def Fill_ZTTembedded(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value):
    fillNominalSapesAndTauEsVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    #fillJECvariants_withFineBinToo(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    return

def Fill_VVandSingleTop(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value):
    fillNominalSapesAndTauEsVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    #fillJECvariants_withFineBinToo(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    return

def Fill_TTbarMC(maxPairTypeAndIndex,SAMPLE_ADD,wt_dict,histogram_dict,Value):
    fillNominalSapesAndTauEsVariants(maxPairTypeAndIndex,SAMPLE_ADD,wt_dict['topPtNominal'],histogram_dict,Value)    
    #fillZLScaleVariants(maxPairTypeAndIndex,SAMPLE_ADD,wt_dict['topPtNominal'],histogram_dict,Value)
    fillTopPtReweightVariants(maxPairTypeAndIndex,SAMPLE_ADD,wt_dict,histogram_dict,Value)
    fillTopJetTauFakeVariants(maxPairTypeAndIndex,SAMPLE_ADD,wt_dict['topPtNominal'],wt_dict['jetTauFake'],histogram_dict,Value)
    return


def Fill_WjetsMC(maxPairTypeAndIndex,SAMPLE_ADD,wt_dict,histogram_dict,Value):
    fillNominalSapesAndTauEsVariants(maxPairTypeAndIndex,SAMPLE_ADD,wt_dict['jetTauFakeNominal'],histogram_dict,Value)
    #fillJECvariants_withFineBinToo(maxPairTypeAndIndex,SAMPLE_ADD,wt_dict['jetTauFakeNominal'],histogram_dict,Value)
    fillJetTauFakeVariants(maxPairTypeAndIndex,SAMPLE_ADD,wt_dict,histogram_dict,Value)
    return

def Fill_WjetsMC_forWjetsShape(tauIsoFill,maxPairTypeAndIndex,SAMPLE_ADD,wt_dict,histogram_dict,Value):
    decide_fillNominalSapesAndTauEsVariants(tauIsoFill,maxPairTypeAndIndex,SAMPLE_ADD,wt_dict['jetTauFakeNominal'],histogram_dict,Value)
    #decide_fillJECvariants_withFineBinToo(tauIsoFill,maxPairTypeAndIndex,SAMPLE_ADD,wt_dict['jetTauFakeNominal'],histogram_dict,Value)
    decide_fillJetTauFakeVariants(tauIsoFill,maxPairTypeAndIndex,SAMPLE_ADD,wt_dict,histogram_dict,Value)
    return


def FillSUSYBB(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,highPtTauWtSYS,histogram_dict,Value):
    fillNominalSapesAndTauEsVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    fillJECvariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    fillTauEffVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,highPtTauWtSYS,histogram_dict,Value)
    return

def FILLsm_QQHorVH(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value):
    fillNominalSapesAndTauEsVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    #fillJECvariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    #fillTauEffVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,highPtTauWtSYS,histogram_dict,Value)
    return

def FILLsm_GluGluH125(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value):
    fillNominalSapesAndTauEsVariants(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,Value)
    #fillJECvariants(maxPairTypeAndIndex,SAMPLE_ADD,nominalPtRewighted,histogram_dict,Value)
    #fillTauEffVariants(maxPairTypeAndIndex,SAMPLE_ADD,nominalPtRewighted,highPtTauWtSYS,histogram_dict,Value)
    # make sure we pass the non-pt reweighted value here
    #fillHiggsPtReweightVariantsSM125(maxPairTypeAndIndex,SAMPLE_ADD,finalWt,histogram_dict,higgsPtWeightSYSdict,Value)
    return
