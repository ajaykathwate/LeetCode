class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        nums.append(float("inf"))
        results = []
        start = nums[0]
        last = nums[0]
        
        for x in nums[1:]:
            if x != last + 1:
                if start == last:
                    results.append(str(start))
                else:
                    results.append(f"{start}->{last}")
                    
                start = x
                last = x
            else:
                last = x
                
        return results