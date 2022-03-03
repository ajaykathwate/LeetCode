class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0
        
        for i in range(1, n+1,2):
            for j in range(n-i+1):
                total += sum(arr[j:j+i])
        return total