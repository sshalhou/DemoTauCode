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


########################
# return the cross section
# for each of the 3 ttbar MC samples
# the values stored in the trees themselves
# are no longer correct

def getTTmcCrossSection(chain):
    XSttBar = 241.5
    SFttBar = 1.033
    crossReturn = 1.0
    sampleName = chain.SampleName
    if(sampleName=='/TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v2/AODSIM'):
        crossReturn = XSttBar * SFttBar * 0.1050 
    elif(sampleName=='/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM'):
        crossReturn = XSttBar * SFttBar * 0.4380
    elif(sampleName=='/TTJets_HadronicMGDecays_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A_ext-v1/AODSIM'):
        crossReturn = XSttBar * SFttBar * 0.4570
    return crossReturn     

########################
# cross-section weights for W+jets
# need to be treated special-like because
# we combine multiple datasets of the same process

def getWPlusJetsCrossSectionWeight(chain):
    numEvents = 1.0
    sampleName = chain.SampleName
    WJetsSampleA = '/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM'
    WJetsSampleB = '/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'

    W1JetsSampleA = '/W1JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'
    W1JetsSampleB = '/W1JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'

    W2JetsSampleA = '/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'
    W2JetsSampleB = '/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'

    W3JetsSampleA = '/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'
    W3JetsSampleB = '/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'

    W4JetsSample  = '/W4JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'


    if sampleName==WJetsSampleA or sampleName==WJetsSampleB:
        numEvents = (57709905)*CrabJobEfficiency(WJetsSampleA)+(18393090)*CrabJobEfficiency(WJetsSampleB)
    elif sampleName==W1JetsSampleA or sampleName==W1JetsSampleB:
        numEvents = (23141598)*CrabJobEfficiency(W1JetsSampleA)+(29784800)*CrabJobEfficiency(W1JetsSampleB)
    elif sampleName==W2JetsSampleA or sampleName==W2JetsSampleB:
        numEvents = (34044921)*CrabJobEfficiency(W2JetsSampleA)+(30693853)*CrabJobEfficiency(W2JetsSampleB)
    elif sampleName==W3JetsSampleA or sampleName==W3JetsSampleB:
        numEvents = (15539503)*CrabJobEfficiency(W3JetsSampleA)+(15241144)*CrabJobEfficiency(W3JetsSampleB)
    elif sampleName==W4JetsSample:
        numEvents = (13382803)*CrabJobEfficiency(W4JetsSample)

    #print 'single sample nevents = ',  chain.numberEvents, 'combined = ',  numEvents
    weight = 1000.0*19.7*chain.crossSection/(numEvents)
    return weight

###################
# additonal W+jets shape weight

def WjetsShapeAdditionalCorrection(chain, maxPairTypeAndIndex):
    value = 0.0

    # for tau_h with |eta| < 1.2
    WWeight_mutau_central = TF1("WWeight_mutau_central","(-1.41E-03)*x+(1.06E+00)",30.,2000.)
    # for tau_h with |eta| between 1.2 and 1.7
    WWeight_mutau_medium =  TF1("WWeight_mutau_medium","(-6.36E-03)*x+(1.26E+00)",30.,2000.)
    # for tau_h with |eta| > 1.7
    WWeight_mutau_forward = TF1("WWeight_mutau_forward","(-8.61E-03)*x+(1.34E+00)",30.,2000.)

    #################
    # get tau pt and eta
    i = maxPairTypeAndIndex[0]
    TAUPT = 0.0
    ABSETA = 0.0
    if maxPairTypeAndIndex[1] == 'eleTau':
        Tvec = TLorentzVector(0,0,0,0)
        Tvec.SetXYZT(chain.eT_tau_corrected_p4_x[i], chain.eT_tau_corrected_p4_y[i], chain.eT_tau_corrected_p4_z[i],chain.eT_tau_corrected_p4_t[i])
        TAUPT = Tvec.Pt()
        ABSETA = abs(Tvec.Eta())
    elif maxPairTypeAndIndex[1] == 'muTau':
        Tvec = TLorentzVector(0,0,0,0)
        Tvec.SetXYZT(chain.muT_tau_corrected_p4_x[i], chain.muT_tau_corrected_p4_y[i], chain.muT_tau_corrected_p4_z[i],chain.muT_tau_corrected_p4_t[i])
        TAUPT = Tvec.Pt()
        ABSETA = abs(Tvec.Eta())

    if(ABSETA < 1.2) :
        value = WWeight_mutau_central(TAUPT)
    elif(ABSETA > 1.7) :
        value = WWeight_mutau_forward(TAUPT)
    else:
        value = WWeight_mutau_medium(TAUPT)

    if value < 0:
        return 0.0
    else:
        return value;



####################
# QCD jet->tau weights
# and systematic variations
# down = 1.0
# nominal = apply weight
# up = apply weight*weight
# xT_etaDepQCDShapeTemplateCorrection

