from collections import deque
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_sizes = {}
        island_id = 2
        
        # Step 1: Assign a unique ID and calculate the size for each island
        def get_island_size(r, c, idx):
            queue = deque([(r, c)])
            grid[r][c] = idx
            size = 1
            while queue:
                curr_r, curr_c = queue.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = idx
                        queue.append((nr, nc))
                        size += 1
            return size

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[island_id] = get_island_size(r, c, island_id)
                    island_id += 1
        
        # If the grid is already all 1s
        max_island = max(island_sizes.values(), default=0)
        
        # Step 2: Check every '0' cell and see what happens if we flip it to '1'
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    neighbor_ids = set()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            neighbor_ids.add(grid[nr][nc])
                    
                    potential_size = 1 + sum(island_sizes[id_] for id_ in neighbor_ids)
                    max_island = max(max_island, potential_size)
                    
        return max_island


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna