import numpy as np
a=np.linspace(start=0,stop=1,num=1000,endpoint=True)

f=lambda x:x**2
def integral2(f,x):
    k=0
    for i in range(len(x)-1):
        k+=(x[i+1]-x[i])*f(x[i+1])
    
    return k


def integral1(f,x):
    k=0
    for i in range(len(x)-1):
        k+=(x[i+1]-x[i])*f(x[i])
    return k

print('func fs range is {} < S < {}'.format(integral1(f,a),integral2(f,a)))
    
