#暴力解法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        templist=[]
        total=[]
        for i in s:
            if not i in templist: 
                templist.append(i)
                total.append(len(templist))
            else:
                total.append(len(templist))
                print
                templist=list(templist[-1])
        if total==[]: return len(templist)
        return max(total)
