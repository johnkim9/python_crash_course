#cubes
cubes = []
for value in range (1,11):
	cubes.append(value**3)

print (cubes)

#comprehension of cubes
cubes = [value**3 for value in range(1,11)]
print (cubes)

#odd numbers from 1 to 20
odd_numbers = []
for value in range (1,21,2):
	odd_number = value
	odd_numbers.append(odd_number)

print (odd_numbers)

#list of multiples of 3 from 3 to 30
threes = []
for value in range (3,31,3):
	three = value
	threes.append(three)

print(threes)

#listing 1~20
numbers = list(range(1,21))
print (numbers)

#counting up to one million
numbers = []
for value in range (1,1000001):
	number = value
	numbers.append(number)

print (numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

