#8-12 Write a function that accepts a list of items a person wants on a sandwich
def make_sandwich(*toppings):
	print("\nMaking a sandwich with the following toppings:")
	for topping in toppings:
		print("-" + topping)

make_sandwich('ham','turkey')

#8-13 User profile
def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
        return profile
    
user_profile = build_profile('John','Kim',location='DC',field='nonprofit finance')
print(user_profile) 

#8-14 Cars
def make_car(manufacturer,model,**car_info):
	car = {}
	car['manufacturer_name'] = manufacturer
	car['model_name'] = model
	for key,value in car_info.items():
		car[key] = value
		return car

car = make_car('subaru','outback',color='blue',tow_package = True)
print(car)

