a=[1,2,3,4,5,6,1,2,3]
b=[10,29,3,123,15412,1,3,4,2,1,2]
c=[10,29,3,123,15412,1,3,4,2,1,2]
d=[10,29,3,123,15412,1,3,4,2,1,2]

class machine():
    def __init__(self):
        self.mid=[]
        self.all=[]

    def sum(self,*list):
       
        for i in range(len(list)):
            if len(list[i])>=len(self.mid):
                self.mid=list[i]
        for i in range(len(list)):
            for k in range(len(list[i])):
                if list[i][k] not in self.all:
                    self.all.append(list[i][k])
        self.all.sort()
        print(self.all)
        return self.all
    
    def crossvalue(self,*list):     #교집합.
        for i in range(len(list)):
            self.mid.append(list[i])
            print(self.mid)
            print(list)
        for i in range(len(list)):
            for k in range(len(list[i])):
                for z in range(len(list)):
                    if list[i][k] in list[z]:       # 자기 자신의 리스트를 참고하지 않으려면 ..어떻게 해야하는가 ... 
                        if list[i][k]==list[z][k]:
                            continue
                        elif list[i][k] not in self.all:
                            self.all.append(list[i][k])
                            break 
                    else: continue
        self.all.sort()
        print(self.all)  
    
ad=machine()
ad.crossvalue(a,b)