def QCDoSsSWeights(chain, maxPairTypeAndIndex):
	retVal = 1.0
	MASS = 0

	BTAGOSSS =  TF1("BTAGOSSS","1.1+1.418*exp(-0.11*x)",20.,2000.)
	INCLUSIVEOSSS = TF1("INCLUSIVEOSSS","1.13+1.0*exp(-0.087*x)",20.,2000.)


	i = maxPairTypeAndIndex[0]
	if maxPairTypeAndIndex[1] == 'eleTau':
		MASS = chain.eT_correctedSVFitMass[i]
	elif maxPairTypeAndIndex[1] == 'muTau':
		MASS = chain.muT_correctedSVFitMass[i]	

	if 'Reject' in str(maxPairTypeAndIndex[2]):
		retVal = INCLUSIVEOSSS(MASS)
	elif 'btag' in str(maxPairTypeAndIndex[2]):
		retVal = BTAGOSSS(MASS)
	return retVal

def UpdatedQCDEtaDepWeights(chain, maxPairTypeAndIndex):
    value = 0.0
    ####################
    # new functions that correctly account for loose-tight
    # extrapolation (same function for ETau and MuTau)

    # for tau_h with |eta| < 1.2
    QCDWeight_mutau_central = TF1("QCDWeight_mutau_central","0.936+0.002487385*x",20.,2000.)
    # for tau_h with |eta| between 1.2 and 1.7
    QCDWeight_mutau_medium =  TF1("QCDWeight_mutau_medium","1.116-0.00451078*x",20.,2000.)
    # for tau_h with |eta| > 1.7
    QCDWeight_mutau_forward = TF1("QCDWeight_mutau_forward","1.387-0.015387226*x",20.,2000.)

    #################
    # get tau pt and eta
    i = maxPairTypeAndIndex[0]
    TAUPT = 0.0
    ABSETA = 0.0
    if maxPairTypeAndIndex[1] == 'eleTau':
        Tvec = TLorentzVector(0,0,0,0)
        Tvec.SetXYZT(chain.eT_tau_corrected_p4_x[i], chain.eT_tau_corrected_p4_y[i], chain.eT_tau_corrected_p4_z[i],chain.eT_tau_corrected_p4_t[i])
        TAUPT = Tvec.Pt()
        ABSETA = abs(Tvec.Eta())
    elif maxPairTypeAndIndex[1] == 'muTau':
        Tvec = TLorentzVector(0,0,0,0)
        Tvec.SetXYZT(chain.muT_tau_corrected_p4_x[i], chain.muT_tau_corrected_p4_y[i], chain.muT_tau_corrected_p4_z[i],chain.muT_tau_corrected_p4_t[i])
        TAUPT = Tvec.Pt()
        ABSETA = abs(Tvec.Eta())
    #print 'tau pt and abseta = ', TAUPT,    ABSETA

    if(ABSETA < 1.2) :
        value = QCDWeight_mutau_central(TAUPT)
    elif(ABSETA > 1.7) :
        value = QCDWeight_mutau_forward(TAUPT)
    else:
        value = QCDWeight_mutau_medium(TAUPT)

    if value < 0:
        return 0.0
    else:
        return value;



def QCDShapeWeights(chain, maxPairTypeAndIndex, QCDShapeWeightsDownNominalUp_dict):
    value = UpdatedQCDEtaDepWeights(chain, maxPairTypeAndIndex)
    #print 'new QCD shape weight is :', value
    QCDShapeWeightsDownNominalUp_dict['Down'] = 1.0
    QCDShapeWeightsDownNominalUp_dict['Nominal'] = value
    QCDShapeWeightsDownNominalUp_dict['Up'] = value*value
    return
    


################################
# get the e->tau fake weight correction

def getFakeZeeWeight(chain,maxPairTypeAndIndex):
    returnWeight = 1.0
    i = maxPairTypeAndIndex[0]
    if maxPairTypeAndIndex[1] == 'eleTau':
      returnWeight = chain.eT_ZeeScaleFactor[i]
    return returnWeight


####################################
# get embedding weights

def getEmbedWeight(chain,maxPairTypeAndIndex):
    returnWeight = 1.0
    i = maxPairTypeAndIndex[0]
    if maxPairTypeAndIndex[1] == 'eleTau':
      returnWeight = chain.eT_embedWeight[i]
    elif maxPairTypeAndIndex[1] == 'muTau':
      returnWeight = chain.muT_embedWeight[i]
    return returnWeight

####################################
# get nominal jet->tau fake weights

def getjetTauFakeWt(chain,maxPairTypeAndIndex):
    returnWeight = 1.0
    i = maxPairTypeAndIndex[0]
    if maxPairTypeAndIndex[1] == 'eleTau':
      returnWeight = chain.eT_TauFakeCorrection[i]
    elif maxPairTypeAndIndex[1] == 'muTau':
      returnWeight = chain.muT_TauFakeCorrection[i]
    return returnWeight

