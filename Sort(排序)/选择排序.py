#encoding:utf-8
#Time:2020/10/19 16:15
#Email:1215399218@qq.com
#Author:Mr.jia
#File:选择排序.PY
#Software:PyCharm
from sort import randomList
from typing import List
# def selection_sort(nums):
#     count=0
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i]>nums[j]:
#                 count+=1
#                 nums[i],nums[j]=nums[j],nums[i]
#                 print('第%s次结果为'%(count),nums)
#     print(nums)
# def selection_sort(nums:List):
#     if len(nums)<=1:
#         return  nums
#     for i in range(len(nums)-1):
#         minindex=i
#         for j in range(i+1,len(nums)):
#             if nums[j]<nums[minindex]:
#                 minindex=j
#         nums[i],nums[minindex]=nums[minindex],nums[i]
#         print('第%s次结果为'%(i+1),nums)
#
# nums=[7, 82, 78, 97, 49, 12, 84, 14, 59, 13]
# selection_sort(nums)

a=randomList.randomL(10)
print(a)


