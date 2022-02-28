class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def manhattanDistance(x1,y1):
            return abs(x-x1)+abs(y-y1)
        def distanceIndex(i):
            return (manhattanDistance(*points[i]), i)
        def hasSameCoord(x1, y1):
            return x == x1 or y == y1
        res = min([distanceIndex(i) for i in range(len(points)) if hasSameCoord(*points[i])], default=None)
        return -1 if res is None else res[1]
