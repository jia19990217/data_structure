#encoding:utf-8
#Time:2020/10/21 15:33
#Email:1215399218@qq.com
#Author:Mr.jia
#File:归并排序.PY
#Software:PyCharm


def mergeSort(nums):
    if len(nums)<=1:
        return  nums
    middle=len(nums)//2
    left,right=nums[0:middle],nums[middle:]
    return  merge(mergeSort(left),mergeSort(right))
def merge(left,right):

    list=[]
    while left and right:
        if left[0]>=right[0]:
            list.append(right.pop(0))
        else:
            list.append(left.pop(0))
    # while left:[
    #     list.append(left.pop(0))
    # while right:
    #     list.append(right.pop(0))
    if left:
        list.extend(left)
    if right:
        list.extend(right)
    return list
def merge1(left,right):
    l=len(left)
    r=len(right)
    list=[]
    i=0
    j=0
    while i<l and j<r:
        if left[i]<=right[j]:
            list.append(left[i])
            i+=1
        else:
            list.append(right[j])
            j+=1
    list.extend(left[i:])
    list.extend(right[j:])
    return list
nums=[8,7,2,6,1,4,5,2]
print(mergeSort(nums))