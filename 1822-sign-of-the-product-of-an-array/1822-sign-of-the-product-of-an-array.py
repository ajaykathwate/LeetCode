import math
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        temp = math.prod(nums)
        
        if temp == 0: return 0
        elif temp > 0: return 1
        else:
            return -1