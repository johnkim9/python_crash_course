#Positional Arguments
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " +animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster','harry')
#Multiple function cals
describe_pet('dog', 'willie')

describe_pet(animal_type = 'hamster', pet_name = 'harry')

def describe_pet(pet_name, animal_type='dog'):
	"""Display info about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
describe_pet(pet_name='harry', animal_type='hamster')
#When you use default values, any parameter with a default value
#needs to be listed after all the parameters that don't have default values.
#This allows Python to continue interpreting positional arguments correctly.

#Equivalent Funcation Calls
def describe_pet(pet_name, animal_type='dog'):
	#A dog named Willie.
	describe_pet(pet_name ='willie')
	describe_pet('willie')
	#A hamster named Harry
	describe_pet('harry', 'hamster')
	describe_pet(pet_name='harry', animal_type ='hamster')
	describe_pet(animal_type = 'hamster', pet_name='harry')


