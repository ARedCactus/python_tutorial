class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[n]

    def minCostClimbingStairs_滚动数组(self, cost: list[int]) -> int:
        n = len(cost)
        a, b, c = 0, 0, 0
        for i in range(2, n+1):
            c = min(a+cost[i-2], b+cost[i-1])
            a, b = b, c
        return c