'''An alternate solution of splitting of array in horizontal or vertical rather than this we can use is hsplit() and vsplit()'''
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr1 = np.vsplit(arr, 3)
newarr2= np.hsplit(arr, 3)

print(newarr1)
print(newarr2)