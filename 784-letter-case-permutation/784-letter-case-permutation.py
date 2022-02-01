class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        
        def recursion(ip, op=''):
            if not ip:
                res.append(op)
                return
            
            cur = ip[0]
            if cur.isalpha():
                recursion(ip[1:], op + cur.lower())
                recursion(ip[1:], op + cur.upper())
            else:
                recursion(ip[1:], op + cur)
            
        recursion(s)
        return res