class Solution:
    def titleToNumber(self, s: str) -> int:
        number = 0
        for ch  in s:
            dec = ord(ch) - ord('A') + 1
            number = dec + number*26
        return number
        
        
        
#        return sum( (ord(char) - ord('A') + 1) *  26 ** i for i, char in enumerate( reversed(s) ) )
