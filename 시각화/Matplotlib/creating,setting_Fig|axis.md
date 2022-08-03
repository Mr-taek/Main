# API SITE : https://matplotlib.org/stable/api/pyplot_summary.html
1. import matplotlib.pyplot as plt 로 import한다.

2. plt.plot() : 
    - 사용법
        1. plt.plot(DataFrame obj)
        2. plt.plot(obj.loc[~],obj[~])
# histogram 만들기
1. plt.hist()
    - parameter
        1. x_array : 1/2차원 까지 됨. 2차원은 무슨 뜻인지 모르겠음. 아무튼, 1차원 안에 값의 개수를 자동으로 계산, x축은 등장 값, y축은 등장 값의 횟수
# 그래프의 설명란 다루기
1. fig.set_title() : x축 제목 만들기

2. axis.set_xlabel('str') , axis.set_ylabel('str') : x축 y축 이름 만들기.
3. 축 설정하기
   1. axis객체.spines["right"/"left"/"top"/"bottom"].set_visible(True(default)/False) : axis의 좌우상하의 line의 visible을 선택한다
   2. axis객체.tick_params(labelleft=True(default),labelbottom=True(default),left=True(default),bottom=True(default))
4. 글자 넣기
    1. axis객체.text(그래프의x위치,y위치,넣을글씨,글씨크기["large"])
# 그래프의 틀
    - 그래프 만들기
        1. obj= plt.figure() : 그래프의 틀 정보 설정, figure()자체가 하나의 메모리 주소이다. 해당 figure객체로부터 발생한 axes들은 원래의 figure에 포함된다
            - axis=obj.add_subplots() : figure객체의 메모리 주소를 담은 axis을 만드는 방법. 주로 projection="3d"할 때 이렇게 사용했다
            - parameters : 단일 figure, subplots 생성때 사용가능하다
                1. figsize : tow-element tuple, width and height in inches of windows
                2. dpi : float,resolution. 그냥 창의 크기 없는게 나을 수도
                3. facecolor : 바탕색,'red,green,blue..'등 있음
                4. edgecolor
                5. tight_layout : bool or dict,

        2. fig,axex=plt.subplots(nrows=default 1,ncol?=default 1) : norws는 한 개의 figure에 몇개의 행을 만들 것이란 의미이다. fig하나와 해당 fig에 포함되는 axis 를 리턴한다.
    - 그래프 축 다루기
        1. axis객체.vlines(y축의center지점(2D->(,),3D->(,,),Y축의MIN,Y축의MAX,colors=color설명란참고) : 그래프의 수직선을 긋는다
        2. axis객체.hlines(x축의center지점(2D->(,),3D->(,,),x축의MIN,x축의MAX,colors=color설명란참고) : 그래프의 수평선을 긋는다
    - 그래프 여닫기
        1. plt.show() : 지금까지 생성된 모든 fig 객체를 show한다
        2. plt.close() : 지금까지 생성된 모든 fig 객체의 메모리를 해제한다. show하고나서 다음에 또 fig가 나올게 있으면 반드시 해줘야한다.
    - 그래프 여백
        - ※ FIGURE의 공간은 0~1로 이루어져 있다. 0은 제일 왼쪽을 의미하며 0.5는 CENTER을 의미한다. 방향은 왼쪽에서 오른쪽이다. 즉 가장 오른쪽은 1.0이다. 위아래는 가장 아래가 0이며 가장 위가 1.0이다.
        1. fig객체.subplots_adjust()
            - left/right/bottom/top : float(0.0~1.0)
# (중요) axe 객체 : plt.figure에서 만들어진 그래프 틀을 기반으로 다양한 plot객체를 생성하는데, 여기서 만드는 객체를 axe객체라 함.
1. 사용법
```
fig=plt.figure(dpi=152.5,facecolor='black')//해상도 152.5, 배경색 검은색
axe1=fig.add_subplot(1,2,1)//1개의 행과 2개의열을 1번 인덱스에 위치
axe2=fig.add_subplot(2,2,2)//2개의 행과 열 2번 인덱스에 위치
```
