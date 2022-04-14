# 단위 행렬과 제로 행열(2-D) , or 배열.

#Ex 1) 단위 배열: 배열의 형태선언과 함께 인자를 튜플 데이터 타입으로 취해서 배열을 채운다(하지만 크게 중요하지는 않는 듯). default Dtype: float
import numpy as np

#e= np.ones(shape=(3,3),dtype=int)   # e= np.ones((3,3),dtype=int)
#print(e)
#print(type(e[1][1]))    #보다시피 튜플타입이 아니라 numpy.int 인 클래스의 데이터 타입이다.

# Ex 2) zero 배열: 단위 배열과 같은 특징이다.
#z= np.zeros((4,3))
#print(z,type(z))    # class<numpy.ndarray>타입이다.


#  Ex 3) ones_like(다른배열) , zoers_like(다른배열): 다른배열의 shape와 같으면서 zero or ones 로 채워진 행열을 만든다.
x=np.array([[1,2,3],[2,3,4],[4,5,2]])

a=np.zeros_like(x)
b=np.ones_like(x)

print(a,type(a))
print(b,type(b))