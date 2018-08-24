#How the input() Function works
#input() function pauses your program and waits for the user to enter some text. Once Python receives the user's input, it stores it in a variable.

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#The input() function takes one argument: the prompt or instructions. 

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
	message = input(prompt)
	print(message)

	if message != 'quit':
		print(message)

#Using Flag
active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)
#Flag is when you define a variable that determines whether or not the entire program is active.

#Using break to Exit a Loop
