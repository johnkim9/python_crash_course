#A dictionary of Similar objects
#dictionary is useful for storing the results of a simple poll

favorite_languages = {
	'jen':'pyhton',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}

print ("Sarah's favorite langauge is " +
	favorite_languages['sarah'].title() +
	".")

#Looping Through All Key Value Pairs
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + 
		language.title() + ".")

#6-1. Person
person_0 = {
	'first name':'john',
	'last name':'kim',
	'age':'26',
	'city':'Washington DC'
}

print(person_0)

#6-2. Favorite Numbers
favorite_numbers = {
	'john':9,
	'sam':1,
	'jess':2,
	'janet':8,
	'hyun':10
}

print(favorite_numbers)

#Looping Through All the Keys in a Dictionary
favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}

for name in favorite_languages.keys():
	print(name.title())

friends = ['phil','sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() +
			", I see your favorite language is " + 
			favorite_languages[name].title() + "!")

#You can use the keys() method to find out if a particular person was polled. 

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

#Looping THrough a Dictionary's Keys in Order
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")
#Used sorted function

#Looping Through All Values in a Dictionary
#You can use the value() method to return a list of values without any keys.

print("The following languages have been mentiond:")
for language in favorite_languages.values():
	print(language.title())

#Use a set function to see each language chosen without repetition
print("\nThe following languages have been mentiond:")
for language in set(favorite_languages.values()):
	print(language.title())

favorite_languages = {
	'jen':['python', 'ruby'],
	'sarah':['c'],
	'edward': ['ruby','go'],
	'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
	if len(languages) < 2:
		print("\n" + name.title() + "'s favorite languages is:")
		for language in languages:
			print("\t" + language.title())
	else:
		print("\n" + name.title() + "'s favorite languages are:")
		for language in languages:
			print("\t" + language.title())

print(len(languages))

