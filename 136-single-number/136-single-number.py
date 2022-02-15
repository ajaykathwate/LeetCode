class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
        
        
#        c=Counter(nums)
#        for i in nums:
#            if c[i]==1:
#                return i
        
        
#        res = 0
#        for n in nums:
#            res = n ^ res
#        return res
            