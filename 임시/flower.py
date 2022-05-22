from sklearn.preprocessing import scale
from sklearn.datasets import load_iris
# load_iris() 는 .data .target 으로 분류시킨다.
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
iris=load_iris()
k=iris.data # 이미 데이터가 numpy array임. 더 이상 

df=pd.DataFrame(k,columns=["sepal_length","sepal_width","petal_length","petal_width"])

kmeans=KMeans(3,init="k-means++",max_iter=300,random_state=0)
# kmeans.fit(df)
cluster_labe=kmeans.fit_predict(df)
# print(np.unique(cluster_labe)) 오,... unique는 한 개의 리스트 안에 중복값이 없도록 해줌.
# DF["target"]=iris.target
df["cluster"]=kmeans.labels_

# rst=DF.groupby(["target","cluster"])["sepal_length"].count()

# print(rst)


pca=PCA(2)
pca_trans=pca.fit_transform(iris.data)# numpy array
pca_x1=pca_trans[:,0]
pca_x2=pca_trans[:,1]

marker0=df[df["cluster"]==0].index
marker1=df[df["cluster"]==1].index
marker2=df[df["cluster"]==2].index

import matplotlib.pyplot as plt

# plt.scatter(df.loc[marker0,pca_x1],df.loc[marker0,pca_x2],marker="o") 
# plt.scatter(pca_x1[marker0],pca_x2[marker0])
# plt.show()

# ------------------------

