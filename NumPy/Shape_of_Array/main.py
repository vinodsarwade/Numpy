#shape() returns a tuple with no of rows and no of column.
import numpy as np
arr = np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])
print(np.shape(arr)) # it returns (3,4) --> 3 row , 4 column
#print(arr.shape) # we can directly write like this

print(np.size(arr)) # give total elements in array
