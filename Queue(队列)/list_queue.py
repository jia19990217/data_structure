#encoding:utf-8
#Time:2020/10/12 12:05
#Email:1215399218@qq.com
#Author:Mr.jia
#File:队列.PY
#Software:PyCharm
from typing import List
class Pueue:
    def __init__(self):
        self.entries=[]
        self.size=0
    def __repr__(self):
        return f'{self.entries}'
    def put(self,data):
        self.entries.append(data)
        self.size+=1
    def depueue(self):
        self.entries=self.entries[1:]
        self.size-=1
    def length(self):
        return self.size
    def reversal(self):
        self.entries=self.entries[::-1]


a=Pueue()
a.put(1)
a.put(2)
a.put(3)
a.put(4)
a.put(5)
# print(a.get(2))
# print(a.length())
print(a)
a.reversal()
print(a)
