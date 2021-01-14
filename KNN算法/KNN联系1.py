# 导入模块
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd

# 读取数据
data=pd.read_excel(r'F:\python\KNN算法\电影分类数据.xlsx')

train=data.iloc[:,2:5]
test=np.array(data.columns[-3:],dtype=np.int)

# 计算相似度
train['相似度']=np.sqrt(((train - test) ** 2).sum(axis=1))

# 排序
train.sort_values(by="相似度",inplace=True,)

# print(train)
# 取k值
k=5

k_index=train.iloc[:5,:].index

label=data.loc[k_index,'电影类型'].mode()

print(label)
