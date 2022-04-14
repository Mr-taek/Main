# 판다스로 읽어온 모든 파일 포맷은 DataFrame으로 변형된다. 데이터 가져오기의 핵심은 모두 같은 형식의 format으로 만드는 것이다.
# pandas의 인덱스 는 두 가지다. 1. 정수형 위치 인덱스 2. 
# 슬라이싱을 통한 정수형 인덱스는 끝-1만큼 이고 인덱스 라벨의 슬라이싱은 끝을 포함한다.
### python 몇가지 유용한 함수
1. type() : 인자의 타입을 리턴한다.

### Series, DataFrame 기본
1. Series : Series객체는 dictionary 객체와 매우 흡사. key와 대응 되는 value가 있음.
    - 특징
        1. dict의 형태와 매우 비슷해서 보통 dict형태 객체를 Series객체로 변환시킨다.
            - pandas.Seriese(dict obj)
        2. 행의 인덱스는 열의 인덱스 처럼 보이지만 사실 모드 행 인덱스이다.
            - 모형
            ```
            key     0   1   2   3   4   5   ...
            value   5   2   32  2   41  1   ...
            ```
            -> (주의!) 따라서 Series객체의 평균값을 알고 싶다면 열이 아니라 행 축을 중심으로 실행해야 옳다.
            -> .mean(axis=1) [x] , .mean(axis=0) [o]
        3. value자리에 한 가지 값만 오는 것이 아니라 리스트 객체도 올 수 있다.
        ```
        List=[
            [1,2,3,4,5,2],[3,4,5,6,2,1]
        ]
        data=pd.Series(List)
        ```
        ->
        ````
        0    [1, 2, 3, 4, 5, 2]
        1    [3, 4, 5, 6, 2, 1]
        dtype: object
        ```
    - 사용법
        - obj= pd.Series(obj1) # 객체1을 시리즈 객체로 변환시키기.
        - Series[PositionNum Or 'key'] 
        - Series[PositionNum1:PositionNum2]
            - 인자
                1. name=~ : 원소들을 대표하는 행 인덱스 이름을 지정.(datafram으로 섞이면 열 인덱스가 됨.)
                2. index=[~]ir ~ : 각 원소를 지칭할 열 인덱스를 지정
        - Series['c'] or [['d':'c']]==['d':'c'] or [0] or [[0:5]] : 단일 원소와 여러개의 원소를 추출하는 방법
        - List -> Series
            - 설명 : 리스트를 시리즈로 변환할 때는 딕셔너리처의 키처럼 인덱스로 변활될 값이 없으므로 인덱스르 별도지정하지 않는 한 디폴트인 정수형 위치 인덱스가 자동 지정된다.
        - 
    - 함수
        1. .index : 시리즈 객체의 인덱스를 모두 리턴
        2. .values : 인덱스와 대응 되는 원소를 모두 리턴

2. DataFrame : 여러 Series 객체를 붙여 놓은 것으로 생각해도 되는 데이터 타입
    - 설명 : 판다스의 데이터프레임 자료구조는 R의 데이터프레임에서 유래했다고 알려 짐.
    - 용어
        1. 데이터프레임 : 시리즈 객체가 열을 이룬 것. 시리즈를 열벡터라고도 함. 2차원 벡터 또는 행렬임.
        2. 행 : 다양한 속성(열의 원소)데이터들이 모인 "레코드"
        3. 열 : 공통의 속성(특징)을 갖는 일련(sequence)의 데이터.
    - 사용법 : pandas.DataFrame(Arg)
        - DataFrame 만들기
            1. dict-> dataframe : 키는 열의 인덱스가 되고 value들은 열벡터를 이룬다. 행 인덱스는 지정하지 않으면 디폴트이다.
            ```
            Dict={
                'c1':[~],'c2':[~],'c3':~,'c4':~
            }
            data=pd.DataFrame(Dict)
            ```
            2. List -> Dataframe : 리스트는 key가 없으므로 열벡터를 이루지 않고 그대로 행에 대입된다. 행,열의 인덱스는 디폴트가 된다. 
        - dataframe.index=[], dataframe.columns=[] : 프레임에 행과 열 인덱스를 할당시켜준다.

        - df.rename(index={기존인덱스:새인덱스, 기존인덱스2:새인덱스, ...},columns={이하 동치},inplace=True/False)

        - 열 호출법 : DataFrame[num or 'key'] , Series를 붙여놓은 것으로 생각해도 될 정도로, 열은 Series와 호출방식이 그냥 같음.
        - 행 호출법 : 슬라이싱 기법 또한 허용
            1. Df.loc['행str','열str']
            2. Df.loc['행의str':'str2','열str]
            3. Df.iloc[num,num]
    - 인자
        1. index=[] : 행의 인덱스를 할당, 행의 개수가 굉장히 많을 경우엔 무의미 할 수 있다.
        2. columns=[] : 이하동치.
3. 열추가, 행추가
    - 사용법
        1. 열추가 : Seriese/DataFrame['새로추가할열이름']=리스트,Seriese의 경우는 값 하나.

4. 열 인덱스 호출로 인한 DataType 차이
    - type(df['age']) -> Series
    - type(df[['age']]) - > DataFrame

1. pd.loc pd[]
### pandas 함수
1. pandas.cut() : Category, Seriese, or ndarray 타입을 리턴
    - 인자 정보
        1. x = Array-like : input데이터로서 경계를 구분할 값들, 반드시 1차원 데이터(flattend, 1-dimentional data)이어야 함.
        2. bins = int /sequence of scalars/intervallndex : int일 경우, input 데이터의 최대 값에서 int 값을 나눠 width가 같은 경계를 int개 만큼 생성. 스칼라 일련데이터(리스트,etc)가 들어오면 그 데이터 안에 담긴 값대로 경계를 구분 짓는다([1,2,3]이면 1,2,3으로만 구분을 나눔).inter~은 모르겟음.
        3. labels= Array or False(default) : 경계값들에 별명을 붙이는 것. 반드시 bins의 데이터 크기와 같은 크기의 Array가 들어와야하고, False면 그냥 bins 인자에 사용된 숫자들을 사용한다.
        4. retbins = bool : 두개를 리턴하는 .cut()함수, 그중 bins(경계)에 대한 값을 리턴할 지 안 할지 결정
        5. right = bool : True(default)일 경우 경계값에서 (1,2], (2,4] .. 식으로 포함범위를 지정한다. False면 (~) 로 포함시키지 않는다.
        6. include_lowest =bool : 첫 경계값에서 소수점 이하를 포함할 지 안 할지를 결정 하는 듯한 인자 인듯?
    - Return
         1. out : Category, Seriese, or ndarray 타입을 리턴. value의 labels에 따라 리턴타입이 결정됨.
         2. bins : ndarray,intervallindex타입 리턴.retbins 인자가True일 때만 반환된다.
     ```
    data=sns.load_dataset('titanic')
    data.dropna(axis=0,subset=['age'],inplace=True)
    count,nn=np.histogram(a=data['age'],bins=4,density=True)
    bbc=['하','중','상','최상']
    data['new']=pd.cut(x=data['age'],bins=nn,labels=bbc,include_lowest=True)
    print(data[['age','new']],'\n',data['new'])     
     ```
    - ex) 1 : label 없는 경우
    ```
          age              new
    0    22.0  (20.315, 40.21]
    1    38.0  (20.315, 40.21]
    2    26.0  (20.315, 40.21]
    ..    ...              ...
    890  32.0  (20.315, 40.21]
    
    [714 rows x 2 columns] 
    0      (20.315, 40.21]
    1      (20.315, 40.21]
    4      (20.315, 40.21]
                ...
    890    (20.315, 40.21]
    Name: new, Length: 714, dtype: category
    ```
    - ex 2 : label 있는 경우
    ```
          age new
    0    22.0   중
    1    38.0   중
    2    26.0   중
    ..    ...  ..
    890  32.0   중
    [714 rows x 2 columns] 
    0      중
    1      중
    2      중
        ..
    890    중
    Name: new, Length: 714, dtype: category
    ```
    - 직접 한 예제
    ```
    data=sns.load_dataset('titanic')

    data['age'].fillna(value=data['age'].mean(),inplace=True,)
    count,category_age=np.histogram(a=data['age'],bins=[0,10,20,30,40,50,60,70,80])
    Labels=['유아','10대','20대','30대','40대','50대','60대','70대이상'] # cut함수에서 bin 라벨은 반드시 bin edges보다 하나 적어야 한대서 80대 뺌

    data['hist']=pd.cut(x=data['age'],bins=category_age,right=True,labels=Labels)

    print(data.info())
    ```
2. pandas.get_dummies() : Array-list,Series, DataFrame타입을 받아서 데이터 내 모든 value를 분리시키고 해당 값이 존재하는 지의 여부를 0과 1로 구분하는 DataFrame을 반환한다.
    - 특징 : 보통 get_dummies를 한 열은 삭제 된다. 이미 다 분리를 해놨기 때문. category 형을 분리할 때 자주 사용한다. 원소의 종류가 제한적이기 때문이고 연속적이지 않기 때문이다. 만약 정수처럼 15,23,123,.. 등의 데이터에 사용하면 엄청 많은 열이 만들어 질 것이다.
    - 인자
        1. data = Array-like/Series/DataFrame
        2. prefix = str/list of str/dict of strNone(default) : 새로 만들어진 열에 접두사를 붙이는 건데 어떤 열에서 분할 되었는 지 명시할 때 사용.
        3. dummy_na = bool : NaN값을 포함할 지 안할지.False(default)
        4. columns = list-like/None(default)
        5. .. 추후에 봅시다.
3. pandas.set_option() : 출력할 최대 열의 개수
    - API :https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.set_option.html?highlight=set_option#pandas.set_option
    - 인자
        1. (pat='display.max_columns',val=10) # 출력할 최대 10개 열의 개수
           ('display.max_colwidth',20) # 출력할 열의 너비
           ('display.unicode.east_asian_width',True) #유니코드 사용 너비 조정

    
### DataFrame, Series 공통함수
0. .loc , .iloc : 사용법은 대충 알고 있으니, 핵심만 설명함.
    1. .loc[0:4,'aa':'bb] : 분명 숫자는 안 된다고 알고 있지만, 인덱스가 int형이라면 상관없음. 더불어 슬라이싱이라도 마지막 범위의 값이 포함됨.
1. (Seriese 전용) Seriese obj.fillna(arg) : nan값을 특정 값으로 채워주는 함수
    - 인자 정보
        1. method : 데이터 특성상 특정 value 앞 또는 뒤등 인접 정보와 유사할 가능성이 높음(온도, 엔트로피변화 등 시간에 대한 변화 정보).
            - method='ffill' : frontfill,nan이 있는 행의 직전 행에 있는 값으로 채워준다
            - method='bfill' : backfill,nan이 있는 다음 행의 값으로 채운다.
2. .replace() : 
    - 인자정보
        1. to_replace : 데이터 프레임 안에서 변경할 문자, 숫자의 정보
        2. value : 변경될 데이터
        3. inplace : 이미 알 것이니 생략
        4. method='ffill' or 'bfill' : .fillna 와 같은 방식.
        5. (자료형 변경).replace({1:'kbs',2:'bbc', ...}) , .replace({'abc':5,'bbc':3, ..}) : 특정 Series 열에 대한 값을 변경시켜준다. 또한 자료형도 자동으로 변경된다. 
    - ex
        1. 
        ```
        data['age'].replace(to_replace=np.nan,value=5,inplace=True)
        print(list(data['age']))
        ```
        -> 모든 nan값이 5로 대체 됨.
3. .duplicated(arg): 행의 레코드 값이 이전, 또는 다음 행의 레코드와 같은 지 다른지 중복검사 해주는 메소드
    - 반환 값 : Series 타입, key: bool 을 반환한다. 인자의 조건에 맞는 중복들은 True을 아니면 False를 반환한다.
    - 인자
        1. keep='last','first'(default),False : last가 나오면 현재 행에서 뒤에 행과 비교한다. first는 현재 행에서 앞에 행과 비교한다. False는 모든 레코드의 값이 같은 것을 비교한다.
        2. subset='열이름'or['열이름1','열이름2',..] : 특정 열에 대해서만 중복 체크를 한다.
4. .drop_duplicates(arg): 중복에 해당되는 모든 행을 제거한다.
    - 반환 : DataFrame
    - 인자 : 3번, .duplicated와 동일

5. .round() : 반올림
    - 인자
        1. decimals=0(default) : 반올림할 자릿수를 선택
6. .astype() : value의 타입을 변환시키기.
    - 인자
        1. dtype='int'/'float'/'categori'....etc : 변환시킬 타입을 적는다
        2. (데이터프레임 전용)dtype={col name:dtype,col name2:dtype..} : 해당 열에 대한 데이터 타입을 변경. 딕셔너리로 사용을 주의.
        3. Df=Df.astype() : 데이터셋의 모든 값을 특정 변수타입으로 변환.
    - 사용법
        ```
        1~2. DF['ORIGIN']=DF['ORIGIN'].astype(dtype=int)
        3. DF=DF.astype(object/str) # 
        ```
7. .sample() : 무작위 행 또는 열의 정보를 가져오기
    - 인자
        1. replace=True/False : 한번 가져온 행을 다시 가져오는 것.
        2. n=number : 샘플로 가져올 개수
        3. axis = 0,1 : 설명 생략
        4. frac : 암튼 n 인자와 같이 사용하면 안 된다고 함.
8. .dropna() : 인자에 해당되는 행 또는 열을 아예 삭제해버린다.
    - 인자
        1. axis=0(default)or1 :  nan값이 있는 열, 행을 제거한다.
        2. subset =['열이름/행이름'] or ['열이름1/행1', '열이름2/행2', ..] : 만약 axis=0이면 열이름을 넣는다. nan이 있는 열 중 subset안에 있는 열만 체크해서 그 행을 제거해 버린다.
        3. inplace=~
        4. thresh=number : nan의 개수가 number이상인 행/열 을 선택하게 한다.
        5. how='any'all' : any면 nan값이 있기만 하면 이란 뜻, all이면 해당 행/열에 모든 값이 nan이면.
9. DF['COLUMNS'].dtypes : 해당 열에 대한 데이터 타입을 리턴한다.

10. .max() , .min() : 

11. (Series전용) .unique() : 시리즈의 나오는 모든 원소를 중복값 없이 리스트로 묶어서 리턴해
    - 특징 : Uniques are returned "in order of appearance"(등장하는 순서). Hash table-based unique, therefore does NOT sort.
    - 반환 : ndarray, numpy array

12. .idxmax()
    - Dataframe : 각 열에 대해 가장 큰 값을 갖는 행 인덱스를 택해서 모아 Series로 리턴한다.
    - Series : 원소 중 가장 큰 값을 갖는 인덱스를 택해서 그 값만 리턴한다.

13. .drop()
    - 인자
        1. axis=0(default)/1 : 행또는 열중 삭제할 것
        2. labels=Single/list-like RowIndexORcolumn index : 제거할 행 또는 열 설정
### Series, DataFrame의 행 열, 정보 얻기
1. pd.head() ,(DataFrame 전용) pd.info() , pd. ... 아 시발ㅈ 같은 onedrive

2. obj[~].describe() / obj.loc[~].describe()
    - 리턴 값 : Series을 반환하며(input이 Series라서), Series 안에 mean std min 데이터 값들이 존재.
        - .describe()['mean'] - > 평균값이 등장. describe는 Seriese 객체이기때문.
        - 오직 숫자형 타입에만 적용되며, 문자형 타입은 리턴값에서 빠진다.

3. .fillna=number : NaN값을 number값으로 대체.
    + DataFrame[열이름].fillna(채울 값(문자열,정수),inplace=~)
    + DataFrame.loc[행이름].fillna=번호
4. sort_values(by='',ascending=True/False): 내가 봤을 때는 Seriese에서 value값을 정렬하는 것 같다. DataFrame에서는 잘 안 됨.

### 행, 열의 값 정보 얻기 
1. DataFrame.value_counts(Argument): 행또는 열에 있는 value의 개수를 셈. (아직 가능한 지는 모르겠음..Series객체만 가능했음,.)
    + DataFrame['열이름'].value_counts() : 가장 정확하게 가능한 형태. 
    - 인자
        1. normalize
            - True : 해당 행 또는 열의 1이라는 숫자의 개수, 또는 True/False가 있는 개수
            ```
            False    714
            True     177
            Name: age, dtype: int64
            ```
            - False : 해당 행 또는 열이 1이라는 숫자가 나오는 백분율. 또는 True/False가 나오는 백분율
             ```
            False    0.801347
            True     0.198653
            Name: age, dtype: float64
            ```
    - 리턴 형태
        1. Series 타입 객체를 반환한다.
    - 사용 예시(중요!)
    ```
    from numpy import NaN
    import seaborn as sns
    import pandas as pd
    data=sns.load_dataset('titanic')
    missing=data.isnull()
    print(missing.head())
    colum_data=missing.columns
    for col in colum_data:
    count=missing[col].value_counts(dropna=False,normalize=True)//normalize를 통해 백분율로, 전체 행 데이터중에 해당 데이터가 차지하는 백분율로 나타냄
    #print(col,": ", ) #print 하기전에 생각해보니 value_counts()로 리턴되는 타입이 Series인지 Dataframe인지 알아야함.
    # Series면 열이 하나이므로 열의 인덱스가 무의미하니 당연히 행 인덱스로 지정해서 print해야하고, 만약 dataFrame이면 행과 열 둘중 하나를 일단 선택해야했음.
    #print(count) # Series가 반환됨을 확인
    # 단순히 print(col,':',count[True])하면 오류가 남. 왜냐하면 True라는 key가 존재하지 않는 Series가 있기 때문임 따라서 예외처리문을 써줌
    try :
        print(col,': ',count[True])
    except:
        print(None)
    ```
2. .dtypes : 각 행에 대한 data value의 객체 타입을 출력한다.
### index 
1. DataFrames.columns : 속성값이며, 열 인덱스 값을 가져와 인덱스 타입을 반환. value 값은 int,str,float 로 다양할 수 있음.
2. DataFrames.index : 속성값이며 , 행 인덱스 값을 겨자와 인덱스 타입을 반환.

### add,sub,div,sum,mean ..

1. DataFrame/Series.sum(Argument) : 값이 있거나, 1(True)인 값을 출력한다.

2. Series.mean(axis=0(default,1은 존재가 불가능)) 

3. (Series 전용) obj.sum : 시리즈 객체 안에 원소를 모두 더하고 int OR float 타입을 리턴한다.

### 필터링(매우매우매우 중요!!!!!)

- 설명 : 원하는 조건식이 있을때 꾿이 if문을 쓰지 않고 함수를 이용해서 찾기. (유용하긴함 NaN값 바로 찾음 ㅋ)

- 과정
    1. 역시 if문 처럼 조건식을 사용한다. & | ! < > = .. 등을 사용해서 원하는 조건을 코딩한다.
    2. 짜여진 조건식을 .loc[]에 대입한다(공부전필수 참고)
    ```
    data=sns.load_dataset('titanic')
    mask=(data.age>=10)&(data.age<20)
    ```
    - 코드 해석 : mask 객체를 잘 이해해야한다. data.age가 나오는 순간 age에 잇는 모든 원소들이 등장하고 10과 비교를 하게 된다. 여기서 True인 원소들이 남고 다시 오른쪽 20과 비교되어 남겨진 원소들과 & 연산을 하게 되어 최종적으로 data.age에서 특정 행을 갖고 age열 인덱스를 갖는 살아남은 데이터가 존재한다.
    - 증명
    ```
    dd=data.loc[data['age'][0],:] # mask 객체에서 연산의 결과는 분명 mask = data['age'][?] , data['age'][?], ...일 것이다.
    print(dd)
    ```
    -> 그러자 Series가 등장했다. 이론적으로 이게 맞는 듯 하다.
    ```
    survived                1
    pclass                  3
    sex                female
    age                  15.0
    sibsp                   0
    parch                   0
    fare               8.0292
    embarked                Q
    class               Third
    who                 child
    adult_male          False
    deck                  NaN
    embark_town    Queenstown
    alive                 yes
    alone                True
    Name: 22, dtype: object
    ```
    3. 마무리
    ```
    p=data.loc[mask,:]
    print(p.head())
    ```

    + 추가 예제!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!(중요해!!)
    ```
    data=sns.load_dataset('titanic')
    mask1=(data['fare']>50)|(data['age']>40)#핵심, 마스크가 두개임
    mask=(data.deck=='C')&(data.age<20)# 핵심, 마스크가 두개임
    dd=data.loc[mask1|mask,'sex':'fare'] # 그 마스크를 다시 논리연산시켯음.
    print(dd.info())    
    ```
    ->
    ```
    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 265 entries, 1 to 879   # 총 265 명이 나옴.
    #   Column  Non-Null Count  Dtype
    ---  ------  --------------  -----
    0   sex     265 non-null    object
    1   age     243 non-null    float64 # 널값이 여전히 있음.
    2   sibsp   265 non-null    int64
    3   parch   265 non-null    int64
    4   fare    265 non-null    float64
    dtypes: float64(2), int64(2), object(1)
    memory usage: 12.4+ KB
    None    
    ```
    4. DataFrame column obj.isin(값의 리스트) 메소드 : 괄호 한에는 조건식이 불가능해서 확실한 값들만 쓸 수 있을 듯 하다. 예를들어 sex열에 'male'을 작성하면 실제로 male 인 경우만 등장한다.
        - 예제
            1. 
            ```
            data=sns.load_dataset('titanic')
            df=data['age'].isin([20,30,21])
            Nd=data[df]
            print(Nd)
            ```