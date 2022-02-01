class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        #eturn n & (-n) == n
        while n %2 == 0:
            n /= 2
        return n==1