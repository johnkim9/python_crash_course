#Changing values of an item in a list
motorcycles = ['honda','yamaha','suzuki']
print (motorcycles)
motorcycles[0]='ducati'
print (motorcycles)
motorcycles[0]='honda'

#append function adds an element to the end of the list
motorcycles.append('ducati')
print (motorcycles)

motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#Inserting Elementes into a List
motorcycles=['honda','yamaha','suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

#Removing Elements from a List by using the del Statement
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[0]
print (motorcycles)
del motorcycles[1]
print (motorcycles)

#Removing an Item Using the pop() Method
motorcycles=['honda','yamaha','suzuki']
print (motorcycles)

popped_motorcycle = motorcycles.pop()
#stored popped variable in the variable poppped_motorcycle
print(motorcycles)
print(popped_motorcycle)

motorcycles=['honda','yamaha','suzuki']
last_owned=motorcycles.pop()
print("The last motorcycles I owned was a " + last_owned.title() + ".")

#Popping Items from any position in a list
motorcycles = ['honda','yamaha','suzuki']
first_owned= motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

#Removing an Item by value - using function remove()
motorcycles = ['honda','yamaha','suzuki','ducati']
print (motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

