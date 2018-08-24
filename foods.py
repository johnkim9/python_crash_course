#Copying a List
#To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:])
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

print ("My favorite foods are:")
print(my_foods)

print ("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favortie foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#examples below doesn't work because both lists refer to each other.
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are")
print(friend_foods)

#4-10. Slices exercise
my_pizzas=['pepperoni', 'hawaiian', 'bbq', 'korean', 'papa johns']
print("The first three items in the list are:")
print(my_pizzas[0:3])

print("Three items from the middle of the list are:")
print(my_pizzas[1:4])

print("The last three items in the list are:")
print(my_pizzas[2:])

#4.11 My pizzas, your pizzas
friend_pizzas = my_pizzas[:]
my_pizzas.append('dominos')
friend_pizzas.append('pizza hut')

print("My favorite pizzas are:")
print(my_pizzas)

print("My friend's favorite pizzas are:")
print(friend_pizzas)

#4.12 Loops

print("I like following foods:")
for food in my_foods[0:2]:
	print(food)
for pizza in my_pizzas[:3]:
	print(pizza)

