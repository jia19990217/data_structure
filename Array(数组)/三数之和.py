#encoding:utf-8
#Time:2020/10/13 10:59
#Email:1215399218@qq.com
#Author:Mr.jia
#File:三数之和.PY
#Software:PyCharm
def Three_sum(nums):
    nums.sort()
    num1 = []
    for i in range(len(nums) - 2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        head = i + 1
        tail = len(nums) - 1
        while head < tail:
            sum = nums[head] + nums[tail] + nums[i]
            if sum == 0:
                num1.append([nums[i], nums[head], nums[tail]])
                while head<tail and nums[head]==nums[head+1]:
                    head+=1
                while head<tail and nums[tail]==nums[tail-1]:
                    tail-=1
                head += 1
                tail -= 1
            else:
                if sum > 0:
                    tail -= 1
                else:
                    head += 1
    return num1
nums = [-1, 0, 1, 2, -1, -4]
print(Three_sum(nums))