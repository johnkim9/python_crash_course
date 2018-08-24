import pizza_import

pizza_import.make_pizza(16,'pepperoni')
pizza_import.make_pizza(12,'mushrooms','green peppers','extra cheese')
#module_name.function_name()

#Importing Specific Functions  
"""from module_name import function_name
	from module_name import function_0, function_1, function_2"""

from pizza_import import make_pizza
make_pizza (16, 'pepperoni')
make_pizza (12, 'mushrooms', 'green peppers', 'extra cheese')

#Using as to give a function an Alias
from pizza_import import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers' , 'extra cheese')
"""The general syntax for providing an alias is:
	from module_name import function_name as fn"""

#Using as to Give a Module an Alias
import pizza_import as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""General syntax is
	import module_name as mn"""

#Importing all functions in a module
from pizza_import import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'ham')

