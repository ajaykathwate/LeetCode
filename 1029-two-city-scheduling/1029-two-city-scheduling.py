class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
		# sorting using key
        costs.sort(key=lambda x: x[0]-x[1])

		# returning sum(first half to city a) + sum(second half to city b)
        return sum(costs[i][0] for i in range(len(costs)//2)) + \
					sum(costs[i][1] for i in range(len(costs)//2,len(costs)))