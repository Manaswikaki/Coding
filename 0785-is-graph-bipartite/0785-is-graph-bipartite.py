class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = {}  # Stores the color (0 or 1) assigned to each node
        
        # Loop through all nodes to handle disconnected graphs
        for i in range(n):
            if i not in color:
                # Start a BFS traversal for the unvisited component
                queue = [i]
                color[i] = 0
                
                while queue:
                    node = queue.pop(0)
                    
                    for neighbor in graph[node]:
                        if neighbor not in color:
                            # Assign the opposite color to the neighbor
                            color[neighbor] = 1 - color[node]
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            # A conflict is found (adjacent nodes have the same color)
                            return False
                            
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna