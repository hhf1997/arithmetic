from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

data=pd.read_csv(r'F:\python\KNN算法\iris.csv')

print(data.head(20))