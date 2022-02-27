class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_ = 0
        mul_ = 1
        for i in str(n):
            sum_ += int(i)
            mul_ *= int(i)
        return mul_ - sum_