#encoding:utf-8
#Time:2020/10/8 19:11
#Email:1215399218@qq.com
#Author:Mr.jia
#File:删除重复.PY
#Software:PyCharm
from typing import List
# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
# 示例 1:
# 给定数组 nums = [1,1,2],
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
# 你不需要考虑数组中超出新长度后面的元素。
# 示例 2:
# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
# 你不需要考虑数组中超出新长度后面的元素。

# class Solution:
#     def removeDuplicates(self, nums):
#         m=0
#         k=1
#         while k<len(nums):
#             if nums[k]==nums[m]:
#                 k+=1
#             else:
#                 m+=1
#                 nums[m]=nums[k]
#                 k+=1
#         return m+1
class Solution:
    def removeDuplicates(self, nums):
        n=len(set(nums))
        i=0
        while i<n-1:
            if nums[i]==nums[i+1]:
                temp=nums[i+1]
                nums[i+1:len(nums)-1]=nums[i+2:]
                nums[-1]=temp
                # continue
            else:
                i+=1
        return i+1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums = [1,1,2]
a=Solution()
print(a.removeDuplicates(nums),nums)