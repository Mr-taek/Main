# 머신러닝등에서 데이터 분석의 정확도는 분석 데이터의 품질에 의해 좌우됨.

# 품질 향상을 위해 누락데이터, 중복 데이터 등의 오류를 수정하는 과정이 필요하다.

# 일반적으로 유효한 데이터 값이 존재하지 않는 누락 데이터를 NaN(Not a number)로 표시한다.

# 머신러닝 분석 모형에 데이터를 입력하기 전에 "반드시" 누락 데이터를 제거하거나, 적절한 값으로 대체해야한다. 누락 데이터가 많아지면 데이터 품질(신뢰성)이 떨어지고 머신러닝 분석 알고리즘을 왜곡하는 현상이 발생하기 때문이다.


### 누락 데이터 확인

1. Dataframe.info()
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890   // 총 891개의 행이 존재
Data columns (total 15 columns):    // 총 15개의 열이 존재
 #   Column       Non-Null Count  Dtype(값의 데이터 타입)
---  ------       --------------  -----
 0   survived     891 non-null    int64 // 891개의 행 중 891개의 값이 존재
 1   pclass       891 non-null    int64 // 891개의 행 중 891개의 값이 존재
 2   sex          891 non-null    object    // 891개의 행 중 891개의 값이 존재
 3   age          714 non-null    float64
 4   sibsp        891 non-null    int64 // 891개의 행 중 891개의 값이 존재
 5   parch        891 non-null    int64 // 891개의 행 중 891개의 값이 존재
 6   fare         891 non-null    float64   // 891개의 행 중 891개의 값이 존재
 7   embarked     889 non-null    object    // 891개의 행 중 889개의 값이 존재
 8   class        891 non-null    category  //범주형 데이터
 9   who          891 non-null    object
 10  adult_male   891 non-null    bool
 11  deck         203 non-null    category  // 891개의 행 중 203개의 값이 존재, 즉 나머지는 누락데이터임!! 
 12  embark_town  889 non-null    object
 13  alive        891 non-null    object
 14  alone        891 non-null    bool
