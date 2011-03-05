#import from sys module
from sys import argv

#unpack argv
script, filename = argv

#open the file
txt = open(filename)

#print filename
print "Here's your file %r" % filename
#print the contents of the file
print txt.read()

#print the string
print "I'll also ask you to type it again:"
#get the file name again
file_again = raw_input (">")

#open the file again
txt_again = open(file_again)

#print the new file
print txt_again.read()
