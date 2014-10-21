import sys
import os
import re

my_file = open(sys.argv[1], 'r')

header = "import FWCore.ParameterSet.Config as cms"
header = header + "\n" +"myfilelist = cms.untracked.vstring()" + "\n"

for line in my_file:
	line = line.rstrip('\n')
	DirNameCommand = "ls "+line+"/"
	getDirName = os.popen(DirNameCommand)
	DirName = getDirName.read()
	FileListName = DirName.rstrip('\n') + "LIST.py"
	rmCommand = "rm -rf "+FileListName
	os.system(rmCommand)
	f = open(FileListName, 'w')
	print >> f, header
	NTUPLISTCOMMAND = DirNameCommand+"*/*/*root"
	getNtupleListCommand = os.popen(NTUPLISTCOMMAND)
	Files = getNtupleListCommand.read()
	AllFiles = Files.split('\n')
	for x in range(0,len(AllFiles)-1):
		currentFile = "myfilelist.extend([\x27file:"+AllFiles[x]+"\x27])"
		print >> f, currentFile
	CatCommand = "cat "+os.environ['CMSSW_BASE']+"/src/UserCode/FlatTuple/GenerateFileLists/flattree_GENERAL.py"
	CatCommandNominal = CatCommand + "| sed \x27s/SHIFT/Nominal/g\x27"
	CatCommandUp = CatCommand + "| sed \x27s/SHIFT/Up/g\x27"
	CatCommandDown = CatCommand + "| sed \x27s/SHIFT/Down/g\x27"
	os.system(CatCommand)
	f.close()
