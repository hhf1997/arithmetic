# 导入模块说明
# 导入画图模块
import matplotlib.pyplot as plt
# 导入创建数据集模块
from sklearn import datasets
# 导入聚类模块
from sklearn.cluster import KMeans
# 导入评估模型
from sklearn.metrics import calinski_harabasz_score


# 创建数据集
# x 为样本特征y 为样本类别，共1000个样本，每个样本4个特征值，共四个簇
data = datasets.make_blobs(n_samples=1000,n_features=2,centers=[[-1,-1],[0,0],[1,1],[2,2]],cluster_std=[0.4,0.1,0.1,0.1],random_state=1)
    # n_samples  产生多少个数
    # n_features 样本的特征数
    # centers   生成的中心位置
    # random_state  为创建数组值生成随机数
# 画图
plt.plot(data[:,0],data[:,1])