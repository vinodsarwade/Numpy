import numpy as np
import statistics as st
baked_food = [200, 300, 150, 130, 200, 280, 170, 188]
a = np.array(baked_food)
print(np.mean(a))  # sum of all the values/number of values
                    # it will first sort the array then find mid value in array in return
print(np.median(a))
                     # if array has even value then it takes two middle value add them and give average for that
print(st.mode(a))  # most of the times the value will be occured
print(np.std(a)) #standard deviation
print(np.var(a)) #varience is a square if standard deviation


'''Key Points:
Mean (μ): The average of all the values in the dataset.
Variance (σ²): The average of the squared differences from the mean. Variance measures the spread of the data points.
Standard Deviation (σ): The square root of the variance. It provides a measure of the dispersion in the same units as the original data, making it easier to interpret.


'''

