import tensorflow as tf
import numpy as np
# numpy() 함수를 이용하면 numpy 타입으로 변환할 수 있음. tensorflow type을 넘파이로 바꾸면 그냥 숫자만 나오게 된다.
# ch1 의 핵심 "Eager Execution(즉시 실행 모드)기능이 2. 버전에서 패치되면서, tensorflow를 python처럼 사용이 가능하다."
# a=tf.constant(20)
# c=a.numpy()
# print(a,c,type(c))
# tf_ten=tf.convert_to_tensor(c)
# print(tf_ten,type(tf_ten))

#---------------------------
# 2.~ version 이전에는 session()함수를 선언해야만 실제 연산한 값들이 나타나지만, 2.~ 버전 이후로는 즉시 연산이 가능해졌다.
# a=tf.constant(2)
# b=tf.constant(3)
# c=a+b
# print(c,c.numpy())

#--------------------------

# w=tf.Variable(tf.random.normal([1]))

# for step in range(2):
#     w=w+1.0
#     print(step,w)

#-------------------------

# 2.~ version 이전에는 def함수를 실행해서 결과를 얻으려면 tf.placeholder(?)에 입력값을 넣고, 이제 이 변수를 함수에 넣어야 했으나 더 이상 그럴 필요가 없다.
# 훨씬 직관적이게 됨.
# a=tf.constant(4)
# b=tf.constant(5)

# def summ(x,y):
#     return x+y

# c=summ(a,b)
# print(type(c),c)