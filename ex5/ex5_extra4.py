my_name = 'Zed A. show'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

my_height_cms = my_height * 2.54
my_weight_kgs = my_weight * 0.45359237

print "Let's talk about %s." % my_name
print "He's %d inches or %d cms tall." % (my_height, my_height_cms)
print "He's %d pounds or %d Kgs heavy." % (my_weight, my_weight_kgs)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
