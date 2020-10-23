# encoding:utf-8
# Time:2020/10/7 13:47
# Email:1215399218@qq.com
# Author:Mr.jia
# File:节点4.PY
# Software:PyCharm
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.data)


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        cur = self.head
        str_data = ''
        while cur:
            str_data += f'{cur}-->'
            cur = cur.next
        return str_data + 'END'
# 查

    def get(self, index):
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur

# 添加
    def insert(self, index, data):
        node = Node(data)
        if index < 0 or index > self.size:
            raise ('越界')
        elif self.size == 0:
            self.head = node
            self.tail = node
        elif index == 0:
            node.next = self.head
            self.head = node
        elif index == self.tail:
            self.tail.next = node
            self.tail = node
        else:
            pre = self.get(index - 1)
            node.next = pre.next
            pre.next = node
        self.size += 1
#删除
    def remove(self, index):
        if index<0 or index>=self.size or self.size==0:
            raise ('越界')
        elif  index==0:   #删除头
            self.head=self.head.next
        elif index==self.size-1:   #删除尾
            pre=self.get(index-1)
            pre.next=None
            self.tail=pre
        else:
            pre=self.get(index-1)
            pre.next=pre.next.next
        self.size-=1
#翻转
    def revese(self):
        pre=None
        cur=self.head
        while cur:
            next_node=cur.next
            cur.next=pre
            pre=cur
            cur=next_node
        self.head=pre
#是否有环
    def huan(self):
        k=self.head
        m=self.head
        while k.next and k :
            k=k.next.next
            m=m.next
            if k==m:
                return  True
        return False
# 倒数第k个元素
    def daoshu(self,k):
        index=self.size-k
        cur=self.get(index)
        return  cur
a = Linkedlist()
a.insert(0, 1)
a.insert(1, 2)
a.insert(2, 3)
a.insert(2, 4)
a.insert(2, 5)
a.insert(2, 6)
a.insert(2, 7)

print(a)
print(a.size)
print(a.huan())
print(a.daoshu(4))



# 找到倒数第k个元素
