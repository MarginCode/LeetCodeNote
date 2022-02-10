#暴力解法
#生成所有子字符串，筛掉重复子字符串，
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        #防止单字符进入循环
        if len(s)==1: return 1
        max_size=0
        for i in range(len(s)):
            #注意避免本位和增加最后一位
            for j in range(i+1,len(s)+1):
                templist=(s[i:j])
                if len(templist)!=len(set(templist)):
                   break
                if max_size<len(templist): max_size=len(templist)        
        return max_size