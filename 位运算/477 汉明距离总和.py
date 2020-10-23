#encoding:utf-8
#Time:2020/10/18 21:17
#Email:1215399218@qq.com
#Author:Mr.jia
#File:477 汉明距离总和.PY
#Software:PyCharm
from typing import  List
# 两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。
# 计算一个数组中，任意两个数之间汉明距离的总和。
# 示例:
# 输入: 4, 14, 2
# 输出: 6
# 解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
# 所以答案为：
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        zc=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                a=nums[i]^nums[j]
                count = 0
                while a != 0:
                    a = a & (a - 1)
                    count += 1
                zc+=count
        return zc
b=Solution()
print(b.totalHammingDistance([4,14,2]))

