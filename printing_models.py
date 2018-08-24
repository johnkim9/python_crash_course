#Modifying a List in a Function
#Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Simiulate printing each design, until none are left.
#Move each design to completed_models after printing.
while unprinted_designs:
	current_design = unprinted_designs.pop()
	#Simulate creating a 3D print from the design.

	print("Printing model: " + current_design)
	completed_models.append(current_design)
	#Have to indent

#Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)

#Using two functions
def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("\nPrinting model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Senindg a copy of a list to a function:
function_name(list_name[:])
#slice notation [:] makes a copy of the list to send to the function.

print_models(unprinted_designs[:],completed_models)
#This will use a copy of the original unprinted designs list, not the actual unprinted_designs list.


