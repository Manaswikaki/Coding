from collections import deque

class Solution:
    def isCyclic(self, V: int, edges: list[list[int]]) -> bool:
        # Step 1: Build the adjacency list and calculate in-degrees
        adj = [[] for _ in range(V)]
        in_degree = [0] * V

        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1

        # Step 2: Push all vertices with an in-degree of 0 to the queue
        queue = deque([i for i in range(V) if in_degree[i] == 0])

        visited_count = 0

        # Step 3: Process the graph using BFS
        while queue:
            u = queue.popleft()
            visited_count += 1

            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        # Step 4: If visited_count matches V, there is no cycle
        return visited_count != V


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna