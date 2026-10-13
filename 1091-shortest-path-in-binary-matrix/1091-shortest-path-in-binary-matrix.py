from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # Base cases: if the start or end cell is blocked, no clear path exists
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        # If the grid is 1x1 and the starting cell is 0, path length is 1
        if n == 1:
            return 1
            
        # Queue stores tuples of (row, col, current_path_length)
        queue = deque([(0, 0, 1)])
        
        # Mark the starting cell as visited by changing 0 to 1
        grid[0][0] = 1
        
        # Define all 8 possible movements (horizontal, vertical, diagonal)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        while queue:
            r, c, length = queue.popleft()
            
            # If we reached the bottom-right corner, return the path length
            if r == n - 1 and c == n - 1:
                return length
            
            # Explore all 8 adjacent neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check if the neighbor is within boundaries and is a clear cell (0)
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1  # Mark as visited in-place
                    queue.append((nr, nc, length + 1))
                    
        return -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna