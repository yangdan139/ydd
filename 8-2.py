import tensorflow as tf
import math as m
import numpy as np

x = tf.constant(np.array([64.3,96.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]))
y = tf.constant(np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]))

sum1 = (tf.size(x).numpy())*(tf.reduce_sum(tf.multiply(x,y)).numpy())

sum3 = tf.reduce_sum(x).numpy()
sum2 =tf.reduce_sum(y).numpy()

sum4 = (tf.size(x).numpy())*(tf.reduce_sum(tf.pow(x,2)).numpy())

x1=sum4-(sum3*sum3)
a=sum1-sum3*sum2


w = a/x1

b = (sum2-w*sum3)/(tf.size(x).numpy())

print(w)
print(b)