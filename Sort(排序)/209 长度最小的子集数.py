#encoding:utf-8
#Time:2020/10/21 8:58
#Email:1215399218@qq.com
#Author:Mr.jia
#File:209 长度最小的子集数.PY
#Software:PyCharm
def samil(nums,s):
    n=len(nums)
    left,right,sum,res=0,0,0,n+1
    while right<n:
        sum+=nums[right]
        while sum>=s:
            res=min(res,right-left+1)
            sum-=nums[left]
            left+=1
        right+=1
    return 0 if res==n+1 else res
