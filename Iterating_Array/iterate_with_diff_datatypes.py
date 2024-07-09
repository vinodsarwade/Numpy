'''We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.'''
#NumPy does not change the data type of the element in-place 
#(where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, 
#and in order to enable it in nditer() we pass flags=['buffered'].

import numpy as np
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

'''in this above case we are using op_dtypes arguments with data type to convert an array.
to convert array compiler need different space so we used flags as a buffered to create a seperate space.'''