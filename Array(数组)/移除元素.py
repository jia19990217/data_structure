#encoding:utf-8
#Time:2020/10/8 22:41
#Email:1215399218@qq.com
#Author:Mr.jia
#File:移除元素.PY
#Software:PyCharm
from typing import List
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
# 示例 1:
# 给定 nums = [3,2,2,3], val = 3,
# 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
# 你不需要考虑数组中超出新长度后面的元素。
# 示例 2:
# 给定 nums = [0,1,2,2,3,0,4,2], val = 2,
# 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
# 注意这五个元素可为任意顺序。
# 你不需要考虑数组中超出新长度后面的元素。
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        m=0
        while k <len(nums):
            if nums[k]==val:
                k+=1
            else:
                nums[m]=nums[k]
                k+=1
                m+=1
        return m



# nums = [3, 2, 2, 3]
nums = [0,1,2,2,3,0,4,2]
# val = 3
val = 2
a=Solution()
print(a.removeElement(nums,val),nums)