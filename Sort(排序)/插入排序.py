#encoding:utf-8
#Time:2020/10/20 15:04
#Email:1215399218@qq.com
#Author:Mr.jia
#File:插入排序.PY
#Software:PyCharm
from sort import randomList
from typing import List
def insert_sort(nums:List):
    for r in range(1,len(nums)):
        target=nums[r]
        for l in range(r):
            if nums[l]>nums[r]:
                nums[l+1:r+1]=nums[l:r]
                nums[l]=target
                break
    return nums
nums=randomList.randomL(10)
print(insert_sort(nums))

