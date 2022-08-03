1. axis객체.plot():
    - parameter
        1. x:
        2. y:
        3. (zs) : 만약 add_subplot(projection="3d")일 때 사용된다. 이 경우 x와 y에 모두 s를 붙여준다
        4. fmt : str, 옵션이다. format string 자리임.라인 꾸미기에 사용됨. 라인 특성의 축약형임.
        5. data : ??
        6. color : 'r''g''b', 또는 바탕화면 색 이름 참고
        7. linestype : 'dashed','--'
        8. marker : 'o'
        9. drawstyle='steps-post'
        10. label : 해당 plot객체의 이름이다. 나중에 .legend()할 때 필수이다

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
2. axis객체.scatter()
    - EX)
        ```
        fig, (ax1,ax2,ax3) = plt.subplots(1, 3,sharex=True)

        ax2.scatter([1,2,3,4,5],[10,11,12,13,14]) - > x,y의 개수가 일치해야 한다.
        plt.show()
        ```

