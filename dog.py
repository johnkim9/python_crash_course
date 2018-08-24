#Chapter 9 - Classes
class Dog():
	"""A simple attempt to model a dog"""
	def __init__(self,name,age):
		"""initialize name and age attributes."""
		self.name = name
		self. age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")
	
	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")

#Note: A function that's part of a class is a method. 

#Making an Instance from a Class
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
#Accesing Attributes

print("My dog is " + str(my_dog.age) + " years old.")

#Calling methods
my_dog.sit()
my_dog.roll_over()
#To call a method, give the name of the instance and the method you want to call, separated by a dot.

your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + "years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

