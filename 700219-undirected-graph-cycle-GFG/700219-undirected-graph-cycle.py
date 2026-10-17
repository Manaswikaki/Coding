class Solution:
    def isCycle(self, V: int, edges: list[list[int]]) -> bool:
        # Step 1: Build the adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Step 2: Track visited vertices
        visited = [False] * V

        # Step 3: DFS helper function
        def dfs(node, parent):
            visited[node] = True

            for neighbor in adj[node]:
                # If neighbor is not visited, recurse
                if not visited[neighbor]:
                    if dfs(neighbor, node):
                        return True
                # If neighbor is visited and not the parent, a cycle is found
                elif neighbor != parent:
                    return True

            return False

        # Step 4: Handle multiple disconnected components
        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True

        return False


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna