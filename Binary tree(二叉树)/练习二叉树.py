#encoding:utf-8
#Time:2020/10/14 11:57
#Email:1215399218@qq.com
#Author:Mr.jia
#File:lsfd.PY
#Software:PyCharm
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __repr__(self):
        return f'Node{self.data}'
class Tree:
    def __init__(self):
        self.root=None
    def add(self,data):
        node=Node(data)
        if self.root is None:
            self.root=node
        else:
            temp=[self.root]
            while True:
                pop=temp.pop(0)
                if pop.left is None:
                    pop.left=node
                    return
                elif pop.right is None:
                    pop.right=node
                    return
                else:
                    temp.append(pop.left)
                    temp.append(pop.right)
if __name__ == '__main__':
    a = Tree()
    a.add(1)
    a.add(2)
    a.add(3)
    a.add(4)
    print(a.root.left)
    print(a.root.left.left)
