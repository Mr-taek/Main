# linspace(start, stop, num=50, endpoint=True, retstep=False),start: 값의 시작, stop: 값의 끝, num: 시작과 끝 값 인덱스와 사이 인덱스의 총합
# endpoint=값의 끝을 포함할 지를 결정. retstep: 값을 출력할 뿐만 아니라 값들의 증감 값을 함께 포현하며, type을 numpy.ndarray가 아닌 tuple로 변화까지 시킨다.
# arange 처럼 인덱스 각각에 값에 곱하기가 불가능하다. range와 같은 성질을 가진 함수이다.
import numpy as np

a=np.linspace(1,10,9,retstep=True,endpoint=True)
