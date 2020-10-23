#encoding:utf-8
#Time:2020/10/9 15:40
#Email:1215399218@qq.com
#Author:Mr.jia
#File:stack.PY
#Software:PyCharm
from typing import List
class Stack:
    def __init__(self):
        self.stack=[]
        self.size=0
    def __repr__(self):
        return f'{self.stack}'
    def push(self,data):
        self.stack.append(data)
        self.size+=1
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.size-=1
    def peek(self):
        if self.stack:
            return self.stack[-1]
    def is_empty(self):
        return   not bool(self.stack)
a=Stack()
a.push(1)
a.push(12)
a.push(13)
print(a)


