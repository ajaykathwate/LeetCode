class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        result =  0
        while True:
            if target <= startValue:
                result = result + startValue - target
                break
            if target % 2 == 0:
                target = target // 2
                result += 1
            else:
                target += 1
                result += 1
        return result