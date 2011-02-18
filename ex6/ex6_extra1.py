#Assing a string to a variable
x = "There are %d types of people." % 10
#Assing a string to a variable
binary = "binary"
#Assing a string to a variable
do_not = "don't"
#Assing a string to a variable
y = "Those who know %s and those who %s." % (binary, do_not)

#print the string
print x
print y

#print the string
print "I said: %r." % x
print "I also said: '%s'." % y

#Assign a string to a variable
hilarious = False
#This is the evaluation string
joke_evaluation = "Isn't that joke so funny?! %r"

#print both the string
print joke_evaluation % hilarious

#Assign a string to a variable
w = "This is the left side of..."
#Assign a string to a variable
e = "a string with a right side."

#print both the string
print w + e
