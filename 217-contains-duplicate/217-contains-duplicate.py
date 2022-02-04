class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i, val in enumerate(nums):
            if val in dict:
                return True
            else:
                dict[val]  = i
        return False
        
        
        
#        return len(set(nums)) != len(nums) # 866ms
        
        
        
#        arr = set() #740ms
#        for i in nums:
#            if i in arr:
#                return True
#            else:
#                arr.add(i)
#       return False