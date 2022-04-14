# file을 읽을 때, b'~'로 시작하는 것은 이 데이터가 binary라는 것임. 따라서 나중에 .decode() 함수로 문자로 바꿔줄 수가 있음.

1. open()
    - parameter
        1. path + filename.type : 경로와 파일이름과 형식
        2. 파일 열기모드
            - r : 읽기모드 , 그냥 읽기용
            - w : write모드, 파일에 내용쓰기. 파일을 열 때 이미 존재하는 파일을 열게 되면 해당 원본 파일의 내용이 모두 사라진다. 방지를 위해선 반드시 "a"모드로 한다.
            - a : 추가모드, 파일의 마지막에 새로운 내용추가
            - b : binary mode
            - wb : 내용을 쓰면서 바이너리.

2. file.write() 

3. file.close() : 파일이 열렸으면 반드시 닫아야만 적용된다. 사실 이걸 쓰기가 귀찮아서 5번으 with를 사용한다.

4. file.read() : 파일의 내용 전체를 문자열로 돌려준다.

5. with def(value) as _alias_ : 항상 open으로 열고 close로 닫아야 했다. 이걸 동시에 처리해 주는 것이 with이다. 사실상 open 전용이다. 이외에는 뭐 사용이 안 된다.
    - 사용법
        ```
        with open(patn,mode) as f:
            f.write(~)
        ```
-----------------------------

1. 