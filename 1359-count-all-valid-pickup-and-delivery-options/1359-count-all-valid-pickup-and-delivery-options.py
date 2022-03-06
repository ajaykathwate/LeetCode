class Solution:
    def countOrders(self, n: int) -> int:
        
        
        ans = 1
        
        for i in range(2, n + 1):
            ans = math.floor((ans * ((((i - 1) * 2 + 1) + 1) * ((i - 1) * 2 + 1) / 2)) % (10 ** 9 + 7))
        return ans