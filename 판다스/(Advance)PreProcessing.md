- 차례
    1. 함수 맵핑
    2. 그룹 연산
    3. DataFrame 합치기, Structure modifing

### 함수 맵핑

#### apply()함수를 통해 리턴되는 객체 타입은, 리턴되는 Series들의 타입이 모두 같으면 같은 데이터 타입을, int,object 타입이면, object타입의 시리즈를 리턴

1. Series obj.apply(맵핑할 함수) : 인자인 맵핑함수에 obj객체의 모든 원소를 하나씩 입력하고 맵핑함수의 리턴 값을 받는다.
    - 특징 : Series객체가 가장 먼저 함수의 인자로 전달되고, 그 다음부터 함수의 다른 매개변수가 호출된다.
    - 리턴 값 : 시리즈의 원소 개수만큼 함수를 돌려서 같은 크기의 시리즈 객체를 반환한다.
    - 인자 종류
        1. func = : 적용할 함수의 이름을 넣기, 
        2. args = tuple() : Series객체가 먼저 통과 한 다음에 만약 함수가 다른 매개변수를 포함한다면, keyword 인수(함수의 매개변수 이름을 직접 선언하는 것) 로서 선언해야함.
    - ex)
        1. 
        ```
        def sub(n):
            return n-10;
        Sr1=data['num'].apply(sub) # 각 원소에 10을 뺀 시리즈 객체가 리턴된다.
        ```
        2. 
        ```
        def two(a,b):
            return a+b
        Sr2=data['num'].apply(two,b=10) # 키워드 인수(keyword argument) 선언
        OR
        Sr2=data['num'].apply(two,args=(15,65,...))
        ```
        3. lamda 함수 적용
        ```
        def Ga(n):
            return n-10;
        Sr3=data['num'].apply(lamda x: Ga(x))
        ```

### 데이터 프레임의 apply() 사용시 꼭 기억할 것.
- 설명 : 함수의 인자의 구성에 특히 유의하라. 함수는 최소 한 개이상의 매개변수를 갖고 있어야 한다. 데이터 프레임은 무조건 Series(데이터프레임 첫번째 열의)를 '첫 번째'인자로 보낸다. 이 때 첫번째 인자는 apply를 적용한 dataframe(ex:df.apply(),여기서 df)이다.
- 사용 규칙
    1. 함수의 두번째 인자부터 apply함수 인자에 이름과 똑같이 적어야 한다.
    2. 연산을 진행할 객체들 사이의 타입이 일치한 지 꼭 확인.
        + 오류시:#The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

1. DataFrame obj.apply(맵핑함수. axis=0/1) : (주의!) axis=0이면 데이터프레임의 열을 부분적으로 보내고 axis=1이면 행을 부분적으로 보낸다.
    - 설명 : 모든 "열을 하나씩 분리해서" 매핑 함수의 인자로 "각 열(Series)를 전달"하는데, (중요!) 함수에 따라 반환되는 객체의 종류가 달라짐.
    - 특징 : 결국엔 Series를 인자로 집어 넣는다. (중요!) 함수에 따라 반환되는 객체의 종류가 달라지고 형태가 달라진다. 즉 Series를 넣었을 때 int나 다른 타입이 나올 수 있다는 것이고 Sereise의 길이가 50이었던 것이 만약 Series의 함수인 .max()를 만나면 길이가 1인 Series객체를 반환함.
        + 추가 특징 : axis에 따라 데이터의 행과 열을 추출하는 것이 달라진다.
    - 종류
        1. 시리즈를 입력 받고, 시리즈를 반환하는 함수는 데이터 프레임을 반환한다.
        ```
        data=sns.load_dataset('titanic')
        df=data.loc[:,['age','fare']]
        def Isnull_ret(n):
            return n.isnull() # isnull은 각 개체가 null값인지 체크해주며 dataframe을 반환하는 함수다.
        ndata=df.apply(Isnull_ret)
        # 원본 데이터프레임과 크기가 같은 데이터 프레임 반환
        ```
        2. 시리즈를 입력받고, 하나의 값을 반환하는 함수는 시리즈를 반환한다.
        - 특징 : 리턴되는 시리즈의 인덱스는, 원래 시리즈의 열의 인덱스이다.
        ```
        def min_max(x)
            return x.max()-x.min()# 매개변수가 Series객체임을 안다면, max와 min의 사용을 예측할 수 있고, 또한 각 Series의 최대 최소만을 가져오기 때문에 Series의 크기가 원래 매개변수의 시리즈보다 작은 시리즈가 리턴된다.
        ```
        3. 람다함수의 사용
        ```
        import pandas as pd
        import seaborn as sns
        data=sns.load
        def func(n1,n2):
            return n1+n2
        #res=data['age'].apply(func,args=(data['fere']))이거는 불가능 꼭 함수의 매개변수를 명시해줘야함.
        print(res) # 두개를 더하기때문에..아마 하나의 시리즈가 나올 듯.
        ```
