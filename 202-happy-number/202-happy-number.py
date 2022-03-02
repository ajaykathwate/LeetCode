class Solution:
    def isHappy(self, n: int) -> bool:
    
        def rec_magic(n):
            if n==1:
                return True
            else: 	 
                result = 0
                for iter in str(n):
                    result = result + int(iter)**2
                if result in listt:
                    return False
                else:
                    listt.append(result)
                    return rec_magic(result)
            
        listt = []         
        return rec_magic(n)