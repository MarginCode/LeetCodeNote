#暴力解法
#生成所有子字符串，筛掉重复子字符串，
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        #防止单字符进入循环
        if len(s)==1: return s
        max_size=[]
        for i in range(len(s)):
            #注意避免本位和增加最后一位
            for j in range(i+1,len(s)+1):
                x,y=i,j
                print(s[x:y])
                while(x<y):
                    if s[x]!=s[y-1]:
                        break
                    x=x+1
                    y=y-1
                if x-y==1 or y-x==1:
                    if len(max_size)<len(s[x:y]): max_size=s[x:y]
        return max(max_size)