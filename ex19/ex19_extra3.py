def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

def add(num1, num2):
    print "Adding %d and %d, gives %d" % (num1, num2, num1 + num2)

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine that two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

num1 = 10
num2 = 20

add (5,10)
add (5*3, 10*2)
add (5+3, 10+2)
add (num1, num2)
add (num1 + 10, num2)
add (num1, num2 + 10)
add (num1 +10, num2 + 10)
add (num1, 10)
add (10, num2)
add (10 + 10, num2 * 10)
