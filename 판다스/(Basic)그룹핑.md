- SQL 이 인기 있는 이유 중 하나는 데이터를 쉽게 합/변형/분류 할 수 있기 때문. 그러나, 그룹 연산에 제약이 있음.

- 이것과 달리 PYTHON+PANDAS 조합으로 아주 쉽고 빠르고 정확한 그륩 연산이 가능하다.

1. Grouping
    1. .groupby()
        - parameter
            1. by :  Using func is most common way to use by. must come by discrete scale.
            2. axis : 0과1인데, 왠만하면 1(column)은 안 쓸듯.0을 기준으로 평균을 냄. default=0. 1을 선택한 것은 해석적으로 보통 인덱스에는 사람 이름이 있다면 열은 상품이니 각 상품별로 해당 상품이 골라진 총 개수. 이해를 돕고자 행인 경우는 각 사람이 여러 상품을 각각 고른 개수.
        - Example
            1. by
                1. dataframe과 col 명시
                ```
                data=pd.DataFrame(dic)
                g=data.groupby(data['place'])
                또는
                g=data.groupby([data['place'],data['year']])
                이 경우 place기준으로 먼저 묶고 그 다음 year기준으로 데이터를 묶는다.
                ```
                2. 그냥 column이름만 써주기
                ```
                data=pd.DataFrame(dic)
                g=data.groupby(['place','year'])
                ```
                3. function이용해서 grouping
                    1. len
                    ```
                    
                    ```
        - Example 2 : axis=1일 경우, 이해 잘 안감 그래서 안하려구.
            1. 
            ```
            data=pd.DataFrame([[1,1,0,0,1],
            [1,0,0,0,1],
            [1,1,1,1,1],
            [1,0,0,0,0]],
            columns=['a','b','c','d','e'],index=['cal','deril','meggi','grims'])
            dic={'a':'red','b':''blue','c':'red','d':'blue','e':'orange'}
            g=data.groupby(dic,axis=1)
            ```
2. Groupby의 메소드 : 대부분 NA값은 무시하고 계속 계산한다. 대박인 것은 숫자 메소드면 숫자만, 그외 애매하면 케릭터 컬럼도 출력해준다.
    1. .mean()

    2. .size() : 최종 각 그룹에 묶여있는 데이터의 개수를 출력\
        ```
        df=pd.Dataframe(~)
        g=df.groupby([])
        ```
    3. count()

    4. median()

    5. std(), var()

    6. min(),max()

    7. prod() : 모두 곱하기.

    8. first,last() : 첫번째,마지막 값

    9. 자신만의 집계함수 :data.groupby().agg(func)/aggregate(func)을 사용한다.
        ```
        dicc={'gov':['kor','jan','chi','rus','vie','mon'],
        'era':[1950,1895,1950,1886,1955,1955],
        'pre':['mon','xi','hon','put','ang','chan'],
        'pla':['asi','asi','asi','ura','asi','asi'],
        'gdp':[356.6,658.6,815.6,321.5,156.6,100.5]}
        def my_f(arr):
        return arr.mean()
        rst=pd.DataFrame(dicc).groupby('pla').agg(my_f)
        print(rst)
        ->
              era     gdp
        pla
        asi  1941.0  417.58
        ura  1886.0  321.50
        ```