#!/usr/bin/python

import sys
import os


if len(sys.argv) is 2:
  print "------------------------"
  print "Will generate crab and config files for sample :"
  print sys.argv[1]
  print "------------------------\n"

else:
  print "usage : python generate_configs.py <full sample name>"
  print " for example : python generate_configs.py /WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM"
  sys.exit()


fileNameXML=os.environ['CMSSW_BASE']+"/src/UserCode/ConfigFileGenerator/test.xml"
print fileNameXML



import xml.etree.ElementTree as ET
tree = ET.parse(fileNameXML)
root = tree.getroot()


interested_in = str(sys.argv[1])

for element in root.findall('Sample'):
  SampleName = element.get("SampleName")
  if interested_in == SampleName:
    PhysicsProcess = element.get("PhysicsProcess")
    CrossSection = element.get("CrossSection")
    Mass = element.get("Mass")
    isNonTopEmbeddedSample = element.get("isNonTopEmbeddedSample")
    isTopEmbeddedSample = element.get("isTopEmbeddedSample")
    runOnMC = element.get("runOnMC")

    BaseCommand=os.environ['CMSSW_BASE']+"/src/UserCode/ConfigFileGenerator/das_client.py --query=\""



    WhiteListCommand=BaseCommand
    WhiteListCommand+="site dataset="
    WhiteListCommand+=interested_in
    WhiteListCommand+="\" --verbose=1 | egrep \"T2|T3\" | awk \'{printf $1\" \"}\'"
    getWhiteList = os.popen(WhiteListCommand)
    whiteList = getWhiteList.read()
    print "list = ", whiteList

    SummaryCommand=BaseCommand
    SummaryCommand+="summary dataset="
    SummaryCommand+=interested_in

    nFilesCommand = SummaryCommand+"\" --verbose=1 | grep nfiles | awk \'{ print $3 }\'"
    getNfiles = os.popen(nFilesCommand)
    nfiles = getNfiles.read()
    print "nfiles = ", nfiles
