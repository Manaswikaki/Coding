class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            # Base case: check boundary conditions and if the cell is water (0)
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0
            
            # Mark the current cell as visited by turning it into water (0)
            grid[r][c] = 0
            
            # Sum up the current cell plus all 4 adjacent directions
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    # Update the maximum area found so far
                    max_area = max(max_area, dfs(r, c))
                    
        return max_area


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna