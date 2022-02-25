class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        #把值拆成列表
        x=list(str(x))
        result=[]
        #列表反转
        for i in range(len(x)-1,-1,-1):
            result.append(x[i])
        #负数处理
        if result[-1]=='-':
            result.pop()
            result.insert(0,'-')
        result=int(''.join(result))
        #判断结果是否超过int32范围
        if result>INT_MAX or result<INT_MIN:
            result=0
        print(result)        
        return result
