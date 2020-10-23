#encoding:utf-8
#Time:2020/10/22 11:23
#Email:1215399218@qq.com
#Author:Mr.jia
#File:计数排序.PY
#Software:PyCharm
from  typing import  List
def countSort(arr:List):
    max_value=max(arr)
    count_arr=[0]*(max_value+1)
    for i in range(len(arr)):
        count_arr[arr[i]]+=1
    sort_arr=[]
    for i  in range(len(count_arr)):
        for j in range(count_arr[i]):
            sort_arr.append(i)
    return  sort_arr
arr=[2,3,5,6,3,2,2,99]
print(countSort(arr))