'''flattning means we can reshape the 2d or 3d array to a single dimention array'''
#Flattening array means converting a multidimensional array into a 1D array.
#We can use reshape(-1) to do this.
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr.reshape(-1))