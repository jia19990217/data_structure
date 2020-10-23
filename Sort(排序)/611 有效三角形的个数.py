#encoding:utf-8
#Time:2020/10/21 15:08
#Email:1215399218@qq.com
#Author:Mr.jia
#File:三角形.PY
#Software:PyCharm
from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        for i in range(2,len(nums)):
            left=0
            right=i-1
            while left<right:
                if nums[left]+nums[right]>nums[i]:
                    count+=right-left
                    right-=1
                else:
                    left+=1
        return  count
nums=[2,2,3,4]
a=Solution()
print(a.triangleNumber(nums))