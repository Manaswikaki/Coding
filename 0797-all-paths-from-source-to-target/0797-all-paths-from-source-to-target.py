class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        results = []
        
        def dfs(node, path):
            # If we reach the target node, save the current path
            if node == target:
                results.append(list(path))
                return
            
            # Explore all neighbors of the current node
            for neighbor in graph[node]:
                path.append(neighbor)  # Choose
                dfs(neighbor, path)    # Explore
                path.pop()             # Unchoose (backtrack)
                
        # Start DFS from the source node (0) with the initial path [0]
        dfs(0, [0])
        return results


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna