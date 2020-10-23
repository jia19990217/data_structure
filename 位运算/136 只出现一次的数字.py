#encoding:utf-8
#Time:2020/10/16 16:31
#Email:1215399218@qq.com
#Author:Mr.jia
#File:136 只出现一次的数字.PY
#Software:PyCharm
from typing import  List
def zo(list:List):
    res=0
    for i in list:
        res=res^i
    return res
list=[4,1,2,1,2]
print(zo(list))

