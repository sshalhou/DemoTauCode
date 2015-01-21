{

//TFile *_file0 = TFile::Open("/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_22_1_1Nq_skimmed.root");
TFile *_file0 = TFile::Open("~/no_backup/NEWSKIMV9X/nMSSM_bba1tautaum80_FLATv9Xntup/FlatTuple_11_1_S7e_skimmed.root");
TTree * FlatTree = (_file0).Get("TauEsNominal/FlatTuple");
FlatTree->MakeSelector("FlatTreeSel");
gROOT->ProcessLine(Form(".! sed -i -e 's/return kTRUE\;/fChain->GetTree\(\)->GetEntry\(entry\)\; return kTRUE\;/g' FlatTreeSel.C"));


}
