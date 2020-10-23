#encoding:utf-8
#Time:2020/10/9 17:39
#Email:1215399218@qq.com
#Author:Mr.jia
#File:删除重复,可以保留2个.PY
#Software:PyCharm
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        m=0
        count=1
        while k<len(nums):
            if nums[m]==nums[k]:
                count+=1
                if count==2:
                    m+=1
                    nums[m]=nums[k]
                k+=1
            else:
                m+=1
                nums[m]=nums[k]
                k+=1
                count=1
        return m+1