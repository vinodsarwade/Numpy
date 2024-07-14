#The searchsorted() method is assumed to be used on sorted arrays.
import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 9) # it will give you index of element to search in sorted array.
print(x)



#sort from right side use side='right'
#in this case this will give the index of that number and  at what position the number will be  inserted  to maintain the order.
import numpy as np
arr = np.array([5, 7, 8, 9])
x = np.searchsorted(arr, 4, side='right') #here 4 is smallest number to insert so it could be insert at 0th index to maintain order.so output = 0
print(x)
y = np.searchsorted(arr, 6, side='right') # 6 is greater than 5 so it could be inserted at 1st index
print(y)


