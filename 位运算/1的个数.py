#encoding:utf-8
#Time:2020/10/16 16:16
#Email:1215399218@qq.com
#Author:Mr.jia
#File:1个个数.PY
#Software:PyCharm

def sn(n):
    count=0
    while True:
        if n==0:
            break
        else:
            n=n&(n-1)
            count+=1
    return  count

print(sn(31))