#encoding:utf-8
#Time:2020/10/13 10:10
#Email:1215399218@qq.com
#Author:Mr.jia
#File:两数之和(返回值).PY
#Software:PyCharm
# def Two_sum(nums,target):
#     head=0
#     tail=len(nums)-1
#     while head<tail:
#         sum=nums[head]+nums[tail]
#         if sum==target:
#             print(nums[head],nums[tail]) #返回的值不是索引
#             head+=1
#             tail-=1
#         else:
#             if sum>target:
#                 tail-=1
#             else:
#                 head+=1
# def Two_sum(nums,target):
#     dict={}
#     for i in range(len(nums)):
#         temp=target-nums[i]
#         if temp in dict:
#             return  [i,dict[temp]]
#         else:
#             dict[nums[i]]=i
# def Two_sum(nums,target):
#     for i in range(len(nums)-1):
#         for j in range(1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 return [i,j]
def Two_sum(nums,target):
    for i in range(len(nums)):
        for j in nums[i+1:]:
            if nums[i]+j==target:
                return [nums[i],j]  #返回的值不是索引
a=[1,2,3,4,5,6,7]
print(Two_sum(a,9))

