#encoding:utf-8
#Time:2020/10/7 21:10
#Email:1215399218@qq.com
#Author:Mr.jia
#File:入环点.PY
#Software:PyCharm
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.data)
# 入环点
# def huan(head):
#     k = head
#     m = head
#     while k and k.next:
#         k = k.next.next
#         m = m.next
#         if k == m :
#             m=head
#             while True:
#                 if m==k:
#                     return m
#                 m=m.next
#                 k=k.next
#                 if m==k:
#                     return m


    # def detectCirclePoint(head):
    #     slow=head
    #     fast=head
    #     while fast and fast.next :
    #         slow=slow.next
    #         fast=fast.next.next
    #         if slow==fast:
    #             break
    #     slow=head
    #     while slow!=fast:
    #         slow=slow.next
    #         fast=fast.next
    #     return slow
def huan(head):#判断是否是环
    k=head
    m=head
    while k and k.next:
        k=k.next.next
        m=m.next
        if k==m:
            return  True
    return False
def ruhuandian(head): #找入环点
    k=head
    m=head
    while k and k.next:
        k=k.next.next
        m=m.next
        if k==m:
            m=head
            while m!=k:
                m=m.next
                k=k.next
            return  k

def remove_data(head,val): #删除指点元素
    dummy=Node(0)
    dummy.next=head
    cur=dummy
    while cur.next:
        if cur.next.data==val:
            cur.next=cur.next.next
        else:
            cur=cur.next
    return  dummy.next

def jiaohuan(head):  #两两交换
    pre=dummy=Node(0)
    dummy.next=head
    while pre.next and pre.next.next:
        #指针上岗
        k=pre.next.next
        m=pre.next
        #交换位置
        pre.next=k
        m.next=k.next
        k.next=m
        pre=pre.next.next
    return  dummy.next

def hebing(l1:Node,l2:Node): #合并
    dummy=Node(0)
    cur=dummy
    while l1 and l2: #or
        if l1.data>=l2.data:
            cur.next=Node(l1.data)
            l1.next=l1
        else:
            cur.next=Node(l2.data)
            l2.next=next
        cur=cur.next
    if l1 is None: #缩进拉后 加break
        cur.next=l2
    if l2 is None:
        cur.next=l1
    return dummy.next

def print_data(head):  #格式输出
    pre=head
    while pre:
        print(pre.data,end="-->")
        pre=pre.next
if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None









