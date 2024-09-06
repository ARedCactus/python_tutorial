class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = grid
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i==j==0:
                    continue
                elif i==0:
                    dp[i][j] += dp[i][j-1]
                elif j==0:
                    dp[i][j] += dp[i-1][j]
                else:
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
if __name__ == "__main__":
    grid: list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    ans = Solution().minPathSum(grid)
    print(ans)

        