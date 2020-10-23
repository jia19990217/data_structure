#encoding:utf-8
#Time:2020/10/20 16:23
#Email:1215399218@qq.com
#Author:Mr.jia
#File:插入排序 链表.PY
#Software:PyCharm
class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
    def __repr__(self):
        return f'Node({self.data})'
def insertList(head:Node):
    dummy=Node(0)
    pre=dummy
    cur=head
    while cur:
        temp=cur.next
        while pre.next and pre.next.data<cur.data:
            pre=pre.pre.next
        cur.next=pre.next
        pre.next=cur
        cur=temp
        pre=dummy
    return dummy.next
if __name__ == '__main__':
    n1=Node(3)
    n2=Node(4)
    n3=Node(1)
    n4=Node(2)
    n5=Node(5)
    n1.next=n2
    n2.next=n3
    n3.next=n4
    n4.next=n5
    print(insertList(n1))

