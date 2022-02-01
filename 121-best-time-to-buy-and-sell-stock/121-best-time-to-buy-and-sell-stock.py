class Solution:
    
    def maxProfit(self, arr: List[int]) -> int:
        n = len(arr)
        max_, cur = 0,0
        for i in range(1,n):
            cur = max(cur + arr[i]-arr[i-1], 0)
            max_ = max(max_, cur)
        return max_
        
        
        
        
        # Another solution
        #start = 0
        #end = 1
        #maxProfit = 0
        #while end < len(arr):
            #if arr[start] < arr[end]:
                #profit  = arr[end] - arr[start]
                #maxProfit = max(maxProfit, profit)
            #else:
                #start = end
            #end += 1
        #return maxProfit