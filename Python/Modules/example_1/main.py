import utility
from utility import divide, multiply
from packages.shopping_cart import buy

import sys
import random
import pyjokes

print(utility.multiply(2, 3))
print(divide(6, 3))
print(multiply(2, 3))
print(buy('apple', 'oranges'))

# built in random function
print(random)
# help(random) # gives helpful information regarding the package random
print(dir(random)) # list all the function available in random

print('---*print random values from 0 to 1*---')
for i in range(10):
    print(random.random())

print('---*print random values from 0 to 10*---')
for i in range(10):
    print(random.randint(0, 10))

print('---*print random values within given list*---')
for i in range(10):
    print(random.choice([10, 20, 30, 40, 50, 60]))

print('---*shuffle the given list randomly*---')
mylist = [10, 20, 30, 40, 50, 60]
random.shuffle(mylist)
print(mylist)

# built in sys function

#pyjokes
print(pyjokes.get_joke('en', 'neutral'))