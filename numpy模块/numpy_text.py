import numpy as np
import random

# ndarray运算
# 逻辑运算
stock_change=np.random.normal(0,1,(8,10))
stock_c=stock_change[0:5,0:5]
stock_c[stock_c>1]=2
# print(stock_c)
stock_d=stock_change[0:2,0:5]

# print(np.where(stock_d > 0.5, 1, 0))

A=np.array([[1,2,3],[4,5,6],[7,8,0]])
B=np.array([[1,2,1],[1,1,2],[2,1,1]])
print(np.matmul(A,B))