1. plt.figure() : 최대 4개의 plot이 가능하다.
    - figure() 객체의 개수에 따라 나중에 show 할때 객체 개수만큼 뜬다.
        - ex
        ```
        a=plt.figure()
        b=plt.fugure()
        plt.show()
        -> 총 a와 b 두개 등장.
        ```
    - parameter(다 생략도 가능)
        - NUM : 그림 식별자, 번호/문자열 다 됨. 없으면 default 실행됨
        - figsize : tow-element tuple, width and height in inches of windows
        - dpi : float,resolution. 그냥 창의 크기 없는게 나을 수도
        - facecolor : 바탕색,'red,green,blue..'등 있음
        - edgecolor
        - tight_layout : bool or dict,

2. plt.subplot()

3. plt.close(figure객체) : 많은 figure 생성시 사용. 닫아야만 메모리 공간이 저장된다


1. figure객체.add_subplot()
    - parameter
        0. *args : int or (1.int,2.int,index) , index는 1부터 시작 그리고 index는 subplot할 위치에 1.행과 2.열만큼 plot만듦.
            - 중요! index가 tuple (1.int,2.int) 시 , 칸을 1.부터 2.까지 사용하겠다는 뜻임. 단 2는 홀수는 안 됨.
        1. projection : 그래프의 형태{None, 'aitoff', 'hammer', 'lambert', 'mollweide', 'polar', 'rectilinear', str} 중에 하나를 골라서 선택. str is a custom projection(직접제작)
        2. polar : bool, true면 projection에서 polar가 선택됨.
        3. 

1. plt.subplots() : figure와 subplot 동시 생성
    - parameter
        1. nrows,ncols : 행렬개념으로 subplot을 생성. 2,1 이면 위 아래 한 개씩 서브플롯이, 2,2면 총 4개가 생성.
            + EX)
                1. fig, (ax1,ax4,ax2,ax3) = plt.subplots(1, 4)
                2. fig, ((ax1,ax2),(ax2,ax3)) = plt.subplots(2, 2)
                3. fig, ((ax1,ax4,ax5),(ax2,ax3,ax6),(ax7,ax8,ax9),(걍하나더)) = plt.subplots(3, 4)
        2. sharex,sharey : bool, x,y축을 모든 서브플롯이 공유할 지 말 지를 결정하는 것. 공유시 가장 큰 범위 값을 갖는 서브플롯이 축 scale을 지배한다.
            + EX) ax1.plot(np.arange(0,50)),ax2.plot(np.arange(50,400)) -> ax2가 더 큼으로 ax2가 x축을 다 지배


2. figure객체.plot(),add_subplot객체.plot : plt.plot은 가장마지막에 등장한 subplot을, add~객체는 특정 subplot을 지정
    - parameter
        1. x,y : array-like or scalar. x vlaue는 옵션이며 없을 시 default로 len(y) 이다. 그런데 x,y는 굳이 써주지 말고
        ax3.plot(np.arange(0,50),np.random.randn(50)) 이렇게 해야 오류가 안남
        2. fmt : str, 옵션이다. format string 자리임.라인 꾸미기에 사용됨. 라인 특성의 축약형임.
        3. data : 

2. figure객체.hist()
    - parameter
        1. x : array/sequence
        2. bins : int/sequence/str/default=10
        3. range : 
        4. density

    - Ex)
        ```
        data=np.random.randint(0,10,20)
        data=np.sort(data) -> hist 검증을 위해 sort한 것.
        print(data) - > hist의 개수를 판단하기 위함
        fig, (ax1,ax2,ax3) = plt.subplots(1, 3,sharex=True)
        ax1.hist(data)
        plt.show()
        ```
2. plt.scatter()
    - EX)
        ```
        fig, (ax1,ax2,ax3) = plt.subplots(1, 3,sharex=True)

        ax2.scatter([1,2,3,4,5],[10,11,12,13,14]) - > x,y의 개수가 일치해야 한다.
        plt.show()
        ```


3. plt.show() : plt.plot으로 설정을 마친 plot을 화면에 보여준다.
    - EX)
        ```
        
        ```
4. subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=None,hspace=None)
    - 설명 : wspace와 hspace로 subplot간의 거리 차이를 조절가능.