###############
# get nominal top pt weights

def getTopPtWeight(chain,maxPairTypeAndIndex):
    returnWeight = 1.0
    i = maxPairTypeAndIndex[0]
    if maxPairTypeAndIndex[1] == 'eleTau':
      returnWeight = chain.eT_TTbarPtWeight[i]
    elif maxPairTypeAndIndex[1] == 'muTau':
      returnWeight = chain.muT_TTbarPtWeight[i]
    return returnWeight


##############
# stitching W+jets weight

def getStitchingWjetsWt(chain, maxPairTypeAndIndex):
    returnWeight = 1.0
    i = maxPairTypeAndIndex[0]
    nup = 999
    njet = 999
    #########################
    # need to take care of 2 issues :
    # (1) v19 w+jets MC has no nup info, need to get
    #     njets from file names
    # (2) for all other w+jets MC the weights are slightly
    #     wrong, and so need to replace with updated values
    #     below

    if 'V19' not in str(chain.SampleName) :
        #print 'V19 is not in name'
        if maxPairTypeAndIndex[1] == 'eleTau':
            nup = chain.eT_hepNUP[i]
        elif maxPairTypeAndIndex[1] == 'muTau':
            nup = chain.muT_hepNUP[i]
        if(nup==999): return 1.0
        njet = nup - 5
        #print 'set njet = ', njet


    elif 'V19' in str(chain.SampleName) :
        #print 'V19 is in name'
        if   'W1Jets' in str(chain.SampleName) : njet = 1
        elif 'W2Jets' in str(chain.SampleName) : njet = 2
        elif 'W3Jets' in str(chain.SampleName) : njet = 3
        elif 'W4Jets' in str(chain.SampleName) : njet = 4
        #print 'set njet = ', njet

    if   njet==0: returnWeight =  0.0004822832531
    elif njet==1: returnWeight =  0.00009812141584
    elif njet==2: returnWeight =  0.00003056796532
    elif njet==3: returnWeight =  0.00001953280552
    elif njet>=4: returnWeight =  0.00001856311314

    return returnWeight*19.7*1000

##############
# stitching Z+jets weight

def getStitchingZjetsWt(chain, maxPairTypeAndIndex):

    # stitching weights in FlatTuple are slightly wrong
    # re-derive them from the FlatTuple's nup-5 instead

    returnWeight = 1.0
    i = maxPairTypeAndIndex[0]
    nup = 999
    if maxPairTypeAndIndex[1] == 'eleTau':
        nup = chain.eT_hepNUP[i]
    elif maxPairTypeAndIndex[1] == 'muTau':
        nup = chain.muT_hepNUP[i]
    if(nup==999): return 1.0

    njet = nup-5

    if   njet==0: returnWeight = 0.0001159539602
    elif njet==1: returnWeight = 0.00002251042347
    elif njet==2: returnWeight = 0.000009135481997
    elif njet==3: returnWeight = 0.000005300125109
    elif njet>=4: returnWeight = 0.000004146923304

    return returnWeight*19.7*1000.0    



def getStitchingLowMassDY(chain, maxPairTypeAndIndex):
    returnWeight = 1.0
    i = maxPairTypeAndIndex[0]
    nup = 999
    if maxPairTypeAndIndex[1] == 'eleTau':
        nup = chain.eT_hepNUP[i]
    elif maxPairTypeAndIndex[1] == 'muTau':
        nup = chain.muT_hepNUP[i]
    if(nup==999): return 1.0

    njet = nup-5

    if   njet==0: returnWeight = 0.0003884338095
    elif njet==1: returnWeight = 0.00009075714979
    elif njet==2: returnWeight = 0.00001297251708 
    elif njet==3: returnWeight = 0.0003884338095 # no exc. samples exist
    elif njet>=4: returnWeight = 0.0003884338095 # no exc. samples exist
    return returnWeight*19.7*1000.0




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
# high pt tau ID systematic

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
     return returnWeight
  else:
    returnWeight = (0.20*tauPt/1000.0)
  #print tauPt,   returnWeight
  return returnWeight

##################
# higgsPt weight systematic
# for ggH susy samples only

def higgsPtWeightSYS(chain, maxPairTypeAndIndex,higgsPtWeightSYSdict):
  i = maxPairTypeAndIndex[0]
  if maxPairTypeAndIndex[1] == 'eleTau':
    higgsPtWeightSYSdict['tanBetaUp'] = chain.eT_upPOWHEGmhmod[i]
    higgsPtWeightSYSdict['tanBetaDown'] = chain.eT_downPOWHEGmhmod[i]
    higgsPtWeightSYSdict['scaleUp'] = chain.eT_upPOWHEGscale[i]
    higgsPtWeightSYSdict['scaleDown'] = chain.eT_downPOWHEGscale[i]
  elif maxPairTypeAndIndex[1] == 'muTau':
    higgsPtWeightSYSdict['tanBetaUp'] = chain.muT_upPOWHEGmhmod[i]
    higgsPtWeightSYSdict['tanBetaDown'] = chain.muT_downPOWHEGmhmod[i]
    higgsPtWeightSYSdict['scaleUp'] = chain.muT_upPOWHEGscale[i]
    higgsPtWeightSYSdict['scaleDown'] = chain.muT_downPOWHEGscale[i]
  return


