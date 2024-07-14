'''We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].'''
import numpy as np
arr =np.array([10,20,30,40])
print(arr[0:3])

#Slice elements from index 4 to the end of the array:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])


#Use the minus operator to refer to an index from the end:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1]) #negative index always start from 1. it will print form 1 to 3(2nd and 3rd element from negative index)