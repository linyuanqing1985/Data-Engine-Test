# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 23:02:16 2020

@author: LinYuanqing
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:17:59 2020

@author: LinYuanqing
"""


import pandas as pd
from efficient_apriori import apriori

def use_efficient_apriori(tran):
    # 使用 efficient_apriori
    # 挖掘频繁项集和频繁规则
    item, rules = apriori(tran, min_support=0.09,  min_confidence=0.4)
    print("频繁项集：", item)
    print("关联规则：", rules)
    


def main():
    address='C:\\Users\\linyuanqing\\Desktop\\订单表.csv'
    data=pd.read_csv(address,encoding='gbk')
    order_list=data[['客户ID','产品名称']]
    transactions = []
    for customer in order_list['客户ID'].drop_duplicates():
        temp=order_list.loc[(order_list['客户ID'] == customer)]
        tempproduct=[]
        for product in temp['产品名称']:
            if product not in tempproduct:
                tempproduct.append(product)
                
        transactions.append(tempproduct)
   

    use_efficient_apriori(transactions)

if __name__ == '__main__':
    main()
