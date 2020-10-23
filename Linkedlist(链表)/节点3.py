# encoding:utf-8
# Time:2020/10/6 21:32
# Email:1215399218@qq.com
# Author:Mr.jia
# File:节点2.PY
# Software:PyCharm
from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.data)


class Linkedlist:
    def __init__(self):
        self.head = None

    def __repr__(self):
        cur = self.head
        str_data = ''
        while cur:
            str_data += f'{cur}-->'
            cur = cur.next
        return str_data + 'END'
# 添加头部

    def insert_head(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
        self.head = node
# 添加尾部

    def append(self, data):
        if self.head:
            temp = self.head
            while temp:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.insert_head(data)
# 位置插入

    def insert(self, i, data):
        if i == 1 or self.head is None:
            self.insert_head(data)
        else:
            j = 1
            temp = self.head
            while j < i:
                pre = temp
                temp = temp.temp
                j += 1
            node = Node(data)
            pre.next = node
            node.next = temp


# 列表插入

    def linklist(self, object: List):
        self.head = Node(object[0])
        temp = self.head
        for i in object[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.nex
# 删除头部

    def delete_head(self):
        temp = self.head
        if temp:
            self.head = temp.next
# 删除尾部

    def delete(self):
        temp = self.head
        if temp:
            if temp.next is None:
                temp = None
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next = None
        else:
            print('空链表')
# 翻转`
    def reverse(self):
        pre=None
        cur=self.head
        while cur:
            next_node=cur.next
            cur.next=pre
            pre=cur
            cur=next_node
        self.head=pre

#raise indexerror("the linked list is empty")
# 查
    def get(self,index):
        cur=self.head
        if cur is None:
            print('空的')
        for _ in range(1,index):
            if cur.next is None:
                print('越界')
            cur=cur.next
        return cur
# 改
    def set(self,index,data):
        cur=self.head
        if cur is None:
            print('空的')
        for _ in range(1,index):
            if cur.next is None:
                print('越界')
            cur=cur.next
        cur.data=data



a = Linkedlist()
a.insert_head(2)
a.insert_head(3)
a.insert_head(4)
a.reverse()
a.set(2,6)
print(a.get(2))
