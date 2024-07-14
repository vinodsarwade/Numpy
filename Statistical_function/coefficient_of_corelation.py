import numpy as np
tobacco_consumption = [30,50,10,30,50,40]
death = [100,120,70,100,120,112]
'''coefficient of corelation is gives you the how much the data will corelates to each other.
here in this case if the tobacco consumption increases then death retio also increaes, it means data corelates to each other.
if it return 1 = propertional relationship (data corelated)
-1 = inversaly propertional(didnt corelates data)
0 = no relationship'''
#basically it gives how much the data corelates to each other
print(np.corrcoef(tobacco_consumption,death))