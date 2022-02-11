#暴力解法
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #合并列表后排序
        x = nums1+nums2
        x.sort()
        #判断列表元素个数的奇偶性，分别返回中位数
        if len(x)%2==0:
            return (x[int(len(x)/2)]+x[int((len(x)/2)-1)])/2                      
        else:
            return x[int((len(x)-1)/2)] 