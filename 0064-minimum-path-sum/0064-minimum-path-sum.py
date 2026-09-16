class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Initialize the first row (can only come from the left)
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
            
        # Initialize the first column (can only come from above)
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
            
        # Fill the rest of the dynamic programming grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                
        return grid[-1][-1]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna