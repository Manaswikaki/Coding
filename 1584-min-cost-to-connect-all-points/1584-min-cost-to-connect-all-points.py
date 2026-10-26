import collections

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n == 0:
            return 0
            
        # Track the minimum distance from the MST to each point
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        visited = [False] * n
        
        total_cost = 0
        
        for _ in range(n):
            # 1. Find the unvisited node with the minimum distance to the MST
            curr_node = -1
            curr_dist = float('inf')
            
            for i in range(n):
                if not visited[i] and min_dist[i] < curr_dist:
                    curr_dist = min_dist[i]
                    curr_node = i
            
            # Add the chosen node's edge weight to our total cost
            visited[curr_node] = True
            total_cost += curr_dist
            
            # 2. Update distances from the newly added node to all other unvisited nodes
            x1, y1 = points[curr_node]
            for next_node in range(n):
                if not visited[next_node]:
                    x2, y2 = points[next_node]
                    # Calculate Manhattan distance
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    if dist < min_dist[next_node]:
                        min_dist[next_node] = dist
                        
        return total_cost


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna