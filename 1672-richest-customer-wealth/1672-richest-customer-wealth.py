class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        #maxwelth = [maxwelth  for i in accounts   if sum(i) > maxwelth]
        max_ = 0
        for i in accounts:
            if sum(i) > max_:
                max_  = sum(i)
        return max_