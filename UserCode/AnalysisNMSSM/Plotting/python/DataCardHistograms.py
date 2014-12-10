import time
import sys
import os
from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TDirectoryFile
from array import array

from Plotting.python.FileName import FileNamePrefix



###########################
# create the File dict

dataCardFiles = {}

##################
# master lists

eventType = []
dataCardCategories = []
sampleType = []
sampleTitle = []


##############################
# fill the lists

eventType.append("muTau")
eventType.append("eleTau")

dataCardCategories.append("inclusive")
dataCardCategories.append("btag")
dataCardCategories.append("btag_high")
dataCardCategories.append("btag_low")
dataCardCategories.append("nobtag")
dataCardCategories.append("nobtag_high")
dataCardCategories.append("nobtag_medium")
dataCardCategories.append("nobtag_low")

#########################
# create the histogram names and titles

sampleType.append('QCD')
sampleType.append('QCD_CMS_htt_QCDShape_etau_btag_8TeVDown')
sampleType.append('QCD_CMS_htt_QCDShape_etau_btag_8TeVUp')
sampleType.append('QCD_CMS_htt_QCDShape_mutau_btag_8TeVDown')
sampleType.append('QCD_CMS_htt_QCDShape_mutau_btag_8TeVUp')
sampleType.append('QCD_CMS_htt_QCDfrShape_etau_8TeVDown')
sampleType.append('QCD_CMS_htt_QCDfrShape_etau_8TeVUp')
sampleType.append('QCD_CMS_htt_QCDfrShape_mutau_8TeVDown')
sampleType.append('QCD_CMS_htt_QCDfrShape_mutau_8TeVUp')

sampleType.append('TT')
sampleType.append('TT_CMS_htt_ttbarJetFake_8TeVDown')
sampleType.append('TT_CMS_htt_ttbarJetFake_8TeVUp')
sampleType.append('TT_CMS_htt_ttbarPtReweight_8TeVDown')
sampleType.append('TT_CMS_htt_ttbarPtReweight_8TeVUp')
sampleType.append('TT_CMS_scale_t_etau_8TeVDown')
sampleType.append('TT_CMS_scale_t_etau_8TeVUp')
sampleType.append('TT_CMS_scale_t_mutau_8TeVDown')
sampleType.append('TT_CMS_scale_t_mutau_8TeVUp')

sampleType.append('VH_SM125')
sampleType.append('VH_SM125_CMS_scale_t_etau_8TeVDown')
sampleType.append('VH_SM125_CMS_scale_t_etau_8TeVUp')
sampleType.append('VH_SM125_CMS_scale_t_mutau_8TeVDown')
sampleType.append('VH_SM125_CMS_scale_t_mutau_8TeVUp')

sampleType.append('qqH_SM125')
sampleType.append('qqH_SM125_CMS_scale_t_etau_8TeVDown')
sampleType.append('qqH_SM125_CMS_scale_t_etau_8TeVUp')
sampleType.append('qqH_SM125_CMS_scale_t_mutau_8TeVDown')
sampleType.append('qqH_SM125_CMS_scale_t_mutau_8TeVUp')


sampleType.append('VV')
sampleType.append('VV_CMS_scale_t_etau_8TeVDown')
sampleType.append('VV_CMS_scale_t_etau_8TeVUp')
sampleType.append('VV_CMS_scale_t_mutau_8TeVDown')
sampleType.append('VV_CMS_scale_t_mutau_8TeVUp')

sampleType.append('W')
sampleType.append('W_CMS_htt_WShape_etau_btag_8TeVDown')
sampleType.append('W_CMS_htt_WShape_etau_btag_8TeVUp')
sampleType.append('W_CMS_htt_WShape_mutau_btag_8TeVDown')
sampleType.append('W_CMS_htt_WShape_mutau_btag_8TeVUp')
sampleType.append('W_CMS_scale_t_etau_8TeVDown')
sampleType.append('W_CMS_scale_t_etau_8TeVUp')
sampleType.append('W_CMS_scale_t_mutau_8TeVDown')
sampleType.append('W_CMS_scale_t_mutau_8TeVUp')

sampleType.append('ZJ')
sampleType.append('ZJ_CMS_scale_t_etau_8TeVDown')
sampleType.append('ZJ_CMS_scale_t_etau_8TeVUp')
sampleType.append('ZJ_CMS_scale_t_mutau_8TeVDown')
sampleType.append('ZJ_CMS_scale_t_mutau_8TeVUp')

sampleType.append('ZL')
sampleType.append('ZL_CMS_htt_ZLScale_etau_8TeVDown')
sampleType.append('ZL_CMS_htt_ZLScale_etau_8TeVUp')
sampleType.append('ZL_CMS_htt_ZLScale_mutau_8TeVDown')
sampleType.append('ZL_CMS_htt_ZLScale_mutau_8TeVUp')
sampleType.append('ZL_CMS_scale_t_etau_8TeVDown')
sampleType.append('ZL_CMS_scale_t_etau_8TeVUp')
sampleType.append('ZL_CMS_scale_t_mutau_8TeVDown')
sampleType.append('ZL_CMS_scale_t_mutau_8TeVUp')

sampleType.append('ZTT')
sampleType.append('ZTT_CMS_scale_t_etau_8TeVDown')
sampleType.append('ZTT_CMS_scale_t_etau_8TeVUp')
sampleType.append('ZTT_CMS_scale_t_mutau_8TeVDown')
sampleType.append('ZTT_CMS_scale_t_mutau_8TeVUp')

sampleType.append('ZTT_lowMass')
sampleType.append('ZTT_lowMass_CMS_scale_t_etau_8TeVDown')
sampleType.append('ZTT_lowMass_CMS_scale_t_etau_8TeVUp')
sampleType.append('ZTT_lowMass_CMS_scale_t_mutau_8TeVDown')
sampleType.append('ZTT_lowMass_CMS_scale_t_mutau_8TeVUp')

sampleType.append('data_obs')

sampleType.append('ggH_SM125')
sampleType.append('ggH_SM125_CMS_scale_t_etau_8TeVDown')
sampleType.append('ggH_SM125_CMS_scale_t_etau_8TeVUp')
sampleType.append('ggH_SM125_CMS_scale_t_mutau_8TeVDown')
sampleType.append('ggH_SM125_CMS_scale_t_mutau_8TeVUp')

