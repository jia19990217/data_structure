#encoding:utf-8
#Time:2020/10/13 17:14
#Email:1215399218@qq.com
#Author:Mr.jia
#File:二分查找.PY
#Software:PyCharm
from typing import List
class Solution:
    def search(self, nums: List[int], target: int):
        p1=0
        p2=len(nums)-1
        while p1<p2:
            mid=(p1+p2)//2
            if target not in nums:
                return -1
            if target>nums[mid]:
                p1=mid
            elif target<nums[mid]:
                p2=mid
            else:
                return mid

nums = [-1,0,3,5,9,12]
target = 9
a=Solution()
print(a.search(nums,target))