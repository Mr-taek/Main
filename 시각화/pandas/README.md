# Series 와 DataFrame class 는 모두 plot 메소드가 있음

1. a=pd.Series(np.random.randint(10),cumsum(),index=np.arange(0,100,10)) - > a.plot() : Series임으로 index는 x축으로 자동 해석 된다.
    - parameter
        1. use_index : bool, index가 x축으로 사용되는 것을 조절가능.