#encoding:utf-8
#Time:2020/10/8 9:02
#Email:1215399218@qq.com
#Author:Mr.jia
#File:简略版.PY
#Software:PyCharm
# from typing import ListNode
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f'Node({self.data})'
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
        for _ in range(index):
            temp=temp.next
        return  temp
# 改
    def set(self,index,data):
        temp=self.head
        for _ in range(index):
            temp=temp.next
        temp.data=data
#增
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
# 删
    def remove(self,index):
        if index<0 or index>=self.size:
            raise ('越界')
        elif index==0:
            self.head = self.head.next
        elif index==self.size-1:
            pre = self.get(index-1)
            pre.next = None
            self.tail = pre
        else:
            pre = self.get(index - 1)
            pre.next = pre.next.next
        self.size-=1

    def deleteNode(self,data):
        cur = self.head
        if cur.data == data:
            self.remove(0)
        while cur.next:
            if cur.next.data == data:
                cur.next = cur.next.next
            else:
                cur = cur.next
    def remove_data(self,head,val):
        dummy=Node(0)
        dummy.next=head
        cur=dummy
        while cur.next:
            if cur.next.data==val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return  dummy.next
a = Linkedlist()
a.insert(0, 1)
a.insert(1, 2)
a.insert(2, 3)

# a.deleteNode(1)

a.remove_data(Node(1),2)
print(a)

