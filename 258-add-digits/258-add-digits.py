class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        else:
            while len(str(num)) != 1:
                x = str(num)
                val = 0
                for i in x:
                    val += int(i)
                num = val
        s = Solution()
        return s.addDigits(num)
            
            
                