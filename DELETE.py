#1. 
import pandas as pd

data=pd.read_excel('C:/Users/dlrms/OneDrive/Desktop/population_in_Seoul.xls',)

k=data.drop([0])
# k.to_sql("kakaka",con='sqlalchemy.engine')
k.to_excel('C:/Users/dlrms/OneDrive/Desktop/kbs.xlsx')
print(k)