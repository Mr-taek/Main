# 미완, 문자열을 정수타입으로 바꿀때 valyeerror가 뜨는데 이것을 해결할 방법이 떠오르지 않음. - > 해결 아래가 해결책.
class say():
    operator={'plus':'+','minus':'-','mul':'*','div':'%'}
    def __init__(self):
        self.number=[]
    def cul(self):
        while True:
            self.number.append(input("please type the number"))
            
            for i in range(len(self.number)):
                    self.number[i]=int(self.number[i])
                    if self.number[i]==ValueError:
                        break;
            print(self.number)
            

abc=say()
c=abc.cul()
