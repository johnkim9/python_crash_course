#Tuples
#You use parentheses instead of square brackets
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#Looping through all values in a tuple
for dimension in dimensions:
	print(dimension)

#Writing over a Tuple
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)

#4-13 exercise 
buffet = ("rice", "shrimp", "beef", "pork", "eggs")
print(buffet)
for food in buffet:
	print(food)

print(buffet[0])
buffet[0]=noodle
#error because you can't change the tuple
print(buffet)