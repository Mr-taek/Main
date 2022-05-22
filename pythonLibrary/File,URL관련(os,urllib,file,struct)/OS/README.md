# os(Oprating System): 운영체제에서 제공되는 여러 기능을 파이썬에서 수행할 수 있게 하는 module.

## os.
1. .mkdir(str) : str은 경로인데, 해당 경로 마지막 위치에 경로 마지막 이름과 같은 folder를 생성한다. file은 생성되지 않는다.


## os.path
1. .exists(str) : str은 path경로, 끝은 /folder 또는 /~.csv,.txt 등등이 가능

2. .join(*str) : 인자의 개수는 무관하며 str 객체이고 모든 객체가 "\"을 사이에 두고 하나로 묶인다.(이렇게하면 오류가 반드시 난다.) e.g : join("k","s") : "k\s". 이렇게 해야 한다. e.g : join("k/","s) : "k/s" , url 주소는 \이 아니라 /로 되어 있다.

3. .getsize(path) : path에 있는 파일의 bytes 크기 반환.