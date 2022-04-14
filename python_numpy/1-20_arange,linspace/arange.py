# arange(start, stop, step,  dtype(default=None)), start의 default=0,구간의 끝은 매개변수 stop의 값이 결정.step의 default=1,step이 주어지면 start는 꼭 지정되어야함.
#dtype은 주어지지 않으면 입력 인자들로부터 자동 유추되어 설정된다.
# arange "함수"는 파이썬의 내장함수 range와 유사하다. 그러나 range를 시각화 하기 위해선 list로 객체화 해야한다는 것이다(불편하다). 또한 만약 범위를 지정한 내부 
# 인덱스 각각에 특정 값을 곱해주는 것 자체도 for문을 사용해야하는 번거로움이 있다. np.arange는 그럴 필요가 없다.
import numpy as np

ran=range(1,10)
ranList=list(ran)
aran=np.arange(1,10)
print(ran)
print(list(ran))
print(aran)
#ran=ran*3
#  -> 파이썬 내부에서 range class는  아예 산술 연산 자체가 불가능하다.
#  -> 실행시 오류가 뜨는 것을 찾을 수 있으며 산술 연산자의 적용이 불가능하다고 뜬다.
print("type(ran)",type(ran),"range의 타입이 range 클래스 타입이라는 것을 볼 수있다.")
print("type(ranlist)",type(ranList)," range를 list 타입변화 list 형태로 변화하며")
print(ranList*3,"역시 예상과 다르게 엉뚱하게 아예 list의 길이가 늘어나는 것을 확인할 수있다.")
print("--------------------------------------------------")
aran=aran*3
print("aran=aran*3")
print(aran,"넘파이 aran에 *3을 하면 예상대로 인덱스마다 3이 곱해진 것을 확인할 수 있다.")
print("--------------------------------------------------")
p1=np.arange(start=1,stop=10,step=3,dtype=float)
print("p1=np.arange(start=1,stop=10,step=3,dtype=float)\n",p1)
p1=np.arange(start=1,stop=10,dtype=float)
print("p1=np.arange(start=1,stop=10,dtype=float)\n",p1)
p1=np.arange(stop=10,start=1,dtype=int)
print("p1=np.arange(stop=10,start=1,dtype=float)\n",p1)