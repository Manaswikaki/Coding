class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        # A connected graph with n nodes requires at least n - 1 edges
        if len(connections) < n - 1:
            return -1
        
        # Initialize parent array for Union-Find
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])  # Path compression
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False

        # Count how many components are merged
        components = n
        for u, v in connections:
            if union(u, v):
                components -= 1
                
        return components - 1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna