class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        dp = defaultdict(int)
        ans = 0
        mod = 10**9+7
        for i in range(2, len(arr)):
            for j in range(i-1):
                dp[arr[j] + arr[i-1]] += 1
            ans += dp[target - arr[i]]
            ans %= mod
        return ans