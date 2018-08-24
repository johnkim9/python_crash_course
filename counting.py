current_number = 1
while current_number <= 5:
	print (current_number)
	current_number += 1
# The while loop is then set to keep running as long as the value of current_number is less than or equal to 5. 
# The code inside the loop prints the value of current_number then adds 1 to that value with current_number and then adds 1

#The += operator is shorthand for current_number = current_number + 1. 

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number %2 == 0:
		continue

	print(current_number)

#Use the continue statement to return to the beginning of the loop based on the result of a conditional test.

#Avoiding Infinite Loops
x = 1
while x <= 5:
	print(x)
	x += 1

#This loop runs forever!
x = 1
while x <=5:
	print(x)