##############
# higgs pt weight for SM125 GluGlu

def SM125higgsPtWeightSYS(chain, maxPairTypeAndIndex,higgsPtWeightSYSdict):
    higgsPtWeightSYSdict['Up'] = 1.0
    higgsPtWeightSYSdict['Down'] = 1.0
    higgsPtWeightSYSdict['Nominal'] = 1.0
    i = maxPairTypeAndIndex[0]
    genBosonPt = 125.0
    Tvec = TLorentzVector(0,0,0,0)
    if maxPairTypeAndIndex[1] == 'eleTau':
        Tvec.SetXYZT(chain.eT_genBosonP4_x[i], chain.eT_genBosonP4_y[i], chain.eT_genBosonP4_z[i],chain.eT_genBosonP4_t[i])
        genBosonPt = Tvec.Pt()

    elif maxPairTypeAndIndex[1] == 'muTau':
        Tvec.SetXYZT(chain.muT_genBosonP4_x[i], chain.muT_genBosonP4_y[i], chain.muT_genBosonP4_z[i],chain.muT_genBosonP4_t[i])
        genBosonPt = Tvec.Pt()

    if genBosonPt > 0.0 and math.isnan(genBosonPt) is False:
        histFile = TFile("SMGluGluHiggsPtRewight/HRes_weight_pTH_mH125_8TeV.root","READ")

        NominalHist = TH1F(histFile.Get("Nominal"))
        TheBinNominal = NominalHist.GetXaxis().FindBin(genBosonPt)

        UpHist = TH1F(histFile.Get("Up"))
        TheBinUp = UpHist.GetXaxis().FindBin(genBosonPt)

        DownHist = TH1F(histFile.Get("Down"))
        TheBinDown = DownHist.GetXaxis().FindBin(genBosonPt)

        higgsPtWeightSYSdict['Up'] = UpHist.GetBinContent(TheBinUp)
        higgsPtWeightSYSdict['Down'] = DownHist.GetBinContent(TheBinDown)
        higgsPtWeightSYSdict['Nominal'] = NominalHist.GetBinContent(TheBinNominal)
    return


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

##################################
# trigger weights for 'embedded samples'
# just return the data weights to emulate the
# usual triggers

def embeddedTriggerEmulationWeight(chain, maxPairTypeAndIndex):
  returnWeight = 1.0
  i = maxPairTypeAndIndex[0]
  if maxPairTypeAndIndex[1] == 'eleTau':
    returnWeight *= chain.eT_EffDataELE20andELE22[i]
    returnWeight *= chain.eT_HadronicTauDataTrigEffAntiEMed[i]
  elif maxPairTypeAndIndex[1] == 'muTau':
    returnWeight *= chain.muT_EffDataISOMU17andISOMU18[i]
    returnWeight *= chain.muT_HadronicTauDataTrigEffAntiMuMed[i]
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
    adjustedDataWt = chain.eT_EffDataHighPtTauTrigger[i]
    # fix computation for data
    if adjustedDataWt != 1.0:
        adjustedDataWt = ((chain.eT_EffDataHighPtTauTrigger[i]-0.3)/0.7)
        adjustedDataWt = (1-0.6245691177080073)+adjustedDataWt*(0.6245691177080073)
        #print "original, new ", chain.eT_EffDataHighPtTauTrigger[i], adjustedDataWt
    returnWeight *= divisionHelp(adjustedDataWt, chain.eT_EffMcHighPtTauTrigger[i])
  elif maxPairTypeAndIndex[1] == 'muTau':
    adjustedDataWt = chain.muT_EffDataHighPtTauTrigger[i]
    # fix computation for data
    if adjustedDataWt != 1.0:
       adjustedDataWt = ((chain.muT_EffDataHighPtTauTrigger[i]-0.3)/0.7)
       adjustedDataWt = (1-0.6245691177080073)+adjustedDataWt*(0.6245691177080073)
       #print "original, new ", chain.muT_EffDataHighPtTauTrigger[i], adjustedDataWt
    returnWeight *= divisionHelp(adjustedDataWt, chain.muT_EffMcHighPtTauTrigger[i])
  return returnWeight

def highPtTauTriggerBugWeights_forEMBEDDED(chain, maxPairTypeAndIndex):
  returnWeight = 1.0
  i = maxPairTypeAndIndex[0]
  if maxPairTypeAndIndex[1] == 'eleTau':
    adjustedDataWt = chain.eT_EffDataHighPtTauTrigger[i]
    # fix computation for data
    if adjustedDataWt != 1.0:
        adjustedDataWt = ((chain.eT_EffDataHighPtTauTrigger[i]-0.3)/0.7)
        adjustedDataWt = (1-0.6245691177080073)+adjustedDataWt*(0.6245691177080073)
        #print "original, new ", chain.eT_EffDataHighPtTauTrigger[i], adjustedDataWt
    returnWeight *= adjustedDataWt
  elif maxPairTypeAndIndex[1] == 'muTau':
    adjustedDataWt = chain.muT_EffDataHighPtTauTrigger[i]
    # fix computation for data
    if adjustedDataWt != 1.0:
       adjustedDataWt = ((chain.muT_EffDataHighPtTauTrigger[i]-0.3)/0.7)
       adjustedDataWt = (1-0.6245691177080073)+adjustedDataWt*(0.6245691177080073)
       #print "original, new ", chain.muT_EffDataHighPtTauTrigger[i], adjustedDataWt
    returnWeight *= adjustedDataWt
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


def CrabJobEfficiency(sampleName):
    eff = 1.0    
    return eff

#############
# for nMSSM signals at low mass

