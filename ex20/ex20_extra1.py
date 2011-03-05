from sys import argv #import from modules

script, input_file = argv

#function definition
def print_all(f):
    print f.read()

#function definition
def rewind(f):
    f.seek(0)

#function definition
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file) #call the function

print "First let's print the whole file:\n"

print_all(current_file) #call the function

print "Now let's rewind, kind of like a tape."

rewind(current_file) #call the function

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file) #call the function

current_line = current_line + 1
print_a_line(current_line, current_file) #call the function

current_line = current_line + 1
print_a_line(current_line, current_file) #call the function
