{

TFile *_file0 = TFile::Open("/uscms/home/shalhout/no_backup/NEWSKIM/VBFHToTauTauM125_v9FlatTuple/FlatTuple_22_1_1Nq_skimmed.root");
TTree * FlatTree = (_file0).Get("TauEsNominal/FlatTuple");
FlatTree->MakeSelector("FlatTreeSel");
gROOT->ProcessLine(Form(".! sed -i -e 's/return kTRUE\;/fChain->GetTree\(\)->GetEntry\(entry\)\; return kTRUE\;/g' FlatTreeSel.C"));


}
