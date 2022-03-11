class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=list(str(x))
        symbol=True
        for i in range(len(x)//2):
            if x[i]!=x[-(i+1)]:
                symbol=False
                break
        for i in x:
            if i=="-":
                symbol=False
        return symbol