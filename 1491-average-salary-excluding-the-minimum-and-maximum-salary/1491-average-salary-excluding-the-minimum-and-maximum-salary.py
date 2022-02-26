class Solution:
    def average(self, salary: List[int]) -> float:
        total_sal = sum(salary) - min(salary) - max(salary)
        res = total_sal / (len(salary)-2)
        return res