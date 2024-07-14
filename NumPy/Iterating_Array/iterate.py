'''Iterating means going through elements one by one.
As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.'''

import numpy as np
arr = np.array([1, 2, 3])
for x in arr:
  print(x)

#iterating 2D array
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)

'''By using above this method for 2D array we are getting  array as a return value in for loop also.
to get each and every elements in array, we need to iterate the array in each dimension'''

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)

#iterating 3D arrays
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)
#to return atcuall value in array for 3D then use for loop like below
  '''for x in arr:
        for y in x:
            for z in y:
                print(z) '''