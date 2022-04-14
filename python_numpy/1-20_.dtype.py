import numpy as np
f=np.array([1,2,3,4,5,6,7],dtype=float)
print(f)# f는 실수형 타입으로 나올 것이다.
a=np.array([1,2,3]).dtype
print(f.dtype)
print(np.array([1,2,3]).dtype)
print(type(a))

#다른 데이터 유형도 가능

d=np.array([1+2j,2+4j,5+6j])
print(d.dtype,d)


d=np.array([True,False,True])
print(d,d.dtype)

d=np.array(['nohao','lala','xiexie'])
print(d,d.dtype)