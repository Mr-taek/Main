import numpy as np

a=np.random.randint(low=0,high=50,size=(3,5))
b=[]
c=[]
for i in  range(len(a)):
    b.append({np.max(a[i]):np.argmax(a[i])})
   
    c.append({np.min(a[i]):np.argmin(a[i])})
print('max value: {}\n min value: {}\n a= {}'.format(b,c,a))# 순서대로 나열되니까 각 열에서 어떤 값이 큰 지 알 수가 있네...