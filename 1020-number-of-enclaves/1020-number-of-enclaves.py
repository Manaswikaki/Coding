class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(r: int, c: int):
            # Base case: Out of bounds or already a water/visited cell
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return
            
            # Mark as visited by converting land to water
            grid[r][c] = 0
            
            # Explore 4-directional neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        # Step 1 & 2: Run DFS from the left and right boundaries
        for r in range(m):
            if grid[r][0] == 1:
                dfs(r, 0)
            if grid[r][n - 1] == 1:
                dfs(r, n - 1)
                
        # Run DFS from the top and bottom boundaries
        for c in range(n):
            if grid[0][c] == 1:
                dfs(0, c)
            if grid[m - 1][c] == 1:
                dfs(m - 1, c)
                
        # Step 3: Sum up the remaining land cells that couldn't reach any boundary
        return sum(sum(row) for row in grid)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna