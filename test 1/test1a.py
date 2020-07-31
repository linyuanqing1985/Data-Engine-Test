# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 00:04:21 2020

@author: LinYuanqing
"""



import requests
import pandas as pd
from bs4 import BeautifulSoup

car_list=pd.DataFrame(columns=['名称','最低价格','最高价格','产品图片链接'])

# 请求URL
url = 'http://car.bitauto.com/xuanchegongju/?mid=8&page='
# 得到页面的内容
i=1
j=1
k=1
for x in range(1,4):
    urll=url+str(x)
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(urll,headers=headers,timeout=10)
    content = html.text
# 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content,"html.parser")  
    
  
   
# 分析取出结果
    print()
    for tag in soup.find_all('div', class_='search-result-list'):  
         for name in tag.find_all('p', class_='cx-name text-hover'):
            car_list.loc[i,'名称']=name.get_text()
            i=i+1
         for picture in tag.find_all('img'):
            car_list.loc[j,'产品图片链接']='http'+picture.get('src') 
            j=j+1
         for price in tag.find_all('p', class_='cx-price'):
            price1=price.get_text()
            if price1!='暂无':
                car_list.loc[k,'最低价格']=price1[0:price1.rfind('-')]+"万"
                car_list.loc[k,'最高价格']=price1[price1.rfind('-')+1:]
                k=k+1
            else:
                car_list.loc[k,'最低价格']="暂无"
                car_list.loc[k,'最高价格']="暂元"
                k=k+1                        


car_list.to_csv('project A result.csv',encoding="GBK")

    
    
    


