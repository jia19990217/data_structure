#encoding:utf-8
#Time:2020/10/13 17:15
#Email:1215399218@qq.com
#Author:Mr.jia
#File:合并两个有序数组.PY
#Software:PyCharm
from typing import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i=m-1
    j=n-1
    k=m+n-1
    while i>=0 and j>=0:
        if nums1[i]>nums2[j]:
            nums1[k]=nums1[i]
            i-=1
        else:
            nums1[k]=nums2[j]
            j-=1
        k-=1
    while i>=0:
        nums1[k]=nums1[i]
        k-=1
        i-=1
    while j >= 0:
        nums1[k] = nums1[j]
        k -= 1
        j -= 1
    return nums1

nums1 = [0]
m = 3
nums2 = [1]
n = 3
print(merge(nums1,m,nums2,n))