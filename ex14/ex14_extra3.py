from sys import argv

script, first_name, last_name = argv
prompt = '> '

print "Hi %s %s, I'm the %s script." % (first_name, last_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s %s?" % (first_name, last_name)
likes = raw_input(prompt)

print "Where do you live %s %s?" % (first_name, last_name)
lives = raw_input(prompt)

print "What kind of ocmputer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
