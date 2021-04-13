print("Hello user! What's your name ?")
name = input("My name is: ")
print("Welcome "+name+"!")
print("And, how old are you?")
age = int(input("I'm: "))
if age>21:
	print("Cool! You're an adult. I hope that you're been very responsable. ")
elif age<0: 
	print("Really? It's impossible that you have this age!")
else:
	print("Too young to have a conversation with a computer!")

#Defines a list of names
names = ["Harry", "Ron", "Hermione", "Ginny"]

# .append adiciona mais um elemento ao array
names.append("Draco")

# .sort ordena o array aleatoriamente
names.sort()

print(names)

# Create an empty set
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

s.remove(2)
print(s)

print(f"The set has {len(s)} elements")


#Loop

# for i in [0, 1, 2, 3, 4, 5]:
# Or just use range like this: 
for i in range(6):
	print(i)


for name in names:
	print(name)


# Dictionary
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}

houses["Hermione"] = "Gryffindor"

print(houses["Draco"])


# Functions in Python

# Square is a function made in another file
# Like this: def square(x): return x*x

#Import data of another file
from functions import square
for i in range(10):
	print(f"The square of {i} is {square(i)}")


# Object Oriented Programming

# First, create a class to define states
# of objects in a function
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

p = Point(2, 8)
print(p.x)
print(p.y)


class Flight():
	def __init__(self, capacity):
		self.capacity = capacity
		self.passangers = []

	def add_passanger(self, name):
		if not self.open_seats(): #This condition verify what seats are open
			return False
		self.passangers.append(name)
		return True

	def open_seats(self):
	    return self.capacity - len(self.passangers)

#Defines the capacity of Flight
flight= Flight(3)

#Defines passangers who want to get a flight
people = ["Harry", "Ron", "Hermione", "Ginny"]
#This loop calls the class flight in function add_passanger
#To add passangers to seats available
for person in people:
	sucess = flight.add_passanger(person)
	#And this condition verify who's added.
	if sucess:
		print(f"Added {person} to flight sucessfully.")
	else:
		print(f"No available seats for {person}")


# Decorators
def announce(f):
	def wrapper():
		print("About to run the function...")
		f()
		print("Done with the function.")
		return wrapper

#The hello function is wrapper inside of this annoumce decorator
#where what the announce decorator does, is it takes our hello
#function of input and gets us a new function that first prints
#an alert warning that we're about to run the function, actually
#runs the function and then prints another message.
@announce
def hello():
	print("Hello, world!")

	hello()


# Exceptions

#this feature allows you to create exceptions 
#for some types of errors that you may 
#encounter during development

import sys

try: 
	x = int(input("x: "))
	y = int(input("y: "))
except ValueError:
	print("Error: Invalid input.")
	#function sys to exit program
	sys.exit(1)


try:
	result = x / y
except ZeroDivisionError:
	print("Error: Cannot divide by 0.")
	sys.exit(1)

print(f"{x} / {y} = {result}")


