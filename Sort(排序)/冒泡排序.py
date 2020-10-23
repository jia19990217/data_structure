#encoding:utf-8
#Time:2020/10/19 15:20
#Email:1215399218@qq.com
#Author:Mr.jia
#File:冒泡排序.PY
#Software:PyCharm
from sort import randomList
def bubble(nums):
    count=0
    for i  in range(1,len(nums)):
        fl=True
        for j in range(len(nums)-i):

            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                # fl=False
                count += 1
                print('第%s轮排序结果'%(count),nums)
        # if fl:
        #     break
    return nums
nums=[13, 26, 100, 88]
# nums=randomList.randomL(10)
print(bubble(nums))