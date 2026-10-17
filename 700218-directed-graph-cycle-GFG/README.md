# [Directed Graph Cycle](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1)
## Medium
Given a directed graph with V vertices numbered from 0 to V - 1 and E directed edges. The graph is represented using a 2D array edges[][] of size E, where each entry edges[i] = [u, v] denotes a directed edge from vertex u to vertex v.Check whether the graph contains any cycle. Return true if there exists at least one cycle in the graph; otherwise, return false.Examples:Input: V = 4, edges[][] = [[0, 1], [1, 2], [2, 0], [2, 3]]



Output: true
Explanation: The diagram clearly shows a cycle 0 -&gt; 1 -&gt; 2 -&gt; 0Input: V = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
Output: false
Explanation: no cycle in the graphConstraints:1 ≤ V ≤ 1050 ≤ E ≤ 1050 ≤ edges[i][0], edges[i][1] &lt; V