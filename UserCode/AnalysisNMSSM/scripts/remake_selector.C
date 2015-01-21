{

//TFile *_file0 = TFile::Open("../HOLDER/Signal25_FlatTuple_10_1_wrN_skimmed.root");
TFile *_file0 = TFile::Open("~/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_11_1_S7e_skimmed.root");
TTree * FlatTree = (_file0).Get("TauEsNominal/FlatTuple");
FlatTree->MakeSelector("FlatTreeSel");
gROOT->ProcessLine(Form(".! sed -i -e 's/return kTRUE\;/fChain->GetTree\(\)->GetEntry\(entry\)\; return kTRUE\;/g' FlatTreeSel.C"));


}
