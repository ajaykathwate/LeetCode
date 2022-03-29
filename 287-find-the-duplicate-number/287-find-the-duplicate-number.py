class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < mid + 1:
                high = mid - 1
            else:
                low = mid + 1
        return low