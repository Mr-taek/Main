# All the 지식 for programing

# 환경변수, Path의 의미와 사용법
    - 의미 : cmd실행시, 어떤 경로에도 구애받지 않고 실행하고자 하는 파일 이름만 적으면 바로 실행할 수 있게끔 함.
        + 절대경로 , c:users\dlrms> c:\users\dlrsms\귀혼\file.exe , 이것을 절대경로라 하여 환경변수를 설정해주지 않을 시 해당 .exe파일을 실행시키기 위한 방법
        + 상대경로 , c:users\dlrms> \귀혼\file.exe , 이것이 상대경로.
    - 사용법
        1. 시스템속성, 환경변수 -> 사용자변수, 시스템 변수 중 path를 클릭, 해당 .exe 던 .txt 던 실행파일이 있는 경로를 지정
            - Ex) c:\Hello\file.txt 가 있음. 그러면 path엔 c:\Hello 로 새로만들기. 그러면 cmd창에선 file.txt 치면 실행
            + 시스템 변수의 path : 사용자 상관없이 변수 사용가능
            + 사용자 변수의 path : 오직 해당 경로를 넣은 사용자 계정만 변수 사용 가능
# What must have to do when the first git installed
    1. use " git bash "
    2. type "git config --global user.name " ? " , "git config --global user.email " ? "
    3. than every finished
# VS CODE usage branch
    1. F1 or CTRL+SHIFT+P
    2. git: create new branch 택
    3. 브랜치 이름정하기.
# Note , 만약 가상환경설치가 다 됐는데 import 후 해당 lib가 없다면 interpreter을 가상환경의 것으로 바꾸었는 지 체크한다. 이 오류는 pip의 버전이 맞지 않기 떄문이라고 한다. pip install --upgrade pip 해주면 될 것같은데 안 된다.

# VS CODE 가상환경 만드는 법과 접속법. 설치할 폴더위치에서 vscode를 run
- 가상환경 만드는 법 (Through vs code)
    1. CTRL + SHIFT + P 로 우선 python interpreter check, and 가상환경의 python interpreter가 없는 지 체크. 반드시 vscode로 다운받을거면 python inter~가 anaconda가 아닌 걸로 선택해야한다. 아나콘다로 다운받으면 아래 오류를 범하게 될 수도 있는데 해결은 삭제후 다시 이 스탭이다.
    2. cmd prompt 에서 " python -m venv Name 을 적어준다. 그러면 해당 폴더에 Name의 venv폴더가 등장한다.
    3. F1 or ctrl+shift+p 로 select python interpreter 설정을 보면 Name의 python interpreter가 등장한다.
    4. TERMINAL은 POWERSHELL이 아니라 CMD 커맨드를 통해 작동시킨다. 만약 POWERSHELL로 하면 오류 구문이 등장한다. 그게 아닌 일반환경으로 다시 변경해서 작동하면 정상.
    5. cmd에서 라이브러리를 다운받으면 가상환경에서만 적용된다.
- 가상환경 만드는 법(Through cmd)
    1. vscode 의 TERMINAL서 cmd 또는 window cmd 에 접속한다.
    2. Use " cd " command to move path. Type " cd \ " then will the path be set like " c:\> "
    3. Use " mkdir venvs/원하는 이름 " to make folder which wiil be used for Virtual env.
    4. Type cd venvs/원하는 이름 into cmd, it will access to venvs/원하는 이름 folder
    5. Type like " C:\venvs> python -m venv mysite/원하는이름 " it will generate make folder as given name.
- 가상환경 접속법
    1. vscode 의 TERMINAL을 cmd 로 둔다.
    2. c:\~ 로 현재 폴더의 위치가 나타날 것이다.
    3. "cd \"(따옴표 빼고)을 사용해서 경로를 c:\로 초기화 한다.
    4. " C:\>cd C:\Users\dlrms\OneDrive\Desktop\ " 와 비슷하게 경로를 타입한다. 이때 " cd " 키워드는 모든 경로 접속을 위해 사용된다.
    5. 예를 더 들자면 , 위 경로에서 더 다른 폴더로 가기위해 " cd Djanngo " or " cd Djanngo\ " 를 타입하면
    6. " C:\Users\dlrms\OneDrive\Desktop\Djanggo "처럼 더 접속하게 된다.
    7. 이 상태로 위에서 만들어둔 가상환경 폴더로 접근해서 Scripts 에 접속한다. 결과적으로
    8. C:\Users\dlrms\OneDrive\Desktop\Djanggo\Django\Scripts>activate
    9. (Django) C:\Users\dlrms\OneDrive\Desktop\Djanggo\Django\Scripts>
    10. 나가려면 deactivate 한다.
- 가상환경 나가는 법
    1. 가상환경이 켜진 상태에서 deactivate 를 친다.
    2. 그러면 마지막 Path가 Scripts인 상태에 앞에 (~)가 사라진다. 그 상태에서 다시 activate 하면 가상환경에 진입한다.
# Fatal error in launcher 시 cmd에 python -m pip~ 으로 하면 해결이다. 실제로 python -m pip --upgrade pip 하면 가상환경도 결국 원래 환경을 가져온 것임으로 가상안에서라도 적용이 된다.더불어 pip도 라이브러리이다.

# 가상환경에서 library가 sll/ts 것 때문에 설치되지 않는다 에러 : 이 글을 쓰는 시점에선 아나콘다와 vs의 스파이더/파이썬 을 동시에 사용해서 문제가 되었다. 가상환경 폴더에 pyvenv.cfg 을 찾으면 home이 있다. 그곳은 anaconda의 파이썬을 실행시키는 파일인데, 아나콘다를 열면 아마 실행이 될 것이다. 하지만 나는 그게 아님으로 이 주소를 일반 python.exe가 있는 폴더 경로를 써주면 된다. C:/user/anaconda3 에서 c~ \python\python310으로 옮겼더니 설치가 된다.

# 파일과 github 연동방법
    1. github에서 새로운 나의 repository를 만든다
    2. 해당 repository에 들어가서 code를 누르고 clone에서 해당 repository의 주소를 복사한다.
    3. 다시 VS CODE로 돌아와 CTRL+P -> git clone를 타입한다
    4. 이제 복사한 주소를 붙여놓고 깃허브에서 만든 파일을 데스크탑에 저장할 장소를 고른다.
    5. github에 생성된 repository의 이름이 적힌 파일이 만들어 지고 연동에 성공한다.
# How to bring Github repository into desktop
    1. Copy url of repository
    2. inter sthe Vscode and open the vscode search masician(ctrl+p)
    3. type ">git clone" and paste the url and choose directory
# tensorflow 와 numpy는 서로 상호작용이 가능하다.
파이썬 Tensorflow 공부를 위한 Repository 입니다. 아무튼 방학동안 이것만 ㅈㄴ 팔겁니다.

Rank : 몇 차원 array냐? ex) s=483 , 0 DIMENTION.. s=[1.1,2.2,3.3], 1 DIMEN- OR VECTOR . s=[[1,3,4],[4,6,7],[2,3,1]] 2 DIMENTION - OR ARRAY

DATE TPYE은 보통 tf.float32 or int32을 많이 사용.

tensorflow 에서 tensor는 차원을 뜻하는데. 0차는 스칼라 1차는 벡터 2차는 행열 3차는 큐브 4차부터는 D4임. 따라서 tensor는 데이터 타입과 형상(즉 1,3 인지 1,1,3 인지 등등)을 갖는다.

모든 함수의 ***shape*** Argument 는 차원이라서 shape=[2,2] 즉 2X2 행렬을 뜻하고 shape=[3,2,2]는 즉 벡터값이 두개 고 이 벡터를 묶어서 두개 있으며(행렬), 이 묶은 것이 3개 더 있다. 즉 총 6개의 괄호로 덮여진 Tensor다. 

# 수치미분 1차버전
: f'x=lim(delta x->0) (f(x+delta x)-f(x))/delta x = lim(dalta x-> 0) (f(x+delta x)-f(x-delta x))/(2*delta x)
**중요**: 분모가 2*delta x인 식을 자주 사용하게 될탠데, 그 이유는 이렇게 계산한 미분ㄱ밧이 상대적으로 오차가 작기 때문이다. 수치해석 프로그램은 수학적으로는 문제가 없는 수식이라도 다양한 방정식에 대해 오차가 가장 작은 동치식으로 변형해주는 것이 핵심이다.



# 집합을 이용한 합,차,교 집합 계산을 하고싶다면 python 'set'에 대해 알아보도록 하라.
