class Solution:
    
    def maxProfit(self, arr: List[int]) -> int:
        start = 0
        end = 1
        maxProfit = 0
        while end < len(arr):
            if arr[start] < arr[end]:
                profit  = arr[end] - arr[start]
                maxProfit = max(maxProfit, profit)
            else:
                start = end
            end += 1
        return maxProfit