### 판다스로 로드한 데이터는 모두 자동으로 DataFrame으로 변환된다.
### 파일 저장
1. pd.read_excel
2. pd.read_csv(Argument)
    - (오류)'utf-8' codec can't decode byte 0xb3 in position 0: invalid start byte
        - 설명 : 불러오는 파일의 encoding 설정이 python encoding 설정이 서로 맞지 않으면 발생한다. 한글은 보통 'utf-8' 체계를 사용함. 이 경우에는 encoding='cp949'로 인코딩 인자를 설정하면 된다. 참고로 cp949는 파이썬 인코딩방식.
    - 인자
        1. sep='~' : 파일 내 원소를 구분해주는 문자선언.
        2. index_col=number/'문자' : 행 인덱스로 선언할 열을 선택. 열의 순서 번호를 넣어도 되고 열 인덱스 이름을 써줘도 됨.
        3. names=['str','str2',....],header=None : 열 인덱스 이름이 없을 때 names로 지정해준다. 이때 header는 없음으로 해준다.
        4. skiprows=[num1,num2,...] : 불러올 때 스킵할 행을 결정.
        5. nrows=num : 파일의 위에서부터 num개만큼의 행만 불러옴.
        6. na_values['??','?','N/A','nan',...] : 파일 내에 결측값으로 표현된 값을 선언. '~' 같은 문자가 결측값으로 누군가 표시했으나 실제 코드에선 str,object로 표현되기 때문에 사전에 결측값으로 표현된 문자를 알아내서 na_values로 선언을 해줘야 후에 오류가 안 남. Series의 전체가 int라도 하나가 str이면 Series는 object타입으로 변환됨.
        7. dtype={'columIndexName1':dtype,'columName2':dtype,....} : DB사용자는 데이터 유형을 명시적을 설정해주는 것에 익숙하다. 사용하려는 데이터의 열 데이터 타입이 사용자의 의도와 다르다면 이걸로 변경이 가능하다. 
3. pd.read_json


### 파일 쓰기
- 설명 : 데이터프레임은 2차원 배열로 구조화된 데이터라서 csv파일로 변환이 가능하다.
1. dataframe obj.to_excel('저장위치')
2. dataframe obj.to_csv('저장위치')

2. pd.to_json

# DataFrame , Series 를 python의 class로 변환
1. Series -> list
    1. Series.tolist() : 시리즈 객체를 list 로 변환
        - ex
        ```
        data['age'].tolist()
        ```
        ->
        ```
        <class 'numpy.float64'>
        [22.0, 38.0, 26.0, 35.0, 35.0, nan, 54.0, 2.0, 27.0, 14.0, 4.0, 58.0, 20.0, 39.0, 14.0, 55.0, 2.0, nan, 31.0, nan, 35.0, 34.0, 15.0, 28.0, 8.0, 38.0, nan, 19.0, nan, nan, 40.0, nan, nan, 66.0,.......
        .....]
        ```
2. DataFrame -> list : 근데 굳이 Frame 전체를 list로 바꿔야 하나 싶음 대충 예상해보자면..
    - 예상 모양
    ```
    [
        [글,숫자,카테고리1,str,...], # list객체를 DataFrame으로 바꿀때와 반대로 되지 않을까 예상해봄.
        [글2,숫자2,카테고리2,str2,...]
    ]
    ```