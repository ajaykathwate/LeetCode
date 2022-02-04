class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        
        
        
#        arr = set()
#        for i in nums:
#            if i in arr:
#                return True
#            else:
#                arr.add(i)
#       return False