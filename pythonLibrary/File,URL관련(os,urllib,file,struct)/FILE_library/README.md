# file을 읽을 때, b'~'로 시작하는 것은 이 데이터가 binary라는 것임. 따라서 나중에 .decode() 함수로 문자로 바꿔줄 수가 있음.


# 1. general func


1. open() : mode에 따라 파일을 읽는데, 파일은 binary로 되어 있어서 자동으로 text로 읽는 것이 기본값임. 
    - parameter
        1. path + filename.type : 경로와 파일이름과 형식, file이 해당 path에 없으면 filename.type대로 파일을 하나 생성한다.
            - path="./~" 면 해당 파일의 경로에 바로 접근함을 의미한다.
        2. 파일 열기모드 : (r/w/a)(t/b). e.g : rb,ab. r(자동t지정)
            - r : 읽기모드 , 그냥 읽기용
            - w : write모드, 파일에 내용쓰기. 파일을 열 때 이미 존재하는 파일을 열게 되면 해당 원본 파일의 내용이 모두 사라진다(truncation). 방지를 위해선 반드시 "a"모드로 한다.
            - a : 추가모드, 파일의 마지막에 새로운 내용추가
            - t(default)/b : text/binary mode.
            - wb : 내용을 쓰면서 바이너리.
        3. encoding : 
            0. cp949 : default encoding way. codec page 949.
            1. utf-8 : 보편적인 문자인코딩 방식. "cp949" 코덱 에러가 뜨면 이 형식을 바꿧 ㅣㅇㄺ는다.
2. file.write()
    - parameter
        1. value : file에 쓸 내용적기. e.g : hi,hs,kb -> .csv의도 작성 / kbs jb \r\nkk as -> .txt.의도 작성

3. file.close() : 파일이 열렸으면 반드시 닫아야만 적용된다. 사실 이걸 쓰기가 귀찮아서 5번으 with를 사용한다.

4. file.read(bytes) : 파일의 내용 전체를 "문자열"로 돌려준다. 
    - parameter
        1. bytes : -1(default): read while file. 파일은 결국 memory에 byte 형식으로 저장되기 때문에 영문은 1bytes, 한글은 4bytes씩 읽는 것을 유의해야한다.
    - bytes결과 예제. 딱 bytes만큼만 읽어낸다.
        - .read(4) - > b'
        1. .read(4) : 

<<<<<<< HEAD:pythonLibrary/File,URL관련(os,urllib,file,struct)/FILE_library/README.md
    - example
    1. 한글 파일 읽기 : utf-8의 정체가 궁굼해지는군..
    ```
    사랑은 은하수다방에서 둘이 만나 ->love.txt
    k=open("./love.txt,"r",encoding="utf-8")
    print(k.read(14)) -> 사랑은 은하수다방에서 둘이 -> 한글은 4bytes라고 했는데 여기선 한글이 한 문자당 1바이트로 읽힌다.. 이유는 알 수가 읎다.
    ```
    2. 영문 파일 읽기
    ```
    import urllib.request as req
    import gzip, os, os.path
    savepath = "./mnist"
    baseurl =..... -> de.txt
    k=open("./de.txt,"r",encoding="utf-8")
    print(k.read(17)) -> import urllib.req. 여기는 당연히 한 글자당 1bytes로 내가 알고있는 대로 나온다.
    ```
5. file.split() : sep를 기준으로 문장을 잘라서 결과를 list로 반환
    - parameter
        1. sep : "\t" "\n" "\s" .. 
    - Ex
        1. .read().split("\n")
        ```
        .read() ->
        1.2,3.2,4.5
        5.2,1.2,4.5
        ...
        .read().split(\n) ->
        ["1.2,3.2,4.5","5.2,1.2,4.5"]
        ```
5. with def(value) as _alias_ : 항상 open으로 열고 close로 닫아야 했다. 이걸 동시에 처리해 주는 것이 with이다. 사실상 open 전용이다. 이외에는 뭐 사용이 안 된다.
=======
4. file.readline(bytes),readlines() : 파일의 내용을 읽음.
    1. file.readline() : bytes만큼 읽음.
    2. readlines() : bytes는 노상관. \n까지도 읽어옴. 원리는 아직 잘..
        ```
        
        ```
6. with def(value) as _alias_ : 항상 open으로 열고 close로 닫아야 했다. 이걸 동시에 처리해 주는 것이 with이다. 사실상 open 전용이다. 이외에는 뭐 사용이 안 된다.
>>>>>>> c183d0233670ed4646f018cdf5a36e56732da5b4:File,URL관련(os,urllib,file,struct)/FILE_library/README.md
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
2. n bytes씩 끊어서 읽기
    ```
    with open("~.txt","r") as f:
        while True:
            k=f.read(3)
            if not k: # 숫자가 다 있으니 True이니 실행은 안 되고 0이 되는 순간 작동
                break
    ```
