class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapify(stones) 
        while len(stones)>= 2:
            y = heappop(stones) * -1
            x = heappop(stones) * -1
            heappush(stones, 0 if x == y else (y-x) * -1)
        return heappop(stones) * -1