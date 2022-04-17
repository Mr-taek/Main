# numpy에는 matmul 기능이 있음. tf도 있으며, tf와 np는 상호작용이 가능.
# matmul과 dot에는 2차원 계산은 서로 다름이 없지만 3차원부터는
# 원리가 달라진다.

# 탠서 : 2차원을 초과, 

import tensorflow as tf
import numpy as np
a=tf.constant([[1,2],[3,4]])
b=tf.add(a,1)

c=np.matmul(a,b)
d=tf.matmul(a,b)
print(c,d)

# dot의 연구...
a=np.array([[
    [1,2,3,4],
    [4,3,2,1]
],[
    [0,1,1,0],
    [1,2,3,4]
]]) # 2,2,4

b=np.array([[
    [1,1],
    [1,1],
    [1,1],
    [1,1]
],[
    [1,1],
    [1,1],
    [1,1],
    [1,1]
]]) # 2,4,2

print(np.dot(a,b).ndim)