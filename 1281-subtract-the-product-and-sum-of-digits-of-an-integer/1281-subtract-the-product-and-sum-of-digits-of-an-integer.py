class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return (lambda n: prod(n) - sum(n))(list(map(int,str(n))))
