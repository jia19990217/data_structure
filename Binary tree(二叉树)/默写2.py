#encoding:utf-8
#Time:2020/10/16 9:04
#Email:1215399218@qq.com
#Author:Mr.jia
#File:默写2.PY
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
        return pformat({'%s'%(self.value):(self.left,self.right)})
class Bst:
    def __init__(self):
        self.root=None
    def __repr__(self):
        return str(self.root)
    def is_right(self,node):
        return node==node.parent.right
    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False
    def insert(self,value):
        #添加元素,先创建一个节点,看根史否为空,为空直接赋值,不为空,用变量记录根,开循环,传进来的值和根的值比较
        #如果大于,放到right,先看他是否为空,不为空让他变成他的下一个,反之left一样
        node=Node(value,None)
        if self.is_empty():
            self.root=node
        else:
            parent_node=self.root
            while True:
                if value>=parent_node.value:
                    if parent_node.right is None:
                        parent_node.right=node
                        break
                    else:
                        parent_node=parent_node.right
                else:
                    if parent_node.left is None:
                        parent_node.left=node
                        break
                    else:
                        parent_node=parent_node.left
            node.parent=parent_node
    def search(self,value):
        #先判断是否为空 不为空把根记录下来:开循环,比较
        if self.is_empty():
            raise ('空树')
        else:
            node=self.root
            while node and node.value!=value:
                if value>node.value:
                    node=node.right
                else:
                    node=node.left
            return  node
    def remove(self,data):
        #
        node=self.search(data)



    def pre_order(self,node):
        if node is None:
            return None
        print(node.value)
        self.pre_order(node.left)
        self.pre_order(node.right)
    def pre_order1(self,node):
        stack=[node]
        while len(stack)>0:
            print(node.value)
            if node.right :
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node=stack.pop()

    def in_order(self,node):
        # 中序递归
        if node is None:
            return None
        self.in_order(node.left)
        print(node.value)
        self.in_order(node.right)

    def houxu(self,node):
        # 后序递归
        if node is None:
            return None
        self.houxu(node.left)
        self.houxu(node.right)
        print(node.value)

    def post_order(self,node):
        #先判断是否为空,创俩个栈
        if node is None:
            return  False
        stack1=[]
        stack2=[]
        stack1.append(node)
        while stack1:
            node=stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            print(stack2.pop().value)


a = Bst()
a.insert(10)
a.insert(7)
a.insert(6)
a.insert(8)
a.insert(4)
print(a)
print(a.post_order(a.root))