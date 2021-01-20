from sklearn.datasets import load_iris,fetch_20newsgroups
import seaborn as sns
import  matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
# 1.1数据集获取
iris=load_iris()
# print(iris)

# 1.2大数据集获取
# nwes=fetch_20newsgroups()
# print(nwes)

# 特征值
data=iris['data']
# print(data)

# 目标值
target=iris.target
# print(target)

# 鸢尾花特征的名字
feature_names=iris.feature_names
# print(feature_names)

# 鸢尾花目标值的名字
target=iris.target_names
# print(target)

# 鸢尾花描述
desc=iris.DESCR
# print(desc)


# 数据可视化
# 创建DataFrame
# iris_d=pd.DataFrame(iris.data,columns=['Sepal length','Sepal width','petal length','petal width'])
# # 确定目标值
# iris_d['Species']=iris.target
#
# def plot_iris(iris,col1,col2):
#     sns.lmplot(x=col1,y=col2,data=iris,hue="Species",fit_reg=False)
#     plt.xlabel(col1)
#     plt.ylabel(col2)
#     plt.title("鸢尾花种类分布")
#     plt.show()
# plot_iris(iris_d,'petal width','petal length')

# 数据集划分
x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.2)