class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #行数小于2直接返回
        if numRows < 2: return s
        #生成与指定行数相同的元素个数的list(内部为")
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            #将c的值第i项
            res[i] += c
            #判断是否第一行或者最后一行，如果到最后一行，将游标反转
            if i == 0 or i == numRows - 1: flag = -flag
            #更新游标值给i
            i += flag
        return "".join(res)