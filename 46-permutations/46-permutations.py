class Solution:
    def __init__(self):
        self.permutations = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, [])
        return self.permutations
    def backtrack(self, nums, path):
        if not nums:
            self.permutations.append(path)
        for iterator in range(len(nums)):
            self.backtrack(nums[:iterator] + nums[iterator+1:], path + [nums[iterator]])