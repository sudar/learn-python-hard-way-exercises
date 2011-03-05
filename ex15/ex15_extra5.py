filename = raw_input("Enter filename >")
txt = open(filename)

print "Here's your file %r" % filename
print txt.read()
