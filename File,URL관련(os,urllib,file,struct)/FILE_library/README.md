# file을 읽을 때, b'~'로 시작하는 것은 이 데이터가 binary라는 것임. 따라서 나중에 .decode() 함수로 문자로 바꿔줄 수가 있음.

# 1. general func


1. open()
    - parameter
        1. path + filename.type : 경로와 파일이름과 형식, file이 해당 path에 없으면 filename.type대로 파일을 하나 생성한다.
            - path="./~" 면 해당 파일의 경로에 바로 접근함을 의미한다.
        2. 파일 열기모드 : (r/w/a)(t/b). e.g : rb,ab. r(자동t지정)
            - r : 읽기모드 , 그냥 읽기용
            - w : write모드, 파일에 내용쓰기. 파일을 열 때 이미 존재하는 파일을 열게 되면 해당 원본 파일의 내용이 모두 사라진다(truncation). 방지를 위해선 반드시 "a"모드로 한다.
            - a : 추가모드, 파일의 마지막에 새로운 내용추가
            - t(default)/b : text/binary mode.
            - wb : 내용을 쓰면서 바이너리.
            
2. file.write() 

3. file.close() : 파일이 열렸으면 반드시 닫아야만 적용된다. 사실 이걸 쓰기가 귀찮아서 5번으 with를 사용한다.

4. file.read(bytes) : 파일의 내용 전체를 "문자열"로 돌려준다. 
    - bytes결과 예제. 딱 bytes만큼만 읽어낸다.
        - .read(4) - > b'
        1. .read(4) : 
5. with def(value) as _alias_ : 항상 open으로 열고 close로 닫아야 했다. 이걸 동시에 처리해 주는 것이 with이다. 사실상 open 전용이다. 이외에는 뭐 사용이 안 된다.
    - 사용법
        ```
        with open(patn,mode) as f:
            f.write(~)
        ```

-----------------------------

# 응용

1. ","을 delimator로 사용하는 csv로 저장하기.
    - ※주의 : with open문은 자동으로 close하기 때문에 모든 코드는 이 안에 넣어야 한다.
    ```
    with open("./text.csv",mode="w") as f:
        f.write("weight,height,label\r\n") # csv가 ","을 deli로 잡는 특성을 사용. \r은 Carriage return이다.
        for i in range(20):
            f.wirte("{},{},{}".format(i,i**2,bmi(i,i/2)))
    ```