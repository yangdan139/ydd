import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

boston_housing = tf.keras.datasets.boston_housing
(train_x,train_y),(_,_) = boston_housing.load_data(test_split = 0)

plt.rcParams['font.sans-serif'] = "SimHei"
plt.rcParams["axes.unicode_minus"] = False

titles = np.array(["CRIM","ZN","INDUS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B-1000","LSTAT","MEDV"])
plt .figure(figsize=(5,5))


i = 1
for i in range(13):
    print("%d----%s"%(i+1,titles[i]))
i = int(input("请输入属性序号值："))
plt.scatter(train_x[:,i-1],train_y)
plt.xlabel(titles[i-1])
plt.ylabel("price($1000's)")
plt.title(str(i)+"."+titles[i-1]+"-price")
plt.show()