def genFilterEff(sampleName):
	eff = 1.0
	if(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m25_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
		eff = 0.02170
	elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m30_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
		eff = 0.03182
	elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m35_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
		eff = 0.04325
	elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m40_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
		eff = 0.05953
	elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m45_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
		eff = 0.07875
	elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m50_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
		eff = 0.1008
	elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m55_FilterMuOrEle15_8TeV/Summer12DR53X-PU_S10_START53_V19-v2/AODSIM'):
		eff = 0.11808
	elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m60_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
		eff = 0.143
	elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m65_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
		eff = 0.16048
	elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m70_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
		eff = 0.18227
	elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m75_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
		eff = 0.20248
	elif(sampleName=='/PYTHIA6_Tauola_nMSSM_bba1_tautau_m80_FilterMuOrEle15_8TeV/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'):
		eff = 0.21765
	return eff

def signalSUSYweightGluGlu(chain, maxPairTypeAndIndex, Verbose):
  returnWeight = 1.0
  allWeights = {}
  allWeights['PU'] = PUweight(chain, maxPairTypeAndIndex)
  allWeights['regularTrigger'] = mcTriggerWeight(chain, maxPairTypeAndIndex)
  allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
  allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
  allWeights['TriggerBug'] =  highPtTauTriggerBugWeights(chain, maxPairTypeAndIndex)
  # because the next line is here, when taking higgs pt up and down need to divide by the
  # nominal scale factor 1st
  allWeights['higgsPtNEW'] = higgsPtReWeight(chain, maxPairTypeAndIndex, 'USENEW', 'NOMINAL')
  allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
  allWeights['nevents'] = 1000.0*19.7/(chain.numberEvents*CrabJobEfficiency(chain.SampleName))
  #allWeights['tauPolarization'] = tauPolarizationWeight(chain, maxPairTypeAndIndex)
  # this is a SYS allWeights['highPtTauEff'] = highPtTauSF(chain, maxPairTypeAndIndex)
  for key, value in allWeights.iteritems():
    returnWeight*=value
  if Verbose:
    print allWeights
  return returnWeight


def nMSSMweights(chain, maxPairTypeAndIndex, Verbose):
	returnWeight = 1.0
	allWeights = {}
	allWeights['PU'] = PUweight(chain, maxPairTypeAndIndex)
	allWeights['regularTrigger'] = mcTriggerWeight(chain, maxPairTypeAndIndex)
	allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
	allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
	allWeights['TriggerBug'] =  highPtTauTriggerBugWeights(chain, maxPairTypeAndIndex)
	allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
	allWeights['nevents'] = genFilterEff(chain.SampleName)*1000.0*19.7/(chain.numberEvents*CrabJobEfficiency(chain.SampleName))
	#allWeights['tauPolarization'] = tauPolarizationWeight(chain, maxPairTypeAndIndex)
	# this is a SYS allWeights['highPtTauEff'] = highPtTauSF(chain, maxPairTypeAndIndex)
	for key, value in allWeights.iteritems():
		returnWeight*=value
	if Verbose:
		print allWeights
	return returnWeight

def signalSUSYweightBB(chain, maxPairTypeAndIndex, Verbose):
   returnWeight = 1.0
   allWeights = {}
   allWeights['PU'] = PUweight(chain, maxPairTypeAndIndex)
   allWeights['regularTrigger'] = mcTriggerWeight(chain, maxPairTypeAndIndex)
   allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
   allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
   allWeights['TriggerBug'] =  highPtTauTriggerBugWeights(chain, maxPairTypeAndIndex)
   allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
   allWeights['nevents'] = 1000.0*19.7/(chain.numberEvents*CrabJobEfficiency(chain.SampleName))
   #allWeights['tauPolarization'] = tauPolarizationWeight(chain, maxPairTypeAndIndex)
   # this is a SYS allWeights['highPtTauEff'] = highPtTauSF(chain, maxPairTypeAndIndex)
   for key, value in allWeights.iteritems():
     returnWeight*=value
   if Verbose:
     print allWeights
   return returnWeight


def getWeightForTauPolOffDY_noStitch(chain,maxPairTypeAndIndex,Verbose):
    returnWeight = 1.0
    allWeights = {}
    allWeights['PU'] = PUweight(chain, maxPairTypeAndIndex)
    allWeights['regularTrigger'] = mcTriggerWeight(chain, maxPairTypeAndIndex)
    allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
    allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
    allWeights['TriggerBug'] =  highPtTauTriggerBugWeights(chain, maxPairTypeAndIndex)
    allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
    allWeights['nevents'] = 1000.0*19.7*(3504.0)/(chain.numberEvents*CrabJobEfficiency(chain.SampleName))
    allWeights['TauPolarization'] = tauPolarizationWeight(chain, maxPairTypeAndIndex)
    #allWeights['tauPolarization'] = tauPolarizationWeight(chain, maxPairTypeAndIndex)
    # this is a SYS allWeights['highPtTauEff'] = highPtTauSF(chain, maxPairTypeAndIndex)
    for key, value in allWeights.iteritems():
      returnWeight*=value
    if Verbose:
      print allWeights
      print 'crossSection is hardcoded to ',  3504.0
    return returnWeight



def getWeightForTauPolOffDY(chain,maxPairTypeAndIndex,Verbose):
    returnWeight = 1.0
    allWeights = {}
    allWeights['PU'] = PUweight(chain, maxPairTypeAndIndex)
    allWeights['regularTrigger'] = mcTriggerWeight(chain, maxPairTypeAndIndex)
    allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
    allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
    allWeights['TriggerBug'] =  highPtTauTriggerBugWeights(chain, maxPairTypeAndIndex)
    allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
    #allWeights['nevents'] = 1000.0*19.7*(3504.0)/(chain.numberEvents*CrabJobEfficiency(chain.SampleName))
    allWeights['StitchingZjets'] = getStitchingZjetsWt(chain, maxPairTypeAndIndex)
    allWeights['TauPolarization'] = tauPolarizationWeight(chain, maxPairTypeAndIndex)
    #allWeights['tauPolarization'] = tauPolarizationWeight(chain, maxPairTypeAndIndex)
    # this is a SYS allWeights['highPtTauEff'] = highPtTauSF(chain, maxPairTypeAndIndex)
    for key, value in allWeights.iteritems():
      returnWeight*=value
    if Verbose:
      print allWeights
      print 'crossSection is hardcoded to ',  3504.0
    return returnWeight


def getWeightForRegularDY(chain,maxPairTypeAndIndex,Verbose):
    returnWeight = 1.0
    allWeights = {}
    allWeights['PU'] = PUweight(chain, maxPairTypeAndIndex)
    allWeights['regularTrigger'] = mcTriggerWeight(chain, maxPairTypeAndIndex)
    allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
    allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
    allWeights['TriggerBug'] =  highPtTauTriggerBugWeights(chain, maxPairTypeAndIndex)
    allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
    #allWeights['nevents'] = 1000.0*19.7*(chain.crossSection)/(chain.numberEvents*CrabJobEfficiency(chain.SampleName))
    allWeights['StitchingZjets'] = getStitchingZjetsWt(chain, maxPairTypeAndIndex)
    for key, value in allWeights.iteritems():
      returnWeight*=value
    if Verbose:
      print allWeights
      print 'crossSection is read from tree as ',  chain.crossSection
    return returnWeight

def getWeightForRegularDY_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose):
    returnWeight = 1.0
    allWeights = {}
    allWeights['PU'] = PUweight(chain, maxPairTypeAndIndex)
    allWeights['regularTrigger'] = mcTriggerWeight(chain, maxPairTypeAndIndex)
    allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
    allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
    allWeights['TriggerBug'] =  highPtTauTriggerBugWeights(chain, maxPairTypeAndIndex)
    if classification == '_ZTT_':
        allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
    #allWeights['nevents'] = 1000.0*19.7*(chain.crossSection)/(chain.numberEvents*CrabJobEfficiency(chain.SampleName))
    allWeights['StitchingZjets'] = getStitchingZjetsWt(chain, maxPairTypeAndIndex)
    for key, value in allWeights.iteritems():
      returnWeight*=value
    if Verbose:
      print allWeights
      print 'crossSection is read from tree as ',  chain.crossSection
    return returnWeight


