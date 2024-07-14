import numpy as np
arr = np.array([20,40,60,70])
print(np.sum(arr))
print(np.min(arr))
print(np.max(arr))
print(np.size(arr))
print(np.mean(arr))
print(np.cumsum(arr)) #cumulative sum of elements in array
print(np.cumprod(arr))


a = np.array([100,150,199,200,250,130])
b = np.array([10,50,30,40,30,10])
price = np.array(a)
quantity = np.array(b)
print(price,"\n",quantity) #print array as it is
print()
c = np.cumprod([price,quantity],axis=0) #cumalative product of price and quantity, it return two rows of array for price and cumprod
print(c)
print(c[1].sum()) #we need to do sum of cumprod so ,it is in 2nd row so c[1] and .sum() for addition 