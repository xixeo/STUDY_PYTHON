# import newPizza #1
# from newPizza import make_pizza #2
from newPizza import make_pizza as mp #3

# newPizza.make_pizza(16, 'pepperoni') #1
# newPizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') #2
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese') #3