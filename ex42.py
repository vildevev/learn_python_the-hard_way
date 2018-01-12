## Animal is-a object (yes, sort of confusing) look at the extra credit 
class Animal(object):
	pass

## Dog is-an animal 
class Dog(Animal):

	def __init__(self, name):
		## Has-a name 
		self.name = name 


## Cat is-an animal 
class Cat(Animal):

	def __init__(self, name):
		## Has-a name 
		self.name = name 


## Person is a class
class Person(object):

	def __init__(self, name):
		## Has-a name
		self.name = name 

		## Person has-a pet of some kind 
		self.pet = None 

## Employee is-a person 
class Employee(Person):

	def __init__(self, name, salary):
		## inherits traits from person class while adding salary attribute
		super(Employee, self).__init__(name)
		self.salary = salary


class Fish(object):
	def __init__(self):

		self.beautiful_in_their_own_way = True

class Salmon(Fish):
	pass 

class Halibut(Fish):
	pass 


# rover is-a Dog 
rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover 

flipper = Fish()

crouse = Salmon()

harry = Halibut()