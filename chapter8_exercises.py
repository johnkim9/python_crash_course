#8-3 & 8-4 T-shirt
def make_shirt(size, message):
	print("This person would like to order " + size + "-sized shirt with the message, " + message + ".")

make_shirt('medium', 'Just Do It')	
make_shirt('large', "I love Python")

#8-5 & 8-6 Cities 
def describe_city(city, country):
	print(city + " is in " + country + ".")

describe_city('Reykjavik', 'Iceland')
describe_city('Florence', 'Italy')
describe_city('Seoul', 'Korea')

#8-7 Album
def make_album(artist_name, title, tracks = ''):
	album = {'artist': artist_name, 'title': title}
	if tracks:
		album['tracks'] = tracks
	return album

album = make_album('Kanye', 'Life of Pablo')
print(album)

album = make_album("Taylor Swift", 'Bad Blood')
print(album)

album = make_album("Taylor Swift", 'Bad Blood', tracks = 12)
print(album)

#8-9 Magicians
def show_magicians (names):
	for name in names:
		msg = "Printing names of magicians: " + name.title()
		print (msg)

names = ['david copperfield', 'david blaine', 'criss angel']
show_magicians(names)



