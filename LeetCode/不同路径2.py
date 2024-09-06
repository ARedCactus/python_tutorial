class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [0]*m
        dp[0] = 1 if obstacleGrid[0][0]==0 else 0
        print(dp)
        for i in range(0, n):
            for j in range(0, m):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                    continue
                elif j-1>=0 and obstacleGrid[i][j-1]==0:
                    dp[j] += dp[j-1]
        return dp[-1]
    
if __name__ == "__main__":
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    ans = Solution().uniquePathsWithObstacles(obstacleGrid)
    print(ans)