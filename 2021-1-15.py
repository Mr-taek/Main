import tensorflow as tf
import numpy as np
a=tf.constant([1,2,3,4,5,6])
b=np.array([1,2,3,4,5,6])
q=tf.constant(b)
print(a,b,q)
c=tf.constant(1,dtype=tf.float32,shape=(3,3))
print(c)

#-------------------gradient example tensorflow ------------------------
a=tf.constant(1,dtype=tf.float32)

a1=tf.Variable(a)

z=a1*a1
print(z)
with tf.GradientTape() as g:
    print(g.gradient(z,a1)) 

#-------error가 났으나 아직 이유를 찾지 못했다. eroor이유는 , terminal에서 나오다시피, GradientTape 함수는 오직 float 타입의 tensor만 미분할 수 있기 때문이다.