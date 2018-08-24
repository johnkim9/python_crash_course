rivers = {
	'nile':'egypt',
	'seine':'france',
	'han':'korea',
	'potomac':'us',
	'rhine':'germany'
}

for	name, country in rivers.items():
	print("The " + name.title() + " runs through " + country.title() + ".")

#Nesting
alien_0 = {'color':'green','points':5}
alien_1 = {'color': 'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print (alien)

#Make an empty list for storing aliens

aliens = []

#Make 30 green aliens.
for alien_number in range(30):
	#range() returns a set of numbers, which just tells Python how many times we want the loop to repeat. 
	new_alien = {'color':'green', 'points':5, 'speed':'slow'}
	#each time the loop runs we create new alien
	aliens.append(new_alien)
	#append each new alien to the list aliens.

#using slice to show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")

#Show how many aliens have been created.
print("Total number of alins:" + str(len(aliens)))
#print the length of the list to prove we've actually generated the full fleet of 30 aliens.

for alien in aliens[0:3]:
	if alien['color']=='green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

#A list in a dictionary


