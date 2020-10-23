#encoding:utf-8
#Time:2020/10/19 18:21
#Email:1215399218@qq.com
#Author:Mr.jia
#File:75 最大回文子串.PY
#Software:PyCharm
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 示例 1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
# 输入: "cbbd"
# 输出: "bb"
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)-1):
            for j in range(len(s)-1,0,-1):
                if s[i]==s[j]:
                    return s[i:j+1]
# a='babad'
a='cddb'
b=Solution()
print(b.longestPalindrome(a))
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=len(s)
        if length<2:
            return s
        maxlen=1
        res=s[0]
        odd=[]
        ecen=[]
        for i in range(length-1):
            odd=self.centerSpread(s,i,i)
            even=self.centerSpread(s,i,i+1)
            maxstr=odd if len(odd)>len(even) else even
            if maxlen<len(maxstr):
                maxlen=len(maxstr)
                res=maxstr
        return res
    def centerSpread(self,s:str,left:int,right:int):
        length=len(s)
        i=left
        j=right
        while i>=0 and j<length:
            if s[i]==s[j]:
                i-=1
                j+=1
            else:
                break
        return s[i+1:j]




