#encoding:utf-8
#Time:2020/10/19 15:27
#Email:1215399218@qq.com
#Author:Mr.jia
#File:随机数.PY
#Software:PyCharm
import random
from typing import List
def randomL(n:int)->List:
    ilist=[]
    for i in range(n):
        ilist.append(random.randint(1, 100))
    return  ilist

# print(randomL(5))
