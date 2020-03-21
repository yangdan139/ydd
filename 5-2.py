import numpy as np
import math
#from numpy import *
x =np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y = np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])

aver1 = np.sum(x)/(x.size)
aver2 = np.sum(y)/(y.size)
i = 0
sum1 = 0
sum2 = 0
while i<x.size:
    sum1 = sum1 + int((x[i]-aver1)*(y[i]-aver2))
    sum2 = sum2 + int((x[i]-aver1)*(x[i]-aver1))
    i = i+1


w = sum1/sum2
b = aver2-(w*(int(aver1)))
print(w,b)




