class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        mask, output = 0, 0
        for k in range(32, -1,-1):
            mask = mask | 1 << k
            found = set([n & mask for n in nums])
                
            temp = output | 1 << k
            for f in found:
                if f ^ temp  in found:
                    output = temp
        return output