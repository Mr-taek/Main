# numpy.copy()

#copy(obj, order='K') : obj: 복사할 array   order: 'C' 'F' 'A' 'K' 가 있는데, C: C 언어의 순서. F: 포트란의 순서. A: obj객체가 포트란 연속체면 F를 의미.그렇지 않으면 C를 의미한다. K: obj 레이아웃을 최대한 일치시키는 것.

import numpy as np
# Ex 1) np.copy(obj, order='K') order의 default='K'
a=[[1,2],[2,3],[3,2]]
x=np.array(a,order='K') # order을 다 적용해 봤지만 변화가 없음..
print(x)
y=np.copy(x)
print(y,type(y))

# Ex 2) 배열변수.copy(No argument)

b=[[1,2],[52,13],[32,13]]

c=np.array(b)

d=c.copy()  #이렇게 카피도 가능.

print(d,type(d))