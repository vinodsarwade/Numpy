# '''in list we can join element like below directly'''
# list1 = [30,40,50]
# list2 = [5,6,7]
# print(list1 + list2)
# #output => [30, 40, 50, 5, 6, 7]

'''but in numpy if we use like above then it will add elements in array.
to avoid that need to use concatenate function'''

import numpy as np
# arr1 = [30,40,50]
# arr2 = [5,6,7]
# print(np.concatenate([arr1, arr2]))


# Ex:2
'''if we need to concatenate 2D array then we can do it using Axis. 
axis is like a horizontal or vertical array to be join.'''

a = [[30, 40], [50, 60]]
b = [[5, 6], [7, 8]]

print(np.concatenate([a, b], axis=1))  # horizontal concatenate use axis = 1

print(np.concatenate([a, b], axis=0))  # vertical concatenate use axis = 0
