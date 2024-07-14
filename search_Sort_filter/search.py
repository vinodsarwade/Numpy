'''for search we use where() function and it takes 1 arguments and return tuple index of that element. '''
import numpy as np
arr = np.array([3,4,1,7,8])
s = np.where(arr == 4)
n = np.where(arr % 2 == 0)
print(s)
print(n)


import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)