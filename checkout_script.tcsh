#!/bin/tcsh

echo "checking out basic stuff : "

################################################
git cms-addpkg DataFormats/MuonReco
git cms-addpkg DataFormats/PatCandidates
git cms-addpkg DataFormats/TauReco
git cms-addpkg FWCore/Version
git cms-addpkg PhysicsTools/PatAlgos
git cms-addpkg PhysicsTools/PatExamples
git cms-addpkg RecoTauTag/RecoTau
git cms-addpkg EgammaAnalysis/ElectronTools
git cms-addpkg PhysicsTools/Utilities
git cms-addpkg SimDataFormats/PileupSummaryInfo
git cms-addpkg RecoTauTag/Configuration
git cms-addpkg DataFormats/VertexReco
git cms-addpkg DataFormats/Common
git cms-addpkg CondFormats/JetMETObjects
git cms-addpkg CommonTools/UtilAlgos
################################################

echo "soft link to UserCode "
################################################
ln -s ../../UserCode UserCode
################################################

echo "some needed Fixes "
################################################
git cms-merge-topic cms-analysis-tools:5_3_14-updateSelectorUtils
git cms-merge-topic cms-analysis-tools:5_3_13_patch2-testNewTau
git cms-merge-topic -u TaiSakuma:53X-met-131120-01
git cms-merge-topic -u cms-met:53X-MVaNoPuMET-20131217-01
################################################

echo "checking out SVFit code : "

################################################
wget --no-check-certificate https://github.com/cms-analysis/TauAnalysis-CandidateTools/archive/TauAnalysis-CandidateTools-V00-02-03s.tar.gz .
tar -xzvf TauAnalysis-CandidateTools-V00-02-03s
mkdir TauAnalysis
mv TauAnalysis-CandidateTools-TauAnalysis-CandidateTools-V00-02-03s TauAnalysis/CandidateTools
rm -rf TauAnalysis-CandidateTools-V00-02-03s
################################################

echo "checking out MET Recoil Correction Code : "

################################################
wget http://web.mit.edu/~pcharris/www/RecoilCorrector_v7.tgz RecoilCorrector_v7.tgz
tar -xzvf RecoilCorrector_v7.tgz
mv RecoilCorrector_v7/recoilfits UserCode/RecoilCorrector/recoilfits
rm -rf RecoilCorrector_v7
rm -rf RecoilCorrector_v7.tgz
################################################

echo "checking out Electron MVA Code : "
################################################
cd EgammaAnalysis/ElectronTools/data/
cat download.url | xargs wget
cd -
################################################

echo "checking out improved Tau ID : "
################################################
git cms-merge-topic -u cms-tau-pog:CMSSW_5_3_X_boostedTaus_2013Dec17
################################################

echo "copying MVA PF MET code from Phil Harris : "
################################################
cp -r /uscms/home/shalhout/public/RecoMET .
#mkdir $CMSSW_BASE/src/RecoMET
#cp -r  /afs/cern.ch/work/p/pharris/public/tmp/CMSSW_5_3_13/src/RecoMET .
#cp /afs/cern.ch/work/p/pharris/public/tmp/CMSSW_5_3_13/src/RecoMET/METPUSubtraction/python/mvaPFMET_leptons_cff.py
#$CMSSW_BASE/src/RecoMET/METPUSubtraction/python/.
#cp /afs/cern.ch/user/p/pharris/public/MVAMetUpdate/*Sep*.root $CMSSW_BASE/src/RecoMET/METPUSubtraction/data/
################################################


#echo "Get The Correct Version of DataFormats/JetReco for use with MVA MET"
################################################
#rm -rf DataFormats/JetReco
#git clone https://github.com/cms-cvs-history/DataFormats-JetReco DataFormats/JetReco
################################################


#echo "Get The Correct Version of DataFormats/METReco for use with MVA MET"
################################################
#rm -rf DataFormats/METReco
#git clone https://github.com/cms-cvs-history/DataFormats-METReco DataFormats/METReco
################################################


#echo "Get The Correct Version of RecoJets-JetProducers"
################################################
#rm -rf RecoJets/JetProducers
#git clone https://github.com/cms-cvs-history/RecoJets-JetProducers RecoJets/JetProducers
################################################


#echo "Get The Correct Version of CommonTools-Utils"
################################################
#rm -rf CommonTools/Utils
#git clone https://github.com/cms-cvs-history/CommonTools-Utils CommonTools/Utils
################################################


#echo "Get The Correct Version of FWCore-Utilities"
################################################
#rm -rf FWCore/Utilities
#git clone https://github.com/cms-cvs-history/FWCore-Utilities FWCore/Utilities
################################################
