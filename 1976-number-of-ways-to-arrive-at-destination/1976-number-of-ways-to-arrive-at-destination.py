import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD = 10**9 + 7
        
        # Build adjacency list
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
            
        # dist[i] stores the minimum time to reach node i
        dist = [float('inf')] * n
        # ways[i] stores the number of ways to reach node i in min time
        ways = [0] * n
        
        dist[0] = 0
        ways[0] = 1
        
        # Min-heap stores (current_time, node)
        min_heap = [(0, 0)]
        
        while min_heap:
            curr_time, u = heapq.heappop(min_heap)
            
            if curr_time > dist[u]:
                continue
                
            for v, time in graph[u]:
                if curr_time + time < dist[v]:
                    dist[v] = curr_time + time
                    ways[v] = ways[u]
                    heapq.heappush(min_heap, (dist[v], v))
                elif curr_time + time == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
                    
        return ways[n - 1] % MOD


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna