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
	configNominalName = "nominalTauEsFlatTuple_"+DirName.rstrip('\n')+".py"
	configDownName = "downTauEsFlatTuple_"+DirName.rstrip('\n')+".py"
	configUpName = "upTauEsFlatTuple_"+DirName.rstrip('\n')+".py"
	print "will create : ", configDownName, configNominalName, configUpName
	rmCommand = "rm -rf "+os.environ['CMSSW_BASE']+"/src/UserCode/FileLists/python/"+FileListName
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

	CatCommandNominal = CatCommand + "| sed \x27s/SHIFT/Nominal/g\x27" + "| sed \x27s/FILELISTNAME/"+FileListName+"/g\x27"
	CatCommandUp = CatCommand + "| sed \x27s/SHIFT/Up/g\x27"  + "| sed \x27s/FILELISTNAME/"+FileListName+"/g\x27"
	CatCommandDown = CatCommand + "| sed \x27s/SHIFT/Down/g\x27"  + "| sed \x27s/FILELISTNAME/"+FileListName+"/g\x27"

	CatCommandNominal = CatCommandNominal + "| sed \x27s/FILEOUTNAME/"+DirName.rstrip('\n')+"/g\x27"
	CatCommandUp = CatCommandUp + "| sed \x27s/FILEOUTNAME/"+DirName.rstrip('\n')+"/g\x27"
	CatCommandDown = CatCommandDown + "| sed \x27s/FILEOUTNAME/"+DirName.rstrip('\n')+"/g\x27"

	configNameNominal = "FlatTuple_"+DirName.rstrip('\n')+"_TauEsNominal.py"
	rmCommand = "rm -rf "+configNameNominal
	os.system(rmCommand)
	CatCommandNominal = CatCommandNominal + " >> " + configNameNominal

	configNameUp = "FlatTuple_"+DirName.rstrip('\n')+"_TauEsUp.py"
	rmCommand = "rm -rf "+configNameUp
	os.system(rmCommand)
	CatCommandUp = CatCommandUp + " >> " + configNameUp

	configNameDown = "FlatTuple_"+DirName.rstrip('\n')+"_TauEsDown.py"
	rmCommand = "rm -rf "+configNameDown
	os.system(rmCommand)
	CatCommandDown = CatCommandDown + " >> " + configNameDown

	os.system(CatCommandNominal)
	os.system(CatCommandUp)
	os.system(CatCommandDown)

	mvCommand = "mv "+FileListName+" "+os.environ['CMSSW_BASE']+"/src/UserCode/FileLists/python/."
	os.system(mvCommand)

	f.close()
