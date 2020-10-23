#encoding:utf-8
#Time:2020/10/14 12:08
#Email:1215399218@qq.com
#Author:Mr.jia
#File:练习二叉搜索树.PY
#Software:PyCharm
from pprint import pformat
class Node:
    def __init__(self,data,parent):
        self.value=data
        self.left=None
        self.right=None
        self.parent=parent
    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        # return pformat({'%s'%(self.data):(self.left,self.right)})
        return pformat({'%s'%(self.value):(self.left,self.right)})
class Bst:
    def __init__(self):
        self.root=None
    def __repr__(self):
        return str(self.root)
    def insert(self,value):
        node=Node(value,None)
        if self.root is None:
            self.root=node
        else:
            par=self.root
            while True:
                if value< par.value:
                    if par.left is None:
                        par.left=node
                        break
                    else:
                        par=par.left
                else:
                    if par.right is None:
                        par.right=node
                        break
                    else:
                        par=par.right
            node.parent=par

a=Bst()
a.insert(10)
a.insert(7)
a.insert(6)
a.insert(8)
a.insert(4)
print(a)