sampleType.append('bba125')
sampleType.append('bba125_CMS_scale_t_etau_8TeVDown')
sampleType.append('bba125_CMS_scale_t_etau_8TeVUp')
sampleType.append('bba125_CMS_scale_t_mutau_8TeVDown')
sampleType.append('bba125_CMS_scale_t_mutau_8TeVUp')
sampleType.append('bba130')
sampleType.append('bba130_CMS_scale_t_etau_8TeVDown')
sampleType.append('bba130_CMS_scale_t_etau_8TeVUp')
sampleType.append('bba130_CMS_scale_t_mutau_8TeVDown')
sampleType.append('bba130_CMS_scale_t_mutau_8TeVUp')
sampleType.append('bba135')
sampleType.append('bba135_CMS_scale_t_etau_8TeVDown')
sampleType.append('bba135_CMS_scale_t_etau_8TeVUp')
sampleType.append('bba135_CMS_scale_t_mutau_8TeVDown')
sampleType.append('bba135_CMS_scale_t_mutau_8TeVUp')
sampleType.append('bba140')
sampleType.append('bba140_CMS_scale_t_etau_8TeVDown')
sampleType.append('bba140_CMS_scale_t_etau_8TeVUp')
sampleType.append('bba140_CMS_scale_t_mutau_8TeVDown')
sampleType.append('bba140_CMS_scale_t_mutau_8TeVUp')
sampleType.append('bba145')
sampleType.append('bba145_CMS_scale_t_etau_8TeVDown')
sampleType.append('bba145_CMS_scale_t_etau_8TeVUp')
sampleType.append('bba145_CMS_scale_t_mutau_8TeVDown')
sampleType.append('bba145_CMS_scale_t_mutau_8TeVUp')
sampleType.append('bba150')
sampleType.append('bba150_CMS_scale_t_etau_8TeVDown')
sampleType.append('bba150_CMS_scale_t_etau_8TeVUp')
sampleType.append('bba150_CMS_scale_t_mutau_8TeVDown')
sampleType.append('bba150_CMS_scale_t_mutau_8TeVUp')
sampleType.append('bba155')
sampleType.append('bba155_CMS_scale_t_etau_8TeVDown')
sampleType.append('bba155_CMS_scale_t_etau_8TeVUp')
sampleType.append('bba155_CMS_scale_t_mutau_8TeVDown')
sampleType.append('bba155_CMS_scale_t_mutau_8TeVUp')
sampleType.append('bba160')
sampleType.append('bba160_CMS_scale_t_etau_8TeVDown')
sampleType.append('bba160_CMS_scale_t_etau_8TeVUp')
sampleType.append('bba160_CMS_scale_t_mutau_8TeVDown')
sampleType.append('bba160_CMS_scale_t_mutau_8TeVUp')
sampleType.append('bba165')
sampleType.append('bba165_CMS_scale_t_etau_8TeVDown')
sampleType.append('bba165_CMS_scale_t_etau_8TeVUp')
sampleType.append('bba165_CMS_scale_t_mutau_8TeVDown')
sampleType.append('bba165_CMS_scale_t_mutau_8TeVUp')
sampleType.append('bba170')
sampleType.append('bba170_CMS_scale_t_etau_8TeVDown')
sampleType.append('bba170_CMS_scale_t_etau_8TeVUp')
sampleType.append('bba170_CMS_scale_t_mutau_8TeVDown')
sampleType.append('bba170_CMS_scale_t_mutau_8TeVUp')
sampleType.append('bba175')
sampleType.append('bba175_CMS_scale_t_etau_8TeVDown')
sampleType.append('bba175_CMS_scale_t_etau_8TeVUp')
sampleType.append('bba175_CMS_scale_t_mutau_8TeVDown')
sampleType.append('bba175_CMS_scale_t_mutau_8TeVUp')
sampleType.append('bba180')
sampleType.append('bba180_CMS_scale_t_etau_8TeVDown')
sampleType.append('bba180_CMS_scale_t_etau_8TeVUp')
sampleType.append('bba180_CMS_scale_t_mutau_8TeVDown')
sampleType.append('bba180_CMS_scale_t_mutau_8TeVUp')



sampleTitle.append('QCD')
sampleTitle.append('QCD_CMS_htt_QCDShape_etau_btag_8TeVDown')
sampleTitle.append('QCD_CMS_htt_QCDShape_etau_btag_8TeVUp')
sampleTitle.append('QCD_CMS_htt_QCDShape_mutau_btag_8TeVDown')
sampleTitle.append('QCD_CMS_htt_QCDShape_mutau_btag_8TeVUp')
sampleTitle.append('QCD_CMS_htt_QCDfrShape_etau_8TeVDown')
sampleTitle.append('QCD_CMS_htt_QCDfrShape_etau_8TeVUp')
sampleTitle.append('QCD_CMS_htt_QCDfrShape_mutau_8TeVDown')
sampleTitle.append('QCD_CMS_htt_QCDfrShape_mutau_8TeVUp')

