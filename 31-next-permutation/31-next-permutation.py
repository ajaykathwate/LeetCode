class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                for j in range(i, len(nums)):
                    if j+1 == len(nums) or nums[j+1] <= nums[i-1]:
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        nums[i:] = nums[:i-1:-1]
                        return
        nums[:] = nums[::-1]