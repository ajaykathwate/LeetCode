class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        add = 0
        for i in nums:
            add += i
            if add >= total:
                total = add
            elif add < 0:
                add = 0
        if total == 0:
            return max(nums)
        return total