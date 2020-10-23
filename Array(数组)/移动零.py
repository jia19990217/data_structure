#encoding:utf-8
#Time:2020/10/8 23:10
#Email:1215399218@qq.com
#Author:Mr.jia
#File:移动零.PY
#Software:PyCharm
from typing import List
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 示例:
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k=0
        m=0
        while k<len(nums):
            if nums[k]==0:
                k+=1
            else:
                nums[m]=nums[k]
                k+=1
                m+=1
        for i in range(1,len(nums)-m+1):
            nums[-i]=0
        return nums
nums=[0,1,0,3,12,2,5]
a=Solution()
print(a.moveZeroes(nums))