class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s:
            return True
        
        if not t:
            return False
        
        z = []
        a = 0
        for x in range(len(t)):
            if t[x] == s[a]:
                z.append(1)
                if a == len(s)-1:
                    break
                else:
                    a += 1
            else:
                continue

        return len(s) == len(z)