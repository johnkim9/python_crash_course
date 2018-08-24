#9-1 & 9-2 Restaurant
class Restaurant():
	def __init__(self, name, cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type

	def open_restaurant(self):
		print(self.name.title() + " is now open!")

	def describe_restaurant(self):
		print(self.name.title() + " serves " + self.cuisine_type + " food.")

my_restaurant = Restaurant('boqueria', 'spanish')
korean_restaurant = Restaurant('mandoo', 'korean')
french_restaurant = Restaurant('le diplomate', 'french')

my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()

korean_restaurant.open_restaurant()
korean_restaurant.describe_restaurant()

french_restaurant.open_restaurant()
french_restaurant.describe_restaurant()

