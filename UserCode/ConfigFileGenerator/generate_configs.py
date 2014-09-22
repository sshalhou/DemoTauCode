#!/usr/bin/python

import sys
import os
import re



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

    # get list of T2/T3 sites hosting the data

    WhiteListCommand=BaseCommand
    WhiteListCommand+="site dataset="
    WhiteListCommand+=interested_in
    WhiteListCommand+="\" --verbose=1 | egrep \"T2|T3\" | awk \'{printf $1\" \"}\'"
    getWhiteList = os.popen(WhiteListCommand)
    whiteList = getWhiteList.read()
    print "list = ", whiteList

    # get basic info

    SummaryCommand=BaseCommand
    SummaryCommand+="summary dataset="
    SummaryCommand+=interested_in
    SummaryCommand+="\" --verbose=1 "
    getSummary = os.popen(SummaryCommand)
    summary = getSummary.read()
    summarySplit = re.split(' |\n',summary)
    nfiles = summarySplit[18]
    nevents  = summarySplit[22]
    nblocks = summarySplit[26]
    nlumis = summarySplit[31]
    file_size = summarySplit[33]
    print "nfiles, nevents, nblocks, nlumis, file_size = ", nfiles, nevents, nblocks, nlumis, file_size

    # get the dataType mc or data
    TypeCommand=BaseCommand
    TypeCommand+="datatype dataset="
    TypeCommand+=interested_in
    TypeCommand+="\" --verbose=1 | egrep \"mc|data\""
    getType = os.popen(TypeCommand)
    type = getType.read()
    print "type = ", type
