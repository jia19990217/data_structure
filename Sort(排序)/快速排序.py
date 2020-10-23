#encoding:utf-8
#Time:2020/10/21 16:25
#Email:1215399218@qq.com
#Author:Mr.jia
#File:快速排序.PY
#Software:PyCharm
# def quickSort(array):
#     if len(array)<2:
#         return  array
#     else:
#         pivot=array[0]
#         less=[i for i in array[1:] if i <= pivot]
#         greater=[i for i in array[1:] if i > pivot]
#         return quickSort(less)+[pivot]+quickSort(greater)
# print(quickSort([6,4,3,9,2,7]))
from typing import  List
def swap(iList,p,q):
    iList[p],iList[q]=iList[q]=iList[p]
# def partition(iList:List,start,end):
#     pivot=iList[start]
#     p=start+1
#     q=end
#     while p<=q:
#         while p<=q and iList[p]<pivot:
#             p+=1
#         while p <= q and iList[q] > pivot:
#             q-=1
#         if p<q:
#             swap(iList,p,q)
#     swap(iList,start,q)
#     return q
def partition(iList:List,start,end):
    pivot=iList[start]
    mark=start
    for i in range(start+1,end+1):
        if iList[i]<pivot:
            mark+=1
            iList[mark],iList[i]=iList[i],iList[mark]
    iList[start]=iList[mark]
    iList[mark]=pivot
    return  mark
def quickSort(iList,start,end):
    if start>=end:
        return
    mid=partition(iList,start,end)
    quickSort(iList,start,mid-1)
    quickSort(iList,mid+1,end)
    return iList