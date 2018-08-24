#Checking for Inequality
#When you want to determine whether two values are not equal,
#you can use (!=). The exclamation point represents not.

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies")
#Stored a requested pizza topping in a variable and then printed a message
#if the person did not order anchovies

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print ("\nAdding mushrooms.")
if 'pepperoni' in requested_toppings:
	print ("Adding pepperoni.")
#because this is not an elif or else statement, this test runs regardless
#of whether the previous test passed or not.
if 'extra cheese' in requested_toppings:
	print ("Adding extra cheese.")

print("\nFinished making your pizza!")

#this would have not worked if we used if-elif-else blcok because the code
#would stop running after only one test passes.

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print ("\nAdding mushrooms.")
elif 'pepperoni' in requested_toppings:
	print ("Adding pepperoni.")
elif 'extra cheese' in requested_toppings: 
	print ("Adding extra cheese.")

print("\nFinished making your pizza!")

#Checking for Special Items
requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print ("Adding " + requested_topping + ".")
print ("\nFinished making your pizza!")

#Checking That a List Is Not Empty
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

#Using multiple lists
available_toppings = ['mushrooms','olives','green peppers', 'pepperoni', 'pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")

#A List in a Dictionary
#Store information about a pizza  being ordered.
pizza = {
	'crust':'thick',
	'toppings':['mushrooms','extra cheese'],
	}
#summarizae the order
print("\nYou ordered a " + pizza['crust'] + "-crust pizza with the folloing toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)

