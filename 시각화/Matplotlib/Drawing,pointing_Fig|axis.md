1. figure객체.plot(),add_subplot객체.plot : plt.plot은 가장마지막에 등장한 subplot을, add~객체는 특정 subplot을 지정
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

