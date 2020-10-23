#encoding:utf-8
#Time:2020/10/18 21:01
#Email:1215399218@qq.com
#Author:Mr.jia
#File:461汉明距离.PY
#Software:PyCharm
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
# 注意：
# 0 ≤ x, y < 231.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/hamming-distance
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a=x^y
        count=0
        while a!=0:
            a=a&(a-1)
            count+=1
        return  count

