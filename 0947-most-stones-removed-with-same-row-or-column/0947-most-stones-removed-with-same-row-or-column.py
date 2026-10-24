class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        parent = {}
        
        def find(i):
            # Path compression
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        # Connect rows and columns
        for x, y in stones:
            # Shift y-coordinate to avoid collision with x-coordinate values
            y_encoded = ~y 
            
            if x not in parent:
                parent[x] = x
            if y_encoded not in parent:
                parent[y_encoded] = y_encoded
                
            union(x, y_encoded)
            
        # Count the number of unique connected components
        num_components = len({find(x) for x in parent})
        
        # Max stones removed = Total stones - Number of components
        return len(stones) - num_components


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna