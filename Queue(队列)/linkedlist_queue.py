#encoding:utf-8
#Time:2020/10/12 16:31
#Email:1215399218@qq.com
#Author:Mr.jia
#File:linkedlist_queue.PY
#Software:PyCharm
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f'Node({self.data})'
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    def enpueue(self,data):
        node=Node(data)
        if self.front:
            node.next=self.front
            self.front=node
        else:
            self.front=node
            self.rear=node
        self.size+=1
    def depueue(self):
        if self.size==0:
            raise IndexError('空队列')
        else:
            node=self.front
            self.front = self.front.next
            self.size -= 1
        return node
    def __repr__(self):
        cur=self.front
        str_q=''
        while cur:
            str_q+=f'{cur}-->'
            cur=cur.next
        return str_q+'end'

    def is_empty(self):
        return  self.front is None
    def empty(self):
        return  not bool(self.front)
if __name__ == '__main__':
    q=Queue()
    q.enpueue(1)
    q.enpueue(2)
    q.enpueue(2)
    print(q)
    print(q.is_empty())
    print(q.empty())