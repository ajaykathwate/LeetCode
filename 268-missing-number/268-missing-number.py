class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n*(n+1)/2
        sum_of_a = sum(nums)
        return int(total_sum - sum_of_a)