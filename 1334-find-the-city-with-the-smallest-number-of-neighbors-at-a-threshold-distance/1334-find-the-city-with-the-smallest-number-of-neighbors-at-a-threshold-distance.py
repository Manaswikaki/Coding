class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix with infinity
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Distance from a city to itself is 0
        for i in range(n):
            dist[i][i] = 0
            
        # Populate the matrix with initial edge weights
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
            
        # Floyd-Warshall algorithm to find all-pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        # Find the city with the smallest number of reachable neighbors within the threshold
        min_neighbors = float('inf')
        best_city = -1
        
        for i in range(n):
            # Count how many neighbors are within the distanceThreshold
            reachable_count = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
            
            # Update best_city if we find a smaller neighbor count, 
            # or an equal count but with a larger city ID (i >= best_city condition via sequential loop)
            if reachable_count <= min_neighbors:
                min_neighbors = reachable_count
                best_city = i
                
        return best_city


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna