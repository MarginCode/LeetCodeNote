#暴力解法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxl,max_len,n = 0,0,len(s)
        for i in range(2*n-1):
            l,r = i//2,i//2+i%2
            while l>=0 and r < n and s[l]==s[r]:
                if r-l+1>max_len: maxl,max_len = l,r-l+1
                l-=1
                r+=1
        return s[maxl:maxl+max_len]