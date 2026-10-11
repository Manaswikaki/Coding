class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
            
        ROWS, COLS = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()
        
        def dfs(r, c, visited, prev_height):
            # Check boundaries, if already visited, or if the water cannot flow uphill
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                (r, c) in visited or heights[r][c] < prev_height):
                return
                
            visited.add((r, c))
            
            # Traverse all 4 neighboring directions
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # 1. Start DFS from the top and bottom rows
        for c in range(COLS):
            dfs(0, c, pacific_visited, heights[0][c])        # Top row (Pacific)
            dfs(ROWS - 1, c, atlantic_visited, heights[ROWS - 1][c])  # Bottom row (Atlantic)
            
        # 2. Start DFS from the left and right columns
        for r in range(ROWS):
            dfs(r, 0, pacific_visited, heights[r][0])        # Left col (Pacific)
            dfs(r, COLS - 1, atlantic_visited, heights[r][COLS - 1])  # Right col (Atlantic)
            
        # 3. Find the intersection of cells reachable by both oceans
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    result.append([r, c])
                    
        return result


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna