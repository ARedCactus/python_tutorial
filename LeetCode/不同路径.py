class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*m] + [[1]+[0]*(m-1) for _ in range(n-1)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]

    def uniquePaths_2(self, m: int, n: int) -> int:
        dp = [1]*m
        for i in range(1, n):
            for j in range(1, m):
                dp[j] += dp[j-1]
        return dp[-1]

if __name__ == "__main__":
    ans = Solution().uniquePaths(3, 7)
    ans2 = Solution().uniquePaths_2(3, 7)
    print(ans, ans2)