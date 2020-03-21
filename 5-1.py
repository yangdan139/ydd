import numpy as np
#from numpy import *

print("请输入一个1-100之间整数：")
x = int(input())
i = 1
y = 1000/x
print(y)
np.random.seed(612)
rand = np.random.rand(1000)
for j in range(1000):

    if j%x==0:
        print(i,x,rand[j])
        i = i+1


