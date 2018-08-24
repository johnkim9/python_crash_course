def greet_user():
#def defines a function
	"""Display a simple greeting."""
	#This is a comment called doctstrings, which describes what function is doing. 
	print("Hello!")

greet_user()
#you call the name of function to use it.

#Passing information to a function
def greet_user(username):
	"""Display a simple greeting."""
	print("Hello," + username.title() + "!")

greet_user('jesse')

def display_message():
	"""Display a message for the 8-1 exercise."""
	print("Hey how are you?")

display_message()

def favorite_book(title):
	print("One of my favorite books is " + title.title() + ".")

favorite_book('Alice in Wonderland')

#Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
 	"""Return a full name, neatly formatted."""
 	full_name = first_name + ' ' + last_name
 	return full_name

while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")

	f_name = input("First name: ")
	if f_name == 'q':
		break

	l_name = input("Last name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")


