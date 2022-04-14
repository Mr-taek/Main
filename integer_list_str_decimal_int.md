# 정수를 각각 리스트에 분리시켜 정수의 자리수를 파악하기 위한 코딩.
```
import numpy as np
a=np.random.randint(0,1000)
b=np.random.randint(0,1000)
a=list(str(a))
b=list(str(b))
print(a,b)
def abc():
        
        for i in range(len(a)):
            a[i]=int(a[i])
        for i in range(len(b)):
            b[i]=int(b[i])
        a.reverse()
        b.reverse()
        c=0
        d=0
        q=0
        for i in range(0,len(a)):
            k=10**i
            j=a[i]*k
            c+=j
        d=c
        c=0
        for i in range(0,len(b)):
            k=10**i
            j=b[i]*k
            c+=j
        q=c

        return d,q
print(abc())
```