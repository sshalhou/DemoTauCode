import sys
import os
import re

my_file = open(sys.argv[1], 'r')

header = "import FWCore.ParameterSet.Config as cms"
header = header + "\n" +"myfilelist = cms.untracked.vstring()" + "\n"

for line in my_file:
	line = line.rstrip('\n')
	DirNameCommand = "ls "+line+"/"
	#getDirName = os.popen(DirNameCommand)
	#DirName = getDirName.read()
	#print "DirName = ", DirName, os.path.basename(line.rstrip('\n'))
	DirName = os.path.basename(line.rstrip('\n'))
	FileListName = DirName.rstrip('\n') + "LIST.py"
	configName = "FlatTuple_"+DirName.rstrip('\n')+".py"
	print "will create : ", configName, " using list of files called ", FileListName
	rmCommand = "rm -rf "+os.environ['CMSSW_BASE']+"/src/UserCode/FileLists/python/"+FileListName
	os.system(rmCommand)
	f = open(FileListName, 'w')
	print >> f, header
	NTUPLISTCOMMAND = DirNameCommand+"*/*root"
	getNtupleListCommand = os.popen(NTUPLISTCOMMAND)
	Files = getNtupleListCommand.read()
	AllFiles = Files.split('\n')
	for x in range(0,len(AllFiles)-1):
		currentFile = "myfilelist.extend([\x27file:"+AllFiles[x]+"\x27])"
		print >> f, currentFile
	CatCommand = "cat "+os.environ['CMSSW_BASE']+"/src/UserCode/FlatTuple/GenerateFileLists/flattree_GENERAL.py"

	CatCommandNominal = CatCommand + "| sed \x27s/FILELISTNAME/"+FileListName.rstrip('.py')+"/g\x27"
	CatCommandNominal = CatCommandNominal + "| sed \x27s/FILEOUTNAME/"+DirName.rstrip('\n')+"/g\x27"


	rmCommand = "rm -rf "+configName
	os.system(rmCommand)
	CatCommandNominal = CatCommandNominal + " >> " + configName
	os.system(CatCommandNominal)


	mvCommand = "mv "+FileListName+" "+os.environ['CMSSW_BASE']+"/src/UserCode/FileLists/python/."
	os.system(mvCommand)
	f.close()


rmCommand = "rm -rf "+os.environ['CMSSW_BASE']+"/src/FileLists"
os.system(rmCommand)
cpCommand = "cp -r "+os.environ['CMSSW_BASE']+"/src/UserCode/FileLists"+" "+os.environ['CMSSW_BASE']+"/src/FileLists"
os.system(cpCommand)
