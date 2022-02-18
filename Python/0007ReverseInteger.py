class Solution:
    def reverse(self, x: int) -> int:
        x=list(str(x))
        result=[]
        for i in range(len(x)-1,-1,-1):
            result.append(x[i])
        if result[-1]=='-':
            result.pop()
            result.insert(0,'-')
        print(result)
        
        return int(''.join(result))
