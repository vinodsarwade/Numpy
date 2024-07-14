import numpy as np
arr = np.array([10,20,30,40])
print(np.append(arr,[90]))

#for appending elements in 2D array, first compiler will convert it in to 1D and then append & return whole array as a 1D array
arr2 = np.array([[10,20],[30,40]])
print(np.append(arr2,[90]))


#insert()
arr3 = np.array([[10,20],[30,40]])
print(np.insert(arr3, 2, 90)) # (array, position, element to insert)

arr3 = np.array([[10,20,30,40]])
print(np.insert(arr3, 2,100)) 

#if we need to insert multiple elements at some position then use []

arr4 = np.array([[10,20,30,40]])
print(np.insert(arr4, 2,[100,90,80,70])) # here we insert whole numbers at position 2


'''here in this case we can axis also at horizontal or vertical you need to insert the elements.'''
print(np.insert(arr4,2,[78],axis=1))


#delete elements from array
arr5=[1,2,3,4,5,6,7,8]
print(np.delete(arr5,3)) # delete 3rd index from arr5

arr5=[[1,2,3,4],[5,6,7,8]]
print(np.delete(arr5,1,axis=1)) 

