import tensorflow as tf
import numpy as np

tf.random.set_seed(1)
a=tf.random.normal([3])
print(a)
e=[3.5,4.6,3.8]
e=tf.constant(e)
er=e-a
print(e,er)
d=tf.reduce_mean(tf.square(er))
print(d)