#encoding:utf-8
#Time:2020/10/21 8:57
#Email:1215399218@qq.com
#Author:Mr.jia
#File:16 最接近的三数之和.PY
#Software:PyCharm
def threeSumClosest(nums,target):
    nums.sort()
    min=abs(nums[0]+nums[1]+nums[2]-target)
    res=nums[0]+nums[1]+nums[2]
    for i in range(len(nums)-2):
        left=i+1
        right=len(nums)-1
        while left<right:
            sum=nums[i]+nums[left]+nums[right]
            if abs(sum-target)<min:
                min=abs(sum-target)
                res=sum
            if sum>target:
                right-=1
            elif sum<target:
                left+=1
            else:
                return sum
    return  res
num=[1,-1,0,-9]
print(threeSumClosest(num,100))