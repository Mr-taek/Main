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

3. 글자 넣기
    1. axis객체.text(그래프의x위치,y위치,넣을글씨,글씨크기["large"])
# 그래프의 틀
    - 그래프 만들기
        1. obj= plt.figure() : 그래프의 틀 정보 설정, figure()자체가 하나의 메모리 주소이다. 해당 figure객체로부터 발생한 axes들은 원래의 figure에 포함된다
            - axis=obj.add_subplots() : figure객체의 메모리 주소를 담은 axis을 만드는 방법. 주로 projection="3d"할 때 이렇게 사용했다
            - parameters : 단일 figure, subplots 생성때 사용가능하다
                1. figsize : tow-element tuple, width and height in inches of windows, default = [6.4,4.8]
                2. dpi : float,resolution. 그냥 창의 크기 없는게 나을 수도
                3. facecolor : 바탕색,'red,green,blue..'등 있음
                4. edgecolor : 경계선 컬러
                5. tight_layout : bool or dict,
                6. frameon : default = True, if False Suppress drawing the figure frame -> facecolor도 동작하지 않게 됨.

        2. fig,axex=plt.subplots(nrows=default 1,ncol?=default 1) : norws는 한 개의 figure에 몇개의 행을 만들 것이란 의미이다. fig하나와 해당 fig에 포함되는 axis 를 리턴한다.            - parameters : 아래것을 제외한 모두 1번 .figure()의 것과 동일하다.
    - 그래프 축/눈금(axis/tick) 다루기
        1. axis객체.spines["right"/"left"/"top"/"bottom"]: axis의 상하좌우 축의 객체를 value로 포함하는 dict.
            - 사용 요령 : dict객체임으로 axis객체.spines.items()로 
            - 함수
                1. .set_visible(True(default)/False) : 선택된 축의 보이기 여부를 결정한다
                2. .set_linewidth(number) : 축의 두께를 변경한다
                3. .set_position("center"/("axis"/"data",비율)) : 축의 위치를 변경한다. ("axis",0)은 축의 비율상 중심에 맞춤을 의미하며,("data",0)은 눈금글씨의 데이터의 기준으로 중심을 맞춤을 의미한다 따라서 y축의 1에 맞추고 싶다면 axis.spines["bottom"].set_position(("data",1))로 맞춘다
                4. .set_alpha(0.0~1.0) : 축의 투명도를 변경한다
                5. .set_color(color) : 축의 색을 변경한다
                6. 
             - e.g : 일반적인 sin파형 그래프 만들기
                ```
                wavelength=np.arange(-10,10,1)
                sine=np.sin(wavelength)
                fig,axes=plt.subplots()
                axes.spines["right"].set_visible(False)
                axes.spines["top"].set_visible(False)
                axes.spines["left"].set_position("center")
                axes.spines["bottom"].set_position("center")
                axes.plot(wavelength,sine)
                plt.show()
                ```
        2. axis객체.tick_params() : tick은 눈금을 의미한다. 눈금을 조절한다
            - parameters
                1. axis = "x"/"y" , defalult=x,y. 눈금 파라미터를 적용시킬 축을 정한다. 없으면 아래의 모은 parameter는 두개 축에 적용된다
                2. labelsize : int, 눈금글씨 크기 조절
                3. laength : 눈금선의 길이 조절
                4. width : int, 눈금선의 두께 설정
                5. bottom(default)/left(defaylt)/top(False)/right(False)=True는 보이기 False는 안 보이기. 눈금선 없애기/보이기
                6. labelleft(default)/labelbottom(default)/labelright(False)/labelleft(False)=True는 보이기, 눈금 글씨(label) 없애기/보이기
                7. 5번 6번 한번에 적용
                    1. axis객체.get_xaxis()/.get_yaxis().set_visible(False/True)
                8. rotation : degree, 눈금 글씨(label)의 글씨 회전. 180은 글을 반대로 돌리기, 90은 생각에 맡김. +는 반시계 -는 시계
                9. color : 눈금선의 색, 없으면 clolrs의 색을 따라감.
                10. colors : 눈금 글씨(label)의 색
                11. direction : in/out(default) , 눈금선이 뻗치는 방향
                12. which : 주("major") 눈금과 조("minor") 눈금을 지정한다.
         3. axis객체.xticks, axis객체.yticks : x,y축에 들어가는 값을 넣어주기. np.arange나 list안에 있는 값이 해당 축에 값으로 반영된다. 반드시 number(int,float)만 가능하다
            - 주 눈금(major)과, 주 눈금 사이에 작은눈금(minor) 만들기
                ```
                major=np.arange(0,100,10) -> 0,10,20,...
                minor=np.arange(0,100,2) -> 0,2,4,6,8,10 ... 으로 사이사이에 등장
                axis.set_xticks(major)
                axis.set_xticks(minor,minor=True)
                axis.tick_params(axis='x') 
                axis.tick_params(axis='x',which='minor') # which가 꼭 필요하댐.
                ```
         4. axis객체.set_xlim, axis객체.set_ylim : 3번과의 차이는 최소 최대값만 지정가능하며 그 사이에 값의 범위는 정하지 못함
         5. axis객체.xticklabels()/ axis객체.yticklabels() : .set_xticks()가 먼저 기준을 정하고, 그 기준에 값(글)을 덮어 씌우기. 숫자만 가능한 xticks에 string을 얹을 수 있다.
            - 구현방법
                ```
                fig,axes=plt.subplots()
                mainlabel=np.arange(0,100,20)
                replacelabel=["hi","what","ho","thankyou","good"]
                axes.set_xticks(mainlabel)
                axes.set_xticklabels(replacelabel)
                plt.show()
                ```
             - parameters
                1. ha(horizontal alignment) : center/right/left, 세팅한 글의 위치를 조정하기. center는 눈금 중앙과 일치, right는 글 오른쪽을 눈금선에 맞추기, left는 글 왼쪽을 눈금선에 맞추기
          6. axis객체.set_xscale()/.set_yscale() : 값이 10000000000 , 100000000002 .... 이렇게 되면 크기가 너무커서 figure에 표현이 어렵다. 따라서 값의 크기(scale)을 조정하는 작업인 scaling이 필요하다.
            - parameters
                1. "log"
        - 그래프 그리드(grid) 만들기
            1. 설명 : axis객체.grid()로 사용합니다. ticks(눈금선)을 기준으로 만들어지기 때문에 눈금선이 많을 수록 그리드도 많아집니다
            2. axis객체.grid()
                - parameters
                    - axis : 'x'/'y' , 특정 축에만 grid를 생성할지의 여부. 없으면 x,y둘다 생성된다
                    - linewidth : grid의 선 두깨를 조절한다.
                    - linestyle : ":"/"-."/"--"/"-" , 4가지 라인스타일로 grid 그리기가 가능하다 
                    - color : color모음 확인, grid의 색을 결정한다.
                    - which : "major"/"minor", .x/yticks()에서 minor=True/1이 된 다음, minor로 지정된 ticks에 적용되는 grid가 만들어 진다.
            3. grid의 격자를 좁히고 싶다면 set_?ticks()를 사용해서 grid의 폭을 조정해야한다.
            
            4. 
                    
                    
                    
                    
                    
        - 비적절한 내용 다른 곳으로 옮겨야함. plot에 더 적절한 내용들 -----
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
