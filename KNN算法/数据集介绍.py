from sklearn.datasets import load_iris,fetch_20newsgroups
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
print(desc)