'''Splitting is reverse operation of Joining.
Joining merges multiple arrays into one and Splitting breaks one array into multiple.
We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.'''

import numpy as np
# arr = [1,2,3,4,5,6]
# print(np.array_split(arr,3)) #The return value is a list containing three arrays.


# #If the array has less elements than required, it will adjust from the end accordingly.
# arr = [1,2,3,4,5,6]
# print(np.array_split(arr,4))

# '''We also have the method split() available but it will not adjust the elements when elements are less in source array for splitting like in example above, array_split() worked properly but split() would fail.'''


# #Access the splitted arrays:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 3)
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])


# #splitting of 2D array
# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
# newarr = np.array_split(arr, 3)
# print(newarr)


'''if you want to split array on a specific axis like horizontal of vertical i.e: axis= 0 or axis= 1'''
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)