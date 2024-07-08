import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2]) #[start:end:step]
print(arr[::2])

""" slicing of 2D array"""
#From the second element, slice elements from index 1 to index 4 (not included):
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1,1:4])

#From both elements, return index 2:
print(arr[0:2,2]) #0th row and 2nd column for index2(element 3rd in arr)


'''From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:'''
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])
#in 2d array alwayd return a same numbers from both array.
#if we give 2 elements in 1st array and 4 in 2nd array still it will return 4 elements. MATRIX rule.( same no of row and column )

print(arr[1,3]) #will print second array 4th element
