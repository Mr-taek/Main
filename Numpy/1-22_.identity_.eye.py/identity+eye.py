# identity array: 주 대각선에 1이 있는 배열(정확히는 행열)을 의미한다.

# .identity(n, dtype=None):     n: 출력의 행 및 열 수를 정의하는 정수. 즉 nXn 행열.
import numpy as np

x=np.identity(4,dtype=float)
print(x)

# eye: identity와 조금 다르게 배열(꼭 행열이 아님)을 만들 수 있는 함수. 주 대각선을 자유롭게 바꿀 수 있으며 선택된 대각선에 1을 채운다.

# eye(N,M=N,k=0,dtype=float): N: 출력 배열의 행을 결정. M: 출력 배열의 열을 결정. default=N. k: 주 대각선의 위치. 0은 중앙,양수는 중앙에서 위,음수는 아래로 주 대각선 생성.
# ndarray type을 반환.
y=np.eye(5,k=3)
print(y,type(y))
y=np.eye(5,3)
print(y)