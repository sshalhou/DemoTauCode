#!/bin/tcsh


echo "checking out improved Tau ID : "
################################################
git cms-merge-topic -u cms-tau-pog:CMSSW_5_3_X_boostedTaus_2013Dec17
#git cms-merge-topic -u cms-tau-pog:CMSSW_5_3_X_tauID2014
################################################

echo "soft link to UserCode "
################################################
ln -s ../../UserCode UserCode
################################################


echo "checking out SVFit code : "

################################################
wget --no-check-certificate https://github.com/cms-analysis/TauAnalysis-CandidateTools/archive/TauAnalysis-CandidateTools-V00-02-03s.tar.gz .
tar -xzvf TauAnalysis-CandidateTools-V00-02-03s
mkdir TauAnalysis
rm -rf TauAnalysis/CandidateTools
mv TauAnalysis-CandidateTools-TauAnalysis-CandidateTools-V00-02-03s TauAnalysis/CandidateTools
rm -rf TauAnalysis-CandidateTools-V00-02-03s
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


echo "checking out MET Recoil Correction Code : "

################################################
wget http://web.mit.edu/~pcharris/www/RecoilCorrector_v7.tgz RecoilCorrector_v7.tgz
tar -xzvf RecoilCorrector_v7.tgz
rm -rf UserCode/RecoilCorrector/recoilfits
mv RecoilCorrector_v7/recoilfits UserCode/RecoilCorrector/recoilfits
cp /uscms/home/shalhout/public/LLR_recoilfits/*RR*.root UserCode/RecoilCorrector/recoilfits/.
cp /uscms/home/shalhout/public/53_Dec2012/*root ./RecoMET/METPUSubtraction/data/.
rm -rf RecoilCorrector_v7
rm -rf RecoilCorrector_v7.tgz
################################################

echo "checking out Electron MVA Code : "
################################################
git cms-addpkg EgammaAnalysis/ElectronTools
cd EgammaAnalysis/ElectronTools/data/
cat download.url | xargs wget
cd -
################################################



echo "soft link MVA MET leptons PAT config :"
################################################
cd RecoMET/METPUSubtraction/python/
ln -s ../../../UserCode/mvaPFMET_leptons_PAT_cfi.py mvaPFMET_leptons_PAT_cfi.py
cd -
################################################

echo " copy pile up jet ID configs "
################################################
rm -rf RecoJets
cp -r /uscms/home/shalhout/public/RecoJets .
rm -rf DataFormats/JetReco
cp -r /uscms/home/shalhout/public/JetReco_v2 DataFormats/JetReco
rm -rf DataFormats/METReco
cp -r /uscms/home/shalhout/public/METReco_v2 DataFormats/METReco
cp -r /uscms/home/shalhout/public/SelectorUtils PhysicsTools/.
cp -r /uscms/home/shalhout/public/PhysicsTools_Utilities PhysicsTools/Utilities
cp -r /uscms/home/shalhout/public/TauSpinnerInterface TauSpinnerInterface
cp /uscms/home/shalhout/public/mvaPFMEt_53_Dec2012.db RecoMET/METPUSubtraction/data/.
################################################

ehco "getting pile-up correction root files "
####################################################

mkdir UserCode/PileUpReWeightFiles
cp /afs/cern.ch/user/a/agilbert/public/HTT_Pileup/13-09-13/MC_Summer12_PU_S10-600bins.root UserCode/PileUpReWeightFiles/.
cp /afs/cern.ch/user/a/agilbert/public/HTT_Pileup/13-09-13/Data_Pileup_2012_ReRecoPixel-600bins.root UserCode/PileUpReWeightFiles/.
####################################################

echo "setting up JEC and uncertainty "
################################################
git cms-addpkg JetMETCorrections/Modules
cp JetMETCorrections/Modules/test/JetCorrectionDBReader_cfg.py RecoJets/JetAnalyzers/test/.
sed -i 's/string(\x27AK5PF\x27)/string(\x27AK5PFchs\x27)/g' RecoJets/JetAnalyzers/test/JetCorrectionDBReader_cfg.py
cd RecoJets/JetAnalyzers/test/

echo "running JEC DB file pull for MC under START53_V23 : "
sed -i 's/GR_R_42_V19/START53_V23/g' JetCorrectionDBReader_cfg.py
cmsRun JetCorrectionDBReader_cfg.py

echo "running JEC DB file pull for DATA under START53_V23 : "
sed -i 's/START53_V23/FT_53_V21_AN4/g' JetCorrectionDBReader_cfg.py
cmsRun JetCorrectionDBReader_cfg.py
cd -
################################################
