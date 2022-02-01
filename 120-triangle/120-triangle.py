class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j>0 and j<len(triangle[i])-1:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
                elif j==0:
                    triangle[i][0] += triangle[i-1][j]
                else:
                    triangle[i][j] += triangle[i-1][j-1]
        return min(triangle[-1])