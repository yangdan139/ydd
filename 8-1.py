import tensorflow as tf
import math as m
import numpy as np

x = tf.constant(np.array([64.3,96.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]))
y = tf.constant(np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]))


sum1 = tf.reduce_sum(x).numpy()
sum2 =tf.reduce_sum(y).numpy()



aver1 = sum1/(tf.size(x).numpy())
aver2 = sum2/(tf.size(y).numpy())



x1 = tf.fill([1,10],aver1)
y1 = tf.fill([1,10],aver2)

sum = 0.0
sum3 = 0.0


sum3 =tf.reduce_sum((tf.subtract(x,x1))*(tf.subtract(y,y1))).numpy()
sum = (tf.reduce_sum(tf.pow(tf.subtract(x,x1),2)).numpy())
w = sum3/(sum)


b = aver2-w*aver1

print(w)
print(b)
