#encoding:utf-8
#Time:2020/10/9 16:08
#Email:1215399218@qq.com
#Author:Mr.jia
#File:linkedlist_stack.PY
#Software:PyCharm
from typing import List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f'Node({self.data})'
class Stack:
    def __init__(self):
        self.top=None
        self.size=0
    def push(self,data):
        node=Node(data)
        if self.top is None:
            self.top=node
        else:
            node.next=self.top
            self.top=node
        self.size+=1
    def pop(self):
        if self.top:
            self.top=self.top.next
            self.size-=1
        else:
            raise  IndexError('越界')
    def __repr__(self):
        cur=self.top
        str_data=''
        while cur:
            str_data+=f'{cur}-->'
            cur=cur.next
        return str_data+'END'
a=Stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.pop()
print(a)

class Stack1:
    def __init__(self):
        self.top=None
        self.size=0
    def __repr__(self):
        cur=self.top
        str_data=''
        while cur:
            str_data+=f'{cur}-->'
            cur=cur.next
        return str_data+'END'
    def push(self,data):
        node=Node(data)
        if self.top is None:
            self.top=node
        else:
            node.next=self.top
            self.top=node
        self.size+=1
    def pop(self):
        self.top=self.top.next
        self.size-=1
a=Stack1()
a.push(1)
a.push(3)
a.push(3)
a.push(4)
a.pop()
print(a)