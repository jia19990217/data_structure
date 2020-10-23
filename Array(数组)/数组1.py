#encoding:utf-8
#Time:2020/10/9 9:21
#Email:1215399218@qq.com
#Author:Mr.jia
#File:数组1.PY
#Software:PyCharm
from typing import List
class Array:
    def __init__(self,capacity):
        self.array=[None]*capacity
        self.size=0
    def insert(self,index,element):
        if index<0 or index>len(self.array):
            raise ('越界')
        if self.size==len(self.array) or index>len(self.array):
            self.addcapcity()
        for i in range(self.size-1,index-1,-1):
            self.array[i+1]=self.array[i]
        self.array[index]=element
        self.size+=1
    def remove(self,index):
        for i  in range(index,self.size):
            self.array[i]=self.array[i+1]
        self.size-=1
    def addcapcity(self):
        new_array=[None]*len(self.array)*2
        for i  in  range(self.size):
            new_array[i]=self.array[i]
        self.array=new_array


a = Array(10)
a.insert(0, 1)
a.insert(1, 2)
a.insert(3, 3)
print(a.array)