#encoding:utf-8
#Time:2020/10/15 11:12
#Email:1215399218@qq.com
#Author:Mr.jia
#File:黄金分割数列.PY
#Software:PyCharm
import  time
def fib(n):
    if n<=1:
        return  n
    else:
        return  fib(n-1) +fib(n-2)
a=time.time()
print(fib(40))
b=time.time()
c=b-a
print(c)