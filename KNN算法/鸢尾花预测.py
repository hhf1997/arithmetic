# 机器学习流程步骤
"""
1获取数据
2数据基本处理
3特征工程
4机器学习（模型训练）
5模型评估
"""
#获取数据模块
from sklearn.datasets import load_iris
# 数据分割
from sklearn.model_selection import  train_test_split
# 标准化模块
from sklearn.preprocessing import StandardScaler
# 机器学习模型KNN模块
from sklearn.neighbors import KNeighborsClassifier


# 1获取数据集
iris=load_iris()
# 2数据基本处理
x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,random_state=22,test_size=0.2)
# 3特征工程
# 3.1实例化
transfer = StandardScaler()
# 3.2调用api
x_train = transfer.fit_transform(x_train)
x_test  = transfer.fit_transform(x_test)

# 4机器学习（模型训练）
# 4.1实列化一个估计器
estimator=KNeighborsClassifier(n_neighbors=5)
# 进行模型训练
estimator.fit(x_train,y_train)

# 5模型评估
# 5.1输出预测值
y_pre=estimator.predict(x_test)
print("预测值是：\n",y_pre)
# 5.2输出准确率
ret=estimator.score(x_test,y_test)
print("准确率是：\n",ret)