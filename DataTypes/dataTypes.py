'''i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )'''

#The NumPy array object has a property called "dtype" that returns the data type of the array:
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)


import numpy as np
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

'''Creating Arrays With a Defined Data Type'''
#We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:
#Example
#Create an array with data type string:
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='S') #dtype = string
print(arr)
print(arr.dtype)


#Create an array with data type 4 bytes integer:
import numpy as np
arr = np.array([1,2,3,4],dtype='i4')  #dtype = integer with 4 bytes
print(arr)
print(arr.dtype)


'''What if a Value Can Not Be Converted?'''
##A non integer string like 'a' can not be converted to integer (will raise an error):
# import numpy as np
# arr = np.array(['a', '2', '3'], dtype='i') # for this we get value error bcz  string element "a" is not converted in integer.


'''Converting Data Type on Existing Arrays'''
#The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
#The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype(int)
newarr = arr.astype('i')                    #astype() will create new copy of array  and can convert in given format. it is same like "dtype" but we are using astype bcz creating new copy of array.
# newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)