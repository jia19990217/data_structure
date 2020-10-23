#encoding:utf-8
#Time:2020/10/7 21:13
#Email:1215399218@qq.com
#Author:Mr.jia
#File:简略版 节点.PY
#Software:PyCharm
from typing import  List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return  f'Node({self.data})'
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def __repr__(self):
        cur=self.head
        str_data=''
        while cur:
            str_data+=f'{cur}-->'
            cur=cur.next
        return  str_data+'END'
#查
    def get(self,index):
        temp=self.head
        if temp is None:
            print('空的')
        for _ in range(index):
            temp=temp.next
        return temp
#改
    def set(self,index,data):
        temp=self.head
        if temp is None:
            print('空的')
        for _ in range(index):
            temp=temp.next
        temp.data=data
# 添加
    def insert(self,index,data):
        node=Node(data)
        if index<0 or index>self.size:
            raise ('越界')
        elif self.size==0:
            self.head=node
            self.tail=node
        elif index==0:
            node.next=self.head
            self.head=node
        elif index==self.size:
            self.tail.next=node
            self.tail=node
        else:
            pre=self.get(index-1)
            node.next=pre.next
            pre.next=node
        self.size+=1
#删除
    def remove(self,index):
        if index<0 or index>=self.size or self.size==0:
            print('越界')
        elif index==0:
            self.head=self.head.next
        elif index==self.size-1:
            pre=self.get(index-1)
            pre.next=None
            self.tail=pre
        else:
            pre=self.get(index-1)
            pre.next=pre.next.next
        self.size-=1
# 翻转
    def reverse(self):
        pre=None
        cur=self.head
        while cur:
            node=cur.next
            cur.next=pre
            pre=cur
            cur=node
        self.head=pre
# 列表插入
    def linklist(self,object:List):
        self.head=object[0]
        temp=self.head
        for i in object[1:]:
            node=Node(i)
            temp.next=node
            temp=temp.next

a = Linkedlist()
a.insert(0, 1)
a.insert(1, 2)
a.insert(2, 3)
a.insert(2, 4)
a.insert(2, 5)
a.insert(2, 6)
a.insert(2, 7)

print(a)