2. DataFrame obj.applymap(맵핑할 함수)
    - 특징 : 기존에 apply의 기능을 수행하지만 과정이 다름. apply는 Series별로 나눠서 함수에게 전달했다면 applymap은 원소 하나하나 넣어서 리턴받음. 방법은 apply와 같음.
    - 인자
        1. func = 함수이름
        2. na_action None(default)/'ignore' : ignore면 NaN값은 무시하고 다음 원소로 넘어감
        3. **kwargs : 추가적인 키워드 인자. 함수로 보낼 다른 인자들.
    ```
    data=dataframe.loc[:,['one','two']] # DataFrame 형태 객체
    Sr1=data.applymap(Func)
    ```

3. 실제 응용 예시
```
data=sns.load_dataset('titanic')
def funcc(n1,n2):
    return n1-n2
data=data.loc[:,['age','fare']]
res=data['age'].apply(funcc,n2=data['fare'])
print(res,data.head()) # 예측 : 두개를 더하기때문에..아마 하나의 시리즈가 나올 듯.
```
->
```
       0        1       2     3      4        5        6       7        8        9    ...      881      882  ...
0    14.75(22-7.25) -49.2833(14.75-71.2833)  14.075 -31.1  13.95  13.5417 -29.8625   0.925  10.8667  -8.0708  ...  14.1042  11.4833  
1    30.75(38-7.25) -33.2833(38-71.283)  30.075 -15.1  29.95  29.5417 -13.8625  16.925  26.8667   7.9292  ...  30.1042  27.4833    
2    18.75(18.75-7.25) -45.2833  18.075 -27.1  17.95  17.5417 -25.8625   4.925  14.8667  -4.0708  ...  18.1042  15.4833   
3    27.75 -36.2833  27.075 -18.1  26.95  26.5417 -16.8625  13.925  23.8667   4.9292  ...  27.1042  24.4833   
4    27.75 -36.2833  27.075 -18.1  26.95  26.5417 -16.8625  13.925  23.8667   4.9292  ...  27.1042  24.4833  
...  

[891 rows x 891 columns]     age     fare
0  22.0   7.2500
1  38.0  71.2833
2  26.0   7.9250
3  35.0  53.1000
4  35.0   8.0500
```

4. obj.pipe(매핑함수): 데이터프레임 객체만 넘기는 함수, 함수의 매개변수는 하나.
    - 특징 : 함수의 리턴 값에 따라 데이터 프레임, 시리즈, 단일 값을 반환한다.
    - 경우 
        1. 데이터프레임 반환 : return n.isnull()
        2. ... 중요성을 못 느껴서 일단 패스

### 열 재구성

1. 열 순서 변경
    - 방법 : 어떤 방법이 되던 최종적으로는 2번의 방법으로 열의 순서를 변경한다.
        1. DF -> LIST 타입변환 -> DF
        2. ndata=data[열이름이나열된리스트]
    - 예시
        1. sorted() : 리스트 안에 알파벳 순으로 정렬시켜줌
        ```
        columns=data.columns
        List=list(columns)
        column_sorted=sorted(List)
        New_data=data[column_sorted]# 
        ```
        2. reversed() : 리스트안에 순서를 반대로 바꿔준다.
        3. 직접 변경 : 직접 데이터 열의 이름을 기억하고 원하는 순서대로 리스트를 만들고 대입시킨다. 
            1. 열의 개수가 적은경우
                ```
                List=['라면','짜장','복밥']
                New_data=data[List]
                ```
            2. 열의 개수가 엄청 많은 경우
                1. column=data.columns # column 데이터에 대한 인덱스 순서 확보
                2. 터미널에 띄운 다음 싹다 복사해서 내가 만든 리스트 안에 집어넣기.
                3. 이제 마우스로 왔다 갔다..
                ```
                Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
                'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
                'alive', 'alone'],
                dtype='object')
                ```
                -> List라는 객체에 복사해서 이 안에서 순서를 바꾸고 데이터프레임에 대입
                ```
                List=['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
                'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
                'alive', 'alone']
                data=data[List]#[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
                #'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
                #'alive', 'alone']]
                ```

