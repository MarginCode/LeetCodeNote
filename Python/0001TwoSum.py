#双循环穷举
#n(O^2)时间复杂度
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        for i in range(len(nums)):
            #注意避免本位相加
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    result.extend((i,j))
        return result

#循环列表+字典检查判断
#n(O)时间复杂度
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary= {}
        for key, value in enumerate(nums):
            difference= target- value
            #检查字典中是否有差值，如果有直接返回两个索引
            if difference in dictionary:
                return [dictionary[difference], key]
            #没有就将差值加入字典，等待下一次循环
            else:
                dictionary[value]=key