sampleTitle.append('TT')
sampleTitle.append('TT_CMS_htt_ttbarJetFake_8TeVDown')
sampleTitle.append('TT_CMS_htt_ttbarJetFake_8TeVUp')
sampleTitle.append('TT_CMS_htt_ttbarPtReweight_8TeVDown')
sampleTitle.append('TT_CMS_htt_ttbarPtReweight_8TeVUp')
sampleTitle.append('TT_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('TT_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('TT_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('TT_CMS_scale_t_mutau_8TeVUp')

sampleTitle.append('VH_SM125')
sampleTitle.append('VH_SM125_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('VH_SM125_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('VH_SM125_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('VH_SM125_CMS_scale_t_mutau_8TeVUp')

sampleTitle.append('qqH_SM125')
sampleTitle.append('qqH_SM125_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('qqH_SM125_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('qqH_SM125_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('qqH_SM125_CMS_scale_t_mutau_8TeVUp')


sampleTitle.append('VV')
sampleTitle.append('VV_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('VV_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('VV_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('VV_CMS_scale_t_mutau_8TeVUp')

sampleTitle.append('W')
sampleTitle.append('W_CMS_htt_WShape_etau_btag_8TeVDown')
sampleTitle.append('W_CMS_htt_WShape_etau_btag_8TeVUp')
sampleTitle.append('W_CMS_htt_WShape_mutau_btag_8TeVDown')
sampleTitle.append('W_CMS_htt_WShape_mutau_btag_8TeVUp')
sampleTitle.append('W_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('W_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('W_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('W_CMS_scale_t_mutau_8TeVUp')

sampleTitle.append('ZJ')
sampleTitle.append('ZJ_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('ZJ_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('ZJ_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('ZJ_CMS_scale_t_mutau_8TeVUp')

sampleTitle.append('ZL')
sampleTitle.append('ZL_CMS_htt_ZLScale_etau_8TeVDown')
sampleTitle.append('ZL_CMS_htt_ZLScale_etau_8TeVUp')
sampleTitle.append('ZL_CMS_htt_ZLScale_mutau_8TeVDown')
sampleTitle.append('ZL_CMS_htt_ZLScale_mutau_8TeVUp')
sampleTitle.append('ZL_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('ZL_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('ZL_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('ZL_CMS_scale_t_mutau_8TeVUp')

sampleTitle.append('ZTT')
sampleTitle.append('ZTT_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('ZTT_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('ZTT_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('ZTT_CMS_scale_t_mutau_8TeVUp')

sampleTitle.append('ZTT_lowMass')
sampleTitle.append('ZTT_lowMass_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('ZTT_lowMass_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('ZTT_lowMass_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('ZTT_lowMass_CMS_scale_t_mutau_8TeVUp')

sampleTitle.append('data_obs')

sampleTitle.append('ggH_SM125')
sampleTitle.append('ggH_SM125_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('ggH_SM125_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('ggH_SM125_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('ggH_SM125_CMS_scale_t_mutau_8TeVUp')

sampleTitle.append('bba125')
sampleTitle.append('bba125_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('bba125_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('bba125_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('bba125_CMS_scale_t_mutau_8TeVUp')
sampleTitle.append('bba130')
sampleTitle.append('bba130_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('bba130_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('bba130_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('bba130_CMS_scale_t_mutau_8TeVUp')
sampleTitle.append('bba135')
sampleTitle.append('bba135_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('bba135_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('bba135_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('bba135_CMS_scale_t_mutau_8TeVUp')
sampleTitle.append('bba140')
sampleTitle.append('bba140_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('bba140_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('bba140_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('bba140_CMS_scale_t_mutau_8TeVUp')
sampleTitle.append('bba145')
sampleTitle.append('bba145_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('bba145_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('bba145_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('bba145_CMS_scale_t_mutau_8TeVUp')
sampleTitle.append('bba150')
sampleTitle.append('bba150_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('bba150_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('bba150_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('bba150_CMS_scale_t_mutau_8TeVUp')
sampleTitle.append('bba155')
sampleTitle.append('bba155_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('bba155_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('bba155_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('bba155_CMS_scale_t_mutau_8TeVUp')
sampleTitle.append('bba160')
sampleTitle.append('bba160_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('bba160_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('bba160_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('bba160_CMS_scale_t_mutau_8TeVUp')
sampleTitle.append('bba165')
sampleTitle.append('bba165_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('bba165_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('bba165_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('bba165_CMS_scale_t_mutau_8TeVUp')
sampleTitle.append('bba170')
sampleTitle.append('bba170_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('bba170_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('bba170_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('bba170_CMS_scale_t_mutau_8TeVUp')
sampleTitle.append('bba175')
sampleTitle.append('bba175_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('bba175_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('bba175_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('bba175_CMS_scale_t_mutau_8TeVUp')
sampleTitle.append('bba180')
sampleTitle.append('bba180_CMS_scale_t_etau_8TeVDown')
sampleTitle.append('bba180_CMS_scale_t_etau_8TeVUp')
sampleTitle.append('bba180_CMS_scale_t_mutau_8TeVDown')
sampleTitle.append('bba180_CMS_scale_t_mutau_8TeVUp')


#############################
# declare histogram dictionary

histogram_dict = {}


#######################
# declare files

for evT in range(0, len(eventType)):
  fileName = FileNamePrefix+"davis_htt_mssm_"+eventType[evT]+".root"
  dataCardFiles[fileName] = TFile( fileName, 'RECREATE', 'test' )

################################
# add directories to files

for evT in range(0, len(eventType)):
  fileName = FileNamePrefix+"davis_htt_mssm_"+eventType[evT]+".root"
  dataCardFiles[fileName].cd()
  for index in range(0, len(dataCardCategories)):
    directoryName = eventType[evT]+"_"+dataCardCategories[index]
    dataCardFiles[fileName].mkdir(directoryName)
    #TDirectoryFile(directoryName,directoryName)

#############################
# add histograms to dictionaries



binning_nominal_btag = [0 , 5 , 10 , 15 , 20 , 25, 30, 35, 40, 45, 
50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 
160, 180, 200]

binning_nominal_nobtag = [0 , 5 , 10 , 15 , 20 , 25, 30, 35, 40, 45, 
50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 
160, 180, 200]

for evT in range(0, len(eventType)):
  for dictIndx in range(0, len(dataCardCategories)):
    for sampleIndx in range(0, len(sampleType)):
      histName = eventType[evT]+"_"+sampleType[sampleIndx]+"_"+dataCardCategories[dictIndx]
      if 'fine_binning' in sampleType[sampleIndx]:
        histogram_dict[histName] = TH1F(histName,sampleTitle[sampleIndx],400,0,2000)
      else:
        if 'nobtag' in dataCardCategories[dictIndx] or 'inclusive' in dataCardCategories[dictIndx]:
          histogram_dict[histName] = TH1F(histName,sampleTitle[sampleIndx],len(binning_nominal_nobtag)-1,array('d',binning_nominal_nobtag))
        else:
          histogram_dict[histName] = TH1F(histName,sampleTitle[sampleIndx],len(binning_nominal_btag)-1,array('d',binning_nominal_btag))
      histogram_dict[histName].Sumw2()
      #histogram_dict[histName].SetDirectory(0)



def ShouldIWriteItHere(fileName,directoryName,sampleType,histName):
  writeIt = True
  if 'eleTau' in directoryName and '_mutau' in histName:
    writeIt = False
  if 'muTau' in directoryName and 'etau' in histName:
     writeIt = False
  if directoryName[-len('_btag'):] == '_btag':
    if 'tag_low' in histName:
      writeIt = False
    if 'tag_medium' in histName:
      writeIt = False
    if 'tag_high' in histName:
      writeIt = False
    if 'nobtag' in histName:
      writeIt = False
  if directoryName[-len('_btag_high'):] == '_btag_high':
    if 'tag_low' in histName:
      writeIt = False
    if 'tag_medium' in histName:
      writeIt = False
    if 'nobtag' in histName:
      writeIt = False
    if 'btag_8' in histName:
      writeIt = False
    if histName[-len('_btag'):] == '_btag':
      writeIt = False
  if directoryName[-len('_btag_low'):] == '_btag_low':
    if 'tag_high' in histName:
      writeIt = False
    if 'tag_medium' in histName:
      writeIt = False
    if 'nobtag' in histName:
      writeIt = False
    if 'btag_8' in histName:
      writeIt = False
    if histName[-len('_btag'):] == '_btag':
      writeIt = False
  if directoryName[-len('_nobtag'):] == '_nobtag':
    if 'tag_low' in histName:
      writeIt = False
    if 'tag_medium' in histName:
      writeIt = False
    if 'tag_high' in histName:
      writeIt = False
    if '_btag' in histName:
      writeIt = False
  if directoryName[-len('_nobtag_high'):] == '_nobtag_high':
    if 'tag_low' in histName:
      writeIt = False
    if 'tag_medium' in histName:
      writeIt = False
    if '_btag' in histName:
      writeIt = False
    if 'nobtag_8' in histName:
      writeIt = False
    if histName[-len('_nobtag'):] == '_nobtag':
      writeIt = False
  if directoryName[-len('_nobtag_medium'):] == '_nobtag_medium':
    if 'tag_high' in histName:
      writeIt = False
    if 'tag_low' in histName:
      writeIt = False
    if '_btag' in histName:
      writeIt = False
    if 'nobtag_8' in histName:
      writeIt = False
    if histName[-len('_nobtag'):] == '_nobtag':
      writeIt = False
  if directoryName[-len('_nobtag_low'):] == '_nobtag_low':
    if 'tag_high' in histName:
      writeIt = False
    if 'tag_medium' in histName:
      writeIt = False
    if '_btag' in histName:
      writeIt = False
    if 'nobtag_8' in histName:
      writeIt = False
    if histName[-len('_nobtag'):] == '_nobtag':
      writeIt = False
  if '_inclusive' in directoryName and '_btag' in histName:
    writeIt = False
  if '_inclusive' in directoryName and '_nobtag' in histName:
    writeIt = False
  if '_inclusive' in directoryName and 'fine_binning' in histName:
    writeIt = False
  if '_inclusive' in directoryName and 'TT_CMS_htt_ZLScale_mutau_8TeV' in histName:
    writeIt = False
  if '_inclusive' in directoryName and 'TT_CMS_htt_ZLScale_etau_8TeV' in histName:
    writeIt = False
  return writeIt


def WriteEverything():
  for evT in range(0, len(eventType)):
    fileName = FileNamePrefix+"davis_htt_mssm_"+eventType[evT]+".root"
    dataCardFiles[fileName].cd()
    for dictIndx in range(0, len(dataCardCategories)):
      directoryName = eventType[evT]+"_"+dataCardCategories[dictIndx]
      print 'changing dir to ',directoryName
      dataCardFiles[fileName].cd(directoryName)
      for sampleIndx in range(0, len(sampleType)):
        histName = eventType[evT]+"_"+sampleType[sampleIndx]+"_"+dataCardCategories[dictIndx]
        suffix = "_"+dataCardCategories[dictIndx]
        prefix = eventType[evT]+"_"
        writeAs = histName[:-len(suffix)]
        writeAs = writeAs[len(prefix):]
        #if ShouldIWriteItHere(fileName,directoryName,sampleType[sampleIndx],writeAs):
        histogram_dict[histName].SetName(writeAs)
        histogram_dict[histName].Write(writeAs)
    dataCardFiles[fileName].Close()
  return


# def WriteEverything():
#   for evT in range(0, len(eventType)):
#     fileName = "davis_htt_mssm_"+eventType[evT]+".root"
#     dataCardFiles[fileName].cd()
#     for dictIndx in range(0, len(dataCardCategories)):
#       directoryName = eventType[evT]+"_"+dataCardCategories[dictIndx]
#       dataCardFiles[fileName].cd(directoryName)
#       for sampleIndx in range(0, len(sampleType)):
#         histName = eventType[evT]+"_"+sampleType[sampleIndx]+"_"+dataCardCategories[dictIndx]
#         suffix = "_"+dataCardCategories[dictIndx]
#         prefix = eventType[evT]+"_"
#         writeAs = histName[:-len(suffix)]
#         writeAs = writeAs[len(prefix):]
#         histogram_dict[histName].SetName(writeAs)
#         histogram_dict[histName].Write(writeAs)
#     dataCardFiles[fileName].Close()
#   return
