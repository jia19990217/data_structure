# encoding:utf-8
# Time:2020/10/13 15:12
# Email:1215399218@qq.com
# Author:Mr.jia
# File:二叉搜索树.PY
# Software:PyCharm
from pprint import pformat


class Node:
    def __init__(self, data, parent):
        self.value = data
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({'%s' % (self.value): (
            self.left, self.right)}, indent=3,)


class Bst:  # binary search tree
    def __init__(self):
        self.root = None

    def __repr__(self):
        return str(self.root)

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def insert(self, value):
        node = Node(value, None)
        if self.is_empty():
            self.root = node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = node
                        break
                    else:
                        parent_node = parent_node.right
            node.parent = parent_node

    def search(self, data):
        if self.root is None:
            raise ('空树')
        else:
            node = self.root
            while node and node.value != data:
                if data > node.value:
                    node = node.right
                else:
                    node = node.left
            return node

    def is_right(self, node):
        return node == node.parent.right  # 是否是右孩子
    # def _reassign_node(self,node,new):
    #     if  new is not None:#如果节点不为空
    #         new.parent=node.parent #找父亲
    #     if node.parent is not None:  #找孩子
    #         if self.is_right(node):
    #             node.parent.right=new
    #         else:
    #             node.parent.left=new
    #     else:
    #         self.root=new
    # def remove(self,value):
    #     node=self.search(value)
    #     if node is not None:
    #         if node.left is None and node.right is None:
    #             self._reassign_node(node,None)
    #         elif node.left is None:
    #             self._reassign_node(node,node.right)
    #         elif node.right is None:
    #             self._reassign_node(node,node.left)
    #         else:
    #             temp_node=self.get_max(node.left)
    #             self.remove(temp_node.value)
    #             node.value=temp_node.value

    def remove(self, value):
        node = self.search(value)
        if node:
            if node.left is None and node.right is None:
                self._reassign_node(node, None)
            elif node.left is None:
                self._reassign_node(node, node.right)
            elif node.right is None:
                self._reassign_node(node, node.left)
            else:
                temp = self.get_max(node.left)
                self.remove(temp.value)
                node.value = temp.value

    def _reassign_node(self, node, new):
        if new is not None:
            new.parent = node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right = new
            else:
                node.parent.left = new
        else:
            self.root = new

    def get_max(self, node):
        if node is None:
            node=self.root
        if not self.is_empty():
            while node is not None:
                node=node.right
        return node
    def get_min(self, node):
        if node is None:
            node=self.root
        if not self.is_empty():
            node=self.root
            while node is not None:
                node=node.left
        return node


    def preOrder(self, node):
        if node is None:
            return None
        print(node.value)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def preOrder2(self, node):
        stack = [node]
        while len(stack) > 0:
            print(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node=stack.pop()
    def zhongxu(self,node):
        if node is None:
            return  node
        self.zhongxu(node.left)
        print(node.value)
        self.zhongxu(node.right)

    def in_order_stack(self,node):
        stack=[]
        while node or len(stack)>0:
            while node:
                stack.append(node)
                node=node.left
            if len(stack)>0:
                node=stack.pop()
                print(node.value)
                node=node.right
    def post_order(self,node):
        if node is None:
            return  False
        else:
            s1=[]
            s2=[]
            s1.append(node)
            while s1:
                node=s1.pop()
                if node.left:
                    s1.append(node.left)
                if node.right:
                    s1.append(node.right)
                s2.append(node)
            while s2:
                print(s2.pop().value)

    def cx(self,node):
        if node is  None:
            return None
        else:
            s1=[node]
            while s1:
                node=s1.pop()
                print(node.value)
                if node.left:
                    s1.append(node.left)
                if node.right:
                    s1.append(node.right)# ----------------------------------------------------------------



a = Bst()
a.insert(10)
a.insert(7)
a.insert(6)
a.insert(8)
a.insert(4)
print(a)
# a.remove(4)
# print(a)
# a.preOrder2(a.root)
# a.post_order(a.root)
a.cx(a.root)