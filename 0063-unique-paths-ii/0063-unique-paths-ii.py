class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # 1D array to store the number of paths to each column in the current row
        dp = [0] * n
        dp[0] = 1  # Starting point
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0  # Obstacle blocks all paths to this cell
                elif j > 0:
                    dp[j] += dp[j - 1]  # Ways from top (dp[j]) + ways from left (dp[j-1])
                    
        return dp[n - 1]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna