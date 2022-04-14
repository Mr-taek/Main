# shape 함수는 배열의 차원에 대한 모양을 정수의 튜플로 반환한다.
# 오로지 넘파이 배열 형태만 shape가 가능하며, 반드시 배열의 행과 열,의 총 개수의 합과 같은 값으로 shape 해야한다.ex) 3X6(9) -> 7X2(9)OR -> 5X4
import numpy as np

a=[1,2,3,4,5]
b=np.array(a)
# a.shape=(5,1)
# ->  np의 array형태만  shpape가 가능.
b.shape=(5,1)
print(b)