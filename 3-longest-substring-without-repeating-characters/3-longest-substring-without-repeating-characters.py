class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        start = 0
        
        res = 0
        for i in range(len(s)):
            while s[i] in charset:
                charset.remove(s[start])
                start += 1
            charset.add(s[i])
            res = max(res, i-start+1)
        return res