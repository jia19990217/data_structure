# encoding:utf-8
# Time:2020/10/6 10:40
# Email:1215399218@qq.com
# Author:Mr.jia
# File:节点.PY
# Software:PyCharm
from typing import List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node({})".format(self.data)

class Linkedlist:
    def __init__(self):
        self.head = None
# 头部添加
    def insert_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node
# 尾部添加
    def append(self, data):
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.insert_head(data)
# 按位置添加
    def insert(self, i, data):
        if self.head is None or i == 1:
            self.insert_head(data)
        else:
            j = 1
            temp = self.head
            while j < i:
                pre = temp
                temp = temp.next
                j += 1
            node = Node(data)
            pre.next = node
            node.next = temp
# 插入列表
    def linklist(self, object: List):
        self.head = Node(object[0])
        temp = self.head
        for i in object[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next
# 删除头节点
    def delete_head(self):
        temp=self.head
        if temp:
            self.head=temp.next
#删除尾节点
    def delete(self):
        temp=self.head
        if temp:
            if temp.next is None:
                self.head=None
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next = None
        else:
            return "空链表"
# 格式输出
    def __repr__(self):
        curr = self.head
        str_data = ''
        while curr:
            str_data += "{}->".format(curr)
            curr = curr.next
        return str_data + 'END'

a = Linkedlist()
a.append(2)
a.append(3)
a.append(3)
a.delete()

print(a)
