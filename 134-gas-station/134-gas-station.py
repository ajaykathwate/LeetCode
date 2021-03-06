class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        tank = 0
        shortage = 0
        
        for i in range(len(gas)):
            tank += gas[i]
            if tank >= cost[i]:
                tank -= cost[i]
            else:
                shortage += cost[i] - tank
                start = i + 1
                tank = 0
        if start == len(gas) or tank < shortage:
            return -1
        return start