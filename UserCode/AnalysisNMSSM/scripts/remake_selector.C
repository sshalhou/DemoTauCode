{

//TFile *_file0 = TFile::Open("../HOLDER/Signal25_FlatTuple_10_1_wrN_skimmed.root");
TFile *_file0 = TFile::Open("~/no_backup/NEWSKIMV10/ZTauTauEmbeddedETauA_FlatTupeV10/FlatTuple_1_1_0VF_skimmed.root");
TTree * FlatTree = (_file0).Get("TauEsNominal/FlatTuple");
FlatTree->MakeSelector("FlatTreeSel");
gROOT->ProcessLine(Form(".! sed -i -e 's/return kTRUE\;/fChain->GetTree\(\)->GetEntry\(entry\)\; return kTRUE\;/g' FlatTreeSel.C"));


}
