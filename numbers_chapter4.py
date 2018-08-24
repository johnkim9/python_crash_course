#The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide
for value in range(1,5):
	print(value)

for value in range(1,6):
	print(value)

#Using range() to Make a List of Numbers
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

#squares.py
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)

print(squares)

sqaures=[]
for value in range(1,11):
	squares.append(value**2)

print(squares)

#Simple statistics with a list of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
print (min(digits))
print (max(digits))
print(sum(digits))

#List Comprehensions
squares = [value**2 for value in range(1,11)]
print (squares)

#odd numbers from 1 to 20
odd_numbers = []
for value in range (1,21,2):
	odd_number = value
	odd_numbers.append(odd_number)

print (odd_numbers)

#list of multiples of 3 from 3 to 30
#with the range function, Python stops one item before the second index you specify
threes = []
for value in range (3,31,3):
	three = value
	threes.append(three)

print(threes)

#cubes
cubes = []
for value in range (1,11):
	cubes.append(value**3)

print (cubes)

#comprehension of cubes
cubes = [value**3 for value in range(1,11)]
print (cubes)