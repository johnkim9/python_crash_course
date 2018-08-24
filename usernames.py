#5-8 exercises
user_names = ['admin','sam','jess','john','janet','info']
for user_name in user_names:
	if user_name == 'admin':
		print("Hello " + user_name + ", would you like to see a status report?")
	else:
		print("Hello " + user_name + ", thank you for logging in again.")

#5-9. No users

user_names = []
if user_names:
	for user_name in user_names:
		print("Hello " + user_name + ", would you like to see a status report?")
else:
	print("We need to find some users!")

#5-10. Checking Usernames
current_users = ['admin','sam','jess','john','janet','info']
new_users = ['intern','assistant','ec','admin','info']

for new_user in new_users:
	if new_user in current_users:
		print("Username is already in use. Please enter a new username.")
	else:
		print("Username is available.")

#5-11. Ordinal numbers.
numbers = ['1','2','3','4','5','6','7','8','9']
for number in numbers:
	if number == '1':
		print(number + "st")
	elif number == '2':
		print(number + "nd")
	elif number == '3':
		print (number + "rd")
	else:
		print (number + "st")

