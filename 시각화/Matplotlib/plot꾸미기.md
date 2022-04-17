# 색상 마커 선 스타일

1. plt.plot(x,y,linestyle='--',color='g',marker='o')
    - parameter
        1. color : 'r''g''b'
        2. linestype='dashed','--'
        3. marker='o'
        4. drawstyle='steps-post'
        5. label='name'

2. plt.legend()

# 눈금 라벨 범례

- 그래프를 꾸미는 방법은 크게 2가지.
    1. pyplot 인터페이스 사용해서 순차적으로 꾸미기(matplotlib.pyplot를 뜻함)
    2. maplotlib 에서 제공하는 API를 사용해서 객체지향적으로 꾸미기
※명심!※ 아래 모든 메소드는 가장 최근에 생성된 AxesSubplot(아마 그냥 subplot을 말하는 거인 듯) 객체에 동작한다. 그리고 set/get 메소드로 존재함.
- source code
    ```
    fig,subplot[ax로사용될것임]=plt.subplots(1,1)
    subplot.plot(np.random.randn(1000).cumsum())
    plt.show()
    ```

### x축의 눈금을 변경하기 위한 가장 쉬운 방법
1. ax.set_xticks([0,250,500,750,1000]) : x축의 scale을 지정

1. ax.set_xticklabels(['one','two','three','four','five'],rotation=30,fontsize='small') : font는 문자열의 특징을 말한느 것.

1. ax.set_title('My first matplotlib plot')

1. ax.set_xlabel('Stages')

### 범례 추가하기

1. ax.legend(loc='best')제일 쉬운 방법, 각 그래프에 label parameter 입력
    - parameter
        1. loc : 범례를 그래프 어디에 위치 시킬 지 지정해줌
    - EX
    ```
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.plot(np.random.randn(1000),label='one')
    ax.plot(np.random.randn(1000),label='two')
    ax.plot(np.random.randn(1000),label='three')
    # 이렇게 하면 plt.legend()시 자동으로 범례가 생성된다.
    ax.legend(loc='best')
    ```

### 주석과 그림 추가하기
1. text
2. arrow
3. annotate


### 도형추가

1. plt.Ractangle()
2. plt.Circle()
3. plt.Polygon()