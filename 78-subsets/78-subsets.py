class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        return ([[nums[k] for k in range(n) if i&1<<k] for i in range(2**n)])