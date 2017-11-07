# number of cars
cars = 100 
# how many people they have room for 
space_in_car = 4.0 
# how many drivers there are
drivers = 30 
# how many passengers
passengers = 90 
# calculate how many cars that are not driven 
cars_not_driven = cars - drivers 
# how many cars that are driven 
cars_driven = drivers 
# how many people the cars have space for in total 
carpool_capacity = cars_driven * space_in_car
# the average number of peopl in each available car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
