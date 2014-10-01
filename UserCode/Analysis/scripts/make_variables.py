import sys

my_file = open(sys.argv[1], 'r')
Htype = sys.argv[2]

print "will make C++ code for ", Htype, "using file ", sys.argv[1]
# python make_variables.py electron.vars (one of the Htypes)

prefix = 'x'
theThing = 'x'


# the 2nd argument for eTau variable list

if Htype=='eTau':
  prefix = 'eT_'
  theThing = Htype

# the 2nd argument for muTau variable list


if Htype=='muTau':
  prefix = 'muT_'
  theThing = Htype

# the 2nd argument for electron leg in eTau variable list



if Htype=='eTauElec':
  prefix = 'eT_ele_'
  theThing = 'theElec'

# the 2nd argument for muon leg in eTau variable list

if Htype=='muTauMuon':
  prefix = 'muT_muon_'
  theThing = 'theMuon'



# the 2nd argument for tau leg in eTau variable list


if Htype=='eTauTau':
  prefix = 'eT_tau_'
  theThing = 'theTau'

# the 2nd argument for tau leg in muTau variable list


if Htype=='muTauTau':
  prefix = 'muT_tau_'
  theThing = 'theTau'


# the 2nd argument for eTau Weights variable list

if Htype=='eTauWt':
  prefix = 'eT_'
  theThing = Htype

# the 2nd argument for muTau Weights variable list

if Htype=='muTauWt':
  prefix = 'muT_'
  theThing = Htype


newVariables = []

print "-----------------------------------------"
print "-----------------------------------------"
print "-----------------------------------------"

for line in my_file:
  evt = line.split(' ')
  modName = evt[1].split('m_')
  if evt[0] != "LorentzVector":
    newName = prefix+modName[1].rstrip()
    print "std::vector<",evt[0],">", newName,";"
    newVariables.append(newName)
  if evt[0] == "LorentzVector":
    newName = prefix+modName[1].rstrip()
    print "std::vector< double >", newName+"_x",",",newName+"_y",",",newName+"_z",",",newName+"_t",";"
    newVariables.append(newName+"_x")
    newVariables.append(newName+"_y")
    newVariables.append(newName+"_z")
    newVariables.append(newName+"_t")


print "-----------------------------------------"
print "-----------------------------------------"
print "-----------------------------------------"

for var in newVariables:
  clearCommand=var+".clear();"
  print clearCommand


print "-----------------------------------------"
print "-----------------------------------------"
print "-----------------------------------------"

for var in newVariables:
  addBranch="lepTauTree->Branch(\""+var+"\", &"+var+");"
  print addBranch


print "-----------------------------------------"
print "-----------------------------------------"
print "-----------------------------------------"

my_file2 = open(sys.argv[1], 'r')

for line in my_file2:
  evt = line.split(' ')
  modName = evt[1].split('m_')
  if evt[0] != "LorentzVector":
    newName = prefix+modName[1].rstrip()
    pushBackCommand = newName+".push_back("+theThing+"."+modName[1].rstrip()+"());"
    print pushBackCommand
  if evt[0] == "LorentzVector":
    newName = prefix+modName[1].rstrip()
    pushBackCommand = newName+"_x.push_back("+theThing+"."+modName[1].rstrip()+"().x());"
    print pushBackCommand
    pushBackCommand = newName+"_y.push_back("+theThing+"."+modName[1].rstrip()+"().y());"
    print pushBackCommand
    pushBackCommand = newName+"_z.push_back("+theThing+"."+modName[1].rstrip()+"().z());"
    print pushBackCommand
    pushBackCommand = newName+"_t.push_back("+theThing+"."+modName[1].rstrip()+"().t());"
    print pushBackCommand


#    print "std::vector< double >", newName+"_x",",",newName+"_y",",",newName+"_z",",",newName+"_t",";"
#    newVariables.append(newName+"_x")
#    newVariables.append(newName+"_y")
#    newVariables.append(newName+"_z")
#    newVariables.append(newName+"_t")
