'''Random number does NOT mean a different number every time. Random means something that can not be predicted logically.
NumPy offers the random module to work with random numbers.
'''
from numpy import random
x = random.randint(100)
print(x)

'''The random module's rand() method returns a random float between 0 and 1.'''
from numpy import random
x = random.rand()
print(x)


#generate random array
'''The randint() method takes a size parameter where you can specify the shape of an array.'''
from numpy import random
x = random.randint(100,size=5) #1D array
print(x)

y = random.randint(100,size=(5,3)) #2D array
print(y)

'''Generate Random Number From Array
The choice() method allows you to generate a random value based on an array of values.
The choice() method takes an array as a parameter and randomly returns one of the values.'''

from numpy import random
x = random.choice([3, 5, 7, 9])
print(x)

#The choice() method also allows you to return an array of values.
#Add a size parameter to specify the shape of the array.
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)