dtypes: bool(2), category(2), float64(2), int64(4), object(5)
memory usage: 80.7+ KB
None
```

2. dataframe['열의이름'].value_counts(dropna=True(default)/False) : 특정 열의" 같은 값"의 횟수를 반환하는 Series 객체를 반환한다.
    - 같은 값? : 예를들어 'KBS'라는 열의 인덱스가 있고 그 열 안에는 '나가수' '올림픽'등의 str value가 있는데, '나가수'가 총 80번 있으면 Series객체에 '나가수'라는 key이름에 80이라는 value가 리턴된다.
    - ex 1)
        ```
        import seaborn as sns

        data=sns.load_dataset('titanic')

        print(data['age'].value_counts().sort_values()) // .values_counts()까지 하면 Seriese 객체를 반환하고 이 객체가 다시 sort_values()됨.
        ```
        ->
        ```
        74.00     1 //ascending이 True로 default임.
        34.50     1
        0.42      1
        0.67      1
        66.00     1
                ..
        28.00    25
        19.00    25
        18.00    26
        22.00    27
        24.00    30
        Name: age, Length: 88, dtype: int64
        ```
    - ex 2)
    ```
    print(data['embark_twon'].value_counts())
    ```
    ->
    ```
    Southampton    644
    Cherbourg      168
    Queenstown      77
    Name: embark_town, dtype: int64
    ```

3. DataFrame.isnull() OR DataFrame.notnull()
    1. DataFrame.isnull() : 이름 그대로 널(NaN) 값이니? - > 널이면 True, 널이 아니면 False
    2. DataFrame.notnull(): 널이 아니지? - > 널이 아니면 True , 널이면 False
    - ex
    ```
    import pandas as pd
    data=pd.read_excel('~',header=1)
    data.set_index(data.coloumns[0],inplace=True)//data의 데이터프레임의 0번 
    print(data.insull().sum()) // isnull이 DataFrame을 반환하고 모든 value는 bool type이다. sum은 True의 개수를 샌다.
    ```
    

### 누락 데이터 제거

- 용어(terms) : 레코드 = 한 행의 전체 변수값 = 관측값(행 인덱스 특징을 관측한 값) , 변수 = 열 = 특성

- 설명 : 누락데이터가 들어있는 열을 삭제하면 분석 대상이 갖는 특성을 제거한다. 행을 삭제하면 분석 대상의 관측값을 제거하게 된다.

- 누락데이터 삭제 과정
    - 데이터셋 인덱스 정보를 갖는 인덱스 객체를 만들기.
    - 각 인덱스 마다 내부에 포함된 NaN 개수를 찾기.
    - 누락데이터가 굉장히 많은 행, 또는 열을 삭제
    1. ex1) : 데이터셋의 각 "열"에 누락 데이터가 몇 개씩 포함되어 있는지 체크한다.
    ```
    import pandas as pd
    import seaborn as sns
    data=sns.load_dataset('titanic')
    data=data.isnull()
    colum=data.columns # colum의 인덱스를 인덱스 타입으로 리턴
    for col in colum:
        count=data[col].value_counts(normalize=True) #value_counts()함수를 통해 값의 빈도수를 나타내는 Series객체를 리턴,//normalize를 통해 백분율로, 전체 행 데이터중에 해당 데이터가 차지하는 백분율로 나타냄
        try:
            print(col,': ', count[True]) # Series객체에 key값 접근방법을 이용해 ket값이 나타내는 value를 출력
        except:
            print(col, ': ', 0)
    ```
    - ex2) : 직접한 것, 굳이 모든 데이터들을 True False가 아님
    ```
    import pandas as pd
    import seaborn as sns
    data=sns.load_dataset('titanic')
    col_index=data.columns
    for col in col_index:
        count=data[col].value_counts(dropna=False)# NaN 드랍 비허용으로 Seriese 객체에 NaN 인덱스(key) 허용
        #print(col,': ',count[NaN]), 이렇게 하려니 실패함. 이유는 각 Series마다 NaN 인덱스가 아예 없는 데이터도 존재하기 때문
        try:
            print(col,': ',count[NaN])
        except:
            print(col,': ', 0)
    ```
    2. 누락 데이터가 가장 많은 행 또는 열을 삭제한다.
    ```
    survived :  0
    pclass :  0
    sex :  0
    age :  0.19865319865319866
    sibsp :  0
    parch :  0
    fare :  0
    embarked :  0.002244668911335578
    class :  0
    who :  0
    adult_male :  0
    deck :  0.7721661054994389
    embark_town :  0.002244668911335578
    alive :  0
    alone :  0
    ```
    - deck 열이 가장 누락 데이터가 많으므로, 삭제한다.(누락데이터가 차지하는 비율이 매우 높다.)
        - 사용 API
            1. .drop() : 인자는 설명에 포면 쉽게 이해 가능.
                - ex
                ```
                data.drop(axis=1,labels='deck',inplace=True)
                ```
            2. .dropna(): datafram에 있는 데이터들중 조건에 해당되는 모든 행(axis=0) 또는 열을 아예 삭제(how=any)한다.
                - ex 1
                ```
                data.dropna(axis=1,thresh=670) # 열 축에서 670개 이상 NaN에 해당되는 열을 아예 삭제해 버린다.
                print(data)
                ```
                -> 결과 # deck 열이 사라짐.
                ```
                <class 'pandas.core.frame.DataFrame'>
                RangeIndex: 891 entries, 0 to 890
                Data columns (total 14 columns):
                #   Column       Non-Null Count  Dtype
                ---  ------       --------------  -----
                0   survived     891 non-null    int64
                1   pclass       891 non-null    int64
                2   sex          891 non-null    object
                3   age          714 non-null    float64
                4   sibsp        891 non-null    int64
                5   parch        891 non-null    int64
                6   fare         891 non-null    float64
                7   embarked     889 non-null    object
                8   class        891 non-null    category
                9   who          891 non-null    object
                10  adult_male   891 non-null    bool
                11  embark_town  889 non-null    object
                12  alive        891 non-null    object
                13  alone        891 non-null    bool
                dtypes: bool(2), category(1), float64(2), int64(4), object(5)
                memory usage: 79.4+ KB
                None
                ```
                - ex 2 : 좋은 방법같지는 않음. NaN 값이 일단 있는 행은 삭제 해버리기 때문임.. 1번 처럼 그냥 누락데이터가 많은 열을 직접 없애는게 좋을 듯.
                ```
                data.dropna(subset=['age'],axis=0) # 
                ```
### 누락데이터 치환

- 설명 : 누락데이터라고해서 행과 열을 막 삭제하면 결과의 질이 크게 떨어질 수 있다. 누락데이터가 있어도 다른 데이터는 의미를 갖기 때문이다.

- 누락데이터 대체를 위해 분포와 특성을 잘 나타낼 수 있는 값
    1. 평균값
    2. 최빈값
- pandas의 fillna() 메소드를 사용해 누락데이터를 채운다.
    1. int형 자료채우기
    ```
    mean_val=data[행이름].mean(axis=0)#default는 0이라 생략가능
    data[행이름].fillna(mean_val,inplace=True)
    ```
    ->
    ```
    mean_age=data['age'].mean(axis=0)
    data['age'].fillna(mean_age,inplace=True)# 주의 data.fillna(mean_age,inplace=True) 렇게하면, DataFrame자체에 fillna를하는것인데, value타입이 안맞는 #것들끼리 채워져서 오류가 남.
    ```
    2. str, object 타입 자료채우기
    ```
    frequence=data[행이름].value_counts().idxmax
    data[행이름].fillna(frequence,inplace=True)
    ```
    3.  연속되는 데이터 : 시간에 따라 연속적으로 변화하는 정보 채우기 : 엔트로피 변화, 온도 변화 등의 정보는 앞 또는 뒷 정보와 유사하다
    ```
    data['Temperature'].fillna(method='ffill',inplace=True) # 행의 앞쪽 데이터를 가져와 NaN데이터 채우기.
    또는
    ~.fillna(method='bfill',~)
    ```
    4. .replace()을 사용 : 가끔씩, NaN이 아닌 쓰레기 값('?','_' etc)이 존재한다. 이런 것들을 채워준다.(basic func의 공통함수 section참고)
    ```
    data['~'].replace(to_replace='?',values=np.nan,inplace=True)
    ```

### 중복 데이터 처리
- 설명 : 이전행 또는 다음행의 레코드 값과 현재 행의 레코드 값이 완전히 갖다면 굳이 중복되는 것들이 두개 이상 있을 필요가 없다. 

- 과정
    1. 행의 레코드의 중복여부를 확인한다.(pass가능)
        - .duplicated() 메소드를 사용한다.(basic func에서 공통함수를 참고),Series 객체를 리턴함.
        ```
        0      False
        1      False
        2      False
        3      False
        4       True
            ...
        886     True
        887    False
        888    False
        889    False
        890    False
        Length: 891, dtype: bool        
        ```
    2. 중복되는 레코드 제거
        - .drop_duplicates(arg)

### 데이터 표준화
- 설명 : 여러 곳에서 수집한 데이터들은 여러 원인으로 다양한 형태로 표현됨. 서로 다른 단위라면 비교가 어려워진다. 따라서 단위를 표준화하는 작업이 필요하다.

- 단위 변환 : 국가마다 사용하는 단위가 다르다.
    - Ex
    ```
    df['newColumn']=df['oldColumn']*New_unit # newCoulumn이라는 열에 Series형태의 객체를 대입한다. 
    df['newColumn']=df['newColumn'].round(2) # 열의 모든 값들에 대해 소수점 아래 2번째 자리서 반올림.
    ```
- 자료형 변환 : 숫자로 표현될 자료가 문자열(object)로 구성될 경우가 있다. 이는 잘못된 것이므로 자료형을 변환시켜야 한다.
    - 원인
        1. 데이터 안에 숫자 말고 '?' 또는 '_'등의 문자가 존재할 경우.
        2. 국가 이름처럼 범위가 좁은데 str타입으로 된 자료형은 category로 범주형 데이터로 변환하는 것이 훨씬 효율적이다.
        3. 연도와 같은 것은 숫자형으로 둬도 무방하나, 의미로 봤을 때 순서의 의미가 있으므로 숫자의 크기가 아닌 범주형으로 표현하는 것이 "적절하다".
    - 해결
        1. 문자들을 모두 np.NaN값으로 변환시키고, NaN값을 치환시키던지 아니면 NaN값을 포함한 행을 삭제한다.(만약 해당 열의 값이 매우 핵심이라면,열을 삭제할 수는 없자너)
        ```
        data[열이름].replace('?',np.nan,inplace=True)
        data.dropna(axis=0,subset=[열이름],inplace=True)
        data[열이름]=data[열이름].astype('float') # 정수면 'int'
        ```
        2. 
        ```
        .astype('category')
        ```
        3. 
        ```
        data['year']=data['year'].astype('category')
        ```
### 범주형 데이터 처리
- 설명 : 데이터 중 나이, 속도, 시간 등의 연속 데이터들은 일정한 구간(bin)으로 나눠서 분석하는 것이 효율적인 경우가 있다
    - Ex : 21 세의 데이터가 들어옴 - > 20대 카테고리, 18시32분 데이터가 들어옴 - > 저녁

- 사용 함수
    - obj= numpy.histogram() : python_numpy를 참고. 히스토그램 분포도를 만든다.
    - pd.cut()
    ```
    data=sns.load_dataset('titanic')
    data.dropna(axis=0,subset=['age'],inplace=True)
    count,nn=np.histogram(a=data['age'],bins=4,density=True)
    bbc=['하','중','상','최상']
    data['new']=pd.cut(x=data['age'],bins=nn,labels=bbc,include_lowest=True)
    print(data[['age','new']],'\n',data['new'])
    ``
