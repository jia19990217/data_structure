#encoding:utf-8
#Time:2020/10/18 21:46
#Email:1215399218@qq.com
#Author:Mr.jia
#File:最大公约数.PY
#Software:PyCharm
# def greatest_common_divisor(a,b):
    # if a>b:
    #     s=b
    # else:
    #     s=a
    # for i in range(s+1,0,-1):
    #     if ((a%i==0) and (b%i==0)):
    #         return i
# def greatest_common_divisor(a,b):  #辗转相除法
#     big=max(a,b)
#     smail=min(a,b)
#     if big%smail==0:
#         return smail
#     return greatest_common_divisor(big%smail,smail)
def greatest_common_divisor(a,b):  #更相减损术
    if a-b==0:
        return a
    big=max(a,b)
    smail=min(a,b)
    return  greatest_common_divisor(big-smail,smail)
print(greatest_common_divisor(168,64))