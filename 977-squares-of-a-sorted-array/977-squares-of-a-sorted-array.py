class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        low = 0
        high = len(nums) - 1
        while low <= high:
            if nums[low] * nums[low] > nums[high] * nums[high]:
                arr.append(nums[low] * nums[low])
                low += 1
            else:
                arr.append(nums[high] * nums[high])
                high -= 1
                
        return reversed(arr)