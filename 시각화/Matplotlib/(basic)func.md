### Matplotlib 제일 기본적으로 사용
# API SITE : https://matplotlib.org/stable/api/pyplot_summary.html
# API의 인자는 사이트를 통해 참고해서 사용하고, 이곳에 쓰여진 함수, 속성들은 모두 기본적으로 사용되는 것들임.
# plt.plot 을 위해선 x의 데이터 값과 y로 사용할 데이터 값의 숫자가 같아야한다. 즉 x데이터 숫자=y데이터 숫자 이어야 한다.
1. import matplotlib.pyplot as plt 로 import한다.

2. plt.plot() : 
    - 사용법
        1. plt.plot(DataFrame obj)
        2. plt.plot(obj.loc[~],obj[~])
# histogram 만들기
1. plt.hist()
    - parameter
        1. x_array : 1/2차원 까지 됨. 2차원은 무슨 뜻인지 모르겠음. 아무튼, 1차원 안에 값의 개수를 자동으로 계산, x축은 등장 값, y축은 등장 값의 
# 차트 제목, 축 이름
1. plt.title()

2. plt.xlabel('str') , plt.ylabel('str') : x축 y축 이름 만들기.

# 그래프의 틀, 

1. obj= plt.figure() : 그래프의 틀 정보 설정.

2. ...

# (중요) axe 객체 : plt.figure에서 만들어진 그래프 틀을 기반으로 다양한 plot객체를 생성하는데, 여기서 만드는 객체를 axe객체라 함.
1. 사용법
```
fig=plt.figure(dpi=152.5,facecolor='black')//해상도 152.5, 배경색 검은색
axe1=fig.add_subplot(1,2,1)//1개의 행과 2개의열을 1번 인덱스에 위치
axe2=fig.add_subplot(2,2,2)//2개의 행과 열 2번 인덱스에 위치
```
