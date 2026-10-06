class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            # Base case: if out of bounds or it's water ('0'), stop exploring
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            
            # Mark the current land cell as visited by changing it to '0'
            grid[r][c] = '0'
            
            # Visit all 4 adjacent directions (up, down, left, right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        # Iterate through every cell in the 2D grid
        for r in range(rows):
            for c in range(cols):
                # When a new piece of land is found, it triggers a new island discovery
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c) # Sink the entire island using DFS
                    
        return island_count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna