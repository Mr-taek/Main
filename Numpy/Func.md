# np.random

1. .choice()
    - parameter


2. .loadtxt

3. nditor() : 넘파이의 iterator API
    - class numpy.nditer(op, flags=None, op_flags=None, op_dtypes=None, order='K', casting='safe', op_axes=None, itershape=None, buffersize=0 )
    : 기본적으로 입력의 첫번째 인덱스만 읽으며, 입력된 데이터를 1 차원 베터로 무조건 축소시킨다.(이를 방지하기 위해 flags=['multi_index'])로 다수 인덱스를 허용시킨다.)
    * flags=['String'] : 항상 리스트 또는 튜플형태로 주어져야함.
        + String:
            -  external_loop: 모든 입력 데이터를 1차원 array로 변환.
            -  multi_index: 다차원 입력을 그대로 유지시켜준다.
    * op_flags

    #### 예제 1 , single array iteration
    ```
    import numpy as np
    a=np.arange(start=0,stop=9,step=1).reshape(3,3)
    b=np.zeros_like(a)
    for x in np.nditer(a):
        print(x,end=' ')
    ```

    **설명**: nditer의 가장 기본 작용은 모든 sequence type의 element에 접근하는 것이다, 각 element는 파이썬의 iterator interface를 사용해 접근된다.

    ```
    import numpy as np
    op=np.array([[10,20,30,40],[1,2,3,4]])
    a=np.nditer(op)
    for x in op:    # op의 len은 2이므로 0,1 두번 실행한다.
        print(x)
        print(op)
        op[...]=2*x 

    print(op)
    ``` 
4. .unit_zero(),ones_like(),zoers_like() : 단위 행렬과 제로 행열(2-D) , or 배열.

    - Ex 1) 단위 배열: 배열의 형태선언과 함께 인자를 튜플 데이터 타입으로 취해서 배열을 채운다(하지만 크게 중요하지는 않는 듯). default Dtype: float
    ```
    import numpy as np
    e= np.ones(shape=(3,3),dtype=int)   # e= np.ones((3,3),dtype=int)
    print(e)
    print(type(e[1][1]))    #보다시피 튜플타입이 아니라 numpy.int 인 클래스의 데이터 타입이다.
    ```
    - Ex 2) zero 배열: 단위 배열과 같은 특징이다.
    ```
    #z= np.zeros((4,3))
    #print(z,type(z))    # class<numpy.ndarray>타입이다.
    ```
    - Ex 3) ones_like(다른배열) , zoers_like(다른배열): 다른배열의 shape와 같으면서 zero or ones 로 채워진 행열을 만든다.
    ```
    x=np.array([[1,2,3],[2,3,4],[4,5,2]])
    a=np.zeros_like(x)
    b=np.ones_like(x)
    print(a,type(a))
    print(b,type(b))
    ```

5. .copy()
    - parameter
        1. obj : 복사할 array
        2. order : order: 'C' 'F' 'A' 'K' 가 있는데, "K" 가 default
            1. C : C언어의 순서..?
            2. F : 포트란의 순서
            3. A : obk객체가 포트란 연속체면 F를 의미 아니면 C를 의미
            4. K : obj의 Layout을 최대한 일치시키기
    
    - EX 1 : np.copy(obj, order='K') order의 default='K'
    ```
    a=[[1,2],[2,3],[3,2]]
    x=np.array(a,order='K') # order을 다 적용해 봤지만 변화가 없음..
    print(x)
    y=np.copy(x)
    print(y,type(y))
    ```

    - EX 2 : 배열변수.copy(No argument)
    ```
    b=[[1,2],[52,13],[32,13]]
    c=np.array(b)
    d=c.copy()  #이렇게 카피도 가능.
    print(d,type(d))
    ```

6. .shape() : shape 함수는 배열의 차원에 대한 모양을 정수의 튜플로 반환한다.
    - 오로지 넘파이 배열 형태만 shape가 가능하며, 반드시 배열의 행과 열의 총 개수의 합과 같은 값으로 shape 해야한다.ex) 3X6(9) -> 7X2(9)OR -> 5X4

    - EX
    ```
    a=[1,2,3,4,5]
    b=np.array(a)
    # a.shape=(5,1)
    # ->  np의 array형태만  shpape가 가능.
    b.shape=(5,1)
    print(b)
    ```
7. matmul/dot : numpy에는 matmul 기능이 있음. tf도 있으며, tf와 np는 상호작용이 가능.
 - 주의 : matmul과 dot에는 2차원 계산은 서로 다름이 없지만 3차원부터는원리가 달라진다.
    - 원리차이
        1. matmul
        2. dot
    - 사용법 2차원
    ```
    c=np.matmul(a,b)
    d=tf.matmul(a,b)    
    ```

    - 연구중
    ```
    a=np.array([[
        [1,2,3,4],
        [4,3,2,1]
    ],[
        [0,1,1,0],
        [1,2,3,4]
    ]]) # 2,2,4

    b=np.array([[
        [1,1],
        [1,1],
        [1,1],
        [1,1]
    ],[
        [1,1],
        [1,1],
        [1,1],
        [1,1]
    ]]) # 2,4,2
    ```

8. .dtype
    - EX
    ```
    d=np.array([1+2j,2+4j,5+6j])
    print(d.dtype,d)

    d=np.array([True,False,True])
    print(d,d.dtype)

    d=np.array(['nohao','lala','xiexie'])
    print(d,d.dtype)
    ```
9. .ndim