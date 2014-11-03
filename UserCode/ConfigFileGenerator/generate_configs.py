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
  print "usage : python UserCode/ConfigFileGenerator/generate_configs.py <full sample name>"
  print " for example : python generate_configs.py /WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM"
  sys.exit()


###############
# prepare crab job directory to keep CMSSW_BASE/src from
# getting out of hand

shortDate = "date | awk \'{printf $2$3$6}\'"
getShortDate = os.popen(shortDate)
shortDate = getShortDate.read()

crabJobLocation = os.environ['CMSSW_BASE']+"/src/CRAB_JOBS"

if os.path.isdir(crabJobLocation) is False:
  makeCrabDir = "mkdir "+crabJobLocation
  os.system(makeCrabDir)

crabJobLocation += "/"+ shortDate

if os.path.isdir(crabJobLocation) is False:
  makeCrabDir = "mkdir "+crabJobLocation
  os.system(makeCrabDir)

print "generated crab files will reside in ", crabJobLocation


fileNameXML=os.environ['CMSSW_BASE']+"/src/UserCode/ConfigFileGenerator/testSig.xml"
print fileNameXML



import xml.etree.ElementTree as ET
tree = ET.parse(fileNameXML)
root = tree.getroot()


interested_in = str(sys.argv[1])

for element in root.findall('Sample'):
  SampleName = element.get("SampleName")
  if interested_in == SampleName:
    PhysicsProcess = element.get("PhysicsProcess")
    crossSection = element.get("CrossSection")
    Mass = element.get("Mass")
    isNonTopEmbeddedSample = element.get("isNonTopEmbeddedSample")
    isTopEmbeddedSample = element.get("isTopEmbeddedSample")
    runOnMC = element.get("runOnMC")
    OneWordName=element.get("OneWordName")


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
    # note: this is not used to set runOnMC, but
    # only to decide if we need a lumi_mask or not
    TypeCommand=BaseCommand
    TypeCommand+="datatype dataset="
    TypeCommand+=interested_in
    TypeCommand+="\" --verbose=1 | egrep \"mc|data\""
    getType = os.popen(TypeCommand)
    type = getType.read()
    type = type.rstrip('\n')
    print "type = ", type

    # update values in the xml file, careful it will be overwritten
    element.set('Files', str(nfiles))
    element.set('Events', str(nevents))
    element.set('Nblocks', str(nblocks))
    element.set('Nlumis', str(nlumis))
    element.set('Size', str(file_size))
    element.set('Type', str(type))
    element.set('WhiteList', str(whiteList))
    tree.write(fileNameXML)


    # create mc patTuple and crab files
    DateCommand = os.popen('date')
    dateSuffix = DateCommand.read()
    dateSuffix = dateSuffix.replace(" ","")
    dateSuffix = dateSuffix.replace(":","")
    dateSuffix = dateSuffix.rstrip('\n')

    patTupleConfigName = crabJobLocation+"/PAT_"+OneWordName+"_"+dateSuffix+".py"
    crabConfigName = crabJobLocation+"/crab_"+OneWordName+"_"+dateSuffix+".cfg"
    print "creating a patTupleConfigFile called = ", patTupleConfigName

    CatCommand = "cat "+os.environ['CMSSW_BASE']+"/src/UserCode/ConfigFileGenerator/v8/PAT_template.py"
    CatCommand += ">> "+ patTupleConfigName
    os.system(CatCommand)

    print "creating a crab cfg called = ", crabConfigName

    crabCatCommand = "cat "+os.environ['CMSSW_BASE']+"/src/UserCode/ConfigFileGenerator/v8/crab_template.cfg"
    crabCatCommand += ">> "+ crabConfigName
    os.system(crabCatCommand)



    # set parameters specific to the requested dataset
    # in the patTuple job config file

    writeBR = "sed -i \'s/DUMMY_branchingFraction/"+"999.0"+"/g\'"+" "+patTupleConfigName
    os.system(writeBR)

    writeSampleName = "sed -i \'s/DUMMY_SampleName/"+interested_in.replace("/","\/")+"/g\'"+" "+patTupleConfigName
    os.system(writeSampleName)

    writePhysicsProcess = "sed -i \'s/DUMMY_PhysicsProcess/"+PhysicsProcess+"/g\'"+" "+patTupleConfigName
    os.system(writePhysicsProcess)

    writeMASS = "sed -i \'s/DUMMY_MASS/"+Mass+"/g\'"+" "+patTupleConfigName
    os.system(writeMASS)

    writeisNonTopEmbeddedSample = "sed -i \'s/DUMMY_isNonTopEmbeddedSample/"+isNonTopEmbeddedSample+"/g\'"+" "+patTupleConfigName
    os.system(writeisNonTopEmbeddedSample)

    writeisTopEmbeddedSample = "sed -i \'s/DUMMY_isTopEmbeddedSample/"+isTopEmbeddedSample+"/g\'"+" "+patTupleConfigName
    os.system(writeisTopEmbeddedSample)

    writerunOnMC = "sed -i \'s/DUMMY_runOnMC/"+runOnMC+"/g\'"+" "+patTupleConfigName
    os.system(writerunOnMC)

    writecrossSection = "sed -i \'s/DUMMY_crossSection/"+crossSection+"/g\'"+" "+patTupleConfigName
    os.system(writecrossSection)

    writenevents = "sed -i \'s/DUMMY_numberEvents/"+nevents+"/g\'"+" "+patTupleConfigName
    os.system(writenevents)

    CRABtotal_number_of_events = "sed -i \'s/DUMMY_total_number_of_events/"+nevents+"/g\'"+" "+crabConfigName
    os.system(CRABtotal_number_of_events)

    NUM_JOBS = int(float(nevents)/10000.0)
    if(NUM_JOBS>2500):
      NUM_JOBS = 2500
    print "will aim to generate ",str(NUM_JOBS), "crab jobs"

    CRABnumber_of_jobs = "sed -i \'s/DUMMY_number_of_jobs/"+str(NUM_JOBS)+"/g\'"+" "+crabConfigName
    os.system(CRABnumber_of_jobs)

