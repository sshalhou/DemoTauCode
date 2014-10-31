import time
import sys
import os

from ROOT import gROOT,TChain, TLorentzVector, TSelector, TTree, TF1, TH1F, TCanvas, gStyle, TFile
from ROOT import TApplication,TTreeCache
from ROOT import TDirectoryFile
from array import array


#############
# imports

from python.InputRootFiles import *
from python.directories import *
from python.HistogramList import *
from python.Binning import *
from python.Functions import *
from python.ScaleFactors import *

#########

print 'Will produce final data card inputs for the following channels : ',CHANNELS

##############################
# begin loop over channels   #

for chan in range(0,len(CHANNELS)):

    FILENAME = PREFIX+CHANNELS[chan]+'.root'

    print '***************************************************************'
    print '*     creating root file ', FILENAME
    print '***************************************************************'

    NEWFILE = TFile(FILENAME,'RECREATE')
    HISTOGRAM_DICTIONARY = {}

    for direc in range(0,len(DIRLIST)):
        DIRNAME = CHANNELS[chan]+"_"+DIRLIST[direc]
        print '*** creating directory ', DIRNAME
        NEWFILE.mkdir(DIRNAME)
        for hist in range(0, len(HISTLIST)):
            if RejectHistogram(DIRNAME, HISTLIST[hist]) is False:

                LOCAL_HIST_NAME = DIRNAME+"/"+str(HISTLIST[hist])
                if 'fine_binning' in str(HISTLIST[hist]):
                    HISTOGRAM_DICTIONARY[LOCAL_HIST_NAME] = TH1F(LOCAL_HIST_NAME,
                                                                LOCAL_HIST_NAME,
                                                                fine_binning[0],
                                                                fine_binning[1],
                                                                fine_binning[2])
                    HISTOGRAM_DICTIONARY[LOCAL_HIST_NAME].Sumw2()
                else:
                    if 'nobtag' in str(DIRNAME) or 'inclusive' in str(DIRNAME):
                        HISTOGRAM_DICTIONARY[LOCAL_HIST_NAME] = TH1F(LOCAL_HIST_NAME,
                                                                    LOCAL_HIST_NAME,
                                                                    len(binning_nominal_nobtag)-1,
                                                                    array('d',binning_nominal_nobtag))
                        HISTOGRAM_DICTIONARY[LOCAL_HIST_NAME].Sumw2()

                    else:
                        HISTOGRAM_DICTIONARY[LOCAL_HIST_NAME] = TH1F(LOCAL_HIST_NAME,
                                                                    LOCAL_HIST_NAME,
                                                                    len(binning_nominal_btag)-1,
                                                                    array('d',binning_nominal_btag))
                        HISTOGRAM_DICTIONARY[LOCAL_HIST_NAME].Sumw2()

    print '***************************************************************'
    print '*     begin histogram addition phase for', FILENAME
    print '***************************************************************'

    for addFile in range(0,len(FOR_UNMODIFIED_ADDITION)):
        if str(CHANNELS[chan]) in str(FOR_UNMODIFIED_ADDITION[addFile]):
            GOTFILE = TFile(FOR_UNMODIFIED_ADDITION[addFile],'READ')
            print '*** adding histograms from ', FOR_UNMODIFIED_ADDITION[addFile]
            for key, value in HISTOGRAM_DICTIONARY.iteritems():
                if str(CHANNELS[chan]) in key:
                    GOTHIST = GOTFILE.Get(key)
                    if(GOTHIST):
                        HISTOGRAM_DICTIONARY[key].Add(GOTHIST)
                    else:
                        print 'WARNING FAILED TO FIND :', key


                    #print GOTHIST.GetTitle(),GOTHIST.GetSumOfWeights()


    print '***************************************************************'
    print '*     begin QCD normaization determination for', FILENAME
    print '***************************************************************'


    NORMSDICT = {}
    NORMSDICT['QCD'] = 0.0
    NORMSDICT['W'] = 0.0
    NORMSDICT['ZTT'] = 0.0
    NORMSDICT['ZL'] = 0.0
    NORMSDICT['ZJ'] = 0.0
    NORMSDICT['TT'] = 0.0
    NORMSDICT['VV'] = 0.0

    ##############################
    # this will hold the norm
    # derived by comparing the inclusive
    # selections in SS and OS
    QCDNORM = {}


    for direc in range(0,len(DIRLIST)):
        DIRNAME = CHANNELS[chan]+"_"+DIRLIST[direc]
        NORMSDICT['QCD'] = 0.0
        NORMSDICT['W'] = 0.0
        NORMSDICT['ZTT'] = 0.0
        NORMSDICT['ZL'] = 0.0
        NORMSDICT['ZJ'] = 0.0
        NORMSDICT['TT'] = 0.0
        NORMSDICT['VV'] = 0.0

        print '**************************************'
        print '* starting QCD bkg sub for dir. ', DIRNAME
        print '**************************************'

        for addFile in range(0,len(FOR_QCD_NORM)):
            if str(CHANNELS[chan]) in str(FOR_QCD_NORM[addFile]):
                GOTFILE = TFile(FOR_QCD_NORM[addFile],'READ')
                #print '*** summing QCD norm histograms from ', FOR_QCD_NORM[addFile]

                for key, value in NORMSDICT.iteritems():
                    LOCALNAME = DIRNAME+"/"+key
                    #print "--> ",LOCALNAME
                    GOTHIST = GOTFILE.Get(LOCALNAME)
                    if(GOTHIST):
                        NORMSDICT[key] = value + GOTHIST.GetSumOfWeights()
                    else:
                        print 'WARNING FAILED TO FIND :', key


            # print 'after file ', FOR_QCD_NORM[addFile], ' in directory ', DIRNAME , 'sums are :'
            # for key, value in NORMSDICT.iteritems():
            #         print key,' = ',value



        ################################
        # figure out normalization SFs

        QCDNORM[DIRNAME] =  OStoSSfactor * (NORMSDICT['QCD']-
                                    NORMSDICT['W'] -
                                    NORMSDICT['ZTT'] -
                                    NORMSDICT['ZL'] -
                                    NORMSDICT['ZJ'] -
                                    NORMSDICT['TT'] -
                                    NORMSDICT['VV'])

    # print 'after calculation the bkg sub QCD totals are are : '
    # for key, value in QCDNORM.iteritems():
    #     print key,' = ',value


    print 'transform bkg sub QCD totals into scaleFactors : '
    for key, value in QCDNORM.iteritems():
        print '---------------'
        print 'in channel ',key, 'bkg sub. SS QCD is ', value
        print 'the raw OS estimate was ', HISTOGRAM_DICTIONARY[key+'/QCD'].GetSumOfWeights()
        QCDNORM[key] = value/HISTOGRAM_DICTIONARY[key+'/QCD'].GetSumOfWeights()
        print ' the scale factor is ', QCDNORM[key]


    print 'applying QCD normalizaton ...'
    for direc in range(0,len(DIRLIST)):
        DIRNAME = CHANNELS[chan]+"_"+DIRLIST[direc]
        for key, value in HISTOGRAM_DICTIONARY.iteritems():
            if 'QCD' in str(key) and DIRNAME in str(key):
                 #print 'normalization of ', key, 'in progress ...', HISTOGRAM_DICTIONARY[key].GetSumOfWeights(), ' is now '
                 HISTOGRAM_DICTIONARY[key].Scale(QCDNORM[DIRNAME])
                 #print '-----------> ', HISTOGRAM_DICTIONARY[key].GetSumOfWeights()





    print '***************************************************************'
    print '*     begin ZTT embedded normaization determination for', FILENAME
    print '*     unlike other norm. this is done from inclusive category only'
    print '***************************************************************'

    print '* looping over ZTT templates for embedded TT subtraction :'
    for direc in range(0,len(DIRLIST)):
        DIRNAME = CHANNELS[chan]+"_"+DIRLIST[direc]
        for key, value in HISTOGRAM_DICTIONARY.iteritems():
            if 'ZTT' in str(key) and DIRNAME in str(key):
                print 'begin tt-embedded subtraction from ', key
                for subFile in range(0,len(FOR_TTEMBEDDED_SUB)):
                    if str(CHANNELS[chan]) in str(FOR_TTEMBEDDED_SUB[subFile]):
                        print 'searching for subtraction template ', key, 'in file ',FOR_TTEMBEDDED_SUB[subFile]
                        GOTFILE = TFile(FOR_TTEMBEDDED_SUB[subFile],'READ')

                        GOTHIST = GOTFILE.Get(key)
                        if(GOTHIST):
                            #print 'found ', key, 'for sub. integral = ', GOTHIST.GetSumOfWeights()
                            #print 'subtraction starting for', key, '....'
                            initial = HISTOGRAM_DICTIONARY[key].GetSumOfWeights()
                            print '-----> initial integral = ', initial
                            HISTOGRAM_DICTIONARY[key].Add(GOTHIST,-1.0)
                            final = HISTOGRAM_DICTIONARY[key].GetSumOfWeights()
                            print '-----> final integral = ', final

                            print '****************************************'
                            print '* begin elimination of negative content bins'
                            print '* template integral will be held fixed at ', final
                            print '* bin error will be kept fixed in this case'
                            print '****************************************'
                            newintegral = HISTOGRAM_DICTIONARY[key].GetSumOfWeights()

                            for ibin in range(0, HISTOGRAM_DICTIONARY[key].GetNbinsX()+1):
                                if(HISTOGRAM_DICTIONARY[key].GetBinContent(ibin)<0):
                                    #print 'bin # ', ibin, 'in ', key, 'has value ', HISTOGRAM_DICTIONARY[key].GetBinContent(ibin)
                                    HISTOGRAM_DICTIONARY[key].SetBinContent(ibin,0.00)
                                    newintegral = HISTOGRAM_DICTIONARY[key].GetSumOfWeights()

                            HISTOGRAM_DICTIONARY[key].Scale(final/newintegral)
                            #print '-----> tt-subtracted integral = ', final
                            #print '---------> integral after zero bin elimination ', HISTOGRAM_DICTIONARY[key].GetSumOfWeights()

                        else:
                            print 'WARNING FAILED TO FIND :', key


    print '* begin extraction of ZTT normalization scale factors using only inclusive category :'

    histname = CHANNELS[chan]+"_inclusive/ZTT"
    ZTT_MC_INTEGRAL = 0.0
    for nfile in range(0, len(FOR_ZTT_NORM)):
        if str(CHANNELS[chan]) in str(FOR_ZTT_NORM[nfile]):
            print 'searching for inclusive template ', histname, 'in file ',FOR_ZTT_NORM[nfile]

            GOTFILE = TFile(FOR_ZTT_NORM[nfile],'READ')
            GOTHIST = GOTFILE.Get(histname)
            if(GOTHIST):
                ZTT_MC_INTEGRAL += GOTHIST.GetSumOfWeights()

    print 'total ZTT estimate from MC for ',  histname, ' is ',      ZTT_MC_INTEGRAL
    print 'the raw embedded ZTT template integral is ', HISTOGRAM_DICTIONARY[histname].GetSumOfWeights()
    ZTT_EMBEDDED_SF = ZTT_MC_INTEGRAL/HISTOGRAM_DICTIONARY[histname].GetSumOfWeights()
    print 'giving a scaleFactor for ', CHANNELS[chan], ' of ', ZTT_EMBEDDED_SF
    print 'applying scale factors to all ZTT templates ...'
    for key, value in HISTOGRAM_DICTIONARY.iteritems():
        if 'ZTT' in str(key) and str(CHANNELS[chan]) in str(key):
            print 'apply SF to ', key
            #HISTOGRAM_DICTIONARY[key].Scale(ZTT_EMBEDDED_SF)





                # # NORMSDICT['QCD'] = 0.0
                # NORMSDICT['W'] = 0.0
                # NORMSDICT['ZTT'] = 0.0
                # NORMSDICT['ZL'] = 0.0
                # NORMSDICT['ZJ'] = 0.0
                # NORMSDICT['TT'] = 0.0
                # NORMSDICT['VV'] = 0.0
                #
                # print 'in channel ',DIRNAME, 'bkg sub. SS QCD is ', QCDNORM[DIRNAME]
                # print 'the raw OS estimate was ', HISTOGRAM_DICTIONARY[DIRNAME+'/QCD'].GetSumOfWeights()
                # QCDNORM[DIRNAME] = QCDNORM[DIRNAME]/HISTOGRAM_DICTIONARY[DIRNAME+'/QCD'].GetSumOfWeights()
                # print 'the final norm. factor to be applied to QCD templates is ', QCDNORM[DIRNAME]
                #
                # print 'applying QCD normalizaton ...'
                # for key, value in HISTOGRAM_DICTIONARY.iteritems():
                #     if 'QCD' in str(key) and DIRNAME in str(key):
                #         print 'normalization of ', key, 'in progress ...'
                #         HISTOGRAM_DICTIONARY[key].Scale(QCDNORM[DIRNAME])
                #


    #
    # print '***************************************************************'
    # print '*     begin W normaization determination for', FILENAME
    # print '***************************************************************'
    #
    # W_NORMSDICT = {}
    # W_NORMSDICT['data_obs'] = 0.0
    # W_NORMSDICT['ZTT'] = 0.0
    # W_NORMSDICT['ZL'] = 0.0
    # W_NORMSDICT['ZJ'] = 0.0
    # W_NORMSDICT['TT'] = 0.0
    # W_NORMSDICT['VV'] = 0.0
    #
    # ##############################
    # # this will hold the W norm
    # # derived by comparing the inclusive
    # # selections in default and high mT
    # WNORM = {}
    #
    # for addFile in range(0,len(FOR_W_NORM)):
    #     if str(CHANNELS[chan]) in str(FOR_W_NORM[addFile]):
    #         GOTFILE = TFile(FOR_W_NORM[addFile],'READ')
    #         print '*** summing QCD norm histograms from ', FOR_W_NORM[addFile]
    #
    #         DIRNAME = CHANNELS[chan]+"_inclusive"
    #         for key, value in W_NORMSDICT.iteritems():
    #             LOCALNAME = DIRNAME+"/"+key
    #             print "--> ",LOCALNAME
    #             GOTHIST = GOTFILE.Get(LOCALNAME)
    #             if(GOTHIST):
    #                 W_NORMSDICT[key] = value + GOTHIST.GetSumOfWeights()
    #             else:
    #                 print 'WARNING FAILED TO FIND :', key
    #
    # ################################
    # # figure out normalization SFs
    # WNORM[CHANNELS[chan]] =  1.0 * (W_NORMSDICT['data_obs']-
    #                             W_NORMSDICT['ZTT'] -
    #                             W_NORMSDICT['ZL'] -
    #                             W_NORMSDICT['ZJ'] -
    #                             W_NORMSDICT['TT'] -
    #                             W_NORMSDICT['VV'])
    #
    # print 'in channel ',CHANNELS[chan], 'bkg sub. high mT data is ', WNORM[CHANNELS[chan]]
    # print 'the raw low mT estimate was ', HISTOGRAM_DICTIONARY[(CHANNELS[chan]+'_inclusive/W')].GetSumOfWeights()
    # WNORM[CHANNELS[chan]] = WNORM[CHANNELS[chan]]/HISTOGRAM_DICTIONARY[(CHANNELS[chan]+'_inclusive/W')].GetSumOfWeights()
    # print 'the final norm. factor to be applied to all W templates is ', WNORM[CHANNELS[chan]]
    #
    # print 'applying W normalizaton ...'
    # for key, value in HISTOGRAM_DICTIONARY.iteritems():
    #     if 'W' in str(key):
    #         HISTOGRAM_DICTIONARY[key].Scale(WNORM[CHANNELS[chan]])
    #
    ################################
    # print event totals by sub-channel

    BTAG_TOTALSDICT = {}
    BTAG_TOTALSDICT['data_obs'] = 0.0
    BTAG_TOTALSDICT['QCD'] = 0.0
    BTAG_TOTALSDICT['W'] = 0.0
    BTAG_TOTALSDICT['ZTT'] = 0.0
    BTAG_TOTALSDICT['ZL'] = 0.0
    BTAG_TOTALSDICT['ZJ'] = 0.0
    BTAG_TOTALSDICT['TT'] = 0.0
    BTAG_TOTALSDICT['VV'] = 0.0

    NONBTAG_TOTALSDICT = {}
    NONBTAG_TOTALSDICT['data_obs'] = 0.0
    NONBTAG_TOTALSDICT['QCD'] = 0.0
    NONBTAG_TOTALSDICT['W'] = 0.0
    NONBTAG_TOTALSDICT['ZTT'] = 0.0
    NONBTAG_TOTALSDICT['ZL'] = 0.0
    NONBTAG_TOTALSDICT['ZJ'] = 0.0
    NONBTAG_TOTALSDICT['TT'] = 0.0
    NONBTAG_TOTALSDICT['VV'] = 0.0


    for direc in range(0,len(DIRLIST)):
        DIRNAME = CHANNELS[chan]+"_"+DIRLIST[direc]

        # print '*************************************************************'
        # print '*        Event Totals for ', DIRNAME
        # print '*************************************************************'

        TOTALSDICT = {}
        TOTALSDICT['data_obs'] = 0.0
        TOTALSDICT['QCD'] = 0.0
        TOTALSDICT['W'] = 0.0
        TOTALSDICT['ZTT'] = 0.0
        TOTALSDICT['ZL'] = 0.0
        TOTALSDICT['ZJ'] = 0.0
        TOTALSDICT['TT'] = 0.0
        TOTALSDICT['VV'] = 0.0

        for key, value in TOTALSDICT.iteritems():
                bigkey = DIRNAME+'/'+key
                TOTALSDICT[key] = HISTOGRAM_DICTIONARY[bigkey].GetSumOfWeights()
                if '_btag' in str(DIRNAME):
                    BTAG_TOTALSDICT[key] += HISTOGRAM_DICTIONARY[bigkey].GetSumOfWeights()
                if '_nobtag' in str(DIRNAME):
                    NONBTAG_TOTALSDICT[key] += HISTOGRAM_DICTIONARY[bigkey].GetSumOfWeights()

        print DIRNAME, TOTALSDICT

    print '*************************************************************'
    print '*        Event Totals for BTAG ', CHANNELS[chan]
    print '*************************************************************'

    print 'data_obs ', BTAG_TOTALSDICT['data_obs']
    print 'QCD ',  BTAG_TOTALSDICT['QCD']
    print 'W + jets ',  BTAG_TOTALSDICT['W']
    print 'Z->TT ',  BTAG_TOTALSDICT['ZTT']
    print 'Z->ll ', BTAG_TOTALSDICT['ZL'] + BTAG_TOTALSDICT['ZJ']
    print 'tt + single-t ', BTAG_TOTALSDICT['TT']
    print 'diboson ', BTAG_TOTALSDICT['VV']


    print '*************************************************************'
    print '*        Event Totals for NONBTAG ', CHANNELS[chan]
    print '*************************************************************'

    print 'data_obs ', NONBTAG_TOTALSDICT['data_obs']
    print 'QCD ',  NONBTAG_TOTALSDICT['QCD']
    print 'W + jets ',  NONBTAG_TOTALSDICT['W']
    print 'Z->TT ',  NONBTAG_TOTALSDICT['ZTT']
    print 'Z->ll ', NONBTAG_TOTALSDICT['ZL'] + NONBTAG_TOTALSDICT['ZJ']
    print 'tt + single-t ', NONBTAG_TOTALSDICT['TT']
    print 'diboson ', NONBTAG_TOTALSDICT['VV']




    ##################################
    # finally save all the histograms


    for key, value in HISTOGRAM_DICTIONARY.iteritems():
        SPLITNAME=key.split('/')
        #if SPLITNAME[0]=='muTau_btag_low':
        #    print SPLITNAME[0], SPLITNAME[1]
        NEWFILE.cd(SPLITNAME[0])
        HISTOGRAM_DICTIONARY[key].Write(SPLITNAME[1])

        #NEWFILE.Close()
    #
    #     #
    #     #
    #     #
    #     # if 'fine_binning' in sampleType[sampleIndx]:
    #     #   histogram_dict[histName] = TH1F(histName,sampleTitle[sampleIndx],400,0,2000)
    #     # else:
    #     #   if 'nobtag' in dataCardCategories[dictIndx] or 'inclusive' in dataCardCategories[dictIndx]:
    #     #     histogram_dict[histName] = TH1F(histName,sampleTitle[sampleIndx],len(binning_nominal_nobtag)-1,array('d',binning_nominal_nobtag))
    #     #   else:
    #     #     histogram_dict[histName] = TH1F(histName,sampleTitle[sampleIndx],len(binning_nominal_btag)-1,array('d',binning_nominal_btag))
    #     # histogram_dict[histName].Sumw2()
