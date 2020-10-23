#encoding:utf-8
#Time:2020/10/13 17:16
#Email:1215399218@qq.com
#Author:Mr.jia
#File:反转数组.PY
#Software:PyCharm
def revere(num):
    p1=0
    p2=len(num)-1
    while p1<p2:
        num[p1],num[p2]=num[p2],num[p1]
        p1+=1
        p2-=1
    return  num

num=[1,3,4,6,7] #[4,3,2,1]
print(revere(num))