#    PSET = patTupleConfigName
#    PSET = PSET[len(os.environ['CMSSW_BASE']+"/src"):]
#    PSET = "

    CRABpset = "sed -i \'s/DUMMY_pset/"+patTupleConfigName.replace("/","\/")+"/g\'"+" "+crabConfigName
    os.system(CRABpset)

    directoryName = OneWordName+"_v8ntup"
    pubName = "SZS_"+directoryName

    CRABdatasetpath = "sed -i \'s/DUMMY_datasetpath/"+str(sys.argv[1]).replace("/","\/")+"/g\'"+" "+crabConfigName
    os.system(CRABdatasetpath)

    CRABui_working_dir = "sed -i \'s/DUMMY_ui_working_dir/"+directoryName+"/g\'"+" "+crabConfigName
    os.system(CRABui_working_dir)

    CRABuser_remote_dir = "sed -i \'s/DUMMY_user_remote_dir/"+directoryName+"/g\'"+" "+crabConfigName
    os.system(CRABuser_remote_dir)

    CRABpublish_data_name = "sed -i \'s/DUMMY_publish_data_name/"+pubName+"/g\'"+" "+crabConfigName
    os.system(CRABpublish_data_name)

    SE_WHITE_LIST = re.split(' ',whiteList)
    SE_WHITE_LIST.pop()
    print SE_WHITE_LIST
    whiteListVar = ''
    for z in range(0, len(SE_WHITE_LIST)):
	whiteListVar += SE_WHITE_LIST[z]+' , '
    whiteListVar = whiteListVar[:-3]

    CRABse_white_list = "sed -i \'s/DUMMY_se_white_list/"+whiteListVar+"/g\'"+" "+crabConfigName
    os.system(CRABse_white_list)


    # need to do the following :
    #- sed the configurable parameters
    #- set up options for crab jobs, Davis vs LPC, small test jobs, etc
    #- repeat for ntuple jobs
