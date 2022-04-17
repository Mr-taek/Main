import numpy as np

Cvalues=[25.1,23.5,23.5,24] # 값들 중간 중간 ","를 써야 리스트로 인식이 된다. 이것이 일반적인 리스트 type 객체이다.

print(Cvalues)
print(type(Cvalues[3]))#24는 정수형이다.
C=np.array(Cvalues) # 파이선의 리스트를 넘파이 배열로 바로 바꿀 수 있으며, 이는 앞으로의 연산에서 시간과 복잡성을 덜어주게 된다.
print(C)            # 또한 넘파이 배열은 자동으로 값의 형태를 변경시켜준다. 값 중에 24는 정수지만, 다른 값들은 실수이므로 자동으로 실수로 바뀐다.
print(type(C[3]))#24는 넘파이의 실수형이다.

# 위 배열을 모두 특정 operator로 모두 계산하고 싶다.

Fvalues=Cvalues*5# 결과는 참혹했다.
print(Fvalues)
Fvalues=[x*5 for x in Cvalues]#이렇게 해야 내가 원하던 결과가 나온다.
print(Fvalues)
F=C*5#넘파이 배열로 계산시 쉽게 내가 원하던 결과가 나온다. np.linspace() 예외.
print(F)