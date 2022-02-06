class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        f = 2
        for i in range(2,n):
            if not(nums[i] == nums[f-1] and nums[i] == nums[f-2]):
                nums[f] = nums[i]
                f += 1
        return f