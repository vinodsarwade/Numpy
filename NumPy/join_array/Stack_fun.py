#We pass a sequence of arrays that we want to join to the stack() method along with the axis.
# If axis is not explicitly passed it is taken as 0.
#in concatenate array it will add array one after one
#but in stack it will take one element in each array and stack them one after one.
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)


#Stacking along Rows'''
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)

#Stacking along with Columns'''
arr = np.vstack((arr1, arr2))
print(arr)

a = [[30, 40], [50, 60]]
b = [[5, 6], [7, 8]]
print(np.hstack([a,b]))
print(np.vstack([a,b]))

