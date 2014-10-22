{

TFile *_file0 = TFile::Open("../testCombined.root");
TTree * FlatTree = (_file0).Get("TauEsNominal/FlatTuple");
FlatTree->MakeSelector("FlatTreeSel");
gROOT->ProcessLine(Form(".! sed -i -e 's/return kTRUE\;/fChain->GetTree\(\)->GetEntry\(entry\)\; return kTRUE\;/g' FlatTreeSel.C"));


}
