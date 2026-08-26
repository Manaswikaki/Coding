import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Combine capital and profits, then sort by capital ascending
        projects = sorted(zip(capital, profits))
        
        max_heap = []
        i = 0
        n = len(projects)
        
        # Select up to k projects
        for _ in range(k):
            # Push all affordable projects into the max-heap
            while i < n and projects[i][0] <= w:
                # Python has a min-heap by default, so invert the profit to simulate a max-heap
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            
            # If no affordable projects are available, stop early
            if not max_heap:
                break
                
            # Take the project with the highest profit
            w += -heapq.heappop(max_heap)
            
        return w


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna