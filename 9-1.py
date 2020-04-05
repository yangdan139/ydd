import tensorflow as tf
import numpy as np

x = np.array([137.97,104.50,100.00,124.32,79.2,99.00,124.00,114.00,106.69,138.05,53.75,46.91,68.00,63.02,81.26,86.21])
y = np.array([145.00,110.00,93.00,116.00,65.32,104.00,118.00,91.00,62.00,133.00,51.00,45.00,78.50,69.65,75.69,95.30])
x1 = np.array([3,2,2,3,1,2,3,2,2,3,1,1,1,1,2,2])

x2 = np.ones(len(x))
x3 = np.stack((x,x1,x2),axis = 1)
y1 = y.reshape(-1,1)

x4 = tf.transpose(x3)
x5 = tf.linalg.inv(tf.matmul(x4,x3))
x6 = tf.matmul(x5,x4)

w1 = tf.matmul(x6,y1)
w = tf.reshape(w1,[len(w1),1])

xs = float(input("请输入商品房面积："))
if xs<20 or xs>500:
    xs = float(input("输入不合法。"))
x7 = int(input("请输入房间数："))
if x7<1 or x7>10:
    x7 = float(input("输入不合法。"))
 
y1 = 11.96729293+0.53488599*xs+14.33150378*x7

print("预测房价为：%f" % (y1))