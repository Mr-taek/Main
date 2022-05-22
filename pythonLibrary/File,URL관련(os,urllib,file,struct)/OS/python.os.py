#os
#import os

#a=os.listdir()#---- 지정한 디렉토리 안에 모든 파일과 디렉토리의 리스트를 리턴한다.
#디렉토리를 지정하지 않으면 현재의 working directory를 사용.

# for i in a:
#    print(i)
#---- diretory를 지정하지 않아서 현재 사용되는 파일(GIT_EXCER)이 실행된다.

#path="c:/"
#a=os.listdir(path)

#for i in a:
#    print(i)
#--- 디렉토리가 C 메모리이므로 c메모리에 있는 모든 파일의 이름을불러온다.
#------------------------------------------------------------
#(find,startswith,endswith),찾기,시작문자찾기,끝문자찾기
#find(찾을문자,찾기시작할위치(문자열 또는 숫자의 인덱스))
#startswith(시작하는문자, 시작지점(인덱스))
#endswith(끝나는문자, 문자열의 시작,문자열의 끝)
#a=["lave.py","lalala.py","higiggi.c","number.py"]

#for file in a:
#    if file.endswith(".py"):
#        print(file)
#    if file.endswith("py",1):
#        print(file,"ssss")
#    else: print("거짓말")
#-------------------------------------------------
