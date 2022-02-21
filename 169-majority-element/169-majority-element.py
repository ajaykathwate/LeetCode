class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
        
#        sums = {}
#        for n in nums:
#            if n not in sums:
#                sums[n] = 1
#            else:
#                sums[n] += 1
#                
#            if sums[n] > len(nums)/2:
#                return n