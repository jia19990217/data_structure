#encoding:utf-8
#Time:2020/10/7 17:35
#Email:1215399218@qq.com
#Author:Mr.jia
#File:是否有环.PY
#Software:PyCharm
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.data)

def is_circle(head):
    k = head
    m = head
    while k:
        k = k.next.next
        m = m.next
        if k == m:
            return True
    return False
# 入环点
def huan(head):
    k = head
    m = head
    while k:
        k = k.next.next
        m = m.next
        if k == m :
            m=head
            while True:
                if m==k:
                    return m
                m=m.next
                k=k.next
                if m==k:
                    return m
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n4
print(huan(n1))