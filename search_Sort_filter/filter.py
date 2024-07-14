'''Getting some elements out of an existing array and creating a new array out of them is called filtering.
In NumPy, you filter an array using a boolean index list.'''
#A boolean index list is a list of booleans corresponding to indexes in the array.
#If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

import numpy as np
arr = np.array([41, 42, 43, 44])
filter_arr = [True, False, True, False] #This is a boolean array (or list) of the same length as arr. Each element in filter_arr is either True or False.
newarr = arr[filter_arr]  #arr[filter_arr]: This is called boolean indexing or masking. It creates a new array by selecting elements from arr where the corresponding value in filter_arr is True
print(newarr) 

#output = [41,43] , bcz new array contains only those value where filter array had True.


#EX:2
'''in above ex. we hardcoded boolean values,but common use is to create filter array based on condition.'''
import numpy as np
arr = np.array([41,42,43,44]) #existing array
filter_array = []             #boolean filter array

for elements in arr:         
    if elements > 42:        #condition
        filter_array.append(True)   #if condition true then append "True" in filter_array
    else:
        filter_array.append(False)

newarray = arr[filter_array]  #boolean indexing to print only True elements
print(filter_array)
print(newarray) 


'''Creating filter Directly from Array'''
#We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.
import numpy as np
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


#Create a filter array that will return only even elements from the original array:
import numpy as np
array1 = np.array([1,2,3,4,5,6,7,8])
filter_a = array1 % 2 == 0
newa = array1[filter_a]
print(newa)