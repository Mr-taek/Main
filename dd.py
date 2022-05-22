# sosu=[1]
# derivation=[]
# most=[]
# for i in range(2,1000+1):
#     for k in range(2,i+1):
#        if i%k==0:
#            if k==i:
#                sosu.append(i)
#            else: break

# for i in range(0,len(sosu)-1):
#     derivation.append(sosu[i+1]-sosu[i])
#     if derivation[i]>most:
#         most
    

# # print(derivation)
# print(sosu)
#------ 연습문제 76page


# import numpy as np

# a=np.random.randint(0,50,dtype=int)
# b=[]

# for i in range(1,a+1):
#     if a%i==0:
#         b.append(i)

# print(a,b)


# import numpy as np

# a=np.random.randint(0,50)
# b=np.random.randint(0,50)
# a1=[]
# b1=[]
# intersection=[]
# def inter():
#     for i in range(1,a):
#         if a%i==0:
#             a1.append(i)
#     for i in range(1,b):
#         if b%i==0:
#             b1.append(i)
#     for i in range(len(a1)):
#         if a1[i] in b1:
#             if a1[i] not in intersection:
#                 intersection.append(a1[i])
#     for i in range(len(b1)):
#         if b1[i] in a1:
#             if b1[i] not in intersection:
#                 intersection.append(b1[i])
# inter()
# print(a1,b1)
# print(a,b,np.max(intersection))

# 소인수 2,3 +소수 으로 구성된 값만 찾기.
# import numpy as np

# a=np.random.randint(0,500)
# b=[]
# print(a)
# while True:
#     if a%2==0:
#         a=a/2
#         b.append(2)
#     elif a%3==0:
#         a=a/3
#         b.append(3)
#     else: 
#         b.append(a) 
#         break

# print(b)
    
# 약수찾기.

# import numpy as np
# def abc():
#     a=np.random.randint(0,500)
#     b=[]
#     for i in range(1,a):
#         if a%i==0:
#             b.append(i)
#     b.append(a)
    
#     return b

# print(abc())

# 최대공약수 공배수 구하기

# import numpy as np

# a=np.random.randint(0,500)
# b=np.random.randint(0,500)
# def c():
#     a1=[]
#     b1=[]
#     c1=[]
#     for i in range (1,a):
#            if a%i==0:
#             a1.append(i)
#     a1.append(a)

#     for i in range (1,b):
#         if b%i==0:
#             b1.append(i)
#     b1.append(b)
#     for i in a1:
#         if i in b1:
#             c1.append(i)
#     return a1,b1,np.max(c1)

# print(c())
# import numpy as np
# a=np.random.randint(0,1000)
# b=np.random.randint(0,1000)
# a=list(str(a))
# b=list(str(b))
# print(a,b)
# def abc():
        
#         for i in range(len(a)):
#             a[i]=int(a[i])
#         for i in range(len(b)):
#             b[i]=int(b[i])
#         a.reverse()
#         b.reverse()
#         c=0
#         d=0
#         q=0
#         for i in range(0,len(a)):
#             k=10**i
#             j=a[i]*k
#             c+=j
#         d=c
#         c=0
#         for i in range(0,len(b)):
#             k=10**i
#             j=b[i]*k
#             c+=j
#         q=c

#         return d,q
# print(abc())

# 2진수 a=0

# 임의의 유리수 문제 만들기
# import numpy as np
# from fractions import Fraction
# class Rational_number:
    
#     def question(self):
#         self.constant=np.random.randint(low=-10,high=10,size=4)
        
#         self.pm=np.random.randint(4)

#         if self.pm==0:
#             print('({}/{})+({}/{})= ?'.format(self.constant[0],self.constant[1],self.constant[2],self.constant[3]))

#         elif self.pm==1:
#             print('({}/{})-({}/{})= ?'.format(self.constant[0],self.constant[1],self.constant[2],self.constant[3]))

#         elif self.pm==2:
#             print('({}/{})*({}/{})= ?'.format(self.constant[0],self.constant[1],self.constant[2],self.constant[3]))
#         else: print('({}/{})/({}/{})= ?'.format(self.constant[0],self.constant[1],self.constant[2],self.constant[3]))
    
#     def answer(self):
#         if self.pm==0:
#             return Fraction(self.constant[0],self.constant[1])+Fraction(self.constant[2],self.constant[3])
#         elif self.pm==1:
#             return Fraction(self.constant[0],self.constant[1])-Fraction(self.constant[2],self.constant[3])
#         elif self.pm==2:
#             return Fraction(self.constant[0],self.constant[1])*Fraction(self.constant[2],self.constant[3])
#         else: return Fraction(self.constant[0],self.constant[1])/Fraction(self.constant[2],self.constant[3])

# a=Rational_number()
# a.question()
# print(a.answer())

# 분수를 유한소수로 나타내기 (분수의 분모가 2 또는 5로만 이루어져 있으면 유한 소수가 된다.)
# from fractions import Fraction

# def prime(a):
#     b=range(2,a)
#     primes=[]
#     for i in b:
#         while a%i==0:
#             print(a,i)
#             primes.append(i)
#             a/=i    #a를 초기화 해주는 역할이며, 여기서 바꾼 a는 def 전역에 영향을 미친다.
#             print(a,i)
#     print(a)
#     if primes==[]:
#         prime.append(a[i])
#     return primes

# from fractions import Fraction

# def check(x):
#     origin=x
#     a=range(2,x)
#     b=[]
#     for i in a:
#         while x%i==0:
#             x=x/i
#             b.append(i)
#     for i in b:
#         if i==2 or i==5:
#             continue
#         else:
#             return str(origin)+" is infinite"
#     return str(origin)+" is finite"
    

# print(check(20))

# 두 수가 주어지고 첫째가 분자 둘째가 분모, 이게 유한소수의 조합인지 무한소수인지
# Fraction으로 나온 최종 값은 약분이 다 된 값임. 즉 더 이상 나누어지지 않는 상태의 값이며 이 때 분모에 여전히 2와5이외의 값이 존재하면, 무한소수이다.
# from fractions import Fraction

# def check(x,y):
#     a=Fraction(x,y)
#     print(float(a))
#     b=a.denominator
#     c=range(2,b+1)
#     for i in c:
#         while b%i==0:
#             b=b/i 
#             if i!=2 and i!=5:
#                 return "무한소수"
    
#     return "finite"
# check(36,256)

# 짝수이면 트루를, 돌려주는 람다 함수를 만들고 ,1~10까지 적용.

# import numpy as np
# a=lambda x:x%2!=0
# c=np.array([1,2,3,4,5,6])
    
# print(a(c))

# 

from unittest import TestProgram


dic={"TP":25,"FN":15,"FP":35,"TN":25}

accuracy=dic["TP"]/sum([dic[x] for x in dic])
precision=dic["TP"]/(dic["FP"]+dic["TP"])
recall=dic["TP"]/(dic["FN"]+dic["TP"])
f1score=2*(precision*recall)/(precision+recall)
fpr=dic["FP"]/(dic["FP"]+dic["TN"])
SENSITIVITY=dic["TP"]/(dic["TP"]+dic["FN"])

# TestProgramSPECIFICITY(TNR)


if __name__=="dd":
    print("Dd")
elif __name__=='__main__':
    print("main")