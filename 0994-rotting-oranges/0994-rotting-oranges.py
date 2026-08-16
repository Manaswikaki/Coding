from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_oranges = 0
        minutes = 0
        
        # Step 1: Initialize queue with all initially rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
                    
        # If there are no fresh oranges to begin with, 0 minutes are needed
        if fresh_oranges == 0:
            return 0
            
        # Step 2: Multi-source BFS tracking levels (minutes)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
        
        while queue and fresh_oranges > 0:
            minutes += 1
            # Process all currently rotten oranges at this specific minute
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # If neighbor is valid and is a fresh orange, rot it
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        queue.append((nr, nc))
                        
        # Step 3: Check if any fresh oranges remain trapped
        return minutes if fresh_oranges == 0 else -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna