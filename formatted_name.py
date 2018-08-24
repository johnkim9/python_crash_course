#Return Values
#Return statement takes a value from inside a function and send it back to the line that called the function.
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formated."""
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
