#encoding:utf-8
#Time:2020/10/14 16:55
#Email:1215399218@qq.com
#Author:Mr.jia
#File:默写.PY
#Software:PyCharm
from pprint import  pformat
class Node:
    def __init__(self,data,parent):
        self.value=data
        self.left=None
        self.right=None
        self.parent=parent
    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return  pformat({'%s'%(self.value):(self.left,self.right)})
class Bst:
    def __init__(self):
        self.root=None
    def __repr__(self):
        return  str(self.root)
    def is_right(self,node):
        return  node==node.parent.right
    def search(self,value):
        if self.root is None:
            raise  ('空树')
        else:
            node=self.root
        while node and node.value!=value:
            if value>node.value:
                node=node.right
            else:
                node=node.left
        return  node
    def _reassign(self,node,new):
        if new is not None:
            node.parent=new.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.rigth=new
            else:
                node.parent.left=new
        else:
            self.root=new
    def get_max(self,node):
        while node.left:
            node=node.left
        return  node
    def remove(self,value):
        node=self.search(value)
        if node:
            if node.left is None and node.left is None:
                self._reassign(node,None)
            elif node.left is None:
                self._reassign(node,node.right)
            elif node.right is None:
                self._reassign(node,node.left)
            else:
                temp=self.get_max(node)
                self.remove(temp.value)
                node.value=temp.value
    def insert(self,value):
        node=Node(value,None)
        if self.root is None:
            self.root=node
        else:
            temp=self.root
            while True:
                if value>temp.value:
                    if temp.right is None:
                        temp.right=node
                        break
                    else:
                        temp=temp.right
                else:
                    if temp.left is None:
                        temp.left=node
                        break
                    else:temp=temp.left
            node.parent=temp
a = Bst()
# a.insert(10)
# a.insert(7)
# a.insert(6)
# a.insert(8)
# a.insert(4)
a.insert(3)
a.insert(3)
a.insert(3)
a.insert(3)
a.insert(3)
print(a)
a.remove(3)
print(a)




