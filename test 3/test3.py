# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 18:42:33 2020

@author: LinYuanqing
"""

from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
import pandas as pd

from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt

address='C:\\Users\\linyuanqing\\Desktop\\Data_Engine_with_Python-master\\ProjectC\\CarPrice_Assignment.csv'
data=pd.read_csv(address)


tempdata=data
tempdata=tempdata.drop(columns='CarName')
tempdata=tempdata.drop(columns='car_ID')

# 规范化到 [0,1] 空间
le = LabelEncoder()
for title in['fueltype','aspiration','doornumber','carbody','drivewheel','enginelocation','cylindernumber','enginetype','fuelsystem']:
    tempdata[title] = le.fit_transform(tempdata[title])

min_max_scaler = preprocessing.MinMaxScaler()
tempdata= min_max_scaler.fit_transform(tempdata)


# K手肘法, 观察14为手肘位置
sse = []
for k in range(2, 50):
	# kmeans算法
	kmeans = KMeans(n_clusters=k)
	kmeans.fit(tempdata)
	# 计算inertia簇内误差平方和
	sse.append(kmeans.inertia_)
x = range(2, 50)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()


kmeans = KMeans(n_clusters=14)
kmeans.fit(tempdata)
predict_y = kmeans.predict(tempdata)

# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'group'},axis=1,inplace=True)

# 列出vw车型，选择需要查找竞品的车型
vwcarlist={1:'vokswagen rabbit',
           2:'volkswagen 1131 deluxe sedan',
           3:'volkswagen model 111',
           4:'volkswagen type 3',
           5:'volkswagen 411 (sw)',
           6:'volkswagen super beetle',
           7:'volkswagen dasher',
           8:'vw dasher',
           9:'vw rabbit'}

print('vw 车型列表')
print(vwcarlist)

choosecar=vwcarlist[int(input('请输入对标车型代号: '))]
benchmarkno=result.loc[(result['CarName'] == choosecar)]['group'].values

print(choosecar + '竞品：')
print(result.loc[result['group']==benchmarkno[0]]['CarName'])

# 将结果导出到CSV文件中
result.to_csv("project C result.csv",index="False",encoding="GBK")



