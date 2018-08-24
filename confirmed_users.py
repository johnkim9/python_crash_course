#Using a while loop with Lists and Dictionaries
#Moving Items from one list to another
#Using while loops with lists and dictionaries allows you to collect, store and organize lots of input to examine and report on later

#Start with with users that need to be verified,
#and an empty list to hold confirmed users.
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

#verify each user until there are no more unconfirmed users.
#Move each verified user into the list of confirmed users.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
#pop() function removes unverified users one at a time from the end of unconfirmed_users. 
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

#Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

