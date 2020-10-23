#encoding:utf-8
#Time:2020/10/19 9:34
#Email:1215399218@qq.com
#Author:Mr.jia
#File:青蛙跳.PY
#Software:PyCharm
def watiao(n):
    if n<=2:
        return n
    else:
        return watiao(n-1)+watiao(n-2)
print(watiao(3))