def getWeightForTauPolOffDY_NOSTITCH_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose):
    returnWeight = 1.0
    allWeights = {}
    allWeights['PU'] = PUweight(chain, maxPairTypeAndIndex)
    allWeights['regularTrigger'] = mcTriggerWeight(chain, maxPairTypeAndIndex)
    allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
    allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
    allWeights['TriggerBug'] =  highPtTauTriggerBugWeights(chain, maxPairTypeAndIndex)
    if classification == '_ZTT_':
        allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
    allWeights['nevents'] = 1000.0*19.7*(3504.0)/(chain.numberEvents*CrabJobEfficiency(chain.SampleName))
    #allWeights['StitchingZjets'] = getStitchingZjetsWt(chain, maxPairTypeAndIndex)
    allWeights['TauPolarization'] = tauPolarizationWeight(chain, maxPairTypeAndIndex)
    #allWeights['tauPolarization'] = tauPolarizationWeight(chain, maxPairTypeAndIndex)
    # this is a SYS allWeights['highPtTauEff'] = highPtTauSF(chain, maxPairTypeAndIndex)
    for key, value in allWeights.iteritems():
      returnWeight*=value
    if Verbose:
      print allWeights
      print 'crossSection is hardcoded to ',  3504.0
    return returnWeight


def getWeightForTauPolOffDY_withClassificationCheck(chain,maxPairTypeAndIndex,classification,Verbose):
    returnWeight = 1.0
    allWeights = {}
    allWeights['PU'] = PUweight(chain, maxPairTypeAndIndex)
    allWeights['regularTrigger'] = mcTriggerWeight(chain, maxPairTypeAndIndex)
    allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
    allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
    allWeights['TriggerBug'] =  highPtTauTriggerBugWeights(chain, maxPairTypeAndIndex)
    if classification == '_ZTT_':
        allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
    #allWeights['nevents'] = 1000.0*19.7*(3504.0)/(chain.numberEvents*CrabJobEfficiency(chain.SampleName))
    allWeights['StitchingZjets'] = getStitchingZjetsWt(chain, maxPairTypeAndIndex)
    allWeights['TauPolarization'] = tauPolarizationWeight(chain, maxPairTypeAndIndex)
    #allWeights['tauPolarization'] = tauPolarizationWeight(chain, maxPairTypeAndIndex)
    # this is a SYS allWeights['highPtTauEff'] = highPtTauSF(chain, maxPairTypeAndIndex)
    for key, value in allWeights.iteritems():
      returnWeight*=value
    if Verbose:
      print allWeights
      print 'crossSection is hardcoded to ',  3504.0
    return returnWeight



def getWeightForVV(chain,maxPairTypeAndIndex,Verbose):
    returnWeight = 1.0
    allWeights = {}
    allWeights['PU'] = PUweight(chain, maxPairTypeAndIndex)
    allWeights['regularTrigger'] = mcTriggerWeight(chain, maxPairTypeAndIndex)
    allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
    allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
    allWeights['TriggerBug'] =  highPtTauTriggerBugWeights(chain, maxPairTypeAndIndex)
    allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
    allWeights['nevents'] = 1000.0*19.7*(chain.crossSection)/(chain.numberEvents*CrabJobEfficiency(chain.SampleName))
    for key, value in allWeights.iteritems():
      returnWeight*=value
    if Verbose:
      print allWeights
      print 'crossSection is read from tree as ',  chain.crossSection
    return returnWeight

def getWeightForTTmc(chain,maxPairTypeAndIndex,wt_dict,Verbose):
    returnWeight = 1.0
    allWeights = {}
    allWeights['PU'] = PUweight(chain, maxPairTypeAndIndex)
    allWeights['regularTrigger'] = mcTriggerWeight(chain, maxPairTypeAndIndex)
    allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
    allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
    allWeights['TriggerBug'] =  highPtTauTriggerBugWeights(chain, maxPairTypeAndIndex)
    # LLR has this off
    #allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
    allWeights['ttXsection'] = getTTmcCrossSection(chain)
    allWeights['nevents'] = 1000.0*19.7*(1.0)/(chain.numberEvents*CrabJobEfficiency(chain.SampleName))
	# off for now, will add in next round
	#allWeights['jetTauFakeRate'] = getjetTauFakeWt(chain,maxPairTypeAndIndex)
    allWeights['topPtreweight'] = getTopPtWeight(chain,maxPairTypeAndIndex)
    for key, value in allWeights.iteritems():
      returnWeight*=value
    if(allWeights['topPtreweight']!=0):
        wt_dict['topPtDown'] = returnWeight/allWeights['topPtreweight']
        wt_dict['topPtNominal'] = returnWeight
        wt_dict['topPtUp'] = returnWeight*allWeights['topPtreweight']
    if Verbose:
      print allWeights
      print 'final wts under topPt variation : ', wt_dict
      print 'crossSection is read from tree as ',  chain.crossSection
    return

