class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ways_hash = {index:[] for index in range(0, target + 1)}
        ways_hash[0] = [[]]
        
        for candidate in candidates:
            for index in range(candidate, len(ways_hash)):
                for combo in ways_hash[index - candidate]:
                    newCombo = combo + [candidate]
                    ways_hash[index].append(newCombo)

        return ways_hash[target]