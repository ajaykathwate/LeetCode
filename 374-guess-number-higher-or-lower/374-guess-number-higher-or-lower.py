# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #Using Binary search
        low, high = 0, n
        while low <= high:
            mid = (low + high) // 2
            res = guess(mid)
            if res > 0:
                low = mid + 1
            elif res < 0:
                high = mid -1
            else:
                return mid