### 머시러닝 알고리즘 적용을 위한 더미 변수
- 설명 : category, 범주형 이터는 머시러닝 알고리즘에 바로 사용할 수 없는 경우가 있어서 컴퓨터가 인식 가능한 입력값으로 변환해야 한다. 이 때 숫자 0과 1로 표현되는 더미 변수(dummy variable)를 사용한다. 0은 특성이 있고 1은 없음을 의미. 
- one hot incoding : 범주형 데이터를 컴퓨터가 인식할 수 있도록 0과 1로만 구성되는 one hot vector로 변환하는 것.
```
from numpy import NaN, nan
import numpy as np
import seaborn as sns
import pandas as pd
data=sns.load_dataset('titanic')
data['age'].fillna(value=data['age'].mean(),inplace=True,)
count,category_age=np.histogram(a=data['age'],bins=[0,10,20,30,40,50,60,70,80])
Labels=['유아','10대','20대','30대','40대','50대','60대','70대이상']
data['hist']=pd.cut(x=data['age'],bins=category_age,right=True,labels=Labels)
data_dummis=pd.get_dummies(data['hist'])
print(data_dummis['70대이상'])
```

### 정규화
- 설명 : 이미 알고 있는 대로.. 예전에 분산인가 공분산 계산할 때 비교할 두 대상의 크기를 맞춘 적이 있다. 0~1000의 데이터를 0~100으로 맞추고 이 데이터를 0~100인 데이터와 비교하는 것. 각 열(변수)에 속하는 데이터 값을 동일한 크기의 기준으로 나눈 비율로 나타내는 것을 정규화(normalization)이라고 한다. 보통 정규화를 거친 데이터의 범위는 0~1 또는 -1~1이다.
- 정규화의 방법
    1. 각 열의 데이터를 해당 열의 최대값으로 나누는 방법
    ```
    df['price']=df['price']/abs(df['price'].max())
    ```
    2. (해당 변수-최소값)/(해당 열의 최대값-해당 열의 최소값) : 0~1사이의 범위로 변환.

    