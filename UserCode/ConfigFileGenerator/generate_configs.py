#!/usr/bin/python

import sys


if len(sys.argv) is 2:
  print "------------------------"
  print "Will generate crab and config files for sample :"
  print sys.argv[1]
  print "------------------------\n"

else:
  print "usage : python generate_configs.py <full sample name>"
  print " for example : python generate_configs.py /WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM"
  sys.exit()


import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()

#for child in root:
#  print child.tag, child.attrib

interested_in = str(sys.argv[1])

for element in tree.iterfind('Sample[@SampleName="/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM"]'):
  SampleName = element.get("SampleName")
  PhysicsProcess = element.get("PhysicsProcess")
  CrossSection = element.get("CrossSection")
  Mass = element.get("Mass")
  isNonTopEmbeddedSample = element.get("isNonTopEmbeddedSample")
  isTopEmbeddedSample = element.get("isTopEmbeddedSample")
  runOnMC = element.get("runOnMC")
  Events = element.get("Events")
  Files = element.get("Files")
  SizeTB = element.get("SizeTB")
  print "Mass = ", Mass
  print "SizeTB = ", SizeTB

from subprocess import call
call(['./das_client.py','--query="file dataset=/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM" --verbose=1'])
