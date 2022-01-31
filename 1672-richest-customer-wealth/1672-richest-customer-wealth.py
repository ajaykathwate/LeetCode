class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwelth = 0
                
        for i in accounts:
            if sum(i) > maxwelth:
                maxwelth = sum(i)
        return maxwelth