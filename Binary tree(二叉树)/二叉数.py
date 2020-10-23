#encoding:utf-8
#Time:2020/10/13 11:08
#Email:1215399218@qq.com
#Author:Mr.jia
#File:二叉数.PY
#Software:PyCharm

#满二叉数:
#一个二叉树的所有非叶子结点都存在左右孩子,并且所有的叶子结点都爱在统一层级上,叫做满二叉数
#完全二叉树:
#对树中的结点按从上至下、从左到右的顺序进行编号，如果编号为i（1≤i≤n）的结点与满二叉树中编号为i的结点在二叉树中的位置相同，则这棵二叉树称为完全二叉树。
# 二叉搜索树:
# 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。
#平衡树(AVL)|红黑树



class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __repr__(self):
        return f'Node({self.data})'
class Tree:
    def __init__(self):
        self.root=None
    def add(self,item): #添加结点
        node=Node(item)
        if self.root is None:
            self.root=node
        else:
            temp=[self.root]
            while True:
                pop_hode=temp.pop(0)
                if pop_hode.left is None:
                    pop_hode.left=node
                    return
                elif pop_hode.right is None:
                    pop_hode.right=node
                    return
                else:
                    temp.append(pop_hode.left)
                    temp.append(pop_hode.right)

    def get_parent(self,item):
        if self.root.data==item:
            return  None #根节点没有父节点
        temp=[self.root]
        while temp:
            pop_node=temp.pop(0)
            if pop_node.left.data==item:
                return pop_node
            if pop_node.right.data==item:
                return pop_node
            if pop_node.left:
                temp.append(pop_node.left)
            if pop_node.right:
                temp.append(pop_node.right)
        return None

if __name__ == '__main__':
    a=Tree()
    a.add(1)
    a.add(2)
    a.add(3)
    a.add(4)
    print(a.get_parent(4))
