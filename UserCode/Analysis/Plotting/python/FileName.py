f = open('./fileName.txt', 'r')
FileNamePrefix = ""

for x in f:
    FileNamePrefix = x.rstrip('\n')

print "files will be created with prefix : ", x
