class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boatCount = 0
        low = 0
        high=  len(people)-1
        while low <= high:
            if people[low] + people[high] > limit:
                boatCount += 1
                high -= 1
            else:
                boatCount += 1
                high -= 1
                low += 1
        return boatCount