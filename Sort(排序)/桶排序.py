#encoding:utf-8
#Time:2020/10/23 10:01
#Email:1215399218@qq.com
#Author:Mr.jia
#File:同排序.PY
#Software:PyCharm
def bucket(nums):
    big=max(nums)
    small=min(nums)
    sum=len(nums)
    d=big-small
    list=[]
    for i in range(sum):
        list.append([])
    for i in nums:
        k=int((i-big)*(sum-1)/d)
        list[k-1].append(i)
    # for i in range(len(list)):
    #     list[i].sort()
    sort_arr=[]
    return list
    # for i in list:
    #     for j in i:
    #         sort_arr.append(j)
    # return sort_arr
nums=[21,3,4,5,2,6,1]
print(bucket(nums))