2. (Series 전용)열 분리
    - 방법 : pandas에서 str 데이터를 다루는 함수 .str 을 사용
        1. .str.split('-' or '?' ..) : 문자를 인자의 값으로서 분리시키고 분리시킨 문자를 리턴한다.
        ```
        Area=pd.Series(['인천-중구','인천-남구'])
        NArea=d.str.split("-")
        ```
        ->
        ```
        0    [인천, 중구]
        1    [인천, 남구]
        dtype: object # 오브젝트지만 또 [0]찍으면 list 등장
        ```
        2. Series obj.str.get(인덱스) : 분리된 문자를 인덱스로 나눠서 새로운 열을 만든다
        ```
        data['광역시']=NArea.str.get(0)
        data['구']=NArea.str.get(1)
        ```
### 데이터프레임 합치기
- 설명 : 중요한 데이터가 한 곳에 있지 않고 여러 파일에 나누어져 있을 때 하나로 합치거나 데이터를 연결해야 한다.

- 사용 메소드 : pd.concat() , pd.merge(), pd.join()

1. pd.concat() : 아주 기본적인 데이터프레임 합치기 메소드. 합치고자 하는 데이터 프레임을 리스트로 묶어서 인자로 전달하면 된다.
    - 중요 특징 : axis=1일 경우에 가능하면 행 인덱스를 모두 정수형 인덱스로 한 상태에서 합친다. reset_index 메소드를 사용해서 합치려는 데이터의 행 인덱스를 초기화 해라.
    - 인자
        0. objs : List of dataFrame.
        1. axis : 0(default)/1 , join 인자의 영향을 받는다.
            - case
                1. axis=1 : 데이터프레임을 좌우 열 방향으로 연결한다. 행 인덱스는 그대로 유지한다. nan값이 발생한다, 아래 예시를 참고하자. 행 인덱스
                2. axis=0 : 데이터프레임을 아래 방향으로 연결한다. 행 인덱스는 그대로 유지한다. nan값이 발생한다, 아래 예시를 참고하자.
                ```
                    a   b   c   d               a   b   c               a   b   c   d
                0   1   5   6   8           2   3   3   3           0   1   5   6   8   
                1   2   3   3   4           3   5   6   4           1   2   3   3   4
                2   3   3   0   0       +   4   3   3   2       =   2   3   3   0   0   
                                                                    2   3   3   3   nan
                                                                    3   5   6   4   nan
                                                                    4   3   3   2   nan       
                ```
        2. join : 'outer'(default), 인덱스들을 합집합시킨다. 즉 어느것 하나 빼먹지 않고 모두 포함시켜 새로운 데이터 셋을 만듦. 'inner'는 인덱스를 교집합 시킨다, 즉 두 데이터간 같은 인덱스를 공유한 데이터들만 가져와서 새 데이터셋을 만듦. axis에 영향을 받는다. 1이면 열에 대해 같은 이름,숫자의 인덱스들만 가져옴.
        3. ignore_index : True, 합쳐지면서 서로 다른 두 데이터의 행 인덱스도 같이 붙여지는데, 기존의 행 인덱스를 무시하고 새롭게 인덱스를 만듦
        ```
            a   b   c   d               a   b   c   d
        0   1   5   6   8           0   1   5   6   8
        1   2   3   3   4           1   2   3   3   4
        2   3   3   0   0       - > 2   3   3   0   0
        2   3   3   3   nan         3   3   3   3   nan
        3   5   6   4   nan         4   5   6   4   nan
        4   3   3   2   nan         5   3   3   2   nan
        ```