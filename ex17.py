from sys import argv
from os.path import exists

script, from_file, to_file = argv


print "Copying %s to %s" % (from_file,to_file)

in_file = open(from_file,"r")
in_data = in_file.read()
print("The input file is %d bytes long" % len(in_data))

out_file = open(to_file,"w")