#wt_dict['jetTauFakeDown'] = 1.0
#wt_dict['jetTauFakeNominal'] = 1.0
#wt_dict['jetTauFakeUp'] = 1.0
def getWeightForW(chain,maxPairTypeAndIndex,wt_dict,Verbose):
    returnWeight = 1.0
    allWeights = {}
    allWeights['PU'] = PUweight(chain, maxPairTypeAndIndex)
    allWeights['regularTrigger'] = mcTriggerWeight(chain, maxPairTypeAndIndex)
    allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
    allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
    allWeights['TriggerBug'] =  highPtTauTriggerBugWeights(chain, maxPairTypeAndIndex)
    allWeights['additionalWShape'] = WjetsShapeAdditionalCorrection(chain, maxPairTypeAndIndex)
    #print allWeights['additionalWShape']
    allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
    #allWeights['nevents'] = getWPlusJetsCrossSectionWeight(chain)
    allWeights['StitchingWjets'] = getStitchingWjetsWt(chain, maxPairTypeAndIndex)
    allWeights['jetTauFakeWt'] = getjetTauFakeWt(chain,maxPairTypeAndIndex)
    for key, value in allWeights.iteritems():
      returnWeight*=value
    if(allWeights['jetTauFakeWt']!=0):
        wt_dict['jetTauFakeDown'] = returnWeight/allWeights['jetTauFakeWt']
        wt_dict['jetTauFakeNominal'] = returnWeight
        wt_dict['jetTauFakeUp'] = returnWeight*allWeights['jetTauFakeWt']
    if Verbose:
      print allWeights
      print 'final wts under jet->tau fake variation : ', wt_dict
      print 'crossSection is read from tree as ',  chain.crossSection
    return

def getWeightEmbeddedZTT(chain,maxPairTypeAndIndex,Verbose):
    returnWeight = 1.0
    allWeights = {}
    allWeights['embeddingWeight'] = getEmbedWeight(chain,maxPairTypeAndIndex)
    allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
    allWeights['triggerBug'] = highPtTauTriggerBugWeights_forEMBEDDED(chain, maxPairTypeAndIndex)
    allWeights['embeddedEmulationOfTrigger'] = embeddedTriggerEmulationWeight(chain,maxPairTypeAndIndex)
    allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
    allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
    for key, value in allWeights.iteritems():
        returnWeight*=value
    if Verbose:
        print allWeights
    return returnWeight

def getWeightEmbeddedTTbar(chain,maxPairTypeAndIndex,Verbose):
    returnWeight = 1.0
    allWeights = {}
    allWeights['PU'] = PUweight(chain, maxPairTypeAndIndex)
    allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
    allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
    #allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
    allWeights['embeddedEmulationOfTrigger'] = embeddedTriggerEmulationWeight(chain,maxPairTypeAndIndex)
    allWeights['triggerBug'] = highPtTauTriggerBugWeights_forEMBEDDED(chain, maxPairTypeAndIndex)
    allWeights['embeddingWeight'] = getEmbedWeight(chain,maxPairTypeAndIndex)
    # use the number of events of the parent MC sample
    # use cross-section =
    allWeights['nevents'] = 1000.0*19.7*(5.8869*4.45013504560974305)/(12011428*CrabJobEfficiency(chain.SampleName))
    allWeights['topPtreweight'] = getTopPtWeight(chain,maxPairTypeAndIndex)
    for key, value in allWeights.iteritems():
        returnWeight*=value
    if Verbose:
        print allWeights
    return returnWeight

def getWeightFor_XSM125(chain, maxPairTypeAndIndex, Verbose, CROSSXBR):
    # need the CROSSXBR argument because I forgot to fill these in when
    # creating the xml file
    returnWeight = 1.0
    allWeights = {}
    allWeights['PU'] = PUweight(chain, maxPairTypeAndIndex)
    allWeights['regularTrigger'] = mcTriggerWeight(chain, maxPairTypeAndIndex)
    allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
    allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
    allWeights['TriggerBug'] =  highPtTauTriggerBugWeights(chain, maxPairTypeAndIndex)
    allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
    allWeights['nevents'] = 1000.0*19.7*CROSSXBR/(chain.numberEvents*CrabJobEfficiency(chain.SampleName))
    for key, value in allWeights.iteritems():
        returnWeight*=value
    if Verbose:
        print allWeights
    return returnWeight


def getWeightForLowMassDY(chain,maxPairTypeAndIndex,Verbose):
    returnWeight = 1.0
    allWeights = {}
    allWeights['PU'] = PUweight(chain, maxPairTypeAndIndex)
    allWeights['regularTrigger'] = mcTriggerWeight(chain, maxPairTypeAndIndex)
    allWeights['leptonID'] = leptonIDweights(chain, maxPairTypeAndIndex)
    allWeights['leptonISOL'] = leptonISOLweights(chain, maxPairTypeAndIndex)
    allWeights['TriggerBug'] =  highPtTauTriggerBugWeights(chain, maxPairTypeAndIndex)
    allWeights['decayMode'] = decayModeCorrection(chain,maxPairTypeAndIndex)
    allWeights['StitchingLowMassDY'] = getStitchingLowMassDY(chain, maxPairTypeAndIndex)
    for key, value in allWeights.iteritems():
      returnWeight*=value    
    if Verbose:
      print allWeights
    return returnWeight
