#encoding:utf-8
#Time:2020/10/19 9:18
#Email:1215399218@qq.com
#Author:Mr.jia
#File:阶乘.PY
#Software:PyCharm
def jiecheng(n):
    if n==1:
        return n
    return jiecheng(n-1)*n
print(jiecheng(3))