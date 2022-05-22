## 1. strucnt 

## 2. Buffer란, BufferReader 객체

# Python으로 Binary 형식을 처리하기 위해 사용되는데

# open의 mode를 "b"로 하는 경우 사용될 수 있다.

# bit : 2진수 하나가 저장됨

# byte : 8개 비트가 모임. 알파/숫자 하나를 표현하는 최소 단위

# open 으로 BufferedReader/writer 일 경우 사용한다. 버퍼를 이용해서 읽고 쓰는 함수이다. 이 때 struct를 사용한다.
# 바이트 저장순서 (byte order)


## 1. strucnt 
- python에서 현재 사용중인 system의 endianness 확인은 "sys.byteorder"로 확인

설명 : 컴퓨터에서 데이터를 메모리에 저장할 때는 byte단위로 저장. 32/64비트(4바이트/8바이트)로 구성. 연속되는 바이트를 순서대로 저장해야 하는데 이 때 big endian/little endian 으로 방식이 나뉜다.

1. big endian : struct 에선 ">". 사람이 숫자를 쓰는 방법과 같이 큰 단위(숫자)가 바이트 앞에옴.

2. little endian : struct에선 "<". Intel format이라고도 하며, 윈도우 환경에서 사용하는 방식. 작은 단위(숫자)가 바이트 앞에 옴.

3. middle endian : 위에 두 경우에 속하지 않는 경우.

- unpack requires a buffer of 8 bytes

# struct 사용법

- format : 앞에는 항상 @<>=! 중 하나가 나온다. 모든 struct 메소드에 반드시 들어가는 인자가 format이다.
    - @,= : Byteorder가 host system에 의존한다. sys.byteorder로 확인해서 나오는 str로 결정한다. 단 @ 은 모든것을 system에 의존한다. 만약 format에 아무것도 지정되지 않으면 자동으로 @이 지정된다. 
    - 4h : hhhh를 의미한다.

1. .pack : 정보를 bytes 상태로 변환시킨상태에서 packing한다. 문자는 반드시 encoding을 거친 다음에 실행되어야 한다
    - Usage
    ```
    import struct 

    st="abcdqwe".encode("utf-8")
    print(st)
    k=struct.pack("@s",st)
    d=struct.unpack("@s",k)
    print(d)
    ```
2. .unpack() : bytes의 buffer 또는 packing된 정보를 꺼내온다.
    - parameter : 반드시 buffer의 사이즈(바이트크기)는 format에서 지정된 것과 동일해야한다.
        1. format : format 형식. e.g : "ii"(@에다총8바이트),"hhl"(@에다간2+2+4바이트)
        2. buffer : Buffer object. 


## 2. Buffer란, BufferReader 객체


- BufferReader : 읽는 순간 뒤에 남아 있는 값들이 계속 들어온다.