import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # Min-heap stores tuples of: (max_elevation_so_far, r, c)
        min_heap = [(grid[0][0], 0, 0)]
        
        # Track visited cells
        visited = {(0, 0)}
        
        # Directions for 4-way movement
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while min_heap:
            time, r, c = heapq.heappop(min_heap)
            
            # Reached the bottom-right corner
            if r == n - 1 and c == n - 1:
                return time
            
            # Check neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and if not visited
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    
                    # The time to enter the next cell is the max of the current path time 
                    # and the cell's own elevation
                    next_time = max(time, grid[nr][nc])
                    heapq.heappush(min_heap, (next_time, nr, nc))
                    
        return 0


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna