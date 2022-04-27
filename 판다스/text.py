import pandas as pd
import numpy as np
def bmi2(size):
    h=np.random.randint(150,200,size=size)
    w=np.random.randint(80,120,size=size)
    bmi=w/(h/100)**2
    bmiCopy=np.copy(bmi)
    bmi=bmi.astype(np.str0)
    print(bmi)
    for id,value in enumerate(bmiCopy):
        print(id,value)
        if value<18.5:  bmi[id]="thin"
        elif value<25: bmi[id]="normal"
        else : bmi[id]="fat"
    data=pd.DataFrame({"height":h,"weight":w,"bmi":bmi})
        
    return data

data=bmi2(20)
d=np.array([[1,256,52],[12,"s",3.23]])

print(d)