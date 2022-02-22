class Solution:
    def titleToNumber(self, s: str) -> int:
        return sum( (ord(char) - ord('A') + 1) *  26 ** i for i, char in enumerate( reversed(s) ) )
