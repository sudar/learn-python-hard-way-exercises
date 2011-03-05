from sys import argv
from os.path import exists

script, from_file, to_file = argv
indata = open(from_file).read()

output = open(to_file, 'w')
output.write(indata)
output.close()
