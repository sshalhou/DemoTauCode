//g++ -I `root-config --incdir` -o skimFlatTuple.o skimFlatTuple.cpp `root-config --libs`

#include "TChain.h"
#include "TTree.h"
#include <string>
#include <cstring>
#include "TSelector.h"
#include "TObject.h"
#include <iostream>
#include <fstream>

#include "TFile.h"
#include "Branches.h"
#include "Filter.h"


using namespace std;

int main(int argc, char* argv[])
{

	/////////////
	// read in list of files to process

	std::cout<<" reading in files from "<<argv[1]<<std::endl;
	ifstream myfile(argv[1]);
	string line;
	vector <string> afile;




	if (myfile.is_open())
		{
			while(getline (myfile,line))
				{
					cout << line << '\n';
					afile.push_back(line);
				}
				myfile.close();
			}

			else cout << "Unable to open file, please supply name of text file as argument";





			for(size_t i=0; i<afile.size();++i)
				{



					TChain * chain1 = new TChain("TauEsNominal/FlatTuple");
					TChain * chain2 = new TChain("TauEsUp/FlatTuple");
					TChain * chain3 = new TChain("TauEsDown/FlatTuple");




					chain1->AddFile(afile[i].c_str(),0,"TauEsNominal/FlatTuple");
					chain2->AddFile(afile[i].c_str(),0,"TauEsUp/FlatTuple");
					chain3->AddFile(afile[i].c_str(),0,"TauEsDown/FlatTuple");

					unsigned int start = afile[i].rfind('.');
					unsigned int end = afile[i].rfind('/');
					string FileName = afile[i].substr(end+1,start-end-1);
					FileName = FileName+"_skimmed.root";
					std::cout<<FileName<<std::endl;




					TFile X(FileName.c_str(),"RECREATE");

					Long64_t maxEntries1 = chain1->GetEntries();
					Long64_t maxEntries2 = chain2->GetEntries();
					Long64_t maxEntries3 = chain3->GetEntries();



					TChain* outputChain1 = (maxEntries1>0) ? (TChain*)chain1->CloneTree(0) : 0;
					TChain* outputChain2 = (maxEntries2>0) ? (TChain*)chain2->CloneTree(0) : 0;
					TChain* outputChain3 = (maxEntries3>0) ? (TChain*)chain3->CloneTree(0) : 0;



					TTree* outputTree1 = (maxEntries1>0) ? outputChain1->GetTree() : 0;
					TTree* outputTree2 = (maxEntries2>0) ? outputChain2->GetTree() : 0;
					TTree* outputTree3 = (maxEntries3>0) ? outputChain3->GetTree() : 0;




					if(maxEntries1>0)
						{
							Init(chain1);
							int nfilled = 0;

							for (long entry = 0; entry < maxEntries1; ++entry)
								{
									Long64_t entryNumber = chain1->GetEntryNumber(entry);
									Long64_t localEntry = chain1->LoadTree(entryNumber);
									if (localEntry < 0) continue;

									if(entry%2500 == 0) std::cout<<"tauEsNominal "<<entry<<" of "<<maxEntries1<<" of "<<FileName<<" ";
									if(entry%2500 == 0) std::cout<<"filled "<<nfilled<<" of "<<entry<<" \n";


									chain1->GetEntry(chain1->GetChainEntryNumber(entry));
									if(passesMuTauOrETau(chain1)){ nfilled++; outputTree1->Fill();}



								}
							}

			if(maxEntries2>0){
				Init(chain2);
				int nfilled = 0;


				for (long entry = 0; entry < maxEntries2; ++entry)
					{
						Long64_t entryNumber = chain2->GetEntryNumber(entry);
						Long64_t localEntry = chain2->LoadTree(entryNumber);
						if (localEntry < 0) continue;

						if(entry%2500 == 0) std::cout<<"tauEsUp "<<entry<<" of "<<maxEntries2<<" of "<<FileName<<" ";
						if(entry%2500 == 0) std::cout<<"filled "<<nfilled<<" of "<<entry<<" \n";


						chain2->GetEntry(chain2->GetChainEntryNumber(entry));
						if(passesMuTauOrETau(chain2)) {nfilled++;outputTree2->Fill();}




					}
				}


			if(maxEntries3>0)
				{


					Init(chain3);
					int nfilled = 0;

					for (long entry = 0; entry < maxEntries3; ++entry)
						{
							Long64_t entryNumber = chain3->GetEntryNumber(entry);
							Long64_t localEntry = chain3->LoadTree(entryNumber);
							if (localEntry < 0) continue;

							if(entry%2500 == 0) std::cout<<"tauEsDown "<<entry<<" of "<<maxEntries3<<" of "<<FileName<<" ";
							if(entry%2500 == 0) std::cout<<"filled "<<nfilled<<" of "<<entry<<" \n";


							chain3->GetEntry(chain3->GetChainEntryNumber(entry));
							if(passesMuTauOrETau(chain3)) {nfilled++;outputTree3->Fill();}


						}
					}

				X.cd();
				X.mkdir("TauEsNominal");
				X.mkdir("TauEsUp");
				X.mkdir("TauEsDown");


				if(maxEntries1>0) {X.cd("TauEsNominal"); outputTree1->Write("FlatTuple");}
				if(maxEntries2>0) {X.cd("TauEsUp"); outputTree2->Write("FlatTuple");}
				if(maxEntries3>0) {X.cd("TauEsDown"); outputTree3->Write("FlatTuple");}
				X.Close();

				delete chain1;
				delete chain2;
				delete chain3;



			} // loop over files
}
