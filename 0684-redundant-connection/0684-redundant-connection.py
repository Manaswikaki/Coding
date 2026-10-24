class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # There are n nodes and n edges, numbered from 1 to n
        n = len(edges)
        parent = list(range(n + 1))
        rank = [1] * (n + 1)
        
        def find(node):
            # Path compression: point node directly to its ultimate root
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
            
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            
            # If they share the same root, a cycle is detected
            if root1 == root2:
                return False
                
            # Union by rank: attach the smaller tree under the larger tree
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna