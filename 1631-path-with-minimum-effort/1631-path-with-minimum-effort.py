import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        # Min-heap stores tuples of (current_max_effort, r, c)
        min_heap = [(0, 0, 0)]
        
        # Distance array initialized with infinity to track minimum effort to each cell
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        
        # 4-directional movements
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while min_heap:
            current_effort, r, c = heapq.heappop(min_heap)
            
            # If we reached the bottom-right cell, return the effort
            if r == rows - 1 and c == cols - 1:
                return current_effort
                
            # If we found a path with greater effort than a previously recorded one, skip it
            if current_effort > efforts[r][c]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    # New effort is the max of the current path's effort and the jump to the next cell
                    next_effort = max(current_effort, abs(heights[r][c] - heights[nr][nc]))
                    
                    # If this path yields a lower effort to (nr, nc), update and push to heap
                    if next_effort < efforts[nr][nc]:
                        efforts[nr][nc] = next_effort
                        heapq.heappush(min_heap, (next_effort, nr, nc))
                        
        return 0


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna