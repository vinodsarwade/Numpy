import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])


#Get third and fourth elements from the following array and add them.
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])



'''Accessing 2D arrays'''
#Access the element on the first row, second column:
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr)
print(' 1st row,2nd element: ', arr[0, 1]) # 0 for first row and and 1 for 2nd column.
print(' 2nd row, 5th element: ', arr[1, 4])


'''Accessing 3D arrays'''
#Access the third element of the second array of the first array:
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr[0, 1, 2])


#Use negative indexing to access an array from the end.
#Print the last element from the 2nd dim:
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])