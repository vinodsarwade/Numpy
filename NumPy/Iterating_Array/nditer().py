'''In basic for loops, iterating through each scalar of an array we need to use n for loops
which can be difficult to write for arrays with very high dimensionality.'''
'''to overcome this we used nditer()'''

import numpy as np
arr = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
for x in  np.nditer(arr):
    print(x)
#by using this we can directly get an elements of multidimension array. we dont need to use multiple for loops.