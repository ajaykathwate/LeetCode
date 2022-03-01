class Solution:
    def arraySign(self, nums: List[int]) -> int:
        temp = 1
        
        for i in nums:
            temp *= i
        if temp == 0: return 0
        elif temp > 0: return 1
        else:
            return -1