#encoding:utf-8
#Time:2020/10/16 11:23
#Email:1215399218@qq.com
#Author:Mr.jia
#File:二叉堆.PY
#Software:PyCharm

class Heap:
    def __init__(self):
        self.data_list=[]
    def __repr__(self):
        return str(self.data_list)
    def get_parent_index(self,index):
        if index==0 or index>len(self.data_list)-1:
            return  None
        else:
            return (index-1)>>1
    def  swap(self,index_a,index_b):
        self.data_list[index_a], self.data_list[index_b]=self.data_list[index_b],self.data_list[index_a]
    def insert(self,data):
        self.data_list.append(data)
        index=len(self.data_list)-1
        parent=self.get_parent_index(index)
        while  parent is not  None and self.data_list[parent]<self.data_list[index] :
            self.swap(parent,index)
            index=parent
            parent=self.get_parent_index(index)
    def pop(self):
        remove_data=self.data_list[0]
        self.data_list[0]=self.data_list[-1]
        del  self.data_list[-1]
        self.heapify(0)
        return  remove_data
    def heapify(self,index):
        todoy=len(self.data_list)-1
        max_index = index
        while True:
            if 2*index+1<=todoy and  self.data_list[2*index+1]>self.data_list[max_index]:
                max_index=2*index+1
            if 2 * index + 2 <= todoy and self.data_list[2 * index + 1] > self.data_list[max_index]:
                max_index = 2 * index + 2
            if max_index==index:
                break
            self.swap(index ,max_index)
            index=max_index


if __name__ == '__main__':
    a=Heap()
    for i in range(5):
        a.insert(i+1)
    print('建堆:',a.data_list)
    print('删除堆顶元素:', a.pop())
    print('删除堆顶元素:', a.pop())
    print('删除堆顶元素:', a.pop())
    print('删除堆顶元素:', a.pop())
    print('删除堆顶元素:', a.pop())
