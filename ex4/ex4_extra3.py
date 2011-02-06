#total number of cars
cars = 100
#space in one car
space_in_a_car = 4.0
#total number of drivers
drivers = 30
#total number of passengers
passengers = 90
#number of cars that are not driven today
cars_not_driven = cars - drivers
#number of cars that are dirven today
cars_driven = drivers
#total carpool capacity
carpool_capacity = cars_driven * space_in_a_car
#average number of passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
