1. 
```
import pandas as pd

data=pd.read_excel('C:/Users/dlrms/OneDrive/Desktop/인공지능.xlsx',header=1)//
data.set_index(data.columns[0],inplace=True)
print(data.head())
```